---
title: "AI Wiki Assistant"
---

<div class="ai-wiki-container">
<div class="ai-wiki-header">
<h2>🤖 AI Wiki Assistant</h2>
<p class="subtitle">Intelligent knowledge extraction and concept linking powered by AI</p>
</div>

<div class="ai-wiki-controls">
<button id="extractConceptsBtn" class="btn-primary">🔍 Extract Concepts from Papers</button>
<button id="generateExplanationsBtn" class="btn-secondary">📝 Generate AI Explanations</button>
<button id="linkRelatedPapersBtn" class="btn-secondary">🔗 Link Related Papers</button>
</div>

<div class="ai-wiki-stats">
<div class="stat-item">
<span class="stat-label">Concepts Extracted:</span>
<span class="stat-value" id="conceptCount">0</span>
</div>
<div class="stat-item">
<span class="stat-label">AI Explanations:</span>
<span class="stat-value" id="explanationCount">0</span>
</div>
<div class="stat-item">
<span class="stat-label">Paper Links:</span>
<span class="stat-value" id="linkCount">0</span>
</div>
</div>

<div class="ai-wiki-section">
<h3>📚 Extracted Concepts</h3>
<div id="extractedConcepts" class="concept-list"></div>
</div>

<div class="ai-wiki-section">
<h3>💡 AI-Generated Explanations</h3>
<div id="aiExplanations" class="explanation-list"></div>
</div>

<div class="ai-wiki-section">
<h3>🔗 Concept-Paper Connections</h3>
<div id="conceptPaperLinks" class="link-list"></div>
</div>
</div>

<style>
.ai-wiki-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.ai-wiki-header {
  margin-bottom: 30px;
}

.ai-wiki-header h2 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.ai-wiki-controls {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.btn-primary, .btn-secondary {
  padding: 10px 20px;
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

.ai-wiki-stats {
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

.ai-wiki-section {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
}

.ai-wiki-section h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
}

.concept-list, .explanation-list, .link-list {
  display: grid;
  gap: 15px;
}

.concept-card {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
}

.concept-name {
  font-weight: 600;
  color: #2c5aa0;
  font-size: 16px;
  margin-bottom: 8px;
}

.concept-definition {
  color: #555;
  line-height: 1.6;
  margin-bottom: 10px;
}

.concept-papers {
  font-size: 13px;
  color: #7f8c8d;
}

.concept-papers a {
  color: #2c5aa0;
  text-decoration: none;
  margin-right: 10px;
}

.concept-papers a:hover {
  text-decoration: underline;
}

.explanation-card {
  background: #fff3e0;
  border: 1px solid #ff9800;
  border-radius: 6px;
  padding: 15px;
}

.explanation-concept {
  font-weight: 600;
  color: #f57c00;
  font-size: 16px;
  margin-bottom: 8px;
}

.explanation-text {
  color: #555;
  line-height: 1.6;
}

.link-card {
  background: #e8f5e9;
  border: 1px solid #4caf50;
  border-radius: 6px;
  padding: 15px;
}

.link-concept {
  font-weight: 600;
  color: #2e7d32;
  font-size: 16px;
  margin-bottom: 8px;
}

.link-papers {
  color: #555;
  font-size: 14px;
}

.link-papers a {
  color: #2c5aa0;
  text-decoration: none;
  display: inline-block;
  margin-right: 10px;
  margin-bottom: 5px;
}

.link-papers a:hover {
  text-decoration: underline;
}

.empty-state {
  text-align: center;
  padding: 40px;
  color: #7f8c8d;
  font-style: italic;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #7f8c8d;
}
</style>

<script>
let allPapers = [];
let extractedConcepts = {};
let aiExplanations = {};
let conceptPaperLinks = {};

async function loadWikiData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    // Load existing wiki data from user data
    const userResponse = await fetch('http://localhost:5001/api/user/data');
    const userData = await userResponse.json();
    
    extractedConcepts = userData.wikiConcepts || {};
    aiExplanations = userData.wikiExplanations || {};
    conceptPaperLinks = userData.wikiLinks || {};
    
  } catch (error) {
    console.error('Failed to load wiki data:', error);
  }
}

function extractConceptsFromPapers() {
  const concepts = {};
  
  allPapers.forEach(paper => {
    const title = paper.title || '';
    const abstract = paper.abstract || '';
    const text = (title + ' ' + abstract).toLowerCase();
    
    // Extract key AI/ML concepts
    const conceptPatterns = [
      { pattern: /\b(agent|agents|agentic)\b/gi, concept: 'AI Agent', definition: 'An autonomous system that can perceive its environment, reason about actions, and act to achieve goals.' },
      { pattern: /\b(retrieval|rag|retrieval-augmented)\b/gi, concept: 'Retrieval-Augmented Generation', definition: 'A technique that combines information retrieval with text generation to reduce hallucination and provide citations.' },
      { pattern: /\b(reasoning|chain-of-thought|cot)\b/gi, concept: 'LLM Reasoning', definition: 'The ability of language models to perform logical inference and step-by-step problem solving.' },
      { pattern: /\b(multi-modal|multimodal|vision-language)\b/gi, concept: 'Multi-Modal Learning', definition: 'Models that can process and understand multiple types of data (text, images, audio) simultaneously.' },
      { pattern: /\b(tool use|tool calling)\b/gi, concept: 'Tool Use', definition: 'The capability of AI agents to invoke external tools and APIs to accomplish tasks.' },
      { pattern: /\b(planning|planner)\b/gi, concept: 'Planning', definition: 'The process of breaking down complex tasks into sequential steps to achieve a goal.' },
      { pattern: /\b(memory|context)\b/gi, concept: 'Memory Systems', definition: 'Mechanisms for maintaining context and storing information across interactions.' },
      { pattern: /\b(safety|alignment)\b/gi, concept: 'AI Safety', definition: 'Research focused on ensuring AI systems behave as intended and avoid harmful outcomes.' },
      { pattern: /\b(evaluation|benchmark)\b/gi, concept: 'Evaluation', definition: 'Methods and metrics for assessing AI system performance and capabilities.' },
      { pattern: /\b(gui|graphical user interface)\b/gi, concept: 'GUI Agents', definition: 'AI agents that can interact with graphical user interfaces to automate tasks.' },
      { pattern: /\b(embedding|vector)\b/gi, concept: 'Embeddings', definition: 'Dense vector representations of text or other data that capture semantic meaning.' },
      { pattern: /\b(hallucination)\b/gi, concept: 'Hallucination', definition: 'When AI models generate information that is not grounded in facts or context.' }
    ];
    
    conceptPatterns.forEach(({ pattern, concept, definition }) => {
      if (text.match(pattern)) {
        if (!concepts[concept]) {
          concepts[concept] = {
            definition: definition,
            papers: []
          };
        }
        concepts[concept].papers.push({
          id: paper.arxiv_id,
          title: paper.title,
          url: paper.url
        });
      }
    });
  });
  
  return concepts;
}

function generateAIExplanations(concepts) {
  const explanations = {};
  
  Object.entries(concepts).forEach(([conceptName, conceptData]) => {
    const paperCount = conceptData.papers.length;
    const paperTitles = conceptData.papers.slice(0, 3).map(p => p.title);
    
    explanations[conceptName] = {
      explanation: `${conceptData.definition} This concept appears in ${paperCount} paper${paperCount !== 1 ? 's' : ''} in your collection${paperTitles.length > 0 ? ', including: ' + paperTitles.join(', ') : ''}.`,
      generatedAt: new Date().toISOString()
    };
  });
  
  return explanations;
}

function linkConceptsToPapers(concepts) {
  const links = {};
  
  Object.entries(concepts).forEach(([conceptName, conceptData]) => {
    links[conceptName] = conceptData.papers;
  });
  
  return links;
}

async function saveWikiData() {
  try {
    await fetch('http://localhost:5001/api/user/wiki-data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        wikiConcepts: extractedConcepts,
        wikiExplanations: aiExplanations,
        wikiLinks: conceptPaperLinks
      })
    });
  } catch (error) {
    console.error('Failed to save wiki data:', error);
  }
}

function renderConcepts() {
  const container = document.getElementById('extractedConcepts');
  
  if (Object.keys(extractedConcepts).length === 0) {
    container.innerHTML = '<div class="empty-state">No concepts extracted yet. Click "Extract Concepts from Papers" to begin.</div>';
    return;
  }
  
  container.innerHTML = Object.entries(extractedConcepts).map(([name, data]) => `
    <div class="concept-card">
      <div class="concept-name">${name}</div>
      <div class="concept-definition">${data.definition}</div>
      <div class="concept-papers">
        Found in ${data.papers.length} paper${data.papers.length !== 1 ? 's' : ''}: 
        ${data.papers.slice(0, 3).map(p => `<a href="${p.url}" target="_blank">${p.title.substring(0, 50)}...</a>`).join(', ')}
      </div>
    </div>
  `).join('');
}

function renderExplanations() {
  const container = document.getElementById('aiExplanations');
  
  if (Object.keys(aiExplanations).length === 0) {
    container.innerHTML = '<div class="empty-state">No explanations generated yet. Click "Generate AI Explanations" to create them.</div>';
    return;
  }
  
  container.innerHTML = Object.entries(aiExplanations).map(([concept, data]) => `
    <div class="explanation-card">
      <div class="explanation-concept">${concept}</div>
      <div class="explanation-text">${data.explanation}</div>
    </div>
  `).join('');
}

function renderLinks() {
  const container = document.getElementById('conceptPaperLinks');
  
  if (Object.keys(conceptPaperLinks).length === 0) {
    container.innerHTML = '<div class="empty-state">No links created yet. Click "Link Related Papers" to create connections.</div>';
    return;
  }
  
  container.innerHTML = Object.entries(conceptPaperLinks).map(([concept, papers]) => `
    <div class="link-card">
      <div class="link-concept">${concept}</div>
      <div class="link-papers">
        ${papers.map(p => `<a href="${p.url}" target="_blank">${p.title.substring(0, 60)}...</a>`).join('')}
      </div>
    </div>
  `).join('');
}

function updateStats() {
  document.getElementById('conceptCount').textContent = Object.keys(extractedConcepts).length;
  document.getElementById('explanationCount').textContent = Object.keys(aiExplanations).length;
  document.getElementById('linkCount').textContent = Object.keys(conceptPaperLinks).length;
}

// Event listeners
document.getElementById('extractConceptsBtn').addEventListener('click', () => {
  const btn = document.getElementById('extractConceptsBtn');
  btn.textContent = '⏳ Extracting...';
  btn.disabled = true;
  
  setTimeout(() => {
    extractedConcepts = extractConceptsFromPapers();
    renderConcepts();
    updateStats();
    saveWikiData();
    btn.textContent = '🔍 Extract Concepts from Papers';
    btn.disabled = false;
  }, 500);
});

document.getElementById('generateExplanationsBtn').addEventListener('click', () => {
  const btn = document.getElementById('generateExplanationsBtn');
  btn.textContent = '⏳ Generating...';
  btn.disabled = true;
  
  setTimeout(() => {
    if (Object.keys(extractedConcepts).length === 0) {
      alert('Please extract concepts first!');
      btn.textContent = '📝 Generate AI Explanations';
      btn.disabled = false;
      return;
    }
    
    aiExplanations = generateAIExplanations(extractedConcepts);
    renderExplanations();
    updateStats();
    saveWikiData();
    btn.textContent = '📝 Generate AI Explanations';
    btn.disabled = false;
  }, 500);
});

document.getElementById('linkRelatedPapersBtn').addEventListener('click', () => {
  const btn = document.getElementById('linkRelatedPapersBtn');
  btn.textContent = '⏳ Linking...';
  btn.disabled = true;
  
  setTimeout(() => {
    if (Object.keys(extractedConcepts).length === 0) {
      alert('Please extract concepts first!');
      btn.textContent = '🔗 Link Related Papers';
      btn.disabled = false;
      return;
    }
    
    conceptPaperLinks = linkConceptsToPapers(extractedConcepts);
    renderLinks();
    updateStats();
    saveWikiData();
    btn.textContent = '🔗 Link Related Papers';
    btn.disabled = false;
  }, 500);
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadWikiData().then(() => {
    renderConcepts();
    renderExplanations();
    renderLinks();
    updateStats();
  });
});
</script>
