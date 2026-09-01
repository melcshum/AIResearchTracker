#!/usr/bin/env python3
"""Generate paper notes page with annotation and reading progress features."""

import json
import re
from pathlib import Path

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
                papers.append({
                    'title': title_m.group(1),
                    'authors': authors_m.group(1).strip(),
                    'date': date_m.group(1).strip(),
                    'topics': [t.strip() for t in topics_m.group(1).split(',')],
                    'arxiv_id': arxiv_m.group(1).strip(),
                    'url': str(f.with_suffix('.html').relative_to(Path('.')))
                })
    
    return papers

def generate_page(papers):
    """Generate the notes page with annotation features."""
    
    page = f'''---
title: "Paper Notes & Progress"
---

Track your reading progress and add personal annotations to papers. All data is stored locally in your browser.

<div class="notes-container">
  <div class="notes-header">
    <h2>My Paper Notes</h2>
    <div class="notes-actions">
      <button id="exportNotesBtn" class="btn-primary">Export Notes</button>
      <button id="importNotesBtn" class="btn-secondary">Import Notes</button>
      <input type="file" id="importFile" accept=".json" style="display:none">
    </div>
  </div>

  <div class="progress-summary">
    <div class="progress-stat">
      <div class="progress-value" id="toReadCount">0</div>
      <div class="progress-label">To Read</div>
    </div>
    <div class="progress-stat">
      <div class="progress-value" id="readingCount">0</div>
      <div class="progress-label">Reading</div>
    </div>
    <div class="progress-stat">
      <div class="progress-value" id="readCount">0</div>
      <div class="progress-label">Read</div>
    </div>
    <div class="progress-stat">
      <div class="progress-value" id="notesCount">0</div>
      <div class="progress-label">With Notes</div>
    </div>
  </div>

  <div class="notes-controls">
    <input type="text" id="paperSearch" placeholder="Search papers..." class="search-input">
    <select id="statusFilter" class="filter-select">
      <option value="">All Status</option>
      <option value="to-read">To Read</option>
      <option value="reading">Reading</option>
      <option value="read">Read</option>
    </select>
    <select id="hasNotesFilter" class="filter-select">
      <option value="">All Papers</option>
      <option value="yes">Has Notes</option>
      <option value="no">No Notes</option>
    </select>
  </div>

  <div id="papersList" class="papers-list"></div>
</div>

<style>
.notes-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}}

.notes-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 15px;
}}

.notes-header h2 {{
  margin: 0;
  color: #2c3e50;
}}

.notes-actions {{
  display: flex;
  gap: 10px;
}}

.btn-primary, .btn-secondary {{
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}}

.btn-primary {{
  background: #4a90e2;
  color: white;
}}

.btn-primary:hover {{
  background: #357abd;
}}

.btn-secondary {{
  background: #6c757d;
  color: white;
}}

.btn-secondary:hover {{
  background: #5a6268;
}}

.progress-summary {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
}}

.progress-stat {{
  text-align: center;
}}

.progress-value {{
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 5px;
}}

.progress-label {{
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.9;
}}

.notes-controls {{
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}}

.search-input {{
  flex: 1;
  min-width: 200px;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}}

.search-input:focus {{
  outline: none;
  border-color: #4a90e2;
}}

.filter-select {{
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}}

.papers-list {{
  display: grid;
  gap: 15px;
}}

.paper-card {{
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  transition: all 0.2s;
}}

.paper-card:hover {{
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}

.paper-header {{
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 15px;
  gap: 15px;
}}

.paper-title {{
  flex: 1;
}}

.paper-title a {{
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  text-decoration: none;
}}

.paper-title a:hover {{
  color: #4a90e2;
}}

.paper-meta {{
  color: #666;
  font-size: 14px;
  margin-top: 5px;
}}

.status-selector {{
  display: flex;
  gap: 5px;
}}

.status-btn {{
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: all 0.2s;
}}

.status-btn:hover {{
  background: #f0f0f0;
}}

.status-btn.active {{
  background: #4a90e2;
  color: white;
  border-color: #4a90e2;
}}

.status-btn.to-read.active {{
  background: #ffc107;
  border-color: #ffc107;
  color: #000;
}}

.status-btn.reading.active {{
  background: #17a2b8;
  border-color: #17a2b8;
}}

.status-btn.read.active {{
  background: #28a745;
  border-color: #28a745;
}}

.notes-section {{
  margin-top: 15px;
}}

.notes-textarea {{
  width: 100%;
  min-height: 100px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-family: inherit;
  font-size: 14px;
  resize: vertical;
}}

.notes-textarea:focus {{
  outline: none;
  border-color: #4a90e2;
}}

.notes-saved {{
  color: #28a745;
  font-size: 12px;
  margin-top: 5px;
  opacity: 0;
  transition: opacity 0.3s;
}}

.notes-saved.show {{
  opacity: 1;
}}

.topic-tag {{
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-top: 8px;
}}
</style>

<script>
const papers = {json.dumps(papers, indent=2)};

function loadNotes() {{
  return JSON.parse(localStorage.getItem('paperNotes') || '{{}}');
}}

function saveNotes(notes) {{
  localStorage.setItem('paperNotes', JSON.stringify(notes));
}}

function updateProgressSummary() {{
  const notes = loadNotes();
  const statuses = Object.values(notes).map(n => n.status).filter(s => s);
  
  document.getElementById('toReadCount').textContent = statuses.filter(s => s === 'to-read').length;
  document.getElementById('readingCount').textContent = statuses.filter(s => s === 'reading').length;
  document.getElementById('readCount').textContent = statuses.filter(s => s === 'read').length;
  document.getElementById('notesCount').textContent = Object.values(notes).filter(n => n.notes && n.notes.trim()).length;
}}

function renderPapers() {{
  const searchTerm = document.getElementById('paperSearch').value.toLowerCase();
  const statusFilter = document.getElementById('statusFilter').value;
  const hasNotesFilter = document.getElementById('hasNotesFilter').value;
  const notes = loadNotes();
  
  let filtered = papers.filter(paper => {{
    const matchesSearch = !searchTerm || 
      paper.title.toLowerCase().includes(searchTerm) ||
      paper.authors.toLowerCase().includes(searchTerm);
    
    const paperNotes = notes[paper.arxiv_id] || {{}};
    const matchesStatus = !statusFilter || paperNotes.status === statusFilter;
    const hasNotes = paperNotes.notes && paperNotes.notes.trim();
    const matchesNotes = !hasNotesFilter || 
      (hasNotesFilter === 'yes' && hasNotes) ||
      (hasNotesFilter === 'no' && !hasNotes);
    
    return matchesSearch && matchesStatus && matchesNotes;
  }});
  
  const container = document.getElementById('papersList');
  
  if (filtered.length === 0) {{
    container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">No papers found.</p>';
    return;
  }}
  
  container.innerHTML = filtered.map(paper => {{
    const paperNotes = notes[paper.arxiv_id] || {{}};
    const status = paperNotes.status || '';
    const noteText = paperNotes.notes || '';
    
    return `
      <div class="paper-card" data-arxiv-id="${{paper.arxiv_id}}">
        <div class="paper-header">
          <div class="paper-title">
            <a href="${{paper.url}}" target="_blank">${{paper.title}}</a>
            <div class="paper-meta">${{paper.authors}} • ${{paper.date}}</div>
            <div>
              ${{paper.topics.map(t => `<span class="topic-tag">${{t}}</span>`).join('')}}
            </div>
          </div>
          <div class="status-selector">
            <button class="status-btn to-read ${{status === 'to-read' ? 'active' : ''}}" data-status="to-read">To Read</button>
            <button class="status-btn reading ${{status === 'reading' ? 'active' : ''}}" data-status="reading">Reading</button>
            <button class="status-btn read ${{status === 'read' ? 'active' : ''}}" data-status="read">Read</button>
          </div>
        </div>
        <div class="notes-section">
          <textarea class="notes-textarea" placeholder="Add your notes, thoughts, or key takeaways...">${{noteText}}</textarea>
          <div class="notes-saved">✓ Saved</div>
        </div>
      </div>
    `;
  }}).join('');
  
  // Attach event listeners
  document.querySelectorAll('.status-btn').forEach(btn => {{
    btn.addEventListener('click', function() {{
      const card = this.closest('.paper-card');
      const arxivId = card.dataset.arxivId;
      const status = this.dataset.status;
      
      // Update UI
      card.querySelectorAll('.status-btn').forEach(b => b.classList.remove('active'));
      if (card.querySelector(`[data-status="${{status}}"]`).classList.contains('active')) {{
        // Deselect if clicking same button
        this.classList.remove('active');
        updatePaperStatus(arxivId, '');
      }} else {{
        this.classList.add('active');
        updatePaperStatus(arxivId, status);
      }}
    }});
  }});
  
  document.querySelectorAll('.notes-textarea').forEach(textarea => {{
    let timeout;
    textarea.addEventListener('input', function() {{
      const card = this.closest('.paper-card');
      const arxivId = card.dataset.arxivId;
      const savedMsg = card.querySelector('.notes-saved');
      
      clearTimeout(timeout);
      timeout = setTimeout(() => {{
        updatePaperNotes(arxivId, this.value);
        savedMsg.classList.add('show');
        setTimeout(() => savedMsg.classList.remove('show'), 2000);
        updateProgressSummary();
      }}, 500);
    }});
  }});
}}

function updatePaperStatus(arxivId, status) {{
  const notes = loadNotes();
  if (!notes[arxivId]) notes[arxivId] = {{}};
  notes[arxivId].status = status;
  saveNotes(notes);
  updateProgressSummary();
}}

function updatePaperNotes(arxivId, noteText) {{
  const notes = loadNotes();
  if (!notes[arxivId]) notes[arxivId] = {{}};
  notes[arxivId].notes = noteText;
  saveNotes(notes);
}}

function exportNotes() {{
  const notes = loadNotes();
  const data = {{
    exportDate: new Date().toISOString(),
    notes: notes
  }};
  
  const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `paper-notes-${{new Date().toISOString().split('T')[0]}}.json`;
  a.click();
  URL.revokeObjectURL(url);
}}

function importNotes(file) {{
  const reader = new FileReader();
  reader.onload = function(e) {{
    try {{
      const data = JSON.parse(e.target.result);
      if (data.notes) {{
        const existing = loadNotes();
        const merged = {{...existing, ...data.notes}};
        saveNotes(merged);
        renderPapers();
        updateProgressSummary();
        alert('Notes imported successfully!');
      }} else {{
        alert('Invalid file format');
      }}
    }} catch (err) {{
      alert('Error importing file: ' + err.message);
    }}
  }};
  reader.readAsText(file);
}}

document.getElementById('exportNotesBtn').addEventListener('click', exportNotes);
document.getElementById('importNotesBtn').addEventListener('click', () => {{
  document.getElementById('importFile').click();
}});
document.getElementById('importFile').addEventListener('change', (e) => {{
  if (e.target.files.length > 0) {{
    importNotes(e.target.files[0]);
  }}
}});

document.getElementById('paperSearch').addEventListener('input', renderPapers);
document.getElementById('statusFilter').addEventListener('change', renderPapers);
document.getElementById('hasNotesFilter').addEventListener('change', renderPapers);

renderPapers();
updateProgressSummary();
</script>
'''
    
    return page

def main():
    papers = parse_papers()
    page_content = generate_page(papers)
    Path('notes.md').write_text(page_content)
    print(f"Generated notes page for {len(papers)} papers")

if __name__ == '__main__':
    main()
