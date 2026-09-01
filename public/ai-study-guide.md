---
title: "AI Study Guide"
---

<div class="study-guide-container">
<div class="guide-header">
<h2>🎓 AI Study Guide</h2>
<p class="subtitle">Auto-generated study materials from your saved papers</p>
</div>

<div class="guide-controls">
<button id="generateGuideBtn" class="btn-primary">📚 Generate Study Guide</button>
<button id="exportGuideBtn" class="btn-secondary">📥 Export as Markdown</button>
</div>

<div id="studyGuideContent" class="study-guide-content">
<div class="empty-state">
<p>Click "Generate Study Guide" to create personalized study materials based on your saved papers and notes.</p>
</div>
</div>
</div>

<style>
.study-guide-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.guide-header {
  margin-bottom: 30px;
}

.guide-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.guide-controls {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
}

.btn-primary, .btn-secondary {
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
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

.study-guide-content {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 30px;
  line-height: 1.8;
}

.study-guide-content h3 {
  color: #2c3e50;
  margin-top: 30px;
  margin-bottom: 15px;
  border-bottom: 2px solid #2c5aa0;
  padding-bottom: 10px;
}

.study-guide-content h4 {
  color: #2c5aa0;
  margin-top: 25px;
  margin-bottom: 10px;
}

.concept-card {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
  margin: 15px 0;
}

.concept-title {
  font-weight: 600;
  color: #2c5aa0;
  margin-bottom: 8px;
  font-size: 16px;
}

.concept-definition {
  color: #555;
  margin-bottom: 10px;
}

.concept-papers {
  font-size: 13px;
  color: #7f8c8d;
}

.flashcard {
  background: #fff3e0;
  border: 1px solid #ff9800;
  border-radius: 6px;
  padding: 15px;
  margin: 10px 0;
}

.flashcard-question {
  font-weight: 600;
  color: #f57c00;
  margin-bottom: 8px;
}

.flashcard-answer {
  color: #555;
  padding-left: 15px;
  border-left: 3px solid #ff9800;
}

.key-insight {
  background: #e8f5e9;
  border-left: 4px solid #4caf50;
  padding: 15px;
  margin: 15px 0;
}

.key-insight-label {
  font-weight: 600;
  color: #2e7d32;
  margin-bottom: 5px;
}

.connection-map {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 20px;
  margin: 15px 0;
}

.connection-item {
  padding: 8px 0;
  border-bottom: 1px solid #e0e0e0;
}

.connection-item:last-child {
  border-bottom: none;
}

.connection-concepts {
  color: #2c5aa0;
  font-weight: 600;
}

.connection-description {
  color: #555;
  font-size: 14px;
  margin-top: 5px;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #7f8c8d;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #7f8c8d;
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
let allPapers = [];
let userBookmarks = [];
let userNotes = {};
let userSummaries = {};

async function loadStudyData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(API_BASE + '/api/user/data');
    const userData = await userResponse.json();
    userBookmarks = userData.bookmarks || [];
    userNotes = userData.notes || {};
    
    const summariesResponse = await fetch(API_BASE + '/api/user/summaries');
    const summariesData = await summariesResponse.json();
    userSummaries = summariesData.summaries || {};
    
  } catch (error) {
    console.error('Failed to load study data:', error);
  }
}

function extractKeyConcepts(papers) {
  const concepts = {};
  
  papers.forEach(paper => {
    const title = paper.title.toLowerCase();
    const abstract = (paper.abstract || '').toLowerCase();
    const text = title + ' ' + abstract;
    
    // Extract common AI/ML concepts
    const conceptPatterns = [
      { pattern: /\b(agent|agents|agentic)\b/gi, concept: 'AI Agents' },
      { pattern: /\b(retrieval|rag|retrieval-augmented)\b/gi, concept: 'Retrieval-Augmented Generation' },
      { pattern: /\b(reasoning|chain-of-thought|cot)\b/gi, concept: 'LLM Reasoning' },
      { pattern: /\b(multi-modal|multimodal|vision-language)\b/gi, concept: 'Multi-Modal Learning' },
      { pattern: /\b(tool use|tool calling)\b/gi, concept: 'Tool Use' },
      { pattern: /\b(planning|planner)\b/gi, concept: 'Planning' },
      { pattern: /\b(memory|context)\b/gi, concept: 'Memory & Context' },
      { pattern: /\b(safety|alignment)\b/gi, concept: 'AI Safety' },
      { pattern: /\b(evaluation|benchmark)\b/gi, concept: 'Evaluation' },
      { pattern: /\b(gui|graphical user interface)\b/gi, concept: 'GUI Agents' }
    ];
    
    conceptPatterns.forEach(({ pattern, concept }) => {
      if (text.match(pattern)) {
        if (!concepts[concept]) {
          concepts[concept] = [];
        }
        concepts[concept].push(paper);
      }
    });
  });
  
  return concepts;
}

function generateFlashcards(papers, notes) {
  const flashcards = [];
  
  papers.forEach(paper => {
    const note = notes[paper.arxiv_id];
    if (note && note.length > 20) {
      flashcards.push({
        question: `What is the main contribution of "${paper.title}"?`,
        answer: note.substring(0, 200) + (note.length > 200 ? '...' : '')
      });
    }
    
    // Generate from abstract
    if (paper.abstract) {
      const sentences = paper.abstract.split(/[.!?]+/).filter(s => s.trim().length > 30);
      if (sentences.length > 0) {
        flashcards.push({
          question: `What problem does "${paper.title}" address?`,
          answer: sentences[0].trim()
        });
      }
    }
  });
  
  return flashcards.slice(0, 10); // Limit to 10 flashcards
}

function generateConnections(concepts) {
  const connections = [];
  const conceptNames = Object.keys(concepts);
  
  // Find papers that appear in multiple concepts
  for (let i = 0; i < conceptNames.length; i++) {
    for (let j = i + 1; j < conceptNames.length; j++) {
      const papers1 = new Set(concepts[conceptNames[i]].map(p => p.arxiv_id));
      const papers2 = concepts[conceptNames[j]].filter(p => papers1.has(p.arxiv_id));
      
      if (papers2.length > 0) {
        connections.push({
          concept1: conceptNames[i],
          concept2: conceptNames[j],
          count: papers2.length,
          description: `${papers2.length} paper${papers2.length > 1 ? 's' : ''} explore both ${conceptNames[i]} and ${conceptNames[j]}`
        });
      }
    }
  }
  
  return connections.sort((a, b) => b.count - a.count).slice(0, 5);
}

function generateStudyGuide() {
  const savedPapers = userBookmarks.map(id => allPapers.find(p => p.arxiv_id === id)).filter(p => p);
  
  if (savedPapers.length === 0) {
    return '<div class="empty-state"><p>No papers saved yet. Save papers from the search page to generate a study guide.</p></div>';
  }
  
  const concepts = extractKeyConcepts(savedPapers);
  const flashcards = generateFlashcards(savedPapers, userNotes);
  const connections = generateConnections(concepts);
  
  let guide = '';
  
  // Overview
  guide += '<h3>📖 Study Overview</h3>';
  guide += `<p>You have saved <strong>${savedPapers.length} papers</strong> covering <strong>${Object.keys(concepts).length} key concepts</strong>.</p>`;
  
  // Key Concepts
  guide += '<h3>🎯 Key Concepts</h3>';
  Object.entries(concepts).forEach(([concept, papers]) => {
    guide += `
<div class="concept-card">
<div class="concept-title">${concept}</div>
<div class="concept-definition">Found in ${papers.length} paper${papers.length > 1 ? 's' : ''} in your collection</div>
<div class="concept-papers">
          ${papers.slice(0, 3).map(p => `<a href="${p.url}" target="_blank">${p.title.substring(0, 60)}...</a>`).join(', ')}
</div>
</div>
    `;
  });
  
  // Key Insights from Notes
  const papersWithNotes = savedPapers.filter(p => userNotes[p.arxiv_id]);
  if (papersWithNotes.length > 0) {
    guide += '<h3>💡 Key Insights from Your Notes</h3>';
    papersWithNotes.slice(0, 5).forEach(paper => {
      const note = userNotes[paper.arxiv_id];
      guide += `
<div class="key-insight">
<div class="key-insight-label">From: ${paper.title}</div>
<div>${note.substring(0, 300)}${note.length > 300 ? '...' : ''}</div>
</div>
      `;
    });
  }
  
  // Flashcards
  if (flashcards.length > 0) {
    guide += '<h3>📝 Study Flashcards</h3>';
    guide += '<p>Test your understanding with these auto-generated questions:</p>';
    flashcards.forEach(card => {
      guide += `
<div class="flashcard">
<div class="flashcard-question">Q: ${card.question}</div>
<div class="flashcard-answer">A: ${card.answer}</div>
</div>
      `;
    });
  }
  
  // Concept Connections
  if (connections.length > 0) {
    guide += '<h3>🔗 Concept Connections</h3>';
    guide += '<p>See how different research areas relate to each other:</p>';
    guide += '<div class="connection-map">';
    connections.forEach(conn => {
      guide += `
<div class="connection-item">
<div class="connection-concepts">${conn.concept1} ↔ ${conn.concept2}</div>
<div class="connection-description">${conn.description}</div>
</div>
      `;
    });
    guide += '</div>';
  }
  
  // Study Recommendations
  guide += '<h3>📚 Study Recommendations</h3>';
  guide += '<ol>';
  guide += '<li><strong>Start with the basics:</strong> Review papers on fundamental concepts first</li>';
  guide += '<li><strong>Follow the connections:</strong> Explore how concepts relate across papers</li>';
  guide += '<li><strong>Use flashcards:</strong> Test your understanding regularly</li>';
  guide += '<li><strong>Add more notes:</strong> The more you note, the better your study guide becomes</li>';
  guide += '</ol>';
  
  return guide;
}

function exportAsMarkdown() {
  const content = document.getElementById('studyGuideContent').innerHTML;
  
  // Simple HTML to Markdown conversion
  let md = '# AI Study Guide\n\n';
  md += `*Generated on ${new Date().toLocaleDateString()}*\n\n`;
  md += '---\n\n';
  
  // Extract text content (simplified)
  const tempDiv = document.createElement('div');
  tempDiv.innerHTML = content;
  md += tempDiv.textContent.replace(/\s+/g, ' ').trim();
  
  const blob = new Blob([md], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'study-guide.md';
  a.click();
  URL.revokeObjectURL(url);
}

// Event listeners
document.getElementById('generateGuideBtn').addEventListener('click', () => {
  const btn = document.getElementById('generateGuideBtn');
  btn.textContent = '⏳ Generating...';
  btn.disabled = true;
  
  setTimeout(() => {
    const guide = generateStudyGuide();
    document.getElementById('studyGuideContent').innerHTML = guide;
    btn.textContent = '📚 Generate Study Guide';
    btn.disabled = false;
  }, 500);
});

document.getElementById('exportGuideBtn').addEventListener('click', exportAsMarkdown);

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadStudyData();
});
</script>
