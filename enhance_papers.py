#!/usr/bin/env python3
"""
Enhance paper detail pages with structured summaries and related papers.
Improved version: extracts full sentences for key contributions.
"""

import os
import re
from pathlib import Path

def split_sentences(text):
    """Split text into sentences, handling abbreviations."""
    # Simple sentence splitter
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    return [s.strip() for s in sentences if s.strip()]

def extract_key_contributions(abstract):
    """Extract key contributions from abstract as full sentences."""
    sentences = split_sentences(abstract)
    contributions = []
    
    # Keywords that signal key contributions
    keywords = [
        'we propose', 'we introduce', 'we present', 'we develop',
        'our method', 'our approach', 'our framework', 'our system',
        'first', 'novel', 'new', 'state-of-the-art',
        'outperform', 'improve', 'achieve', 'demonstrate',
        'eliminates', 'enables', 'supports', 'introduces'
    ]
    
    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(kw in sentence_lower for kw in keywords):
            contributions.append(sentence)
    
    # If no keyword matches, take the most informative sentences
    if not contributions:
        # Take sentences with numbers or specific claims
        for sentence in sentences:
            if re.search(r'\d+', sentence) or 'show' in sentence.lower():
                contributions.append(sentence)
    
    return contributions[:3]  # Limit to top 3

def find_related_papers(current_paper, all_papers):
    """Find related papers based on shared concepts."""
    current_id = current_paper.get('arxiv_id', '')
    current_topics = current_paper.get('topics', [])
    
    related = []
    for paper in all_papers:
        if paper.get('arxiv_id') == current_id:
            continue
        
        # Check for shared topics
        paper_topics = paper.get('topics', [])
        shared_topics = set(current_topics) & set(paper_topics)
        
        if shared_topics:
            related.append({
                'title': paper.get('title', ''),
                'url': paper.get('url', ''),
                'shared_topics': list(shared_topics)
            })
    
    return related[:5]  # Top 5 related

def parse_paper_file(filepath):
    """Parse a paper markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    paper = {}
    
    # Extract title
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        paper['title'] = title_match.group(1)
    
    # Extract arXiv ID
    id_match = re.search(r'\*\*arXiv ID:\*\* (.+)', content)
    if id_match:
        paper['arxiv_id'] = id_match.group(1).strip()
    
    # Extract URL
    url_match = re.search(r'\*\*URL:\*\* (.+)', content)
    if url_match:
        paper['url'] = url_match.group(1).strip()
    
    # Extract topics
    topics_match = re.search(r'\*\*Topics:\*\* (.+)', content)
    if topics_match:
        topics_str = topics_match.group(1).strip()
        paper['topics'] = [t.strip() for t in topics_str.split(',')]
    
    # Extract abstract
    abstract_match = re.search(r'## Abstract\n\n(.+?)(?=\n\n## |\Z)', content, re.DOTALL)
    if abstract_match:
        paper['abstract'] = abstract_match.group(1).strip()
    
    return paper

def enhance_paper_page(filepath, all_papers):
    """Enhance a single paper page."""
    paper = parse_paper_file(filepath)
    
    if not paper.get('abstract'):
        return
    
    # Read current content
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract key contributions
    contributions = extract_key_contributions(paper['abstract'])
    
    # Replace placeholder or garbled key contributions
    if contributions:
        contrib_text = "\n".join([f"- {c}" for c in contributions])
        # Match both placeholder and any existing garbled content
        content = re.sub(
            r'## Key Contributions\n\n(?:\[To be extracted from full paper\]|(?:- .+\n?)+)',
            f'## Key Contributions\n\n{contrib_text}'.replace('\\', '\\\\'),
            content
        )
    
    # Find related papers
    related = find_related_papers(paper, all_papers)
    
    # Add or replace related papers section
    if related:
        related_text = "\n\n## Related Papers\n\n"
        for rel in related:
            topics_str = ', '.join(rel['shared_topics'])
            related_text += f"- [{rel['title']}]({rel['url']}) (shared topics: {topics_str})\n"
        
        # Remove existing related papers section if present
        content = re.sub(r'\n\n## Related Papers\n\n.*$', '', content, flags=re.DOTALL)
        content += related_text
    
    # Write enhanced content
    with open(filepath, 'w') as f:
        f.write(content)

def main():
    papers_dir = Path('/Users/ailcshum/workspace/research-notes/papers')
    
    # Parse all papers from all date directories
    all_papers = []
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for filepath in date_dir.glob('*.md'):
            paper = parse_paper_file(filepath)
            paper['filepath'] = filepath
            all_papers.append(paper)
    
    print(f"Found {len(all_papers)} papers")
    
    # Enhance each paper
    for paper in all_papers:
        enhance_paper_page(paper['filepath'], all_papers)
        print(f"Enhanced: {paper['title'][:50]}...")

if __name__ == '__main__':
    main()
