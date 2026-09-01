#!/usr/bin/env python3
"""
Weekly Digest Generator
Automatically generates personalized weekly summaries of new papers and learning progress.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Import user management
from user_manager import get_current_user, load_user_data, load_user_config

def get_papers_from_last_week(papers_dir="papers"):
    """Get all papers added in the last 7 days."""
    papers = []
    cutoff_date = datetime.now() - timedelta(days=7)
    
    papers_path = Path(papers_dir)
    if not papers_path.exists():
        return papers
    
    for date_dir in papers_path.iterdir():
        if not date_dir.is_dir():
            continue
        
        try:
            dir_date = datetime.strptime(date_dir.name, "%Y-%m-%d")
            if dir_date >= cutoff_date:
                # Load all papers from this date
                for paper_file in date_dir.glob("*.md"):
                    paper = parse_paper_markdown(paper_file)
                    if paper:
                        paper['date_added'] = dir_date.strftime("%Y-%m-%d")
                        papers.append(paper)
        except ValueError:
            continue
    
    return papers

def parse_paper_markdown(file_path):
    """Parse a paper markdown file and extract metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        paper = {'file_path': str(file_path)}
        
        # Extract title from first heading
        import re
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            paper['title'] = title_match.group(1).strip()
        
        # Extract metadata from bold fields
        arxiv_match = re.search(r'\*\*arXiv ID:\*\*\s*(.+)', content)
        if arxiv_match:
            paper['arxiv_id'] = arxiv_match.group(1).strip()
        
        authors_match = re.search(r'\*\*Authors:\*\*\s*(.+)', content)
        if authors_match:
            paper['authors'] = authors_match.group(1).strip()
        
        date_match = re.search(r'\*\*Date:\*\*\s*(.+)', content)
        if date_match:
            paper['date'] = date_match.group(1).strip()
        
        topics_match = re.search(r'\*\*Topics:\*\*\s*(.+)', content)
        if topics_match:
            topics_str = topics_match.group(1).strip()
            paper['topics'] = [t.strip() for t in topics_str.split(',')]
        
        # Extract abstract
        abstract_match = re.search(r'## Abstract\s+(.+?)(?=\n## |\Z)', content, re.DOTALL)
        if abstract_match:
            paper['abstract'] = abstract_match.group(1).strip()
        
        # Extract arxiv_id from filename if not found
        if 'arxiv_id' not in paper:
            filename = file_path.stem
            if '-' in filename:
                paper['arxiv_id'] = filename.split('-')[0]
        
        return paper
        
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def analyze_weekly_themes(papers):
    """Analyze papers to identify key themes and topics."""
    theme_counts = defaultdict(int)
    theme_papers = defaultdict(list)
    
    for paper in papers:
        topics = paper.get('topics', [])
        if isinstance(topics, str):
            topics = [t.strip() for t in topics.split(',')]
        
        for topic in topics:
            theme_counts[topic] += 1
            theme_papers[topic].append(paper)
    
    # Sort themes by frequency
    sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_themes, theme_papers

def identify_highlight_papers(papers, user_data):
    """Identify papers that are particularly important or relevant."""
    highlights = []
    
    bookmarks = set(user_data.get('bookmarks', []))
    notes = user_data.get('notes', {})
    reading_progress = user_data.get('readingProgress', {})
    
    for paper in papers:
        arxiv_id = paper.get('arxiv_id')
        if not arxiv_id:
            continue
        
        score = 0
        
        # Boost if bookmarked
        if arxiv_id in bookmarks:
            score += 10
        
        # Boost if has notes
        if arxiv_id in notes and notes[arxiv_id]:
            score += 5
        
        # Boost if marked as read
        if arxiv_id in reading_progress:
            status = reading_progress[arxiv_id].get('status')
            if status == 'read':
                score += 8
            elif status == 'reading':
                score += 3
        
        if score > 0:
            highlights.append((paper, score))
    
    # Sort by score and return top 5
    highlights.sort(key=lambda x: x[1], reverse=True)
    return [h[0] for h in highlights[:5]]

def generate_learning_summary(user_data):
    """Generate summary of learning progress for the week."""
    reading_progress = user_data.get('readingProgress', {})
    notes = user_data.get('notes', {})
    
    # Count papers read this week
    papers_read = 0
    papers_with_notes = 0
    
    for arxiv_id, progress in reading_progress.items():
        if progress.get('status') == 'read':
            papers_read += 1
    
    papers_with_notes = len([n for n in notes.values() if n])
    
    return {
        'papers_read': papers_read,
        'papers_with_notes': papers_with_notes,
        'total_bookmarks': len(user_data.get('bookmarks', []))
    }

def generate_digest_markdown(week_start, week_end, papers, themes, highlights, learning_summary, username):
    """Generate the weekly digest in markdown format."""
    
    digest = f"""---
title: "Weekly Research Digest - Week of {week_start}"
date: {datetime.now().strftime("%Y-%m-%d")}
---

# 📊 Weekly Research Digest

**Period:** {week_start} to {week_end}  
**User:** {username}  
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## 📈 This Week's Overview

- **New Papers Added:** {len(papers)}
- **Papers Read:** {learning_summary['papers_read']}
- **Papers with Notes:** {learning_summary['papers_with_notes']}
- **Total Bookmarks:** {learning_summary['total_bookmarks']}

---

## 🎯 Key Themes This Week

"""
    
    if themes:
        for theme, count in themes[:5]:
            digest += f"- **{theme}**: {count} paper{'s' if count != 1 else ''}\n"
    else:
        digest += "No major themes identified this week.\n"
    
    digest += "\n---\n\n## ⭐ Highlight Papers\n\n"
    
    if highlights:
        for i, paper in enumerate(highlights, 1):
            title = paper.get('title', 'Untitled')
            arxiv_id = paper.get('arxiv_id', '')
            authors = paper.get('authors', 'Unknown')
            date_added = paper.get('date_added', '')
            
            digest += f"""### {i}. {title}

**arXiv ID:** {arxiv_id}  
**Authors:** {authors}  
**Added:** {date_added}

"""
    else:
        digest += "No highlight papers this week. Start bookmarking and noting papers to see them here!\n"
    
    digest += """
---

## 📚 Recent Papers

"""
    
    if papers:
        for paper in papers[:10]:
            title = paper.get('title', 'Untitled')
            arxiv_id = paper.get('arxiv_id', '')
            topics = paper.get('topics', [])
            if isinstance(topics, str):
                topics = [t.strip() for t in topics.split(',')]
            
            digest += f"- **{title}** ({arxiv_id}) - {', '.join(topics[:2])}\n"
    else:
        digest += "No new papers this week.\n"
    
    digest += f"""
---

## 💡 Learning Insights

"""
    
    if learning_summary['papers_read'] > 0:
        digest += f"Great progress! You read {learning_summary['papers_read']} paper{'s' if learning_summary['papers_read'] != 1 else ''} this week.\n\n"
    
    if learning_summary['papers_with_notes'] > 0:
        digest += f"You added notes to {learning_summary['papers_with_notes']} paper{'s' if learning_summary['papers_with_notes'] != 1 else ''}. Keep building your knowledge base!\n\n"
    
    if learning_summary['papers_read'] == 0 and learning_summary['papers_with_notes'] == 0:
        digest += "Consider setting aside time this week to review your bookmarked papers and add notes.\n\n"
    
    digest += """
---

## 🔗 Quick Links

- [View All Papers](search-papers.html)
- [My Learning Path](my-learning-path.html)
- [AI Study Guide](ai-study-guide.html)
- [Dashboard](dashboard.html)

---

*This digest was automatically generated by AI Research Tracker.*
"""
    
    return digest

def generate_weekly_digest():
    """Main function to generate the weekly digest."""
    username = get_current_user()
    user_data = load_user_data(username)
    
    # Get papers from last week
    papers = get_papers_from_last_week()
    
    if not papers:
        print("No new papers this week. Skipping digest generation.")
        return None
    
    # Analyze themes
    themes, theme_papers = analyze_weekly_themes(papers)
    
    # Identify highlights
    highlights = identify_highlight_papers(papers, user_data)
    
    # Generate learning summary
    learning_summary = generate_learning_summary(user_data)
    
    # Calculate week dates
    today = datetime.now()
    week_end = today.strftime("%Y-%m-%d")
    week_start = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Generate markdown
    digest_markdown = generate_digest_markdown(
        week_start, week_end, papers, themes, highlights, learning_summary, username
    )
    
    # Save digest
    digest_dir = Path("public/digests")
    digest_dir.mkdir(exist_ok=True)
    
    week_number = today.isocalendar()[1]
    year = today.year
    digest_filename = f"week-{year}-{week_number:02d}.md"
    digest_path = digest_dir / digest_filename
    
    with open(digest_path, 'w', encoding='utf-8') as f:
        f.write(digest_markdown)
    
    print(f"✅ Weekly digest generated: {digest_path}")
    return digest_path

if __name__ == "__main__":
    generate_weekly_digest()
