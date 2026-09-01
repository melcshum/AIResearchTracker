---
title: "Research Questions"
---

# ❓ Research Questions

Track questions that arise during your research and mark them as answered when you find the answers.

<div class="questions-container">
<div class="questions-header">
<button id="addQuestionBtn" class="btn-primary">+ Add Question</button>
<div class="questions-stats">
<span class="stat">❓ <span id="totalQuestions">0</span> Questions</span>
<span class="stat">✅ <span id="answeredQuestions">0</span> Answered</span>
<span class="stat">⏳ <span id="pendingQuestions">0</span> Pending</span>
</div>
</div>

<div class="filter-bar">
<input type="text" id="searchQuestions" placeholder="Search questions...">
<select id="filterStatus">
<option value="all">All Status</option>
<option value="pending">Pending</option>
<option value="answered">Answered</option>
</select>
<select id="filterTopic">
<option value="all">All Topics</option>
</select>
<select id="sortBy">
<option value="date">Date Added</option>
<option value="status">Status</option>
<option value="topic">Topic</option>
</select>
</div>

<div id="questionsList" class="questions-list"></div>
</div>

<!-- Add Question Modal -->
<div id="addQuestionModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Add Research Question</h2>
<button class="close-btn" onclick="closeAddModal()">&times;</button>
</div>
<div class="modal-body">
<div class="form-group">
<label>Question</label>
<textarea id="questionText" placeholder="What question arose while reading?" rows="3" required></textarea>
</div>
<div class="form-group">
<label>Context (optional)</label>
<textarea id="questionContext" placeholder="What were you reading when this question came up?" rows="2"></textarea>
</div>
<div class="form-group">
<label>Related Paper (optional)</label>
<select id="questionPaper">
<option value="">No specific paper</option>
</select>
</div>
<div class="form-group">
<label>Topic</label>
<select id="questionTopic">
<option value="">General</option>
</select>
</div>
<div class="form-group">
<label>Priority</label>
<select id="questionPriority">
<option value="low">Low</option>
<option value="medium" selected>Medium</option>
<option value="high">High</option>
</select>
</div>
</div>
<div class="modal-footer">
<button class="btn-secondary" onclick="closeAddModal()">Cancel</button>
<button class="btn-primary" onclick="saveQuestion()">Save Question</button>
</div>
</div>
</div>

<!-- Question Detail Modal -->
<div id="questionDetailModal" class="modal" style="display: none;">
<div class="modal-content">
<div class="modal-header">
<h2>Question Details</h2>
<button class="close-btn" onclick="closeDetailModal()">&times;</button>
</div>
<div class="modal-body" id="questionDetailContent"></div>
<div class="modal-footer">
<button class="btn-danger" onclick="deleteQuestion()">Delete</button>
<button class="btn-secondary" onclick="closeDetailModal()">Close</button>
</div>
</div>
</div>

<style>
.questions-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.questions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.questions-stats {
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

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.question-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-left: 4px solid #f39c12;
  cursor: pointer;
  transition: all 0.2s;
}

.question-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.question-card.answered {
  border-left-color: #27ae60;
  opacity: 0.8;
}

.question-card.priority-high {
  border-left-color: #e74c3c;
}

.question-card.priority-medium {
  border-left-color: #f39c12;
}

.question-card.priority-low {
  border-left-color: #95a5a6;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.question-text {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  line-height: 1.5;
  flex: 1;
}

.question-status {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-left: 1rem;
}

.status-pending {
  background: #fff3cd;
  color: #856404;
}

.status-answered {
  background: #d4edda;
  color: #155724;
}

.question-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.question-tag {
  background: #e8f4f8;
  color: #2c5aa0;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
}

.question-context {
  color: #555;
  line-height: 1.6;
  margin-top: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  font-style: italic;
}

.question-answer {
  margin-top: 1rem;
  padding: 1rem;
  background: #d4edda;
  border-radius: 6px;
  border-left: 3px solid #27ae60;
}

.question-answer-label {
  font-weight: 600;
  color: #155724;
  margin-bottom: 0.5rem;
}

.question-answer-text {
  color: #155724;
  line-height: 1.6;
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

.btn-success {
  background: #27ae60;
  color: white;
}

.btn-success:hover {
  background: #229954;
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
let questions = [];
let currentQuestionId = null;

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    questions = userData.questions || [];
    
    populateSelects();
    renderQuestions();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populateSelects() {
  // Populate paper select
  const paperSelect = document.getElementById('questionPaper');
  allPapers.forEach(paper => {
    const option = document.createElement('option');
    option.value = paper.arxiv_id;
    option.textContent = paper.title;
    paperSelect.appendChild(option);
  });
  
  // Populate topic select
  const topics = new Set();
  allPapers.forEach(paper => {
    if (paper.topics) {
      paper.topics.forEach(topic => topics.add(topic));
    }
  });
  
  const topicSelect = document.getElementById('questionTopic');
  const filterTopicSelect = document.getElementById('filterTopic');
  
  Array.from(topics).sort().forEach(topic => {
    const option1 = document.createElement('option');
    option1.value = topic;
    option1.textContent = topic;
    topicSelect.appendChild(option1);
    
    const option2 = document.createElement('option');
    option2.value = topic;
    option2.textContent = topic;
    filterTopicSelect.appendChild(option2);
  });
}

function renderQuestions() {
  const container = document.getElementById('questionsList');
  const searchTerm = document.getElementById('searchQuestions').value.toLowerCase();
  const filterStatus = document.getElementById('filterStatus').value;
  const filterTopic = document.getElementById('filterTopic').value;
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = questions.filter(q => {
    const matchesSearch = !searchTerm || 
      q.question.toLowerCase().includes(searchTerm) ||
      (q.context && q.context.toLowerCase().includes(searchTerm)) ||
      (q.answer && q.answer.toLowerCase().includes(searchTerm));
    
    const matchesStatus = filterStatus === 'all' || 
      (filterStatus === 'pending' && !q.answered) ||
      (filterStatus === 'answered' && q.answered);
    
    const matchesTopic = filterTopic === 'all' || q.topic === filterTopic;
    
    return matchesSearch && matchesStatus && matchesTopic;
  });
  
  // Sort
  if (sortBy === 'date') {
    filtered.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
  } else if (sortBy === 'status') {
    filtered.sort((a, b) => (a.answered ? 1 : 0) - (b.answered ? 1 : 0));
  } else if (sortBy === 'topic') {
    filtered.sort((a, b) => (a.topic || '').localeCompare(b.topic || ''));
  }
  
  if (filtered.length === 0) {
    container.innerHTML = `
<div class="empty-state">
<div class="empty-state-icon">❓</div>
<p>No questions yet. Start tracking questions that arise during your research!</p>
</div>
    `;
    return;
  }
  
  container.innerHTML = filtered.map(q => {
    const paper = allPapers.find(p => p.arxiv_id === q.paperId);
    const date = new Date(q.createdAt).toLocaleDateString();
    const priorityClass = q.priority ? `priority-${q.priority}` : '';
    
    return `
<div class="question-card ${q.answered ? 'answered' : ''} ${priorityClass}" onclick="showQuestionDetail('${q.id}')">
<div class="question-header">
<div class="question-text">${q.question}</div>
<span class="question-status ${q.answered ? 'status-answered' : 'status-pending'}">
            ${q.answered ? '✅ Answered' : '⏳ Pending'}
</span>
</div>
<div class="question-meta">
<span>📅 ${date}</span>
          ${q.topic ? `<span class="question-tag">${q.topic}</span>` : ''}
          ${q.priority ? `<span class="question-tag">Priority: ${q.priority}</span>` : ''}
          ${paper ? `<span class="question-tag">📄 ${paper.title.substring(0, 40)}...</span>` : ''}
</div>
        ${q.context ? `<div class="question-context">${q.context}</div>` : ''}
        ${q.answer ? `
<div class="question-answer">
<div class="question-answer-label">Answer:</div>
<div class="question-answer-text">${q.answer}</div>
</div>
        ` : ''}
</div>
    `;
  }).join('');
}

function updateStats() {
  const total = questions.length;
  const answered = questions.filter(q => q.answered).length;
  const pending = total - answered;
  
  document.getElementById('totalQuestions').textContent = total;
  document.getElementById('answeredQuestions').textContent = answered;
  document.getElementById('pendingQuestions').textContent = pending;
}

function openAddModal() {
  document.getElementById('addQuestionModal').style.display = 'flex';
}

function closeAddModal() {
  document.getElementById('addQuestionModal').style.display = 'none';
  document.getElementById('questionText').value = '';
  document.getElementById('questionContext').value = '';
  document.getElementById('questionPaper').value = '';
  document.getElementById('questionTopic').value = '';
  document.getElementById('questionPriority').value = 'medium';
}

async function saveQuestion() {
  const question = document.getElementById('questionText').value.trim();
  const context = document.getElementById('questionContext').value.trim();
  const paperId = document.getElementById('questionPaper').value;
  const topic = document.getElementById('questionTopic').value;
  const priority = document.getElementById('questionPriority').value;
  
  if (!question) {
    alert('Please enter a question');
    return;
  }
  
  const q = {
    id: 'q_' + Date.now(),
    question,
    context,
    paperId,
    topic,
    priority,
    answered: false,
    createdAt: new Date().toISOString()
  };
  
  questions.push(q);
  await saveQuestions();
  
  closeAddModal();
  renderQuestions();
  updateStats();
}

async function saveQuestions() {
  try {
    const userResponse = await fetch(`${API_BASE}/api/user/data`);
    const userData = await userResponse.json();
    userData.questions = questions;
    
    await fetch(`${API_BASE}/api/user/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving questions:', error);
  }
}

function showQuestionDetail(id) {
  currentQuestionId = id;
  const q = questions.find(q => q.id === id);
  if (!q) return;
  
  const paper = allPapers.find(p => p.arxiv_id === q.paperId);
  const date = new Date(q.createdAt).toLocaleDateString();
  
  const content = `
<div style="margin-bottom: 1.5rem;">
<h3 style="margin-bottom: 0.5rem; color: #2c3e50;">Question</h3>
<p style="font-size: 1.1rem; line-height: 1.6;">${q.question}</p>
</div>
    
    ${q.context ? `
<div style="margin-bottom: 1.5rem;">
<h4 style="margin-bottom: 0.5rem; color: #2c3e50;">Context</h4>
<p style="color: #555; line-height: 1.6; font-style: italic;">${q.context}</p>
</div>
    ` : ''}
    
<div style="margin-bottom: 1.5rem;">
<h4 style="margin-bottom: 0.5rem; color: #2c3e50;">Details</h4>
<p><strong>Date Added:</strong> ${date}</p>
      ${q.topic ? `<p><strong>Topic:</strong> ${q.topic}</p>` : ''}
      ${q.priority ? `<p><strong>Priority:</strong> ${q.priority}</p>` : ''}
      ${paper ? `<p><strong>Related Paper:</strong> ${paper.title}</p>` : ''}
</div>
    
    ${q.answer ? `
<div style="margin-bottom: 1.5rem; padding: 1rem; background: #d4edda; border-radius: 6px; border-left: 3px solid #27ae60;">
<h4 style="margin-bottom: 0.5rem; color: #155724;">Answer</h4>
<p style="color: #155724; line-height: 1.6;">${q.answer}</p>
</div>
    ` : `
<div style="margin-bottom: 1.5rem;">
<h4 style="margin-bottom: 0.5rem; color: #2c3e50;">Add Answer</h4>
<textarea id="answerInput" placeholder="What's the answer to this question?" rows="4" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 6px; font-size: 1rem; font-family: inherit; resize: vertical;"></textarea>
<button class="btn-success" onclick="markAsAnswered()" style="margin-top: 1rem;">Mark as Answered</button>
</div>
    `}
  `;
  
  document.getElementById('questionDetailContent').innerHTML = content;
  document.getElementById('questionDetailModal').style.display = 'flex';
}

function closeDetailModal() {
  document.getElementById('questionDetailModal').style.display = 'none';
  currentQuestionId = null;
}

async function markAsAnswered() {
  const answer = document.getElementById('answerInput').value.trim();
  if (!answer) {
    alert('Please enter an answer');
    return;
  }
  
  const q = questions.find(q => q.id === currentQuestionId);
  if (!q) return;
  
  q.answer = answer;
  q.answered = true;
  q.answeredAt = new Date().toISOString();
  
  await saveQuestions();
  closeDetailModal();
  renderQuestions();
  updateStats();
}

async function deleteQuestion() {
  if (!confirm('Are you sure you want to delete this question?')) return;
  
  questions = questions.filter(q => q.id !== currentQuestionId);
  await saveQuestions();
  
  closeDetailModal();
  renderQuestions();
  updateStats();
}

// Event listeners
document.getElementById('addQuestionBtn').addEventListener('click', openAddModal);
document.getElementById('searchQuestions').addEventListener('input', renderQuestions);
document.getElementById('filterStatus').addEventListener('change', renderQuestions);
document.getElementById('filterTopic').addEventListener('change', renderQuestions);
document.getElementById('sortBy').addEventListener('change', renderQuestions);

// Initialize
loadData();
</script>
