#!/usr/bin/env python3
"""
Generate dynamic topic pages for the active user.
Creates one page per enabled topic, supporting hierarchical display.
Integrates with Quarto build process.
"""

import json
from pathlib import Path
from datetime import datetime
from user_manager import get_current_user, load_user_config, get_enabled_topics

def load_all_papers():
    """Load all papers from the shared papers directory."""
    papers_dir = Path('papers')
    papers = []
    
    if not papers_dir.exists():
        return papers
    
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for paper_file in date_dir.glob('*.md'):
            paper = parse_paper_markdown(paper_file)
            if paper:
                papers.append(paper)
    
    return papers

def parse_paper_markdown(filepath):
    """Parse a paper markdown file and extract metadata."""
    try:
        content = filepath.read_text()
        lines = content.split('\n')
        
        paper = {
            'file': str(filepath),
            'title': '',
            'arxiv_id': '',
            'authors': '',
            'date': '',
            'url': '',
            'topics': [],
            'abstract': ''
        }
        
        in_abstract = False
        abstract_lines = []
        
        for line in lines:
            if line.startswith('# '):
                paper['title'] = line[2:].strip()
            elif line.startswith('**arXiv ID:**'):
                paper['arxiv_id'] = line.split('**')[2].strip()
            elif line.startswith('**Authors:**'):
                paper['authors'] = line.split('**')[2].strip()
            elif line.startswith('**Date:**'):
                paper['date'] = line.split('**')[2].strip()
            elif line.startswith('**URL:**'):
                paper['url'] = line.split('**')[2].strip()
            elif line.startswith('**Topics:**'):
                topics_str = line.split('**')[2].strip()
                paper['topics'] = [t.strip() for t in topics_str.split(',') if t.strip()]
            elif line.startswith('## Abstract'):
                in_abstract = True
            elif in_abstract and line.startswith('## '):
                in_abstract = False
            elif in_abstract:
                abstract_lines.append(line)
        
        paper['abstract'] = ' '.join(abstract_lines).strip()
        
        return paper
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def filter_papers_by_topic(papers, topic_config, all_topics):
    """Filter papers that match a topic's keywords."""
    keywords = [k.lower() for k in topic_config.get('keywords', [])]
    matched_papers = []
    
    for paper in papers:
        # Check if paper's topics field includes this topic
        if topic_config['id'] in paper.get('topics', []):
            matched_papers.append(paper)
            continue
        
        # Check if paper matches topic keywords
        text = (paper['title'] + ' ' + paper['abstract']).lower()
        score = sum(1 for kw in keywords if kw in text)
        
        if score > 0:
            matched_papers.append(paper)
    
    # Sort by date (newest first)
    matched_papers.sort(key=lambda p: p.get('date', ''), reverse=True)
    
    return matched_papers

def generate_topic_page(topic_config, papers, output_dir, parent_topic=None):
    """Generate a markdown page for a topic."""
    topic_id = topic_config['id']
    topic_name = topic_config['name']
    topic_icon = topic_config.get('icon', '📄')
    description = topic_config.get('description', '')
    
    # Filter papers for this topic
    all_topics = {}  # Would need to pass this in for full classification
    matched_papers = filter_papers_by_topic(papers, topic_config, all_topics)
    
    # Build page content
    content = f"""---
title: "{topic_icon} {topic_name}"
---

<div class="topic-page">
<div class="topic-header">
<h1>{topic_icon} {topic_name}</h1>
<p class="topic-description">{description}</p>
<div class="topic-meta">
<span>📄 {len(matched_papers)} papers</span>
<span>🔍 {len(topic_config.get('queries', []))} search queries</span>
<span>🏷️ {len(topic_config.get('keywords', []))} keywords</span>
</div>
</div>

"""
    
    # Add children topics if any
    children = topic_config.get('children', [])
    if children:
        content += """
<div class="subtopics-section">
<h2>📚 Sub-Topics</h2>
<div class="subtopics-grid">
"""
        for child in children:
            child_id = child['id']
            child_name = child['name']
            child_icon = child.get('icon', '📄')
            child_desc = child.get('description', '')
            
            content += f"""
<div class="subtopic-card">
<a href="{child_id}.html">
<div class="subtopic-icon">{child_icon}</div>
<div class="subtopic-name">{child_name}</div>
<div class="subtopic-description">{child_desc}</div>
</a>
</div>
"""
        
        content += """
</div>
</div>

"""
    
    # Add papers list
    if matched_papers:
        content += """
<div class="papers-section">
<h2>📄 Recent Papers</h2>
<div class="papers-list">
"""
        
        for paper in matched_papers[:20]:  # Limit to 20 most recent
            title = paper['title']
            url = paper['url']
            authors = paper['authors']
            date = paper['date']
            arxiv_id = paper['arxiv_id']
            
            # Truncate authors if too long
            if len(authors) > 100:
                authors = authors[:100] + '...'
            
            content += f"""
<div class="paper-card">
<div class="paper-title">
<a href="{url}" target="_blank">{title}</a>
</div>
<div class="paper-meta">
<span class="paper-authors">{authors}</span>
<span class="paper-date">{date}</span>
<span class="paper-arxiv">arXiv:{arxiv_id}</span>
</div>
</div>
"""
        
        content += """
</div>
</div>
"""
    else:
        content += """
<div class="no-papers">
<p>No papers found for this topic yet. Run the paper fetcher to populate this topic.</p>
</div>
"""
    
    content += """
</div>

<style>
.topic-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.topic-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color, #e0e0e0);
}

.topic-header h1 {
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.topic-description {
  color: var(--text-secondary, #666);
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.topic-meta {
  display: flex;
  gap: 1.5rem;
  color: var(--text-muted, #999);
  font-size: 0.9rem;
}

.subtopics-section {
  margin-bottom: 2rem;
}

.subtopics-section h2 {
  color: var(--text-primary, #2c3e50);
  margin-bottom: 1rem;
}

.subtopics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.subtopic-card {
  background: var(--bg-secondary, #f8f9fa);
  border: 1px solid var(--border-color, #e0e0e0);
  border-radius: 8px;
  padding: 1rem;
  transition: all 0.2s;
}

.subtopic-card:hover {
  border-color: var(--accent-color, #667eea);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.subtopic-card a {
  text-decoration: none;
  color: inherit;
  display: block;
}

.subtopic-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.subtopic-name {
  font-weight: 600;
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.subtopic-description {
  color: var(--text-secondary, #666);
  font-size: 0.9rem;
}

.papers-section h2 {
  color: var(--text-primary, #2c3e50);
  margin-bottom: 1rem;
}

.papers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.paper-card {
  background: var(--bg-secondary, #f8f9fa);
  border: 1px solid var(--border-color, #e0e0e0);
  border-radius: 8px;
  padding: 1rem;
}

.paper-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.paper-title a {
  color: var(--accent-color, #667eea);
  text-decoration: none;
}

.paper-title a:hover {
  text-decoration: underline;
}

.paper-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  color: var(--text-muted, #999);
  font-size: 0.85rem;
}

.no-papers {
  text-align: center;
  padding: 3rem;
  color: var(--text-secondary, #666);
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 8px;
}
</style>
"""
    
    # Write to file
    output_file = output_dir / f"{topic_id}.md"
    output_file.write_text(content)
    
    return output_file

def generate_topics_index(enabled_topics, output_dir):
    """Generate an index page listing all topics."""
    content = """---
title: "📚 My Research Topics"
---

<div class="topics-index">
<h1>📚 My Research Topics</h1>
<p class="index-description">Browse your personalized research topics and discover relevant papers.</p>

<div class="topics-grid">
"""
    
    for topic_id, topic_config in enabled_topics.items():
        # Skip child topics (they have '.' in their ID)
        if '.' in topic_id:
            continue
        
        topic_name = topic_config['name']
        topic_icon = topic_config.get('icon', '📄')
        description = topic_config.get('description', '')
        
        content += f"""
<div class="topic-card">
<a href="{topic_id}.html">
<div class="topic-icon">{topic_icon}</div>
<div class="topic-name">{topic_name}</div>
<div class="topic-description">{description}</div>
</a>
</div>
"""
    
    content += """
</div>
</div>

<style>
.topics-index {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.topics-index h1 {
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.index-description {
  color: var(--text-secondary, #666);
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.topic-card {
  background: var(--bg-secondary, #f8f9fa);
  border: 1px solid var(--border-color, #e0e0e0);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}

.topic-card:hover {
  border-color: var(--accent-color, #667eea);
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.topic-card a {
  text-decoration: none;
  color: inherit;
  display: block;
}

.topic-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.topic-name {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.topic-description {
  color: var(--text-secondary, #666);
  font-size: 0.95rem;
  line-height: 1.5;
}
</style>
"""
    
    output_file = output_dir / "topics-index.md"
    output_file.write_text(content)
    
    return output_file

def main():
    """Generate topic pages for the active user."""
    print("📚 Generating dynamic topic pages...")
    print("=" * 60)
    
    # Get current user
    username = get_current_user()
    print(f"Active user: {username}")
    
    # Load user config
    config = load_user_config(username)
    enabled_topics = get_enabled_topics(username)
    
    print(f"Enabled topics: {len(enabled_topics)}")
    
    # Load all papers
    papers = load_all_papers()
    print(f"Total papers: {len(papers)}")
    
    # Output directory
    output_dir = Path('public/topics')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate index page
    print("\n📋 Generating topics index...")
    index_file = generate_topics_index(enabled_topics, output_dir)
    print(f"   ✓ {index_file}")
    
    # Generate page for each enabled topic
    print("\n📄 Generating topic pages...")
    for topic_id, topic_config in enabled_topics.items():
        output_file = generate_topic_page(topic_config, papers, output_dir)
        print(f"   ✓ {topic_config['name']} → {output_file}")
    
    print("\n" + "=" * 60)
    print(f"✅ Generated {len(enabled_topics) + 1} pages in {output_dir}")
    print("\nNext steps:")
    print("1. Run: quarto render")
    print("2. Open: http://localhost:8000/public/topics/topics-index.html")

if __name__ == '__main__':
    main()
