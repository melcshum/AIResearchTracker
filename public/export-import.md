---
title: "Export & Import"
---

# 💾 Export & Import Data

Backup your research data, share curated lists, or import from other systems.

<div class="export-import-container">
  <div class="section">
    <h2>📤 Export Your Data</h2>
    <p>Download your bookmarks, notes, summaries, and reading progress in various formats.</p>
    
    <div class="export-options">
      <div class="export-card">
        <div class="export-icon">📋</div>
        <h3>Export Bookmarks</h3>
        <p>Export all your bookmarked papers with metadata</p>
        <div class="export-buttons">
          <button onclick="exportBookmarks('json')" class="btn-primary">JSON</button>
          <button onclick="exportBookmarks('csv')" class="btn-secondary">CSV</button>
          <button onclick="exportBookmarks('markdown')" class="btn-secondary">Markdown</button>
        </div>
      </div>
      
      <div class="export-card">
        <div class="export-icon">📝</div>
        <h3>Export Notes</h3>
        <p>Export all your paper notes and annotations</p>
        <div class="export-buttons">
          <button onclick="exportNotes('json')" class="btn-primary">JSON</button>
          <button onclick="exportNotes('markdown')" class="btn-secondary">Markdown</button>
        </div>
      </div>
      
      <div class="export-card">
        <div class="export-icon">🤖</div>
        <h3>Export AI Summaries</h3>
        <p>Export all AI-generated paper summaries</p>
        <div class="export-buttons">
          <button onclick="exportSummaries('json')" class="btn-primary">JSON</button>
          <button onclick="exportSummaries('markdown')" class="btn-secondary">Markdown</button>
        </div>
      </div>
      
      <div class="export-card">
        <div class="export-icon">📊</div>
        <h3>Export Reading Progress</h3>
        <p>Export your reading status and progress tracking</p>
        <div class="export-buttons">
          <button onclick="exportProgress('json')" class="btn-primary">JSON</button>
          <button onclick="exportProgress('csv')" class="btn-secondary">CSV</button>
        </div>
      </div>
      
      <div class="export-card full-width">
        <div class="export-icon">💾</div>
        <h3>Export Complete Backup</h3>
        <p>Export everything: bookmarks, notes, summaries, progress, and topics</p>
        <div class="export-buttons">
          <button onclick="exportCompleteBackup()" class="btn-primary">Download Full Backup (JSON)</button>
        </div>
      </div>
    </div>
  </div>
  
  <div class="section">
    <h2>📥 Import Data</h2>
    <p>Import data from a backup file or from other systems.</p>
    
    <div class="import-options">
      <div class="import-card">
        <div class="import-icon">💾</div>
        <h3>Import Complete Backup</h3>
        <p>Restore from a complete backup file</p>
        <input type="file" id="importBackup" accept=".json" onchange="importCompleteBackup(event)" class="file-input">
        <label for="importBackup" class="file-label">Choose File</label>
      </div>
      
      <div class="import-card">
        <div class="import-icon">📋</div>
        <h3>Import Bookmarks</h3>
        <p>Import bookmarks from JSON or CSV file</p>
        <input type="file" id="importBookmarks" accept=".json,.csv" onchange="importBookmarks(event)" class="file-input">
        <label for="importBookmarks" class="file-label">Choose File</label>
      </div>
      
      <div class="import-card">
        <div class="import-icon">📝</div>
        <h3>Import Notes</h3>
        <p>Import notes from JSON or Markdown file</p>
        <input type="file" id="importNotes" accept=".json,.md" onchange="importNotes(event)" class="file-input">
        <label for="importNotes" class="file-label">Choose File</label>
      </div>
    </div>
  </div>
  
  <div class="section">
    <h2>🔗 Integration Options</h2>
    <p>Export data in formats compatible with popular research tools.</p>
    
    <div class="integration-options">
      <div class="integration-card">
        <div class="integration-icon">📚</div>
        <h3>Zotero Export</h3>
        <p>Export bookmarks in BibTeX format for Zotero</p>
        <button onclick="exportToZotero()" class="btn-secondary">Export BibTeX</button>
      </div>
      
      <div class="integration-card">
        <div class="integration-icon">📓</div>
        <h3>Notion Export</h3>
        <p>Export data in Notion-compatible format</p>
        <button onclick="exportToNotion()" class="btn-secondary">Export for Notion</button>
      </div>
      
      <div class="integration-card">
        <div class="integration-icon">📊</div>
        <h3>Spreadsheet Export</h3>
        <p>Export all data as CSV for Excel/Google Sheets</p>
        <button onclick="exportToSpreadsheet()" class="btn-secondary">Export CSV</button>
      </div>
    </div>
  </div>
</div>

<style>
.export-import-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.section h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.section p {
  color: #666;
  margin-bottom: 2rem;
}

.export-options, .import-options, .integration-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.export-card, .import-card, .integration-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border: 2px solid #e0e0e0;
  transition: all 0.2s;
}

.export-card:hover, .import-card:hover, .integration-card:hover {
  border-color: #2c5aa0;
  box-shadow: 0 4px 12px rgba(44, 90, 160, 0.1);
}

.export-card.full-width {
  grid-column: 1 / -1;
}

.export-icon, .import-icon, .integration-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.export-card h3, .import-card h3, .integration-card h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.export-card p, .import-card p, .integration-card p {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.export-buttons {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.btn-primary, .btn-secondary {
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
  font-size: 0.9rem;
}

.btn-primary {
  background: #2c5aa0;
  color: white;
}

.btn-primary:hover {
  background: #1e4a8f;
}

.btn-secondary {
  background: #e0e0e0;
  color: #2c3e50;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.file-input {
  display: none;
}

.file-label {
  display: inline-block;
  padding: 0.6rem 1.2rem;
  background: #2c5aa0;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
  font-size: 0.9rem;
}

.file-label:hover {
  background: #1e4a8f;
}

.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 1rem 1.5rem;
  background: #4caf50;
  color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  z-index: 10000;
  animation: slideIn 0.3s ease-out;
}

.notification.error {
  background: #f44336;
}

@keyframes slideIn {
  from {
    transform: translateX(400px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
</style>

<script>
let userData = null;
let allPapers = [];

async function loadUserData() {
  try {
    const response = await fetch('http://localhost:5001/api/user/data');
    userData = await response.json();
    
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
  } catch (error) {
    console.error('Error loading data:', error);
    showNotification('Error loading data', 'error');
  }
}

function showNotification(message, type = 'success') {
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.remove();
  }, 3000);
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// Export Functions
function exportBookmarks(format) {
  if (!userData || !userData.bookmarks) {
    showNotification('No bookmarks to export', 'error');
    return;
  }
  
  const bookmarkedPapers = allPapers.filter(p => userData.bookmarks.includes(p.arxiv_id));
  
  if (format === 'json') {
    const data = JSON.stringify(bookmarkedPapers, null, 2);
    downloadFile(data, 'bookmarks.json', 'application/json');
  } else if (format === 'csv') {
    const headers = ['arxiv_id', 'title', 'authors', 'date', 'topics', 'abstract'];
    const rows = bookmarkedPapers.map(p => [
      p.arxiv_id,
      `"${p.title.replace(/"/g, '""')}"`,
      `"${p.authors.replace(/"/g, '""')}"`,
      p.date,
      `"${(p.topics || []).join(', ')}"`,
      `"${(p.abstract || '').replace(/"/g, '""').substring(0, 200)}..."`
    ]);
    const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
    downloadFile(csv, 'bookmarks.csv', 'text/csv');
  } else if (format === 'markdown') {
    let md = '# My Bookmarked Papers\n\n';
    bookmarkedPapers.forEach(p => {
      md += `## ${p.title}\n\n`;
      md += `**Authors:** ${p.authors}\n\n`;
      md += `**Date:** ${p.date}\n\n`;
      md += `**Topics:** ${(p.topics || []).join(', ')}\n\n`;
      md += `**Abstract:** ${p.abstract || 'N/A'}\n\n`;
      md += `**Link:** [Read Paper](${p.url})\n\n---\n\n`;
    });
    downloadFile(md, 'bookmarks.md', 'text/markdown');
  }
  
  showNotification(`Exported ${bookmarkedPapers.length} bookmarks as ${format.toUpperCase()}`);
}

function exportNotes(format) {
  if (!userData || !userData.notes || Object.keys(userData.notes).length === 0) {
    showNotification('No notes to export', 'error');
    return;
  }
  
  if (format === 'json') {
    const data = JSON.stringify(userData.notes, null, 2);
    downloadFile(data, 'notes.json', 'application/json');
  } else if (format === 'markdown') {
    let md = '# My Paper Notes\n\n';
    Object.entries(userData.notes).forEach(([arxivId, note]) => {
      const paper = allPapers.find(p => p.arxiv_id === arxivId);
      if (paper) {
        md += `## ${paper.title}\n\n`;
        md += `**Authors:** ${paper.authors}\n\n`;
        md += `**Date:** ${paper.date}\n\n`;
        md += `### My Notes\n\n${note}\n\n---\n\n`;
      }
    });
    downloadFile(md, 'notes.md', 'text/markdown');
  }
  
  showNotification(`Exported ${Object.keys(userData.notes).length} notes as ${format.toUpperCase()}`);
}

function exportSummaries(format) {
  if (!userData || !userData.summaries || Object.keys(userData.summaries).length === 0) {
    showNotification('No summaries to export', 'error');
    return;
  }
  
  if (format === 'json') {
    const data = JSON.stringify(userData.summaries, null, 2);
    downloadFile(data, 'summaries.json', 'application/json');
  } else if (format === 'markdown') {
    let md = '# AI-Generated Paper Summaries\n\n';
    Object.entries(userData.summaries).forEach(([arxivId, summary]) => {
      const paper = allPapers.find(p => p.arxiv_id === arxivId);
      if (paper) {
        md += `## ${paper.title}\n\n`;
        md += `**Authors:** ${paper.authors}\n\n`;
        md += `**Date:** ${paper.date}\n\n`;
        md += `### Summary\n\n${summary}\n\n---\n\n`;
      }
    });
    downloadFile(md, 'summaries.md', 'text/markdown');
  }
  
  showNotification(`Exported ${Object.keys(userData.summaries).length} summaries as ${format.toUpperCase()}`);
}

function exportProgress(format) {
  if (!userData || !userData.readingProgress || Object.keys(userData.readingProgress).length === 0) {
    showNotification('No reading progress to export', 'error');
    return;
  }
  
  if (format === 'json') {
    const data = JSON.stringify(userData.readingProgress, null, 2);
    downloadFile(data, 'reading-progress.json', 'application/json');
  } else if (format === 'csv') {
    const headers = ['arxiv_id', 'title', 'status', 'progress', 'lastUpdated'];
    const rows = Object.entries(userData.readingProgress).map(([arxivId, progress]) => {
      const paper = allPapers.find(p => p.arxiv_id === arxivId);
      return [
        arxivId,
        `"${(paper?.title || 'Unknown').replace(/"/g, '""')}"`,
        progress.status || 'unread',
        progress.progress || 0,
        progress.lastUpdated || ''
      ];
    });
    const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
    downloadFile(csv, 'reading-progress.csv', 'text/csv');
  }
  
  showNotification(`Exported ${Object.keys(userData.readingProgress).length} progress records as ${format.toUpperCase()}`);
}

function exportCompleteBackup() {
  if (!userData) {
    showNotification('No data to export', 'error');
    return;
  }
  
  const backup = {
    version: '1.0',
    exportDate: new Date().toISOString(),
    bookmarks: userData.bookmarks || [],
    notes: userData.notes || {},
    summaries: userData.summaries || {},
    readingProgress: userData.readingProgress || {},
    topics: userData.topics || []
  };
  
  const data = JSON.stringify(backup, null, 2);
  const timestamp = new Date().toISOString().split('T')[0];
  downloadFile(data, `research-backup-${timestamp}.json`, 'application/json');
  
  showNotification('Complete backup exported successfully');
}

// Import Functions
async function importCompleteBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  
  try {
    const text = await file.text();
    const backup = JSON.parse(text);
    
    if (!backup.version || !backup.bookmarks) {
      throw new Error('Invalid backup file format');
    }
    
    // Merge with existing data
    const mergedData = {
      ...userData,
      bookmarks: [...new Set([...(userData.bookmarks || []), ...backup.bookmarks])],
      notes: { ...(userData.notes || {}), ...backup.notes },
      summaries: { ...(userData.summaries || {}), ...backup.summaries },
      readingProgress: { ...(userData.readingProgress || {}), ...backup.readingProgress }
    };
    
    // Save to API
    await fetch('http://localhost:5001/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(mergedData)
    });
    
    userData = mergedData;
    showNotification(`Imported backup: ${backup.bookmarks.length} bookmarks, ${Object.keys(backup.notes).length} notes`);
  } catch (error) {
    console.error('Import error:', error);
    showNotification('Error importing backup: ' + error.message, 'error');
  }
}

async function importBookmarks(event) {
  const file = event.target.files[0];
  if (!file) return;
  
  try {
    const text = await file.text();
    let bookmarks = [];
    
    if (file.name.endsWith('.json')) {
      const data = JSON.parse(text);
      bookmarks = Array.isArray(data) ? data.map(p => p.arxiv_id) : [];
    } else if (file.name.endsWith('.csv')) {
      const lines = text.split('\n').slice(1); // Skip header
      bookmarks = lines.map(line => line.split(',')[0]).filter(Boolean);
    }
    
    // Merge with existing bookmarks
    const mergedBookmarks = [...new Set([...(userData.bookmarks || []), ...bookmarks])];
    
    await fetch('http://localhost:5001/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...userData, bookmarks: mergedBookmarks })
    });
    
    userData.bookmarks = mergedBookmarks;
    showNotification(`Imported ${bookmarks.length} bookmarks`);
  } catch (error) {
    console.error('Import error:', error);
    showNotification('Error importing bookmarks: ' + error.message, 'error');
  }
}

async function importNotes(event) {
  const file = event.target.files[0];
  if (!file) return;
  
  try {
    const text = await file.text();
    let notes = {};
    
    if (file.name.endsWith('.json')) {
      notes = JSON.parse(text);
    } else if (file.name.endsWith('.md')) {
      // Parse markdown format
      const sections = text.split('## ').slice(1);
      sections.forEach(section => {
        const lines = section.split('\n');
        const title = lines[0];
        const paper = allPapers.find(p => p.title === title);
        if (paper) {
          const noteContent = section.split('### My Notes\n\n')[1]?.split('\n\n---')[0] || '';
          notes[paper.arxiv_id] = noteContent.trim();
        }
      });
    }
    
    // Merge with existing notes
    const mergedNotes = { ...(userData.notes || {}), ...notes };
    
    await fetch('http://localhost:5001/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...userData, notes: mergedNotes })
    });
    
    userData.notes = mergedNotes;
    showNotification(`Imported ${Object.keys(notes).length} notes`);
  } catch (error) {
    console.error('Import error:', error);
    showNotification('Error importing notes: ' + error.message, 'error');
  }
}

// Integration Exports
function exportToZotero() {
  if (!userData || !userData.bookmarks) {
    showNotification('No bookmarks to export', 'error');
    return;
  }
  
  const bookmarkedPapers = allPapers.filter(p => userData.bookmarks.includes(p.arxiv_id));
  
  let bibtex = '';
  bookmarkedPapers.forEach(p => {
    const key = p.arxiv_id.replace(/[^a-zA-Z0-9]/g, '');
    const authors = p.authors.split(',').map(a => a.trim()).join(' and ');
    const year = new Date(p.date).getFullYear();
    
    bibtex += `@article{${key},\n`;
    bibtex += `  title = {${p.title}},\n`;
    bibtex += `  author = {${authors}},\n`;
    bibtex += `  year = {${year}},\n`;
    bibtex += `  eprint = {${p.arxiv_id}},\n`;
    bibtex += `  archivePrefix = {arXiv},\n`;
    bibtex += `  url = {https://arxiv.org/abs/${p.arxiv_id}}\n`;
    bibtex += `}\n\n`;
  });
  
  downloadFile(bibtex, 'zotero-export.bib', 'application/x-bibtex');
  showNotification('Exported to BibTeX format for Zotero');
}

function exportToNotion() {
  if (!userData) {
    showNotification('No data to export', 'error');
    return;
  }
  
  const notionData = {
    bookmarks: userData.bookmarks || [],
    notes: userData.notes || {},
    summaries: userData.summaries || {},
    readingProgress: userData.readingProgress || {}
  };
  
  const data = JSON.stringify(notionData, null, 2);
  downloadFile(data, 'notion-import.json', 'application/json');
  showNotification('Exported for Notion import');
}

function exportToSpreadsheet() {
  if (!userData) {
    showNotification('No data to export', 'error');
    return;
  }
  
  const headers = ['arxiv_id', 'title', 'authors', 'date', 'topics', 'bookmarked', 'has_notes', 'has_summary', 'reading_status'];
  const rows = allPapers.map(p => {
    const isBookmarked = userData.bookmarks?.includes(p.arxiv_id) ? 'Yes' : 'No';
    const hasNotes = userData.notes?.[p.arxiv_id] ? 'Yes' : 'No';
    const hasSummary = userData.summaries?.[p.arxiv_id] ? 'Yes' : 'No';
    const status = userData.readingProgress?.[p.arxiv_id]?.status || 'unread';
    
    return [
      p.arxiv_id,
      `"${p.title.replace(/"/g, '""')}"`,
      `"${p.authors.replace(/"/g, '""')}"`,
      p.date,
      `"${(p.topics || []).join(', ')}"`,
      isBookmarked,
      hasNotes,
      hasSummary,
      status
    ];
  });
  
  const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
  downloadFile(csv, 'all-papers-data.csv', 'text/csv');
  showNotification('Exported all papers data to CSV');
}

// Initialize
loadUserData();
</script>
