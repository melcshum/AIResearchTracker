---
title: "Research Wiki"
---

<div class="wiki-container">
<div class="wiki-header">
<h2>📖 Research Wiki</h2>
<p class="wiki-subtitle">Interactive knowledge building with real paper references and persistent contributions</p>
</div>

<div class="wiki-search-bar">
<input type="text" id="wikiSearch" placeholder="🔍 Search wiki entries, terms, and concepts..." onkeyup="searchWiki()">
<div id="searchResults" class="wiki-search-results"></div>
</div>

<div class="wiki-workflow-guide">
<div class="workflow-step">
<div class="step-icon">👆</div>
<div class="step-content">
<h4>1. Select a Term</h4>
<p>Click any highlighted term in the article to begin exploring</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">❓</div>
<div class="step-content">
<h4>2. Ask Questions</h4>
<p>What would you like to know? Formulate your research question</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">🔍</div>
<div class="step-content">
<h4>3. Search Sources</h4>
<p>Find reliable academic sources and papers to answer your question</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">💡</div>
<div class="step-content">
<h4>4. Build Explanation</h4>
<p>Synthesize information, add examples, and cite sources</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">✅</div>
<div class="step-content">
<h4>5. Review & Approve</h4>
<p>Review your contribution, refine if needed, and submit to the wiki</p>
</div>
</div>
</div>

<div class="wiki-content-area">
<div class="wiki-article">
<h3>AI Agent Systems</h3>
<p>
An AI agent is an autonomous system that can 
perceive its environment, 
reason about actions, and 
act to achieve goals. Modern AI agents often use 
large language models as their reasoning core, combined with 
tool use capabilities and 
planning algorithms.
</p>
<p>
Key components include memory systems for maintaining context, 
retrieval mechanisms for accessing knowledge, and 
multi-agent coordination for complex tasks.
</p>
<h3>Retrieval-Augmented Generation</h3>
<p>
RAG combines retrieval with generation by first searching a knowledge base for relevant documents, then using those documents as context for the language model. This approach reduces hallucination and provides verifiable citations.
</p>
<p>
Advanced RAG systems use dense retrieval with vector embeddings, hybrid search combining lexical and semantic methods, and reranking to improve result quality.
</p>
</div>

<div class="wiki-sidebar">
<div class="wiki-actions">
<h4>📝 Wiki Actions</h4>
<div id="selectedTerm" class="selected-term-display">
<p class="hint">Click any highlighted term to start</p>
</div>
<div id="actionButtons" class="action-buttons" style="display: none;">
<button class="wiki-btn primary" onclick="askQuestion()">❓ Ask Question</button>
<button class="wiki-btn" onclick="searchSources()">🔍 Search Sources</button>
<button class="wiki-btn" onclick="addExplanation()">💡 Add Explanation</button>
<button class="wiki-btn" onclick="viewRelatedPapers()">📄 Related Papers</button>
<button class="wiki-btn" onclick="viewBacklinks()">🔗 Backlinks</button>
<button class="wiki-btn" onclick="viewHistory()">📜 View History</button>
<button class="wiki-btn" onclick="openGraphView()">🕸️ View Graph</button>
</div>
</div>

<div id="questionPanel" class="wiki-panel" style="display: none;">
<h4>Ask a Question</h4>
<textarea id="questionInput" placeholder="What would you like to know about this term?"></textarea>
<button class="wiki-btn primary" onclick="submitQuestion()">Submit Question</button>
</div>

<div id="searchPanel" class="wiki-panel" style="display: none;">
<h4>Search Sources</h4>
<div id="searchResults" class="search-results">
<p class="hint">Searching for reliable sources...</p>
</div>
</div>

<div id="explainPanel" class="wiki-panel" style="display: none;">
<h4>Add Explanation</h4>
<textarea id="explanationInput" placeholder="Contribute your understanding..."></textarea>
<div class="explanation-tools">
<button class="tool-btn" onclick="simplify()">🔧 Simplify</button>
<button class="tool-btn" onclick="addExample()">📋 Add Example</button>
<button class="tool-btn" onclick="addCitation()">📚 Add Citation</button>
</div>
<button class="wiki-btn primary" onclick="submitExplanation()">Submit to Wiki</button>
</div>

<div id="papersPanel" class="wiki-panel" style="display: none;">
<h4>Related Papers</h4>
<div id="relatedPapers" class="related-papers">
<p class="hint">Loading related papers...</p>
</div>
</div>

<div id="reviewPanel" class="wiki-panel" style="display: none;">
<h4>Review & Refine</h4>
<div id="reviewContent" class="review-content"></div>
<div class="review-actions">
<button class="wiki-btn success" onclick="approve()">✅ Approve</button>
<button class="wiki-btn warning" onclick="requestRevision()">🔄 Request Revision</button>
<button class="wiki-btn danger" onclick="reject()">❌ Reject</button>
</div>
</div>

<div id="historyPanel" class="wiki-panel" style="display: none;">
<h4>Version History</h4>
<div id="versionHistory" class="version-history">
<p class="hint">Loading history...</p>
</div>
</div>
</div>
</div>

<div class="wiki-contributions">
<div class="contributions-header">
<h3>Recent Contributions</h3>
<div class="contributions-actions">
<button class="export-btn" onclick="exportWiki()">📥 Export Wiki</button>
<button class="export-btn" onclick="importWiki()">📤 Import Wiki</button>
</div>
</div>
<div id="contributionsList" class="contributions-list">
<p class="hint">No contributions yet. Start by clicking a term above!</p>
</div>
</div>
</div></div>

<div id="backlinksPanel" class="wiki-panel" style="display: none;">
<h4>🔗 Backlinks</h4>
<div id="backlinksContent" class="backlinks-content">
<p class="hint">Loading backlinks...</p>
</div>
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
  text-align: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #e0e0e0;
}

.wiki-header h2 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.wiki-subtitle {
  color: #666;
  font-size: 16px;
}

.wiki-search-bar {
  position: relative;
  margin-bottom: 30px;
}

#wikiSearch {
  width: 100%;
  padding: 15px 20px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 16px;
  transition: all 0.3s;
}

#wikiSearch:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.wiki-search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  margin-top: 5px;
  max-height: 400px;
  overflow-y: auto;
  display: none;
  z-index: 1000;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.wiki-search-results.active {
  display: block;
}

.search-result-item {
  padding: 12px 20px;
  border-bottom: 1px solid #f0f0f0;
  cursor: pointer;
  transition: background 0.2s;
}

.search-result-item:hover {
  background: #f8f9fa;
}

.search-result-item:last-child {
  border-bottom: none;
}

.wiki-workflow-guide {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 30px;
  border-radius: 12px;
  margin-bottom: 40px;
  color: white;
}

.workflow-step {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 15px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  margin-bottom: 15px;
  backdrop-filter: blur(10px);
}

.workflow-step:last-child {
  margin-bottom: 0;
}

.step-icon {
  font-size: 32px;
  flex-shrink: 0;
}

.step-content h4 {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 600;
}

.step-content p {
  margin: 0;
  font-size: 14px;
  opacity: 0.9;
  line-height: 1.5;
}

.wiki-content-area {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
  margin-bottom: 40px;
}

.wiki-article {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  line-height: 1.8;
}

.wiki-article h3 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.wiki-term {
  background: #e3f2fd;
  color: #1976d2;
  padding: 2px 6px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  border-bottom: 2px solid #1976d2;
}

.wiki-term:hover {
  background: #bbdefb;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.wiki-term.selected {
  background: #1976d2;
  color: white;
}

.wiki-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.wiki-actions {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.wiki-actions h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.selected-term-display {
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 15px;
  min-height: 60px;
}

.selected-term-display .hint {
  color: #999;
  font-style: italic;
  margin: 0;
}

.selected-term-display .term-name {
  font-size: 18px;
  font-weight: bold;
  color: #1976d2;
  margin-bottom: 5px;
}

.selected-term-display .term-definition {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.wiki-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
  background: #6c757d;
  color: white;
}

.wiki-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.wiki-btn.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.wiki-btn.success {
  background: #28a745;
}

.wiki-btn.warning {
  background: #ffc107;
  color: #212529;
}

.wiki-btn.danger {
  background: #dc3545;
}

.wiki-panel {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.wiki-panel h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.wiki-panel textarea {
  width: 100%;
  min-height: 120px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-family: inherit;
  font-size: 14px;
  resize: vertical;
  margin-bottom: 15px;
}

.explanation-tools {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

.tool-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  cursor: pointer;
  font-size: 13px;
  transition: all 0.2s;
}

.tool-btn:hover {
  background: #f8f9fa;
  border-color: #667eea;
}

.search-results {
  max-height: 400px;
  overflow-y: auto;
}

.search-result-item {
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  margin-bottom: 10px;
  cursor: pointer;
  transition: all 0.2s;
}

.search-result-item:hover {
  border-color: #667eea;
  background: #f8f9fa;
}

.search-result-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.search-result-meta {
  font-size: 12px;
  color: #666;
}

.related-papers {
  max-height: 400px;
  overflow-y: auto;
}

.related-paper-item {
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  margin-bottom: 10px;
  transition: all 0.2s;
}

.related-paper-item:hover {
  border-color: #667eea;
  background: #f8f9fa;
}

.related-paper-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
  font-size: 14px;
}

.related-paper-meta {
  font-size: 12px;
  color: #666;
  margin-bottom: 5px;
}

.related-paper-abstract {
  font-size: 12px;
  color: #888;
  line-height: 1.4;
}

.version-history {
  max-height: 400px;
  overflow-y: auto;
}

.version-item {
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  margin-bottom: 10px;
}

.version-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 12px;
  color: #666;
}

.version-content {
  font-size: 13px;
  color: #444;
  line-height: 1.5;
}

.review-content {
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 15px;
  min-height: 100px;
}

.review-actions {
  display: flex;
  gap: 10px;
}

.wiki-contributions {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.contributions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.contributions-header h3 {
  margin: 0;
  color: #2c3e50;
}

.contributions-actions {
  display: flex;
  gap: 10px;
}

.export-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  font-size: 13px;
  transition: all 0.2s;
}

.export-btn:hover {
  background: #f8f9fa;
  border-color: #667eea;
}

.contributions-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.contribution-item {
  padding: 15px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  transition: all 0.2s;
}

.contribution-item:hover {
  border-color: #667eea;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.contribution-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.contribution-meta {
  font-size: 12px;
  color: #999;
}

.contribution-preview {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.hint {
  color: #999;
  font-style: italic;
  text-align: center;
  padding: 20px;
}
.backlinks-info {
  padding: 15px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  color: white;
  margin-bottom: 15px;
}

.backlink-item {
  padding: 12px;
  background: #f8f9fa;
  border-radius: 6px;
  margin-bottom: 8px;
  cursor: pointer;
  transition: all 0.2s;
  border-left: 3px solid #667eea;
}

.backlink-item:hover {
  background: #e9ecef;
  transform: translateX(5px);
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
}

.backlink-title {
  font-weight: 600;
  color: #2c3e50;
  font-size: 14px;
  margin-bottom: 4px;
}

.backlink-meta {
  font-size: 12px;
  color: #999;
}

.backlink-context {
  margin-top: 6px;
  padding: 8px;
  background: #fff;
  border-radius: 4px;
  font-size: 13px;
  color: #495057;
  border-left: 2px solid #667eea;
}

.backlinks-empty {
  text-align: center;
  padding: 30px;
  background: #f8f9fa;
  border-radius: 8px;
}

.backlinks-empty .hint {
  margin-bottom: 15px;
}

.term-stats {
  margin-top: 10px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.stat-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 500;
}

.backlink-stats {
  display: flex;
  gap: 10px;
  margin-top: 10px;
  flex-wrap: wrap;
}

.stat-tag {
  background: rgba(255, 255, 255, 0.2);
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

h5 {
  font-size: 14px;
  font-weight: 600;
  color: #495057;
  margin: 15px 0 10px 0;
  padding-bottom: 5px;
  border-bottom: 2px solid #e9ecef;
}
</style>

<script>
let currentTerm = null;
let wikiContributions = JSON.parse(localStorage.getItem('wikiContributions') || '[]');
let termVersions = JSON.parse(localStorage.getItem('termVersions') || '{}');

// Wiki term database with paper references
const wikiTerms = {
  'ai-agent': {
    name: 'AI Agent',
    definition: 'An autonomous system that can perceive, reason, and act to achieve goals',
    relatedTerms: ['perception', 'reasoning', 'act', 'planning', 'tool-use'],
    keywords: ['agent', 'autonomous', 'planning', 'tool']
  },
  'perception': {
    name: 'Perception',
    definition: 'The ability to sense and interpret environmental information',
    relatedTerms: ['ai-agent', 'multi-modal'],
    keywords: ['perception', 'sense', 'input', 'observation']
  },
  'reasoning': {
    name: 'Reasoning',
    definition: 'The process of drawing conclusions from available information',
    relatedTerms: ['ai-agent', 'llm', 'planning'],
    keywords: ['reasoning', 'logic', 'inference', 'thinking']
  },
  'act': {
    name: 'Action',
    definition: 'Executing operations to change the environment or achieve goals',
    relatedTerms: ['ai-agent', 'tool-use'],
    keywords: ['action', 'execute', 'operation', 'perform']
  },
  'llm': {
    name: 'Large Language Model',
    definition: 'Neural networks trained on vast text corpora for language understanding and generation',
    relatedTerms: ['ai-agent', 'reasoning'],
    keywords: ['llm', 'language model', 'gpt', 'transformer']
  },
  'tool-use': {
    name: 'Tool Use',
    definition: 'The ability to invoke external functions, APIs, or systems to extend capabilities',
    relatedTerms: ['ai-agent', 'act'],
    keywords: ['tool', 'function', 'api', 'invoke']
  },
  'planning': {
    name: 'Planning',
    definition: 'Decomposing goals into sequences of actions',
    relatedTerms: ['ai-agent', 'reasoning'],
    keywords: ['planning', 'decompose', 'sequence', 'goal']
  },
  'memory': {
    name: 'Memory Systems',
    definition: 'Mechanisms for storing and retrieving information across interactions',
    relatedTerms: ['ai-agent', 'retrieval'],
    keywords: ['memory', 'store', 'retrieve', 'context']
  },
  'retrieval': {
    name: 'Retrieval',
    definition: 'Finding and accessing relevant information from knowledge bases',
    relatedTerms: ['memory', 'rag'],
    keywords: ['retrieval', 'search', 'find', 'access']
  },
  'multi-agent': {
    name: 'Multi-Agent Systems',
    definition: 'Multiple AI agents working together to solve complex problems',
    relatedTerms: ['ai-agent', 'coordination'],
    keywords: ['multi-agent', 'coordination', 'collaboration', 'team']
  },
  'rag': {
    name: 'Retrieval-Augmented Generation',
    definition: 'Combining retrieval with generation to reduce hallucination and provide citations',
    relatedTerms: ['retrieval', 'llm', 'dense-retrieval'],
    keywords: ['rag', 'retrieval', 'generation', 'citation']
  },
  'dense-retrieval': {
    name: 'Dense Retrieval',
    definition: 'Using vector embeddings to find semantically similar documents',
    relatedTerms: ['retrieval', 'rag'],
    keywords: ['dense', 'embedding', 'vector', 'semantic']
  },
  'hybrid-search': {
    name: 'Hybrid Search',
    definition: 'Combining lexical and semantic search methods for better results',
    relatedTerms: ['retrieval', 'dense-retrieval'],
    keywords: ['hybrid', 'lexical', 'semantic', 'search']
  },
  'reranking': {
    name: 'Reranking',
    definition: 'Reordering retrieved results using a more sophisticated model',
    relatedTerms: ['retrieval', 'rag'],
    keywords: ['reranking', 'reorder', 'rank', 'score']
  }
};

// Paper database (loaded from actual papers)
const paperDatabase = [
  {
    title: "WM-R1: Training GUI Agents to Reason and leverage World Models",
    authors: "Han, Y, Qian, T",
    date: "2026-08-31",
    abstract: "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities...",
    topics: ["ai-agents"],
    arxiv_id: "2608.27508",
    keywords: ["agent", "gui", "reasoning", "world model"]
  },
  {
    title: "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery",
    authors: "Huang, Y, He, W, Lin, Z",
    date: "2026-08-31",
    abstract: "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator...",
    topics: ["ai-agents"],
    arxiv_id: "2608.27475",
    keywords: ["agent", "scientific", "hypothesis", "evaluation"]
  },
  {
    title: "Retrieving Relations, Detecting Fallacies: A RAG Approach",
    authors: "Dore, D, Damo, G, Cabrio, E",
    date: "2026-08-31",
    abstract: "Fallacies are arguments that employ invalid reasoning, making their automatic detection critical...",
    topics: ["rag-retrieval"],
    arxiv_id: "2608.27471",
    keywords: ["rag", "retrieval", "fallacy", "reasoning"]
  },
  {
    title: "SABER: Stability-Aware Early Exit for LLM Reasoning",
    authors: "Cheng, W, Xiang, H, Li, J",
    date: "2026-08-31",
    abstract: "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient...",
    topics: ["llm-reasoning"],
    arxiv_id: "2608.27963",
    keywords: ["llm", "reasoning", "efficiency", "early exit"]
  }
];

// Initialize term click handlers
document.querySelectorAll('.wiki-term').forEach(term => {
  term.addEventListener('click', function() {
    selectTerm(this);
  });
});

// Enhanced backlink index for bidirectional linking
let backlinkIndex = {};

function buildBacklinkIndex() {
  backlinkIndex = {};
  
  // Index all wiki terms and their relationships
  Object.entries(wikiTerms).forEach(([id, term]) => {
    if (!backlinkIndex[id]) backlinkIndex[id] = [];
    
    // Add related terms as backlinks
    term.relatedTerms.forEach(relId => {
      backlinkIndex[id].push({
        source: relId,
        sourceName: wikiTerms[relId]?.name || relId,
        type: 'term',
        relationship: 'related to'
      });
    });
  });
  
  // Index contributions that mention terms
  wikiContributions.forEach(contrib => {
    if (contrib.termId && contrib.content) {
      if (!backlinkIndex[contrib.termId]) backlinkIndex[contrib.termId] = [];
      
      // Find terms mentioned in this contribution
      Object.keys(wikiTerms).forEach(termId => {
        if (contrib.content.includes(wikiTerms[termId].name) && termId !== contrib.termId) {
          backlinkIndex[contrib.termId].push({
            source: termId,
            sourceName: wikiTerms[termId].name,
            type: 'contribution',
            relationship: 'mentioned in',
            context: contrib.content.substring(0, 100) + '...'
          });
        }
      });
    }
  });
  
  // Index papers that mention terms
  paperDatabase.forEach(paper => {
    Object.keys(wikiTerms).forEach(termId => {
      const term = wikiTerms[termId];
      if (paper.keywords.some(k => term.keywords.includes(k)) ||
          paper.topics.some(t => t === term.category)) {
        if (!backlinkIndex[termId]) backlinkIndex[termId] = [];
        
        backlinkIndex[termId].push({
          source: paper.arxiv_id,
          sourceName: paper.title,
          type: 'paper',
          relationship: 'discussed in',
          context: paper.abstract.substring(0, 150) + '...'
        });
      }
    });
  });
  
  return backlinkIndex;
}

function selectTerm(element) {
  document.querySelectorAll('.wiki-term.selected').forEach(t => t.classList.remove('selected'));
  element.classList.add('selected');
  const termId = element.getAttribute('data-term');
  currentTerm = wikiTerms[termId];
  currentTerm.id = termId;
  
  document.getElementById('selectedTerm').innerHTML = `
    <div class="term-name">${currentTerm.name}</div>
    <div class="term-definition">${currentTerm.definition}</div>
    <div class="term-stats">
      <span class="stat-badge">${getBacklinkCount(termId)} connections</span>
    </div>
  `;
  document.getElementById('actionButtons').style.display = 'flex';
  
  // Build backlink index on first term selection
  if (Object.keys(backlinkIndex).length === 0) {
    buildBacklinkIndex();
  }
}

function askQuestion() {
  hideAllPanels();
  document.getElementById('questionPanel').style.display = 'block';
}

function searchSources() {
  hideAllPanels();
  document.getElementById('searchPanel').style.display = 'block';
  
  const results = document.getElementById('searchResults');
  results.innerHTML = '<p class="hint">Searching for reliable sources...</p>';
  
  setTimeout(() => {
    const relatedPapers = paperDatabase.filter(p => 
      p.keywords.some(k => currentTerm.keywords.includes(k)) ||
      p.topics.some(t => currentTerm.keywords.includes(t))
    );
    
    if (relatedPapers.length === 0) {
      results.innerHTML = '<p class="hint">No papers found for this term</p>';
      return;
    }
    
    results.innerHTML = relatedPapers.map(paper => `
      <div class="search-result-item" onclick="selectSource('${paper.arxiv_id}')">
        <div class="search-result-title">${paper.title}</div>
        <div class="search-result-meta">${paper.authors} • ${paper.date}</div>
      </div>
    `).join('');
  }, 500);
}

function viewRelatedPapers() {
  hideAllPanels();
  document.getElementById('papersPanel').style.display = 'block';
  
  const papersDiv = document.getElementById('relatedPapers');
  papersDiv.innerHTML = '<p class="hint">Loading related papers...</p>';
  
  setTimeout(() => {
    const relatedPapers = paperDatabase.filter(p => 
      p.keywords.some(k => currentTerm.keywords.includes(k)) ||
      p.topics.some(t => currentTerm.keywords.includes(t))
    );
    
    if (relatedPapers.length === 0) {
      papersDiv.innerHTML = '<p class="hint">No related papers found</p>';
      return;
    }
    
    papersDiv.innerHTML = relatedPapers.map(paper => `
      <div class="related-paper-item">
        <div class="related-paper-title">${paper.title}</div>
        <div class="related-paper-meta">${paper.authors} • ${paper.date}</div>
        <div class="related-paper-abstract">${paper.abstract.substring(0, 150)}...</div>
      </div>
    `).join('');
  }, 500);
}

function viewHistory() {
  hideAllPanels();
  document.getElementById('historyPanel').style.display = 'block';
  
  const historyDiv = document.getElementById('versionHistory');
  const versions = termVersions[currentTerm.id] || [];
  
  if (versions.length === 0) {
    historyDiv.innerHTML = '<p class="hint">No version history for this term</p>';
    return;
  }
  
  historyDiv.innerHTML = versions.map((v, i) => `
    <div class="version-item">
      <div class="version-header">
        <span>Version ${versions.length - i}</span>
        <span>${new Date(v.timestamp).toLocaleString()}</span>
      </div>
      <div class="version-content">${v.content}</div>
    </div>
  `).join('');
}

function addExplanation() {
  hideAllPanels();
  document.getElementById('explainPanel').style.display = 'block';
}

function submitQuestion() {
  const question = document.getElementById('questionInput').value;
  if (!question) {
    alert('Please enter a question');
    return;
  }
  
  addContribution('question', question);
  document.getElementById('questionInput').value = '';
  hideAllPanels();
  alert('Question submitted and saved!');
}

function submitExplanation() {
  const explanation = document.getElementById('explanationInput').value;
  if (!explanation) {
    alert('Please enter an explanation');
    return;
  }
  
  hideAllPanels();
  document.getElementById('reviewPanel').style.display = 'block';
  document.getElementById('reviewContent').innerHTML = `
    <strong>Term:</strong> ${currentTerm.name}<br><br>
    <strong>Your Explanation:</strong><br>
    ${explanation}
  `;
  
  window.pendingExplanation = explanation;
}

function approve() {
  if (window.pendingExplanation) {
    addContribution('explanation', window.pendingExplanation);
    
    // Save to version history
    if (!termVersions[currentTerm.id]) {
      termVersions[currentTerm.id] = [];
    }
    termVersions[currentTerm.id].push({
      content: window.pendingExplanation,
      timestamp: Date.now()
    });
    localStorage.setItem('termVersions', JSON.stringify(termVersions));
    
    window.pendingExplanation = null;
    document.getElementById('explanationInput').value = '';
  }
  
  hideAllPanels();
  alert('Explanation approved and added to wiki!');
}

function requestRevision() {
  hideAllPanels();
  document.getElementById('explainPanel').style.display = 'block';
  document.getElementById('reviewPanel').style.display = 'none';
}

function reject() {
  if (confirm('Are you sure you want to reject this explanation?')) {
    window.pendingExplanation = null;
    document.getElementById('explanationInput').value = '';
    hideAllPanels();
  }
}

function simplify() {
  const textarea = document.getElementById('explanationInput');
  textarea.value = textarea.value.replace(/\b\w{15,}\b/g, match => match.substring(0, 10) + '...');
}

function addExample() {
  const textarea = document.getElementById('explanationInput');
  textarea.value += '\n\nExample: ' + currentTerm.name + ' can be seen in systems like...';
}

function addCitation() {
  const textarea = document.getElementById('explanationInput');
  textarea.value += '\n\n[Citation needed]';
}

function selectSource(arxivId) {
  const paper = paperDatabase.find(p => p.arxiv_id === arxivId);
  if (paper) {
    const textarea = document.getElementById('explanationInput');
    textarea.value += `\n\nSource: ${paper.title} (${paper.date})`;
    hideAllPanels();
    document.getElementById('explainPanel').style.display = 'block';
  }
}

function addContribution(type, content) {
  const contribution = {
    term: currentTerm.name,
    termId: currentTerm.id,
    type: type,
    content: content,
    timestamp: Date.now()
  };
  
  wikiContributions.unshift(contribution);
  localStorage.setItem('wikiContributions', JSON.stringify(wikiContributions));
  renderContributions();
}

function renderContributions() {
  const list = document.getElementById('contributionsList');
  
  if (wikiContributions.length === 0) {
    list.innerHTML = '<p class="hint">No contributions yet. Start by clicking a term above!</p>';
    return;
  }
  
  list.innerHTML = wikiContributions.slice(0, 10).map(c => `
    <div class="contribution-item">
      <div class="contribution-header">
        <strong>${c.term}</strong> - ${c.type} ${c.type === 'question' ? 'asked' : 'added'}
        <span class="contribution-meta">${new Date(c.timestamp).toLocaleString()}</span>
      </div>
      <div class="contribution-preview">${c.content.substring(0, 150)}${c.content.length > 150 ? '...' : ''}</div>
    </div>
  `).join('');
}

function searchWiki() {
  const query = document.getElementById('wikiSearch').value.toLowerCase();
  const resultsDiv = document.getElementById('searchResults');
  
  if (query.length < 2) {
    resultsDiv.classList.remove('active');
    return;
  }
  
  const results = [];
  
  // Search terms
  Object.entries(wikiTerms).forEach(([id, term]) => {
    if (term.name.toLowerCase().includes(query) || 
        term.definition.toLowerCase().includes(query) ||
        term.keywords.some(k => k.includes(query))) {
      results.push({
        type: 'term',
        id: id,
        name: term.name,
        description: term.definition
      });
    }
  });
  
  // Search contributions
  wikiContributions.forEach(c => {
    if (c.content.toLowerCase().includes(query) || c.term.toLowerCase().includes(query)) {
      results.push({
        type: 'contribution',
        term: c.term,
        content: c.content.substring(0, 100)
      });
    }
  });
  
  if (results.length === 0) {
    resultsDiv.innerHTML = '<div class="search-result-item">No results found</div>';
  } else {
    resultsDiv.innerHTML = results.slice(0, 10).map(r => {
      if (r.type === 'term') {
        return `<div class="search-result-item" onclick="jumpToTerm('${r.id}')">
          <strong>${r.name}</strong><br>
          <small>${r.description}</small>
        </div>`;
      } else {
        return `<div class="search-result-item">
          <strong>${r.term}</strong> - contribution<br>
          <small>${r.content}...</small>
        </div>`;
      }
    }).join('');
  }
  
  resultsDiv.classList.add('active');
}

function jumpToTerm(termId) {
  const termElement = document.querySelector(`[data-term="${termId}"]`);
  if (termElement) {
    termElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    selectTerm(termElement);
    document.getElementById('searchResults').classList.remove('active');
    document.getElementById('wikiSearch').value = '';
  }
}

function exportWiki() {
  const data = {
    contributions: wikiContributions,
    versions: termVersions,
    exportDate: new Date().toISOString()
  };
  
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `wiki-export-${new Date().toISOString().split('T')[0]}.json`;
  a.click();
  URL.revokeObjectURL(url);
}

function importWiki() {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = 'application/json';
  
  input.onchange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    
    reader.onload = (event) => {
      try {
        const data = JSON.parse(event.target.result);
        
        if (data.contributions) {
          wikiContributions = data.contributions;
          localStorage.setItem('wikiContributions', JSON.stringify(wikiContributions));
        }
        
        if (data.versions) {
          termVersions = data.versions;
          localStorage.setItem('termVersions', JSON.stringify(termVersions));
        }
        
        renderContributions();
        alert('Wiki imported successfully!');
      } catch (error) {
        alert('Error importing wiki: ' + error.message);
      }
    };
    
    reader.readAsText(file);
  };
  
  input.click();
}

function hideAllPanels() {
  document.getElementById('questionPanel').style.display = 'none';
  document.getElementById('searchPanel').style.display = 'none';
  document.getElementById('explainPanel').style.display = 'none';
  document.getElementById('reviewPanel').style.display = 'none';
  document.getElementById('papersPanel').style.display = 'none';
  document.getElementById('historyPanel').style.display = 'none';
  document.getElementById('backlinksPanel').style.display = 'none';
}

function viewBacklinks() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  hideAllPanels();
  document.getElementById('backlinksPanel').style.display = 'block';
  
  // Build index if not already built
  if (Object.keys(backlinkIndex).length === 0) {
    buildBacklinkIndex();
  }
  
  // Get all backlinks for current term
  const backlinks = backlinkIndex[currentTerm.id] || [];
  
  const backlinksList = document.getElementById('backlinksContent');
  if (backlinks.length > 0) {
    // Group by type
    const terms = backlinks.filter(b => b.type === 'term');
    const papers = backlinks.filter(b => b.type === 'paper');
    const contributions = backlinks.filter(b => b.type === 'contribution');
    
    backlinksList.innerHTML = `
      <div class="backlinks-info">
        <p><strong>${backlinks.length}</strong> connections found for <strong>${currentTerm.name}</strong></p>
        <div class="backlink-stats">
          <span class="stat-tag">📚 ${terms.length} related terms</span>
          <span class="stat-tag">📄 ${papers.length} papers</span>
          <span class="stat-tag">💬 ${contributions.length} contributions</span>
        </div>
      </div>
      ${terms.length > 0 ? `
        <h5>Related Terms</h5>
        ${terms.map(b => `
          <div class="backlink-item" onclick="jumpToTerm('${b.source}')">
            <div class="backlink-title">${b.sourceName}</div>
            <div class="backlink-meta">${b.relationship} • term</div>
          </div>
        `).join('')}
      ` : ''}
      ${papers.length > 0 ? `
        <h5>Related Papers</h5>
        ${papers.map(b => `
          <div class="backlink-item">
            <div class="backlink-title">${b.sourceName}</div>
            <div class="backlink-meta">${b.relationship} • paper</div>
            ${b.context ? `<div class="backlink-context">${b.context}</div>` : ''}
          </div>
        `).join('')}
      ` : ''}
      ${contributions.length > 0 ? `
        <h5>Mentioned in Contributions</h5>
        ${contributions.map(b => `
          <div class="backlink-item">
            <div class="backlink-title">${b.sourceName}</div>
            <div class="backlink-meta">${b.relationship} • contribution</div>
            ${b.context ? `<div class="backlink-context">${b.context}</div>` : ''}
          </div>
        `).join('')}
      ` : ''}
    `;
  } else {
    backlinksList.innerHTML = `
      <div class="backlinks-empty">
        <p class="hint">No backlinks found for <strong>${currentTerm.name}</strong>.</p>
        <p class="hint">Be the first to connect this term to other concepts or papers!</p>
        <button class="wiki-btn primary" onclick="addExplanation()">💡 Add Connection</button>
      </div>
    `;
  }
}

function getBacklinkCount(termId) {
  if (Object.keys(backlinkIndex).length === 0) {
    buildBacklinkIndex();
  }
  return (backlinkIndex[termId] || []).length;
}

function openGraphView() {
  window.open('wiki-graph.html', '_blank');
}

// Initialize
renderContributions();

// Close search results when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.wiki-search-bar')) {
    document.getElementById('searchResults').classList.remove('active');
  }
});
</script>
