---
title: "Feedback Dashboard"
---

<div class="dashboard-container">
  <div class="dashboard-header">
    <h2>📊 Feedback Dashboard</h2>
    <p class="subtitle">View and manage all your HITL contributions</p>
  </div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-icon">⭐</div>
      <div class="stat-info">
        <div class="stat-number" id="summaryFeedbackCount">0</div>
        <div class="stat-label">Summary Ratings</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🧠</div>
      <div class="stat-info">
        <div class="stat-number" id="conceptValidationCount">0</div>
        <div class="stat-label">Concept Validations</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">👍</div>
      <div class="stat-info">
        <div class="stat-number" id="recommendationRatingCount">0</div>
        <div class="stat-label">Recommendation Ratings</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">📝</div>
      <div class="stat-info">
        <div class="stat-number" id="annotationCount">0</div>
        <div class="stat-label">Annotations</div>
      </div>
    </div>
  </div>

  <div class="dashboard-tabs">
    <button class="tab-btn active" onclick="switchTab('summary')">⭐ Summary Feedback</button>
    <button class="tab-btn" onclick="switchTab('concept')">🧠 Concept Validation</button>
    <button class="tab-btn" onclick="switchTab('recommendation')">👍 Recommendations</button>
    <button class="tab-btn" onclick="switchTab('export')">💾 Export All</button>
  </div>

  <div id="summaryTab" class="tab-content active">
    <div class="feedback-list" id="summaryFeedbackList"></div>
  </div>

  <div id="conceptTab" class="tab-content">
    <div class="feedback-list" id="conceptValidationList"></div>
  </div>

  <div id="recommendationTab" class="tab-content">
    <div class="feedback-list" id="recommendationRatingList"></div>
  </div>

  <div id="exportTab" class="tab-content">
    <div class="export-section">
      <h3>Export Your Feedback Data</h3>
      <p>Download all your HITL contributions for backup or analysis</p>
      <div class="export-buttons">
        <button onclick="exportAllFeedback('json')" class="btn-primary">📄 Export as JSON</button>
        <button onclick="exportAllFeedback('csv')" class="btn-secondary">📊 Export as CSV</button>
        <button onclick="clearAllFeedback()" class="btn-danger">🗑️ Clear All Feedback</button>
      </div>
    </div>
  </div>
</div>

<style>
.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.dashboard-header {
  margin-bottom: 2rem;
}

.dashboard-header h2 {
  margin: 0 0 0.5rem 0;
  color: #2c5aa0;
}

.subtitle {
  color: #666;
  margin: 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  font-size: 2.5rem;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #2c5aa0;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.dashboard-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #e0e0e0;
}

.tab-btn {
  padding: 0.75rem 1.5rem;
  background: transparent;
  border: none;
  border-bottom: 3px solid transparent;
  cursor: pointer;
  font-size: 1rem;
  color: #666;
  transition: all 0.2s;
}

.tab-btn:hover {
  color: #2c5aa0;
}

.tab-btn.active {
  color: #2c5aa0;
  border-bottom-color: #2c5aa0;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
}

.feedback-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.feedback-item {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
}

.feedback-item-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.feedback-item-title {
  font-weight: 600;
  color: #2c5aa0;
  margin: 0 0 0.25rem 0;
}

.feedback-item-date {
  font-size: 0.85rem;
  color: #999;
}

.feedback-item-content {
  color: #333;
  line-height: 1.6;
}

.feedback-rating {
  display: inline-flex;
  gap: 0.25rem;
  margin: 0.5rem 0;
}

.star {
  color: #ffd700;
  font-size: 1.2rem;
}

.star.empty {
  color: #ddd;
}

.feedback-tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.tag {
  padding: 0.25rem 0.75rem;
  background: #e3f2fd;
  color: #1976d2;
  border-radius: 4px;
  font-size: 0.85rem;
}

.export-section {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 2rem;
}

.export-section h3 {
  margin: 0 0 0.5rem 0;
  color: #2c5aa0;
}

.export-section p {
  color: #666;
  margin: 0 0 1.5rem 0;
}

.export-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-primary,
.btn-secondary,
.btn-danger {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
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
  background: #f44336;
  color: white;
}

.btn-danger:hover {
  background: #d32f2f;
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
let allFeedback = {
  summary: [],
  concept: [],
  recommendation: []
};

function loadAllFeedback() {
  // Load summary feedback
  const summaryLog = JSON.parse(localStorage.getItem('ai_feedback_log') || '[]');
  allFeedback.summary = summaryLog;

  // Load concept validations
  const conceptLog = JSON.parse(localStorage.getItem('concept_validation_log') || '[]');
  allFeedback.concept = conceptLog;

  // Load recommendation ratings
  const recommendationLog = JSON.parse(localStorage.getItem('recommendation_rating_log') || '[]');
  allFeedback.recommendation = recommendationLog;

  // Count annotations
  let annotationCount = 0;
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key.startsWith('annotations_')) {
      const annotations = JSON.parse(localStorage.getItem(key) || '[]');
      annotationCount += annotations.length;
    }
  }

  // Update stats
  document.getElementById('summaryFeedbackCount').textContent = allFeedback.summary.length;
  document.getElementById('conceptValidationCount').textContent = allFeedback.concept.length;
  document.getElementById('recommendationRatingCount').textContent = allFeedback.recommendation.length;
  document.getElementById('annotationCount').textContent = annotationCount;

  // Render lists
  renderSummaryFeedback();
  renderConceptValidation();
  renderRecommendationRatings();
}

function renderSummaryFeedback() {
  const list = document.getElementById('summaryFeedbackList');
  
  if (allFeedback.summary.length === 0) {
    list.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">⭐</div>
        <p>No summary feedback yet</p>
        <p style="font-size: 0.9rem;">Rate AI summaries in the paper reader to see them here</p>
      </div>
    `;
    return;
  }

  list.innerHTML = allFeedback.summary.map(feedback => `
    <div class="feedback-item">
      <div class="feedback-item-header">
        <div>
          <h3 class="feedback-item-title">Paper: ${feedback.paperId}</h3>
          <div class="feedback-item-date">${new Date(feedback.timestamp).toLocaleString()}</div>
        </div>
      </div>
      <div class="feedback-item-content">
        <div class="feedback-rating">
          ${renderStars(feedback.summaryRating)}
        </div>
        ${feedback.accuracy ? `<p><strong>Accuracy:</strong> ${feedback.accuracy}</p>` : ''}
        ${feedback.improvements && feedback.improvements.length > 0 ? `
          <div class="feedback-tags">
            ${feedback.improvements.map(imp => `<span class="tag">${imp}</span>`).join('')}
          </div>
        ` : ''}
        ${feedback.comments ? `<p style="margin-top: 0.75rem;"><em>"${feedback.comments}"</em></p>` : ''}
      </div>
    </div>
  `).join('');
}

function renderStars(rating) {
  let stars = '';
  for (let i = 1; i <= 5; i++) {
    stars += `<span class="star ${i <= rating ? '' : 'empty'}">★</span>`;
  }
  return stars;
}

function renderConceptValidation() {
  const list = document.getElementById('conceptValidationList');
  
  if (allFeedback.concept.length === 0) {
    list.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">🧠</div>
        <p>No concept validations yet</p>
        <p style="font-size: 0.9rem;">Validate AI-extracted concepts in the paper reader</p>
      </div>
    `;
    return;
  }

  list.innerHTML = allFeedback.concept.map(item => `
    <div class="feedback-item">
      <div class="feedback-item-header">
        <div>
          <h3 class="feedback-item-title">Paper: ${item.paperId}</h3>
          <div class="feedback-item-date">${new Date(item.timestamp).toLocaleString()}</div>
        </div>
      </div>
      <div class="feedback-item-content">
        <p><strong>${item.validations.length}</strong> concepts validated</p>
        <div class="feedback-tags">
          ${item.validations.map(v => `
            <span class="tag" style="background: ${v.validated ? '#e8f5e9' : '#ffebee'}; color: ${v.validated ? '#2e7d32' : '#c62828'};">
              ${v.validated ? '✓' : '✗'} ${v.concept}
            </span>
          `).join('')}
        </div>
      </div>
    </div>
  `).join('');
}

function renderRecommendationRatings() {
  const list = document.getElementById('recommendationRatingList');
  
  if (allFeedback.recommendation.length === 0) {
    list.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">👍</div>
        <p>No recommendation ratings yet</p>
        <p style="font-size: 0.9rem;">Rate paper recommendations to see them here</p>
      </div>
    `;
    return;
  }

  list.innerHTML = allFeedback.recommendation.map(item => `
    <div class="feedback-item">
      <div class="feedback-item-header">
        <div>
          <h3 class="feedback-item-title">Paper: ${item.paperId}</h3>
          <div class="feedback-item-date">${new Date(item.timestamp).toLocaleString()}</div>
        </div>
      </div>
      <div class="feedback-item-content">
        <p>
          <strong>Helpful:</strong> 
          <span style="color: ${item.isHelpful ? '#4caf50' : '#f44336'}; font-weight: 600;">
            ${item.isHelpful ? '👍 Yes' : '👎 No'}
          </span>
        </p>
        ${item.feedback ? `<p style="margin-top: 0.5rem;"><em>"${item.feedback}"</em></p>` : ''}
      </div>
    </div>
  `).join('');
}

function switchTab(tabName) {
  // Update buttons
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');

  // Update content
  document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
  document.getElementById(tabName + 'Tab').classList.add('active');
}

function exportAllFeedback(format) {
  const data = {
    exportedAt: new Date().toISOString(),
    summary: allFeedback.summary,
    concept: allFeedback.concept,
    recommendation: allFeedback.recommendation
  };

  let content, filename, mimeType;

  if (format === 'json') {
    content = JSON.stringify(data, null, 2);
    filename = `feedback_export_${Date.now()}.json`;
    mimeType = 'application/json';
  } else if (format === 'csv') {
    content = convertToCSV(data);
    filename = `feedback_export_${Date.now()}.csv`;
    mimeType = 'text/csv';
  }

  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  showNotification(`✓ Exported feedback as ${format.toUpperCase()}`, 'success');
}

function convertToCSV(data) {
  let csv = 'Type,Paper ID,Timestamp,Details\n';

  data.summary.forEach(item => {
    csv += `Summary Rating,${item.paperId},${item.timestamp},"Rating: ${item.summaryRating}/5, Accuracy: ${item.accuracy || 'N/A'}"\n`;
  });

  data.concept.forEach(item => {
    const concepts = item.validations.map(v => `${v.concept}:${v.validated}`).join('; ');
    csv += `Concept Validation,${item.paperId},${item.timestamp},"${concepts}"\n`;
  });

  data.recommendation.forEach(item => {
    csv += `Recommendation Rating,${item.paperId},${item.timestamp},"Helpful: ${item.isHelpful}, Feedback: ${item.feedback || 'N/A'}"\n`;
  });

  return csv;
}

function clearAllFeedback() {
  if (!confirm('Are you sure you want to delete ALL feedback? This cannot be undone.')) {
    return;
  }

  if (!confirm('This will permanently delete all your feedback data. Continue?')) {
    return;
  }

  // Clear all feedback keys
  const keysToRemove = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key.includes('feedback') || key.includes('validation') || key.includes('rating')) {
      keysToRemove.push(key);
    }
  }

  keysToRemove.forEach(key => localStorage.removeItem(key));

  showNotification('✓ All feedback cleared', 'success');
  setTimeout(() => location.reload(), 1000);
}

function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 1rem 1.5rem;
    background: ${type === 'success' ? '#4caf50' : type === 'error' ? '#f44336' : '#2196f3'};
    color: white;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    z-index: 10000;
    font-weight: 500;
    animation: slideIn 0.3s ease-out;
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease-out';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// Initialize
loadAllFeedback();
</script>
