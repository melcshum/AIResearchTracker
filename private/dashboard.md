---
title: "Dashboard"
---

<div class="dashboard-container">
<div class="dashboard-hero">
<h1>🎯 AI Research Tracker</h1>
<p class="dashboard-subtitle">Curated research on AI agents, reasoning, RAG, and multi-modal systems</p>
</div>

<div class="main-sections">
<h2> Navigate by Section</h2>
<p class="section-desc">Choose your access level to explore the system</p>

<div class="section-grid">
<a href="external-hub.html" class="section-card external">
<div class="section-icon">🌐</div>
<h3>Research Portal</h3>
<p class="section-tagline">Research Workflow & System Settings</p>
<ul class="section-features">
<li>🔄 5-phase research lifecycle (Discovery → Citation)</li>
<li>📚 Paper discovery, reading lists, and annotations</li>
<li>🧠 Concept exploration, wiki, and knowledge graph</li>
<li>⚙️ System configuration and automation</li>
<li>📊 Monitoring, analytics, and statistics</li>
</ul>
<span class="section-cta">Enter Research Portal →</span>
</a>

<a href="internal-hub.html" class="section-card internal">
<div class="section-icon">🔧</div>
<h3>Internal Part</h3>
<p class="section-tagline">System Architecture & Engineering</p>
<ul class="section-features">
<li>🏗️ 8-layer architecture with interactive UML diagrams</li>
<li>🔗 Component relationships and data flow visualization</li>
<li>⚡ Performance metrics and scalability analysis</li>
<li>🛠️ Technology stack and implementation patterns</li>
<li>📖 Engineering resources and technical documentation</li>
</ul>
<span class="section-cta">Enter Internal Part →</span>
</a>
</div>
</div>

<div class="quick-stats">
<div class="stat-card">
<div class="stat-icon">📄</div>
<div class="stat-content">
<div class="stat-number">77</div>
<div class="stat-label">Papers</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">👥</div>
<div class="stat-content">
<div class="stat-number">346</div>
<div class="stat-label">Authors</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">🏷️</div>
<div class="stat-content">
<div class="stat-number">4</div>
<div class="stat-label">Topics</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">📅</div>
<div class="stat-content">
<div class="stat-number">Daily</div>
<div class="stat-label">Updates</div>
</div>
</div>
</div>

<div class="quick-access">
<h3>⚡ Quick Access</h3>
<div class="quick-links">
<a href="global-search.html" class="quick-link">🔍 Global Search</a>
<a href="reading-list.html" class="quick-link">📋 Reading List</a>
<a href="wiki.html" class="quick-link">📖 Wiki</a>
<a href="wiki-graph.html" class="quick-link">🕸️ Knowledge Graph</a>
<a href="topics/ai-agents.html" class="quick-link"> AI Agents</a>
<a href="topics/llm-reasoning.html" class="quick-link">🧠 LLM Reasoning</a>
</div>
</div>
</div>

<style>
.dashboard-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.dashboard-hero {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 16px;
  margin-bottom: 40px;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
}

.dashboard-hero h1 {
  font-size: 3rem;
  margin-bottom: 15px;
  font-weight: 800;
}

.dashboard-subtitle {
  font-size: 1.3rem;
  opacity: 0.95;
}

.main-sections {
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin-bottom: 40px;
  text-align: center;
}

.main-sections h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.section-desc {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 30px;
}

.section-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 30px;
  margin-top: 30px;
}

.section-card {
  display: block;
  padding: 35px;
  border-radius: 16px;
  text-decoration: none;
  color: inherit;
  text-align: left;
  transition: all 0.3s;
  border: 3px solid transparent;
  position: relative;
  overflow: hidden;
}

.section-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.section-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.15);
}

.section-card.external {
  background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
  border-color: #667eea;
}

.section-card.external::before {
  background: linear-gradient(90deg, #667eea, #764ba2);
}

.section-card.external:hover {
  border-color: #764ba2;
}

.section-card.internal {
  background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%);
  border-color: #4facfe;
}

.section-card.internal::before {
  background: linear-gradient(90deg, #4facfe, #00f2fe);
}

.section-card.internal:hover {
  border-color: #00f2fe;
}

.section-icon {
  font-size: 4rem;
  margin-bottom: 15px;
}

.section-card h3 {
  font-size: 1.8rem;
  margin-bottom: 8px;
  color: #2c3e50;
}

.section-tagline {
  color: #666;
  font-size: 1rem;
  margin-bottom: 20px;
}

.section-features {
  list-style: none;
  padding: 0;
  margin: 0 0 20px 0;
}

.section-features li {
  padding: 6px 0;
  color: #444;
  font-size: 0.95rem;
}

.section-cta {
  display: inline-block;
  padding: 10px 20px;
  background: #2c3e50;
  color: white;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.2s;
}

.section-card.external .section-cta {
  background: linear-gradient(135deg, #667eea, #764ba2);
}

.section-card.internal .section-cta {
  background: linear-gradient(135deg, #4facfe, #00f2fe);
}

.section-card:hover .section-cta {
  transform: translateX(4px);
}

.quick-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  gap: 20px;
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.stat-icon {
  font-size: 3rem;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #667eea;
  line-height: 1;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  margin-top: 5px;
}

.quick-access {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 40px;
}

.quick-access h3 {
  color: #2c3e50;
  margin-bottom: 20px;
  font-size: 1.3rem;
}

.quick-links {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.quick-link {
  padding: 12px 20px;
  background: #f8f9fa;
  border-radius: 8px;
  text-decoration: none;
  color: #2c3e50;
  font-weight: 500;
  transition: all 0.2s;
  border: 2px solid transparent;
}

.quick-link:hover {
  background: #667eea;
  color: white;
  border-color: #667eea;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .dashboard-hero h1 {
    font-size: 2rem;
  }
  
  .section-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links {
    flex-direction: column;
  }
  
  .quick-link {
    width: 100%;
    text-align: center;
  }
}
</style>
