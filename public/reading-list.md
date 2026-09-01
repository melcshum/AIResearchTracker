---
title: "My Reading List"
---

<div class="reading-list-container">
<div class="list-header">
<h2>📚 Reading List</h2>
<div class="list-actions">
<select id="statusFilter" class="filter-select">
<option value="all">All Status</option>
<option value="inbox">📥 Inbox</option>
<option value="reading">📖 Reading</option>
<option value="read">✅ Read</option>
<option value="cited">📝 Cited</option>
<option value="archived">🗄️ Archived</option>
</select>
<button id="exportBibBtn" class="btn-secondary">Export BibTeX</button>
<button id="exportMdBtn" class="btn-secondary">Export Markdown</button>
<button id="clearBtn" class="btn-danger">Clear All</button>
</div>
</div>

<div class="reading-stats">
<div class="stat-box">
<div class="stat-number" id="inboxCount">0</div>
<div class="stat-label">Inbox</div>
</div>
<div class="stat-box">
<div class="stat-number" id="readingCount">0</div>
<div class="stat-label">Reading</div>
</div>
<div class="stat-box">
<div class="stat-number" id="readCount">0</div>
<div class="stat-label">Read</div>
</div>
<div class="stat-box">
<div class="stat-number" id="citedCount">0</div>
<div class="stat-label">Cited</div>
</div>
</div>
  
<div id="readingList" class="reading-list">
<p class="empty-state">Your reading list is empty. Click the bookmark icon on any paper to add it here.</p>
</div>
  
<div class="list-stats">
<span id="paperCount">0 papers saved</span>
</div>
</div>

<style>
.reading-list-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e0e0e0;
}

.list-header h2 {
  margin: 0;
  color: #2c3e50;
}

.list-actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.filter-select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  background: white;
}

.reading-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 15px;
  margin-bottom: 30px;
}

.stat-box {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.stat-box .stat-number {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 5px;
}

.stat-box .stat-label {
  font-size: 14px;
  opacity: 0.9;
}

.btn-secondary, .btn-danger {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

.btn-danger {
  background: #dc3545;
  color: white;
}

.btn-danger:hover {
  background: #c82333;
}

.reading-list {
  display: grid;
  gap: 15px;
}

.paper-item {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  transition: all 0.2s;
  position: relative;
}

.paper-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-color: #4a90e2;
}

.paper-item-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 10px;
}

.paper-title {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  flex: 1;
  margin-right: 15px;
}

.paper-title a {
  color: #2c3e50;
  text-decoration: none;
}

.paper-title a:hover {
  color: #4a90e2;
}

.paper-actions {
  display: flex;
  gap: 8px;
  align-items: center;
}

.status-select {
  padding: 6px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  background: white;
}

.remove-btn {
  background: none;
  border: none;
  color: #dc3545;
  cursor: pointer;
  font-size: 20px;
  padding: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: background 0.2s;
}

.remove-btn:hover {
  background: #fee;
}

.paper-meta {
  color: #666;
  font-size: 14px;
  margin-bottom: 10px;
}

.paper-abstract {
  color: #444;
  font-size: 14px;
  line-height: 1.6;
  margin-top: 10px;
}

.paper-notes {
  margin-top: 15px;
  padding: 12px;
  background: #f8f9fa;
  border-radius: 6px;
  border-left: 3px solid #4a90e2;
}

.paper-notes textarea {
  width: 100%;
  min-height: 80px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  font-size: 13px;
  resize: vertical;
}

.paper-notes button {
  margin-top: 8px;
  padding: 6px 12px;
  background: #4a90e2;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
}

.paper-notes button:hover {
  background: #357abd;
}

.empty-state {
  text-align: center;
  color: #999;
  padding: 60px 20px;
  font-size: 16px;
}

.list-stats {
  margin-top: 30px;
  padding-top: 15px;
  border-top: 1px solid #e0e0e0;
  color: #666;
  font-size: 14px;
}

.topic-tag {
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-top: 8px;
}

.status-badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
  margin-top: 8px;
}

.status-inbox { background: #e3f2fd; color: #1976d2; }
.status-reading { background: #fff3e0; color: #f57c00; }
.status-read { background: #e8f5e9; color: #388e3c; }
.status-cited { background: #f3e5f5; color: #7b1fa2; }
.status-archived { background: #eceff1; color: #546e7a; }
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
const papers = [
  {
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "authors": "Nolasque, T, Grey, J, Pham, C, Vani, A",
    "date": "2026-08-31",
    "abstract": "Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there ",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27506",
    "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html"
  },
  {
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "authors": "Dore, D, Damo, G, Cabrio, E, Villata, S",
    "date": "2026-08-31",
    "abstract": "Fallacies are arguments that employ invalid reasoning, making their automatic detection critical in sensitive contexts such as high-stakes political debates, where public opinion is shaped. Spotting a",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27471",
    "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html"
  },
  {
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "authors": "Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "date": "2026-08-31",
    "abstract": "Give an agent a human&#39;s credential and it inherits the person&#39;s reach without the judgment that limits its use. It can sweep every reachable record into model context, where hidden instruction",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27646",
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement chang",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27475",
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently pr",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27840",
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, ",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27508",
    "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html"
  },
  {
    "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
    "authors": "Ghawate, P, Patil, T",
    "date": "2026-08-31",
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an audita",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27484",
    "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html"
  },
  {
    "title": "The Illusion of $\\\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
    "authors": "Wang, Y, Du, Y, Liu, Z, Zhang, R, Zhao, B, Yang, B, Kong, M, Wei, H, Liu, J, Zhu, Q",
    "date": "2026-08-31",
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded se",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27953",
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning y",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27963",
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\\\emph{cross-session decomposition attack",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27945",
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places",
    "authors": "Armitage, J, Tsochantaridis, I, Mazzone, L, Yan, C, Narayanan, S, Ebling, S",
    "date": "2026-08-31",
    "abstract": "We introduce MAP, the first benchmark to evaluate multimodal AI systems as assistants for users with accessibility requirements when planning visits to places in the real world. In our evaluation, sys",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.28384",
    "url": "papers/2026-08-31/2608.28384-MAP-A-Benchmark-on-Multimodal-Accessibility-Planni.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approac",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.27869",
    "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html"
  },
  {
    "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
    "authors": "Tejas, J M, Roy, U B, Goswami, T, Goswami, S, Dhar, M",
    "date": "2026-08-31",
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce bl",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27524",
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents",
    "authors": "Liu, Z, Zhang, H, Niu, L, Cao, Z, Li, H, Liu, J, Chen, W, Zhao, C, Yu, C, Meng, F",
    "date": "2026-08-31",
    "abstract": "Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.28062",
    "url": "papers/2026-08-31/2608.28062-WeAgent-MMSearch-Native-Text-Vision-Interaction-fo.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary a",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.27548",
    "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html"
  },
  {
    "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
    "authors": "Liu, R, Gu, N, Ai, M, Li, Y, Fu, P, Lin, Z, Wang, W",
    "date": "2026-08-31",
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promisin",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.27867",
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, ",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27919",
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  }
];

// User data management via API
let userBookmarks = [];
let userReadingProgress = {};
let userNotes = {};

async function loadUserData() {
  try {
    const response = await fetch(API_BASE + '/api/user/data');
    const data = await response.json();
    userBookmarks = data.bookmarks || [];
    userReadingProgress = data.readingProgress || {};
    userNotes = data.notes || {};
  } catch (error) {
    console.error('Failed to load user data:', error);
  }
}

async function saveBookmark(arxivId) {
  try {
    await fetch(API_BASE + '/api/user/bookmarks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ paperId: arxivId })
    });
    if (!userBookmarks.includes(arxivId)) {
      userBookmarks.push(arxivId);
    }
  } catch (error) {
    console.error('Failed to save bookmark:', error);
  }
}

async function removeBookmark(arxivId) {
  try {
    await fetch(`${API_BASE}/api/user/bookmarks/${arxivId}`, {
      method: 'DELETE'
    });
    userBookmarks = userBookmarks.filter(id => id !== arxivId);
  } catch (error) {
    console.error('Failed to remove bookmark:', error);
  }
}

async function updateReadingProgress(arxivId, status) {
  try {
    await fetch(`${API_BASE}/api/user/reading-progress/${arxivId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status })
    });
    userReadingProgress[arxivId] = { status, updatedAt: new Date().toISOString() };
  } catch (error) {
    console.error('Failed to update reading progress:', error);
  }
}

async function saveNote(arxivId, note) {
  try {
    await fetch(`${API_BASE}/api/user/notes/${arxivId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ note })
    });
    userNotes[arxivId] = note;
  } catch (error) {
    console.error('Failed to save note:', error);
  }
}

function updateStats() {
  const counts = { inbox: 0, reading: 0, read: 0, cited: 0, archived: 0 };
  userBookmarks.forEach(arxivId => {
    const progress = userReadingProgress[arxivId];
    const s = progress ? progress.status : 'inbox';
    counts[s] = (counts[s] || 0) + 1;
  });
  
  document.getElementById('inboxCount').textContent = counts.inbox;
  document.getElementById('readingCount').textContent = counts.reading;
  document.getElementById('readCount').textContent = counts.read;
  document.getElementById('citedCount').textContent = counts.cited;
}

function renderReadingList() {
  const filter = document.getElementById('statusFilter').value;
  const container = document.getElementById('readingList');
  const countEl = document.getElementById('paperCount');
  
  if (userBookmarks.length === 0) {
    container.innerHTML = '<p class="empty-state">Your reading list is empty. Click the bookmark icon on any paper to add it here.</p>';
    countEl.textContent = '0 papers saved';
    updateStats();
    return;
  }
  
  const filteredList = userBookmarks.filter(arxivId => {
    if (filter === 'all') return true;
    const progress = userReadingProgress[arxivId];
    const status = progress ? progress.status : 'inbox';
    return status === filter;
  });
  
  if (filteredList.length === 0) {
    container.innerHTML = '<p class="empty-state">No papers with this status.</p>';
    countEl.textContent = `${userBookmarks.length} total, 0 matching filter`;
    updateStats();
    return;
  }
  
  container.innerHTML = filteredList.map(arxivId => {
    const paper = papers.find(p => p.arxiv_id === arxivId);
    if (!paper) return '';
    
    const progress = userReadingProgress[arxivId];
    const currentStatus = progress ? progress.status : 'inbox';
    const currentNotes = userNotes[arxivId] || '';
    
    return `
      <div class="paper-item">
        <div class="paper-item-header">
          <div class="paper-title">
            <a href="${paper.url}" target="_blank">${paper.title}</a>
          </div>
          <div class="paper-actions">
            <select class="status-select" onchange="updateStatus('${arxivId}', this.value)">
              <option value="inbox" ${currentStatus === 'inbox' ? 'selected' : ''}>📥 Inbox</option>
              <option value="reading" ${currentStatus === 'reading' ? 'selected' : ''}>📖 Reading</option>
              <option value="read" ${currentStatus === 'read' ? 'selected' : ''}>✅ Read</option>
              <option value="cited" ${currentStatus === 'cited' ? 'selected' : ''}>📝 Cited</option>
              <option value="archived" ${currentStatus === 'archived' ? 'selected' : ''}>🗄️ Archived</option>
            </select>
            <button class="remove-btn" onclick="removePaper('${arxivId}')" title="Remove from list">×</button>
          </div>
        </div>
        <div class="paper-meta">
          <strong>Authors:</strong> ${paper.authors}<br>
          <strong>Date:</strong> ${paper.date}<br>
          <strong>Topics:</strong> ${paper.topics.map(t => `<span class="topic-tag">${t}</span>`).join(' ')}
        </div>
        <div class="paper-abstract">${paper.abstract}...</div>
        <div class="paper-notes">
          <textarea id="notes-${arxivId}" placeholder="Add your notes about this paper...">${currentNotes}</textarea>
          <button onclick="saveNotes('${arxivId}')">💾 Save Notes</button>
        </div>
      </div>
    `;
  }).join('');
  
  countEl.textContent = `${filteredList.length} of ${userBookmarks.length} papers shown`;
  updateStats();
}

async function updateStatus(arxivId, newStatus) {
  await updateReadingProgress(arxivId, newStatus);
  updateStats();
}

async function saveNotes(arxivId) {
  const textarea = document.getElementById(`notes-${arxivId}`);
  await saveNote(arxivId, textarea.value);
  alert('Notes saved!');
}

async function removePaper(arxivId) {
  await removeBookmark(arxivId);
  delete userReadingProgress[arxivId];
  delete userNotes[arxivId];
  renderReadingList();
}

function exportBibTeX() {
  if (userBookmarks.length === 0) {
    alert('Your reading list is empty');
    return;
  }
  
  const selectedPapers = userBookmarks.map(id => papers.find(p => p.arxiv_id === id)).filter(p => p);
  
  let bib = '';
  selectedPapers.forEach(paper => {
    const key = paper.arxiv_id;
    const authors = paper.authors.replace(/,/g, ' and');
    bib +=  PH5 ;
    bib +=  PH6 ;
    bib +=  PH7 ;
    bib +=  PH8 ;
    bib +=  PH9 ;
    bib +=  PH10 ;
    bib +=  PH11 ;
    bib +=  PH12 ;
  });
  
  const blob = new Blob([bib], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download =  PH13 ;
  a.click();
  URL.revokeObjectURL(url);
}

function exportMarkdown() {
  if (userBookmarks.length === 0) {
    alert('Your reading list is empty');
    return;
  }
  
  const selectedPapers = userBookmarks.map(id => papers.find(p => p.arxiv_id === id)).filter(p => p);
  
  let md = '# My Reading List\n\n';
  md +=  PH14 ;
  md +=  PH15 ;
  
  selectedPapers.forEach((paper, i) => {
    const progress = userReadingProgress[paper.arxiv_id];
    const s = progress ? progress.status : 'inbox';
    const n = userNotes[paper.arxiv_id] || '';
    
    md +=  PH16 ;
    md +=  PH17 ;
    md +=  PH18 ;
    md +=  PH19 ;
    md +=  PH20 ;
    md +=  PH21 ;
    md +=  PH22 ;
    md +=  PH23 ;
    
    if (n) {
      md +=  PH24 ;
    }
    
    md +=  PH25 ;
  });
  
  const blob = new Blob([md], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download =  PH26 ;
  a.click();
  URL.revokeObjectURL(url);
}

function clearList() {
  if (confirm('Are you sure you want to clear your entire reading list?')) {
    userBookmarks = [];
    userReadingProgress = {};
    userNotes = {};
    renderReadingList();
  }
}

document.getElementById('exportBibBtn').addEventListener('click', exportBibTeX);
document.getElementById('exportMdBtn').addEventListener('click', exportMarkdown);
document.getElementById('clearBtn').addEventListener('click', clearList);
document.getElementById('statusFilter').addEventListener('change', renderReadingList);

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
  loadUserData().then(() => {
    renderReadingList();
  });
});
</script>
