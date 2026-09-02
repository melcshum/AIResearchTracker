---
title: "Key Takeaways"
---

# 💡 Key Takeaways

Extract the main conclusions, contributions, and insights from each paper you read.

<div class="takeaways-container">
<div class="takeaways-header">
<button id="addTakeawayBtn" class="btn-primary">+ Add Takeaway</button>
<div class="takeaways-stats">
<span class="stat">💡 <span id="totalTakeaways">0</span> Takeaways</span>
<span class="stat">📄 <span id="papersWithTakeaways">0</span> Papers</span>
</div>
</div>

<div class="filter-bar">
<input type="text" id="searchTakeaways" placeholder="Search takeaways...">
<select id="filterByPaper">
<option value="all">All Papers</option>
</select>
<select id="sortBy">
<option value="date">Date Added</option>
<option value="paper">By Paper</option>
</select>
</div>

<div id="takeawaysList" class="takeaways-list"></div>
</div>

<!-- Add Takeaway Modal -->
<div id="addTakeawayModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Add Key Takeaway</h2>
<button class="close-btn" onclick="closeAddModal()">&times;</button>
</div>
<div class="modal-body">
<div class="form-group">
<label>Paper</label>
<select id="takeawayPaper" required>
<option value="">Select a paper...</option>
</select>
</div>
<div class="form-group">
<label>Category</label>
<select id="takeawayCategory">
<option value="main-conclusion">Main Conclusion</option>
<option value="key-contribution">Key Contribution</option>
<option value="methodology">Methodology Insight</option>
<option value="result">Important Result</option>
<option value="limitation">Limitation</option>
<option value="future-work">Future Work</option>
<option value="implication">Implication</option>
</select>
</div>
<div class="form-group">
<label>Takeaway</label>
<textarea id="takeawayText" placeholder="What's the key takeaway from this paper?" rows="4" required></textarea>
</div>
<div class="form-group">
<label>Supporting Details (optional)</label>
<textarea id="takeawayDetails" placeholder="Additional context or evidence..." rows="3"></textarea>
</div>
<div class="form-group">
<label>Importance</label>
<select id="takeawayImportance">
<option value="low">Low</option>
<option value="medium" selected>Medium</option>
<option value="high">High</option>
<option value="critical">Critical</option>
</select>
</div>
</div>
<div class="modal-footer">
<button class="btn-secondary" onclick="closeAddModal()">Cancel</button>
<button class="btn-primary" onclick="saveTakeaway()">Save Takeaway</button>
</div>
</div>
</div>

<!-- Takeaway Detail Modal -->
<div id="takeawayDetailModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Takeaway Details</h2>
<button class="close-btn" onclick="closeDetailModal()">&times;</button>
</div>
<div class="modal-body" id="takeawayDetailContent"></div>
<div class="modal-footer">
<button class="btn-danger" onclick="deleteTakeaway()">Delete</button>
<button class="btn-secondary" onclick="closeDetailModal()">Close</button>
</div>
</div>
</div>

<style>
.takeaways-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.takeaways-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.takeaways-stats {
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

.takeaways-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.takeaway-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-left: 4px solid #3498db;
  cursor: pointer;
  transition: all 0.2s;
}

.takeaway-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.takeaway-card.importance-critical {
  border-left-color: #e74c3c;
}

.takeaway-card.importance-high {
  border-left-color: #f39c12;
}

.takeaway-card.importance-medium {
  border-left-color: #3498db;
}

.takeaway-card.importance-low {
  border-left-color: #95a5a6;
}

.takeaway-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.takeaway-paper {
  font-weight: 600;
  color: #2c3e50;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.takeaway-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: #666;
  flex-wrap: wrap;
}

.takeaway-category {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  background: #e8f4f8;
  color: #2c5aa0;
}

.takeaway-text {
  font-size: 1.05rem;
  line-height: 1.6;
  color: #2c3e50;
  margin: 1rem 0;
}

.takeaway-details {
  color: #555;
  line-height: 1.6;
  margin-top: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  font-size: 0.95rem;
}

.takeaway-details-label {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
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
let takeaways = [];
let currentTakeawayId = null;

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    takeaways = userData.takeaways || [];
    
    populatePaperSelects();
    renderTakeaways();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populatePaperSelects() {
  // Populate filter dropdown
  const filterSelect = document.getElementById('filterByPaper');
  const papersWithTakeaways = [...new Set(takeaways.map(t => t.paperId))];
  
  papersWithTakeaways.forEach(paperId => {
    const paper = allPapers.find(p => p.arxiv_id === paperId);
    if (paper) {
      const option = document.createElement('option');
      option.value = paperId;
      option.textContent = paper.title.substring(0, 60) + (paper.title.length > 60 ? '...' : '');
      filterSelect.appendChild(option);
    }
  });
  
  // Populate add takeaway dropdown
  const addSelect = document.getElementById('takeawayPaper');
  allPapers.forEach(paper => {
    const option = document.createElement('option');
    option.value = paper.arxiv_id;
    option.textContent = paper.title;
    addSelect.appendChild(option);
  });
}

function renderTakeaways() {
  const container = document.getElementById('takeawaysList');
  const searchTerm = document.getElementById('searchTakeaways').value.toLowerCase();
  const filterPaper = document.getElementById('filterByPaper').value;
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = takeaways.filter(t => {
    const matchesSearch = !searchTerm || 
      t.text.toLowerCase().includes(searchTerm) ||
      (t.details && t.details.toLowerCase().includes(searchTerm));
    
    const matchesPaper = filterPaper === 'all' || t.paperId === filterPaper;
    
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
<div class="empty-state-icon">💡</div>
<p>No takeaways yet. Start extracting key insights from your papers!</p>
</div>
    `;
    return;
  }
  
  container.innerHTML = filtered.map(t => {
    const paper = allPapers.find(p => p.arxiv_id === t.paperId);
    const date = new Date(t.createdAt).toLocaleDateString();
    const importanceClass = t.importance ? `importance-${t.importance}` : '';
    
    return `
<div class="takeaway-card ${importanceClass}" onclick="showTakeawayDetail('${t.id}')">
<div class="takeaway-header">
<div>
<div class="takeaway-paper">${paper?.title || 'Unknown Paper'}</div>
<div class="takeaway-meta">
<span class="takeaway-category">${formatCategory(t.category)}</span>
<span>${date}</span>
              ${t.importance ? `<span>Importance: ${t.importance}</span>` : ''}
</div>
</div>
</div>
<div class="takeaway-text">${t.text}</div>
        ${t.details ? `
<div class="takeaway-details">
<div class="takeaway-details-label">Supporting Details:</div>
            ${t.details}
</div>
        ` : ''}
</div>
    `;
  }).join('');
}

function formatCategory(category) {
  const labels = {
    'main-conclusion': '🎯 Main Conclusion',
    'key-contribution': '✨ Key Contribution',
    'methodology': '🔬 Methodology',
    'result': '📊 Result',
    'limitation': '⚠️ Limitation',
    'future-work': '🔮 Future Work',
    'implication': '💭 Implication'
  };
  return labels[category] || category;
}

function updateStats() {
  document.getElementById('totalTakeaways').textContent = takeaways.length;
  const papersWithTakeaways = new Set(takeaways.map(t => t.paperId));
  document.getElementById('papersWithTakeaways').textContent = papersWithTakeaways.size;
}

function openAddModal() {
  document.getElementById('addTakeawayModal').style.display = 'flex';
}

function closeAddModal() {
  document.getElementById('addTakeawayModal').style.display = 'none';
  document.getElementById('takeawayPaper').value = '';
  document.getElementById('takeawayCategory').value = 'main-conclusion';
  document.getElementById('takeawayText').value = '';
  document.getElementById('takeawayDetails').value = '';
  document.getElementById('takeawayImportance').value = 'medium';
}

async function saveTakeaway() {
  const paperId = document.getElementById('takeawayPaper').value;
  const category = document.getElementById('takeawayCategory').value;
  const text = document.getElementById('takeawayText').value.trim();
  const details = document.getElementById('takeawayDetails').value.trim();
  const importance = document.getElementById('takeawayImportance').value;
  
  if (!paperId || !text) {
    alert('Please select a paper and enter takeaway text');
    return;
  }
  
  const takeaway = {
    id: 'tk_' + Date.now(),
    paperId,
    category,
    text,
    details,
    importance,
    createdAt: new Date().toISOString()
  };
  
  takeaways.push(takeaway);
  await saveTakeaways();
  
  closeAddModal();
  populatePaperSelects();
  renderTakeaways();
  updateStats();
}

async function saveTakeaways() {
  try {
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    userData.takeaways = takeaways;
    
    await fetch(`${API_BASE}/api/user/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving takeaways:', error);
  }
}

function showTakeawayDetail(id) {
  currentTakeawayId = id;
  const takeaway = takeaways.find(t => t.id === id);
  if (!takeaway) return;
  
  const paper = allPapers.find(p => p.arxiv_id === takeaway.paperId);
  const date = new Date(takeaway.createdAt).toLocaleDateString();
  
  const content = `
<div class="takeaway-paper" style="font-size: 1.2rem; margin-bottom: 1rem;">${paper?.title || 'Unknown Paper'}</div>
<div class="takeaway-meta" style="margin-bottom: 1.5rem;">
<span class="takeaway-category">${formatCategory(takeaway.category)}</span>
<span>Added: ${date}</span>
      ${takeaway.importance ? `<span>Importance: ${takeaway.importance}</span>` : ''}
</div>
<div style="margin-bottom: 1.5rem;">
<h4 style="margin-bottom: 0.5rem; color: #2c3e50;">Takeaway</h4>
<p style="font-size: 1.05rem; line-height: 1.6;">${takeaway.text}</p>
</div>
    ${takeaway.details ? `
<div style="margin-bottom: 1.5rem;">
<h4 style="margin-bottom: 0.5rem; color: #2c3e50;">Supporting Details</h4>
<p style="color: #555; line-height: 1.6;">${takeaway.details}</p>
</div>
    ` : ''}
  `;
  
  document.getElementById('takeawayDetailContent').innerHTML = content;
  document.getElementById('takeawayDetailModal').style.display = 'flex';
}

function closeDetailModal() {
  document.getElementById('takeawayDetailModal').style.display = 'none';
  currentTakeawayId = null;
}

async function deleteTakeaway() {
  if (!confirm('Are you sure you want to delete this takeaway?')) return;
  
  takeaways = takeaways.filter(t => t.id !== currentTakeawayId);
  await saveTakeaways();
  
  closeDetailModal();
  populatePaperSelects();
  renderTakeaways();
  updateStats();
}

// Event listeners
document.getElementById('addTakeawayBtn').addEventListener('click', openAddModal);
document.getElementById('searchTakeaways').addEventListener('input', renderTakeaways);
document.getElementById('filterByPaper').addEventListener('change', renderTakeaways);
document.getElementById('sortBy').addEventListener('change', renderTakeaways);

// Initialize
loadData();
</script>
<script src="js/stage-navigation.js"></script>
