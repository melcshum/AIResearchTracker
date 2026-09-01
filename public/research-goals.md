---
title: "Research Goals"
---

# 🎯 Research Goals & Progress Tracking

Set learning goals and track your progress over time.

<div class="goals-container">
<div class="goals-header">
<button id="createGoalBtn" class="btn-primary">+ Create Goal</button>
<div class="goals-stats">
<span class="stat">🎯 <span id="activeGoals">0</span> Active Goals</span>
<span class="stat">✅ <span id="completedGoals">0</span> Completed</span>
</div>
</div>
  
<div id="goalsList" class="goals-list"></div>
</div>

<!-- Create Goal Modal -->
<div id="createGoalModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Create New Goal</h2>
<button class="close-btn" onclick="closeCreateModal()">&times;</button>
</div>
<div class="modal-body">
<div class="form-group">
<label>Goal Title</label>
<input type="text" id="goalTitle" placeholder="e.g., Read 10 papers on GUI Agents">
</div>
<div class="form-group">
<label>Goal Type</label>
<select id="goalType">
<option value="papers_count">Read X papers</option>
<option value="topic_focus">Focus on specific topic</option>
<option value="time_based">Read for X days</option>
<option value="notes_count">Add notes to X papers</option>
</select>
</div>
<div class="form-group">
<label>Target Value</label>
<input type="number" id="goalTarget" placeholder="e.g., 10" min="1">
</div>
<div class="form-group">
<label>Topic (optional, for topic-focused goals)</label>
<select id="goalTopic">
<option value="">All topics</option>
</select>
</div>
<div class="form-group">
<label>Deadline</label>
<input type="date" id="goalDeadline">
</div>
<div class="form-group">
<label>Description (optional)</label>
<textarea id="goalDescription" placeholder="Why is this goal important to you?"></textarea>
</div>
</div>
<div class="modal-footer">
<button class="btn-secondary" onclick="closeCreateModal()">Cancel</button>
<button class="btn-primary" onclick="createGoal()">Create Goal</button>
</div>
</div>
</div>

<!-- Goal Detail Modal -->
<div id="goalDetailModal" class="modal" style="display: none;">
<div class="modal-content modal-large">
<div class="modal-header">
<h2 id="detailGoalTitle">Goal Title</h2>
<button class="close-btn" onclick="closeDetailModal()">&times;</button>
</div>
<div class="modal-body">
<div class="goal-progress-section">
<div class="progress-circle" id="goalProgressCircle">
<svg viewBox="0 0 100 100">
<circle class="progress-bg" cx="50" cy="50" r="45"/>
<circle class="progress-fill" cx="50" cy="50" r="45" id="progressCircle"/>
</svg>
<div class="progress-text">
<div class="progress-percentage" id="progressPercentage">0%</div>
<div class="progress-label">Complete</div>
</div>
</div>
<div class="goal-stats-detail">
<div class="stat-row">
<span class="stat-label">Current Progress:</span>
<span class="stat-value" id="currentProgress">0</span>
</div>
<div class="stat-row">
<span class="stat-label">Target:</span>
<span class="stat-value" id="targetValue">0</span>
</div>
<div class="stat-row">
<span class="stat-label">Deadline:</span>
<span class="stat-value" id="deadlineDate">-</span>
</div>
<div class="stat-row">
<span class="stat-label">Days Remaining:</span>
<span class="stat-value" id="daysRemaining">-</span>
</div>
</div>
</div>
      
<div class="goal-description" id="goalDescriptionText"></div>
      
<div class="goal-actions">
<button class="btn-secondary" onclick="editGoal()">✏️ Edit Goal</button>
<button class="btn-primary" onclick="markAsCompleted()">✅ Mark as Completed</button>
<button class="btn-danger" onclick="deleteGoal()">🗑️ Delete Goal</button>
</div>
      
<div class="goal-activity">
<h3>📊 Progress Timeline</h3>
<div id="progressTimeline" class="timeline-chart"></div>
</div>
      
<div class="goal-papers">
<h3>📄 Related Papers</h3>
<div id="relatedPapers" class="papers-list"></div>
</div>
</div>
</div>
</div>

<style>
.goals-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.goals-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.goals-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  font-size: 1rem;
  color: #666;
}

.goals-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.goal-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: all 0.2s;
  border-left: 4px solid #2c5aa0;
}

.goal-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.goal-card.completed {
  border-left-color: #27ae60;
  opacity: 0.8;
}

.goal-card.overdue {
  border-left-color: #e74c3c;
}

.goal-card-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.goal-card-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
  flex: 1;
}

.goal-card-status {
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 600;
}

.status-active {
  background: #e8f4f8;
  color: #2c5aa0;
}

.status-completed {
  background: #d4edda;
  color: #27ae60;
}

.status-overdue {
  background: #f8d7da;
  color: #e74c3c;
}

.goal-progress-bar {
  margin: 1rem 0;
}

.progress-bar-bg {
  width: 100%;
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #2c5aa0, #4a90e2);
  transition: width 0.3s;
}

.goal-card.completed .progress-bar-fill {
  background: linear-gradient(90deg, #27ae60, #58d68d);
}

.goal-card.overdue .progress-bar-fill {
  background: linear-gradient(90deg, #e74c3c, #ec7063);
}

.goal-card-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
  color: #666;
  margin-top: 0.5rem;
}

.goal-card-description {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-top: 1rem;
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
  max-width: 600px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-large {
  max-width: 900px;
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
}

.form-group textarea {
  min-height: 100px;
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

.goal-progress-section {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
  align-items: center;
}

.progress-circle {
  position: relative;
  width: 150px;
  height: 150px;
}

.progress-circle svg {
  transform: rotate(-90deg);
  width: 100%;
  height: 100%;
}

.progress-bg {
  fill: none;
  stroke: #e0e0e0;
  stroke-width: 8;
}

.progress-fill {
  fill: none;
  stroke: #2c5aa0;
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: 283;
  stroke-dashoffset: 283;
  transition: stroke-dashoffset 0.5s;
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.progress-percentage {
  font-size: 2rem;
  font-weight: bold;
  color: #2c5aa0;
}

.progress-label {
  font-size: 0.9rem;
  color: #666;
}

.goal-stats-detail {
  flex: 1;
}

.stat-row {
  display: flex;
  justify-content: space-between;
  padding: 0.8rem 0;
  border-bottom: 1px solid #e0e0e0;
}

.stat-row:last-child {
  border-bottom: none;
}

.stat-label {
  color: #666;
}

.stat-value {
  font-weight: 600;
  color: #2c3e50;
}

.goal-description {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 2rem;
  color: #555;
  line-height: 1.6;
}

.goal-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.goal-activity, .goal-papers {
  margin-top: 2rem;
}

.goal-activity h3, .goal-papers h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.timeline-chart {
  height: 200px;
  background: #f8f9fa;
  border-radius: 6px;
  padding: 1rem;
}

.papers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.paper-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
}

.paper-item-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.paper-item-meta {
  font-size: 0.9rem;
  color: #666;
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
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
let goals = [];
let allPapers = [];
let userData = null;
let currentGoalId = null;

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(API_BASE + '/api/user/data');
    userData = await userResponse.json();
    goals = userData.goals || [];
    
    populateTopicSelect();
    renderGoals();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populateTopicSelect() {
  const topics = new Set();
  allPapers.forEach(paper => {
    if (paper.topics) {
      paper.topics.forEach(topic => topics.add(topic));
    }
  });
  
  const select = document.getElementById('goalTopic');
  Array.from(topics).sort().forEach(topic => {
    const option = document.createElement('option');
    option.value = topic;
    option.textContent = topic;
    select.appendChild(option);
  });
}

function renderGoals() {
  const container = document.getElementById('goalsList');
  
  if (goals.length === 0) {
    container.innerHTML = `
<div class="empty-state">
<div class="empty-state-icon">🎯</div>
<p>No goals yet. Create your first research goal to start tracking your progress!</p>
</div>
    `;
    return;
  }
  
  container.innerHTML = goals.map(goal => {
    const progress = calculateProgress(goal);
    const status = getGoalStatus(goal);
    const daysLeft = getDaysRemaining(goal);
    
    return `
<div class="goal-card ${status}" onclick="openGoalDetail('${goal.id}')">
<div class="goal-card-header">
<h3 class="goal-card-title">${goal.title}</h3>
<span class="goal-card-status status-${status}">${status}</span>
</div>
<div class="goal-progress-bar">
<div class="progress-bar-bg">
<div class="progress-bar-fill" style="width: ${progress}%"></div>
</div>
<div class="goal-card-meta">
<span>${progress.toFixed(0)}% complete</span>
<span>${daysLeft >= 0 ? `${daysLeft} days left` : 'Overdue'}</span>
</div>
</div>
        ${goal.description ? `<p class="goal-card-description">${goal.description}</p>` : ''}
</div>
    `;
  }).join('');
}

function calculateProgress(goal) {
  const current = getCurrentValue(goal);
  const target = goal.target || 1;
  return Math.min(100, (current / target) * 100);
}

function getCurrentValue(goal) {
  const bookmarks = userData.bookmarks || [];
  const notes = userData.notes || {};
  
  switch (goal.type) {
    case 'papers_count':
      if (goal.topic) {
        return bookmarks.filter(id => {
          const paper = allPapers.find(p => p.arxiv_id === id);
          return paper && paper.topics && paper.topics.includes(goal.topic);
        }).length;
      }
      return bookmarks.length;
    
    case 'topic_focus':
      return bookmarks.filter(id => {
        const paper = allPapers.find(p => p.arxiv_id === id);
        return paper && paper.topics && paper.topics.includes(goal.topic);
      }).length;
    
    case 'time_based':
      const startDate = new Date(goal.createdAt);
      const today = new Date();
      const daysDiff = Math.floor((today - startDate) / (1000 * 60 * 60 * 24));
      return Math.min(goal.target, daysDiff);
    
    case 'notes_count':
      if (goal.topic) {
        return Object.keys(notes).filter(id => {
          const paper = allPapers.find(p => p.arxiv_id === id);
          return paper && paper.topics && paper.topics.includes(goal.topic);
        }).length;
      }
      return Object.keys(notes).length;
    
    default:
      return 0;
  }
}

function getGoalStatus(goal) {
  if (goal.completed) return 'completed';
  
  const daysLeft = getDaysRemaining(goal);
  if (daysLeft < 0 && calculateProgress(goal) < 100) return 'overdue';
  
  return 'active';
}

function getDaysRemaining(goal) {
  if (!goal.deadline) return 999;
  
  const deadline = new Date(goal.deadline);
  const today = new Date();
  const diffTime = deadline - today;
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
}

function updateStats() {
  const active = goals.filter(g => !g.completed).length;
  const completed = goals.filter(g => g.completed).length;
  
  document.getElementById('activeGoals').textContent = active;
  document.getElementById('completedGoals').textContent = completed;
}

function openCreateModal() {
  document.getElementById('createGoalModal').style.display = 'flex';
}

function closeCreateModal() {
  document.getElementById('createGoalModal').style.display = 'none';
  document.getElementById('goalTitle').value = '';
  document.getElementById('goalType').value = 'papers_count';
  document.getElementById('goalTarget').value = '';
  document.getElementById('goalTopic').value = '';
  document.getElementById('goalDeadline').value = '';
  document.getElementById('goalDescription').value = '';
}

async function createGoal() {
  const title = document.getElementById('goalTitle').value.trim();
  const type = document.getElementById('goalType').value;
  const target = parseInt(document.getElementById('goalTarget').value);
  const topic = document.getElementById('goalTopic').value;
  const deadline = document.getElementById('goalDeadline').value;
  const description = document.getElementById('goalDescription').value.trim();
  
  if (!title || !target) {
    alert('Please fill in required fields');
    return;
  }
  
  const newGoal = {
    id: 'goal_' + Date.now(),
    title,
    type,
    target,
    topic: topic || null,
    deadline: deadline || null,
    description,
    createdAt: new Date().toISOString(),
    completed: false
  };
  
  goals.push(newGoal);
  await saveGoals();
  
  closeCreateModal();
  renderGoals();
  updateStats();
}

async function saveGoals() {
  try {
    userData.goals = goals;
    await fetch(API_BASE + '/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving goals:', error);
  }
}

function openGoalDetail(goalId) {
  currentGoalId = goalId;
  const goal = goals.find(g => g.id === goalId);
  
  if (!goal) return;
  
  document.getElementById('detailGoalTitle').textContent = goal.title;
  document.getElementById('goalDescriptionText').textContent = goal.description || 'No description';
  
  const progress = calculateProgress(goal);
  const current = getCurrentValue(goal);
  const daysLeft = getDaysRemaining(goal);
  
  document.getElementById('currentProgress').textContent = current;
  document.getElementById('targetValue').textContent = goal.target;
  document.getElementById('deadlineDate').textContent = goal.deadline ? new Date(goal.deadline).toLocaleDateString() : 'No deadline';
  document.getElementById('daysRemaining').textContent = daysLeft >= 0 ? daysLeft : 'Overdue';
  document.getElementById('progressPercentage').textContent = progress.toFixed(0) + '%';
  
  // Update progress circle
  const circumference = 283;
  const offset = circumference - (progress / 100) * circumference;
  document.getElementById('progressCircle').style.strokeDashoffset = offset;
  
  renderRelatedPapers(goal);
  
  document.getElementById('goalDetailModal').style.display = 'flex';
}

function closeDetailModal() {
  document.getElementById('goalDetailModal').style.display = 'none';
  currentGoalId = null;
}

function renderRelatedPapers(goal) {
  const container = document.getElementById('relatedPapers');
  const bookmarks = userData.bookmarks || [];
  
  let relatedPapers = bookmarks
    .map(id => allPapers.find(p => p.arxiv_id === id))
    .filter(p => p);
  
  if (goal.topic) {
    relatedPapers = relatedPapers.filter(p => p.topics && p.topics.includes(goal.topic));
  }
  
  if (relatedPapers.length === 0) {
    container.innerHTML = '<p style="text-align: center; color: #999;">No related papers yet</p>';
    return;
  }
  
  container.innerHTML = relatedPapers.slice(0, 10).map(paper => `
<div class="paper-item">
<div class="paper-item-title">${paper.title}</div>
<div class="paper-item-meta">${paper.authors} • ${paper.date}</div>
</div>
  `).join('');
}

async function markAsCompleted() {
  if (!confirm('Mark this goal as completed?')) return;
  
  const goal = goals.find(g => g.id === currentGoalId);
  if (!goal) return;
  
  goal.completed = true;
  goal.completedAt = new Date().toISOString();
  
  await saveGoals();
  closeDetailModal();
  renderGoals();
  updateStats();
}

async function deleteGoal() {
  if (!confirm('Are you sure you want to delete this goal?')) return;
  
  goals = goals.filter(g => g.id !== currentGoalId);
  await saveGoals();
  
  closeDetailModal();
  renderGoals();
  updateStats();
}

function editGoal() {
  alert('Edit functionality coming soon!');
}

document.getElementById('createGoalBtn').addEventListener('click', openCreateModal);

// Initialize
loadData();
</script>
