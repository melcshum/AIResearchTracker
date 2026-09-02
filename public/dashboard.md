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

<div class="dashboard-section learning-metrics-section">
<h3>🎓 Learning Metrics</h3>
<div class="learning-stats-grid">
<div class="learning-stat-card">
<div class="learning-stat-icon">📖</div>
<div class="learning-stat-value" id="dashTermsExplored">0</div>
<div class="learning-stat-label">Terms Explored</div>
</div>
<div class="learning-stat-card">
<div class="learning-stat-icon">✍️</div>
<div class="learning-stat-value" id="dashExplanationsWritten">0</div>
<div class="learning-stat-label">Explanations Written</div>
</div>
<div class="learning-stat-card">
<div class="learning-stat-icon">🌱</div>
<div class="learning-stat-value" id="dashSeedling">0</div>
<div class="learning-stat-label">Seedling 🌱</div>
</div>
<div class="learning-stat-card">
<div class="learning-stat-icon">🌿</div>
<div class="learning-stat-value" id="dashGrowing">0</div>
<div class="learning-stat-label">Growing 🌿</div>
</div>
<div class="learning-stat-card">
<div class="learning-stat-icon">🌳</div>
<div class="learning-stat-value" id="dashMastered">0</div>
<div class="learning-stat-label">Mastered 🌳</div>
</div>
<div class="learning-stat-card">
<div class="learning-stat-icon">⏱️</div>
<div class="learning-stat-value" id="dashTimeSpent">0m</div>
<div class="learning-stat-label">Time Learning</div>
</div>
</div>

<div class="learning-stages">
<h4>📊 Stage Completion</h4>
<div class="stage-completion-grid" id="stageCompletion"></div>
</div>

<div class="learning-streak">
<h4>🔥 Learning Streak</h4>
<div class="streak-display">
<div class="streak-number" id="dashStreak">0</div>
<div class="streak-label">day streak</div>
</div>
<div class="streak-calendar" id="streakCalendar"></div>
</div>

<div class="learning-achievements">
<h4>🏆 Achievements</h4>
<div class="achievements-grid" id="achievementsGrid"></div>
</div>
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

.learning-metrics-section {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
}

.learning-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 15px;
  margin-bottom: 30px;
}

.learning-stat-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  transition: all 0.3s;
}

.learning-stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.1);
  border-color: #4a90e2;
}

.learning-stat-icon {
  font-size: 32px;
  margin-bottom: 8px;
}

.learning-stat-value {
  font-size: 28px;
  font-weight: bold;
  color: #2c5aa0;
  margin-bottom: 4px;
}

.learning-stat-label {
  font-size: 13px;
  color: #7f8c8d;
}

.learning-stages,
.learning-streak,
.learning-achievements {
  margin-top: 30px;
}

.learning-stages h4,
.learning-streak h4,
.learning-achievements h4 {
  color: #2c3e50;
  font-size: 18px;
  margin-bottom: 15px;
}

.stage-completion-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}

.stage-completion-item {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
}

.stage-completion-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.stage-completion-name {
  font-weight: 600;
  color: #2c3e50;
  font-size: 14px;
}

.stage-completion-percent {
  font-size: 14px;
  font-weight: bold;
  color: #4a90e2;
}

.learning-streak {
  display: flex;
  gap: 30px;
  align-items: center;
  flex-wrap: wrap;
}

.streak-display {
  text-align: center;
  min-width: 120px;
}

.streak-number {
  font-size: 48px;
  font-weight: bold;
  color: #e74c3c;
  line-height: 1;
  margin-bottom: 8px;
}

.streak-label {
  font-size: 14px;
  color: #7f8c8d;
}

.streak-calendar {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
  min-width: 300px;
}

.streak-day {
  aspect-ratio: 1;
  background: #e0e0e0;
  border-radius: 4px;
  position: relative;
  transition: all 0.2s;
}

.streak-day.active {
  background: linear-gradient(135deg, #27ae60, #2ecc71);
}

.streak-day.today {
  border: 2px solid #3498db;
}

.streak-day:hover::after {
  content: attr(data-date);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.8);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 11px;
  white-space: nowrap;
  z-index: 10;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
}

.achievement-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  padding: 16px;
  text-align: center;
  transition: all 0.3s;
}

.achievement-card.unlocked {
  border-color: #f39c12;
  background: linear-gradient(135deg, #fff9e6 0%, #ffffff 100%);
}

.achievement-card.locked {
  opacity: 0.5;
}

.achievement-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.achievement-icon {
  font-size: 36px;
  margin-bottom: 8px;
}

.achievement-name {
  font-weight: 600;
  color: #2c3e50;
  font-size: 14px;
  margin-bottom: 4px;
}

.achievement-desc {
  font-size: 12px;
  color: #7f8c8d;
}

@media (max-width: 768px) {
  .learning-stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .learning-streak {
    flex-direction: column;
    align-items: stretch;
  }
  
  .streak-calendar {
    min-width: auto;
  }
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

function renderLearningMetrics() {
  const contributions = JSON.parse(localStorage.getItem('wikiContributions') || '[]');
  
  // Calculate basic stats
  const terms = new Set(contributions.map(c => c.termId));
  const explanations = contributions.filter(c => c.type === 'explanation');
  
  document.getElementById('dashTermsExplored').textContent = terms.size;
  document.getElementById('dashExplanationsWritten').textContent = explanations.length;
  
  // Calculate mastery levels
  const masteryLevels = { seedling: 0, growing: 0, mastered: 0 };
  const termMastery = {};
  
  contributions.forEach(c => {
    if (c.type === 'explanation' && c.content) {
      const len = c.content.length;
      if (len > 200) masteryLevels.mastered++;
      else if (len > 100) masteryLevels.growing++;
      else masteryLevels.seedling++;
      
      if (!termMastery[c.termId] || termMastery[c.termId] < len) {
        termMastery[c.termId] = len;
      }
    }
  });
  
  // Recount based on best explanation per term
  const termLevels = { seedling: 0, growing: 0, mastered: 0 };
  Object.values(termMastery).forEach(len => {
    if (len > 200) termLevels.mastered++;
    else if (len > 100) termLevels.growing++;
    else termLevels.seedling++;
  });
  
  document.getElementById('dashSeedling').textContent = termLevels.seedling;
  document.getElementById('dashGrowing').textContent = termLevels.growing;
  document.getElementById('dashMastered').textContent = termLevels.mastered;
  
  // Calculate time spent (estimate: 2 min per term explored, 5 min per explanation)
  const timeMinutes = (terms.size * 2) + (explanations.length * 5);
  const timeStr = timeMinutes >= 60 ? `${Math.floor(timeMinutes/60)}h ${timeMinutes%60}m` : `${timeMinutes}m`;
  document.getElementById('dashTimeSpent').textContent = timeStr;
  
  // Render stage completion
  renderStageCompletion(contributions);
  
  // Render streak
  renderStreak(contributions);
  
  // Render achievements
  renderAchievements(contributions, terms.size, explanations.length, termLevels);
}

function renderStageCompletion(contributions) {
  const container = document.getElementById('stageCompletion');
  
  const stages = [
    { name: '✍️ Write', color: '#3498db', key: 'explanation' },
    { name: '🔍 Review', color: '#f39c12', key: 'review' },
    { name: '🤖 Enhance', color: '#9b59b6', key: 'enhance' },
    { name: '🧠 Attain', color: '#27ae60', key: 'quiz' },
    { name: '📈 Update', color: '#e74c3c', key: 'update' }
  ];
  
  const stageCounts = {};
  contributions.forEach(c => {
    stageCounts[c.type] = (stageCounts[c.type] || 0) + 1;
  });
  
  const maxCount = Math.max(...stages.map(s => stageCounts[s.key] || 0), 1);
  
  container.innerHTML = stages.map(stage => {
    const count = stageCounts[stage.key] || 0;
    const percent = Math.round((count / maxCount) * 100);
    
    return `
<div class="stage-completion-item">
<div class="stage-completion-header">
<span class="stage-completion-name">${stage.name}</span>
<span class="stage-completion-percent">${count}</span>
</div>
<div class="progress-bar">
<div class="progress-fill" style="width: ${percent}%; background: ${stage.color}"></div>
</div>
</div>
    `;
  }).join('');
}

function renderStreak(contributions) {
  // Calculate streak from contribution timestamps
  const activityDates = new Set();
  contributions.forEach(c => {
    if (c.timestamp) {
      const dateStr = new Date(c.timestamp).toISOString().split('T')[0];
      activityDates.add(dateStr);
    }
  });
  
  // Calculate current streak
  let streak = 0;
  const today = new Date();
  for (let i = 0; i < 365; i++) {
    const checkDate = new Date(today);
    checkDate.setDate(checkDate.getDate() - i);
    const dateStr = checkDate.toISOString().split('T')[0];
    
    if (activityDates.has(dateStr)) {
      streak++;
    } else if (i > 0) {
      break;
    }
  }
  
  document.getElementById('dashStreak').textContent = streak;
  
  // Render calendar (last 28 days)
  const calendar = document.getElementById('streakCalendar');
  const days = [];
  for (let i = 27; i >= 0; i--) {
    const date = new Date();
    date.setDate(date.getDate() - i);
    const dateStr = date.toISOString().split('T')[0];
    const isActive = activityDates.has(dateStr);
    const isToday = i === 0;
    
    days.push(`
<div class="streak-day ${isActive ? 'active' : ''} ${isToday ? 'today' : ''}" data-date="${dateStr}"></div>
    `);
  }
  
  calendar.innerHTML = days.join('');
}

function renderAchievements(contributions, termsCount, explanationsCount, termLevels) {
  const container = document.getElementById('achievementsGrid');
  
  const achievements = [
    {
      icon: '🌱',
      name: 'First Steps',
      desc: 'Explore your first term',
      unlocked: termsCount >= 1
    },
    {
      icon: '📖',
      name: 'Curious Mind',
      desc: 'Explore 10 terms',
      unlocked: termsCount >= 10
    },
    {
      icon: '✍️',
      name: 'Knowledge Builder',
      desc: 'Write 5 explanations',
      unlocked: explanationsCount >= 5
    },
    {
      icon: '🎯',
      name: 'Deep Thinker',
      desc: 'Write 10 explanations',
      unlocked: explanationsCount >= 10
    },
    {
      icon: '🌿',
      name: 'Growing Knowledge',
      desc: 'Master 5 concepts',
      unlocked: termLevels.mastered >= 5
    },
    {
      icon: '🌳',
      name: 'Knowledge Master',
      desc: 'Master 10 concepts',
      unlocked: termLevels.mastered >= 10
    },
    {
      icon: '🔥',
      name: 'On Fire',
      desc: 'Maintain 7-day streak',
      unlocked: false // Would need streak calculation
    },
    {
      icon: '🏆',
      name: 'Scholar',
      desc: 'Explore 50 terms',
      unlocked: termsCount >= 50
    }
  ];
  
  container.innerHTML = achievements.map(ach => `
<div class="achievement-card ${ach.unlocked ? 'unlocked' : 'locked'}">
<div class="achievement-icon">${ach.icon}</div>
<div class="achievement-name">${ach.name}</div>
<div class="achievement-desc">${ach.desc}</div>
</div>
  `).join('');
}

function renderDashboard() {
  updateStats();
  renderTopicProgress();
  renderRecentBookmarks();
  renderRecentNotes();
  renderReadingActivity();
  renderLearningMetrics();
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadDashboardData().then(() => {
    renderDashboard();
  });
});
</script>
