---
title: "Settings"
---

<div class="settings-container">
<div class="settings-header">
<h2>⚙️ Project Settings</h2>
<p class="settings-subtitle">Configure how the AI Research Tracker works for you</p>
</div>

<div class="settings-nav">
<button class="nav-btn active" onclick="showSection('ingestion')">📥 Ingestion</button>
<button class="nav-btn" onclick="showSection('sources')">🔗 Sources</button>
<button class="nav-btn" onclick="showSection('topics')">🏷️ Topics</button>
<button class="nav-btn" onclick="showSection('display')">🎨 Display</button>
<button class="nav-btn" onclick="showSection('automation')">🤖 Automation</button>
<button class="nav-btn" onclick="showSection('data')">💾 Data</button>
</div>

<div id="ingestion-section" class="settings-section active">
<h3>📥 Ingestion Settings</h3>
<p class="section-desc">Configure how and when papers are fetched</p>

<div class="setting-group">
<label>Fetch Frequency</label>
<select id="fetchFrequency" onchange="saveSetting('fetchFrequency', this.value)">
<option value="daily">Daily (recommended)</option>
<option value="twice-daily">Twice Daily</option>
<option value="weekly">Weekly</option>
<option value="manual">Manual Only</option>
</select>
<small>How often to check for new papers</small>
</div>

<div class="setting-group">
<label>Papers per Fetch</label>
<input type="number" id="papersPerFetch" min="5" max="100" value="20" onchange="saveSetting('papersPerFetch', this.value)">
<small>Maximum number of papers to fetch per run (5-100)</small>
</div>

<div class="setting-group">
<label>Date Range</label>
<select id="dateRange" onchange="saveSetting('dateRange', this.value)">
<option value="7">Past 7 days</option>
<option value="14">Past 14 days</option>
<option value="30">Past 30 days</option>
<option value="3">Past 3 days</option>
</select>
<small>How far back to search for papers</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="autoEnhance" checked onchange="saveSetting('autoEnhance', this.checked)">
Auto-enhance papers after fetching
</label>
<small>Automatically extract key contributions and related papers</small>
</div>
</div>

<div id="sources-section" class="settings-section">
<h3>🔗 Data Sources</h3>
<p class="section-desc">Choose which sources to pull papers from</p>

<div class="setting-group">
<label>arXiv Categories</label>
<div class="checkbox-group">
<label><input type="checkbox" class="source-check" value="cs.AI" checked> cs.AI (Artificial Intelligence)</label>
<label><input type="checkbox" class="source-check" value="cs.CL" checked> cs.CL (Computation and Language)</label>
<label><input type="checkbox" class="source-check" value="cs.IR" checked> cs.IR (Information Retrieval)</label>
<label><input type="checkbox" class="source-check" value="cs.LG" checked> cs.LG (Machine Learning)</label>
<label><input type="checkbox" class="source-check" value="cs.MM"> cs.MM (Multimedia)</label>
<label><input type="checkbox" class="source-check" value="cs.CV"> cs.CV (Computer Vision)</label>
<label><input type="checkbox" class="source-check" value="cs.RO"> cs.RO (Robotics)</label>
</div>
<small>Select which arXiv categories to monitor</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="includeCrossListed" checked onchange="saveSetting('includeCrossListed', this.checked)">
Include cross-listed papers
</label>
<small>Papers that appear in multiple categories</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="includeReplacements" onchange="saveSetting('includeReplacements', this.checked)">
Include paper updates/replacements
</label>
<small>Fetch updated versions of existing papers</small>
</div>

<div class="setting-group">
<label>Minimum Citation Count</label>
<input type="number" id="minCitations" min="0" max="1000" value="0" onchange="saveSetting('minCitations', this.value)">
<small>Only fetch papers with at least this many citations (0 = all papers)</small>
</div>
</div>

<div id="topics-section" class="settings-section">
<h3>🏷️ Topic Configuration</h3>
<p class="section-desc">Customize which research areas to focus on</p>

<div class="topic-toggles">
<div class="topic-toggle-card">
<div class="topic-header">
<input type="checkbox" id="topic-agents" checked onchange="toggleTopic('ai-agents', this.checked)">
<label for="topic-agents">🤖 AI Agents</label>
</div>
<p>Autonomous systems, tool use, planning, multi-agent coordination</p>
<div class="topic-keywords">
<input type="text" id="keywords-agents" value="agent,tool use,planning,multi-agent,autonomous" onchange="saveTopicKeywords('ai-agents', this.value)">
</div>
</div>

<div class="topic-toggle-card">
<div class="topic-header">
<input type="checkbox" id="topic-reasoning" checked onchange="toggleTopic('llm-reasoning', this.checked)">
<label for="topic-reasoning">🧠 LLM Reasoning</label>
</div>
<p>Chain-of-thought, self-consistency, tree-of-thought, verification</p>
<div class="topic-keywords">
<input type="text" id="keywords-reasoning" value="reasoning,chain-of-thought,self-consistency,verification" onchange="saveTopicKeywords('llm-reasoning', this.value)">
</div>
</div>

<div class="topic-toggle-card">
<div class="topic-header">
<input type="checkbox" id="topic-rag" checked onchange="toggleTopic('rag-retrieval', this.checked)">
<label for="topic-rag">🔍 RAG & Retrieval</label>
</div>
<p>Dense retrieval, hybrid search, knowledge grounding, citation</p>
<div class="topic-keywords">
<input type="text" id="keywords-rag" value="rag,retrieval,dense retrieval,hybrid search,knowledge grounding" onchange="saveTopicKeywords('rag-retrieval', this.value)">
</div>
</div>

<div class="topic-toggle-card">
<div class="topic-header">
<input type="checkbox" id="topic-multimodal" checked onchange="toggleTopic('multi-modal', this.checked)">
<label for="topic-multimodal">🎬 Multi-Modal</label>
</div>
<p>Vision-language models, audio processing, cross-modal reasoning</p>
<div class="topic-keywords">
<input type="text" id="keywords-multimodal" value="multimodal,vision-language,audio,cross-modal" onchange="saveTopicKeywords('multi-modal', this.value)">
</div>
</div>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="autoClassify" checked onchange="saveSetting('autoClassify', this.checked)">
Auto-classify papers into topics
</label>
<small>Use keywords to automatically assign papers to topics</small>
</div>
</div>

<div id="display-section" class="settings-section">
<h3>🎨 Display Settings</h3>
<p class="section-desc">Customize how the site looks and behaves</p>

<div class="setting-group">
<label>Theme</label>
<select id="theme" onchange="changeTheme(this.value)">
<option value="light">Light</option>
<option value="dark">Dark</option>
<option value="auto">Auto (system preference)</option>
</select>
<small>Choose your preferred color scheme</small>
</div>

<div class="setting-group">
<label>Papers per Page</label>
<select id="papersPerPage" onchange="saveSetting('papersPerPage', this.value)">
<option value="10">10 papers</option>
<option value="20" selected>20 papers</option>
<option value="50">50 papers</option>
<option value="100">100 papers</option>
</select>
<small>Number of papers to show in lists</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="showAbstracts" checked onchange="saveSetting('showAbstracts', this.checked)">
Show paper abstracts by default
</label>
<small>Display abstracts in paper lists (can be toggled per paper)</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="compactMode" onchange="saveSetting('compactMode', this.checked)">
Compact mode
</label>
<small>Reduce spacing and show more content on screen</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="enableAnimations" checked onchange="saveSetting('enableAnimations', this.checked)">
Enable animations
</label>
<small>Smooth transitions and hover effects</small>
</div>
</div>

<div id="automation-section" class="settings-section">
<h3>🤖 Automation Settings</h3>
<p class="section-desc">Configure the automation pipeline</p>

<div class="setting-group">
<label>
<input type="checkbox" id="autoRebuild" checked onchange="saveSetting('autoRebuild', this.checked)">
Auto-rebuild site after fetch
</label>
<small>Automatically run quarto render after fetching papers</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="autoGenerate" checked onchange="saveSetting('autoGenerate', this.checked)">
Auto-generate data pages
</label>
<small>Regenerate statistics, tag cloud, search index after changes</small>
</div>

<div class="setting-group">
<label>Log Level</label>
<select id="logLevel" onchange="saveSetting('logLevel', this.value)">
<option value="error">Error only</option>
<option value="warning" selected>Warnings</option>
<option value="info">Info</option>
<option value="debug">Debug (verbose)</option>
</select>
<small>How much detail to log during automation</small>
</div>

<div class="setting-group">
<label>
<input type="checkbox" id="notifyOnComplete" onchange="saveSetting('notifyOnComplete', this.checked)">
Show notification when automation completes
</label>
<small>Display a notification when daily pipeline finishes</small>
</div>

<div class="automation-status">
<h4>Current Status</h4>
<div class="status-item">
<span class="status-label">Last Run:</span>
<span class="status-value" id="lastRunTime">Never</span>
</div>
<div class="status-item">
<span class="status-label">Papers Fetched:</span>
<span class="status-value" id="papersFetched">0</span>
</div>
<div class="status-item">
<span class="status-label">Next Scheduled:</span>
<span class="status-value" id="nextRun">Not scheduled</span>
</div>
</div>
</div>

<div id="data-section" class="settings-section">
<h3>💾 Data Management</h3>
<p class="section-desc">Export, import, and manage your data</p>

<div class="data-actions">
<div class="data-action-card">
<h4>📥 Export Settings</h4>
<p>Download your configuration as JSON</p>
<button class="action-btn" onclick="exportSettings()">Export Settings</button>
</div>

<div class="data-action-card">
<h4>📤 Import Settings</h4>
<p>Load configuration from JSON file</p>
<button class="action-btn" onclick="importSettings()">Import Settings</button>
</div>

<div class="data-action-card">
<h4>🔄 Reset to Defaults</h4>
<p>Restore all settings to default values</p>
<button class="action-btn danger" onclick="resetSettings()">Reset Settings</button>
</div>

<div class="data-action-card">
<h4>🗑️ Clear All Data</h4>
<p>Remove all local data (reading list, notes, settings)</p>
<button class="action-btn danger" onclick="clearAllData()">Clear All Data</button>
</div>
</div>

<div class="storage-info">
<h4>Storage Usage</h4>
<div class="storage-item">
<span>Settings:</span>
<span id="settingsSize">0 KB</span>
</div>
<div class="storage-item">
<span>Reading List:</span>
<span id="readingListSize">0 KB</span>
</div>
<div class="storage-item">
<span>Notes:</span>
<span id="notesSize">0 KB</span>
</div>
<div class="storage-item">
<span>Wiki Contributions:</span>
<span id="wikiSize">0 KB</span>
</div>
<div class="storage-item total">
<span>Total:</span>
<span id="totalSize">0 KB</span>
</div>
</div>
</div>

<div class="settings-footer">
<button class="save-btn" onclick="saveAllSettings()">💾 Save All Settings</button>
<button class="cancel-btn" onclick="loadSettings()">↩️ Reload Settings</button>
<div id="saveStatus" class="save-status"></div>
</div>
</div>

<style>
.settings-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.settings-header {
  text-align: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #e0e0e0;
}

.settings-header h2 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.settings-subtitle {
  color: #666;
  font-size: 16px;
}

.settings-nav {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  flex-wrap: wrap;
  justify-content: center;
}

.nav-btn {
  padding: 10px 20px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.nav-btn:hover {
  border-color: #667eea;
  background: #f8f9fa;
}

.nav-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

.settings-section {
  display: none;
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 20px;
}

.settings-section.active {
  display: block;
}

.settings-section h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.section-desc {
  color: #666;
  margin-bottom: 30px;
}

.setting-group {
  margin-bottom: 25px;
  padding-bottom: 25px;
  border-bottom: 1px solid #f0f0f0;
}

.setting-group:last-child {
  border-bottom: none;
}

.setting-group > label {
  display: block;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 8px;
  font-size: 15px;
}

.setting-group small {
  display: block;
  color: #888;
  margin-top: 5px;
  font-size: 13px;
}

.setting-group select,
.setting-group input[type="number"],
.setting-group input[type="text"] {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.setting-group input[type="checkbox"] {
  margin-right: 8px;
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  font-weight: normal;
  cursor: pointer;
}

.topic-toggles {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.topic-toggle-card {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border: 2px solid #e0e0e0;
  transition: all 0.2s;
}

.topic-toggle-card:hover {
  border-color: #667eea;
}

.topic-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.topic-header label {
  font-weight: 600;
  font-size: 16px;
  margin: 0;
}

.topic-toggle-card p {
  color: #666;
  font-size: 13px;
  margin: 10px 0;
}

.topic-keywords input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 13px;
  font-family: monospace;
}

.automation-status {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-top: 30px;
}

.automation-status h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.status-item {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #e0e0e0;
}

.status-item:last-child {
  border-bottom: none;
}

.status-label {
  font-weight: 600;
  color: #666;
}

.status-value {
  color: #2c3e50;
}

.data-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.data-action-card {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.data-action-card h4 {
  margin-bottom: 10px;
  color: #2c3e50;
}

.data-action-card p {
  color: #666;
  font-size: 13px;
  margin-bottom: 15px;
}

.action-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.action-btn.danger {
  background: #dc3545;
}

.storage-info {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.storage-info h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.storage-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #e0e0e0;
}

.storage-item:last-child {
  border-bottom: none;
}

.storage-item.total {
  font-weight: bold;
  border-top: 2px solid #2c3e50;
  margin-top: 10px;
  padding-top: 15px;
}

.settings-footer {
  display: flex;
  gap: 15px;
  align-items: center;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  position: sticky;
  bottom: 20px;
}

.save-btn {
  padding: 12px 30px;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: all 0.2s;
}

.save-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.cancel-btn {
  padding: 12px 30px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  font-size: 15px;
  transition: all 0.2s;
}

.cancel-btn:hover {
  border-color: #667eea;
}

.save-status {
  margin-left: auto;
  color: #28a745;
  font-weight: 600;
  opacity: 0;
  transition: opacity 0.3s;
}

.save-status.show {
  opacity: 1;
}
</style>

<script>
// Default settings
const defaultSettings = {
  fetchFrequency: 'daily',
  papersPerFetch: 20,
  dateRange: '7',
  autoEnhance: true,
  sources: ['cs.AI', 'cs.CL', 'cs.IR', 'cs.LG'],
  includeCrossListed: true,
  includeReplacements: false,
  minCitations: 0,
  topics: {
    'ai-agents': { enabled: true, keywords: 'agent,tool use,planning,multi-agent,autonomous' },
    'llm-reasoning': { enabled: true, keywords: 'reasoning,chain-of-thought,self-consistency,verification' },
    'rag-retrieval': { enabled: true, keywords: 'rag,retrieval,dense retrieval,hybrid search,knowledge grounding' },
    'multi-modal': { enabled: true, keywords: 'multimodal,vision-language,audio,cross-modal' }
  },
  autoClassify: true,
  theme: 'light',
  papersPerPage: 20,
  showAbstracts: true,
  compactMode: false,
  enableAnimations: true,
  autoRebuild: true,
  autoGenerate: true,
  logLevel: 'warning',
  notifyOnComplete: false
};

// Load settings from localStorage
function loadSettings() {
  const saved = JSON.parse(localStorage.getItem('projectSettings') || '{}');
  const settings = { ...defaultSettings, ...saved };
  
  // Ingestion
  document.getElementById('fetchFrequency').value = settings.fetchFrequency;
  document.getElementById('papersPerFetch').value = settings.papersPerFetch;
  document.getElementById('dateRange').value = settings.dateRange;
  document.getElementById('autoEnhance').checked = settings.autoEnhance;
  
  // Sources
  document.querySelectorAll('.source-check').forEach(cb => {
    cb.checked = settings.sources.includes(cb.value);
  });
  document.getElementById('includeCrossListed').checked = settings.includeCrossListed;
  document.getElementById('includeReplacements').checked = settings.includeReplacements;
  document.getElementById('minCitations').value = settings.minCitations;
  
  // Topics
  Object.entries(settings.topics).forEach(([topic, config]) => {
    const topicMap = {
      'ai-agents': 'agents',
      'llm-reasoning': 'reasoning',
      'rag-retrieval': 'rag',
      'multi-modal': 'multimodal'
    };
    const id = topicMap[topic];
    if (id) {
      document.getElementById(`topic-${id}`).checked = config.enabled;
      document.getElementById(`keywords-${id}`).value = config.keywords;
    }
  });
  document.getElementById('autoClassify').checked = settings.autoClassify;
  
  // Display
  document.getElementById('theme').value = settings.theme;
  document.getElementById('papersPerPage').value = settings.papersPerPage;
  document.getElementById('showAbstracts').checked = settings.showAbstracts;
  document.getElementById('compactMode').checked = settings.compactMode;
  document.getElementById('enableAnimations').checked = settings.enableAnimations;
  
  // Automation
  document.getElementById('autoRebuild').checked = settings.autoRebuild;
  document.getElementById('autoGenerate').checked = settings.autoGenerate;
  document.getElementById('logLevel').value = settings.logLevel;
  document.getElementById('notifyOnComplete').checked = settings.notifyOnComplete;
  
  // Update automation status
  const lastRun = localStorage.getItem('lastAutomationRun');
  document.getElementById('lastRunTime').textContent = lastRun ? new Date(lastRun).toLocaleString() : 'Never';
  document.getElementById('papersFetched').textContent = localStorage.getItem('totalPapersFetched') || '0';
  
  updateStorageInfo();
}

// Save individual setting
function saveSetting(key, value) {
  const settings = JSON.parse(localStorage.getItem('projectSettings') || '{}');
  settings[key] = value;
  localStorage.setItem('projectSettings', JSON.stringify(settings));
  showSaveStatus();
}

// Save topic keywords
function saveTopicKeywords(topic, keywords) {
  const settings = JSON.parse(localStorage.getItem('projectSettings') || '{}');
  if (!settings.topics) settings.topics = {};
  if (!settings.topics[topic]) settings.topics[topic] = {};
  settings.topics[topic].keywords = keywords;
  localStorage.setItem('projectSettings', JSON.stringify(settings));
  showSaveStatus();
}

// Toggle topic
function toggleTopic(topic, enabled) {
  const settings = JSON.parse(localStorage.getItem('projectSettings') || '{}');
  if (!settings.topics) settings.topics = {};
  if (!settings.topics[topic]) settings.topics[topic] = {};
  settings.topics[topic].enabled = enabled;
  localStorage.setItem('projectSettings', JSON.stringify(settings));
  showSaveStatus();
}

// Save all settings
function saveAllSettings() {
  const settings = {};
  
  // Ingestion
  settings.fetchFrequency = document.getElementById('fetchFrequency').value;
  settings.papersPerFetch = parseInt(document.getElementById('papersPerFetch').value);
  settings.dateRange = document.getElementById('dateRange').value;
  settings.autoEnhance = document.getElementById('autoEnhance').checked;
  
  // Sources
  settings.sources = Array.from(document.querySelectorAll('.source-check:checked')).map(cb => cb.value);
  settings.includeCrossListed = document.getElementById('includeCrossListed').checked;
  settings.includeReplacements = document.getElementById('includeReplacements').checked;
  settings.minCitations = parseInt(document.getElementById('minCitations').value);
  
  // Topics
  settings.topics = {
    'ai-agents': {
      enabled: document.getElementById('topic-agents').checked,
      keywords: document.getElementById('keywords-agents').value
    },
    'llm-reasoning': {
      enabled: document.getElementById('topic-reasoning').checked,
      keywords: document.getElementById('keywords-reasoning').value
    },
    'rag-retrieval': {
      enabled: document.getElementById('topic-rag').checked,
      keywords: document.getElementById('keywords-rag').value
    },
    'multi-modal': {
      enabled: document.getElementById('topic-multimodal').checked,
      keywords: document.getElementById('keywords-multimodal').value
    }
  };
  settings.autoClassify = document.getElementById('autoClassify').checked;
  
  // Display
  settings.theme = document.getElementById('theme').value;
  settings.papersPerPage = parseInt(document.getElementById('papersPerPage').value);
  settings.showAbstracts = document.getElementById('showAbstracts').checked;
  settings.compactMode = document.getElementById('compactMode').checked;
  settings.enableAnimations = document.getElementById('enableAnimations').checked;
  
  // Automation
  settings.autoRebuild = document.getElementById('autoRebuild').checked;
  settings.autoGenerate = document.getElementById('autoGenerate').checked;
  settings.logLevel = document.getElementById('logLevel').value;
  settings.notifyOnComplete = document.getElementById('notifyOnComplete').checked;
  
  localStorage.setItem('projectSettings', JSON.stringify(settings));
  showSaveStatus('Settings saved!');
}

// Show section
function showSection(section) {
  document.querySelectorAll('.settings-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  
  document.getElementById(`${section}-section`).classList.add('active');
  event.target.classList.add('active');
}

// Change theme
function changeTheme(theme) {
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else if (theme === 'light') {
    document.documentElement.removeAttribute('data-theme');
  } else {
    // Auto
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }
  saveSetting('theme', theme);
}

// Export settings
function exportSettings() {
  const settings = JSON.parse(localStorage.getItem('projectSettings') || '{}');
  const blob = new Blob([JSON.stringify(settings, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `research-tracker-settings-${new Date().toISOString().split('T')[0]}.json`;
  a.click();
  URL.revokeObjectURL(url);
}

// Import settings
function importSettings() {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = 'application/json';
  
  input.onchange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    
    reader.onload = (event) => {
      try {
        const settings = JSON.parse(event.target.result);
        localStorage.setItem('projectSettings', JSON.stringify(settings));
        loadSettings();
        alert('Settings imported successfully!');
      } catch (error) {
        alert('Error importing settings: ' + error.message);
      }
    };
    
    reader.readAsText(file);
  };
  
  input.click();
}

// Reset settings
function resetSettings() {
  if (confirm('Are you sure you want to reset all settings to defaults?')) {
    localStorage.removeItem('projectSettings');
    loadSettings();
    alert('Settings reset to defaults!');
  }
}

// Clear all data
function clearAllData() {
  if (confirm('This will delete ALL local data including reading list, notes, wiki contributions, and settings. Continue?')) {
    localStorage.clear();
    loadSettings();
    alert('All data cleared!');
  }
}

// Update storage info
function updateStorageInfo() {
  const calculateSize = (key) => {
    const data = localStorage.getItem(key);
    return data ? (data.length / 1024).toFixed(2) : '0';
  };
  
  document.getElementById('settingsSize').textContent = calculateSize('projectSettings') + ' KB';
  document.getElementById('readingListSize').textContent = calculateSize('readingList') + ' KB';
  document.getElementById('notesSize').textContent = calculateSize('paperNotes') + ' KB';
  document.getElementById('wikiSize').textContent = calculateSize('wikiContributions') + ' KB';
  
  const total = Object.keys(localStorage).reduce((sum, key) => sum + (localStorage.getItem(key) || '').length, 0);
  document.getElementById('totalSize').textContent = (total / 1024).toFixed(2) + ' KB';
}

// Show save status
function showSaveStatus(message = 'Settings saved!') {
  const status = document.getElementById('saveStatus');
  status.textContent = message;
  status.classList.add('show');
  setTimeout(() => status.classList.remove('show'), 2000);
}

// Initialize
loadSettings();
</script>
