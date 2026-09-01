---
title: "My Learning Path"
---

<div class="learning-path-container">
<div class="path-header">
<h2>🎯 My Personalized Learning Path</h2>
<p class="subtitle">AI-generated learning pathway based on your research interests</p>
</div>

<div class="path-overview">
<div class="overview-card">
<div class="overview-icon">📚</div>
<div class="overview-content">
<div class="overview-label">Current Focus</div>
<div class="overview-value" id="currentFocus">Loading...</div>
</div>
</div>

<div class="overview-card">
<div class="overview-icon">✅</div>
<div class="overview-content">
<div class="overview-label">Papers Read</div>
<div class="overview-value" id="papersRead">0</div>
</div>
</div>

<div class="overview-card">
<div class="overview-icon">🎯</div>
<div class="overview-content">
<div class="overview-label">Path Progress</div>
<div class="overview-value" id="pathProgress">0%</div>
</div>
</div>
</div>

<div class="path-section">
<h3>📖 Your Learning Journey</h3>
<div id="learningSteps" class="learning-steps"></div>
</div>

<div class="path-section">
<h3>🔗 Knowledge Connections</h3>
<div id="knowledgeMap" class="knowledge-map"></div>
</div>

<div class="path-section">
<h3>💡 Recommended Next Steps</h3>
<div id="recommendations" class="recommendations"></div>
</div>
</div>

<style>
.learning-path-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.path-header {
  margin-bottom: 30px;
}

.path-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.path-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.overview-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.overview-icon {
  font-size: 36px;
}

.overview-content {
  flex: 1;
}

.overview-label {
  font-size: 13px;
  color: #7f8c8d;
  margin-bottom: 5px;
}

.overview-value {
  font-size: 24px;
  font-weight: bold;
  color: #2c5aa0;
}

.path-section {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 25px;
  margin-bottom: 30px;
}

.path-section h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
}

.learning-steps {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.learning-step {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
  position: relative;
  transition: all 0.2s;
}

.learning-step.completed {
  background: #e8f5e9;
  border-color: #4caf50;
}

.learning-step.current {
  background: #fff3e0;
  border-color: #ff9800;
  box-shadow: 0 2px 8px rgba(255, 152, 0, 0.2);
}

.step-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.step-number {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #2c5aa0;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 14px;
}

.learning-step.completed .step-number {
  background: #4caf50;
}

.learning-step.current .step-number {
  background: #ff9800;
}

.step-title {
  font-weight: 600;
  color: #2c3e50;
  font-size: 16px;
}

.step-status {
  margin-left: auto;
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 4px;
  background: #e0e0e0;
  color: #7f8c8d;
}

.learning-step.completed .step-status {
  background: #4caf50;
  color: white;
}

.learning-step.current .step-status {
  background: #ff9800;
  color: white;
}

.step-content {
  margin-left: 44px;
  color: #555;
  font-size: 14px;
  line-height: 1.6;
}

.step-papers {
  margin-top: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.step-paper {
  font-size: 12px;
  padding: 4px 8px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  color: #2c5aa0;
  text-decoration: none;
}

.step-paper:hover {
  background: #e8f4f8;
}

.knowledge-map {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
}

.knowledge-node {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
  text-align: center;
}

.knowledge-node.active {
  background: #e8f4f8;
  border-color: #2c5aa0;
}

.knowledge-topic {
  font-weight: 600;
  color: #2c5aa0;
  margin-bottom: 8px;
}

.knowledge-stats {
  font-size: 13px;
  color: #7f8c8d;
}

.recommendations {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.recommendation {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
  display: flex;
  gap: 12px;
  align-items: start;
}

.recommendation-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.recommendation-content {
  flex: 1;
}

.recommendation-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.recommendation-desc {
  font-size: 14px;
  color: #555;
  line-height: 1.5;
}

.recommendation-action {
  margin-top: 8px;
}

.recommendation-action a {
  font-size: 13px;
  color: #2c5aa0;
  text-decoration: none;
}

.recommendation-action a:hover {
  text-decoration: underline;
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

async function loadPathData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(API_BASE + '/api/user/data');
    const userData = await userResponse.json();
    userBookmarks = userData.bookmarks || [];
    userReadingProgress = userData.readingProgress || {};
    userNotes = userData.notes || {};
    
    const topicsResponse = await fetch(API_BASE + '/api/user/config');
    const topicsData = await topicsResponse.json();
    userTopics = topicsData.topics || [];
    
  } catch (error) {
    console.error('Failed to load path data:', error);
  }
}

function analyzeLearningProgress() {
  const topicProgress = {};
  
  userTopics.forEach(topic => {
    const topicPapers = allPapers.filter(p => p.topics && p.topics.includes(topic.id));
    const savedPapers = topicPapers.filter(p => userBookmarks.includes(p.arxiv_id));
    const readPapers = savedPapers.filter(p => {
      const progress = userReadingProgress[p.arxiv_id];
      return progress && progress.status === 'read';
    });
    
    topicProgress[topic.id] = {
      name: topic.name,
      total: topicPapers.length,
      saved: savedPapers.length,
      read: readPapers.length,
      papers: savedPapers
    };
  });
  
  return topicProgress;
}

function generateLearningPath(topicProgress) {
  const steps = [];
  
  // Determine learning order based on topic dependencies and progress
  const enabledTopics = userTopics.filter(t => t.enabled);
  
  // Sort topics by progress (least progress first)
  const sortedTopics = enabledTopics.sort((a, b) => {
    const progressA = topicProgress[a.id]?.read || 0;
    const progressB = topicProgress[b.id]?.read || 0;
    return progressA - progressB;
  });
  
  sortedTopics.forEach((topic, index) => {
    const progress = topicProgress[topic.id];
    const readCount = progress?.read || 0;
    const savedCount = progress?.saved || 0;
    
    let status = 'pending';
    if (readCount > 0 && savedCount > 0 && readCount === savedCount) {
      status = 'completed';
    } else if (readCount > 0 || savedCount > 0) {
      status = 'current';
    } else if (index === 0 || (index > 0 && sortedTopics.slice(0, index).every(t => {
      const p = topicProgress[t.id];
      return p && p.read > 0;
    }))) {
      status = 'current';
    }
    
    steps.push({
      number: index + 1,
      topic: topic,
      progress: progress,
      status: status
    });
  });
  
  return steps;
}

function renderLearningSteps(steps) {
  const container = document.getElementById('learningSteps');
  
  if (steps.length === 0) {
    container.innerHTML = '<div class="empty-state">No topics configured. Add topics in the Topics Management page to generate your learning path.</div>';
    return;
  }
  
  container.innerHTML = steps.map(step => {
    const readCount = step.progress?.read || 0;
    const savedCount = step.progress?.saved || 0;
    const totalCount = step.progress?.total || 0;
    
    const papers = step.progress?.papers?.slice(0, 3) || [];
    const papersHtml = papers.map(p => 
      `<a href="${p.url}" class="step-paper" target="_blank">${p.title.substring(0, 50)}...</a>`
    ).join('');
    
    return `
<div class="learning-step ${step.status}">
<div class="step-header">
<div class="step-number">${step.number}</div>
<div class="step-title">${step.topic.name}</div>
<div class="step-status">${step.status === 'completed' ? '✓ Complete' : step.status === 'current' ? 'In Progress' : 'Upcoming'}</div>
</div>
<div class="step-content">
<div>${readCount} of ${savedCount} saved papers read (${totalCount} available)</div>
          ${papersHtml ? `<div class="step-papers">${papersHtml}</div>` : ''}
</div>
</div>
    `;
  }).join('');
}

function renderKnowledgeMap(topicProgress) {
  const container = document.getElementById('knowledgeMap');
  
  const nodes = Object.entries(topicProgress).map(([id, progress]) => ({
    id,
    name: progress.name,
    saved: progress.saved,
    read: progress.read,
    active: progress.read > 0
  }));
  
  container.innerHTML = nodes.map(node => `
<div class="knowledge-node ${node.active ? 'active' : ''}">
<div class="knowledge-topic">${node.name}</div>
<div class="knowledge-stats">${node.saved} saved • ${node.read} read</div>
</div>
  `).join('');
}

function generateRecommendations(topicProgress, steps) {
  const container = document.getElementById('recommendations');
  const recommendations = [];
  
  // Find the current step
  const currentStep = steps.find(s => s.status === 'current');
  
  if (currentStep) {
    const unreadPapers = currentStep.progress.papers.filter(p => {
      const progress = userReadingProgress[p.arxiv_id];
      return !progress || progress.status !== 'read';
    });
    
    if (unreadPapers.length > 0) {
      recommendations.push({
        icon: '📖',
        title: `Continue reading ${currentStep.topic.name} papers`,
        description: `You have ${unreadPapers.length} unread papers in this topic. Pick up where you left off.`,
        action: { text: 'View papers →', url: 'search-papers.html' }
      });
    }
  }
  
  // Find topics with no progress
  const untouchedTopics = steps.filter(s => s.status === 'pending' && s.progress.saved === 0);
  if (untouchedTopics.length > 0) {
    const topic = untouchedTopics[0];
    recommendations.push({
      icon: '🎯',
      title: `Start exploring ${topic.topic.name}`,
      description: `There are ${topic.progress.total} papers available in this topic. Save some to begin your learning journey.`,
      action: { text: 'Search papers →', url: 'search-papers.html' }
    });
  }
  
  // Suggest adding notes
  const papersWithoutNotes = userBookmarks.filter(id => !userNotes[id]);
  if (papersWithoutNotes.length > 3) {
    recommendations.push({
      icon: '✍️',
      title: 'Add notes to your saved papers',
      description: `You have ${papersWithoutNotes.length} papers without notes. Adding notes helps reinforce learning.`,
      action: { text: 'View reading list →', url: 'reading-list.html' }
    });
  }
  
  // Suggest exploring connections
  if (Object.keys(topicProgress).length > 1) {
    recommendations.push({
      icon: '🔗',
      title: 'Explore how concepts connect',
      description: 'See how different research topics relate to each other and build a deeper understanding.',
      action: { text: 'View connections →', url: 'concepts/connections.html' }
    });
  }
  
  container.innerHTML = recommendations.slice(0, 4).map(rec => `
<div class="recommendation">
<div class="recommendation-icon">${rec.icon}</div>
<div class="recommendation-content">
<div class="recommendation-title">${rec.title}</div>
<div class="recommendation-desc">${rec.description}</div>
<div class="recommendation-action">
<a href="${rec.action.url}">${rec.action.text}</a>
</div>
</div>
</div>
  `).join('');
}

function updateOverview(topicProgress, steps) {
  const totalRead = Object.values(topicProgress).reduce((sum, p) => sum + (p.read || 0), 0);
  const totalSaved = Object.values(topicProgress).reduce((sum, p) => sum + (p.saved || 0), 0);
  
  const currentStep = steps.find(s => s.status === 'current');
  const currentFocus = currentStep ? currentStep.topic.name : 'No active topics';
  
  const completedSteps = steps.filter(s => s.status === 'completed').length;
  const progressPercent = steps.length > 0 ? Math.round((completedSteps / steps.length) * 100) : 0;
  
  document.getElementById('currentFocus').textContent = currentFocus;
  document.getElementById('papersRead').textContent = totalRead;
  document.getElementById('pathProgress').textContent = `${progressPercent}%`;
}

function renderLearningPath() {
  const topicProgress = analyzeLearningProgress();
  const steps = generateLearningPath(topicProgress);
  
  updateOverview(topicProgress, steps);
  renderLearningSteps(steps);
  renderKnowledgeMap(topicProgress);
  generateRecommendations(topicProgress, steps);
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadPathData().then(() => {
    renderLearningPath();
  });
});
</script>
