#!/usr/bin/env python3
"""
Generate RSS feed for the AI Research Tracker.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

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
    
    # Extract relative path for link
    paper['filepath'] = filepath
    
    return paper

def generate_rss_feed(papers, output_path):
    """Generate RSS 2.0 feed."""
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    
    # Channel metadata
    ET.SubElement(channel, 'title').text = 'AI Research Tracker'
    ET.SubElement(channel, 'link').text = 'http://100.64.0.17:8001/'
    ET.SubElement(channel, 'description').text = 'Curated research on AI agents, reasoning, RAG, and multi-modal systems'
    ET.SubElement(channel, 'language').text = 'en-us'
    ET.SubElement(channel, 'lastBuildDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
    
    # Sort papers by date (newest first)
    papers_sorted = sorted(papers, key=lambda p: p.get('date', ''), reverse=True)
    
    # Add items (papers)
    for paper in papers_sorted[:50]:  # Limit to 50 most recent
        item = ET.SubElement(channel, 'item')
        
        # Title
        ET.SubElement(item, 'title').text = paper.get('title', 'Untitled')
        
        # Link - construct URL from filepath
        # Source is in papers/, rendered HTML is in _site/papers/
        rel_path = paper['filepath'].relative_to(Path('/Users/ailcshum/workspace/research-notes'))
        html_path = rel_path.with_suffix('.html')
        link = f"http://100.64.0.17:8001/{html_path}"
        ET.SubElement(item, 'link').text = link
        
        # Description - use abstract
        description = paper.get('abstract', '')
        if paper.get('authors'):
            description = f"**Authors:** {paper['authors']}\n\n{description}"
        if paper.get('topics'):
            topics_str = ', '.join(paper['topics'])
            description = f"**Topics:** {topics_str}\n\n{description}"
        ET.SubElement(item, 'description').text = description
        
        # GUID - use arXiv ID
        ET.SubElement(item, 'guid').text = paper.get('url', link)
        
        # Publication date
        if paper.get('date'):
            try:
                date_obj = datetime.strptime(paper['date'], '%Y-%m-%d')
                ET.SubElement(item, 'pubDate').text = date_obj.strftime('%a, %d %b %Y 00:00:00 %z')
            except:
                pass
    
    # Pretty print
    xml_str = ET.tostring(rss, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ')
    
    # Remove extra blank lines
    lines = [line for line in pretty_xml.split('\n') if line.strip()]
    pretty_xml = '\n'.join(lines)
    
    # Write to file
    with open(output_path, 'w') as f:
        f.write(pretty_xml)
    
    print(f"Generated RSS feed with {len(papers_sorted)} papers")

def main():
    papers_dir = Path('/Users/ailcshum/workspace/research-notes/papers')
    output_path = Path('/Users/ailcshum/workspace/research-notes/_site/rss.xml')
    
    # Parse all papers
    all_papers = []
    for date_dir in papers_dir.iterdir():
        if date_dir.is_dir():
            for filepath in date_dir.glob('*.md'):
                paper = parse_paper_file(filepath)
                all_papers.append(paper)
    
    print(f"Found {len(all_papers)} papers")
    
    # Generate RSS feed
    generate_rss_feed(all_papers, output_path)

if __name__ == '__main__':
    main()
