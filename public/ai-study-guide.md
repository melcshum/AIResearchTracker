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

.scaffold-hint {
  font-style: italic;
  margin: 1rem 0;
  padding: 1rem;
  background: #e3f2fd;
  border-radius: 6px;
  color: #1565c0;
}

/* Construction Scaffold Styles (DP2-Aligned) */
.construction-scaffold {
  padding: 2rem;
}

.scaffold-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #2c5aa0;
}

.scaffold-header h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.scaffold-intro {
  color: #555;
  font-size: 1.1rem;
}

.scaffold-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #2c5aa0;
}

.scaffold-section h4 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.scaffold-note, .scaffold-tip {
  font-style: italic;
  color: #666;
  margin: 0.5rem 0;
  font-size: 0.95rem;
}

.concept-suggestions {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.concept-suggestion-card {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #e0e0e0;
}

.concept-name {
  font-weight: 600;
  color: #2c5aa0;
  margin-bottom: 0.5rem;
}

.concept-count {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.concept-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 1rem;
  margin: 0.5rem 0;
}

.flashcard-builder {
  margin: 1rem 0;
}

.flashcard-template {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border: 1px solid #e0e0e0;
}

.flashcard-question, .flashcard-answer {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  font-family: inherit;
}

.flashcard-answer {
  resize: vertical;
}

.connection-builder {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  background: white;
  padding: 1rem;
  border-radius: 6px;
}

.concept-select {
  padding: 0.5rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  min-width: 150px;
}

.connection-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  min-width: 200px;
}

.scaffold-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.ai-hints {
  margin-top: 2rem;
  padding: 1.5rem;
  background: #fff3e0;
  border: 1px solid #ff9800;
  border-radius: 8px;
}

.ai-hints h4 {
  color: #e65100;
  margin-bottom: 1rem;
}

.hint-section {
  margin: 1rem 0;
  padding: 1rem;
  background: white;
  border-radius: 6px;
}

.hint-section h5 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.hint-warning {
  color: #e65100;
  font-style: italic;
  margin-top: 1rem;
  padding: 0.75rem;
  background: #ffe0b2;
  border-radius: 4px;
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

// DP2-Aligned: Scaffold learner to construct their own study guide
function generateStudyGuide() {
  const savedPapers = userBookmarks.map(id => allPapers.find(p => p.arxiv_id === id)).filter(p => p);
  
  if (savedPapers.length === 0) {
    return `
<div class="empty-state">
  <h3>📚 Build Your Study Guide</h3>
  <p>No papers saved yet. Save papers from the search page to begin constructing your study materials.</p>
  <p class="scaffold-hint"><strong>Why construct your own?</strong> Research shows that actively creating study materials leads to deeper understanding and better retention than passively reviewing AI-generated content.</p>
  <a href="/public/search.html" class="btn-primary">Browse Papers</a>
</div>`;
  }
  
  const concepts = extractKeyConcepts(savedPapers);
  
  // Scaffold: Ask learner to construct their own guide
  let guide = '';
  
  guide += `
<div class="construction-scaffold">
  <div class="scaffold-header">
    <h3>🛠️ Construct Your Study Guide</h3>
    <p class="scaffold-intro">You have <strong>${savedPapers.length} papers</strong> covering <strong>${Object.keys(concepts).length} key concepts</strong>. Let's build your study materials together.</p>
  </div>
  
  <div class="scaffold-section">
    <h4>Step 1: Identify Key Concepts</h4>
    <p>Based on your papers, what are the main concepts you want to study? Here are some suggestions:</p>
    <div class="concept-suggestions">
      ${Object.entries(concepts).map(([concept, papers]) => `
        <div class="concept-suggestion-card">
          <div class="concept-name">${concept}</div>
          <div class="concept-count">${papers.length} paper${papers.length > 1 ? 's' : ''}</div>
          <button onclick="selectConcept('${concept}')" class="btn-secondary">Use This Concept</button>
        </div>
      `).join('')}
    </div>
    <p class="scaffold-note">Or write your own concept:</p>
    <input type="text" id="customConcept" class="concept-input" placeholder="Enter your own concept...">
    <button onclick="addCustomConcept()" class="btn-primary">Add Concept</button>
  </div>
  
  <div class="scaffold-section">
    <h4>Step 2: Create Your Own Flashcards</h4>
    <p>For each concept, write questions and answers in your own words:</p>
    <div id="flashcardBuilder" class="flashcard-builder">
      <div class="flashcard-template">
        <input type="text" class="flashcard-question" placeholder="Question (e.g., 'What is RAG?')">
        <textarea class="flashcard-answer" rows="3" placeholder="Your answer in your own words..."></textarea>
        <button onclick="addFlashcard()" class="btn-primary">Add Flashcard</button>
      </div>
    </div>
    <p class="scaffold-tip"><strong>Tip:</strong> Writing questions helps you identify what you don't know yet. Writing answers helps you organize your understanding.</p>
  </div>
  
  <div class="scaffold-section">
    <h4>Step 3: Map Connections</h4>
    <p>How do these concepts relate to each other? Draw connections:</p>
    <div id="connectionBuilder" class="connection-builder">
      <select id="concept1" class="concept-select"></select>
      <span>→</span>
      <select id="concept2" class="concept-select"></select>
      <input type="text" id="connectionDescription" class="connection-input" placeholder="How are they related?">
      <button onclick="addConnection()" class="btn-primary">Add Connection</button>
    </div>
  </div>
  
  <div class="scaffold-actions">
    <button onclick="saveStudyGuide()" class="btn-primary btn-large">Save My Study Guide</button>
    <button onclick="getAIHints()" class="btn-secondary">Get AI Hints (Optional)</button>
  </div>
  
  <div id="aiHints" class="ai-hints" style="display:none;">
    <h4>💡 AI Suggestions (for reference only)</h4>
    <p>Use these to check your work, not to replace your thinking:</p>
    <div id="hintsContent"></div>
  </div>
</div>`;
  
  return guide;
}

// Scaffold helper functions
function selectConcept(concept) {
  document.getElementById('customConcept').value = concept;
  alert(`Selected "${concept}". Now create flashcards for this concept!`);
}

function addCustomConcept() {
  const concept = document.getElementById('customConcept').value.trim();
  if (!concept) {
    alert('Please enter a concept name.');
    return;
  }
  alert(`Added "${concept}". Now create flashcards for it!`);
  document.getElementById('customConcept').value = '';
}

function addFlashcard() {
  const templates = document.querySelectorAll('.flashcard-template');
  const lastTemplate = templates[templates.length - 1];
  const question = lastTemplate.querySelector('.flashcard-question').value.trim();
  const answer = lastTemplate.querySelector('.flashcard-answer').value.trim();
  
  if (!question || !answer) {
    alert('Please fill in both question and answer.');
    return;
  }
  
  // Add new template for next flashcard
  const newTemplate = lastTemplate.cloneNode(true);
  newTemplate.querySelector('.flashcard-question').value = '';
  newTemplate.querySelector('.flashcard-answer').value = '';
  document.getElementById('flashcardBuilder').appendChild(newTemplate);
  
  alert('Flashcard added! Add another or save your study guide.');
}

function addConnection() {
  const concept1 = document.getElementById('concept1').value;
  const concept2 = document.getElementById('concept2').value;
  const description = document.getElementById('connectionDescription').value.trim();
  
  if (!concept1 || !concept2 || !description) {
    alert('Please fill in all fields.');
    return;
  }
  
  alert(`Connection saved: ${concept1} → ${concept2}: ${description}`);
  document.getElementById('connectionDescription').value = '';
}

function saveStudyGuide() {
  // TODO: Save to user data
  alert('Study guide saved! Your construction is now part of your learning journey.');
}

async function getAIHints() {
  const hintsDiv = document.getElementById('aiHints');
  hintsDiv.style.display = 'block';
  const hintsContent = document.getElementById('hintsContent');
  
  hintsContent.innerHTML = '<p>Analyzing your papers...</p>';
  
  try {
    const response = await fetch(API_BASE + '/api/wiki/companion', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        mode: 'scaffold',
        action: 'suggest_structure',
        concept: 'Study Guide Structure',
        explanation: 'I have ' + userBookmarks.length + ' papers and want to create a study guide.'
      })
    });
    
    const feedback = await response.json();
    
    hintsContent.innerHTML = `
      <div class="hint-section">
        <h5>Suggested Concepts to Cover:</h5>
        <ul>${feedback.suggestions || ['RAG, Agents, Reasoning'].map(s => `<li>${s}</li>`).join('')}</ul>
      </div>
      <div class="hint-section">
        <h5>Recommended Flashcard Types:</h5>
        <ul>
          <li>Definition cards (What is X?)</li>
          <li>Comparison cards (How does X differ from Y?)</li>
          <li>Application cards (When would you use X?)</li>
        </ul>
      </div>
      <p class="hint-warning"><strong>Remember:</strong> These are suggestions only. Your own thinking is more valuable!</p>
    `;
    
  } catch (error) {
    hintsContent.innerHTML = '<p>Failed to load hints. Continue building on your own!</p>';
  }
}

// Remove old auto-generation code (lines 494-543)
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
