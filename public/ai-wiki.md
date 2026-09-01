---
title: "AI Wiki - Knowledge Base"
---

<div class="wiki-container">
  <!-- Header with Search -->
  <div class="wiki-header">
    <div class="wiki-title">
      <h2>📚 AI Knowledge Wiki</h2>
      <p class="subtitle">Comprehensive knowledge base of AI concepts, methods, and research</p>
    </div>
    <div class="wiki-search">
      <input type="text" id="wikiSearch" placeholder="Search concepts, definitions, papers..." />
      <button onclick="searchWiki()" class="btn-search">🔍</button>
    </div>
  </div>

  <!-- Navigation Tabs -->
  <div class="wiki-tabs">
    <button class="tab-btn active" onclick="switchTab('browse')">📖 Browse</button>
    <button class="tab-btn" onclick="switchTab('graph')">🕸️ Concept Graph</button>
    <button class="tab-btn" onclick="switchTab('timeline')">📅 Timeline</button>
    <button class="tab-btn" onclick="switchTab('stats')">📊 Statistics</button>
  </div>

  <!-- Browse Tab -->
  <div id="browseTab" class="tab-content active">
    <div class="wiki-filters">
      <select id="categoryFilter" onchange="filterConcepts()">
        <option value="all">All Categories</option>
        <option value="agents">AI Agents</option>
        <option value="reasoning">Reasoning</option>
        <option value="retrieval">Retrieval & RAG</option>
        <option value="multimodal">Multi-Modal</option>
        <option value="safety">Safety & Alignment</option>
        <option value="evaluation">Evaluation</option>
      </select>
      <select id="difficultyFilter" onchange="filterConcepts()">
        <option value="all">All Levels</option>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>
      <select id="sortBy" onchange="filterConcepts()">
        <option value="name">Sort by Name</option>
        <option value="papers">Sort by Paper Count</option>
        <option value="recent">Sort by Recent</option>
      </select>
    </div>

    <div id="conceptGrid" class="concept-grid"></div>
  </div>

  <!-- Graph Tab -->
  <div id="graphTab" class="tab-content">
    <div class="graph-controls">
      <button onclick="resetGraph()" class="btn-secondary">Reset View</button>
      <button onclick="toggleLabels()" class="btn-secondary">Toggle Labels</button>
      <select id="graphLayout" onchange="updateGraphLayout()">
        <option value="force">Force-Directed</option>
        <option value="hierarchical">Hierarchical</option>
        <option value="circular">Circular</option>
      </select>
    </div>
    <div id="conceptGraph" class="graph-container"></div>
  </div>

  <!-- Timeline Tab -->
  <div id="timelineTab" class="tab-content">
    <div id="conceptTimeline" class="timeline-container"></div>
  </div>

  <!-- Stats Tab -->
  <div id="statsTab" class="tab-content">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📚</div>
        <div class="stat-info">
          <div class="stat-number" id="totalConcepts">0</div>
          <div class="stat-label">Total Concepts</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🔗</div>
        <div class="stat-info">
          <div class="stat-number" id="totalRelations">0</div>
          <div class="stat-label">Relationships</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">📄</div>
        <div class="stat-info">
          <div class="stat-number" id="coveredPapers">0</div>
          <div class="stat-label">Papers Covered</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🏷️</div>
        <div class="stat-info">
          <div class="stat-number" id="totalTags">0</div>
          <div class="stat-label">Tags</div>
        </div>
      </div>
    </div>
    <div id="categoryBreakdown" class="category-breakdown"></div>
  </div>

  <!-- Concept Detail Modal -->
  <div id="conceptModal" class="modal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close" onclick="closeConceptModal()">&times;</span>
      <div id="conceptDetail"></div>
    </div>
  </div>
</div>

<style>
.wiki-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.wiki-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 20px;
}

.wiki-title h2 {
  margin: 0 0 5px 0;
  color: #2c3e50;
  font-size: 28px;
}

.subtitle {
  color: #7f8c8d;
  font-size: 14px;
  margin: 0;
}

.wiki-search {
  display: flex;
  gap: 10px;
}

.wiki-search input {
  padding: 10px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  width: 300px;
  transition: border-color 0.2s;
}

.wiki-search input:focus {
  outline: none;
  border-color: #2c5aa0;
}

.btn-search {
  padding: 10px 20px;
  background: #2c5aa0;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}

.btn-search:hover {
  background: #1e4a8f;
}

.wiki-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  border-bottom: 2px solid #e0e0e0;
}

.tab-btn {
  padding: 12px 24px;
  background: transparent;
  border: none;
  border-bottom: 3px solid transparent;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: #7f8c8d;
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

.wiki-filters {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.wiki-filters select {
  padding: 8px 12px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  background: white;
}

.concept-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.concept-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.2s;
}

.concept-card:hover {
  border-color: #2c5aa0;
  box-shadow: 0 4px 12px rgba(44, 90, 160, 0.1);
  transform: translateY(-2px);
}

.concept-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 10px;
}

.concept-name {
  font-size: 18px;
  font-weight: 600;
  color: #2c5aa0;
  margin: 0;
}

.concept-category {
  font-size: 12px;
  padding: 4px 8px;
  background: #e3f2fd;
  color: #1976d2;
  border-radius: 4px;
  font-weight: 600;
}

.concept-definition {
  color: #555;
  line-height: 1.6;
  margin-bottom: 15px;
  font-size: 14px;
}

.concept-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: #7f8c8d;
}

.concept-papers {
  display: flex;
  align-items: center;
  gap: 5px;
}

.concept-difficulty {
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
}

.difficulty-beginner {
  background: #e8f5e9;
  color: #2e7d32;
}

.difficulty-intermediate {
  background: #fff3e0;
  color: #f57c00;
}

.difficulty-advanced {
  background: #ffebee;
  color: #c62828;
}

.graph-container {
  width: 100%;
  height: 600px;
  background: #f8f9fa;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  position: relative;
}

.graph-controls {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

.btn-secondary {
  padding: 8px 16px;
  background: #e0e0e0;
  color: #333;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.timeline-container {
  position: relative;
  padding: 20px 0;
}

.timeline-item {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
  position: relative;
}

.timeline-date {
  min-width: 120px;
  font-weight: 600;
  color: #2c5aa0;
  padding-top: 5px;
}

.timeline-content {
  flex: 1;
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
}

.timeline-concepts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
}

.stat-icon {
  font-size: 36px;
}

.stat-number {
  font-size: 32px;
  font-weight: bold;
  color: #2c5aa0;
}

.stat-label {
  color: #7f8c8d;
  font-size: 14px;
}

.category-breakdown {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
}

.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.5);
}

.modal.active {
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  border-radius: 12px;
  padding: 30px;
  max-width: 800px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.close {
  position: absolute;
  right: 20px;
  top: 20px;
  font-size: 28px;
  font-weight: bold;
  color: #7f8c8d;
  cursor: pointer;
}

.close:hover {
  color: #2c3e50;
}

.concept-detail-header {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 2px solid #e0e0e0;
}

.concept-detail-title {
  font-size: 28px;
  color: #2c5aa0;
  margin: 0 0 10px 0;
}

.concept-detail-meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.concept-detail-section {
  margin-bottom: 25px;
}

.concept-detail-section h3 {
  color: #2c3e50;
  font-size: 18px;
  margin: 0 0 15px 0;
}

.concept-detail-definition {
  color: #555;
  line-height: 1.8;
  font-size: 15px;
}

.related-concepts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.related-concept {
  padding: 6px 12px;
  background: #e3f2fd;
  color: #1976d2;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: background 0.2s;
}

.related-concept:hover {
  background: #bbdefb;
}

.papers-list {
  display: grid;
  gap: 10px;
}

.paper-item {
  padding: 12px;
  background: #f8f9fa;
  border-radius: 6px;
  border-left: 3px solid #2c5aa0;
}

.paper-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.paper-authors {
  font-size: 13px;
  color: #7f8c8d;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #7f8c8d;
}

.empty-state-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .wiki-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .wiki-search input {
    width: 100%;
  }
  
  .concept-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\d+$/, ':5001');

let allPapers = [];
let concepts = {};
let currentTab = 'browse';
let graphInstance = null;
let showLabels = true;

// Comprehensive concept database
const conceptDatabase = {
  'AI Agent': {
    category: 'agents',
    difficulty: 'intermediate',
    definition: 'An autonomous system that can perceive its environment, reason about actions, and act to achieve goals. Agents can operate independently or collaborate with other agents.',
    related: ['Planning', 'Tool Use', 'Memory Systems', 'Multi-Agent Systems'],
    tags: ['autonomy', 'decision-making', 'goal-directed']
  },
  'Multi-Agent Systems': {
    category: 'agents',
    difficulty: 'advanced',
    definition: 'Systems composed of multiple interacting agents that coordinate to solve complex problems. These systems exhibit emergent behaviors through agent interactions.',
    related: ['AI Agent', 'Coordination', 'Game Theory', 'Swarm Intelligence'],
    tags: ['coordination', 'emergence', 'collaboration']
  },
  'Retrieval-Augmented Generation': {
    category: 'retrieval',
    difficulty: 'intermediate',
    definition: 'A technique that combines information retrieval with text generation to reduce hallucination and provide citations. RAG systems retrieve relevant documents and use them as context for generation.',
    related: ['Embeddings', 'Vector Search', 'Knowledge Grounding', 'Hallucination'],
    tags: ['retrieval', 'generation', 'citations']
  },
  'LLM Reasoning': {
    category: 'reasoning',
    difficulty: 'advanced',
    definition: 'The ability of language models to perform logical inference and step-by-step problem solving. Includes techniques like chain-of-thought, tree-of-thought, and self-consistency.',
    related: ['Chain-of-Thought', 'Self-Consistency', 'Verification', 'Logic'],
    tags: ['inference', 'logic', 'problem-solving']
  },
  'Chain-of-Thought': {
    category: 'reasoning',
    difficulty: 'intermediate',
    definition: 'A prompting technique that encourages models to show their reasoning process step-by-step before providing a final answer, improving performance on complex tasks.',
    related: ['LLM Reasoning', 'Prompting', 'Self-Consistency'],
    tags: ['reasoning', 'prompting', 'step-by-step']
  },
  'Multi-Modal Learning': {
    category: 'multimodal',
    difficulty: 'advanced',
    definition: 'Models that can process and understand multiple types of data (text, images, audio, video) simultaneously. Enables richer understanding and cross-modal reasoning.',
    related: ['Vision-Language Models', 'Cross-Modal', 'Embeddings'],
    tags: ['multimodal', 'vision', 'cross-modal']
  },
  'Tool Use': {
    category: 'agents',
    difficulty: 'intermediate',
    definition: 'The capability of AI agents to invoke external tools and APIs to accomplish tasks. Extends agent capabilities beyond text generation to real-world actions.',
    related: ['AI Agent', 'Function Calling', 'API Integration'],
    tags: ['tools', 'apis', 'actions']
  },
  'Planning': {
    category: 'agents',
    difficulty: 'intermediate',
    definition: 'The process of breaking down complex tasks into sequential steps to achieve a goal. Includes task decomposition, scheduling, and resource allocation.',
    related: ['AI Agent', 'Task Decomposition', 'Scheduling'],
    tags: ['planning', 'decomposition', 'scheduling']
  },
  'Memory Systems': {
    category: 'agents',
    difficulty: 'intermediate',
    definition: 'Mechanisms for maintaining context and storing information across interactions. Includes short-term (context window) and long-term (external storage) memory.',
    related: ['AI Agent', 'Context Window', 'Knowledge Base'],
    tags: ['memory', 'context', 'storage']
  },
  'AI Safety': {
    category: 'safety',
    difficulty: 'advanced',
    definition: 'Research focused on ensuring AI systems behave as intended and avoid harmful outcomes. Includes alignment, robustness, and interpretability.',
    related: ['Alignment', 'Robustness', 'Interpretability'],
    tags: ['safety', 'alignment', 'robustness']
  },
  'Evaluation': {
    category: 'evaluation',
    difficulty: 'beginner',
    definition: 'Methods and metrics for assessing AI system performance and capabilities. Includes benchmarks, human evaluation, and automated metrics.',
    related: ['Benchmark', 'Metrics', 'Human Evaluation'],
    tags: ['evaluation', 'metrics', 'benchmarks']
  },
  'GUI Agents': {
    category: 'agents',
    difficulty: 'advanced',
    definition: 'AI agents that can interact with graphical user interfaces to automate tasks. Combines computer vision, planning, and action execution.',
    related: ['AI Agent', 'Computer Vision', 'Automation'],
    tags: ['gui', 'automation', 'vision']
  },
  'Embeddings': {
    category: 'retrieval',
    difficulty: 'intermediate',
    definition: 'Dense vector representations of text or other data that capture semantic meaning. Enable similarity search and clustering.',
    related: ['Vector Search', 'Semantic Search', 'Retrieval-Augmented Generation'],
    tags: ['embeddings', 'vectors', 'similarity']
  },
  'Hallucination': {
    category: 'safety',
    difficulty: 'beginner',
    definition: 'When AI models generate information that is not grounded in facts or context. A major challenge in LLM reliability.',
    related: ['Retrieval-Augmented Generation', 'Fact-Checking', 'Verification'],
    tags: ['hallucination', 'reliability', 'facts']
  }
};

async function loadWikiData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    // Initialize concepts from database
    initializeConcepts();
    
    // Extract concepts from papers
    extractConceptsFromPapers();
    
    // Render initial view
    renderConceptGrid();
    updateStats();
    
  } catch (error) {
    console.error('Failed to load wiki data:', error);
    showEmptyState();
  }
}

function initializeConcepts() {
  concepts = {};
  
  for (const [name, data] of Object.entries(conceptDatabase)) {
    concepts[name] = {
      name: name,
      category: data.category,
      difficulty: data.difficulty,
      definition: data.definition,
      related: data.related,
      tags: data.tags,
      papers: [],
      firstSeen: null,
      lastSeen: null
    };
  }
}

function extractConceptsFromPapers() {
  allPapers.forEach(paper => {
    const title = paper.title || '';
    const abstract = paper.abstract || '';
    const text = (title + ' ' + abstract).toLowerCase();
    const paperDate = paper.date || paper.published || '';
    
    // Check each concept
    for (const [conceptName, conceptData] of Object.entries(concepts)) {
      const keywords = [conceptName.toLowerCase(), ...conceptData.tags];
      
      if (keywords.some(keyword => text.includes(keyword.toLowerCase()))) {
        conceptData.papers.push({
          id: paper.id,
          title: paper.title,
          authors: paper.authors,
          date: paperDate
        });
        
        // Track timeline
        if (!conceptData.firstSeen || paperDate < conceptData.firstSeen) {
          conceptData.firstSeen = paperDate;
        }
        if (!conceptData.lastSeen || paperDate > conceptData.lastSeen) {
          conceptData.lastSeen = paperDate;
        }
      }
    }
  });
}

function renderConceptGrid() {
  const grid = document.getElementById('conceptGrid');
  const filteredConcepts = getFilteredConcepts();
  
  if (filteredConcepts.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">📚</div>
        <h3>No concepts found</h3>
        <p>Try adjusting your filters or search terms</p>
      </div>
    `;
    return;
  }
  
  grid.innerHTML = filteredConcepts.map(concept => `
    <div class="concept-card" onclick="showConceptDetail('${concept.name}')">
      <div class="concept-header">
        <h3 class="concept-name">${concept.name}</h3>
        <span class="concept-category">${concept.category}</span>
      </div>
      <p class="concept-definition">${concept.definition.substring(0, 150)}...</p>
      <div class="concept-meta">
        <div class="concept-papers">
          📄 ${concept.papers.length} papers
        </div>
        <span class="concept-difficulty difficulty-${concept.difficulty}">
          ${concept.difficulty}
        </span>
      </div>
    </div>
  `).join('');
}

function getFilteredConcepts() {
  const category = document.getElementById('categoryFilter').value;
  const difficulty = document.getElementById('difficultyFilter').value;
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = Object.values(concepts);
  
  // Filter by category
  if (category !== 'all') {
    filtered = filtered.filter(c => c.category === category);
  }
  
  // Filter by difficulty
  if (difficulty !== 'all') {
    filtered = filtered.filter(c => c.difficulty === difficulty);
  }
  
  // Sort
  if (sortBy === 'name') {
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortBy === 'papers') {
    filtered.sort((a, b) => b.papers.length - a.papers.length);
  } else if (sortBy === 'recent') {
    filtered.sort((a, b) => (b.lastSeen || '').localeCompare(a.lastSeen || ''));
  }
  
  return filtered;
}

function filterConcepts() {
  renderConceptGrid();
}

function searchWiki() {
  const query = document.getElementById('wikiSearch').value.toLowerCase();
  
  if (!query) {
    renderConceptGrid();
    return;
  }
  
  const grid = document.getElementById('conceptGrid');
  const results = Object.values(concepts).filter(concept => {
    return concept.name.toLowerCase().includes(query) ||
           concept.definition.toLowerCase().includes(query) ||
           concept.tags.some(tag => tag.toLowerCase().includes(query));
  });
  
  if (results.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">🔍</div>
        <h3>No results found</h3>
        <p>Try different search terms</p>
      </div>
    `;
    return;
  }
  
  grid.innerHTML = results.map(concept => `
    <div class="concept-card" onclick="showConceptDetail('${concept.name}')">
      <div class="concept-header">
        <h3 class="concept-name">${concept.name}</h3>
        <span class="concept-category">${concept.category}</span>
      </div>
      <p class="concept-definition">${concept.definition.substring(0, 150)}...</p>
      <div class="concept-meta">
        <div class="concept-papers">
          📄 ${concept.papers.length} papers
        </div>
        <span class="concept-difficulty difficulty-${concept.difficulty}">
          ${concept.difficulty}
        </span>
      </div>
    </div>
  `).join('');
}

function showConceptDetail(conceptName) {
  const concept = concepts[conceptName];
  if (!concept) return;
  
  const modal = document.getElementById('conceptModal');
  const detail = document.getElementById('conceptDetail');
  
  detail.innerHTML = `
    <div class="concept-detail-header">
      <h2 class="concept-detail-title">${concept.name}</h2>
      <div class="concept-detail-meta">
        <span class="concept-category">${concept.category}</span>
        <span class="concept-difficulty difficulty-${concept.difficulty}">${concept.difficulty}</span>
        <span>📄 ${concept.papers.length} papers</span>
      </div>
    </div>
    
    <div class="concept-detail-section">
      <h3>Definition</h3>
      <p class="concept-detail-definition">${concept.definition}</p>
    </div>
    
    <div class="concept-detail-section">
      <h3>Tags</h3>
      <div class="related-concepts">
        ${concept.tags.map(tag => `<span class="related-concept">${tag}</span>`).join('')}
      </div>
    </div>
    
    <div class="concept-detail-section">
      <h3>Related Concepts</h3>
      <div class="related-concepts">
        ${concept.related.map(rel => `
          <span class="related-concept" onclick="showConceptDetail('${rel}')">${rel}</span>
        `).join('')}
      </div>
    </div>
    
    <div class="concept-detail-section">
      <h3>Related Papers (${concept.papers.length})</h3>
      <div class="papers-list">
        ${concept.papers.slice(0, 10).map(paper => `
          <div class="paper-item">
            <div class="paper-title">${paper.title}</div>
            <div class="paper-authors">${paper.authors?.slice(0, 3).join(', ') || 'Unknown authors'}</div>
          </div>
        `).join('')}
        ${concept.papers.length > 10 ? `<p style="color: #7f8c8d; text-align: center;">... and ${concept.papers.length - 10} more papers</p>` : ''}
      </div>
    </div>
  `;
  
  modal.classList.add('active');
}

function closeConceptModal() {
  document.getElementById('conceptModal').classList.remove('active');
}

function closeModal(event) {
  if (event.target.classList.contains('modal')) {
    closeConceptModal();
  }
}

function switchTab(tabName) {
  // Update tab buttons
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  
  // Update tab content
  document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
  document.getElementById(tabName + 'Tab').classList.add('active');
  
  currentTab = tabName;
  
  // Initialize tab-specific content
  if (tabName === 'graph') {
    initConceptGraph();
  } else if (tabName === 'timeline') {
    renderTimeline();
  } else if (tabName === 'stats') {
    updateStats();
  }
}

function initConceptGraph() {
  const container = document.getElementById('conceptGraph');
  container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">🕸️</div><h3>Concept Graph</h3><p>Interactive visualization of concept relationships</p></div>';
  
  // Simple graph visualization using SVG
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', '100%');
  svg.setAttribute('height', '600');
  svg.style.background = '#f8f9fa';
  
  const conceptsList = Object.values(concepts).filter(c => c.papers.length > 0);
  const centerX = container.offsetWidth / 2;
  const centerY = 300;
  const radius = 200;
  
  // Draw nodes
  conceptsList.forEach((concept, i) => {
    const angle = (i / conceptsList.length) * 2 * Math.PI;
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);
    
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    circle.setAttribute('r', Math.min(10 + concept.papers.length, 30));
    circle.setAttribute('fill', '#2c5aa0');
    circle.setAttribute('opacity', '0.7');
    circle.style.cursor = 'pointer';
    circle.onclick = () => showConceptDetail(concept.name);
    
    svg.appendChild(circle);
    
    if (showLabels) {
      const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('x', x);
      text.setAttribute('y', y + 25);
      text.setAttribute('text-anchor', 'middle');
      text.setAttribute('font-size', '12');
      text.setAttribute('fill', '#333');
      text.textContent = concept.name;
      
      svg.appendChild(text);
    }
  });
  
  container.appendChild(svg);
}

function resetGraph() {
  initConceptGraph();
}

function toggleLabels() {
  showLabels = !showLabels;
  initConceptGraph();
}

function updateGraphLayout() {
  initConceptGraph();
}

function renderTimeline() {
  const container = document.getElementById('conceptTimeline');
  
  // Group concepts by first seen date
  const timeline = {};
  Object.values(concepts).forEach(concept => {
    if (concept.firstSeen) {
      const date = concept.firstSeen.substring(0, 7); // YYYY-MM
      if (!timeline[date]) {
        timeline[date] = [];
      }
      timeline[date].push(concept);
    }
  });
  
  const sortedDates = Object.keys(timeline).sort().reverse();
  
  if (sortedDates.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">📅</div>
        <h3>No timeline data</h3>
        <p>Concepts will appear here as papers are added</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = sortedDates.map(date => `
    <div class="timeline-item">
      <div class="timeline-date">${date}</div>
      <div class="timeline-content">
        <h4>${timeline[date].length} new concept${timeline[date].length > 1 ? 's' : ''}</h4>
        <div class="timeline-concepts">
          ${timeline[date].map(c => `
            <span class="related-concept" onclick="showConceptDetail('${c.name}')">${c.name}</span>
          `).join('')}
        </div>
      </div>
    </div>
  `).join('');
}

function updateStats() {
  document.getElementById('totalConcepts').textContent = Object.keys(concepts).length;
  
  const totalRelations = Object.values(concepts).reduce((sum, c) => sum + c.related.length, 0);
  document.getElementById('totalRelations').textContent = totalRelations;
  
  const coveredPapers = new Set();
  Object.values(concepts).forEach(c => c.papers.forEach(p => coveredPapers.add(p.id)));
  document.getElementById('coveredPapers').textContent = coveredPapers.size;
  
  const allTags = new Set();
  Object.values(concepts).forEach(c => c.tags.forEach(t => allTags.add(t)));
  document.getElementById('totalTags').textContent = allTags.size;
  
  // Category breakdown
  const categories = {};
  Object.values(concepts).forEach(c => {
    categories[c.category] = (categories[c.category] || 0) + 1;
  });
  
  const breakdown = document.getElementById('categoryBreakdown');
  breakdown.innerHTML = `
    <h3>Concepts by Category</h3>
    ${Object.entries(categories).map(([cat, count]) => `
      <div style="display: flex; justify-content: space-between; padding: 10px; background: #f8f9fa; margin-bottom: 5px; border-radius: 4px;">
        <span style="font-weight: 600; text-transform: capitalize;">${cat}</span>
        <span style="color: #2c5aa0; font-weight: bold;">${count} concepts</span>
      </div>
    `).join('')}
  `;
}

function showEmptyState() {
  const grid = document.getElementById('conceptGrid');
  grid.innerHTML = `
    <div class="empty-state">
      <div class="empty-state-icon">📚</div>
      <h3>No concepts available</h3>
      <p>Start by adding papers to build your knowledge base</p>
    </div>
  `;
}

// Initialize
loadWikiData();

// Search on Enter key
document.getElementById('wikiSearch').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    searchWiki();
  }
});
</script>
