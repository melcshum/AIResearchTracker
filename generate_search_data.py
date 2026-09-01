#!/usr/bin/env python3
"""
Generate JSON data for the search page and inject it into the HTML.
"""

import json
import re
from pathlib import Path

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
    
    # Extract date
    date_match = re.search(r'\*\*Date:\*\* (.+)', content)
    if date_match:
        paper['date'] = date_match.group(1).strip()
    
    # Extract authors
    authors_match = re.search(r'\*\*Authors:\*\* (.+)', content)
    if authors_match:
        paper['authors'] = authors_match.group(1).strip()
    
    # Extract abstract
    abstract_match = re.search(r'## Abstract\n\n(.+?)(?=\n\n## |\Z)', content, re.DOTALL)
    if abstract_match:
        paper['abstract'] = abstract_match.group(1).strip()
    
    # Extract topics
    topics_match = re.search(r'\*\*Topics:\*\* (.+)', content)
    if topics_match:
        topics_str = topics_match.group(1).strip()
        paper['topics'] = [t.strip() for t in topics_str.split(',')]
    
    # Convert URL to local path
    if 'url' in paper:
        arxiv_id = paper.get('arxiv_id', '')
        if arxiv_id:
            # Find the actual HTML file
            html_file = filepath.with_suffix('.html')
            if html_file.exists():
                paper['url'] = str(html_file.relative_to(Path('/Users/ailcshum/workspace/research-notes')))
    
    return paper

def main():
    papers_dir = Path('/Users/ailcshum/workspace/research-notes/papers')
    search_page = Path('/Users/ailcshum/workspace/research-notes/search-papers.md')
    
    # Parse all papers
    all_papers = []
    for date_dir in papers_dir.iterdir():
        if date_dir.is_dir():
            for filepath in date_dir.glob('*.md'):
                paper = parse_paper_file(filepath)
                all_papers.append(paper)
    
    print(f"Found {len(all_papers)} papers")
    
    # Convert to JSON
    papers_json = json.dumps(all_papers, indent=2)
    
    # Read the search page template
    with open(search_page, 'r') as f:
        content = f.read()
    
    # Replace placeholder with actual data
    content = content.replace('PAPERS_DATA_PLACEHOLDER', papers_json)
    
    # Write back
    with open(search_page, 'w') as f:
        f.write(content)
    
    print(f"Updated search page with {len(all_papers)} papers")

if __name__ == '__main__':
    main()
