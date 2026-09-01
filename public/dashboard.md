---
title: "Learning Dashboard"
---

<div class="dashboard-container">
<div class="dashboard-header">
<h2>📊 Learning Dashboard</h2>
<p class="subtitle">Track your research journey across all topics</p>
</div>

<div class="stats-grid">
<div class="stat-card">
<div class="stat-icon">📚</div>
<div class="stat-content">
<div class="stat-number" id="totalPapers">0</div>
<div class="stat-label">Total Papers Saved</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">📖</div>
<div class="stat-content">
<div class="stat-number" id="papersRead">0</div>
<div class="stat-label">Papers Read</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">✍️</div>
<div class="stat-content">
<div class="stat-number" id="papersWithNotes">0</div>
<div class="stat-label">Papers with Notes</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">🎯</div>
<div class="stat-content">
<div class="stat-number" id="activeTopics">0</div>
<div class="stat-label">Active Topics</div>
</div>
</div>
</div>

<div class="dashboard-section">
<h3>📈 Progress by Topic</h3>
<div id="topicProgress" class="topic-progress-grid"></div>
</div>

<div class="dashboard-section">
<h3>⭐ Recent Bookmarks</h3>
<div id="recentBookmarks" class="recent-papers"></div>
</div>

<div class="dashboard-section">
<h3>✍️ Recent Notes</h3>
<div id="recentNotes" class="recent-papers"></div>
</div>

<div class="dashboard-section">
<h3>📚 Reading Activity</h3>
<div id="readingActivity" class="activity-chart"></div>
</div>
</div>

<style>
.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.dashboard-header {
  margin-bottom: 30px;
}

.dashboard-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.stat-icon {
  font-size: 40px;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 32px;
  font-weight: bold;
  color: #2c5aa0;
  line-height: 1;
}

.stat-label {
  font-size: 14px;
  color: #7f8c8d;
  margin-top: 5px;
}

.dashboard-section {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
}

.dashboard-section h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
}

.topic-progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 15px;
}

.topic-card {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
}

.topic-name {
  font-weight: 600;
  color: #2c5aa0;
  margin-bottom: 10px;
  font-size: 16px;
}

.topic-stats {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #7f8c8d;
  margin-bottom: 10px;
}

.progress-bar {
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
  margin-top: 8px;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #2c5aa0, #4a90e2);
  transition: width 0.3s;
}

.recent-papers {
  display: grid;
  gap: 10px;
}

.recent-paper {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.recent-paper-info {
  flex: 1;
}

.recent-paper-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.recent-paper-meta {
  font-size: 13px;
  color: #7f8c8d;
}

.recent-paper-action {
  font-size: 12px;
  color: #2c5aa0;
  background: #e8f4f8;
  padding: 4px 8px;
  border-radius: 4px;
}

.activity-chart {
  display: flex;
  gap: 5px;
  align-items: end;
  height: 150px;
  padding: 20px 0;
}

.activity-bar {
  flex: 1;
  background: linear-gradient(180deg, #4a90e2, #2c5aa0);
  border-radius: 4px 4px 0 0;
  min-height: 10px;
  position: relative;
  transition: opacity 0.2s;
}

.activity-bar:hover {
  opacity: 0.8;
}

.activity-bar-label {
  position: absolute;
  bottom: -25px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  color: #7f8c8d;
  white-space: nowrap;
}

.empty-state {
  text-align: center;
  padding: 40px;
  color: #7f8c8d;
  font-style: italic;
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
let allPapers = [];
let userBookmarks = [];
let userReadingProgress = {};
let userNotes = {};
let userTopics = [];

async function loadDashboardData() {
  try {
    // Load all papers
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    // Load user data
    const userResponse = await fetch(API_BASE + '/api/user/data');
    const userData = await userResponse.json();
    userBookmarks = userData.bookmarks || [];
    userReadingProgress = userData.readingProgress || {};
    userNotes = userData.notes || {};
    
    // Load user topics
    const topicsResponse = await fetch(API_BASE + '/api/user/config');
    const topicsData = await topicsResponse.json();
    userTopics = topicsData.topics || [];
    
  } catch (error) {
    console.error('Failed to load dashboard data:', error);
  }
}

function updateStats() {
  document.getElementById('totalPapers').textContent = userBookmarks.length;
  
  const readCount = Object.values(userReadingProgress).filter(p => p.status === 'read').length;
  document.getElementById('papersRead').textContent = readCount;
  
  const notesCount = Object.keys(userNotes).length;
  document.getElementById('papersWithNotes').textContent = notesCount;
  
  const enabledTopics = userTopics.filter(t => t.enabled).length;
  document.getElementById('activeTopics').textContent = enabledTopics;
}

function renderTopicProgress() {
  const container = document.getElementById('topicProgress');
  
  if (userTopics.length === 0) {
    container.innerHTML = '<div class="empty-state">No topics configured yet</div>';
    return;
  }
  
  const topicStats = userTopics.map(topic => {
    const topicPapers = allPapers.filter(p => p.topics && p.topics.includes(topic.id));
    const savedPapers = topicPapers.filter(p => userBookmarks.includes(p.arxiv_id));
    const readPapers = savedPapers.filter(p => {
      const progress = userReadingProgress[p.arxiv_id];
      return progress && progress.status === 'read';
    });
    
    return {
      name: topic.name,
      total: topicPapers.length,
      saved: savedPapers.length,
      read: readPapers.length,
      progress: savedPapers.length > 0 ? (readPapers.length / savedPapers.length) * 100 : 0
    };
  });
  
  container.innerHTML = topicStats.map(stat => `
    <div class="topic-card">
      <div class="topic-name">${stat.name}</div>
      <div class="topic-stats">
        <span>${stat.saved} saved</span>
        <span>${stat.read} read</span>
        <span>${stat.total} available</span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" style="width: ${stat.progress}%"></div>
      </div>
    </div>
  `).join('');
}

function renderRecentBookmarks() {
  const container = document.getElementById('recentBookmarks');
  
  if (userBookmarks.length === 0) {
    container.innerHTML = '<div class="empty-state">No bookmarks yet. Start saving papers from the search page!</div>';
    return;
  }
  
  const recent = userBookmarks.slice(-5).reverse();
  const papers = recent.map(id => allPapers.find(p => p.arxiv_id === id)).filter(p => p);
  
  container.innerHTML = papers.map(paper => `
    <div class="recent-paper">
      <div class="recent-paper-info">
        <div class="recent-paper-title">${paper.title}</div>
        <div class="recent-paper-meta">${paper.authors} • ${paper.date}</div>
      </div>
      <a href="${paper.url}" class="recent-paper-action">Read →</a>
    </div>
  `).join('');
}

function renderRecentNotes() {
  const container = document.getElementById('recentNotes');
  
  const noteEntries = Object.entries(userNotes);
  
  if (noteEntries.length === 0) {
    container.innerHTML = '<div class="empty-state">No notes yet. Add notes to papers to track your insights!</div>';
    return;
  }
  
  const recent = noteEntries.slice(-5).reverse();
  const papers = recent.map(([id]) => allPapers.find(p => p.arxiv_id === id)).filter(p => p);
  
  container.innerHTML = papers.map(paper => {
    const note = userNotes[paper.arxiv_id];
    const preview = note.length > 100 ? note.substring(0, 100) + '...' : note;
    
    return `
      <div class="recent-paper">
        <div class="recent-paper-info">
          <div class="recent-paper-title">${paper.title}</div>
          <div class="recent-paper-meta">${preview}</div>
        </div>
        <a href="${paper.url}" class="recent-paper-action">View →</a>
      </div>
    `;
  }).join('');
}

function renderReadingActivity() {
  const container = document.getElementById('readingActivity');
  
  // Calculate activity for last 7 days
  const days = [];
  for (let i = 6; i >= 0; i--) {
    const date = new Date();
    date.setDate(date.getDate() - i);
    const dateStr = date.toISOString().split('T')[0];
    days.push({ date: dateStr, label: date.toLocaleDateString('en', { weekday: 'short' }) });
  }
  
  const activity = days.map(day => {
    const count = Object.values(userReadingProgress).filter(p => {
      if (!p.updatedAt) return false;
      const updatedDate = p.updatedAt.split('T')[0];
      return updatedDate === day.date;
    }).length;
    
    return { ...day, count };
  });
  
  const maxCount = Math.max(...activity.map(a => a.count), 1);
  
  container.innerHTML = activity.map(a => {
    const height = (a.count / maxCount) * 100;
    return `
      <div class="activity-bar" style="height: ${height}%" title="${a.count} papers on ${a.date}">
        <div class="activity-bar-label">${a.label}</div>
      </div>
    `;
  }).join('');
}

function renderDashboard() {
  updateStats();
  renderTopicProgress();
  renderRecentBookmarks();
  renderRecentNotes();
  renderReadingActivity();
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadDashboardData().then(() => {
    renderDashboard();
  });
});
</script>
