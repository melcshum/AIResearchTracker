---
title: "Compare Papers"
---

<div class="compare-container">
<div class="compare-header">
<h2>📊 Compare Papers</h2>
<p class="subtitle">Analyze multiple papers side-by-side to understand different approaches</p>
</div>

<div class="compare-controls">
<div class="paper-selector">
<label>Select papers to compare:</label>
<div id="paperCheckboxes" class="paper-checkboxes"></div>
</div>
<button id="compareBtn" class="btn-primary" disabled>Compare Selected (0)</button>
</div>

<div id="comparisonView" class="comparison-view" style="display: none;">
<div class="comparison-header">
<h3>Paper Comparison</h3>
<button id="closeComparison" class="btn-secondary">Close</button>
</div>
<div id="comparisonContent" class="comparison-content"></div>
</div>
</div>

<style>
.compare-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.compare-header {
  margin-bottom: 30px;
}

.compare-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.compare-controls {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
}

.paper-selector label {
  display: block;
  font-weight: 600;
  margin-bottom: 15px;
  color: #2c3e50;
}

.paper-checkboxes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 10px;
  max-height: 400px;
  overflow-y: auto;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  background: #f8f9fa;
}

.paper-checkbox {
  display: flex;
  align-items: start;
  gap: 10px;
  padding: 10px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.paper-checkbox:hover {
  border-color: #2c5aa0;
  background: #f0f7ff;
}

.paper-checkbox input[type="checkbox"] {
  margin-top: 3px;
  cursor: pointer;
}

.paper-checkbox-content {
  flex: 1;
  min-width: 0;
}

.paper-checkbox-title {
  font-weight: 600;
  color: #2c3e50;
  font-size: 14px;
  margin-bottom: 5px;
  line-height: 1.4;
}

.paper-checkbox-meta {
  font-size: 12px;
  color: #7f8c8d;
}

.btn-primary, .btn-secondary {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 15px;
}

.btn-primary {
  background: #2c5aa0;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #1e4a8f;
}

.btn-primary:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.btn-secondary {
  background: #e0e0e0;
  color: #333;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.comparison-view {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
}

.comparison-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e0e0e0;
}

.comparison-header h3 {
  margin: 0;
  color: #2c3e50;
}

.comparison-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.comparison-section {
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  overflow: hidden;
}

.comparison-section-header {
  background: #f8f9fa;
  padding: 15px;
  font-weight: 600;
  color: #2c3e50;
  border-bottom: 1px solid #e0e0e0;
}

.comparison-section-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0;
}

.comparison-cell {
  padding: 15px;
  border-right: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
}

.comparison-cell:last-child {
  border-right: none;
}

.comparison-cell-title {
  font-weight: 600;
  color: #2c5aa0;
  margin-bottom: 10px;
  font-size: 14px;
}

.comparison-cell-content {
  color: #555;
  line-height: 1.6;
  font-size: 14px;
}

.comparison-cell-content p {
  margin: 0 0 10px 0;
}

.comparison-cell-content ul {
  margin: 0;
  padding-left: 20px;
}

.comparison-cell-content li {
  margin-bottom: 5px;
}

.highlight-similar {
  background: #fff3cd;
  padding: 2px 4px;
  border-radius: 3px;
}

.highlight-different {
  background: #d4edda;
  padding: 2px 4px;
  border-radius: 3px;
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
let allPapers = [];
let selectedPapers = [];

async function loadPapers() {
  try {
    const response = await fetch('papers.json');
    allPapers = await response.json();
    renderPaperCheckboxes();
  } catch (error) {
    console.error('Failed to load papers:', error);
  }
}

function renderPaperCheckboxes() {
  const container = document.getElementById('paperCheckboxes');
  
  if (allPapers.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">📚</div><p>No papers available</p></div>';
    return;
  }
  
  container.innerHTML = allPapers.map(paper => `
    <label class="paper-checkbox">
      <input type="checkbox" value="${paper.arxiv_id}" onchange="updateSelection()">
      <div class="paper-checkbox-content">
        <div class="paper-checkbox-title">${paper.title}</div>
        <div class="paper-checkbox-meta">${paper.date} • ${paper.authors}</div>
      </div>
    </label>
  `).join('');
}

function updateSelection() {
  const checkboxes = document.querySelectorAll('.paper-checkboxes input[type="checkbox"]:checked');
  selectedPapers = Array.from(checkboxes).map(cb => cb.value);
  
  const compareBtn = document.getElementById('compareBtn');
  compareBtn.textContent = `Compare Selected (${selectedPapers.length})`;
  compareBtn.disabled = selectedPapers.length < 2;
}

function comparePapers() {
  if (selectedPapers.length < 2) {
    alert('Please select at least 2 papers to compare');
    return;
  }
  
  const papers = selectedPapers
    .map(id => allPapers.find(p => p.arxiv_id === id))
    .filter(p => p);
  
  renderComparison(papers);
}

function renderComparison(papers) {
  const view = document.getElementById('comparisonView');
  const content = document.getElementById('comparisonContent');
  
  view.style.display = 'block';
  
  let html = '';
  
  // Basic Info
  html += `
    <div class="comparison-section">
      <div class="comparison-section-header">📋 Basic Information</div>
      <div class="comparison-section-content">
        ${papers.map(paper => `
          <div class="comparison-cell">
            <div class="comparison-cell-title">${paper.title}</div>
            <div class="comparison-cell-content">
              <p><strong>Authors:</strong> ${paper.authors}</p>
              <p><strong>Date:</strong> ${paper.date}</p>
              <p><strong>arXiv ID:</strong> ${paper.arxiv_id}</p>
              <p><strong>Topics:</strong> ${(paper.topics || []).join(', ')}</p>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  // Abstracts
  html += `
    <div class="comparison-section">
      <div class="comparison-section-header">📝 Abstracts</div>
      <div class="comparison-section-content">
        ${papers.map(paper => `
          <div class="comparison-cell">
            <div class="comparison-cell-title">${paper.title}</div>
            <div class="comparison-cell-content">
              <p>${paper.abstract || 'No abstract available'}</p>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  // Topics Comparison
  const allTopics = [...new Set(papers.flatMap(p => p.topics || []))];
  html += `
    <div class="comparison-section">
      <div class="comparison-section-header">🏷️ Topic Coverage</div>
      <div class="comparison-section-content">
        ${papers.map(paper => {
          const paperTopics = paper.topics || [];
          return `
            <div class="comparison-cell">
              <div class="comparison-cell-title">${paper.title}</div>
              <div class="comparison-cell-content">
                <ul>
                  ${allTopics.map(topic => {
                    const hasTopic = paperTopics.includes(topic);
                    return `<li>${hasTopic ? '✅' : '❌'} ${topic}</li>`;
                  }).join('')}
                </ul>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;
  
  // Key Insights
  html += `
    <div class="comparison-section">
      <div class="comparison-section-header">💡 Key Insights</div>
      <div class="comparison-section-content">
        ${papers.map(paper => `
          <div class="comparison-cell">
            <div class="comparison-cell-title">${paper.title}</div>
            <div class="comparison-cell-content">
              <p><strong>Focus:</strong> ${extractFocus(paper.abstract)}</p>
              <p><strong>Approach:</strong> ${extractApproach(paper.abstract)}</p>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  content.innerHTML = html;
  
  // Scroll to comparison view
  view.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function extractFocus(abstract) {
  if (!abstract) return 'Not specified';
  const sentences = abstract.split(/[.!?]+/);
  return sentences[0] ? sentences[0].trim() + '.' : 'Not specified';
}

function extractApproach(abstract) {
  if (!abstract) return 'Not specified';
  const approachKeywords = ['propose', 'introduce', 'present', 'develop', 'design'];
  const sentences = abstract.split(/[.!?]+/);
  
  for (let sentence of sentences) {
    const lower = sentence.toLowerCase();
    if (approachKeywords.some(kw => lower.includes(kw))) {
      return sentence.trim() + '.';
    }
  }
  
  return sentences.length > 1 ? sentences[1].trim() + '.' : 'Not specified';
}

// Event listeners
document.getElementById('compareBtn').addEventListener('click', comparePapers);
document.getElementById('closeComparison').addEventListener('click', () => {
  document.getElementById('comparisonView').style.display = 'none';
});

// Initialize
document.addEventListener('DOMContentLoaded', loadPapers);
</script>
