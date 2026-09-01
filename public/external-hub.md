---
title: "Research Portal"
---

<div class="hub-container">
<div class="hub-hero external-hero">
<div class="hub-icon">🌐</div>
<h1>Research Portal</h1>
<p class="hub-subtitle">Your complete research management environment — discover, read, synthesize, and cite</p>
</div>

<!-- RECENT ACTIVITY & QUICK ACTIONS -->
<div class="activity-actions-grid">
<div class="activity-feed-card">
<div class="card-header">
<h3>📊 Recent Activity</h3>
<span class="activity-count" id="activityCount">5 new</span>
</div>
<div class="activity-feed" id="activityFeed">
<!-- Populated dynamically by JavaScript -->
</div>
<a href="reading-list.html" class="view-all-link">View all activity →</a>
</div>

<div class="quick-actions-card">
<div class="card-header">
<h3>⚡ Quick Actions</h3>
</div>
<div class="quick-actions-grid">
<a href="global-search.html" class="quick-action-btn">
<div class="action-icon">🔍</div>
<div class="action-label">Search Papers</div>
</a>
<a href="reading-list.html" class="quick-action-btn">
<div class="action-icon">📋</div>
<div class="action-label">Reading List</div>
</a>
<a href="wiki.html" class="quick-action-btn">
<div class="action-icon">📖</div>
<div class="action-label">Wiki</div>
</a>
<a href="statistics.html" class="quick-action-btn">
<div class="action-icon">📊</div>
<div class="action-label">Statistics</div>
</a>
<a href="tag-cloud.html" class="quick-action-btn">
<div class="action-icon">🏷️</div>
<div class="action-label">Tag Cloud</div>
</a>
<a href="digests/index.html" class="quick-action-btn">
<div class="action-icon">📰</div>
<div class="action-label">Weekly Digest</div>
</a>
</div>
</div>
</div>

<div class="hub-sections">

<!-- RESEARCH WORKFLOW SECTION -->
<div class="hub-section workflow-section">
<div class="section-header">
<div class="section-icon">🔄</div>
<h2>Research Workflow</h2>
<p class="section-desc">Complete 5-phase research lifecycle with guided progression</p>
</div>

<div class="workflow-stepper">
<div class="stepper-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 20%"></div>
</div>
<div class="progress-text">Phase 1 of 5</div>
</div>

<div class="stepper-steps">
<div class="stepper-step active" data-phase="1">
<div class="step-indicator">
<div class="step-circle">
<span class="step-icon">📥</span>
</div>
<div class="step-line"></div>
</div>
<div class="step-content">
<div class="step-header">
<h3>Discovery</h3>
<span class="step-badge">Current</span>
</div>
<p class="step-description">Find and bookmark relevant papers for your research</p>
<div class="step-meta">
<span class="meta-item">📄 34 papers available</span>
<span class="meta-item">⏱️ ~15 min</span>
</div>
</div>
</div>

<div class="stepper-step" data-phase="2">
<div class="step-indicator">
<div class="step-circle">
<span class="step-icon">📖</span>
</div>
<div class="step-line"></div>
</div>
<div class="step-content">
<div class="step-header">
<h3>Screening</h3>
<span class="step-badge upcoming">Upcoming</span>
</div>
<p class="step-description">Quickly assess paper relevance and update status</p>
<div class="step-meta">
<span class="meta-item">📋 Inbox review</span>
<span class="meta-item">⏱️ ~10 min</span>
</div>
</div>
</div>

<div class="stepper-step" data-phase="3">
<div class="step-indicator">
<div class="step-circle">
<span class="step-icon">📚</span>
</div>
<div class="step-line"></div>
</div>
<div class="step-content">
<div class="step-header">
<h3>Deep Reading</h3>
<span class="step-badge upcoming">Upcoming</span>
</div>
<p class="step-description">Extract key insights, methodology, and take structured notes</p>
<div class="step-meta">
<span class="meta-item">📝 Detailed notes</span>
<span class="meta-item">⏱️ ~30 min</span>
</div>
</div>
</div>

<div class="stepper-step" data-phase="4">
<div class="step-indicator">
<div class="step-circle">
<span class="step-icon">🧠</span>
</div>
<div class="step-line"></div>
</div>
<div class="step-content">
<div class="step-header">
<h3>Synthesis</h3>
<span class="step-badge upcoming">Upcoming</span>
</div>
<p class="step-description">Connect ideas across papers and build knowledge</p>
<div class="step-meta">
<span class="meta-item">🔗 Concept mapping</span>
<span class="meta-item">⏱️ ~20 min</span>
</div>
</div>
</div>

<div class="stepper-step" data-phase="5">
<div class="step-indicator">
<div class="step-circle">
<span class="step-icon">📝</span>
</div>
</div>
<div class="step-content">
<div class="step-header">
<h3>Citation</h3>
<span class="step-badge upcoming">Upcoming</span>
</div>
<p class="step-description">Export references and integrate with your writing tools</p>
<div class="step-meta">
<span class="meta-item">📚 BibTeX export</span>
<span class="meta-item">⏱️ ~5 min</span>
</div>
</div>
</div>
</div>
</div>

<div class="workflow-dashboard" id="workflowDashboard">
<div class="workflow-stats">
<div class="stat-card">
<div class="stat-icon">📥</div>
<div class="stat-label">Inbox</div>
<div class="stat-value" id="inboxCount">0</div>
<div class="stat-tip">New papers to review</div>
</div>
<div class="stat-card">
<div class="stat-icon">📖</div>
<div class="stat-label">Reading</div>
<div class="stat-value" id="readingCount">0</div>
<div class="stat-tip">Currently reading</div>
</div>
<div class="stat-card">
<div class="stat-icon">✅</div>
<div class="stat-label">Read</div>
<div class="stat-value" id="readCount">0</div>
<div class="stat-tip">Completed</div>
</div>
<div class="stat-card">
<div class="stat-icon">📝</div>
<div class="stat-label">Cited</div>
<div class="stat-value" id="citedCount">0</div>
<div class="stat-tip">Used in research</div>
</div>
</div>
<div class="workflow-actions">
<a href="reading-list.html" class="workflow-action-btn primary">View Reading List</a>
<a href="research-workflow.html" class="workflow-action-btn">Workflow Guide</a>
</div>
</div>
</div>

<!-- RESEARCHER TOOLS SECTION -->
<div class="hub-section researcher-section">
<div class="section-header">
<div class="section-icon">🔬</div>
<h2>Researcher Tools</h2>
<p class="section-desc">Paper discovery, reading management, and knowledge building</p>
</div>

<div class="phase-based-navigation">
<div class="phase-panel" data-phase="discovery">
<div class="phase-header">
<h3>📥 Discovery Phase</h3>
<p>Find relevant papers for your research</p>
</div>
<div class="phase-tools">
<div class="tool-card">
<h4>Topic Exploration</h4>
<div class="tool-links">
<a href="topics/ai-agents.html">🤖 AI Agents</a>
<a href="topics/llm-reasoning.html">🧠 LLM Reasoning</a>
<a href="topics/rag-retrieval.html">🔍 RAG & Retrieval</a>
<a href="topics/multi-modal.html">🎬 Multi-Modal</a>
</div>
</div>
<div class="tool-card">
<h4>Search & Browse</h4>
<div class="tool-links">
<a href="global-search.html">🔍 Global Search (Cmd+K)</a>
<a href="search-papers.html">📄 Search Papers</a>
<a href="tag-cloud.html">🏷️ Tag Cloud</a>
<a href="authors.html">👥 Authors</a>
</div>
</div>
<div class="tool-card">
<h4>Stay Current</h4>
<div class="tool-links">
<a href="digests/index.html">📰 Weekly Digests</a>
<a href="rss.xml">📡 RSS Feed</a>
<a href="must-read-papers.html">⭐ Must-Read Papers</a>
</div>
</div>
</div>
</div>

<div class="phase-panel" data-phase="screening">
<div class="phase-header">
<h3>📖 Screening Phase</h3>
<p>Quickly assess paper relevance</p>
</div>
<div class="phase-tools">
<div class="tool-card">
<h4>Reading Management</h4>
<div class="tool-links">
<a href="reading-list.html">📋 Reading List (Inbox Filter)</a>
<a href="compare-papers.html">️ Compare Papers</a>
</div>
</div>
<div class="tool-card">
<h4>Quick Assessment</h4>
<div class="tool-tips">
<div class="tip-item">✓ Read abstracts first</div>
<div class="tip-item">✓ Check topics & authors</div>
<div class="tip-item">✓ Update status to "Reading"</div>
</div>
</div>
</div>
</div>

<div class="phase-panel" data-phase="reading">
<div class="phase-header">
<h3>📚 Deep Reading Phase</h3>
<p>Extract key insights and methodology</p>
</div>
<div class="phase-tools">
<div class="tool-card">
<h4>Notes & Annotations</h4>
<div class="tool-links">
<a href="notes.html">📝 My Notes</a>
<a href="reading-list.html">📋 Reading List (Reading Filter)</a>
</div>
</div>
<div class="tool-card">
<h4>Structured Notes</h4>
<div class="tool-tips">
<div class="tip-item">💡 Key contributions</div>
<div class="tip-item">🔬 Methodology</div>
<div class="tip-item">📊 Results & limitations</div>
<div class="tip-item">❓ Questions & follow-ups</div>
</div>
</div>
</div>
</div>

<div class="phase-panel" data-phase="synthesis">
<div class="phase-header">
<h3>🧠 Synthesis Phase</h3>
<p>Connect ideas across papers</p>
</div>
<div class="phase-tools">
<div class="tool-card">
<h4>Knowledge Building</h4>
<div class="tool-links">
<a href="wiki.html">📖 Wiki</a>
<a href="wiki-graph.html">🕸️ Knowledge Graph</a>
<a href="concept-explorer.html">🗺️ Concept Explorer</a>
</div>
</div>
<div class="tool-card">
<h4>Connections & Patterns</h4>
<div class="tool-links">
<a href="concepts/connections.html">🔗 Concept Connections</a>
<a href="concepts/papers-by-concept.html">📄 Papers by Concept</a>
<a href="concepts/glossary.html">📚 Glossary</a>
</div>
</div>
<div class="tool-card">
<h4>Comparison Tools</h4>
<div class="tool-links">
<a href="compare-papers.html">️ Compare Papers</a>
<a href="statistics.html">📊 Statistics Dashboard</a>
</div>
</div>
</div>

<div class="phase-panel" data-phase="citation">
<div class="phase-header">
<h3>📝 Citation Phase</h3>
<p>Organize references for writing</p>
</div>
<div class="phase-tools">
<div class="tool-card">
<h4>Export & Integration</h4>
<div class="tool-links">
<a href="reading-list.html">📋 Reading List (Export)</a>
</div>
</div>
<div class="tool-card">
<h4>Export Formats</h4>
<div class="tool-tips">
<div class="tip-item">📄 BibTeX → Zotero/Mendeley</div>
<div class="tip-item">📝 Markdown → Obsidian/Notion</div>
<div class="tip-item">📑 LaTeX → Overleaf</div>
</div>
</div>
</div>
</div>
</div>
</div>

<!-- ADMIN SECTION -->
<div class="hub-section admin-section">
<div class="section-header">
<div class="section-icon">🛠️</div>
<h2>Admin Controls</h2>
<p class="section-desc">System settings, automation, and configuration</p>
</div>

<div class="feature-grid">
<div class="feature-card">
<h3>⚙️ Automation Pipeline</h3>
<p>Daily paper updates and site rebuilds</p>
<div class="feature-links">
<a href="admin.html">📋 Admin Overview</a>
<a href="AUTOMATION.html">📖 Automation Guide</a>
<a href="COMPLETE_AUTOMATION_GUIDE.html">📚 Complete Guide</a>
<a href="SHORTCUTS_SETUP.html">⌨️ macOS Shortcuts</a>
</div>
</div>

<div class="feature-card">
<h3>🔧 Configuration</h3>
<p>System settings and preferences</p>
<div class="feature-links">
<a href="settings.html">️ Settings</a>
<a href="requirements.html">📋 User Requirements</a>
</div>
</div>

<div class="feature-card">
<h3>📊 Monitoring</h3>
<p>System health and statistics</p>
<div class="feature-links">
<a href="statistics.html">📊 Statistics Dashboard</a>
</div>
</div>

<div class="feature-card">
<h3>📖 Documentation</h3>
<p>Technical guides and references</p>
<div class="feature-links">
<a href="AGENTS.html">📋 Agent Guide</a>
<a href="DESIGN_GUIDE.html">🎨 Design Guide</a>
<a href="UI_ENHANCEMENTS.html">✨ UI Enhancements</a>
</div>
</div>

<div class="feature-card">
<h3> Server Management</h3>
<p>Web server control</p>
<div class="feature-links">
<a href="start_server.sh">▶️ Start Server</a>
<a href="stop_server.sh">⏹️ Stop Server</a>
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

.external-hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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

/* Activity & Quick Actions Grid */
.activity-actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.activity-feed-card,
.quick-actions-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid #f3f4f6;
}

.card-header h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #1f2937;
}

.activity-count {
  background: #667eea;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}

.activity-feed {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-height: 300px;
  overflow-y: auto;
}

.activity-item {
  display: flex;
  gap: 0.75rem;
  padding: 0.75rem;
  background: #f9fafb;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.activity-item:hover {
  background: #f0f4ff;
  transform: translateX(4px);
}

.activity-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-weight: 600;
  font-size: 0.9rem;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.activity-desc {
  font-size: 0.85rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
}

.activity-time {
  font-size: 0.75rem;
  color: #9ca3af;
}

.view-all-link {
  display: block;
  text-align: center;
  margin-top: 1rem;
  padding-top: 0.75rem;
  border-top: 1px solid #e5e7eb;
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.view-all-link:hover {
  color: #764ba2;
}

.quick-actions-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
}

.quick-action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 2px solid transparent;
}

.quick-action-btn:hover {
  background: #f0f4ff;
  border-color: #667eea;
  transform: translateY(-2px);
}

.action-icon {
  font-size: 1.5rem;
}

.action-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #4b5563;
  text-align: center;
}

@media (max-width: 768px) {
  .activity-actions-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-actions-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Workflow Stepper */
.workflow-stepper {
  background: white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  border: 1px solid #e5e7eb;
  margin-bottom: 30px;
}

.stepper-progress {
  margin-bottom: 32px;
}

.progress-bar {
  height: 6px;
  background: #f3f4f6;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 8px;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  border-radius: 3px;
  transition: width 0.4s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: #9ca3af;
  font-weight: 500;
  letter-spacing: 0.02em;
}

.stepper-steps {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.stepper-step {
  display: flex;
  gap: 24px;
  padding: 20px 0;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

.stepper-step:hover .step-content {
  background: #f8fafc;
}

.step-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
  width: 48px;
}

.step-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #f3f4f6;
  border: 2px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  position: relative;
  z-index: 2;
}

.step-icon {
  font-size: 1.4rem;
}

.stepper-step.active .step-circle {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-color: #667eea;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.35);
}

.stepper-step.completed .step-circle {
  background: #10b981;
  border-color: #10b981;
}

.step-line {
  width: 2px;
  flex: 1;
  background: #e5e7eb;
  margin-top: 8px;
  min-height: 20px;
}

.stepper-step:last-child .step-line {
  display: none;
}

.stepper-step.active .step-line,
.stepper-step.completed .step-line {
  background: linear-gradient(180deg, #667eea 0%, #e5e7eb 100%);
}

.step-content {
  flex: 1;
  padding: 8px 20px;
  border-radius: 12px;
  transition: background 0.2s ease;
}

.step-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 6px;
}

.step-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}

.stepper-step.active .step-header h3 {
  color: #667eea;
}

.step-badge {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 10px;
  border-radius: 100px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.step-badge.upcoming {
  background: #f3f4f6;
  color: #9ca3af;
}

.step-description {
  font-size: 0.9rem;
  color: #6b7280;
  margin: 0 0 10px 0;
  line-height: 1.5;
}

.step-meta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.meta-item {
  font-size: 0.8rem;
  color: #9ca3af;
  font-weight: 500;
}

@media (max-width: 640px) {
  .stepper-step {
    gap: 16px;
  }
  
  .step-circle {
    width: 40px;
    height: 40px;
  }
  
  .step-icon {
    font-size: 1.2rem;
  }
  
  .step-content {
    padding: 8px 12px;
  }
  
  .step-meta {
    flex-direction: column;
    gap: 4px;
  }
}

/* Workflow Dashboard */
.workflow-dashboard {
  background: #f8f9fa;
  padding: 30px;
  border-radius: 12px;
  margin-top: 20px;
}

.workflow-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-bottom: 25px;
}

.stat-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 800;
  color: #667eea;
  margin-bottom: 5px;
}

.stat-tip {
  font-size: 0.8rem;
  color: #999;
}

.workflow-actions {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.workflow-action-btn {
  padding: 15px 30px;
  background: white;
  border: 2px solid #667eea;
  border-radius: 8px;
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.workflow-action-btn:hover {
  background: #667eea;
  color: white;
  transform: translateY(-2px);
}

.workflow-action-btn.primary {
  background: #667eea;
  color: white;
}

.workflow-action-btn.primary:hover {
  background: #5568d3;
}

/* Phase-Based Navigation */
.phase-based-navigation {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.phase-panel {
  background: #f8f9fa;
  border-radius: 12px;
  overflow: hidden;
  border-left: 5px solid #667eea;
}

.phase-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px 25px;
}

.phase-header h3 {
  margin: 0 0 8px 0;
  font-size: 1.3rem;
}

.phase-header p {
  margin: 0;
  opacity: 0.9;
  font-size: 0.95rem;
}

.phase-tools {
  padding: 25px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.tool-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.tool-card h4 {
  margin: 0 0 15px 0;
  color: #2c3e50;
  font-size: 1.1rem;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 10px;
}

.tool-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tool-links a {
  display: block;
  padding: 10px 15px;
  background: #f8f9fa;
  border-radius: 6px;
  text-decoration: none;
  color: #2c3e50;
  font-size: 0.95rem;
  transition: all 0.2s;
  border: 1px solid #e0e0e0;
}

.tool-links a:hover {
  background: #667eea;
  color: white;
  border-color: #667eea;
  transform: translateX(5px);
}

.tool-tips {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tip-item {
  padding: 10px 15px;
  background: #f0f7ff;
  border-radius: 6px;
  color: #2c3e50;
  font-size: 0.9rem;
  border-left: 3px solid #4facfe;
}

/* Feature Grid (Admin) */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 25px;
}

.feature-card {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 12px;
  transition: all 0.3s;
  border-left: 4px solid #f5576c;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.feature-card h3 {
  color: #2c3e50;
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.feature-card p {
  color: #666;
  margin: 0 0 15px 0;
  font-size: 0.95rem;
}

.feature-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.feature-links a {
  display: block;
  padding: 8px 12px;
  background: white;
  border-radius: 6px;
  text-decoration: none;
  color: #2c3e50;
  font-size: 0.9rem;
  transition: all 0.2s;
  border: 1px solid #e0e0e0;
}

.feature-links a:hover {
  background: #f5576c;
  color: white;
  border-color: #f5576c;
  transform: translateX(5px);
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
  background: #667eea;
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
  
  .workflow-steps {
    flex-direction: column;
  }
  
  .workflow-connector {
    transform: rotate(90deg);
    margin: 10px 0;
  }
  
  .feature-grid,
  .phase-tools {
    grid-template-columns: 1fr;
  }
}
</style>

<script>
// Workflow stepper interactivity
document.querySelectorAll('.stepper-step').forEach(step => {
  step.addEventListener('click', () => {
    document.querySelectorAll('.stepper-step').forEach(s => s.classList.remove('active'));
    step.classList.add('active');
    
    const phase = step.dataset.phase;
    document.querySelectorAll('.phase-panel').forEach(panel => {
      panel.style.display = panel.dataset.phase === phase ? 'block' : 'none';
    });
    
    // Update progress bar
    const progress = (phase / 5) * 100;
    document.querySelector('.progress-fill').style.width = progress + '%';
    document.querySelector('.progress-text').textContent =  PH0 ;
  });
});

// Load reading list stats from localStorage
function loadWorkflowStats() {
  const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
  
  const inboxCount = bookmarks.filter(b => b.status === 'Inbox').length;
  const readingCount = bookmarks.filter(b => b.status === 'Reading').length;
  const readCount = bookmarks.filter(b => b.status === 'Read').length;
  const citedCount = bookmarks.filter(b => b.status === 'Cited').length;
  
  document.getElementById('inboxCount').textContent = inboxCount;
  document.getElementById('readingCount').textContent = readingCount;
  document.getElementById('readCount').textContent = readCount;
  document.getElementById('citedCount').textContent = citedCount;
}

// Load recent activity from localStorage
function loadRecentActivity() {
  const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
  const notes = JSON.parse(localStorage.getItem('paperNotes') || '{}');
  const wikiContributions = JSON.parse(localStorage.getItem('wikiContributions') || '[]');
  
  // Combine all activities with timestamps
  const activities = [];
  
  // Add bookmark activities
  bookmarks.forEach(bookmark => {
    if (bookmark.timestamp) {
      activities.push({
        type: 'bookmark',
        icon: '📥',
        title: 'Paper bookmarked',
        desc: bookmark.title || bookmark.id,
        time: bookmark.timestamp,
        status: bookmark.status
      });
    }
    
    // Add status change activities
    if (bookmark.statusTimestamps) {
      Object.entries(bookmark.statusTimestamps).forEach(([status, timestamp]) => {
        if (timestamp && status !== 'Inbox') {
          const statusIcons = {
            'Reading': '📖',
            'Read': '✅',
            'Cited': '📚',
            'Archived': '🗄️'
          };
          const statusTitles = {
            'Reading': 'Started reading',
            'Read': 'Finished reading',
            'Cited': 'Paper cited',
            'Archived': 'Paper archived'
          };
          activities.push({
            type: 'status',
            icon: statusIcons[status] || '📄',
            title: statusTitles[status] ||  PH1 ,
            desc: bookmark.title || bookmark.id,
            time: timestamp
          });
        }
      });
    }
  });
  
  // Add note activities
  Object.entries(notes).forEach(([paperId, noteData]) => {
    if (noteData.timestamp && noteData.content) {
      activities.push({
        type: 'note',
        icon: '📝',
        title: 'Note added',
        desc:  PH2 ,
        time: noteData.timestamp
      });
    }
  });
  
  // Add wiki contribution activities
  wikiContributions.forEach(contribution => {
    if (contribution.timestamp) {
      activities.push({
        type: 'wiki',
        icon: '🔗',
        title: 'Wiki contribution',
        desc:  PH3 ,
        time: contribution.timestamp
      });
    }
  });
  
  // Sort by timestamp (most recent first)
  activities.sort((a, b) => new Date(b.time) - new Date(a.time));
  
  // Take top 5 activities
  const recentActivities = activities.slice(0, 5);
  
  // Update activity count
  const activityCount = document.getElementById('activityCount');
  if (activityCount) {
    activityCount.textContent =  PH4 ;
  }
  
  // Render activities
  const activityFeed = document.getElementById('activityFeed');
  if (activityFeed) {
    if (recentActivities.length === 0) {
      activityFeed.innerHTML = '<div class="activity-item"><div class="activity-icon">📭</div><div class="activity-content"><div class="activity-title">No recent activity</div><div class="activity-desc">Start by bookmarking papers or adding notes</div></div></div>';
    } else {
      activityFeed.innerHTML = recentActivities.map(activity => {
        const timeAgo = getTimeAgo(new Date(activity.time));
        return  PH5 ;
      }).join('');
    }
  }
}

// Helper function to format time ago
function getTimeAgo(date) {
  const seconds = Math.floor((new Date() - date) / 1000);
  
  if (seconds < 60) return 'just now';
  if (seconds < 3600) return  PH6 ;
  if (seconds < 86400) return  PH7 ;
  if (seconds < 604800) return  PH8 ;
  if (seconds < 2592000) return  PH9 ;
  return date.toLocaleDateString();
}

// Initialize
loadWorkflowStats();
loadRecentActivity();
</script>

</div>
