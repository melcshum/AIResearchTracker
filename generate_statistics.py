#!/usr/bin/env python3
"""Generate statistics dashboard page from paper data."""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

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
                authors = [a.strip() for a in authors_raw.split(',')]
                
                papers.append({
                    'title': title_m.group(1),
                    'authors': authors,
                    'date': date_m.group(1).strip(),
                    'topics': [t.strip() for t in topics_m.group(1).split(',')],
                    'arxiv_id': arxiv_m.group(1).strip()
                })
    
    return papers

def compute_stats(papers):
    """Compute various statistics."""
    stats = {
        'total_papers': len(papers),
        'total_authors': len(set(a for p in papers for a in p['authors'])),
        'topic_counts': defaultdict(int),
        'author_counts': defaultdict(int),
        'papers_per_month': defaultdict(int),
        'collaborations': defaultdict(int),
        'avg_authors_per_paper': 0,
        'most_productive_author': '',
        'most_productive_author_count': 0,
        'most_common_topic': '',
        'most_common_topic_count': 0,
        'date_range': {'earliest': '', 'latest': ''},
        'topic_timeline': defaultdict(lambda: defaultdict(int))
    }
    
    # Count topics and authors
    for paper in papers:
        for topic in paper['topics']:
            stats['topic_counts'][topic] += 1
        
        for author in paper['authors']:
            stats['author_counts'][author] += 1
        
        # Parse date for timeline
        try:
            date = datetime.strptime(paper['date'], '%Y-%m-%d')
            month_key = date.strftime('%Y-%m')
            stats['papers_per_month'][month_key] += 1
            
            for topic in paper['topics']:
                stats['topic_timeline'][month_key][topic] += 1
            
            if not stats['date_range']['earliest'] or date < datetime.strptime(stats['date_range']['earliest'], '%Y-%m-%d'):
                stats['date_range']['earliest'] = paper['date']
            if not stats['date_range']['latest'] or date > datetime.strptime(stats['date_range']['latest'], '%Y-%m-%d'):
                stats['date_range']['latest'] = paper['date']
        except:
            pass
        
        # Count collaborations (pairs of authors)
        for i, author1 in enumerate(paper['authors']):
            for author2 in paper['authors'][i+1:]:
                pair = tuple(sorted([author1, author2]))
                stats['collaborations'][pair] += 1
    
    # Compute averages and find maximums
    if papers:
        stats['avg_authors_per_paper'] = sum(len(p['authors']) for p in papers) / len(papers)
    
    if stats['author_counts']:
        most_productive = max(stats['author_counts'].items(), key=lambda x: x[1])
        stats['most_productive_author'] = most_productive[0]
        stats['most_productive_author_count'] = most_productive[1]
    
    if stats['topic_counts']:
        most_common = max(stats['topic_counts'].items(), key=lambda x: x[1])
        stats['most_common_topic'] = most_common[0]
        stats['most_common_topic_count'] = most_common[1]
    
    # Convert defaultdicts to regular dicts for JSON
    stats['topic_counts'] = dict(stats['topic_counts'])
    stats['author_counts'] = dict(stats['author_counts'])
    stats['papers_per_month'] = dict(stats['papers_per_month'])
    stats['topic_timeline'] = {k: dict(v) for k, v in stats['topic_timeline'].items()}
    
    # Convert collaboration tuples to strings
    stats['collaborations'] = {f"{k[0]} & {k[1]}": v for k, v in stats['collaborations'].items()}
    
    return stats

def generate_page(stats):
    """Generate the statistics dashboard page."""
    
    page = f'''---
title: "Statistics Dashboard"
---

Overview of the research collection's composition and trends.

<div class="stats-container">
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">{stats['total_papers']}</div>
      <div class="stat-label">Total Papers</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{stats['total_authors']}</div>
      <div class="stat-label">Unique Authors</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{stats['avg_authors_per_paper']:.1f}</div>
      <div class="stat-label">Avg Authors/Paper</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{len(stats['topic_counts'])}</div>
      <div class="stat-label">Research Topics</div>
    </div>
  </div>

  <div class="stats-section">
    <h2>Topic Distribution</h2>
    <div id="topicChart" class="chart-container"></div>
  </div>

  <div class="stats-section">
    <h2>Top Authors</h2>
    <div id="authorChart" class="chart-container"></div>
  </div>

  <div class="stats-section">
    <h2>Papers Over Time</h2>
    <div id="timelineChart" class="chart-container"></div>
  </div>

  <div class="stats-section">
    <h2>Topic Timeline</h2>
    <div id="topicTimeline" class="chart-container"></div>
  </div>

  <div class="stats-section">
    <h2>Key Insights</h2>
    <div class="insights-grid">
      <div class="insight-card">
        <div class="insight-icon">📚</div>
        <div class="insight-content">
          <div class="insight-title">Most Productive Author</div>
          <div class="insight-value">{stats['most_productive_author']}</div>
          <div class="insight-detail">{stats['most_productive_author_count']} papers</div>
        </div>
      </div>
      <div class="insight-card">
        <div class="insight-icon">🎯</div>
        <div class="insight-content">
          <div class="insight-title">Most Common Topic</div>
          <div class="insight-value">{stats['most_common_topic']}</div>
          <div class="insight-detail">{stats['most_common_topic_count']} papers</div>
        </div>
      </div>
      <div class="insight-card">
        <div class="insight-icon">📅</div>
        <div class="insight-content">
          <div class="insight-title">Date Range</div>
          <div class="insight-value">{stats['date_range']['earliest']} to {stats['date_range']['latest']}</div>
          <div class="insight-detail">{len(stats['papers_per_month'])} months covered</div>
        </div>
      </div>
      <div class="insight-card">
        <div class="insight-icon">🤝</div>
        <div class="insight-content">
          <div class="insight-title">Collaborations</div>
          <div class="insight-value">{len(stats['collaborations'])}</div>
          <div class="insight-detail">unique author pairs</div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.stats-container {{
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}}

.stats-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}}

.stat-card {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 30px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}

.stat-value {{
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 8px;
}}

.stat-label {{
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.9;
}}

.stats-section {{
  margin-bottom: 40px;
}}

.stats-section h2 {{
  color: #2c3e50;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e0e0e0;
}}

.chart-container {{
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  min-height: 300px;
}}

.insights-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}}

.insight-card {{
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  gap: 15px;
  align-items: center;
  transition: all 0.2s;
}}

.insight-card:hover {{
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}}

.insight-icon {{
  font-size: 36px;
}}

.insight-content {{
  flex: 1;
}}

.insight-title {{
  font-size: 12px;
  text-transform: uppercase;
  color: #666;
  letter-spacing: 1px;
  margin-bottom: 4px;
}}

.insight-value {{
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 4px;
}}

.insight-detail {{
  font-size: 14px;
  color: #999;
}}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<script>
const stats = {json.dumps(stats, indent=2)};

// Topic Distribution Chart
const topicCtx = document.getElementById('topicChart');
if (topicCtx) {{
  const topicData = Object.entries(stats.topic_counts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);
  
  new Chart(topicCtx, {{
    type: 'bar',
    data: {{
      labels: topicData.map(d => d[0]),
      datasets: [{{
        label: 'Papers',
        data: topicData.map(d => d[1]),
        backgroundColor: 'rgba(102, 126, 234, 0.8)',
        borderColor: 'rgba(102, 126, 234, 1)',
        borderWidth: 1
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }}
      }},
      scales: {{
        y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }}
      }}
    }}
  }});
}}

// Top Authors Chart
const authorCtx = document.getElementById('authorChart');
if (authorCtx) {{
  const authorData = Object.entries(stats.author_counts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 15);
  
  new Chart(authorCtx, {{
    type: 'bar',
    data: {{
      labels: authorData.map(d => d[0]),
      datasets: [{{
        label: 'Papers',
        data: authorData.map(d => d[1]),
        backgroundColor: 'rgba(118, 75, 162, 0.8)',
        borderColor: 'rgba(118, 75, 162, 1)',
        borderWidth: 1
      }}]
    }},
    options: {{
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }}
      }},
      scales: {{
        x: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }}
      }}
    }}
  }});
}}

// Timeline Chart
const timelineCtx = document.getElementById('timelineChart');
if (timelineCtx) {{
  const timelineData = Object.entries(stats.papers_per_month)
    .sort((a, b) => a[0].localeCompare(b[0]));
  
  new Chart(timelineCtx, {{
    type: 'line',
    data: {{
      labels: timelineData.map(d => d[0]),
      datasets: [{{
        label: 'Papers',
        data: timelineData.map(d => d[1]),
        borderColor: 'rgba(102, 126, 234, 1)',
        backgroundColor: 'rgba(102, 126, 234, 0.1)',
        fill: true,
        tension: 0.4
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }}
      }},
      scales: {{
        y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }}
      }}
    }}
  }});
}}

// Topic Timeline Chart
const topicTimelineCtx = document.getElementById('topicTimeline');
if (topicTimelineCtx) {{
  const months = Object.keys(stats.topic_timeline).sort();
  const topics = [...new Set(Object.values(stats.topic_timeline).flatMap(m => Object.keys(m)))];
  
  const colors = [
    'rgba(102, 126, 234, 1)',
    'rgba(118, 75, 162, 1)',
    'rgba(255, 154, 158, 1)',
    'rgba(186, 168, 179, 1)',
    'rgba(250, 200, 152, 1)'
  ];
  
  const datasets = topics.map((topic, i) => ({{
    label: topic,
    data: months.map(m => stats.topic_timeline[m][topic] || 0),
    borderColor: colors[i % colors.length],
    backgroundColor: colors[i % colors.length].replace('1)', '0.1)'),
    fill: false,
    tension: 0.4
  }}));
  
  new Chart(topicTimelineCtx, {{
    type: 'line',
    data: {{
      labels: months,
      datasets: datasets
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: true, position: 'top' }}
      }},
      scales: {{
        y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }}
      }}
    }}
  }});
}}
</script>
'''
    
    return page

def main():
    papers = parse_papers()
    stats = compute_stats(papers)
    page_content = generate_page(stats)
    Path('statistics.md').write_text(page_content)
    
    print(f"Generated statistics dashboard from {len(papers)} papers")

if __name__ == '__main__':
    main()
