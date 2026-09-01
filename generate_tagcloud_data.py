#!/usr/bin/env python3
"""Inject paper data into public/tag-cloud.md."""
import json
import re
from pathlib import Path

def strip_html(text):
    """Remove all HTML tags and broken HTML fragments from text."""
    # Remove complete HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove broken HTML attribute fragments (e.g., \" onclick=\"...\")
    text = re.sub(r'\\?"[^"]*\\?"[^"]*\\?"[^"]*>', '', text)
    # Remove any remaining quote-backslash sequences from broken HTML
    text = re.sub(r'\\?"[^>]*>', '', text)
    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

papers = []
papers_dir = Path('public/papers')
for date_dir in papers_dir.iterdir():
    if not date_dir.is_dir():
        continue
    for f in date_dir.glob('*.md'):
        content = f.read_text()
        title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
        authors_m = re.search(r'\*\*Authors:\*\* (.+)', content)
        date_m = re.search(r'\*\*Date:\*\* (.+)', content)
        abstract_m = re.search(r'## Abstract\n\n(.+?)(?=\n\n## |\Z)', content, re.DOTALL)
        topics_m = re.search(r'\*\*Topics:\*\* (.+)', content)
        
        if title_m and authors_m and date_m and abstract_m and topics_m:
            papers.append({
                'title': strip_html(title_m.group(1)),
                'authors': strip_html(authors_m.group(1).strip()),
                'date': date_m.group(1).strip(),
                'abstract': strip_html(abstract_m.group(1).strip()),
                'topics': [strip_html(t.strip()) for t in topics_m.group(1).split(',')],
                'url': str(f.with_suffix('.html').relative_to(Path('public')))
            })

content = Path('public/tag-cloud.md').read_text()
# Replace existing papers data (between 'const papers = [' and the closing '];')
new_data = 'const papers = ' + json.dumps(papers, indent=2) + ';'
content = re.sub(
    r'const papers = \[.*?\];',
    lambda m: new_data,
    content,
    flags=re.DOTALL
)
Path('public/tag-cloud.md').write_text(content)
print(f'Injected {len(papers)} papers into public/tag-cloud.md')
