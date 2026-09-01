---
title: "Topic Management"
---

<div class="topic-management-container">
<div class="header">
<h1>📚 Topic Management</h1>
<p>Configure your research topics and manage users</p>
</div>

<!-- User Switcher -->
<div class="card user-section">
<h2>👤 Active User</h2>
<div class="user-controls">
<select id="userSelect" onchange="switchUser()">
<option value="default">Default User</option>
<option value="melcshum">Mel</option>
</select>
<button onclick="createNewUser()">+ New User</button>
</div>
<div class="user-info">
<span id="currentUserDisplay">Current: <strong>Mel</strong></span>
</div>
</div>

<!-- Topics List -->
<div class="card topics-section">
<h2>🎯 Your Research Topics</h2>
<div id="topicsList" class="topics-list">
<!-- Topics will be loaded here -->
</div>
<button onclick="addNewTopic()" class="btn-primary">+ Add New Topic</button>
</div>

<!-- Topic Templates -->
<div class="card templates-section">
<h2>📦 Import from Templates</h2>
<p>Quick-start with pre-configured topic templates</p>
<div id="templatesList" class="templates-grid">
<!-- Templates will be loaded here -->
</div>
</div>

<!-- Topic Editor Modal -->
<div id="topicEditorModal" class="modal" style="display:none;">
<div class="modal-content">
<div class="modal-header">
<h3 id="editorTitle">Edit Topic</h3>
<button onclick="closeEditor()" class="close-btn">&times;</button>
</div>
<div class="modal-body">
<form id="topicForm">
<div class="form-group">
<label>Topic Name</label>
<input type="text" id="topicName" required>
</div>
<div class="form-group">
<label>Icon (emoji)</label>
<input type="text" id="topicIcon" placeholder="🤖" maxlength="4">
</div>
<div class="form-group">
<label>Description</label>
<textarea id="topicDescription" rows="2"></textarea>
</div>
<div class="form-group">
<label>Search Queries (one per line)</label>
<textarea id="topicQueries" rows="4" placeholder="AI agent&#10;LLM tool use"></textarea>
</div>
<div class="form-group">
<label>Keywords (comma-separated)</label>
<input type="text" id="topicKeywords" placeholder="agent, autonomous, tool">
</div>
<div class="form-group">
<label>arXiv Categories</label>
<div class="checkbox-group">
<label><input type="checkbox" value="cs.AI"> cs.AI</label>
<label><input type="checkbox" value="cs.CL"> cs.CL</label>
<label><input type="checkbox" value="cs.CV"> cs.CV</label>
<label><input type="checkbox" value="cs.LG"> cs.LG</label>
<label><input type="checkbox" value="cs.MA"> cs.MA</label>
<label><input type="checkbox" value="cs.IR"> cs.IR</label>
</div>
</div>
<div class="form-group">
<label>
<input type="checkbox" id="topicEnabled" checked>
              Enabled
</label>
</div>
</form>
</div>
<div class="modal-footer">
<button onclick="closeEditor()" class="btn-secondary">Cancel</button>
<button onclick="saveTopic()" class="btn-primary">Save</button>
</div>
</div>
</div>
</div>

<style>
.topic-management-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.header {
  margin-bottom: 2rem;
}

.header h1 {
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.card {
  background: var(--bg-secondary);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.card h2 {
  color: var(--text-primary);
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.user-controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.user-controls select {
  flex: 1;
  padding: 0.5rem;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-primary);
  color: var(--text-primary);
}

.user-info {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.topics-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1rem;
}

.topic-item {
  background: var(--bg-primary);
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid var(--border-color);
}

.topic-item:hover {
  border-color: var(--accent-color);
}

.topic-info {
  flex: 1;
}

.topic-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.topic-icon {
  font-size: 1.5rem;
}

.topic-name {
  font-weight: 600;
  color: var(--text-primary);
}

.topic-description {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.topic-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}

.topic-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-icon {
  background: none;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
  border-radius: 4px;
  font-size: 1.2rem;
  transition: background 0.2s;
}

.btn-icon:hover {
  background: var(--bg-tertiary);
}

.templates-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.template-card {
  background: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.template-card:hover {
  border-color: var(--accent-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.template-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.template-name {
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.template-description {
  color: var(--text-secondary);
  font-size: 0.85rem;
}

.btn-primary {
  background: var(--accent-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: opacity 0.2s;
}

.btn-primary:hover {
  opacity: 0.9;
}

.btn-secondary {
  background: var(--bg-tertiary);
  color: var(--text-primary);
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

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
  background: var(--bg-secondary);
  border-radius: 12px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  margin: 0;
  color: var(--text-primary);
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  line-height: 1;
}

.modal-body {
  padding: 1.5rem;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  padding: 1.5rem;
  border-top: 1px solid var(--border-color);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  font-weight: 600;
}

.form-group input[type="text"],
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: inherit;
}

.form-group textarea {
  resize: vertical;
}

.checkbox-group {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: normal;
  cursor: pointer;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--bg-tertiary);
  transition: .4s;
  border-radius: 24px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: var(--accent-color);
}

input:checked + .toggle-slider:before {
  transform: translateX(26px);
}
</style>

<script>
// Load user config from backend
async function loadUserConfig() {
  try {
    const response = await fetch('/api/user/config');
    const config = await response.json();
    return config;
  } catch (error) {
    console.error('Failed to load user config:', error);
    return null;
  }
}

// Load topics for current user
async function loadTopics() {
  const config = await loadUserConfig();
  if (!config) return;

  const topicsList = document.getElementById('topicsList');
  topicsList.innerHTML = '';

  config.topics.forEach(topic => {
    const topicEl = createTopicElement(topic);
    topicsList.appendChild(topicEl);
  });
}

// Create topic DOM element
function createTopicElement(topic) {
  const div = document.createElement('div');
  div.className = 'topic-item';
  div.dataset.topicId = topic.id;

  const queriesCount = topic.queries ? topic.queries.length : 0;
  const keywordsCount = topic.keywords ? topic.keywords.length : 0;

  div.innerHTML = `
<div class="topic-info">
<div class="topic-header">
<span class="topic-icon">${topic.icon || '📄'}</span>
<span class="topic-name">${topic.name}</span>
<label class="toggle-switch">
<input type="checkbox" ${topic.enabled ? 'checked' : ''} onchange="toggleTopic('${topic.id}', this.checked)">
<span class="toggle-slider"></span>
</label>
</div>
<div class="topic-description">${topic.description || ''}</div>
<div class="topic-meta">
<span>🔍 ${queriesCount} queries</span>
<span>🏷️ ${keywordsCount} keywords</span>
<span>📁 ${(topic.categories || []).join(', ')}</span>
</div>
</div>
<div class="topic-actions">
<button class="btn-icon" onclick="editTopic('${topic.id}')" title="Edit">✏️</button>
<button class="btn-icon" onclick="deleteTopic('${topic.id}')" title="Delete">🗑️</button>
</div>
  `;

  return div;
}

// Switch user
async function switchUser() {
  const select = document.getElementById('userSelect');
  const username = select.value;

  try {
    const response = await fetch('/api/user/switch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username })
    });

    if (response.ok) {
      document.getElementById('currentUserDisplay').innerHTML = 
        `Current: <strong>${select.options[select.selectedIndex].text}</strong>`;
      loadTopics();
    }
  } catch (error) {
    console.error('Failed to switch user:', error);
    alert('Failed to switch user');
  }
}

// Create new user
async function createNewUser() {
  const username = prompt('Enter username:');
  if (!username) return;

  const displayName = prompt('Enter display name:') || username;

  try {
    const response = await fetch('/api/user/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, displayName })
    });

    if (response.ok) {
      // Add to select
      const select = document.getElementById('userSelect');
      const option = document.createElement('option');
      option.value = username;
      option.text = displayName;
      select.appendChild(option);
      
      // Switch to new user
      select.value = username;
      await switchUser();
    }
  } catch (error) {
    console.error('Failed to create user:', error);
    alert('Failed to create user');
  }
}

// Edit topic
let currentEditTopicId = null;

function editTopic(topicId) {
  currentEditTopicId = topicId;
  document.getElementById('editorTitle').textContent = 'Edit Topic';
  // Load topic data into form
  // TODO: Fetch topic data and populate form
  document.getElementById('topicEditorModal').style.display = 'flex';
}

// Add new topic
function addNewTopic() {
  currentEditTopicId = null;
  document.getElementById('editorTitle').textContent = 'Add New Topic';
  document.getElementById('topicForm').reset();
  document.getElementById('topicEditorModal').style.display = 'flex';
}

// Close editor
function closeEditor() {
  document.getElementById('topicEditorModal').style.display = 'none';
  currentEditTopicId = null;
}

// Save topic
async function saveTopic() {
  const topicData = {
    name: document.getElementById('topicName').value,
    icon: document.getElementById('topicIcon').value || '📄',
    description: document.getElementById('topicDescription').value,
    queries: document.getElementById('topicQueries').value.split('\n').filter(q => q.trim()),
    keywords: document.getElementById('topicKeywords').value.split(',').map(k => k.trim()).filter(k => k),
    categories: Array.from(document.querySelectorAll('.checkbox-group input:checked')).map(cb => cb.value),
    enabled: document.getElementById('topicEnabled').checked
  };

  try {
    const url = currentEditTopicId ? `/api/topic/${currentEditTopicId}` : '/api/topic';
    const method = currentEditTopicId ? 'PUT' : 'POST';

    const response = await fetch(url, {
      method: method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(topicData)
    });

    if (response.ok) {
      closeEditor();
      loadTopics();
    }
  } catch (error) {
    console.error('Failed to save topic:', error);
    alert('Failed to save topic');
  }
}

// Delete topic
async function deleteTopic(topicId) {
  if (!confirm('Are you sure you want to delete this topic?')) return;

  try {
    const response = await fetch(`/api/topic/${topicId}`, {
      method: 'DELETE'
    });

    if (response.ok) {
      loadTopics();
    }
  } catch (error) {
    console.error('Failed to delete topic:', error);
    alert('Failed to delete topic');
  }
}

// Toggle topic enabled
async function toggleTopic(topicId, enabled) {
  try {
    const response = await fetch(`/api/topic/${topicId}/toggle`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled })
    });

    if (!response.ok) {
      throw new Error('Failed to toggle topic');
    }
  } catch (error) {
    console.error('Failed to toggle topic:', error);
    alert('Failed to toggle topic');
    loadTopics(); // Reload to revert UI
  }
}

// Load templates
async function loadTemplates() {
  try {
    const response = await fetch('/api/templates');
    const templates = await response.json();

    const templatesList = document.getElementById('templatesList');
    templatesList.innerHTML = '';

    templates.forEach(template => {
      const card = document.createElement('div');
      card.className = 'template-card';
      card.onclick = () => importTemplate(template.id);

      card.innerHTML = `
<div class="template-icon">${template.icon}</div>
<div class="template-name">${template.name}</div>
<div class="template-description">${template.description}</div>
      `;

      templatesList.appendChild(card);
    });
  } catch (error) {
    console.error('Failed to load templates:', error);
  }
}

// Import template
async function importTemplate(templateId) {
  if (!confirm('Import this template? It will be added to your topics.')) return;

  try {
    const response = await fetch('/api/template/import', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ templateId })
    });

    if (response.ok) {
      loadTopics();
      alert('Template imported successfully!');
    }
  } catch (error) {
    console.error('Failed to import template:', error);
    alert('Failed to import template');
  }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadTopics();
  loadTemplates();
});
</script>
