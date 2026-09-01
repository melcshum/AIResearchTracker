---
title: "Recommended Papers"
---

<div class="recommendations-container">
<div class="rec-header">
<h2>🎯 Recommended for You</h2>
<p class="subtitle">AI-powered suggestions based on your reading history and interests</p>
</div>

<div class="rec-controls">
<button id="refreshRecBtn" class="btn-primary">🔄 Refresh Recommendations</button>
</div>

<div class="rec-stats">
<div class="stat-item">
<span class="stat-label">Based on:</span>
<span class="stat-value" id="basedOn">0 papers</span>
</div>
<div class="stat-item">
<span class="stat-label">Recommendations:</span>
<span class="stat-value" id="recCount">0</span>
</div>
<div class="stat-item">
<span class="stat-label">Topics matched:</span>
<span class="stat-value" id="topicsMatched">0</span>
</div>
</div>

<div id="recommendationsList" class="rec-list"></div>
</div>

<style>
.recommendations-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.rec-header {
  margin-bottom: 30px;
}

.rec-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.rec-controls {
  margin-bottom: 20px;
}

.btn-primary {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  background: #2c5aa0;
  color: white;
  transition: all 0.2s;
}

.btn-primary:hover {
  background: #1e4a8f;
}

.rec-stats {
  display: flex;
  gap: 30px;
  margin-bottom: 30px;
  padding: 15px;
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
}

.stat-item {
  display: flex;
  gap: 10px;
  align-items: center;
}

.stat-label {
  color: #7f8c8d;
  font-size: 14px;
}

.stat-value {
  font-weight: bold;
  color: #2c5aa0;
  font-size: 18px;
}

.rec-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.rec-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: all 0.2s;
}

.rec-card:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  border-color: #2c5aa0;
}

.rec-card-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 12px;
  gap: 15px;
}

.rec-title {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  flex: 1;
}

.rec-title a {
  color: #2c5aa0;
  text-decoration: none;
}

.rec-title a:hover {
  text-decoration: underline;
}

.rec-score {
  background: #e8f5e9;
  color: #2e7d32;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.rec-meta {
  display: flex;
  gap: 15px;
  font-size: 13px;
  color: #7f8c8d;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.rec-meta-item {
  display: flex;
  align-items: center;
  gap: 5px;
}

.rec-abstract {
  color: #555;
  line-height: 1.6;
  margin-bottom: 12px;
  font-size: 14px;
}

.rec-topics {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.topic-tag {
  background: #e8f4f8;
  color: #2c5aa0;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
}

.topic-tag.matched {
  background: #fff3e0;
  color: #f57c00;
  font-weight: 600;
}

.rec-reason {
  margin-top: 12px;
  padding: 10px;
  background: #f8f9fa;
  border-left: 3px solid #2c5aa0;
  font-size: 13px;
  color: #555;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #7f8c8d;
}

.empty-state-icon {
  font-size: 48px;
  margin-bottom: 15px;
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
let allPapers = [];
let userBookmarks = [];
let userTopics = [];
let recommendations = [];

async function loadRecData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(API_BASE + '/api/user/data');
    const userData = await userResponse.json();
    userBookmarks = userData.bookmarks || [];
    
    const topicsResponse = await fetch(API_BASE + '/api/user/config');
    const topicsData = await topicsResponse.json();
    userTopics = (topicsData.topics || []).filter(t => t.enabled);
    
  } catch (error) {
    console.error('Failed to load data:', error);
  }
}

function analyzeUserInterests() {
  const bookmarkedPapers = userBookmarks
    .map(id => allPapers.find(p => p.arxiv_id === id))
    .filter(p => p);
  
  const topicCounts = {};
  const authorCounts = {};
  
  bookmarkedPapers.forEach(paper => {
    // Count topics
    const topics = paper.topics || [];
    topics.forEach(topic => {
      topicCounts[topic] = (topicCounts[topic] || 0) + 1;
    });
    
    // Count authors
    const authors = (paper.authors || '').split(',').map(a => a.trim());
    authors.forEach(author => {
      if (author) {
        authorCounts[author] = (authorCounts[author] || 0) + 1;
      }
    });
  });
  
  return {
    topicCounts,
    authorCounts,
    bookmarkedPapers
  };
}

function generateRecommendations() {
  const { topicCounts, authorCounts, bookmarkedPapers } = analyzeUserInterests();
  const bookmarkedIds = new Set(userBookmarks);
  
  // Find papers not yet bookmarked
  const candidatePapers = allPapers.filter(p => !bookmarkedIds.has(p.arxiv_id));
  
  // Score each paper
  const scoredPapers = candidatePapers.map(paper => {
    let score = 0;
    let reasons = [];
    let matchedTopics = [];
    
    // Topic matching
    const paperTopics = paper.topics || [];
    paperTopics.forEach(topic => {
      if (topicCounts[topic]) {
        score += topicCounts[topic] * 10;
        matchedTopics.push(topic);
        reasons.push(`Matches your interest in ${topic}`);
      }
    });
    
    // Author matching
    const paperAuthors = (paper.authors || '').split(',').map(a => a.trim());
    paperAuthors.forEach(author => {
      if (authorCounts[author]) {
        score += authorCounts[author] * 5;
        reasons.push(`By ${author}, whose work you follow`);
      }
    });
    
    // Recency bonus (papers from last 2 weeks)
    const paperDate = new Date(paper.date);
    const twoWeeksAgo = new Date();
    twoWeeksAgo.setDate(twoWeeksAgo.getDate() - 14);
    if (paperDate >= twoWeeksAgo) {
      score += 5;
      reasons.push('Recent paper');
    }
    
    // Topic config bonus
    userTopics.forEach(topic => {
      if (paperTopics.includes(topic.id)) {
        score += 3;
      }
    });
    
    return {
      paper,
      score,
      reasons: [...new Set(reasons)].slice(0, 3),
      matchedTopics
    };
  });
  
  // Sort by score and return top 20
  scoredPapers.sort((a, b) => b.score - a.score);
  return scoredPapers.filter(p => p.score > 0).slice(0, 20);
}

function renderRecommendations() {
  const container = document.getElementById('recommendationsList');
  
  if (userBookmarks.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">📚</div>
        <p>Bookmark some papers to get personalized recommendations!</p>
        <p>Visit the <a href="search-papers.html">Search Papers</a> page to start building your library.</p>
      </div>
    `;
    return;
  }
  
  if (recommendations.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">🎯</div>
        <p>No recommendations yet. Try bookmarking more papers in your areas of interest!</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = recommendations.map(rec => {
    const paper = rec.paper;
    const abstract = paper.abstract || '';
    const shortAbstract = abstract.length > 200 ? abstract.substring(0, 200) + '...' : abstract;
    
    const topics = (paper.topics || []).map(topic => {
      const isMatched = rec.matchedTopics.includes(topic);
      return `<span class="topic-tag ${isMatched ? 'matched' : ''}">${topic}</span>`;
    }).join('');
    
    const reasons = rec.reasons.length > 0 
      ? `<div class="rec-reason">💡 ${rec.reasons.join(' • ')}</div>`
      : '';
    
    return `
      <div class="rec-card">
        <div class="rec-card-header">
          <div class="rec-title">
            <a href="${paper.url}" target="_blank">${paper.title}</a>
          </div>
          <div class="rec-score">Score: ${rec.score}</div>
        </div>
        <div class="rec-meta">
          <div class="rec-meta-item">📅 ${paper.date}</div>
          <div class="rec-meta-item">👥 ${paper.authors}</div>
        </div>
        <div class="rec-abstract">${shortAbstract}</div>
        <div class="rec-topics">${topics}</div>
        ${reasons}
      </div>
    `;
  }).join('');
}

function updateStats() {
  const { topicCounts } = analyzeUserInterests();
  
  document.getElementById('basedOn').textContent = `${userBookmarks.length} papers`;
  document.getElementById('recCount').textContent = recommendations.length;
  document.getElementById('topicsMatched').textContent = Object.keys(topicCounts).length;
}

function refreshRecommendations() {
  const btn = document.getElementById('refreshRecBtn');
  btn.textContent = '⏳ Generating...';
  btn.disabled = true;
  
  setTimeout(() => {
    recommendations = generateRecommendations();
    renderRecommendations();
    updateStats();
    btn.textContent = '🔄 Refresh Recommendations';
    btn.disabled = false;
  }, 500);
}

// Event listeners
document.getElementById('refreshRecBtn').addEventListener('click', refreshRecommendations);

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadRecData().then(() => {
    recommendations = generateRecommendations();
    renderRecommendations();
    updateStats();
  });
});
</script>
