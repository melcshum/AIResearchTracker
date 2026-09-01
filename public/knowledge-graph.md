---
title: "Knowledge Graph"
---

# 🕸️ Knowledge Graph Visualization

Explore the interconnected landscape of your research papers, authors, topics, and concepts.

<div class="knowledge-graph-container">
  <div class="graph-controls">
    <div class="control-group">
      <label>Node Types:</label>
      <div class="checkbox-group">
        <label><input type="checkbox" id="showPapers" checked> Papers</label>
        <label><input type="checkbox" id="showAuthors" checked> Authors</label>
        <label><input type="checkbox" id="showTopics" checked> Topics</label>
        <label><input type="checkbox" id="showConcepts" checked> Concepts</label>
      </div>
    </div>
    
    <div class="control-group">
      <label>Layout:</label>
      <select id="layoutType">
        <option value="force">Force-Directed</option>
        <option value="radial">Radial</option>
        <option value="hierarchical">Hierarchical</option>
      </select>
    </div>
    
    <div class="control-group">
      <label>Filter by Topic:</label>
      <select id="topicFilter">
        <option value="all">All Topics</option>
      </select>
    </div>
    
    <button id="resetZoomBtn" class="btn-secondary">Reset View</button>
    <button id="exportGraphBtn" class="btn-secondary">Export Graph</button>
  </div>
  
  <div class="graph-legend">
    <div class="legend-item">
      <div class="legend-color paper"></div>
      <span>Papers</span>
    </div>
    <div class="legend-item">
      <div class="legend-color author"></div>
      <span>Authors</span>
    </div>
    <div class="legend-item">
      <div class="legend-color topic"></div>
      <span>Topics</span>
    </div>
    <div class="legend-item">
      <div class="legend-color concept"></div>
      <span>Concepts</span>
    </div>
  </div>
  
  <div class="graph-stats">
    <div class="stat-box">
      <div class="stat-number" id="totalNodes">0</div>
      <div class="stat-label">Total Nodes</div>
    </div>
    <div class="stat-box">
      <div class="stat-number" id="totalEdges">0</div>
      <div class="stat-label">Connections</div>
    </div>
    <div class="stat-box">
      <div class="stat-number" id="totalClusters">0</div>
      <div class="stat-label">Clusters</div>
    </div>
  </div>
  
  <div id="graphContainer" class="graph-container"></div>
  
  <div id="nodeDetails" class="node-details" style="display: none;">
    <div class="details-header">
      <h3 id="detailsTitle">Node Details</h3>
      <button class="close-btn" onclick="closeDetails()">&times;</button>
    </div>
    <div class="details-content" id="detailsContent"></div>
  </div>
</div>

<style>
.knowledge-graph-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.graph-controls {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 1.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  align-items: center;
}

.control-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.control-group label {
  font-weight: 500;
  color: #2c3e50;
}

.checkbox-group {
  display: flex;
  gap: 1rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-weight: normal;
  cursor: pointer;
}

.control-group select {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.btn-secondary {
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  background: #e0e0e0;
  color: #333;
  transition: all 0.2s;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.graph-legend {
  background: white;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 1.5rem;
  display: flex;
  gap: 2rem;
  justify-content: center;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.legend-color {
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.legend-color.paper {
  background: #3498db;
}

.legend-color.author {
  background: #e74c3c;
}

.legend-color.topic {
  background: #f39c12;
}

.legend-color.concept {
  background: #9b59b6;
}

.graph-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-box {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  text-align: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #2c5aa0;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.graph-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  width: 100%;
  height: 700px;
  position: relative;
  overflow: hidden;
}

.node-details {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  width: 500px;
  max-width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  z-index: 1000;
}

.details-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.details-header h3 {
  margin: 0;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #999;
  line-height: 1;
}

.close-btn:hover {
  color: #333;
}

.details-content {
  padding: 1.5rem;
}

.details-section {
  margin-bottom: 1.5rem;
}

.details-section h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.details-section p {
  color: #666;
  line-height: 1.6;
  margin: 0;
}

.details-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.details-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #f0f0f0;
  color: #555;
}

.details-list li:last-child {
  border-bottom: none;
}

.details-link {
  color: #2c5aa0;
  text-decoration: none;
  cursor: pointer;
}

.details-link:hover {
  text-decoration: underline;
}

.node {
  cursor: pointer;
  transition: all 0.2s;
}

.node:hover {
  filter: brightness(1.2);
}

.node-label {
  font-size: 11px;
  fill: #333;
  pointer-events: none;
  text-anchor: middle;
  dominant-baseline: middle;
}

.link {
  stroke: #95a5a6;
  stroke-opacity: 0.6;
  fill: none;
}

.tooltip {
  position: absolute;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.9rem;
  pointer-events: none;
  z-index: 1000;
  max-width: 300px;
}
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
let allPapers = [];
let graphData = { nodes: [], links: [] };
let simulation;
let svg;
let currentZoom;

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    populateTopicFilter();
    buildGraph();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function populateTopicFilter() {
  const topics = new Set();
  allPapers.forEach(paper => {
    if (paper.topics) {
      paper.topics.forEach(topic => topics.add(topic));
    }
  });
  
  const select = document.getElementById('topicFilter');
  Array.from(topics).sort().forEach(topic => {
    const option = document.createElement('option');
    option.value = topic;
    option.textContent = topic;
    select.appendChild(option);
  });
}

function buildGraph() {
  const topicFilter = document.getElementById('topicFilter').value;
  const showPapers = document.getElementById('showPapers').checked;
  const showAuthors = document.getElementById('showAuthors').checked;
  const showTopics = document.getElementById('showTopics').checked;
  const showConcepts = document.getElementById('showConcepts').checked;
  
  graphData = { nodes: [], links: [] };
  const nodeMap = new Map();
  
  // Filter papers by topic if needed
  let filteredPapers = allPapers;
  if (topicFilter !== 'all') {
    filteredPapers = allPapers.filter(p => p.topics && p.topics.includes(topicFilter));
  }
  
  // Add paper nodes
  if (showPapers) {
    filteredPapers.forEach(paper => {
      const nodeId = `paper_${paper.arxiv_id}`;
      if (!nodeMap.has(nodeId)) {
        const node = {
          id: nodeId,
          type: 'paper',
          title: paper.title,
          authors: paper.authors,
          date: paper.date,
          topics: paper.topics || [],
          abstract: paper.abstract,
          url: paper.url,
          radius: 8
        };
        graphData.nodes.push(node);
        nodeMap.set(nodeId, node);
      }
    });
  }
  
  // Add author nodes and links
  if (showAuthors) {
    filteredPapers.forEach(paper => {
      const authors = paper.authors.split(',').map(a => a.trim());
      authors.forEach(author => {
        const authorId = `author_${author}`;
        if (!nodeMap.has(authorId)) {
          const node = {
            id: authorId,
            type: 'author',
            name: author,
            papers: [],
            radius: 6
          };
          graphData.nodes.push(node);
          nodeMap.set(authorId, node);
        }
        
        const authorNode = nodeMap.get(authorId);
        authorNode.papers.push(paper.arxiv_id);
        
        // Link author to paper
        if (showPapers) {
          const paperNodeId = `paper_${paper.arxiv_id}`;
          if (nodeMap.has(paperNodeId)) {
            graphData.links.push({
              source: authorId,
              target: paperNodeId,
              type: 'authored'
            });
          }
        }
      });
    });
  }
  
  // Add topic nodes and links
  if (showTopics) {
    const topics = new Set();
    filteredPapers.forEach(paper => {
      if (paper.topics) {
        paper.topics.forEach(topic => topics.add(topic));
      }
    });
    
    topics.forEach(topic => {
      const topicId = `topic_${topic}`;
      if (!nodeMap.has(topicId)) {
        const node = {
          id: topicId,
          type: 'topic',
          name: topic,
          papers: [],
          radius: 10
        };
        graphData.nodes.push(node);
        nodeMap.set(topicId, node);
      }
      
      const topicNode = nodeMap.get(topicId);
      
      // Link topic to papers
      if (showPapers) {
        filteredPapers.forEach(paper => {
          if (paper.topics && paper.topics.includes(topic)) {
            topicNode.papers.push(paper.arxiv_id);
            const paperNodeId = `paper_${paper.arxiv_id}`;
            if (nodeMap.has(paperNodeId)) {
              graphData.links.push({
                source: topicId,
                target: paperNodeId,
                type: 'categorized'
              });
            }
          }
        });
      }
    });
  }
  
  // Add concept nodes (extracted from abstracts)
  if (showConcepts) {
    const concepts = extractConcepts(filteredPapers);
    
    concepts.forEach(concept => {
      const conceptId = `concept_${concept.name}`;
      if (!nodeMap.has(conceptId)) {
        const node = {
          id: conceptId,
          type: 'concept',
          name: concept.name,
          papers: concept.papers,
          radius: 7
        };
        graphData.nodes.push(node);
        nodeMap.set(conceptId, node);
      }
      
      // Link concept to papers
      if (showPapers) {
        concept.papers.forEach(arxivId => {
          const paperNodeId = `paper_${arxivId}`;
          if (nodeMap.has(paperNodeId)) {
            graphData.links.push({
              source: conceptId,
              target: paperNodeId,
              type: 'related'
            });
          }
        });
      }
    });
  }
  
  renderGraph();
}

function extractConcepts(papers) {
  const conceptMap = new Map();
  
  const conceptPatterns = [
    { pattern: /\b(agent|agents|agentic)\b/gi, name: 'AI Agents' },
    { pattern: /\b(retrieval|rag|retrieval-augmented)\b/gi, name: 'Retrieval' },
    { pattern: /\b(reasoning|chain-of-thought|cot)\b/gi, name: 'Reasoning' },
    { pattern: /\b(multi-modal|multimodal|vision-language)\b/gi, name: 'Multi-Modal' },
    { pattern: /\b(tool use|tool calling)\b/gi, name: 'Tool Use' },
    { pattern: /\b(planning|planner)\b/gi, name: 'Planning' },
    { pattern: /\b(memory|context)\b/gi, name: 'Memory' },
    { pattern: /\b(safety|alignment)\b/gi, name: 'Safety' },
    { pattern: /\b(evaluation|benchmark)\b/gi, name: 'Evaluation' },
    { pattern: /\b(gui|graphical user interface)\b/gi, name: 'GUI' }
  ];
  
  papers.forEach(paper => {
    const text = (paper.title + ' ' + (paper.abstract || '')).toLowerCase();
    
    conceptPatterns.forEach(({ pattern, name }) => {
      if (text.match(pattern)) {
        if (!conceptMap.has(name)) {
          conceptMap.set(name, { name, papers: [] });
        }
        conceptMap.get(name).papers.push(paper.arxiv_id);
      }
    });
  });
  
  return Array.from(conceptMap.values());
}

function renderGraph() {
  const container = document.getElementById('graphContainer');
  container.innerHTML = '';
  
  const width = container.clientWidth;
  const height = container.clientHeight;
  
  svg = d3.select('#graphContainer')
    .append('svg')
    .attr('width', width)
    .attr('height', height);
  
  // Add zoom behavior
  const zoom = d3.zoom()
    .scaleExtent([0.1, 4])
    .on('zoom', (event) => {
      g.attr('transform', event.transform);
      currentZoom = event.transform;
    });
  
  svg.call(zoom);
  
  const g = svg.append('g');
  
  // Create force simulation
  const layoutType = document.getElementById('layoutType').value;
  
  simulation = d3.forceSimulation(graphData.nodes)
    .force('link', d3.forceLink(graphData.links).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(d => d.radius + 5));
  
  // Add links
  const link = g.append('g')
    .selectAll('line')
    .data(graphData.links)
    .join('line')
    .attr('class', 'link')
    .attr('stroke-width', 1.5);
  
  // Add nodes
  const node = g.append('g')
    .selectAll('g')
    .data(graphData.nodes)
    .join('g')
    .attr('class', 'node')
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));
  
  node.append('circle')
    .attr('r', d => d.radius)
    .attr('fill', d => getNodeColor(d.type))
    .attr('stroke', '#fff')
    .attr('stroke-width', 2)
    .on('click', (event, d) => showNodeDetails(d))
    .on('mouseover', (event, d) => showTooltip(event, d))
    .on('mouseout', hideTooltip);
  
  // Add labels for larger nodes
  node.filter(d => d.radius >= 8)
    .append('text')
    .attr('class', 'node-label')
    .attr('dy', d => d.radius + 15)
    .text(d => d.title || d.name || '');
  
  // Update positions on each tick
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    
    node.attr('transform', d => `translate(${d.x},${d.y})`);
  });
  
  function dragstarted(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }
  
  function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }
  
  function dragended(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }
}

function getNodeColor(type) {
  const colors = {
    paper: '#3498db',
    author: '#e74c3c',
    topic: '#f39c12',
    concept: '#9b59b6'
  };
  return colors[type] || '#95a5a6';
}

function showTooltip(event, d) {
  const tooltip = d3.select('body').append('div')
    .attr('class', 'tooltip')
    .style('left', (event.pageX + 10) + 'px')
    .style('top', (event.pageY - 10) + 'px');
  
  let content = '';
  if (d.type === 'paper') {
    content = `<strong>${d.title}</strong><br>${d.authors}<br>${d.date}`;
  } else if (d.type === 'author') {
    content = `<strong>${d.name}</strong><br>${d.papers.length} papers`;
  } else if (d.type === 'topic') {
    content = `<strong>${d.name}</strong><br>${d.papers.length} papers`;
  } else if (d.type === 'concept') {
    content = `<strong>${d.name}</strong><br>${d.papers.length} papers`;
  }
  
  tooltip.html(content);
}

function hideTooltip() {
  d3.select('.tooltip').remove();
}

function showNodeDetails(node) {
  const detailsPanel = document.getElementById('nodeDetails');
  const detailsTitle = document.getElementById('detailsTitle');
  const detailsContent = document.getElementById('detailsContent');
  
  detailsTitle.textContent = node.title || node.name;
  
  let content = '';
  
  if (node.type === 'paper') {
    content = `
      <div class="details-section">
        <h4>Authors</h4>
        <p>${node.authors}</p>
      </div>
      <div class="details-section">
        <h4>Date</h4>
        <p>${node.date}</p>
      </div>
      <div class="details-section">
        <h4>Topics</h4>
        <p>${node.topics.join(', ')}</p>
      </div>
      <div class="details-section">
        <h4>Abstract</h4>
        <p>${node.abstract || 'No abstract available'}</p>
      </div>
      <div class="details-section">
        <h4>Links</h4>
        <ul class="details-list">
          <li><a href="${node.url}" target="_blank" class="details-link">View Paper →</a></li>
        </ul>
      </div>
    `;
  } else if (node.type === 'author') {
    content = `
      <div class="details-section">
        <h4>Papers (${node.papers.length})</h4>
        <ul class="details-list">
          ${node.papers.slice(0, 10).map(arxivId => {
            const paper = allPapers.find(p => p.arxiv_id === arxivId);
            return paper ? `<li><a href="${paper.url}" target="_blank" class="details-link">${paper.title}</a></li>` : '';
          }).join('')}
          ${node.papers.length > 10 ? `<li>... and ${node.papers.length - 10} more</li>` : ''}
        </ul>
      </div>
    `;
  } else if (node.type === 'topic' || node.type === 'concept') {
    content = `
      <div class="details-section">
        <h4>Related Papers (${node.papers.length})</h4>
        <ul class="details-list">
          ${node.papers.slice(0, 10).map(arxivId => {
            const paper = allPapers.find(p => p.arxiv_id === arxivId);
            return paper ? `<li><a href="${paper.url}" target="_blank" class="details-link">${paper.title}</a></li>` : '';
          }).join('')}
          ${node.papers.length > 10 ? `<li>... and ${node.papers.length - 10} more</li>` : ''}
        </ul>
      </div>
    `;
  }
  
  detailsContent.innerHTML = content;
  detailsPanel.style.display = 'block';
}

function closeDetails() {
  document.getElementById('nodeDetails').style.display = 'none';
}

function updateStats() {
  document.getElementById('totalNodes').textContent = graphData.nodes.length;
  document.getElementById('totalEdges').textContent = graphData.links.length;
  
  // Simple clustering based on node types
  const clusters = new Set(graphData.nodes.map(n => n.type));
  document.getElementById('totalClusters').textContent = clusters.size;
}

// Event listeners
document.getElementById('showPapers').addEventListener('change', buildGraph);
document.getElementById('showAuthors').addEventListener('change', buildGraph);
document.getElementById('showTopics').addEventListener('change', buildGraph);
document.getElementById('showConcepts').addEventListener('change', buildGraph);
document.getElementById('layoutType').addEventListener('change', buildGraph);
document.getElementById('topicFilter').addEventListener('change', buildGraph);

document.getElementById('resetZoomBtn').addEventListener('click', () => {
  svg.transition().duration(750).call(
    d3.zoom().transform,
    d3.zoomIdentity
  );
});

document.getElementById('exportGraphBtn').addEventListener('click', () => {
  const dataStr = JSON.stringify(graphData, null, 2);
  const blob = new Blob([dataStr], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'knowledge-graph.json';
  a.click();
  URL.revokeObjectURL(url);
});

// Initialize
loadData();
</script>
