---
title: "Knowledge Graph"
---

<div class="kg-container">
<div class="kg-header">
<h2>🕸️ Knowledge Graph</h2>
<p class="kg-subtitle">Interactive visualization of connections between concepts, papers, and research areas</p>
<div class="kg-toolbar">
<div class="kg-filters">
<button class="kg-filter active" data-filter="all" onclick="filterGraph('all')">All</button>
<button class="kg-filter" data-filter="term" onclick="filterGraph('term')">📚 Terms</button>
<button class="kg-filter" data-filter="paper" onclick="filterGraph('paper')">📄 Papers</button>
<button class="kg-filter" data-filter="topic" onclick="filterGraph('topic')">🏷️ Topics</button>
</div>
<div class="kg-controls">
<input type="text" id="graphSearch" placeholder="🔍 Search nodes..." onkeyup="searchGraph()">
<button class="kg-btn" onclick="resetView()">↺ Reset</button>
<button class="kg-btn" onclick="toggleLabels()">🏷️ Labels</button>
<button class="kg-btn" onclick="toggleForce()">⚡ Physics</button>
</div>
</div>
</div>

<div class="kg-main">
<div class="kg-canvas-wrap">
<div id="graphCanvas" class="kg-canvas"></div>
<div class="kg-legend">
<div class="legend-row"><span class="legend-circle term"></span> Wiki Term</div>
<div class="legend-row"><span class="legend-circle paper"></span> Paper</div>
<div class="legend-row"><span class="legend-circle topic"></span> Topic</div>
<div class="legend-row"><span class="legend-line-strong"></span> Strong link</div>
<div class="legend-row"><span class="legend-line-weak"></span> Weak link</div>
</div>
<div class="kg-stats">
<span id="nodeCount">0 nodes</span> · <span id="linkCount">0 links</span>
</div>
</div>

<div class="kg-sidebar">
<div id="nodePanel" class="kg-panel">
<h3>📌 Node Details</h3>
<div id="nodeDetails" class="kg-details">
<p class="kg-hint">Click any node to explore</p>
</div>
</div>

<div id="connectionsPanel" class="kg-panel">
<h3>🔗 Connections</h3>
<div id="connectionsList" class="kg-connections">
<p class="kg-hint">Select a node to see connections</p>
</div>
</div>

<div id="navigatePanel" class="kg-panel">
<h3>🧭 Navigate</h3>
<div id="navigateList" class="kg-navigate">
<p class="kg-hint">Jump to any node</p>
</div>
</div>
</div>
</div>
</div>

<style>
.kg-container {
  max-width: 1600px;
  margin: 0 auto;
  padding: 20px;
}

.kg-header {
  text-align: center;
  margin-bottom: 24px;
}

.kg-header h2 {
  font-size: 2rem;
  color: #1a1a2e;
  margin-bottom: 8px;
}

.kg-subtitle {
  color: #666;
  font-size: 1.05rem;
  margin-bottom: 20px;
}

.kg-toolbar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.kg-filters {
  display: flex;
  gap: 6px;
  background: #f0f2f5;
  padding: 4px;
  border-radius: 10px;
}

.kg-filter {
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #555;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.2s;
}

.kg-filter:hover { background: rgba(255,255,255,0.6); }
.kg-filter.active { background: white; color: #667eea; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }

.kg-controls {
  display: flex;
  gap: 8px;
  align-items: center;
}

#graphSearch {
  padding: 8px 14px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 13px;
  width: 180px;
  transition: border-color 0.2s;
}

#graphSearch:focus { border-color: #667eea; outline: none; }

.kg-btn {
  padding: 8px 14px;
  border: 2px solid #667eea;
  border-radius: 8px;
  background: white;
  color: #667eea;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.2s;
}

.kg-btn:hover { background: #667eea; color: white; }

.kg-main {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 20px;
  min-height: 650px;
}

.kg-canvas-wrap {
  position: relative;
  background: linear-gradient(135deg, #f8f9ff 0%, #eef1ff 100%);
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(102,126,234,0.12);
  overflow: hidden;
}

.kg-canvas {
  width: 100%;
  height: 650px;
}

.kg-canvas svg {
  width: 100%;
  height: 100%;
  cursor: grab;
}

.kg-canvas svg:active { cursor: grabbing; }

.kg-legend {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(8px);
  padding: 12px 16px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  font-size: 12px;
}

.legend-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
  color: #555;
}

.legend-circle {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.legend-circle.term { background: #667eea; }
.legend-circle.paper { background: #f093fb; }
.legend-circle.topic { background: #4facfe; }

.legend-line-strong {
  width: 20px;
  height: 3px;
  background: #667eea;
  border-radius: 2px;
}

.legend-line-weak {
  width: 20px;
  height: 1px;
  background: #aaa;
}

.kg-stats {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(255,255,255,0.9);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  color: #666;
  font-weight: 500;
}

.kg-sidebar {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.kg-panel {
  background: white;
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}

.kg-panel h3 {
  margin: 0 0 12px 0;
  color: #1a1a2e;
  font-size: 1rem;
}

.kg-details, .kg-connections, .kg-navigate {
  min-height: 80px;
}

.kg-hint {
  color: #999;
  font-style: italic;
  text-align: center;
  padding: 20px 0;
  font-size: 13px;
}

.kg-detail-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 8px;
}

.kg-detail-type {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 600;
  color: white;
  margin-bottom: 10px;
}

.kg-detail-type.term { background: #667eea; }
.kg-detail-type.paper { background: #f093fb; }
.kg-detail-type.topic { background: #4facfe; }

.kg-detail-def {
  color: #555;
  line-height: 1.6;
  font-size: 13px;
  margin-bottom: 10px;
}

.kg-detail-meta {
  font-size: 12px;
  color: #888;
}

.kg-conn-item {
  padding: 10px 12px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 6px;
  cursor: pointer;
  transition: all 0.2s;
  border-left: 3px solid #667eea;
}

.kg-conn-item:hover {
  background: #eef1ff;
  transform: translateX(4px);
}

.kg-conn-title {
  font-weight: 600;
  font-size: 13px;
  color: #2c3e50;
}

.kg-conn-rel {
  font-size: 11px;
  color: #999;
  margin-top: 2px;
}

.kg-nav-item {
  padding: 8px 12px;
  background: #f8f9fa;
  border-radius: 6px;
  margin-bottom: 4px;
  cursor: pointer;
  transition: all 0.15s;
  font-size: 13px;
  color: #444;
}

.kg-nav-item:hover {
  background: #667eea;
  color: white;
}

/* SVG node/link styles */
.graph-node { cursor: pointer; }
.graph-node circle {
  transition: all 0.2s;
  stroke: white;
  stroke-width: 2px;
}
.graph-node:hover circle {
  stroke: #1a1a2e;
  stroke-width: 3px;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));
}
.graph-node.selected circle {
  stroke: #ff6b6b;
  stroke-width: 3px;
  filter: drop-shadow(0 0 8px rgba(255,107,107,0.5));
}
.graph-node.dimmed { opacity: 0.15; }
.graph-node.highlighted circle {
  stroke: #ffd93d;
  stroke-width: 3px;
}

.graph-label {
  font-size: 11px;
  font-weight: 600;
  fill: #2c3e50;
  text-anchor: middle;
  pointer-events: none;
}

.graph-link {
  stroke: #b0b8d1;
  stroke-opacity: 0.5;
  transition: stroke-opacity 0.2s;
}

.graph-link.strong { stroke-width: 2.5px; stroke: #667eea; stroke-opacity: 0.6; }
.graph-link.weak { stroke-width: 1px; stroke-dasharray: 4,4; }
.graph-link.dimmed { stroke-opacity: 0.05; }
.graph-link.highlighted { stroke: #ffd93d; stroke-opacity: 0.9; stroke-width: 3px; }

@media (max-width: 1024px) {
  .kg-main { grid-template-columns: 1fr; }
  .kg-canvas { height: 450px; }
}
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// ============================================================
// KNOWLEDGE GRAPH — Full interactive force-directed visualization
// ============================================================

let graphNodes = [];
let graphLinks = [];
let simulation = null;
let svg, g, linkSel, nodeSel, labelSel;
let zoomBehavior;
let showLabels = true;
let physicsActive = true;
let selectedNode = null;
let currentFilter = 'all';

// Color palette
const COLORS = {
  term: '#667eea',
  paper: '#f093fb',
  topic: '#4facfe',
  link: '#b0b8d1',
  linkStrong: '#667eea',
  highlight: '#ffd93d',
  selected: '#ff6b6b'
};

// Size by connection count
function nodeRadius(d) {
  const conns = graphLinks.filter(l =>
    (l.source.id || l.source) === d.id || (l.target.id || l.target) === d.id
  ).length;
  if (d.type === 'topic') return 28 + conns * 2;
  if (d.type === 'term') return 18 + conns * 1.5;
  return 12 + conns;
}

// ---- DATA: Build from wiki terms + papers ----
function buildGraphData() {
  const nodes = [];
  const links = [];
  const nodeIds = new Set();

  // Topic nodes
  const topics = [
    { id: 'topic-agents', label: 'AI Agents', type: 'topic', definition: 'Autonomous systems that perceive, reason, and act to achieve goals' },
    { id: 'topic-reasoning', label: 'LLM Reasoning', type: 'topic', definition: 'Chain-of-thought, self-consistency, and verification techniques' },
    { id: 'topic-rag', label: 'RAG & Retrieval', type: 'topic', definition: 'Dense retrieval, hybrid search, and knowledge grounding' },
    { id: 'topic-multimodal', label: 'Multi-Modal', type: 'topic', definition: 'Vision-language models and cross-modal reasoning' }
  ];
  topics.forEach(t => { nodes.push(t); nodeIds.add(t.id); });

  // Wiki terms
  const terms = [
    { id: 'ai-agent', label: 'AI Agent', type: 'term', definition: 'Autonomous system that perceives, reasons, and acts' },
    { id: 'llm', label: 'LLM', type: 'term', definition: 'Large Language Model — core reasoning engine' },
    { id: 'rag', label: 'RAG', type: 'term', definition: 'Retrieval-Augmented Generation' },
    { id: 'reasoning', label: 'Reasoning', type: 'term', definition: 'Step-by-step problem solving and logical inference' },
    { id: 'tool-use', label: 'Tool Use', type: 'term', definition: 'Invoking external functions and APIs' },
    { id: 'planning', label: 'Planning', type: 'term', definition: 'Decomposing goals into action sequences' },
    { id: 'retrieval', label: 'Retrieval', type: 'term', definition: 'Finding relevant information from knowledge bases' },
    { id: 'dense-retrieval', label: 'Dense Retrieval', type: 'term', definition: 'Semantic search with vector embeddings' },
    { id: 'multi-agent', label: 'Multi-Agent', type: 'term', definition: 'Multiple agents collaborating on complex tasks' },
    { id: 'memory', label: 'Memory', type: 'term', definition: 'Storing and retrieving context across interactions' },
    { id: 'cot', label: 'Chain-of-Thought', type: 'term', definition: 'Step-by-step reasoning prompting technique' },
    { id: 'self-consistency', label: 'Self-Consistency', type: 'term', definition: 'Sampling multiple reasoning paths for verification' },
    { id: 'verification', label: 'Verification', type: 'term', definition: 'Checking correctness of generated outputs' },
    { id: 'embedding', label: 'Embeddings', type: 'term', definition: 'Dense vector representations of text/images' },
    { id: 'reranking', label: 'Reranking', type: 'term', definition: 'Re-scoring retrieved results for relevance' },
    { id: 'hallucination', label: 'Hallucination', type: 'term', definition: 'Generating factually incorrect information' },
    { id: 'grounding', label: 'Grounding', type: 'term', definition: 'Connecting outputs to verifiable sources' },
    { id: 'vision-lang', label: 'Vision-Language', type: 'term', definition: 'Models processing both images and text' }
  ];
  terms.forEach(t => { nodes.push(t); nodeIds.add(t.id); });

  // Topic → term links
  links.push({ source: 'topic-agents', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'topic-agents', target: 'tool-use', strength: 'strong' });
  links.push({ source: 'topic-agents', target: 'planning', strength: 'strong' });
  links.push({ source: 'topic-agents', target: 'multi-agent', strength: 'strong' });
  links.push({ source: 'topic-agents', target: 'memory', strength: 'weak' });
  links.push({ source: 'topic-reasoning', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'topic-reasoning', target: 'cot', strength: 'strong' });
  links.push({ source: 'topic-reasoning', target: 'self-consistency', strength: 'strong' });
  links.push({ source: 'topic-reasoning', target: 'verification', strength: 'strong' });
  links.push({ source: 'topic-reasoning', target: 'llm', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'rag', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'dense-retrieval', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'reranking', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'embedding', strength: 'strong' });
  links.push({ source: 'topic-rag', target: 'grounding', strength: 'weak' });
  links.push({ source: 'topic-multimodal', target: 'vision-lang', strength: 'strong' });
  links.push({ source: 'topic-multimodal', target: 'embedding', strength: 'weak' });

  // Term → term links
  links.push({ source: 'ai-agent', target: 'llm', strength: 'strong' });
  links.push({ source: 'ai-agent', target: 'tool-use', strength: 'strong' });
  links.push({ source: 'ai-agent', target: 'planning', strength: 'strong' });
  links.push({ source: 'ai-agent', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'ai-agent', target: 'memory', strength: 'strong' });
  links.push({ source: 'rag', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'rag', target: 'llm', strength: 'strong' });
  links.push({ source: 'rag', target: 'grounding', strength: 'strong' });
  links.push({ source: 'rag', target: 'hallucination', strength: 'weak' });
  links.push({ source: 'retrieval', target: 'dense-retrieval', strength: 'strong' });
  links.push({ source: 'retrieval', target: 'embedding', strength: 'strong' });
  links.push({ source: 'retrieval', target: 'reranking', strength: 'strong' });
  links.push({ source: 'reasoning', target: 'cot', strength: 'strong' });
  links.push({ source: 'reasoning', target: 'self-consistency', strength: 'strong' });
  links.push({ source: 'reasoning', target: 'planning', strength: 'strong' });
  links.push({ source: 'reasoning', target: 'verification', strength: 'strong' });
  links.push({ source: 'multi-agent', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'multi-agent', target: 'planning', strength: 'weak' });
  links.push({ source: 'memory', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'memory', target: 'embedding', strength: 'weak' });
  links.push({ source: 'cot', target: 'self-consistency', strength: 'strong' });
  links.push({ source: 'verification', target: 'hallucination', strength: 'weak' });
  links.push({ source: 'grounding', target: 'hallucination', strength: 'strong' });
  links.push({ source: 'vision-lang', target: 'embedding', strength: 'strong' });
  links.push({ source: 'llm', target: 'hallucination', strength: 'weak' });
  links.push({ source: 'llm', target: 'cot', strength: 'strong' });

  // Paper nodes (key papers)
  const papers = [
    { id: 'p-260827508', label: 'WM-R1', type: 'paper', arxiv: '2608.27508', definition: 'Training GUI Agents to Reason with World Models' },
    { id: 'p-260827475', label: 'HER Agent', type: 'paper', arxiv: '2608.27475', definition: 'Hypothesize-Evaluate-Refine: A Scientific Agent' },
    { id: 'p-260827471', label: 'RAG Fallacies', type: 'paper', arxiv: '2608.27471', definition: 'Retrieving Relations & Detecting Fallacies via RAG' },
    { id: 'p-260827963', label: 'SABER', type: 'paper', arxiv: '2608.27963', definition: 'Stability-Aware Early Exit for LLM Reasoning' },
    { id: 'p-260827869', label: 'Multimodal PDE', type: 'paper', arxiv: '2608.27869', definition: 'See-Hypothesize-Validate: Multimodal Agentic Framework' },
    { id: 'p-260827646', label: 'Angel Agents', type: 'paper', arxiv: '2608.27646', definition: 'If Agents Were Angels: No Governance Would Be Necessary' },
    { id: 'p-260827524', label: 'SETU', type: 'paper', arxiv: '2608.27524', definition: 'Agentic Ecosystem for Multilingual Personalization' },
    { id: 'p-260827919', label: 'Docs→Reasoning', type: 'paper', arxiv: '2608.27919', definition: 'From Documents to Reasoning: Validated Synthetic Data' },
    { id: 'p-260827484', label: 'CareGraph', type: 'paper', arxiv: '2608.27484', definition: 'Auditable Hybrid AI for Evidence-Based Care' },
    { id: 'p-260722319', label: 'Naïve→Agentic RAG', type: 'paper', arxiv: '2607.22319', definition: 'Trustworthy and Cost-Efficient: Naïve RAG to Agentic' },
    { id: 'p-260827809', label: 'LINE-Conv', type: 'paper', arxiv: '2608.27809', definition: 'Conversation History Retrieval for Personal Memory RAG' },
    { id: 'p-260828389', label: 'CamoDocs', type: 'paper', arxiv: '2608.28389', definition: 'Poisoning Attack Against Retrieval-Augmented Language Models' }
  ];
  papers.forEach(p => { nodes.push(p); nodeIds.add(p.id); });

  // Paper → term links
  links.push({ source: 'p-260827508', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'p-260827508', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'p-260827508', target: 'vision-lang', strength: 'strong' });
  links.push({ source: 'p-260827475', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'p-260827475', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'p-260827475', target: 'verification', strength: 'strong' });
  links.push({ source: 'p-260827471', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260827471', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'p-260827471', target: 'reasoning', strength: 'weak' });
  links.push({ source: 'p-260827963', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'p-260827963', target: 'llm', strength: 'strong' });
  links.push({ source: 'p-260827963', target: 'verification', strength: 'weak' });
  links.push({ source: 'p-260827869', target: 'vision-lang', strength: 'strong' });
  links.push({ source: 'p-260827869', target: 'multi-agent', strength: 'strong' });
  links.push({ source: 'p-260827869', target: 'verification', strength: 'strong' });
  links.push({ source: 'p-260827646', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'p-260827646', target: 'multi-agent', strength: 'strong' });
  links.push({ source: 'p-260827524', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'p-260827524', target: 'llm', strength: 'strong' });
  links.push({ source: 'p-260827919', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260827919', target: 'reasoning', strength: 'strong' });
  links.push({ source: 'p-260827484', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260827484', target: 'grounding', strength: 'strong' });
  links.push({ source: 'p-260722319', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260722319', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'p-260722319', target: 'ai-agent', strength: 'strong' });
  links.push({ source: 'p-260827809', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260827809', target: 'memory', strength: 'strong' });
  links.push({ source: 'p-260827809', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'p-260828389', target: 'rag', strength: 'strong' });
  links.push({ source: 'p-260828389', target: 'retrieval', strength: 'strong' });
  links.push({ source: 'p-260828389', target: 'hallucination', strength: 'strong' });

  graphNodes = nodes;
  graphLinks = links;
  return { nodes, links };
}

// ---- INITIALIZE GRAPH ----
function initGraph() {
  const container = document.getElementById('graphCanvas');
  const width = container.clientWidth;
  const height = container.clientHeight || 650;

  const data = buildGraphData();

  svg = d3.select('#graphCanvas')
    .append('svg')
    .attr('width', width)
    .attr('height', height);

  // Arrow marker
  svg.append('defs').append('marker')
    .attr('id', 'arrowhead')
    .attr('viewBox', '0 -5 10 10')
    .attr('refX', 20)
    .attr('refY', 0)
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-5L10,0L0,5')
    .attr('fill', COLORS.link);

  g = svg.append('g');

  // Zoom behavior
  zoomBehavior = d3.zoom()
    .scaleExtent([0.2, 5])
    .on('zoom', (event) => {
      g.attr('transform', event.transform);
    });
  svg.call(zoomBehavior);

  // Draw links
  linkSel = g.append('g').attr('class', 'links')
    .selectAll('line')
    .data(data.links)
    .enter().append('line')
    .attr('class', d => `graph-link ${d.strength}`)
    .attr('stroke-width', d => d.strength === 'strong' ? 2.5 : 1);

  // Draw nodes
  nodeSel = g.append('g').attr('class', 'nodes')
    .selectAll('g')
    .data(data.nodes)
    .enter().append('g')
    .attr('class', 'graph-node')
    .call(d3.drag()
      .on('start', dragStarted)
      .on('drag', dragged)
      .on('end', dragEnded))
    .on('click', (event, d) => {
      event.stopPropagation();
      selectNode(d);
    });

  nodeSel.append('circle')
    .attr('r', d => nodeRadius(d))
    .attr('fill', d => COLORS[d.type])
    .attr('opacity', 0.85);

  // Labels
  labelSel = g.append('g').attr('class', 'labels')
    .selectAll('text')
    .data(data.nodes)
    .enter().append('text')
    .attr('class', 'graph-label')
    .attr('dy', d => nodeRadius(d) + 14)
    .text(d => d.label);

  // Force simulation
  simulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.links).id(d => d.id).distance(d => d.strength === 'strong' ? 80 : 140))
    .force('charge', d3.forceManyBody().strength(-350))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(d => nodeRadius(d) + 10))
    .force('x', d3.forceX(width / 2).strength(0.05))
    .force('y', d3.forceY(height / 2).strength(0.05))
    .on('tick', ticked);

  // Click background to deselect
  svg.on('click', () => deselectAll());

  // Update stats
  document.getElementById('nodeCount').textContent = `${data.nodes.length} nodes`;
  document.getElementById('linkCount').textContent = `${data.links.length} links`;

  // Build navigate list
  buildNavigateList();
}

function ticked() {
  linkSel
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y);

  nodeSel.attr('transform', d => `translate(${d.x},${d.y})`);
  labelSel.attr('x', d => d.x).attr('y', d => d.y);
}

// ---- DRAG ----
function dragStarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragEnded(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

// ---- SELECT NODE ----
function selectNode(d) {
  selectedNode = d;

  // Highlight selected + neighbors
  const neighborIds = new Set();
  graphLinks.forEach(l => {
    const sid = l.source.id || l.source;
    const tid = l.target.id || l.target;
    if (sid === d.id) neighborIds.add(tid);
    if (tid === d.id) neighborIds.add(sid);
  });
  neighborIds.add(d.id);

  nodeSel.classed('selected', n => n.id === d.id)
    .classed('dimmed', n => !neighborIds.has(n.id))
    .classed('highlighted', n => neighborIds.has(n.id) && n.id !== d.id);

  linkSel.classed('dimmed', l => {
    const sid = l.source.id || l.source;
    const tid = l.target.id || l.target;
    return sid !== d.id && tid !== d.id;
  }).classed('highlighted', l => {
    const sid = l.source.id || l.source;
    const tid = l.target.id || l.target;
    return sid === d.id || tid === d.id;
  });

  // Update detail panel
  const details = document.getElementById('nodeDetails');
  const connCount = graphLinks.filter(l =>
    (l.source.id || l.source) === d.id || (l.target.id || l.target) === d.id
  ).length;

  details.innerHTML = `
<div class="kg-detail-title">${d.label}</div>
<span class="kg-detail-type ${d.type}">${d.type.toUpperCase()}</span>
<div class="kg-detail-def">${d.definition || 'No description available'}</div>
<div class="kg-detail-meta">
      ${d.arxiv ? `<div>📄 arXiv: <a href="papers/2026-08-31/${d.arxiv}*.html" target="_blank">${d.arxiv}</a></div>` : ''}
<div>🔗 ${connCount} connections</div>
<div>📏 Radius: ${Math.round(nodeRadius(d))}px</div>
</div>
  `;

  // Update connections panel
  const connections = graphLinks.filter(l =>
    (l.source.id || l.source) === d.id || (l.target.id || l.target) === d.id
  );

  const connList = document.getElementById('connectionsList');
  if (connections.length > 0) {
    connList.innerHTML = connections.map(l => {
      const sid = l.source.id || l.source;
      const tid = l.target.id || l.target;
      const otherId = sid === d.id ? tid : sid;
      const other = graphNodes.find(n => n.id === otherId);
      const direction = sid === d.id ? '→' : '←';
      return `
<div class="kg-conn-item" onclick="focusNode('${otherId}')">
<div class="kg-conn-title">${direction} ${other ? other.label : otherId}</div>
<div class="kg-conn-rel">${l.strength} link · ${other ? other.type : ''}</div>
</div>
      `;
    }).join('');
  } else {
    connList.innerHTML = '<p class="kg-hint">No connections</p>';
  }
}

function deselectAll() {
  selectedNode = null;
  nodeSel.classed('selected', false).classed('dimmed', false).classed('highlighted', false);
  linkSel.classed('dimmed', false).classed('highlighted', false);
  document.getElementById('nodeDetails').innerHTML = '<p class="kg-hint">Click any node to explore</p>';
  document.getElementById('connectionsList').innerHTML = '<p class="kg-hint">Select a node to see connections</p>';
}

// ---- FOCUS / ZOOM TO NODE ----
function focusNode(nodeId) {
  const node = graphNodes.find(n => n.id === nodeId);
  if (!node) return;

  selectNode(node);

  const container = document.getElementById('graphCanvas');
  const width = container.clientWidth;
  const height = container.clientHeight || 650;
  const scale = 1.5;

  svg.transition().duration(750).call(
    zoomBehavior.transform,
    d3.zoomIdentity
      .translate(width / 2, height / 2)
      .scale(scale)
      .translate(-node.x, -node.y)
  );
}

// ---- FILTER ----
function filterGraph(filter) {
  currentFilter = filter;

  document.querySelectorAll('.kg-filter').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.filter === filter);
  });

  nodeSel.style('display', d => {
    if (filter === 'all') return null;
    return d.type === filter ? null : 'none';
  });

  labelSel.style('display', d => {
    if (filter === 'all') return null;
    return d.type === filter ? null : 'none';
  });

  linkSel.style('display', l => {
    if (filter === 'all') return null;
    const sType = (typeof l.source === 'object' ? l.source : graphNodes.find(n => n.id === l.source))?.type;
    const tType = (typeof l.target === 'object' ? l.target : graphNodes.find(n => n.id === l.target))?.type;
    return (sType === filter || tType === filter) ? null : 'none';
  });

  // Update visible counts
  const visibleNodes = graphNodes.filter(n => filter === 'all' || n.type === filter);
  const visibleLinks = graphLinks.filter(l => {
    if (filter === 'all') return true;
    const sType = (typeof l.source === 'object' ? l.source : graphNodes.find(n => n.id === l.source))?.type;
    const tType = (typeof l.target === 'object' ? l.target : graphNodes.find(n => n.id === l.target))?.type;
    return sType === filter || tType === filter;
  });

  document.getElementById('nodeCount').textContent = `${visibleNodes.length} nodes`;
  document.getElementById('linkCount').textContent = `${visibleLinks.length} links`;
}

// ---- SEARCH ----
function searchGraph() {
  const query = document.getElementById('graphSearch').value.toLowerCase().trim();
  if (!query) {
    nodeSel.classed('dimmed', false).classed('highlighted', false);
    linkSel.classed('dimmed', false);
    return;
  }

  const matchIds = new Set();
  graphNodes.forEach(n => {
    if (n.label.toLowerCase().includes(query) || (n.definition || '').toLowerCase().includes(query)) {
      matchIds.add(n.id);
    }
  });

  nodeSel.classed('dimmed', n => !matchIds.has(n.id))
    .classed('highlighted', n => matchIds.has(n.id));

  linkSel.classed('dimmed', l => {
    const sid = l.source.id || l.source;
    const tid = l.target.id || l.target;
    return !matchIds.has(sid) && !matchIds.has(tid);
  });

  // If single match, focus it
  if (matchIds.size === 1) {
    const id = [...matchIds][0];
    focusNode(id);
  }
}

// ---- CONTROLS ----
function resetView() {
  const container = document.getElementById('graphCanvas');
  const width = container.clientWidth;
  const height = container.clientHeight || 650;

  svg.transition().duration(500).call(
    zoomBehavior.transform,
    d3.zoomIdentity.translate(0, 0).scale(1)
  );

  deselectAll();
  document.getElementById('graphSearch').value = '';
  filterGraph('all');
}

function toggleLabels() {
  showLabels = !showLabels;
  labelSel.style('display', showLabels ? null : 'none');
}

function toggleForce() {
  physicsActive = !physicsActive;
  if (physicsActive) {
    simulation.alpha(0.5).restart();
  } else {
    simulation.stop();
    // Pin all nodes
    graphNodes.forEach(n => { n.fx = n.x; n.fy = n.y; });
  }
}

// ---- NAVIGATE LIST ----
function buildNavigateList() {
  const navList = document.getElementById('navigateList');
  const sorted = [...graphNodes].sort((a, b) => a.label.localeCompare(b.label));

  navList.innerHTML = sorted.map(n => `
<div class="kg-nav-item" onclick="focusNode('${n.id}')">
      ${n.type === 'term' ? '📚' : n.type === 'paper' ? '📄' : '🏷️'} ${n.label}
</div>
  `).join('');
}

// ---- INIT ON LOAD ----
document.addEventListener('DOMContentLoaded', initGraph);
</script>
