---
title: "Research Workspace"
---

<div class="workspace-container">
<!-- Top Bar -->
<div class="workspace-topbar">
<div class="topbar-left">
<h1>🔬 Research Workspace</h1>
<div class="workspace-stats">
<span class="stat-pill">📚 <span id="totalPapers">0</span> Papers</span>
<span class="stat-pill">📖 <span id="readingNow">0</span> Reading</span>
<span class="stat-pill">✅ <span id="completed">0</span> Completed</span>
<span class="stat-pill">💡 <span id="insightsCount">0</span> Insights</span>
</div>
</div>
<div class="topbar-right">
<button id="focusModeBtn" class="btn-icon" title="Focus Mode (Ctrl+F)">🎯</button>
<button id="quickAddBtn" class="btn-icon" title="Quick Add (Ctrl+N)">➕</button>
<button id="searchBtn" class="btn-icon" title="Search (Ctrl+K)">🔍</button>
<button id="settingsBtn" class="btn-icon" title="Settings">⚙️</button>
</div>
</div>

<!-- Main Workspace Grid -->
<div class="workspace-grid">
<!-- Left Panel: Discovery & Reading -->
<div class="workspace-panel panel-discovery">
<div class="panel-header">
<h2>📖 Reading Queue</h2>
<div class="panel-actions">
<button class="btn-sm" onclick="showAllPapers()">View All</button>
</div>
</div>
<div class="panel-content">
<div class="reading-tabs">
<button class="tab-btn active" data-tab="queue">Queue</button>
<button class="tab-btn" data-tab="reading">Reading Now</button>
<button class="tab-btn" data-tab="completed">Completed</button>
</div>
<div id="readingList" class="reading-list"></div>
</div>
</div>

<!-- Center Panel: Active Paper -->
<div class="workspace-panel panel-active">
<div class="panel-header">
<h2>📄 Active Paper</h2>
<div class="panel-actions">
<button class="btn-sm" onclick="markAsRead()">✓ Mark Read</button>
<button class="btn-sm" onclick="openFullPaper()">🔗 Open</button>
</div>
</div>
<div class="panel-content">
<div id="activePaper" class="active-paper">
<div class="empty-state">
<div class="empty-icon">📄</div>
<p>Select a paper to start reading</p>
<div class="empty-hint">Pick a paper from the Reading Queue on the left</div>
<div class="empty-action">
<button onclick="document.querySelector('[data-tab=queue]').click()">Browse Papers</button>
</div>
</div>
</div>
</div>
</div>

<!-- Right Panel: Insights & Notes -->
<div class="workspace-panel panel-insights">
<div class="panel-header">
<h2>💡 Insights & Notes</h2>
<div class="panel-actions">
<button class="btn-sm" onclick="addQuickNote()">+ Note</button>
</div>
</div>
<div class="panel-content">
<div class="insights-tabs">
<button class="tab-btn active" data-tab="highlights">Highlights</button>
<button class="tab-btn" data-tab="questions">Questions</button>
<button class="tab-btn" data-tab="takeaways">Takeaways</button>
</div>
<div id="insightsList" class="insights-list"></div>
</div>
</div>
</div>

<!-- Bottom Panel: Progress & Goals -->
<div class="workspace-bottom">
<div class="progress-section">
<h3>📊 Today's Progress</h3>
<div class="progress-bars">
<div class="progress-item">
<label>Reading Goal</label>
<div class="progress-bar">
<div class="progress-fill" id="readingProgress" style="width: 0%"></div>
</div>
<span class="progress-text" id="readingGoalText">0/0 papers</span>
</div>
<div class="progress-item">
<label>Notes Added</label>
<div class="progress-bar">
<div class="progress-fill" id="notesProgress" style="width: 0%"></div>
</div>
<span class="progress-text" id="notesGoalText">0 notes</span>
</div>
</div>
</div>
<div class="quick-actions-section">
<h3>⚡ Quick Actions</h3>
<div class="quick-actions">
<button class="action-btn" onclick="fetchNewPapers()">
<span class="action-icon">📥</span>
<span>Fetch New Papers</span>
</button>
<button class="action-btn" onclick="generateDigest()">
<span class="action-icon">📰</span>
<span>Generate Digest</span>
</button>
<button class="action-btn" onclick="exportData()">
<span class="action-icon">💾</span>
<span>Export Data</span>
</button>
<button class="action-btn" onclick="viewTimeline()">
<span class="action-icon">📅</span>
<span>View Timeline</span>
</button>
</div>
</div>
</div>
</div>

<!-- Quick Add Modal -->
<div id="quickAddModal" class="modal" style="display: none;">
<div class="modal-content modal-sm">
<div class="modal-header">
<h3>Quick Add</h3>
<button class="close-btn" onclick="closeQuickAdd()">&times;</button>
</div>
<div class="modal-body">
<div class="quick-add-options">
<button class="quick-add-btn" onclick="addHighlight()">
<span>✨</span> Add Highlight
</button>
<button class="quick-add-btn" onclick="addQuestion()">
<span>❓</span> Add Question
</button>
<button class="quick-add-btn" onclick="addTakeaway()">
<span>💡</span> Add Takeaway
</button>
<button class="quick-add-btn" onclick="addMilestone()">
<span>🎯</span> Add Milestone
</button>
</div>
</div>
</div>
</div>

<!-- Search Modal -->
<div id="searchModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<input type="text" id="globalSearch" placeholder="Search papers, notes, highlights..." class="search-input-large">
<button class="close-btn" onclick="closeSearch()">&times;</button>
</div>
<div class="modal-body">
<div id="searchResults" class="search-results"></div>
</div>
</div>
</div>

<style>
/* Override Quarto's default content margins */
main.content, #quarto-document-content {
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}

.workspace-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 100px);
  background: #f5f7fa;
  padding: 0.5rem;
  gap: 0.75rem;
  margin: 0;
  max-width: 100%;
}

/* Top Bar */
.workspace-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.topbar-left h1 {
  margin: 0;
  font-size: 1.5rem;
  color: #2c3e50;
}

.workspace-stats {
  display: flex;
  gap: 1rem;
}

.stat-pill {
  background: #f0f4f8;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  color: #555;
  font-weight: 500;
}

.topbar-right {
  display: flex;
  gap: 0.5rem;
}

.btn-icon {
  width: 40px;
  height: 40px;
  border: none;
  background: #f0f4f8;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.2rem;
  transition: all 0.2s;
}

.btn-icon:hover {
  background: #e0e8f0;
  transform: translateY(-2px);
}

/* Main Grid */
.workspace-grid {
  display: grid;
  grid-template-columns: 300px 1fr 350px;
  gap: 1rem;
  flex: 1;
  min-height: 0;
}

.workspace-panel {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e0e0e0;
  background: #fafbfc;
}

.panel-header h2 {
  margin: 0;
  font-size: 1.1rem;
  color: #2c3e50;
}

.panel-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-sm {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
  min-height: 36px;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}

.btn-sm:hover {
  background: #f0f4f8;
  border-color: #2c5aa0;
  transform: translateY(-1px);
}

.btn-sm:active {
  transform: translateY(0);
}

.panel-content {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

/* Tabs */
.reading-tabs, .insights-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid #e0e0e0;
}

.tab-btn {
  padding: 0.6rem 1rem;
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 0.9rem;
  color: #666;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: all 0.2s;
}

.tab-btn:hover {
  color: #2c5aa0;
}

.tab-btn.active {
  color: #2c5aa0;
  border-bottom-color: #2c5aa0;
  font-weight: 600;
}

/* Reading List */
.reading-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.reading-item {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  border-left: 3px solid #2c5aa0;
  position: relative;
}

.reading-item:hover {
  background: #f0f4f8;
  transform: translateX(4px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.reading-item.selected {
  background: #e3f2fd;
  border-left-color: #1976d2;
  box-shadow: 0 2px 8px rgba(25, 118, 210, 0.2);
}

.reading-item.reading {
  border-left-color: #f39c12;
}

.reading-item.completed {
  border-left-color: #27ae60;
  opacity: 0.7;
}

.reading-item-status {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  font-size: 0.75rem;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  background: rgba(255,255,255,0.9);
}

.reading-item-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.3rem;
  font-size: 0.95rem;
  line-height: 1.4;
  padding-right: 4rem;
}

.reading-item-meta {
  font-size: 0.8rem;
  color: #666;
}

/* Active Paper */
.active-paper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.active-paper-header {
  padding-bottom: 1rem;
  border-bottom: 1px solid #e0e0e0;
}

.active-paper-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.active-paper-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: #666;
  flex-wrap: wrap;
}

.active-paper-abstract {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  line-height: 1.6;
  color: #555;
}

.active-paper-actions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.action-btn-sm {
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.action-btn-sm:hover {
  background: #2c5aa0;
  color: white;
  border-color: #2c5aa0;
}

/* Insights List */
.insights-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.insight-item {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 3px solid #3498db;
}

.insight-item.highlight {
  border-left-color: #f39c12;
}

.insight-item.question {
  border-left-color: #e74c3c;
}

.insight-item.takeaway {
  border-left-color: #27ae60;
}

.insight-type {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 0.3rem;
  font-weight: 600;
}

.insight-text {
  color: #2c3e50;
  line-height: 1.5;
  font-size: 0.95rem;
}

.insight-paper {
  font-size: 0.8rem;
  color: #666;
  margin-top: 0.5rem;
  font-style: italic;
}

/* Bottom Section */
.workspace-bottom {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.progress-section h3, .quick-actions-section h3 {
  margin: 0 0 1rem 0;
  font-size: 1rem;
  color: #2c3e50;
}

.progress-bars {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.progress-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.progress-item label {
  font-size: 0.9rem;
  color: #666;
}

.progress-bar {
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #2c5aa0, #4a90e2);
  transition: width 0.3s;
}

.progress-text {
  font-size: 0.85rem;
  color: #666;
}

.quick-actions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

.action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn:hover {
  background: #f0f4f8;
  border-color: #2c5aa0;
  transform: translateY(-2px);
}

.action-icon {
  font-size: 1.5rem;
}

.action-btn span:last-child {
  font-size: 0.85rem;
  color: #555;
}

/* Modals */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  max-width: 600px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-sm {
  max-width: 400px;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #999;
}

.close-btn:hover {
  color: #333;
}

.modal-body {
  padding: 1.5rem;
}

.quick-add-options {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.quick-add-btn {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 1rem;
}

.quick-add-btn:hover {
  background: #f0f4f8;
  border-color: #2c5aa0;
}

.quick-add-btn span:first-child {
  font-size: 1.5rem;
}

.search-input-large {
  width: 100%;
  padding: 1rem;
  border: none;
  font-size: 1.1rem;
  outline: none;
}

.search-results {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.empty-state {
  text-align: center;
  padding: 3rem 1rem;
  color: #999;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.empty-state p {
  margin: 0.5rem 0;
  font-size: 0.95rem;
}

.empty-state .empty-hint {
  font-size: 0.85rem;
  color: #aaa;
  margin-top: 1rem;
}

.empty-state .empty-action {
  margin-top: 1.5rem;
}

.empty-state .empty-action button {
  padding: 0.6rem 1.2rem;
  background: #2c5aa0;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.empty-state .empty-action button:hover {
  background: #1e4a8a;
  transform: translateY(-1px);
}

/* Responsive */
@media (max-width: 1400px) {
  .workspace-grid {
    grid-template-columns: 280px 1fr 320px;
  }
}

@media (max-width: 1200px) {
  .workspace-grid {
    grid-template-columns: 250px 1fr 300px;
  }
  
  .workspace-stats {
    gap: 0.5rem;
  }
  
  .stat-pill {
    font-size: 0.8rem;
    padding: 0.4rem 0.8rem;
  }
}

@media (max-width: 900px) {
  .workspace-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto 1fr auto;
  }
  
  .workspace-bottom {
    grid-template-columns: 1fr;
  }
  
  .panel-discovery {
    max-height: 300px;
  }
  
  .panel-insights {
    max-height: 400px;
  }
  
  .workspace-topbar {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .topbar-left {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .topbar-right {
    justify-content: space-between;
  }
}

@media (max-width: 600px) {
  .workspace-container {
    padding: 0.5rem;
    gap: 0.5rem;
  }
  
  .workspace-topbar {
    padding: 0.75rem;
  }
  
  .topbar-left h1 {
    font-size: 1.2rem;
  }
  
  .workspace-stats {
    flex-wrap: wrap;
  }
  
  .stat-pill {
    font-size: 0.75rem;
    padding: 0.3rem 0.6rem;
  }
  
  .panel-header {
    padding: 0.75rem 1rem;
  }
  
  .panel-header h2 {
    font-size: 1rem;
  }
  
  .btn-sm {
    font-size: 0.8rem;
    padding: 0.3rem 0.6rem;
  }
  
  .quick-actions {
    grid-template-columns: 1fr;
  }
}

/* Focus Mode */
body.focus-mode .panel-discovery,
body.focus-mode .panel-insights,
body.focus-mode .workspace-bottom {
  display: none;
}

body.focus-mode .workspace-grid {
  grid-template-columns: 1fr;
}

body.focus-mode .panel-active {
  max-width: 900px;
  margin: 0 auto;
  width: 100%;
}

body.focus-mode .workspace-topbar {
  justify-content: center;
}

body.focus-mode .topbar-left {
  display: none;
}
</style>

<script>
let allPapers = [];
let userData = null;
let currentTab = 'queue';
let currentInsightTab = 'highlights';
let selectedPaperId = null;
let searchTimeout = null;

async function loadWorkspaceData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    userData = await userResponse.json();
    
    updateStats();
    renderReadingList();
    renderInsights();
    updateProgress();
    
    // Auto-select first paper if available
    const firstPaper = getFilteredPapers()[0];
    if (firstPaper) {
      selectPaper(firstPaper.arxiv_id);
    }
  } catch (error) {
    console.error('Error loading workspace data:', error);
  }
}

function getFilteredPapers() {
  const bookmarks = userData.bookmarks || [];
  const readingProgress = userData.readingProgress || {};
  
  let papers = bookmarks.map(id => {
    const paper = allPapers.find(p => p.arxiv_id === id);
    const progress = readingProgress[id];
    return { ...paper, status: progress?.status || 'queue' };
  });
  
  // Filter by tab
  if (currentTab === 'queue') {
    papers = papers.filter(p => p.status === 'queue' || !p.status);
  } else if (currentTab === 'reading') {
    papers = papers.filter(p => p.status === 'reading');
  } else if (currentTab === 'completed') {
    papers = papers.filter(p => p.status === 'read');
  }
  
  return papers;
}

function updateStats() {
  const bookmarks = userData.bookmarks || [];
  const readingProgress = userData.readingProgress || {};
  const highlights = userData.highlights || [];
  const questions = userData.questions || [];
  const takeaways = userData.takeaways || [];
  
  document.getElementById('totalPapers').textContent = allPapers.length;
  document.getElementById('readingNow').textContent = Object.values(readingProgress).filter(p => p.status === 'reading').length;
  document.getElementById('completed').textContent = Object.values(readingProgress).filter(p => p.status === 'read').length;
  document.getElementById('insightsCount').textContent = highlights.length + questions.length + takeaways.length;
}

function renderReadingList() {
  const container = document.getElementById('readingList');
  const papers = getFilteredPapers();
  
  if (papers.length === 0) {
    container.innerHTML = '<div class="empty-state"><p>No papers in this category</p></div>';
    return;
  }
  
  container.innerHTML = papers.slice(0, 15).map(paper => {
    const isSelected = paper.arxiv_id === selectedPaperId;
    const statusLabel = paper.status === 'reading' ? '📖 Reading' : 
                       paper.status === 'read' ? '✅ Done' : '📋 Queue';
    
    return `
<div class="reading-item ${paper.status} ${isSelected ? 'selected' : ''}" 
           onclick="selectPaper('${paper.arxiv_id}')"
           data-paper-id="${paper.arxiv_id}">
<div class="reading-item-status">${statusLabel}</div>
<div class="reading-item-title">${paper.title}</div>
<div class="reading-item-meta">${paper.date} • ${paper.authors.split(',')[0]}</div>
</div>
    `;
  }).join('');
}

function selectPaper(arxivId) {
  selectedPaperId = arxivId;
  const paper = allPapers.find(p => p.arxiv_id === arxivId);
  if (!paper) return;
  
  // Update selection in list
  document.querySelectorAll('.reading-item').forEach(item => {
    item.classList.remove('selected');
  });
  const selectedItem = document.querySelector(`[data-paper-id="${arxivId}"]`);
  if (selectedItem) {
    selectedItem.classList.add('selected');
  }
  
  const readingProgress = userData.readingProgress || {};
  const progress = readingProgress[arxivId];
  const status = progress?.status || 'queue';
  
  const container = document.getElementById('activePaper');
  container.innerHTML = `
<div class="active-paper-header">
<div class="active-paper-title">${paper.title}</div>
<div class="active-paper-meta">
<span>📅 ${paper.date}</span>
<span>👥 ${paper.authors}</span>
<span>🏷️ ${(paper.topics || []).join(', ')}</span>
</div>
</div>
<div class="active-paper-abstract">
      ${paper.abstract || 'No abstract available'}
</div>
<div class="active-paper-actions">
<button class="action-btn-sm" onclick="addHighlightForPaper('${paper.arxiv_id}')">✨ Highlight</button>
<button class="action-btn-sm" onclick="addQuestionForPaper('${paper.arxiv_id}')">❓ Question</button>
<button class="action-btn-sm" onclick="addTakeawayForPaper('${paper.arxiv_id}')">💡 Takeaway</button>
<button class="action-btn-sm" onclick="openPaperNotes('${paper.arxiv_id}')">📝 Notes</button>
<button class="action-btn-sm" onclick="changeReadingStatus('${paper.arxiv_id}', '${status}')">🔄 Status</button>
</div>
  `;
  
  // Render insights for this paper
  renderInsightsForPaper(arxivId);
}

function renderInsightsForPaper(arxivId) {
  const container = document.getElementById('insightsList');
  const highlights = (userData.highlights || []).filter(h => h.paperId === arxivId);
  const questions = (userData.questions || []).filter(q => q.paperId === arxivId);
  const takeaways = (userData.takeaways || []).filter(t => t.paperId === arxivId);
  
  let items = [];
  
  if (currentInsightTab === 'highlights') {
    items = highlights.map(h => ({ ...h, type: 'highlight' }));
  } else if (currentInsightTab === 'questions') {
    items = questions.map(q => ({ ...q, type: 'question' }));
  } else if (currentInsightTab === 'takeaways') {
    items = takeaways.map(t => ({ ...t, type: 'takeaway' }));
  }
  
  // Sort by date
  items.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
  
  if (items.length === 0) {
    container.innerHTML = '<div class="empty-state"><p>No insights for this paper yet</p></div>';
    return;
  }
  
  container.innerHTML = items.map(item => {
    const text = item.text || item.question || '';
    
    return `
<div class="insight-item ${item.type}">
<div class="insight-type">${item.type}</div>
<div class="insight-text">${text.substring(0, 200)}${text.length > 200 ? '...' : ''}</div>
</div>
    `;
  }).join('');
}

function renderInsights() {
  if (selectedPaperId) {
    renderInsightsForPaper(selectedPaperId);
  } else {
    // Show all insights
    const container = document.getElementById('insightsList');
    const highlights = userData.highlights || [];
    const questions = userData.questions || [];
    const takeaways = userData.takeaways || [];
    
    let items = [];
    
    if (currentInsightTab === 'highlights') {
      items = highlights.map(h => ({ ...h, type: 'highlight' }));
    } else if (currentInsightTab === 'questions') {
      items = questions.map(q => ({ ...q, type: 'question' }));
    } else if (currentInsightTab === 'takeaways') {
      items = takeaways.map(t => ({ ...t, type: 'takeaway' }));
    }
    
    // Sort by date
    items.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    
    if (items.length === 0) {
      container.innerHTML = '<div class="empty-state"><p>No insights yet</p></div>';
      return;
    }
    
    container.innerHTML = items.slice(0, 15).map(item => {
      const paper = allPapers.find(p => p.arxiv_id === item.paperId);
      const text = item.text || item.question || '';
      
      return `
<div class="insight-item ${item.type}">
<div class="insight-type">${item.type}</div>
<div class="insight-text">${text.substring(0, 150)}${text.length > 150 ? '...' : ''}</div>
          ${paper ? `<div class="insight-paper">${paper.title.substring(0, 60)}...</div>` : ''}
</div>
      `;
    }).join('');
  }
}

function updateProgress() {
  // Calculate progress based on goals (simplified for now)
  const readingGoal = 5; // papers per day
  const notesGoal = 3; // notes per day
  
  const today = new Date().toISOString().split('T')[0];
  const todayRead = Object.values(userData.readingProgress || {}).filter(p => 
    p.lastUpdated === today && p.status === 'read'
  ).length;
  
  const todayNotes = (userData.highlights || []).filter(h => 
    h.createdAt.startsWith(today)
  ).length + (userData.questions || []).filter(q => 
    q.createdAt.startsWith(today)
  ).length + (userData.takeaways || []).filter(t => 
    t.createdAt.startsWith(today)
  ).length;
  
  const readingPercent = Math.min(100, (todayRead / readingGoal) * 100);
  const notesPercent = Math.min(100, (todayNotes / notesGoal) * 100);
  
  document.getElementById('readingProgress').style.width = readingPercent + '%';
  document.getElementById('notesProgress').style.width = notesPercent + '%';
  document.getElementById('readingGoalText').textContent = `${todayRead}/${readingGoal} papers`;
  document.getElementById('notesGoalText').textContent = `${todayNotes} notes`;
}

// Quick actions for active paper
function addHighlightForPaper(arxivId) {
  window.location.href = `highlights.html?paper=${arxivId}`;
}

function addQuestionForPaper(arxivId) {
  window.location.href = `questions.html?paper=${arxivId}`;
}

function addTakeawayForPaper(arxivId) {
  window.location.href = `takeaways.html?paper=${arxivId}`;
}

function openPaperNotes(arxivId) {
  window.location.href = `notes.html?paper=${arxivId}`;
}

function changeReadingStatus(arxivId, currentStatus) {
  const nextStatus = currentStatus === 'queue' ? 'reading' : 
                     currentStatus === 'reading' ? 'read' : 'queue';
  
  if (!userData.readingProgress) {
    userData.readingProgress = {};
  }
  
  userData.readingProgress[arxivId] = {
    status: nextStatus,
    lastUpdated: new Date().toISOString().split('T')[0]
  };
  
  // Save to API
  fetch(`${API_BASE}/api/user/data`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  }).then(() => {
    updateStats();
    renderReadingList();
    selectPaper(arxivId);
  });
}

// Global search
function performSearch(query) {
  if (!query || query.length < 2) {
    document.getElementById('searchResults').innerHTML = '';
    return;
  }
  
  const lowerQuery = query.toLowerCase();
  const results = allPapers.filter(p => 
    p.title.toLowerCase().includes(lowerQuery) ||
    p.authors.toLowerCase().includes(lowerQuery) ||
    (p.abstract && p.abstract.toLowerCase().includes(lowerQuery))
  ).slice(0, 10);
  
  if (results.length === 0) {
    document.getElementById('searchResults').innerHTML = '<div class="empty-state"><p>No results found</p></div>';
    return;
  }
  
  document.getElementById('searchResults').innerHTML = results.map(paper => `
<div class="reading-item" onclick="selectPaper('${paper.arxiv_id}'); closeSearch();">
<div class="reading-item-title">${paper.title}</div>
<div class="reading-item-meta">${paper.date} • ${paper.authors.split(',')[0]}</div>
</div>
  `).join('');
}

// Tab switching
document.querySelectorAll('.reading-tabs .tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.reading-tabs .tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentTab = btn.dataset.tab;
    renderReadingList();
  });
});

document.querySelectorAll('.insights-tabs .tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.insights-tabs .tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentInsightTab = btn.dataset.tab;
    renderInsights();
  });
});

// Quick actions
function openQuickAdd() {
  document.getElementById('quickAddModal').style.display = 'flex';
}

function closeQuickAdd() {
  document.getElementById('quickAddModal').style.display = 'none';
}

function openSearch() {
  document.getElementById('searchModal').style.display = 'flex';
  document.getElementById('globalSearch').focus();
}

function closeSearch() {
  document.getElementById('searchModal').style.display = 'none';
  document.getElementById('globalSearch').value = '';
  document.getElementById('searchResults').innerHTML = '';
}

// Focus mode
let isFocusMode = false;

function toggleFocusMode() {
  isFocusMode = !isFocusMode;
  
  if (isFocusMode) {
    document.body.classList.add('focus-mode');
    document.getElementById('focusModeBtn').textContent = '🔓';
    document.getElementById('focusModeBtn').title = 'Exit Focus Mode (Ctrl+F)';
  } else {
    document.body.classList.remove('focus-mode');
    document.getElementById('focusModeBtn').textContent = '🎯';
    document.getElementById('focusModeBtn').title = 'Focus Mode (Ctrl+F)';
  }
}

document.getElementById('focusModeBtn').addEventListener('click', toggleFocusMode);

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey || e.metaKey) {
    if (e.key === 'n') {
      e.preventDefault();
      openQuickAdd();
    } else if (e.key === 'k') {
      e.preventDefault();
      openSearch();
    } else if (e.key === 'f') {
      e.preventDefault();
      toggleFocusMode();
    }
  } else if (e.key === 'Escape') {
    closeQuickAdd();
    closeSearch();
    if (isFocusMode) {
      toggleFocusMode();
    }
  }
});

document.getElementById('quickAddBtn').addEventListener('click', openQuickAdd);
document.getElementById('searchBtn').addEventListener('click', openSearch);

// Search input handler
document.getElementById('globalSearch').addEventListener('input', (e) => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    performSearch(e.target.value);
  }, 300);
});

// Quick add actions
function addHighlight() {
  closeQuickAdd();
  window.location.href = 'highlights.html';
}

function addQuestion() {
  closeQuickAdd();
  window.location.href = 'questions.html';
}

function addTakeaway() {
  closeQuickAdd();
  window.location.href = 'takeaways.html';
}

function addMilestone() {
  closeQuickAdd();
  window.location.href = 'timeline.html';
}

// Bottom panel actions
function fetchNewPapers() {
  alert('Fetching new papers... This will run the fetch_arxiv.py script.');
}

function generateDigest() {
  window.location.href = 'digests/index.html';
}

function exportData() {
  window.location.href = 'export-import.html';
}

function viewTimeline() {
  window.location.href = 'timeline.html';
}

// Initialize
loadWorkspaceData();
</script>
