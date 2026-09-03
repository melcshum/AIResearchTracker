---
title: "Internal Part"
---

<div class="hub-container">
<div class="hub-hero internal-hero">
<div class="hub-icon">🔧</div>
<h1>Internal Part</h1>
<p class="hub-subtitle">System Architecture & Engineering — Understand the design and implementation</p>
</div>

<div class="hub-sections">

<!-- SYSTEM ARCHITECTURE OVERVIEW -->
<div class="hub-section architecture-section">
<div class="section-header">
<div class="section-icon">🏗️</div>
<h2>System Architecture Overview</h2>
<p class="section-desc">8-layer architecture powering the AI Research Tracker</p>
</div>

<div class="architecture-diagram">
<div class="layer top-layer">
<div class="layer-title">User Interface Layer</div>
<div class="layer-content">Dashboard, Role Hubs, Navigation</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer">
<div class="layer-title">Search & Discovery Layer</div>
<div class="layer-content">Global Search, Paper Search, Tag Cloud</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer">
<div class="layer-title">Wiki & Knowledge Management</div>
<div class="layer-content">Bidirectional Links, Knowledge Graph, Backlinks</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer">
<div class="layer-title">Data Generation Layer</div>
<div class="layer-content">Search Index, Authors, Statistics, RSS</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer">
<div class="layer-title">Data Enhancement Layer</div>
<div class="layer-content">Key Contributions, Related Papers, Citations</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer">
<div class="layer-title">Data Ingestion Layer</div>
<div class="layer-content">arXiv API, Paper Fetching, Filtering</div>
</div>
<div class="layer-arrow">↓</div>
<div class="layer bottom-layer">
<div class="layer-title">Automation & Deployment</div>
<div class="layer-content">Pipeline Scripts, Server Management, Scheduling</div>
</div>
</div>

<div class="architecture-stats">
<div class="stat-box">
<div class="stat-number">77</div>
<div class="stat-label">Papers Tracked</div>
</div>
<div class="stat-box">
<div class="stat-number">346</div>
<div class="stat-label">Authors Indexed</div>
</div>
<div class="stat-box">
<div class="stat-number">123</div>
<div class="stat-label">Pages Generated</div>
</div>
<div class="stat-box">
<div class="stat-number">15</div>
<div class="stat-label">Python Scripts</div>
</div>
<div class="stat-box">
<div class="stat-number">58s</div>
<div class="stat-label">Pipeline Time</div>
</div>
</div>

<div class="architecture-actions">
<a href="system-architecture.html" class="arch-action-btn primary">View Interactive UML Diagrams</a>
<a href="SYSTEM_ARCHITECTURE.html" class="arch-action-btn">Read Architecture Documentation</a>
</div>
</div>

<!-- COMPONENT RELATIONSHIPS -->
<div class="hub-section component-section">
<div class="section-header">
<div class="section-icon">🔗</div>
<h2>Component Relationships</h2>
<p class="section-desc">How scripts, data, and pages interact</p>
</div>

<div class="component-map">
<div class="component-group ingestion">
<div class="group-title">📥 Data Ingestion</div>
<div class="component">fetch_arxiv.py</div>
<div class="component">automate.py</div>
<div class="component-connector">→</div>
<div class="output">papers/*.md</div>
</div>

<div class="component-group enhancement">
<div class="group-title">🔧 Data Enhancement</div>
<div class="component">enhance_papers.py</div>
<div class="component">enhance_paper_details.py</div>
<div class="component">inject_wikilinks.py</div>
<div class="component">add_bookmark_buttons.py</div>
<div class="component-connector">→</div>
<div class="output">Enhanced Papers</div>
</div>

<div class="component-group generation">
<div class="group-title">📊 Data Generation</div>
<div class="component">generate_search_index.py</div>
<div class="component">generate_authors.py</div>
<div class="component">generate_statistics.py</div>
<div class="component">generate_tagcloud_data.py</div>
<div class="component">generate_notes.py</div>
<div class="component">generate_rss.py</div>
<div class="component-connector">→</div>
<div class="output">Data Pages</div>
</div>

<div class="component-group build">
<div class="group-title">🏗️ Build & Serve</div>
<div class="component">quarto render</div>
<div class="component-connector">→</div>
<div class="output">_site/ (123 pages)</div>
<div class="component-connector">→</div>
<div class="component">python3 -m http.server</div>
<div class="component-connector">→</div>
<div class="output">http://100.64.0.17:8001</div>
</div>
</div>

<div class="component-details">
<div class="detail-card">
<h3>📥 Ingestion Scripts</h3>
<div class="detail-links">
<a href="fetch_arxiv.py">fetch_arxiv.py</a>
<a href="automate.py">automate.py</a>
</div>
</div>
<div class="detail-card">
<h3>🔧 Enhancement Scripts</h3>
<div class="detail-links">
<a href="enhance_papers.py">enhance_papers.py</a>
<a href="enhance_paper_details.py">enhance_paper_details.py</a>
<a href="inject_wikilinks.py">inject_wikilinks.py</a>
</div>
</div>
<div class="detail-card">
<h3>📊 Generation Scripts</h3>
<div class="detail-links">
<a href="generate_search_index.py">generate_search_index.py</a>
<a href="generate_authors.py">generate_authors.py</a>
<a href="generate_statistics.py">generate_statistics.py</a>
</div>
</div>
</div>
</div>

<!-- DATA FLOW -->
<div class="hub-section dataflow-section">
<div class="section-header">
<div class="section-icon">🔄</div>
<h2>Data Flow Pipeline</h2>
<p class="section-desc">Step-by-step transformation from arXiv to rendered pages</p>
</div>

<div class="dataflow-diagram">
<div class="flow-step">
<div class="flow-icon">📡</div>
<div class="flow-title">arXiv API</div>
<div class="flow-desc">Query papers (cs.AI, cs.CL, cs.IR, cs.LG, cs.MM)</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">📥</div>
<div class="flow-title">fetch_arxiv.py</div>
<div class="flow-desc">Download & save as markdown</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">📄</div>
<div class="flow-title">Raw Papers</div>
<div class="flow-desc">papers/YYYY-MM-DD/*.md</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">🔧</div>
<div class="flow-title">Enhancement</div>
<div class="flow-desc">Add contributions, citations, wiki links</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">📊</div>
<div class="flow-title">Data Generation</div>
<div class="flow-desc">Search index, authors, stats, RSS</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">🏗️</div>
<div class="flow-title">Quarto Render</div>
<div class="flow-desc">Build 123 HTML pages</div>
</div>
<div class="flow-arrow">→</div>
<div class="flow-step">
<div class="flow-icon">🌐</div>
<div class="flow-title">Web Server</div>
<div class="flow-desc">Serve at port 8001</div>
</div>
</div>

<div class="dataflow-metrics">
<div class="metric-card">
<div class="metric-label">Fetch Time</div>
<div class="metric-value">~30s</div>
<div class="metric-detail">34 papers</div>
</div>
<div class="metric-card">
<div class="metric-label">Enhance Time</div>
<div class="metric-value">~15s</div>
<div class="metric-detail">77 papers</div>
</div>
<div class="metric-card">
<div class="metric-label">Generate Time</div>
<div class="metric-value">~10s</div>
<div class="metric-detail">All data pages</div>
</div>
<div class="metric-card">
<div class="metric-label">Render Time</div>
<div class="metric-value">~3s</div>
<div class="metric-detail">123 pages</div>
</div>
<div class="metric-card total">
<div class="metric-label">Total Pipeline</div>
<div class="metric-value">58s</div>
<div class="metric-detail">Complete cycle</div>
</div>
</div>
</div>

<!-- TECHNOLOGY STACK -->
<div class="hub-section tech-section">
<div class="section-header">
<div class="section-icon">🛠️</div>
<h2>Technology Stack</h2>
<p class="section-desc">Tools, frameworks, and technologies used</p>
</div>

<div class="tech-grid">
<div class="tech-category">
<div class="category-title">🐍 Backend (Build Time)</div>
<div class="tech-items">
<div class="tech-item">
<div class="tech-name">Python 3.9.6</div>
<div class="tech-desc">Data processing scripts</div>
</div>
<div class="tech-item">
<div class="tech-name">Quarto</div>
<div class="tech-desc">Static site generator</div>
</div>
<div class="tech-item">
<div class="tech-name">arXiv API</div>
<div class="tech-desc">Paper source</div>
</div>
</div>
</div>

<div class="tech-category">
<div class="category-title">🎨 Frontend (Runtime)</div>
<div class="tech-items">
<div class="tech-item">
<div class="tech-name">HTML5</div>
<div class="tech-desc">Structure</div>
</div>
<div class="tech-item">
<div class="tech-name">CSS3</div>
<div class="tech-desc">Styling (cosmo + custom)</div>
</div>
<div class="tech-item">
<div class="tech-name">Vanilla JavaScript</div>
<div class="tech-desc">Interactivity</div>
</div>
<div class="tech-item">
<div class="tech-name">D3.js v7</div>
<div class="tech-desc">Graph visualization</div>
</div>
<div class="tech-item">
<div class="tech-name">Mermaid v10</div>
<div class="tech-desc">Diagram rendering</div>
</div>
</div>
</div>

<div class="tech-category">
<div class="category-title">💾 Storage</div>
<div class="tech-items">
<div class="tech-item">
<div class="tech-name">File System</div>
<div class="tech-desc">Markdown files</div>
</div>
<div class="tech-item">
<div class="tech-name">localStorage</div>
<div class="tech-desc">Client-side data</div>
</div>
</div>
</div>

<div class="tech-category">
<div class="category-title">🚀 Infrastructure</div>
<div class="tech-items">
<div class="tech-item">
<div class="tech-name">Python HTTP Server</div>
<div class="tech-desc">Development server</div>
</div>
<div class="tech-item">
<div class="tech-name">Tailscale</div>
<div class="tech-desc">Network access</div>
</div>
<div class="tech-item">
<div class="tech-name">macOS Shortcuts</div>
<div class="tech-desc">Automation</div>
</div>
</div>
</div>
</div>
</div>

<!-- ENGINEERING RESOURCES -->
<div class="hub-section engineering-section">
<div class="section-header">
<div class="section-icon">⚙️</div>
<h2>Engineering Resources</h2>
<p class="section-desc">Implementation details, patterns, and best practices</p>
</div>

<div class="resource-grid">
<div class="resource-card">
<div class="resource-icon">📋</div>
<h3>Agent Guide</h3>
<p>Complete development guide with architecture summary</p>
<a href="AGENTS.html" class="resource-link">View AGENTS.md →</a>
</div>

<div class="resource-card">
<div class="resource-icon">🎨</div>
<h3>Design Guide</h3>
<p>Design system, components, and visual patterns</p>
<a href="DESIGN_GUIDE.html" class="resource-link">View Design Guide →</a>
</div>

<div class="resource-card">
<div class="resource-icon">✨</div>
<h3>UI Enhancements</h3>
<p>Before/after improvements and visual changes</p>
<a href="UI_ENHANCEMENTS.html" class="resource-link">View UI Enhancements →</a>
</div>

<div class="resource-card">
<div class="resource-icon">📖</div>
<h3>Obsidian Features</h3>
<p>Obsidian feature comparison and implementation status</p>
<a href="OBSIDIAN_ENHANCEMENTS.html" class="resource-link">View Obsidian Features →</a>
</div>

<div class="resource-card">
<div class="resource-icon">🔗</div>
<h3>Backlinks Implementation</h3>
<p>Bidirectional linking implementation details</p>
<a href="BACKLINKS_IMPLEMENTATION.html" class="resource-link">View Implementation →</a>
</div>

<div class="resource-card">
<div class="resource-icon">📊</div>
<h3>Statistics Dashboard</h3>
<p>Analytics and system metrics</p>
<a href="statistics.html" class="resource-link">View Statistics →</a>
</div>
</div>
</div>

<!-- PERFORMANCE & SCALING -->
<div class="hub-section performance-section">
<div class="section-header">
<div class="section-icon">⚡</div>
<h2>Performance & Scaling</h2>
<p class="section-desc">Current metrics and scalability limits</p>
</div>

<div class="performance-grid">
<div class="perf-card">
<div class="perf-title">Runtime Performance</div>
<div class="perf-metrics">
<div class="perf-item">
<span class="perf-label">Page Load:</span>
<span class="perf-value">&lt;100ms</span>
</div>
<div class="perf-item">
<span class="perf-label">Search:</span>
<span class="perf-value">&lt;50ms</span>
</div>
<div class="perf-item">
<span class="perf-label">Graph Render:</span>
<span class="perf-value">~100ms</span>
</div>
<div class="perf-item">
<span class="perf-label">Wiki Backlinks:</span>
<span class="perf-value">~50ms</span>
</div>
</div>
</div>

<div class="perf-card">
<div class="perf-title">Scalability Limits</div>
<div class="perf-metrics">
<div class="perf-item">
<span class="perf-label">Search Index:</span>
<span class="perf-value">~1,000 items</span>
</div>
<div class="perf-item">
<span class="perf-label">Graph Nodes:</span>
<span class="perf-value">~200 nodes</span>
</div>
<div class="perf-item">
<span class="perf-label">Wiki Terms:</span>
<span class="perf-value">~100 terms</span>
</div>
<div class="perf-item">
<span class="perf-label">Current:</span>
<span class="perf-value">77 papers</span>
</div>
</div>
</div>

<div class="perf-card">
<div class="perf-title">Future Enhancements</div>
<div class="perf-metrics">
<div class="perf-item">
<span class="perf-label">Phase 5:</span>
<span class="perf-value">Advanced Features</span>
</div>
<div class="perf-item">
<span class="perf-label">Phase 6:</span>
<span class="perf-value">External Integration</span>
</div>
<div class="perf-item">
<span class="perf-label">Phase 7:</span>
<span class="perf-value">Analytics</span>
</div>
</div>
</div>
</div>
</div>

</div>

<div class="hub-footer">
<a href="dashboard.html" class="back-link">← Back to Dashboard</a>
</div>
</div>

<style>
/* Base styles */
.hub-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.hub-hero {
  text-align: center;
  padding: 60px 20px;
  color: white;
  border-radius: 16px;
  margin-bottom: 40px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}

.internal-hero {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.hub-icon {
  font-size: 4rem;
  margin-bottom: 15px;
}

.hub-hero h1 {
  font-size: 3rem;
  margin-bottom: 15px;
  font-weight: 800;
}

.hub-subtitle {
  font-size: 1.3rem;
  opacity: 0.95;
}

.hub-section {
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin-bottom: 30px;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.section-icon {
  font-size: 3rem;
}

.section-header h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin: 0;
}

.section-desc {
  color: #666;
  font-size: 1.05rem;
  margin: 5px 0 0 0;
}

/* Architecture Diagram */
.architecture-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 30px;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
  border-radius: 12px;
}

.layer {
  width: 100%;
  max-width: 600px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-left: 5px solid #4facfe;
}

.layer.top-layer {
  border-left-color: #667eea;
  background: linear-gradient(135deg, #f8f9ff 0%, #eef0ff 100%);
}

.layer.bottom-layer {
  border-left-color: #f5576c;
  background: linear-gradient(135deg, #fff5f5 0%, #ffe5e5 100%);
}

.layer-title {
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 8px;
  font-size: 1.1rem;
}

.layer-content {
  color: #666;
  font-size: 0.95rem;
}

.layer-arrow {
  font-size: 2rem;
  color: #4facfe;
  font-weight: bold;
}

/* Architecture Stats */
.architecture-stats {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin: 30px 0;
}

.stat-box {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: white;
  padding: 25px;
  border-radius: 12px;
  text-align: center;
  min-width: 120px;
  box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.9;
}

.architecture-actions {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
}

.arch-action-btn {
  padding: 15px 30px;
  background: white;
  border: 2px solid #4facfe;
  border-radius: 8px;
  color: #4facfe;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.arch-action-btn:hover {
  background: #4facfe;
  color: white;
  transform: translateY(-2px);
}

.arch-action-btn.primary {
  background: #4facfe;
  color: white;
}

/* Component Map */
.component-map {
  display: flex;
  flex-direction: column;
  gap: 25px;
  padding: 30px;
  background: #f8f9fa;
  border-radius: 12px;
}

.component-group {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.group-title {
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.component {
  display: inline-block;
  background: #e8f4fd;
  padding: 8px 15px;
  border-radius: 6px;
  margin: 5px;
  font-family: monospace;
  font-size: 0.9rem;
  color: #2c3e50;
  border: 1px solid #b3d7ff;
}

.component-connector {
  display: inline-block;
  margin: 0 10px;
  font-size: 1.5rem;
  color: #4facfe;
  font-weight: bold;
}

.output {
  display: inline-block;
  background: #d4edda;
  padding: 8px 15px;
  border-radius: 6px;
  font-weight: 600;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.component-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.detail-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.detail-card h3 {
  margin: 0 0 15px 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.detail-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.detail-links a {
  display: block;
  padding: 8px 12px;
  background: #f8f9fa;
  border-radius: 6px;
  text-decoration: none;
  color: #4facfe;
  font-size: 0.9rem;
  font-family: monospace;
  transition: all 0.2s;
  border: 1px solid #e0e0e0;
}

.detail-links a:hover {
  background: #4facfe;
  color: white;
  transform: translateX(5px);
}

/* Data Flow Diagram */
.dataflow-diagram {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 15px;
  padding: 30px;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
  border-radius: 12px;
}

.flow-step {
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  min-width: 140px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.flow-icon {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.flow-title {
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
  font-size: 1rem;
}

.flow-desc {
  color: #666;
  font-size: 0.85rem;
}

.flow-arrow {
  font-size: 2rem;
  color: #4facfe;
  font-weight: bold;
}

/* Data Flow Metrics */
.dataflow-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.metric-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border-top: 4px solid #4facfe;
}

.metric-card.total {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: white;
  border-top: none;
  box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);
}

.metric-label {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 10px;
}

.metric-card.total .metric-label {
  color: rgba(255,255,255,0.9);
}

.metric-value {
  font-size: 2rem;
  font-weight: 800;
  color: #4facfe;
  margin-bottom: 5px;
}

.metric-card.total .metric-value {
  color: white;
}

.metric-detail {
  font-size: 0.85rem;
  color: #999;
}

.metric-card.total .metric-detail {
  color: rgba(255,255,255,0.8);
}

/* Tech Grid */
.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}

.tech-category {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 12px;
  border-left: 4px solid #4facfe;
}

.category-title {
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.tech-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tech-item {
  background: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.tech-name {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
  font-size: 1rem;
}

.tech-desc {
  color: #666;
  font-size: 0.9rem;
}

/* Resource Grid */
.resource-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.resource-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  transition: all 0.3s;
  border-left: 4px solid #4facfe;
}

.resource-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

.resource-icon {
  font-size: 2.5rem;
  margin-bottom: 15px;
}

.resource-card h3 {
  margin: 0 0 10px 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.resource-card p {
  color: #666;
  margin: 0 0 15px 0;
  font-size: 0.95rem;
}

.resource-link {
  display: inline-block;
  color: #4facfe;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.2s;
}

.resource-link:hover {
  color: #2c3e50;
  transform: translateX(5px);
}

/* Performance Grid */
.performance-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}

.perf-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  border-left: 4px solid #4facfe;
}

.perf-title {
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 20px;
  font-size: 1.1rem;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 10px;
}

.perf-metrics {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.perf-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: #f8f9fa;
  border-radius: 6px;
}

.perf-label {
  color: #666;
  font-size: 0.95rem;
}

.perf-value {
  color: #4facfe;
  font-weight: 700;
  font-size: 1rem;
}

/* Hub Footer */
.hub-footer {
  text-align: center;
  padding: 20px;
}

.back-link {
  display: inline-block;
  padding: 12px 24px;
  background: #f8f9fa;
  border-radius: 8px;
  text-decoration: none;
  color: #2c3e50;
  font-weight: 600;
  transition: all 0.2s;
}

.back-link:hover {
  background: #4facfe;
  color: white;
  transform: translateX(-5px);
}

/* Responsive */
@media (max-width: 768px) {
  .hub-hero h1 {
    font-size: 2rem;
  }
  
  .section-header {
    flex-direction: column;
    text-align: center;
  }
  
  .architecture-diagram,
  .dataflow-diagram {
    flex-direction: column;
  }
  
  .layer-arrow,
  .flow-arrow {
    transform: rotate(90deg);
    margin: 10px 0;
  }
  
  .tech-grid,
  .resource-grid,
  .performance-grid {
    grid-template-columns: 1fr;
  }
}
</style>
