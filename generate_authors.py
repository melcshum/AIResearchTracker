#!/usr/bin/env python3
"""Generate author profiles page from paper data."""

import json
import re
from pathlib import Path
from collections import defaultdict

def parse_papers():
    papers_dir = Path('papers')
    papers = []
    
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for f in date_dir.glob('*.md'):
            content = f.read_text()
            title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
            authors_m = re.search(r'\*\*Authors:\*\* (.+)', content)
            date_m = re.search(r'\*\*Date:\*\* (.+)', content)
            topics_m = re.search(r'\*\*Topics:\*\* (.+)', content)
            arxiv_m = re.search(r'\*\*arXiv ID:\*\* (.+)', content)
            
            if title_m and authors_m and date_m and topics_m and arxiv_m:
                authors_raw = authors_m.group(1).strip()
                # Parse authors - they're comma-separated, may have initials
                authors = [a.strip() for a in authors_raw.split(',')]
                
                papers.append({
                    'title': title_m.group(1),
                    'authors': authors,
                    'authors_raw': authors_raw,
                    'date': date_m.group(1).strip(),
                    'topics': [t.strip() for t in topics_m.group(1).split(',')],
                    'arxiv_id': arxiv_m.group(1).strip(),
                    'url': str(f.with_suffix('.html').relative_to(Path('.')))
                })
    
    return papers

def build_author_profiles(papers):
    """Build author -> papers mapping."""
    author_papers = defaultdict(list)
    
    for paper in papers:
        for author in paper['authors']:
            author_papers[author].append(paper)
    
    return author_papers

def generate_page(papers, author_papers):
    """Generate the authors page HTML/Markdown."""
    
    # Sort authors by number of papers (descending)
    sorted_authors = sorted(author_papers.items(), key=lambda x: len(x[1]), reverse=True)
    
    # Build JSON data for the page
    authors_data = []
    for author, author_paper_list in sorted_authors:
        topics_set = set()
        for p in author_paper_list:
            topics_set.update(p['topics'])
        
        authors_data.append({
            'name': author,
            'paper_count': len(author_paper_list),
            'topics': sorted(list(topics_set)),
            'papers': [{
                'title': p['title'],
                'url': p['url'],
                'date': p['date'],
                'topics': p['topics']
            } for p in sorted(author_paper_list, key=lambda x: x['date'], reverse=True)]
        })
    
    page = f'''---
title: "Author Profiles"
---

Track research groups and individual contributors across the collection. Click on any author to see their papers and research areas.

<div class="authors-container">
  <div class="authors-controls">
    <input type="text" id="authorSearch" placeholder="Search authors..." class="author-search">
    <select id="topicFilter" class="topic-filter">
      <option value="">All Topics</option>
      <option value="ai-agents">AI Agents</option>
      <option value="llm-reasoning">LLM Reasoning</option>
      <option value="rag-retrieval">RAG & Retrieval</option>
      <option value="multi-modal">Multi-Modal</option>
    </select>
  </div>
  
  <div id="authorCount" class="author-count"></div>
  <div id="authorsList" class="authors-list"></div>
</div>

<style>
.authors-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}}

.authors-controls {{
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}}

.author-search {{
  flex: 1;
  min-width: 200px;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}}

.author-search:focus {{
  outline: none;
  border-color: #4a90e2;
}}

.topic-filter {{
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}}

.author-count {{
  color: #666;
  margin-bottom: 15px;
  font-size: 14px;
}}

.authors-list {{
  display: grid;
  gap: 15px;
}}

.author-card {{
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}}

.author-card:hover {{
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-color: #4a90e2;
}}

.author-card.expanded {{
  border-color: #4a90e2;
  background: #f8fbff;
}}

.author-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.author-name {{
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}}

.author-stats {{
  display: flex;
  gap: 15px;
  align-items: center;
}}

.paper-badge {{
  background: #4a90e2;
  color: white;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}}

.author-topics {{
  margin-top: 8px;
}}

.topic-tag {{
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-top: 4px;
}}

.author-papers {{
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #e0e0e0;
  display: none;
}}

.author-card.expanded .author-papers {{
  display: block;
}}

.paper-entry {{
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}}

.paper-entry:last-child {{
  border-bottom: none;
}}

.paper-entry a {{
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
}}

.paper-entry a:hover {{
  color: #4a90e2;
}}

.paper-date {{
  color: #999;
  font-size: 12px;
  margin-left: 8px;
}}

.expand-icon {{
  color: #999;
  font-size: 14px;
  transition: transform 0.2s;
}}

.author-card.expanded .expand-icon {{
  transform: rotate(90deg);
}}
</style>

<script>
const authorsData = {json.dumps(authors_data, indent=2)};

function renderAuthors() {{
  const searchTerm = document.getElementById('authorSearch').value.toLowerCase();
  const topicFilter = document.getElementById('topicFilter').value;
  
  let filtered = authorsData.filter(author => {{
    const matchesSearch = !searchTerm || author.name.toLowerCase().includes(searchTerm);
    const matchesTopic = !topicFilter || author.topics.includes(topicFilter);
    return matchesSearch && matchesTopic;
  }});
  
  document.getElementById('authorCount').textContent = 
    `Showing ${{filtered.length}} of ${{authorsData.length}} authors`;
  
  const container = document.getElementById('authorsList');
  
  if (filtered.length === 0) {{
    container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">No authors found.</p>';
    return;
  }}
  
  container.innerHTML = filtered.map(author => `
    <div class="author-card" onclick="this.classList.toggle('expanded')">
      <div class="author-header">
        <span class="author-name">${{author.name}}</span>
        <div class="author-stats">
          <span class="paper-badge">${{author.paper_count}} paper${{author.paper_count !== 1 ? 's' : ''}}</span>
          <span class="expand-icon">▶</span>
        </div>
      </div>
      <div class="author-topics">
        ${{author.topics.map(t => `<span class="topic-tag">${{t}}</span>`).join('')}}
      </div>
      <div class="author-papers">
        ${{author.papers.map(p => `
          <div class="paper-entry">
            <a href="${{p.url}}">${{p.title}}</a>
            <span class="paper-date">${{p.date}}</span>
          </div>
        `).join('')}}
      </div>
    </div>
  `).join('');
}}

document.getElementById('authorSearch').addEventListener('input', renderAuthors);
document.getElementById('topicFilter').addEventListener('change', renderAuthors);

renderAuthors();
</script>
'''
    
    return page

def main():
    papers = parse_papers()
    author_papers = build_author_profiles(papers)
    
    page_content = generate_page(papers, author_papers)
    Path('authors.md').write_text(page_content)
    
    print(f"Generated authors page with {len(author_papers)} authors from {len(papers)} papers")

if __name__ == '__main__':
    main()
