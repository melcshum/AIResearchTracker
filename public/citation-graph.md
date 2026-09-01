---
title: "Citation Graph"
---

# 🕸️ Citation Graph & Paper Relationships

Visualize how papers cite each other and trace the evolution of research ideas.

<div class="citation-controls">
<button id="generateGraphBtn" class="btn-primary">Generate Citation Graph</button>
<select id="topicFilter" class="topic-filter">
<option value="all">All Topics</option>
</select>
<div class="graph-legend">
<span class="legend-item"><span class="legend-dot foundational"></span> Foundational</span>
<span class="legend-item"><span class="legend-dot recent"></span> Recent</span>
<span class="legend-item"><span class="legend-dot highly-cited"></span> Highly Cited</span>
</div>
</div>

<div class="citation-stats">
<div class="stat-box">
<div class="stat-number" id="totalPapers">0</div>
<div class="stat-label">Total Papers</div>
</div>
<div class="stat-box">
<div class="stat-number" id="citationLinks">0</div>
<div class="stat-label">Citation Links</div>
</div>
<div class="stat-box">
<div class="stat-number" id="avgCitations">0</div>
<div class="stat-label">Avg Citations</div>
</div>
<div class="stat-box">
<div class="stat-number" id="foundationalPapers">0</div>
<div class="stat-label">Foundational</div>
</div>
</div>

<div id="citationGraph" class="citation-graph"></div>

<div class="paper-relationships">
<h3>📊 Paper Relationships</h3>
<div id="relationshipList" class="relationship-list"></div>
</div>

<div class="citation-timeline">
<h3>📅 Citation Timeline</h3>
<div id="citationTimeline" class="timeline-chart"></div>
</div>

<style>
.citation-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.btn-primary {
  background: #2c5aa0;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #1e4a8f;
}

.topic-filter {
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.graph-legend {
  display: flex;
  gap: 1rem;
  margin-left: auto;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.9rem;
  color: #666;
}

.legend-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.legend-dot.foundational {
  background: #e74c3c;
}

.legend-dot.recent {
  background: #3498db;
}

.legend-dot.highly-cited {
  background: #f39c12;
}

.citation-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-box {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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

.citation-graph {
  width: 100%;
  height: 600px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}

.paper-relationships {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.paper-relationships h3 {
  margin-top: 0;
  color: #2c3e50;
}

.relationship-list {
  display: grid;
  gap: 1rem;
}

.relationship-item {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  border-left: 4px solid #2c5aa0;
}

.relationship-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.relationship-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.relationship-connections {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.connection-tag {
  background: #e8f4f8;
  color: #2c5aa0;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  font-size: 0.85rem;
}

.citation-timeline {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.citation-timeline h3 {
  margin-top: 0;
  color: #2c3e50;
}

.timeline-chart {
  height: 300px;
  position: relative;
}

.node {
  cursor: pointer;
  transition: all 0.2s;
}

.node:hover {
  transform: scale(1.2);
}

.link {
  stroke: #95a5a6;
  stroke-opacity: 0.6;
  stroke-width: 1.5px;
  fill: none;
}

.link:hover {
  stroke-opacity: 1;
  stroke-width: 2.5px;
}

.tooltip {
  position: absolute;
  background: white;
  padding: 1rem;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  pointer-events: none;
  z-index: 1000;
  max-width: 300px;
  font-size: 0.9rem;
}

.tooltip-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.tooltip-meta {
  color: #666;
  font-size: 0.85rem;
}
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
let papers = [];
let citationData = [];
let currentTopic = 'all';

async function loadPapers() {
  try {
    const response = await fetch('papers.json');
    papers = await response.json();
    populateTopicFilter();
    generateCitationGraph();
  } catch (error) {
    console.error('Error loading papers:', error);
  }
}

function populateTopicFilter() {
  const topics = new Set();
  papers.forEach(paper => {
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
  
  select.addEventListener('change', (e) => {
    currentTopic = e.target.value;
    generateCitationGraph();
  });
}

function analyzeCitations() {
  // Extract potential citations from abstracts and titles
  const citationMap = new Map();
  
  papers.forEach(paper => {
    const arxivId = paper.arxiv_id;
    if (!citationMap.has(arxivId)) {
      citationMap.set(arxivId, {
        paper: paper,
        cites: [],
        citedBy: [],
        year: new Date(paper.date).getFullYear()
      });
    }
  });
  
  // Analyze relationships based on topics and dates
  papers.forEach(paper => {
    const paperYear = new Date(paper.date).getFullYear();
    const paperTopics = paper.topics || [];
    
    papers.forEach(otherPaper => {
      if (paper.arxiv_id === otherPaper.arxiv_id) return;
      
      const otherYear = new Date(otherPaper.date).getFullYear();
      const otherTopics = otherPaper.topics || [];
      
      // Check if papers share topics and have temporal relationship
      const sharedTopics = paperTopics.filter(t => otherTopics.includes(t));
      
      if (sharedTopics.length > 0) {
        // Earlier paper might be cited by later paper
        if (otherYear > paperYear) {
          citationMap.get(otherPaper.arxiv_id).cites.push(paper.arxiv_id);
          citationMap.get(paper.arxiv_id).citedBy.push(otherPaper.arxiv_id);
        }
      }
    });
  });
  
  return citationMap;
}

function generateCitationGraph() {
  const citationMap = analyzeCitations();
  const nodes = [];
  const links = [];
  
  // Filter papers by topic if needed
  let filteredPapers = papers;
  if (currentTopic !== 'all') {
    filteredPapers = papers.filter(p => p.topics && p.topics.includes(currentTopic));
  }
  
  // Create nodes
  filteredPapers.forEach(paper => {
    const citationInfo = citationMap.get(paper.arxiv_id);
    const citationCount = citationInfo ? citationInfo.citedBy.length : 0;
    const year = new Date(paper.date).getFullYear();
    const currentYear = new Date().getFullYear();
    
    let nodeType = 'recent';
    if (citationCount >= 3) {
      nodeType = 'highly-cited';
    } else if (currentYear - year >= 2) {
      nodeType = 'foundational';
    }
    
    nodes.push({
      id: paper.arxiv_id,
      title: paper.title,
      authors: paper.authors,
      year: year,
      citations: citationCount,
      type: nodeType,
      topics: paper.topics || []
    });
    
    // Create links
    if (citationInfo) {
      citationInfo.cites.forEach(citedId => {
        if (filteredPapers.find(p => p.arxiv_id === citedId)) {
          links.push({
            source: paper.arxiv_id,
            target: citedId
          });
        }
      });
    }
  });
  
  // Update stats
  document.getElementById('totalPapers').textContent = nodes.length;
  document.getElementById('citationLinks').textContent = links.length;
  const avgCitations = nodes.length > 0 
    ? (nodes.reduce((sum, n) => sum + n.citations, 0) / nodes.length).toFixed(1)
    : 0;
  document.getElementById('avgCitations').textContent = avgCitations;
  document.getElementById('foundationalPapers').textContent = 
    nodes.filter(n => n.type === 'foundational').length;
  
  // Render D3 graph
  renderD3Graph(nodes, links);
  
  // Render relationship list
  renderRelationshipList(nodes, citationMap);
  
  // Render timeline
  renderTimeline(nodes);
}

function renderD3Graph(nodes, links) {
  const container = document.getElementById('citationGraph');
  container.innerHTML = '';
  
  const width = container.clientWidth;
  const height = container.clientHeight;
  
  const svg = d3.select('#citationGraph')
    .append('svg')
    .attr('width', width)
    .attr('height', height);
  
  const simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(30));
  
  // Create links
  const link = svg.append('g')
    .selectAll('line')
    .data(links)
    .join('line')
    .attr('class', 'link')
    .attr('marker-end', 'url(#arrow)');
  
  // Create arrow marker
  svg.append('defs').append('marker')
    .attr('id', 'arrow')
    .attr('viewBox', '0 -5 10 10')
    .attr('refX', 20)
    .attr('refY', 0)
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-5L10,0L0,5')
    .attr('fill', '#95a5a6');
  
  // Create nodes
  const node = svg.append('g')
    .selectAll('circle')
    .data(nodes)
    .join('circle')
    .attr('class', 'node')
    .attr('r', d => Math.max(8, Math.min(20, 8 + d.citations * 2)))
    .attr('fill', d => {
      if (d.type === 'foundational') return '#e74c3c';
      if (d.type === 'highly-cited') return '#f39c12';
      return '#3498db';
    })
    .attr('stroke', '#fff')
    .attr('stroke-width', 2)
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));
  
  // Add tooltips
  node.append('title')
    .text(d => `${d.title}\n${d.authors}\nYear: ${d.year}\nCitations: ${d.citations}`);
  
  // Add hover tooltip
  const tooltip = d3.select('body').append('div')
    .attr('class', 'tooltip')
    .style('opacity', 0);
  
  node.on('mouseover', (event, d) => {
    tooltip.transition()
      .duration(200)
      .style('opacity', .9);
    tooltip.html(`
<div class="tooltip-title">${d.title}</div>
<div class="tooltip-meta">${d.authors}</div>
<div class="tooltip-meta">Year: ${d.year}</div>
<div class="tooltip-meta">Citations: ${d.citations}</div>
<div class="tooltip-meta">Topics: ${d.topics.join(', ')}</div>
    `)
    .style('left', (event.pageX + 10) + 'px')
    .style('top', (event.pageY - 10) + 'px');
  })
  .on('mouseout', () => {
    tooltip.transition()
      .duration(500)
      .style('opacity', 0);
  });
  
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    
    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);
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

function renderRelationshipList(nodes, citationMap) {
  const container = document.getElementById('relationshipList');
  
  // Sort by citation count
  const sortedNodes = nodes.sort((a, b) => b.citations - a.citations).slice(0, 10);
  
  container.innerHTML = sortedNodes.map(node => {
    const citationInfo = citationMap.get(node.id);
    const connections = citationInfo ? [
      ...citationInfo.cites.slice(0, 3).map(id => {
        const paper = papers.find(p => p.arxiv_id === id);
        return paper ? `<span class="connection-tag">Cites: ${paper.title.substring(0, 40)}...</span>` : '';
      }),
      ...citationInfo.citedBy.slice(0, 3).map(id => {
        const paper = papers.find(p => p.arxiv_id === id);
        return paper ? `<span class="connection-tag">Cited by: ${paper.title.substring(0, 40)}...</span>` : '';
      })
    ].filter(Boolean) : [];
    
    return `
<div class="relationship-item">
<div class="relationship-title">${node.title}</div>
<div class="relationship-meta">
          ${node.authors} • ${node.year} • ${node.citations} citations
</div>
<div class="relationship-connections">
          ${connections.join('')}
</div>
</div>
    `;
  }).join('');
}

function renderTimeline(nodes) {
  const container = document.getElementById('citationTimeline');
  container.innerHTML = '';
  
  const width = container.clientWidth;
  const height = container.clientHeight;
  
  const svg = d3.select('#citationTimeline')
    .append('svg')
    .attr('width', width)
    .attr('height', height);
  
  // Group by year
  const yearCounts = {};
  nodes.forEach(node => {
    yearCounts[node.year] = (yearCounts[node.year] || 0) + 1;
  });
  
  const years = Object.keys(yearCounts).sort();
  const maxCount = Math.max(...Object.values(yearCounts));
  
  const xScale = d3.scaleBand()
    .domain(years)
    .range([50, width - 50])
    .padding(0.2);
  
  const yScale = d3.scaleLinear()
    .domain([0, maxCount])
    .range([height - 50, 50]);
  
  // Draw bars
  svg.selectAll('rect')
    .data(years)
    .join('rect')
    .attr('x', d => xScale(d))
    .attr('y', d => yScale(yearCounts[d]))
    .attr('width', xScale.bandwidth())
    .attr('height', d => height - 50 - yScale(yearCounts[d]))
    .attr('fill', '#2c5aa0')
    .attr('rx', 4);
  
  // Add labels
  svg.selectAll('.year-label')
    .data(years)
    .join('text')
    .attr('class', 'year-label')
    .attr('x', d => xScale(d) + xScale.bandwidth() / 2)
    .attr('y', height - 25)
    .attr('text-anchor', 'middle')
    .attr('fill', '#666')
    .attr('font-size', '12px')
    .text(d => d);
  
  // Add count labels
  svg.selectAll('.count-label')
    .data(years)
    .join('text')
    .attr('class', 'count-label')
    .attr('x', d => xScale(d) + xScale.bandwidth() / 2)
    .attr('y', d => yScale(yearCounts[d]) - 10)
    .attr('text-anchor', 'middle')
    .attr('fill', '#2c5aa0')
    .attr('font-size', '12px')
    .attr('font-weight', 'bold')
    .text(d => yearCounts[d]);
}

document.getElementById('generateGraphBtn').addEventListener('click', generateCitationGraph);

// Initialize
loadPapers();
</script>
