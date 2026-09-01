---
title: "Research Timeline"
---

# 📅 Research Timeline

Visualize your research journey and see how your understanding has evolved over time.

<div class="timeline-container">
  <div class="timeline-header">
    <div class="view-toggle">
      <button id="chronologicalView" class="view-btn active">Chronological</button>
      <button id="topicView" class="view-btn">By Topic</button>
      <button id="milestoneView" class="view-btn">Milestones</button>
    </div>
    <div class="timeline-controls">
      <select id="timeRange">
        <option value="all">All Time</option>
        <option value="month">Last Month</option>
        <option value="week">Last Week</option>
        <option value="custom">Custom Range</option>
      </select>
      <button id="addMilestoneBtn" class="btn-primary">+ Add Milestone</button>
    </div>
  </div>

  <div class="timeline-stats">
    <div class="stat-card">
      <div class="stat-number" id="totalPapersTimeline">0</div>
      <div class="stat-label">Papers Added</div>
    </div>
    <div class="stat-card">
      <div class="stat-number" id="researchDays">0</div>
      <div class="stat-label">Research Days</div>
    </div>
    <div class="stat-card">
      <div class="stat-number" id="activeTopics">0</div>
      <div class="stat-label">Active Topics</div>
    </div>
    <div class="stat-card">
      <div class="stat-number" id="milestoneCount">0</div>
      <div class="stat-label">Milestones</div>
    </div>
  </div>

  <div id="timelineView" class="timeline-view">
    <div class="timeline"></div>
  </div>
</div>

<!-- Add Milestone Modal -->
<div id="addMilestoneModal" class="modal" style="display: none;">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Add Research Milestone</h2>
      <button class="close-btn" onclick="closeMilestoneModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="form-group">
        <label>Milestone Title</label>
        <input type="text" id="milestoneTitle" placeholder="e.g., Completed first paper on GUI Agents">
      </div>
      <div class="form-group">
        <label>Date</label>
        <input type="date" id="milestoneDate">
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea id="milestoneDescription" placeholder="What did you achieve?" rows="3"></textarea>
      </div>
      <div class="form-group">
        <label>Category</label>
        <select id="milestoneCategory">
          <option value="discovery">Discovery</option>
          <option value="completion">Completion</option>
          <option value="breakthrough">Breakthrough</option>
          <option value="connection">Connection Made</option>
          <option value="goal">Goal Achieved</option>
        </select>
      </div>
      <div class="form-group">
        <label>Related Papers (optional)</label>
        <select id="milestonePapers" multiple size="5">
        </select>
        <small>Hold Ctrl/Cmd to select multiple papers</small>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn-secondary" onclick="closeMilestoneModal()">Cancel</button>
      <button class="btn-primary" onclick="saveMilestone()">Save Milestone</button>
    </div>
  </div>
</div>

<style>
.timeline-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.view-toggle {
  display: flex;
  gap: 0.5rem;
  background: #f0f0f0;
  padding: 0.3rem;
  border-radius: 8px;
}

.view-btn {
  padding: 0.6rem 1.2rem;
  border: none;
  background: transparent;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.view-btn.active {
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.timeline-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.timeline-controls select {
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.timeline-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2c5aa0;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.timeline-view {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.timeline {
  position: relative;
  padding-left: 3rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 1rem;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #e0e0e0;
}

.timeline-item {
  position: relative;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #2c5aa0;
}

.timeline-item.milestone {
  background: #fff9e6;
  border-left-color: #f39c12;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -2.5rem;
  top: 1.5rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #2c5aa0;
  border: 3px solid white;
  box-shadow: 0 0 0 2px #2c5aa0;
}

.timeline-item.milestone::before {
  background: #f39c12;
  box-shadow: 0 0 0 2px #f39c12;
}

.timeline-date {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.timeline-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.timeline-description {
  color: #555;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.timeline-meta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: #666;
}

.timeline-tag {
  background: #e8f4f8;
  color: #2c5aa0;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
}

.timeline-papers {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e0e0e0;
}

.timeline-papers-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.timeline-paper-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.timeline-paper {
  font-size: 0.9rem;
  color: #555;
  padding: 0.5rem;
  background: white;
  border-radius: 4px;
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

.form-group small {
  display: block;
  margin-top: 0.5rem;
  color: #666;
  font-size: 0.85rem;
}

.btn-primary, .btn-secondary {
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
let userData = null;
let milestones = [];
let currentView = 'chronological';

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    userData = await userResponse.json();
    milestones = userData.milestones || [];
    
    populateMilestonePapers();
    renderTimeline();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populateMilestonePapers() {
  const select = document.getElementById('milestonePapers');
  select.innerHTML = '';
  
  allPapers.forEach(paper => {
    const option = document.createElement('option');
    option.value = paper.arxiv_id;
    option.textContent = `${paper.date} - ${paper.title.substring(0, 60)}...`;
    select.appendChild(option);
  });
}

function renderTimeline() {
  const container = document.querySelector('.timeline');
  const timeRange = document.getElementById('timeRange').value;
  
  // Get all events (papers + milestones)
  let events = [];
  
  // Add papers as events
  allPapers.forEach(paper => {
    events.push({
      type: 'paper',
      date: paper.date,
      title: paper.title,
      authors: paper.authors,
      topics: paper.topics || [],
      paper: paper
    });
  });
  
  // Add milestones as events
  milestones.forEach(milestone => {
    events.push({
      type: 'milestone',
      date: milestone.date,
      title: milestone.title,
      description: milestone.description,
      category: milestone.category,
      papers: milestone.papers || [],
      milestone: milestone
    });
  });
  
  // Filter by time range
  if (timeRange !== 'all') {
    const now = new Date();
    let cutoff;
    
    if (timeRange === 'week') {
      cutoff = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
    } else if (timeRange === 'month') {
      cutoff = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000);
    }
    
    if (cutoff) {
      events = events.filter(e => new Date(e.date) >= cutoff);
    }
  }
  
  // Sort by date
  events.sort((a, b) => new Date(b.date) - new Date(a.date));
  
  if (events.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">📅</div>
        <p>No events in this time range</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = events.map(event => {
    if (event.type === 'milestone') {
      return `
        <div class="timeline-item milestone">
          <div class="timeline-date">${formatDate(event.date)}</div>
          <div class="timeline-title">🎯 ${event.title}</div>
          <div class="timeline-description">${event.description || ''}</div>
          <div class="timeline-meta">
            <span class="timeline-tag">${formatCategory(event.category)}</span>
          </div>
          ${event.papers.length > 0 ? `
            <div class="timeline-papers">
              <div class="timeline-papers-title">Related Papers:</div>
              <div class="timeline-paper-list">
                ${event.papers.map(paperId => {
                  const paper = allPapers.find(p => p.arxiv_id === paperId);
                  return paper ? `<div class="timeline-paper">${paper.title}</div>` : '';
                }).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      `;
    } else {
      return `
        <div class="timeline-item">
          <div class="timeline-date">${formatDate(event.date)}</div>
          <div class="timeline-title">${event.title}</div>
          <div class="timeline-description">${event.authors}</div>
          <div class="timeline-meta">
            ${event.topics.map(topic => `<span class="timeline-tag">${topic}</span>`).join('')}
          </div>
        </div>
      `;
    }
  }).join('');
}

function formatDate(dateStr) {
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  });
}

function formatCategory(category) {
  const labels = {
    'discovery': '🔍 Discovery',
    'completion': '✅ Completion',
    'breakthrough': '💡 Breakthrough',
    'connection': '🔗 Connection Made',
    'goal': '🎯 Goal Achieved'
  };
  return labels[category] || category;
}

function updateStats() {
  document.getElementById('totalPapersTimeline').textContent = allPapers.length;
  
  // Calculate research days
  const dates = allPapers.map(p => p.date);
  const uniqueDates = [...new Set(dates)];
  document.getElementById('researchDays').textContent = uniqueDates.length;
  
  // Active topics
  const topics = new Set();
  allPapers.forEach(p => {
    if (p.topics) {
      p.topics.forEach(t => topics.add(t));
    }
  });
  document.getElementById('activeTopics').textContent = topics.size;
  
  // Milestone count
  document.getElementById('milestoneCount').textContent = milestones.length;
}

function openMilestoneModal() {
  document.getElementById('addMilestoneModal').style.display = 'flex';
  document.getElementById('milestoneDate').value = new Date().toISOString().split('T')[0];
}

function closeMilestoneModal() {
  document.getElementById('addMilestoneModal').style.display = 'none';
  document.getElementById('milestoneTitle').value = '';
  document.getElementById('milestoneDate').value = '';
  document.getElementById('milestoneDescription').value = '';
  document.getElementById('milestoneCategory').value = 'discovery';
  document.getElementById('milestonePapers').selectedIndex = -1;
}

async function saveMilestone() {
  const title = document.getElementById('milestoneTitle').value.trim();
  const date = document.getElementById('milestoneDate').value;
  const description = document.getElementById('milestoneDescription').value.trim();
  const category = document.getElementById('milestoneCategory').value;
  const papersSelect = document.getElementById('milestonePapers');
  const papers = Array.from(papersSelect.selectedOptions).map(o => o.value);
  
  if (!title || !date) {
    alert('Please fill in title and date');
    return;
  }
  
  const milestone = {
    id: 'ms_' + Date.now(),
    title,
    date,
    description,
    category,
    papers,
    createdAt: new Date().toISOString()
  };
  
  milestones.push(milestone);
  await saveMilestones();
  
  closeMilestoneModal();
  renderTimeline();
  updateStats();
}

async function saveMilestones() {
  try {
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const data = await userResponse.json();
    data.milestones = milestones;
    
    await fetch(`${API_BASE}/api/user/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
  } catch (error) {
    console.error('Error saving milestones:', error);
  }
}

// Event listeners
document.getElementById('addMilestoneBtn').addEventListener('click', openMilestoneModal);
document.getElementById('timeRange').addEventListener('change', renderTimeline);

document.getElementById('chronologicalView').addEventListener('click', () => {
  currentView = 'chronological';
  document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('chronologicalView').classList.add('active');
  renderTimeline();
});

document.getElementById('topicView').addEventListener('click', () => {
  currentView = 'topic';
  document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('topicView').classList.add('active');
  // TODO: Implement topic view
  alert('Topic view coming soon!');
});

document.getElementById('milestoneView').addEventListener('click', () => {
  currentView = 'milestone';
  document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('milestoneView').classList.add('active');
  // TODO: Implement milestone-only view
  alert('Milestone view coming soon!');
});

// Initialize
loadData();
</script>
