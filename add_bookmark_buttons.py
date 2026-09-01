#!/usr/bin/env python3
"""Add bookmark buttons to all paper pages."""

import re
from pathlib import Path

def add_bookmark_button(content, arxiv_id):
    """Add bookmark button HTML and JS to paper content."""
    
    # Check if bookmark button already exists
    if 'bookmark-btn' in content:
        return content
    
    # Add bookmark button after the title
    bookmark_html = f'''
<div class="paper-actions">
  <button id="bookmarkBtn" class="bookmark-btn" data-arxiv-id="{arxiv_id}">
    <span class="bookmark-icon">☆</span>
    <span class="bookmark-text">Save to Reading List</span>
  </button>
  <a href="reading-list.html" class="view-list-btn">View Reading List</a>
</div>

<style>
.paper-actions {{
  display: flex;
  gap: 10px;
  margin: 20px 0;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  align-items: center;
}}

.bookmark-btn {{
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: #4a90e2;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}}

.bookmark-btn:hover {{
  background: #357abd;
  transform: translateY(-1px);
}}

.bookmark-btn.saved {{
  background: #28a745;
}}

.bookmark-btn.saved:hover {{
  background: #218838;
}}

.bookmark-icon {{
  font-size: 18px;
}}

.view-list-btn {{
  padding: 10px 20px;
  background: #6c757d;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.2s;
}}

.view-list-btn:hover {{
  background: #5a6268;
}}
</style>

<script>
(function() {{
  const arxivId = "{arxiv_id}";
  const btn = document.getElementById('bookmarkBtn');
  const icon = btn.querySelector('.bookmark-icon');
  const text = btn.querySelector('.bookmark-text');
  
  // Check if already saved
  const saved = JSON.parse(localStorage.getItem('readingList') || '[]');
  if (saved.includes(arxivId)) {{
    btn.classList.add('saved');
    icon.textContent = '★';
    text.textContent = 'Saved to Reading List';
  }}
  
  btn.addEventListener('click', function() {{
    let list = JSON.parse(localStorage.getItem('readingList') || '[]');
    
    if (list.includes(arxivId)) {{
      // Remove from list
      list = list.filter(id => id !== arxivId);
      btn.classList.remove('saved');
      icon.textContent = '☆';
      text.textContent = 'Save to Reading List';
    }} else {{
      // Add to list
      list.push(arxivId);
      btn.classList.add('saved');
      icon.textContent = '★';
      text.textContent = 'Saved to Reading List';
    }}
    
    localStorage.setItem('readingList', JSON.stringify(list));
  }});
}})();
</script>
'''
    
    # Insert after the first </h1> or after the title section
    # Find the title line and insert after it
    lines = content.split('\n')
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            insert_idx = i + 1
            break
    
    if insert_idx > 0:
        lines.insert(insert_idx, bookmark_html)
        content = '\n'.join(lines)
    
    return content

def process_paper_file(filepath):
    """Process a single paper file."""
    content = filepath.read_text()
    
    # Extract arXiv ID
    arxiv_m = re.search(r'\*\*arXiv ID:\*\* (.+)', content)
    if not arxiv_m:
        return False
    
    arxiv_id = arxiv_m.group(1).strip()
    
    # Add bookmark button
    new_content = add_bookmark_button(content, arxiv_id)
    
    if new_content != content:
        filepath.write_text(new_content)
        return True
    return False

def main():
    papers_dir = Path('papers')
    count = 0
    
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for filepath in date_dir.glob('*.md'):
            if process_paper_file(filepath):
                print(f'✓ {filepath.name}')
                count += 1
    
    print(f'\nAdded bookmark buttons to {count} papers')

if __name__ == '__main__':
    main()
