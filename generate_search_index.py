#!/usr/bin/env python3
"""
Generate global search index for fuzzy search.
Creates a JSON index of all searchable content.
"""

import os
import re
import json
from pathlib import Path

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def clean_markdown(content):
    """Remove markdown syntax and extract plain text."""
    # Remove frontmatter
    content = re.sub(r'^---[\s\S]*?---\n', '', content, count=1)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', ' ', content)
    
    # Remove markdown links [text](url)
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove images
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', content)
    
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove headers markers
    content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)
    
    # Remove emphasis
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
    content = re.sub(r'\*([^*]+)\*', r'\1', content)
    content = re.sub(r'_([^_]+)_', r'\1', content)
    
    # Remove list markers
    content = re.sub(r'^[\s]*[-*+]\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^[\s]*\d+\.\s+', '', content, flags=re.MULTILINE)
    
    # Collapse whitespace
    content = re.sub(r'\s+', ' ', content)
    
    return content.strip()

def extract_keywords(text, max_keywords=20):
    """Extract important keywords from text."""
    # Remove common words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
        'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me',
        'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their'
    }
    
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    unique_words = [w for w in words if w not in stop_words]
    
    # Count frequency
    freq = {}
    for word in unique_words:
        freq[word] = freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:max_keywords]]

def build_search_index():
    """Build comprehensive search index."""
    base_dir = Path(__file__).parent
    index = {
        'wiki': [],
        'papers': [],
        'topics': [],
        'concepts': [],
        'pages': []
    }
    
    # Wiki terms (from wiki.md)
    wiki_file = base_dir / 'public' / 'wiki.md'
    if wiki_file.exists():
        wiki_content = wiki_file.read_text(encoding='utf-8')
        
        # Extract wiki terms from JavaScript
        terms_match = re.search(r'const wikiTerms = \{(.*?)\};', wiki_content, re.DOTALL)
        if terms_match:
            terms_block = terms_match.group(1)
            
            # Parse each term
            term_blocks = re.findall(r"'([^']+)':\s*\{([^}]+)\}", terms_block)
            for term_id, term_data in term_blocks:
                name_match = re.search(r"name:\s*'([^']+)'", term_data)
                def_match = re.search(r"definition:\s*'([^']+)'", term_data)
                cat_match = re.search(r"category:\s*'([^']+)'", term_data)
                
                if name_match and def_match:
                    name = name_match.group(1)
                    definition = def_match.group(1)
                    category = cat_match.group(1) if cat_match else 'general'
                    
                    index['wiki'].append({
                        'id': term_id,
                        'title': name,
                        'definition': definition,
                        'category': category,
                        'url': 'wiki.html',
                        'keywords': extract_keywords(f"{name} {definition}")
                    })
    
    # Papers
    papers_dir = base_dir / 'public' / 'papers'
    if papers_dir.exists():
        for paper_file in papers_dir.rglob('*.md'):
            if paper_file.name == 'index.md':
                continue
            
            content = paper_file.read_text(encoding='utf-8')
            
            # Papers use # Title format, not YAML frontmatter
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            
            # Extract arxiv_id from data-arxiv-id attribute
            arxiv_match = re.search(r'data-arxiv-id="([^"]+)"', content)
            
            # Extract abstract - look for "Abstract" section or the paragraph after metadata
            abstract = ''
            # Try to find abstract in a labeled section
            abstract_match = re.search(r'##?\s*Abstract\s*\n+(.+?)(?:\n##|\n<div|\Z)', content, re.DOTALL | re.IGNORECASE)
            if abstract_match:
                abstract = clean_markdown(abstract_match.group(1))[:300]
            else:
                # Fallback: take text after the paper-actions div
                after_actions = re.search(r'</style>\s*\n+(.+?)(?:\n##|\n<div|\Z)', content, re.DOTALL)
                if after_actions:
                    abstract = clean_markdown(after_actions.group(1))[:300]
            
            # Extract topics from the file path or content
            topics = []
            topic_match = re.search(r'topics.*?:\s*\[([^\]]+)\]', content)
            if topic_match:
                topics = [t.strip().strip('"\'') for t in topic_match.group(1).split(',')]
            
            # Infer topic from directory name
            dir_name = paper_file.parent.name
            if 'ai-agent' in dir_name or 'agent' in paper_file.name.lower():
                topics.append('ai-agents')
            
            if title_match:
                title = title_match.group(1).strip()
                arxiv_id = arxiv_match.group(1) if arxiv_match else ''
                
                # Extract authors from "By ..." line or meta section
                authors = ''
                authors_match = re.search(r'(?:By|Authors?:)\s*(.+?)(?:\n|$)', content, re.IGNORECASE)
                if authors_match:
                    authors = authors_match.group(1).strip()[:100]
                
                # Build relative path
                rel_path = paper_file.relative_to(base_dir)
                html_path = str(rel_path).replace('.md', '.html')
                
                index['papers'].append({
                    'title': title,
                    'authors': authors,
                    'abstract': abstract,
                    'arxiv_id': arxiv_id,
                    'topics': topics,
                    'url': html_path,
                    'keywords': extract_keywords(f"{title} {abstract}")
                })
    
    # Topics (from public/topics/)
    topics_dir = base_dir / 'public' / 'topics'
    if topics_dir.exists():
        for topic_file in topics_dir.glob('*.qmd'):
            content = topic_file.read_text(encoding='utf-8')
            
            # Topics use # Title format
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if not title_match:
                # Fallback to YAML frontmatter
                title_match = re.search(r'title:\s*"([^"]+)"', content)
            
            if title_match:
                title = title_match.group(1).strip()
                
                # Clean content for keywords
                clean_content = clean_markdown(content)
                
                rel_path = topic_file.relative_to(base_dir)
                html_path = str(rel_path).replace('.qmd', '.html')
                
                index['topics'].append({
                    'title': title,
                    'url': html_path,
                    'content': clean_content[:500],  # First 500 chars
                    'keywords': extract_keywords(f"{title} {clean_content}")
                })
    
    # Concepts (from public/concepts/)
    concepts_dir = base_dir / 'public' / 'concepts'
    if concepts_dir.exists():
        for concept_file in concepts_dir.glob('*.md'):
            content = concept_file.read_text(encoding='utf-8')
            
            # Extract title
            title_match = re.search(r'title:\s*"([^"]+)"', content)
            if title_match:
                title = title_match.group(1)
                
                clean_content = clean_markdown(content)
                
                rel_path = concept_file.relative_to(base_dir)
                html_path = str(rel_path).replace('.md', '.html')
                
                index['concepts'].append({
                    'title': title,
                    'url': html_path,
                    'content': clean_content[:500],
                    'keywords': extract_keywords(f"{title} {clean_content}")
                })
    
    # Other pages
    page_files = [
        ('public/dashboard.md', 'Dashboard'),
        ('public/researcher-hub.md', 'Researcher Hub'),
        ('public/admin-hub.md', 'Admin Hub'),
        ('public/engineer-hub.md', 'Engineer Hub'),
        ('public/reading-list.md', 'Reading List'),
        ('public/search-papers.md', 'Search Papers'),
        ('public/notes.md', 'My Notes'),
        ('public/compare-papers.md', 'Compare Papers'),
        ('public/statistics.md', 'Statistics'),
        ('public/authors.md', 'Authors'),
        ('public/tag-cloud.md', 'Tag Cloud'),
        ('public/wiki-graph.md', 'Knowledge Graph'),
        ('public/concept-explorer.qmd', 'Concept Explorer'),
        ('public/learning-paths.md', 'Learning Paths'),
        ('public/must-read-papers.md', 'Must-Read Papers'),
        ('public/research-workflow.md', 'Research Workflow'),
    ]
    
    for filename, title in page_files:
        filepath = base_dir / filename
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            clean_content = clean_markdown(content)
            
            html_path = filename.replace('.md', '.html').replace('.qmd', '.html')
            
            index['pages'].append({
                'title': title,
                'url': html_path,
                'content': clean_content[:300],
                'keywords': extract_keywords(f"{title} {clean_content}")
            })
    
    return index

def main():
    """Main function."""
    print("Building search index...")
    index = build_search_index()
    
    # Print stats
    print(f"\n{'='*60}")
    print(f"Search Index Statistics:")
    print(f"  Wiki terms: {len(index['wiki'])}")
    print(f"  Papers: {len(index['papers'])}")
    print(f"  Topics: {len(index['topics'])}")
    print(f"  Concepts: {len(index['concepts'])}")
    print(f"  Pages: {len(index['pages'])}")
    print(f"  Total: {sum(len(v) for v in index.values())}")
    print(f"{'='*60}\n")
    
    # Save index
    output_file = Path(__file__).parent / 'search-index.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Search index saved to: {output_file}")
    
    # Also create a JavaScript version for embedding
    js_file = Path(__file__).parent / '_includes' / 'search-index.js'
    js_file.parent.mkdir(exist_ok=True)
    
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write('// Auto-generated search index\n')
        f.write('const SEARCH_INDEX = ')
        json.dump(index, f, indent=2, ensure_ascii=False)
        f.write(';\n')
    
    print(f"✓ JavaScript index saved to: {js_file}")

if __name__ == '__main__':
    main()
