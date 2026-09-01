---
title: "Paper Highlights"
---

# ✨ Paper Highlights

Extract and organize key insights, quotes, and important passages from your papers.

<div class="highlights-container">
<div class="highlights-header">
<button id="addHighlightBtn" class="btn-primary">+ Add Highlight</button>
<div class="highlights-stats">
<span class="stat">✨ <span id="totalHighlights">0</span> Highlights</span>
<span class="stat">📄 <span id="papersWithHighlights">0</span> Papers</span>
</div>
</div>

<div class="filter-bar">
<input type="text" id="searchHighlights" placeholder="Search highlights...">
<select id="filterByPaper">
<option value="all">All Papers</option>
</select>
<select id="sortBy">
<option value="date">Date Added</option>
<option value="paper">By Paper</option>
</select>
</div>

<div id="highlightsList" class="highlights-list"></div>
</div>

<!-- Add Highlight Modal -->
<div id="addHighlightModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Add Highlight</h2>
<button class="close-btn" onclick="closeAddModal()">&times;</button>
</div>
<div class="modal-body">
<div class="form-group">
<label>Paper</label>
<select id="highlightPaper" required>
<option value="">Select a paper...</option>
</select>
</div>
<div class="form-group">
<label>Highlight Text</label>
<textarea id="highlightText" placeholder="Paste or type the highlighted text..." rows="4" required></textarea>
</div>
<div class="form-group">
<label>Category</label>
<select id="highlightCategory">
<option value="key-insight">Key Insight</option>
<option value="quote">Quote</option>
<option value="methodology">Methodology</option>
<option value="result">Result</option>
<option value="question">Question</option>
<option value="connection">Connection to Other Work</option>
</select>
</div>
<div class="form-group">
<label>Personal Note (optional)</label>
<textarea id="highlightNote" placeholder="Your thoughts on this highlight..." rows="3"></textarea>
</div>
<div class="form-group">
<label>Tags (comma-separated)</label>
<input type="text" id="highlightTags" placeholder="e.g., important, methodology, follow-up">
</div>
</div>
<div class="modal-footer">
<button class="btn-secondary" onclick="closeAddModal()">Cancel</button>
<button class="btn-primary" onclick="saveHighlight()">Save Highlight</button>
</div>
</div>
</div>

<!-- Highlight Detail Modal -->
<div id="highlightDetailModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Highlight Details</h2>
<button class="close-btn" onclick="closeDetailModal()">&times;</button>
</div>
<div class="modal-body" id="highlightDetailContent"></div>
<div class="modal-footer">
<button class="btn-danger" onclick="deleteHighlight()">Delete</button>
<button class="btn-secondary" onclick="closeDetailModal()">Close</button>
</div>
</div>
</div>

<style>
.highlights-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.highlights-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.highlights-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  font-size: 1rem;
  color: #666;
}

.filter-bar {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filter-bar input,
.filter-bar select {
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.filter-bar input {
  flex: 1;
  min-width: 200px;
}

.highlights-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.highlight-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-left: 4px solid #2c5aa0;
  cursor: pointer;
  transition: all 0.2s;
}

.highlight-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.highlight-card.key-insight {
  border-left-color: #f39c12;
}

.highlight-card.quote {
  border-left-color: #9b59b6;
}

.highlight-card.methodology {
  border-left-color: #3498db;
}

.highlight-card.result {
  border-left-color: #27ae60;
}

.highlight-card.question {
  border-left-color: #e74c3c;
}

.highlight-card.connection {
  border-left-color: #16a085;
}

.highlight-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.highlight-paper {
  font-weight: 600;
  color: #2c3e50;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.highlight-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: #666;
}

.highlight-category {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  background: #e8f4f8;
  color: #2c5aa0;
}

.highlight-text {
  background: #fff9e6;
  padding: 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  font-style: italic;
  line-height: 1.6;
  border-left: 3px solid #f39c12;
}

.highlight-note {
  color: #555;
  line-height: 1.6;
  margin-top: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.highlight-tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.tag {
  background: #e0e0e0;
  color: #555;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
}

/* Modal Styles */
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
  max-width: 700px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
  margin: 0;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #999;
  line-height: 1;
}

.close-btn:hover {
  color: #333;
}

.modal-body {
  padding: 1.5rem;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #e0e0e0;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  font-family: inherit;
}

.form-group textarea {
  resize: vertical;
}

.btn-primary, .btn-secondary, .btn-danger {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
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
  color: #333;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.btn-danger {
  background: #e74c3c;
  color: white;
}

.btn-danger:hover {
  background: #c0392b;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #999;
}

.empty-state-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}
</style>

<script>
let allPapers = [];
let highlights = [];
let currentHighlightId = null;

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    highlights = userData.highlights || [];
    
    populatePaperSelects();
    renderHighlights();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populatePaperSelects() {
  // Populate filter dropdown
  const filterSelect = document.getElementById('filterByPaper');
  const papersWithHighlights = [...new Set(highlights.map(h => h.paperId))];
  
  papersWithHighlights.forEach(paperId => {
    const paper = allPapers.find(p => p.arxiv_id === paperId);
    if (paper) {
      const option = document.createElement('option');
      option.value = paperId;
      option.textContent = paper.title.substring(0, 60) + (paper.title.length > 60 ? '...' : '');
      filterSelect.appendChild(option);
    }
  });
  
  // Populate add highlight dropdown
  const addSelect = document.getElementById('highlightPaper');
  allPapers.forEach(paper => {
    const option = document.createElement('option');
    option.value = paper.arxiv_id;
    option.textContent = paper.title;
    addSelect.appendChild(option);
  });
}

function renderHighlights() {
  const container = document.getElementById('highlightsList');
  const searchTerm = document.getElementById('searchHighlights').value.toLowerCase();
  const filterPaper = document.getElementById('filterByPaper').value;
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = highlights.filter(h => {
    const matchesSearch = !searchTerm || 
      h.text.toLowerCase().includes(searchTerm) ||
      (h.note && h.note.toLowerCase().includes(searchTerm)) ||
      (h.tags && h.tags.some(t => t.toLowerCase().includes(searchTerm)));
    
    const matchesPaper = filterPaper === 'all' || h.paperId === filterPaper;
    
    return matchesSearch && matchesPaper;
  });
  
  // Sort
  if (sortBy === 'date') {
    filtered.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
  } else if (sortBy === 'paper') {
    filtered.sort((a, b) => {
      const paperA = allPapers.find(p => p.arxiv_id === a.paperId);
      const paperB = allPapers.find(p => p.arxiv_id === b.paperId);
      return (paperA?.title || '').localeCompare(paperB?.title || '');
    });
  }
  
  if (filtered.length === 0) {
    container.innerHTML = `
<div class="empty-state">
<div class="empty-state-icon">✨</div>
<p>No highlights yet. Start extracting key insights from your papers!</p>
</div>
    `;
    return;
  }
  
  container.innerHTML = filtered.map(h => {
    const paper = allPapers.find(p => p.arxiv_id === h.paperId);
    const date = new Date(h.createdAt).toLocaleDateString();
    
    return `
<div class="highlight-card ${h.category}" onclick="showHighlightDetail('${h.id}')">
<div class="highlight-header">
<div>
<div class="highlight-paper">${paper?.title || 'Unknown Paper'}</div>
<div class="highlight-meta">
<span class="highlight-category">${formatCategory(h.category)}</span>
<span>${date}</span>
</div>
</div>
</div>
<div class="highlight-text">"${h.text}"</div>
        ${h.note ? `<div class="highlight-note">${h.note}</div>` : ''}
        ${h.tags && h.tags.length > 0 ? `
<div class="highlight-tags">
            ${h.tags.map(t => `<span class="tag">${t}</span>`).join('')}
</div>
        ` : ''}
</div>
    `;
  }).join('');
}

function formatCategory(category) {
  const labels = {
    'key-insight': '💡 Key Insight',
    'quote': '💬 Quote',
    'methodology': '🔬 Methodology',
    'result': '📊 Result',
    'question': '❓ Question',
    'connection': '🔗 Connection'
  };
  return labels[category] || category;
}

function updateStats() {
  document.getElementById('totalHighlights').textContent = highlights.length;
  const papersWithHighlights = new Set(highlights.map(h => h.paperId));
  document.getElementById('papersWithHighlights').textContent = papersWithHighlights.size;
}

function openAddModal() {
  document.getElementById('addHighlightModal').style.display = 'flex';
}

function closeAddModal() {
  document.getElementById('addHighlightModal').style.display = 'none';
  document.getElementById('highlightPaper').value = '';
  document.getElementById('highlightText').value = '';
  document.getElementById('highlightCategory').value = 'key-insight';
  document.getElementById('highlightNote').value = '';
  document.getElementById('highlightTags').value = '';
}

async function saveHighlight() {
  const paperId = document.getElementById('highlightPaper').value;
  const text = document.getElementById('highlightText').value.trim();
  const category = document.getElementById('highlightCategory').value;
  const note = document.getElementById('highlightNote').value.trim();
  const tagsStr = document.getElementById('highlightTags').value;
  
  if (!paperId || !text) {
    alert('Please select a paper and enter highlight text');
    return;
  }
  
  const tags = tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(t => t) : [];
  
  const highlight = {
    id: 'hl_' + Date.now(),
    paperId,
    text,
    category,
    note,
    tags,
    createdAt: new Date().toISOString()
  };
  
  highlights.push(highlight);
  await saveHighlights();
  
  closeAddModal();
  populatePaperSelects();
  renderHighlights();
  updateStats();
}

async function saveHighlights() {
  try {
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    userData.highlights = highlights;
    
    await fetch(`${API_BASE}/api/user/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving highlights:', error);
  }
}

function showHighlightDetail(id) {
  currentHighlightId = id;
  const highlight = highlights.find(h => h.id === id);
  if (!highlight) return;
  
  const paper = allPapers.find(p => p.arxiv_id === highlight.paperId);
  const date = new Date(highlight.createdAt).toLocaleDateString();
  
  const content = `
<div class="highlight-paper">${paper?.title || 'Unknown Paper'}</div>
<div class="highlight-meta">
<span class="highlight-category">${formatCategory(highlight.category)}</span>
<span>Added: ${date}</span>
</div>
<div class="highlight-text">"${highlight.text}"</div>
    ${highlight.note ? `
<div class="highlight-note">
<strong>Your Note:</strong><br>
        ${highlight.note}
</div>
    ` : ''}
    ${highlight.tags && highlight.tags.length > 0 ? `
<div class="highlight-tags">
        ${highlight.tags.map(t => `<span class="tag">${t}</span>`).join('')}
</div>
    ` : ''}
  `;
  
  document.getElementById('highlightDetailContent').innerHTML = content;
  document.getElementById('highlightDetailModal').style.display = 'flex';
}

function closeDetailModal() {
  document.getElementById('highlightDetailModal').style.display = 'none';
  currentHighlightId = null;
}

async function deleteHighlight() {
  if (!confirm('Are you sure you want to delete this highlight?')) return;
  
  highlights = highlights.filter(h => h.id !== currentHighlightId);
  await saveHighlights();
  
  closeDetailModal();
  populatePaperSelects();
  renderHighlights();
  updateStats();
}

// Event listeners
document.getElementById('addHighlightBtn').addEventListener('click', openAddModal);
document.getElementById('searchHighlights').addEventListener('input', renderHighlights);
document.getElementById('filterByPaper').addEventListener('change', renderHighlights);
document.getElementById('sortBy').addEventListener('change', renderHighlights);

// Initialize
loadData();
</script>
