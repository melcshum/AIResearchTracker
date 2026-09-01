#!/usr/bin/env python3
"""
Fetch latest papers from arXiv in focus areas.
Searches for papers on AI agents, LLM reasoning, RAG, and multi-modal systems.
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import re
from pathlib import Path
import time

# Focus areas and search queries
FOCUS_AREAS = {
    'ai-agents': [
        'AI agent autonomous',
        'LLM agent tool use',
        'multi-agent systems',
        'agentic AI planning',
        'GUI agent reinforcement learning'
    ],
    'llm-reasoning': [
        'chain of thought reasoning',
        'LLM reasoning verification',
        'large language model reasoning',
        'reasoning efficiency tokens',
        'self-consistency reasoning'
    ],
    'rag-retrieval': [
        'retrieval augmented generation',
        'RAG knowledge graphs',
        'dense retrieval embeddings',
        'hybrid search retrieval',
        'retrieval augmented LLM'
    ],
    'multi-modal': [
        'vision language model',
        'multimodal LLM',
        'image text understanding',
        'multimodal reasoning',
        'document understanding OCR'
    ]
}

def search_arxiv(query, max_results=10, days_back=7):
    """Search arXiv for papers matching query, restricted to CS categories."""
    base_url = 'http://export.arxiv.org/api/query'
    
    # Restrict to CS categories relevant to our focus areas
    category_filter = '(cat:cs.AI OR cat:cs.CL OR cat:cs.CV OR cat:cs.LG OR cat:cs.MA OR cat:cs.IR OR cat:cs.SE)'
    
    # Use exact phrase matching with quotes for multi-word queries
    search_query = f'all:"{query}" AND {category_filter}'
    
    params = {
        'search_query': search_query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode('utf-8')
            return data
    except Exception as e:
        print(f"Error fetching {query}: {e}")
        return None

def parse_arxiv_response(xml_data):
    """Parse arXiv API response into paper list."""
    if not xml_data:
        return []
    
    papers = []
    
    try:
        root = ET.fromstring(xml_data)
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        
        for entry in root.findall('atom:entry', namespace):
            paper = {}
            
            # Extract ID (arXiv ID)
            id_url = entry.find('atom:id', namespace).text
            paper['arxiv_id'] = id_url.split('/abs/')[-1]
            
            # Extract title
            paper['title'] = entry.find('atom:title', namespace).text.strip()
            paper['title'] = re.sub(r'\s+', ' ', paper['title'])  # Normalize whitespace
            
            # Extract abstract
            paper['abstract'] = entry.find('atom:summary', namespace).text.strip()
            paper['abstract'] = re.sub(r'\s+', ' ', paper['abstract'])
            
            # Extract authors
            authors = []
            for author in entry.findall('atom:author', namespace):
                name = author.find('atom:name', namespace).text
                authors.append(name)
            paper['authors'] = ', '.join(authors)
            
            # Extract published date
            published = entry.find('atom:published', namespace).text
            paper['date'] = published.split('T')[0]  # Get YYYY-MM-DD
            
            # Extract categories
            categories = []
            for category in entry.findall('atom:category', namespace):
                categories.append(category.get('term'))
            paper['categories'] = categories
            
            # Extract PDF link
            for link in entry.findall('atom:link', namespace):
                if link.get('title') == 'pdf':
                    paper['pdf_url'] = link.get('href')
                    break
            
            paper['url'] = f"https://arxiv.org/abs/{paper['arxiv_id']}"
            
            papers.append(paper)
    
    except Exception as e:
        print(f"Error parsing XML: {e}")
    
    return papers

def classify_paper(paper):
    """Classify paper into focus areas based on title and abstract."""
    text = (paper['title'] + ' ' + paper['abstract']).lower()
    
    scores = {}
    
    # Score each focus area
    for area, keywords in FOCUS_AREAS.items():
        score = 0
        for keyword in keywords:
            keyword_lower = keyword.lower()
            # Count occurrences
            score += text.count(keyword_lower)
            # Boost for title matches
            if keyword_lower in paper['title'].lower():
                score += 3
        scores[area] = score
    
    # Return areas with score > 0, sorted by score
    classified = [area for area, score in sorted(scores.items(), key=lambda x: x[1], reverse=True) if score > 0]
    
    return classified if classified else ['ai-agents']  # Default to ai-agents

def paper_exists(arxiv_id, papers_dir):
    """Check if paper already exists in our collection."""
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for paper_file in date_dir.glob('*.md'):
            content = paper_file.read_text()
            if arxiv_id in content:
                return True
    return False

def create_paper_markdown(paper, topics):
    """Create markdown file for a paper."""
    # Clean title for filename
    clean_title = re.sub(r'[^\w\s-]', '', paper['title'])
    clean_title = re.sub(r'\s+', '-', clean_title)
    clean_title = clean_title[:80]  # Limit length
    
    filename = f"{paper['arxiv_id']}-{clean_title}.md"
    
    content = f"""# {paper['title']}

**arXiv ID:** {paper['arxiv_id']}
**Authors:** {paper['authors']}
**Date:** {paper['date']}
**URL:** {paper['url']}
**Topics:** {', '.join(topics)}

## Abstract

{paper['abstract']}

## Key Contributions

[To be extracted from full paper]

## Code

[Check paper for code availability]
"""
    
    return filename, content

def fetch_papers(days_back=7, max_per_query=5):
    """Fetch papers from all focus areas."""
    papers_dir = Path('papers')
    papers_dir.mkdir(exist_ok=True)
    
    all_papers = {}  # Use dict to deduplicate by arXiv ID
    new_papers = []
    
    print(f"Fetching papers from last {days_back} days...")
    print("=" * 60)
    
    for area, queries in FOCUS_AREAS.items():
        print(f"\nSearching: {area}")
        
        for query in queries[:2]:  # Limit to first 2 queries per area to avoid rate limits
            print(f"  Query: {query}")
            
            xml_data = search_arxiv(query, max_results=max_per_query, days_back=days_back)
            papers = parse_arxiv_response(xml_data)
            
            print(f"  Found {len(papers)} papers")
            
            for paper in papers:
                arxiv_id = paper['arxiv_id']
                
                # Skip if already in our collection
                if paper_exists(arxiv_id, papers_dir):
                    continue
                
                # Skip if already processed in this run
                if arxiv_id in all_papers:
                    continue
                
                # Classify paper
                topics = classify_paper(paper)
                paper['topics'] = topics
                
                all_papers[arxiv_id] = paper
                new_papers.append(paper)
                
                print(f"    ✓ {paper['title'][:60]}...")
            
            # Rate limiting
            time.sleep(3)
    
    print(f"\n{'=' * 60}")
    print(f"Total new papers: {len(new_papers)}")
    
    return new_papers

def save_papers(papers):
    """Save papers to markdown files."""
    papers_dir = Path('papers')
    saved_count = 0
    
    for paper in papers:
        # Create date directory
        date_dir = papers_dir / paper['date']
        date_dir.mkdir(exist_ok=True, parents=True)
        
        # Create markdown file
        filename, content = create_paper_markdown(paper, paper['topics'])
        filepath = date_dir / filename
        
        filepath.write_text(content)
        saved_count += 1
        
        print(f"Saved: {filename}")
    
    return saved_count

def main():
    """Main entry point."""
    print("arXiv Paper Fetcher")
    print("=" * 60)
    
    # Fetch papers
    new_papers = fetch_papers(days_back=7, max_per_query=5)
    
    if not new_papers:
        print("\nNo new papers found.")
        return
    
    # Save papers
    print(f"\nSaving {len(new_papers)} papers...")
    print("=" * 60)
    saved_count = save_papers(new_papers)
    
    print(f"\n{'=' * 60}")
    print(f"Successfully saved {saved_count} papers")
    print("\nNext steps:")
    print("1. Run: python3 enhance_papers.py")
    print("2. Run: python3 enhance_paper_details.py")
    print("3. Run: quarto render")

if __name__ == '__main__':
    main()
