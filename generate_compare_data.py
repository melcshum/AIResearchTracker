#!/usr/bin/env python3
"""Generate data for compare-papers page."""
import json
import re
from pathlib import Path

papers = []
for date_dir in Path('papers').iterdir():
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
                'title': title_m.group(1),
                'authors': authors_m.group(1).strip(),
                'date': date_m.group(1).strip(),
                'abstract': abstract_m.group(1).strip()[:300],
                'topics': [t.strip() for t in topics_m.group(1).split(',')],
                'url': str(f.with_suffix('.html').relative_to(Path('.')))
            })

print(f"Found {len(papers)} papers")

content = Path('compare-papers.md').read_text()
content = content.replace('PAPERS_DATA_PLACEHOLDER', json.dumps(papers, indent=2))
Path('compare-papers.md').write_text(content)
print("Updated compare-papers.md")
