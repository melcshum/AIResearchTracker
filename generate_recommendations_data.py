#!/usr/bin/env python3
"""
Generate recommendations data from papers and inject into recommendations.md
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

def extract_paper_metadata(paper_path):
    """Extract metadata from a paper markdown file"""
    with open(paper_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(paper_path).stem
    
    # Extract arxiv ID from filename
    filename = Path(paper_path).name
    arxiv_id_match = re.match(r'(\d+\.\d+)', filename)
    arxiv_id = arxiv_id_match.group(1) if arxiv_id_match else ''
    
    # Extract date from directory
    date_match = re.search(r'/papers/(\d{4}-\d{2}-\d{2})/', paper_path)
    date = date_match.group(1) if date_match else ''
    
    # Extract topics from tags
    topics = []
    tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
    if tags_match:
        topics = [t.strip() for t in tags_match.group(1).split(',')]
    
    # Extract authors
    authors = ''
    authors_match = re.search(r'authors?:\s*(.+)', content, re.IGNORECASE)
    if authors_match:
        authors = authors_match.group(1).strip()
    
    # Extract URL
    url = f'https://arxiv.org/abs/{arxiv_id}' if arxiv_id else '#'
    
    return {
        'id': arxiv_id or Path(paper_path).stem,
        'title': title,
        'date': date,
        'topics': topics,
        'authors': authors,
        'url': url
    }

def generate_recommendations_data():
    """Generate recommendations data from all papers"""
    papers_dir = Path('papers')
    all_papers = []
    
    # Walk through all date directories
    for date_dir in papers_dir.iterdir():
        if date_dir.is_dir() and re.match(r'\d{4}-\d{2}-\d{2}', date_dir.name):
            for paper_file in date_dir.glob('*.md'):
                if paper_file.name != 'index.md':
                    try:
                        paper_data = extract_paper_metadata(str(paper_file))
                        all_papers.append(paper_data)
                    except Exception as e:
                        print(f"Error processing {paper_file}: {e}")
    
    print(f"Found {len(all_papers)} papers")
    
    # Sort by date (newest first)
    all_papers.sort(key=lambda x: x['date'], reverse=True)
    
    return all_papers

def inject_data_into_recommendations(papers_data):
    """Inject paper data into recommendations.md"""
    rec_file = Path('recommendations.md')
    
    with open(rec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the placeholder with actual data using simple string replacement
    # (avoids regex escape issues with JSON backslashes)
    papers_json = json.dumps(papers_data, indent=2)
    new_content = content.replace(
        'window.PAPERS_DATA = [];',
        f'window.PAPERS_DATA = {papers_json};'
    )
    
    with open(rec_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Injected {len(papers_data)} papers into recommendations.md")

if __name__ == '__main__':
    print("Generating recommendations data...")
    papers_data = generate_recommendations_data()
    inject_data_into_recommendations(papers_data)
    print("Done!")
