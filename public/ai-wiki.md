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
<button class="tab-btn" onclick="switchTab('learn')">🎯 Learn by Building</button>
<button class="tab-btn" onclick="switchTab('graph')">🕸️ Concept Graph</button>
<button class="tab-btn" onclick="switchTab('timeline')">📅 Timeline</button>
<button class="tab-btn" onclick="switchTab('stats')">📊 Statistics</button>
</div>

<!-- Learn by Building Tab -->
<div id="learnTab" class="tab-content">
<div class="learn-header">
<h3>🎯 Learn by Building</h3>
<p>Construct your understanding by building explanations from scratch</p>
</div>

<div class="learn-mode-selector">
<div class="mode-card" onclick="startLearningMode('build')">
<div class="mode-icon">🏗️</div>
<h4>Build Understanding</h4>
<p>Create your own explanation guided by structured prompts</p>
</div>
<div class="mode-card" onclick="startLearningMode('teach')">
<div class="mode-icon">👨‍🏫</div>
<h4>Teaching Mode</h4>
<p>Explain concepts as if teaching someone else</p>
</div>
<div class="mode-card" onclick="startLearningMode('compare')">
<div class="mode-icon">⚖️</div>
<h4>Compare & Reflect</h4>
<p>Compare your understanding to expert explanations</p>
</div>
</div>

<div id="learningWorkspace" class="learning-workspace" style="display: none;">
<div class="learning-header">
<h3 id="learningTitle">Building Understanding</h3>
<div class="mastery-indicator">
<span class="mastery-level">🌱 Learning</span>
<button onclick="updateMastery()" class="btn-mastery">Update Progress</button>
</div>
</div>

<div class="concept-selector">
<label>Select a concept to work on:</label>
<select id="learningConceptSelect" onchange="loadConceptForLearning()">
<option value="">-- Choose a concept --</option>
</select>
</div>

<div id="learningTemplate" class="learning-template" style="display: none;">
<div class="template-section">
<h4>📝 Your Explanation</h4>
<textarea id="userExplanation" class="learning-textarea" placeholder="Explain this concept in your own words..."></textarea>
</div>

<div class="template-section">
<h4>🔑 Key Ideas</h4>
<textarea id="keyIdeas" class="learning-textarea-small" placeholder="What are the 3-5 most important points?"></textarea>
</div>

<div class="template-section">
<h4>💡 Examples & Applications</h4>
<textarea id="examples" class="learning-textarea-small" placeholder="Give concrete examples or real-world applications..."></textarea>
</div>

<div class="template-section">
<h4>🔗 Connections</h4>
<textarea id="connections" class="learning-textarea-small" placeholder="How does this relate to other concepts you've learned?"></textarea>
</div>

<div class="template-section">
<h4>❓ Questions & Uncertainties</h4>
<textarea id="questions" class="learning-textarea-small" placeholder="What still confuses you? What would you like to explore further?"></textarea>
</div>

<div class="learning-actions">
<button onclick="saveLearningProgress()" class="btn-save">💾 Save Progress</button>
<button onclick="getAIFeedback()" class="btn-ai">🤖 Get AI Feedback</button>
<button onclick="viewExpertExplanation()" class="btn-compare">📚 View Expert Explanation</button>
</div>

<div id="aiFeedback" class="ai-feedback" style="display: none;"></div>
<div id="expertExplanation" class="expert-explanation" style="display: none;"></div>
</div>
</div>
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

<!-- AI Companion Panel (Right Sidebar) -->
<aside class="ai-companion-panel" id="aiCompanionPanel" style="display: none;">
<h3>🤖 AI Companion</h3>
<div class="companion-modes">
<button class="companion-mode-btn active" onclick="switchAIMode('construct')">Construct</button>
<button class="companion-mode-btn" onclick="switchAIMode('reflect')">Reflect</button>
<button class="companion-mode-btn" onclick="switchAIMode('scaffold')">Scaffold</button>
<button class="companion-mode-btn" onclick="switchAIMode('consolidate')">Consolidate</button>
</div>
<div class="companion-content" id="companionContent">
<div class="companion-intro">
<p>Select a concept to work with:</p>
<ul>
<li><strong>Construct:</strong> Write your initial explanation</li>
<li><strong>Reflect:</strong> Get metacognitive questions</li>
<li><strong>Scaffold:</strong> Receive gap detection & hints</li>
<li><strong>Consolidate:</strong> Practice recall</li>
</ul>
</div>
</div>
</aside>
</div>

<style>
/* Import shared AI Companion styles */
@import url('/css/ai-companion.css');

/* Page-specific styles only (no AI Companion duplication) */
/* Learn by Building Styles */
.learn-header {
  text-align: center;
  margin-bottom: 30px;
}

.learn-header h3 {
  color: #2c3e50;
  font-size: 24px;
  margin-bottom: 10px;
}

.learn-header p {
  color: #7f8c8d;
  font-size: 16px;
}

.learn-mode-selector {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.mode-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  padding: 25px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
}

.mode-card:hover {
  border-color: #3498db;
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(52, 152, 219, 0.15);
}

.mode-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.mode-card h4 {
  color: #2c3e50;
  margin: 0 0 10px 0;
  font-size: 18px;
}

.mode-card p {
  color: #7f8c8d;
  margin: 0;
  font-size: 14px;
  line-height: 1.5;
}

.learning-workspace {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.learning-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e0e0e0;
}

.learning-header h3 {
  margin: 0;
  color: #2c3e50;
}

.mastery-indicator {
  display: flex;
  align-items: center;
  gap: 15px;
}

.mastery-level {
  font-size: 16px;
  font-weight: 600;
  color: #27ae60;
}

.btn-mastery {
  padding: 8px 16px;
  background: #f39c12;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.btn-mastery:hover {
  background: #e67e22;
}

.concept-selector {
  margin-bottom: 25px;
}

.concept-selector label {
  display: block;
  margin-bottom: 10px;
  font-weight: 600;
  color: #2c3e50;
}

.concept-selector select {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 15px;
  cursor: pointer;
}

.learning-template {
  margin-top: 20px;
}

.template-section {
  margin-bottom: 25px;
}

.template-section h4 {
  color: #2c3e50;
  margin: 0 0 12px 0;
  font-size: 16px;
}

.learning-textarea {
  width: 100%;
  min-height: 150px;
  padding: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 15px;
  font-family: inherit;
  resize: vertical;
  line-height: 1.6;
}

.learning-textarea-small {
  width: 100%;
  min-height: 100px;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
  resize: vertical;
  line-height: 1.5;
}

.learning-textarea:focus,
.learning-textarea-small:focus {
  outline: none;
  border-color: #3498db;
}

.learning-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 2px solid #e0e0e0;
}

.btn-save,
.btn-ai,
.btn-compare {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-save {
  background: #27ae60;
  color: white;
}

.btn-save:hover {
  background: #229954;
}

.btn-ai {
  background: #9b59b6;
  color: white;
}

.btn-ai:hover {
  background: #8e44ad;
}

.btn-compare {
  background: #3498db;
  color: white;
}

.btn-compare:hover {
  background: #2980b9;
}

.ai-feedback,
.expert-explanation {
  margin-top: 25px;
  padding: 20px;
  border-radius: 8px;
  line-height: 1.6;
}

.ai-feedback {
  background: #f3e5f5;
  border-left: 4px solid #9b59b6;
}

.expert-explanation {
  background: #e3f2fd;
  border-left: 4px solid #3498db;
}

.ai-feedback h4,
.expert-explanation h4 {
  margin: 0 0 15px 0;
  color: #2c3e50;
}

.ai-feedback p,
.expert-explanation p {
  margin: 0;
  color: #34495e;
}

/* Existing styles continue... */
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

/* Concept Editing Styles */
.concept-actions {
  display: flex;
  gap: 10px;
}

.btn-edit, .btn-ai {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.btn-edit {
  background: #e3f2fd;
  color: #1976d2;
}

.btn-edit:hover {
  background: #bbdefb;
}

.btn-ai {
  background: #fff3e0;
  color: #f57c00;
}

.btn-ai:hover {
  background: #ffe0b2;
}

.user-edited-badge {
  background: #e8f5e9;
  color: #2e7d32;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

/* Phase 3: User Contributions Styles */
.btn-contribute {
  background: #4caf50;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-contribute:hover {
  background: #45a049;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
}

.contributions-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.contribution-item {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  transition: all 0.2s;
}

.contribution-item:hover {
  border-color: #2c5aa0;
  box-shadow: 0 2px 8px rgba(44, 90, 160, 0.1);
}

.contribution-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.contribution-meta {
  display: flex;
  gap: 12px;
  align-items: center;
}

.contribution-type-badge {
  background: #2c5aa0;
  color: white;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  text-transform: capitalize;
}

.contribution-date {
  color: #7f8c8d;
  font-size: 13px;
}

.contribution-actions {
  display: flex;
  gap: 8px;
}

.btn-upvote {
  background: #e8f5e9;
  color: #2e7d32;
  border: 1px solid #4caf50;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-upvote:hover {
  background: #c8e6c9;
  transform: translateY(-1px);
}

.btn-delete {
  background: #ffebee;
  color: #c62828;
  border: 1px solid #ef5350;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-delete:hover {
  background: #ffcdd2;
  transform: translateY(-1px);
}

.contribution-content {
  color: #2c3e50;
  line-height: 1.6;
  margin-bottom: 12px;
  white-space: pre-wrap;
}

.contribution-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tag {
  background: #e3f2fd;
  color: #1976d2;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.no-contributions {
  text-align: center;
  color: #7f8c8d;
  font-style: italic;
  padding: 20px;
}

/* Contribution Form Styles */
.contribution-form {
  background: #fff3e0;
  border: 2px solid #ff9800;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 16px;
}

.contribution-form h4 {
  margin: 0 0 16px 0;
  color: #f57c00;
  font-size: 18px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  color: #2c3e50;
  font-weight: 600;
  font-size: 14px;
}

.form-group select,
.form-group textarea,
.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  font-family: inherit;
  transition: border-color 0.2s;
}

.form-group select:focus,
.form-group textarea:focus,
.form-group input:focus {
  outline: none;
  border-color: #2c5aa0;
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.btn-save {
  background: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-save:hover {
  background: #45a049;
}

.btn-cancel {
  background: #e0e0e0;
  color: #333;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cancel:hover {
  background: #d0d0d0;
}

.concept-editor {
  margin-top: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
  background: #f8f9fa;
}

.concept-textarea {
  width: 100%;
  min-height: 200px;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-family: inherit;
  font-size: 14px;
  line-height: 1.6;
  resize: vertical;
  margin-bottom: 15px;
}

.concept-textarea:focus {
  outline: none;
  border-color: #2c5aa0;
}

.editor-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.ai-enhance-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.btn-ai-small {
  padding: 6px 12px;
  background: #fff3e0;
  color: #f57c00;
  border: 1px solid #ff9800;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.btn-ai-small:hover {
  background: #ffe0b2;
  transform: translateY(-1px);
}

.btn-ai-small:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.editor-save-actions {
  display: flex;
  gap: 8px;
}

.btn-save {
  padding: 8px 16px;
  background: #2c5aa0;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}

.btn-save:hover {
  background: #1e4a8f;
}

.btn-cancel {
  padding: 8px 16px;
  background: #e0e0e0;
  color: #333;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}

.btn-cancel:hover {
  background: #d0d0d0;
}

.ai-loading {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid #f57c00;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 0.8s linear infinite;
  margin-right: 6px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
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

// Learn by Building Functions
let currentLearningMode = null;
let currentLearningConcept = null;

function switchTab(tabName) {
  // Hide all tabs
  document.querySelectorAll('.tab-content').forEach(tab => {
    tab.classList.remove('active');
  });
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  
  // Show selected tab
  document.getElementById(tabName + 'Tab').classList.add('active');
  event.target.classList.add('active');
  
  // Initialize learn tab if needed
  if (tabName === 'learn') {
    initializeLearnTab();
  }
}

function initializeLearnTab() {
  const select = document.getElementById('learningConceptSelect');
  if (select.options.length <= 1) {
    // Populate concept selector
    Object.keys(concepts).sort().forEach(conceptName => {
      const option = document.createElement('option');
      option.value = conceptName;
      option.textContent = conceptName;
      select.appendChild(option);
    });
  }
}

function startLearningMode(mode) {
  currentLearningMode = mode;
  document.getElementById('learningWorkspace').style.display = 'block';
  
  const titles = {
    'build': 'Building Understanding',
    'teach': 'Teaching Mode - Explain to Others',
    'compare': 'Compare & Reflect'
  };
  
  document.getElementById('learningTitle').textContent = titles[mode];
  
  // Scroll to workspace
  document.getElementById('learningWorkspace').scrollIntoView({ behavior: 'smooth' });
}

function loadConceptForLearning() {
  const select = document.getElementById('learningConceptSelect');
  const conceptName = select.value;
  
  if (!conceptName) {
    document.getElementById('learningTemplate').style.display = 'none';
    return;
  }
  
  currentLearningConcept = conceptName;
  document.getElementById('learningTemplate').style.display = 'block';
  
  // Load saved progress if exists
  const savedProgress = getLearningProgress(conceptName);
  if (savedProgress) {
    document.getElementById('userExplanation').value = savedProgress.explanation || '';
    document.getElementById('keyIdeas').value = savedProgress.keyIdeas || '';
    document.getElementById('examples').value = savedProgress.examples || '';
    document.getElementById('connections').value = savedProgress.connections || '';
    document.getElementById('questions').value = savedProgress.questions || '';
    
    // Update mastery indicator
    updateMasteryDisplay(savedProgress.mastery || 'learning');
  } else {
    // Clear fields
    document.getElementById('userExplanation').value = '';
    document.getElementById('keyIdeas').value = '';
    document.getElementById('examples').value = '';
    document.getElementById('connections').value = '';
    document.getElementById('questions').value = '';
    updateMasteryDisplay('learning');
  }
  
  // Hide feedback panels
  document.getElementById('aiFeedback').style.display = 'none';
  document.getElementById('expertExplanation').style.display = 'none';
}

function getLearningProgress(conceptName) {
  const progress = JSON.parse(localStorage.getItem('learningProgress') || '{}');
  return progress[conceptName] || null;
}

function saveLearningProgress() {
  if (!currentLearningConcept) {
    alert('Please select a concept first');
    return;
  }
  
  const progress = {
    concept: currentLearningConcept,
    explanation: document.getElementById('userExplanation').value,
    keyIdeas: document.getElementById('keyIdeas').value,
    examples: document.getElementById('examples').value,
    connections: document.getElementById('connections').value,
    questions: document.getElementById('questions').value,
    mastery: getCurrentMasteryLevel(),
    lastUpdated: new Date().toISOString()
  };
  
  const allProgress = JSON.parse(localStorage.getItem('learningProgress') || '{}');
  allProgress[currentLearningConcept] = progress;
  localStorage.setItem('learningProgress', JSON.stringify(allProgress));
  
  alert('Progress saved successfully!');
  updateMasteryDisplay(progress.mastery);
}

function getCurrentMasteryLevel() {
  const masteryEl = document.querySelector('.mastery-level');
  if (masteryEl.textContent.includes('🌱')) return 'learning';
  if (masteryEl.textContent.includes('🌿')) return 'developing';
  if (masteryEl.textContent.includes('🌳')) return 'mastered';
  return 'learning';
}

function updateMasteryDisplay(level) {
  const masteryEl = document.querySelector('.mastery-level');
  const levels = {
    'learning': '🌱 Learning',
    'developing': '🌿 Developing',
    'mastered': '🌳 Mastered'
  };
  masteryEl.textContent = levels[level] || levels['learning'];
}

function updateMastery() {
  if (!currentLearningConcept) {
    alert('Please select a concept first');
    return;
  }
  
  const currentLevel = getCurrentMasteryLevel();
  const levels = ['learning', 'developing', 'mastered'];
  const currentIndex = levels.indexOf(currentLevel);
  const nextIndex = (currentIndex + 1) % levels.length;
  const nextLevel = levels[nextIndex];
  
  updateMasteryDisplay(nextLevel);
  
  // Save to progress
  const progress = getLearningProgress(currentLearningConcept) || {};
  progress.mastery = nextLevel;
  progress.lastUpdated = new Date().toISOString();
  
  const allProgress = JSON.parse(localStorage.getItem('learningProgress') || '{}');
  allProgress[currentLearningConcept] = progress;
  localStorage.setItem('learningProgress', JSON.stringify(allProgress));
}

function getAIFeedback() {
  if (!currentLearningConcept) {
    alert('Please select a concept first');
    return;
  }
  
  const explanation = document.getElementById('userExplanation').value;
  if (!explanation.trim()) {
    alert('Please write your explanation first');
    return;
  }
  
  // Simulate AI feedback (in production, this would call an AI API)
  const feedback = generateAIFeedback(explanation, currentLearningConcept);
  
  const feedbackEl = document.getElementById('aiFeedback');
  feedbackEl.innerHTML = `
<h4>🤖 AI Feedback</h4>
<p>${feedback}</p>
  `;
  feedbackEl.style.display = 'block';
  feedbackEl.scrollIntoView({ behavior: 'smooth' });
}

function generateAIFeedback(explanation, conceptName) {
  const wordCount = explanation.split(/\s+/).length;
  const concept = concepts[conceptName];
  
  let feedback = '<strong>Analysis of your explanation:</strong><br><br>';
  
  // Word count feedback
  if (wordCount < 50) {
    feedback += '⚠️ Your explanation is quite brief. Try expanding on the key concepts and providing more detail.<br><br>';
  } else if (wordCount > 300) {
    feedback += '✅ Good depth! Your explanation is comprehensive.<br><br>';
  } else {
    feedback += '✅ Good length for an explanation.<br><br>';
  }
  
  // Check for key terms from the concept
  const definition = concept.definition.toLowerCase();
  const keyTerms = definition.split(/\s+/).filter(word => word.length > 5);
  const explanationLower = explanation.toLowerCase();
  const matchedTerms = keyTerms.filter(term => explanationLower.includes(term));
  
  if (matchedTerms.length > 0) {
    feedback += `✅ You've included important terms: ${matchedTerms.slice(0, 5).join(', ')}<br><br>`;
  } else {
    feedback += '💡 Consider incorporating key terminology from the concept definition.<br><br>';
  }
  
  // Check for examples
  if (explanationLower.includes('example') || explanationLower.includes('for instance') || explanationLower.includes('such as')) {
    feedback += '✅ Great! You\'ve included examples to illustrate the concept.<br><br>';
  } else {
    feedback += '💡 Adding concrete examples would strengthen your explanation.<br><br>';
  }
  
  // Suggestions
  feedback += '<strong>Suggestions for improvement:</strong><br>';
  feedback += '• Consider explaining why this concept matters<br>';
  feedback += '• Connect it to related concepts you\'ve learned<br>';
  feedback += '• Think about real-world applications';
  
  return feedback;
}

function viewExpertExplanation() {
  if (!currentLearningConcept) {
    alert('Please select a concept first');
    return;
  }
  
  const concept = concepts[currentLearningConcept];
  const expertEl = document.getElementById('expertExplanation');
  
  expertEl.innerHTML = `
<h4>📚 Expert Explanation</h4>
<p><strong>Definition:</strong> ${concept.definition}</p>
<p style="margin-top: 15px;"><strong>Key Points:</strong></p>
<ul style="margin-left: 20px; line-height: 1.8;">
<li>Category: ${concept.category}</li>
<li>Difficulty: ${concept.difficulty}</li>
<li>Related to ${concept.related.length} other concepts</li>
<li>Appears in ${concept.papers.length} research papers</li>
</ul>
<p style="margin-top: 15px;"><strong>Tags:</strong> ${concept.tags.join(', ')}</p>
  `;
  
  expertEl.style.display = 'block';
  expertEl.scrollIntoView({ behavior: 'smooth' });
}

// Wiki Functions
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
  
  // Check if user has custom content
  const userContent = getUserConceptContent(conceptName);
  const displayDefinition = userContent || concept.definition;
  
  detail.innerHTML = `
<div class="concept-detail-header">
<h2 class="concept-detail-title">${concept.name}</h2>
<div class="concept-detail-meta">
<span class="concept-category">${concept.category}</span>
<span class="concept-difficulty difficulty-${concept.difficulty}">${concept.difficulty}</span>
<span>📄 ${concept.papers.length} papers</span>
        ${userContent ? '<span class="user-edited-badge">✏️ User Enhanced</span>' : ''}
</div>
</div>
    
<div class="concept-detail-section">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
<h3 style="margin: 0;">Definition</h3>
<div class="concept-actions">
<button onclick="editConcept('${conceptName}')" class="btn-edit" title="Edit this concept">
            ✏️ Edit
</button>
<button onclick="askAIEnhance('${conceptName}')" class="btn-ai" title="Ask AI to enhance">
            🤖 Ask AI
</button>
</div>
</div>
<div id="conceptDefinition" class="concept-detail-definition">
        ${displayDefinition}
</div>
<div id="conceptEditor" class="concept-editor" style="display: none;">
<textarea id="conceptEditorText" class="concept-textarea">${displayDefinition}</textarea>
<div class="editor-actions">
<div class="ai-enhance-buttons">
<button onclick="aiEnhance('expand')" class="btn-ai-small" title="Add more details">
              📖 Expand
</button>
<button onclick="aiEnhance('simplify')" class="btn-ai-small" title="Make it simpler">
              💡 Simplify
</button>
<button onclick="aiEnhance('examples')" class="btn-ai-small" title="Add examples">
              🔍 Add Examples
</button>
<button onclick="aiEnhance('technical')" class="btn-ai-small" title="Add technical depth">
              ⚙️ Technical
</button>
</div>
<div class="editor-save-actions">
<button onclick="saveConceptEdit('${conceptName}')" class="btn-save">
              💾 Save
</button>
<button onclick="cancelEdit('${conceptName}')" class="btn-cancel">
              ❌ Cancel
</button>
</div>
</div>
</div>
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

<div class="concept-detail-section">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
<h3 style="margin: 0;">Community Contributions</h3>
<button onclick="showContributionForm('${conceptName}')" class="btn-contribute">
          ➕ Add Contribution
</button>
</div>
<div id="contributionsList" class="contributions-list">
        ${renderContributions(conceptName)}
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

// Get user's custom concept content from localStorage
function getUserConceptContent(conceptName) {
  const userConcepts = JSON.parse(localStorage.getItem('userConcepts') || '{}');
  return userConcepts[conceptName] || null;
}

// Save user's custom concept content to localStorage
function saveUserConceptContent(conceptName, content) {
  const userConcepts = JSON.parse(localStorage.getItem('userConcepts') || '{}');
  userConcepts[conceptName] = content;
  localStorage.setItem('userConcepts', JSON.stringify(userConcepts));
}

// Open concept editor
function editConcept(conceptName) {
  document.getElementById('conceptDefinition').style.display = 'none';
  document.getElementById('conceptEditor').style.display = 'block';
  
  // Focus the textarea
  setTimeout(() => {
    document.getElementById('conceptEditorText').focus();
  }, 100);
}

// Cancel editing
function cancelEdit(conceptName) {
  document.getElementById('conceptDefinition').style.display = 'block';
  document.getElementById('conceptEditor').style.display = 'none';
  
  // Reset textarea to saved content
  const userContent = getUserConceptContent(conceptName);
  const concept = concepts[conceptName];
  const displayContent = userContent || concept.definition;
  document.getElementById('conceptEditorText').value = displayContent;
}

// Save concept edit
function saveConceptEdit(conceptName) {
  const newContent = document.getElementById('conceptEditorText').value.trim();
  
  if (!newContent) {
    alert('Content cannot be empty');
    return;
  }
  
  // Save to localStorage
  saveUserConceptContent(conceptName, newContent);
  
  // Update display
  document.getElementById('conceptDefinition').innerHTML = newContent;
  document.getElementById('conceptDefinition').style.display = 'block';
  document.getElementById('conceptEditor').style.display = 'none';
  
  // Show success message
  showNotification('✓ Concept saved successfully', 'success');
  
  // Refresh the concept detail to show the badge
  showConceptDetail(conceptName);
}

// Phase 3: User Contributions System
function renderContributions(conceptName) {
  const contributions = getContributions(conceptName);
  
  if (contributions.length === 0) {
    return '<p class="no-contributions">No contributions yet. Be the first to share your insights!</p>';
  }
  
  return contributions.map((contrib, index) => `
<div class="contribution-item" data-id="${contrib.id}">
<div class="contribution-header">
<div class="contribution-meta">
<span class="contribution-type-badge">${contrib.type}</span>
<span class="contribution-date">${new Date(contrib.timestamp).toLocaleDateString()}</span>
</div>
<div class="contribution-actions">
<button onclick="upvoteContribution('${conceptName}', ${contrib.id})" class="btn-upvote" title="Upvote">
            👍 ${contrib.upvotes || 0}
</button>
<button onclick="deleteContribution('${conceptName}', ${contrib.id})" class="btn-delete" title="Delete">
            🗑️
</button>
</div>
</div>
<div class="contribution-content">
        ${contrib.content}
</div>
      ${contrib.tags && contrib.tags.length > 0 ? `
<div class="contribution-tags">
          ${contrib.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
</div>
      ` : ''}
</div>
  `).join('');
}

function getContributions(conceptName) {
  const key = `wiki_contributions_${conceptName}`;
  return JSON.parse(localStorage.getItem(key) || '[]');
}

function saveContributions(conceptName, contributions) {
  const key = `wiki_contributions_${conceptName}`;
  localStorage.setItem(key, JSON.stringify(contributions));
}

function showContributionForm(conceptName) {
  const formHtml = `
<div class="contribution-form">
<h4>Add Your Contribution</h4>
<div class="form-group">
<label>Type:</label>
<select id="contributionType">
<option value="explanation">💡 Explanation</option>
<option value="example">📝 Example</option>
<option value="insight">🔍 Insight</option>
<option value="question">❓ Question</option>
</select>
</div>
<div class="form-group">
<label>Content:</label>
<textarea id="contributionContent" rows="6" placeholder="Share your knowledge, example, or insight..."></textarea>
</div>
<div class="form-group">
<label>Tags (comma-separated, optional):</label>
<input type="text" id="contributionTags" placeholder="e.g., practical, advanced, beginner-friendly">
</div>
<div class="form-actions">
<button onclick="saveContribution('${conceptName}')" class="btn-save">💾 Save Contribution</button>
<button onclick="cancelContributionForm()" class="btn-cancel">❌ Cancel</button>
</div>
</div>
  `;
  
  const contributionsList = document.getElementById('contributionsList');
  contributionsList.insertAdjacentHTML('afterbegin', formHtml);
  
  // Hide the add button
  const addBtn = contributionsList.parentElement.querySelector('.btn-contribute');
  if (addBtn) addBtn.style.display = 'none';
}

function cancelContributionForm() {
  const form = document.querySelector('.contribution-form');
  if (form) form.remove();
  
  // Show the add button again
  const addBtn = document.querySelector('.btn-contribute');
  if (addBtn) addBtn.style.display = 'block';
}

function saveContribution(conceptName) {
  const type = document.getElementById('contributionType').value;
  const content = document.getElementById('contributionContent').value.trim();
  const tagsInput = document.getElementById('contributionTags').value.trim();
  
  if (!content) {
    alert('Please enter some content');
    return;
  }
  
  const tags = tagsInput ? tagsInput.split(',').map(t => t.trim()).filter(t => t) : [];
  
  const contribution = {
    id: Date.now(),
    type: type,
    content: content,
    tags: tags,
    timestamp: new Date().toISOString(),
    upvotes: 0
  };
  
  const contributions = getContributions(conceptName);
  contributions.unshift(contribution); // Add to beginning
  saveContributions(conceptName, contributions);
  
  // Refresh the contributions list
  document.getElementById('contributionsList').innerHTML = renderContributions(conceptName);
  
  showNotification('✓ Contribution added successfully!', 'success');
}

function deleteContribution(conceptName, contributionId) {
  if (!confirm('Are you sure you want to delete this contribution?')) {
    return;
  }
  
  let contributions = getContributions(conceptName);
  contributions = contributions.filter(c => c.id !== contributionId);
  saveContributions(conceptName, contributions);
  
  // Refresh the contributions list
  document.getElementById('contributionsList').innerHTML = renderContributions(conceptName);
  
  showNotification('✓ Contribution deleted', 'success');
}

function upvoteContribution(conceptName, contributionId) {
  const contributions = getContributions(conceptName);
  const contribution = contributions.find(c => c.id === contributionId);
  
  if (contribution) {
    contribution.upvotes = (contribution.upvotes || 0) + 1;
    saveContributions(conceptName, contributions);
    
    // Refresh the contributions list
    document.getElementById('contributionsList').innerHTML = renderContributions(conceptName);
    
    showNotification('✓ Upvoted!', 'success');
  }
}

// Ask AI to enhance the concept
function askAIEnhance(conceptName) {
  const concept = concepts[conceptName];
  const currentContent = getUserConceptContent(conceptName) || concept.definition;
  
  // Open editor with current content
  editConcept(conceptName);
  
  // Show AI enhancement options
  const editorText = document.getElementById('conceptEditorText');
  editorText.value = currentContent;
  
  // Auto-focus on AI buttons
  setTimeout(() => {
    document.querySelector('.btn-ai-small').focus();
  }, 100);
  
  showNotification('🤖 Choose an AI enhancement option below', 'info');
}

// AI enhancement function with different modes
async function aiEnhance(mode) {
  const editorText = document.getElementById('conceptEditorText');
  const currentContent = editorText.value;
  const buttons = document.querySelectorAll('.btn-ai-small');
  
  // Disable all AI buttons during processing
  buttons.forEach(btn => btn.disabled = true);
  
  // Show loading state
  const originalText = event.target.textContent;
  event.target.innerHTML = '<span class="ai-loading"></span>Processing...';
  
  try {
    let enhancedContent = '';
    
    // Simulate AI enhancement (in production, this would call an AI API)
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    switch(mode) {
      case 'expand':
        enhancedContent = await expandContent(currentContent);
        break;
      case 'simplify':
        enhancedContent = await simplifyContent(currentContent);
        break;
      case 'examples':
        enhancedContent = await addExamples(currentContent);
        break;
      case 'technical':
        enhancedContent = await addTechnicalDepth(currentContent);
        break;
    }
    
    editorText.value = enhancedContent;
    showNotification('✓ Content enhanced successfully', 'success');
    
  } catch (error) {
    console.error('AI enhancement failed:', error);
    showNotification('❌ AI enhancement failed. Please try again.', 'error');
  } finally {
    // Re-enable buttons and restore text
    buttons.forEach(btn => {
      btn.disabled = false;
      btn.textContent = btn.getAttribute('title');
    });
  }
}

// AI enhancement: Expand content with more details
async function expandContent(content) {
  // In production, this would call an AI API
  // For now, simulate expansion
  const expansions = {
    'AI Agent': `\n\n**Key Characteristics:**\n- **Autonomy**: Operates independently without constant human intervention\n- **Goal-directed**: Pursues specific objectives through planned actions\n- **Adaptive**: Learns from experience and adjusts behavior\n- **Interactive**: Communicates with other agents and humans\n\n**Applications:**\n- Autonomous vehicles\n- Personal assistants\n- Robotic process automation\n- Multi-agent systems`,
    
    'Retrieval-Augmented Generation': `\n\n**How RAG Works:**\n1. **Query Processing**: User question is converted to embeddings\n2. **Retrieval**: Similar documents are fetched from knowledge base\n3. **Augmentation**: Retrieved context is added to prompt\n4. **Generation**: LLM generates answer using both knowledge and context\n\n**Benefits:**\n- Reduces hallucination by grounding responses in facts\n- Provides citations and sources\n- Keeps knowledge up-to-date without retraining\n- Improves accuracy on domain-specific questions`,
    
    'Chain-of-Thought': `\n\n**Implementation Approaches:**\n- **Zero-shot CoT**: Simply add "Let's think step by step"\n- **Few-shot CoT**: Provide examples of step-by-step reasoning\n- **Self-Consistency**: Generate multiple reasoning paths and vote\n- **Tree of Thoughts**: Explore multiple reasoning branches\n\n**When to Use:**\n- Mathematical problem solving\n- Logical reasoning tasks\n- Multi-step planning\n- Complex decision making`
  };
  
  // Find matching concept or add generic expansion
  for (const [concept, expansion] of Object.entries(expansions)) {
    if (content.toLowerCase().includes(concept.toLowerCase())) {
      return content + expansion;
    }
  }
  
  // Generic expansion
  return content + `\n\n**Additional Context:**\nThis concept plays an important role in modern AI systems. Understanding its principles helps researchers and practitioners design more effective solutions. The key insights involve balancing complexity with practicality, ensuring that theoretical advances translate into real-world applications.`;
}

// AI enhancement: Simplify content
async function simplifyContent(content) {
  // In production, this would call an AI API
  // For now, simulate simplification by extracting key points
  const sentences = content.split(/[.!?]+/).filter(s => s.trim().length > 0);
  
  if (sentences.length <= 2) {
    return content;
  }
  
  // Keep first sentence and summarize the rest
  const simplified = sentences[0] + '. In simple terms, this concept helps AI systems work more effectively by providing structured approaches to complex problems.';
  
  return simplified;
}

// AI enhancement: Add examples
async function addExamples(content) {
  // In production, this would call an AI API
  const examples = {
    'AI Agent': `\n\n**Real-World Examples:**\n- 🤖 **ChatGPT**: Conversational AI agent that helps users with tasks\n- 🚗 **Tesla Autopilot**: Autonomous driving agent\n- 🏠 **Roomba**: Robot vacuum that navigates and cleans autonomously\n- 💼 **GitHub Copilot**: AI coding assistant that suggests code`,
    
    'Retrieval-Augmented Generation': `\n\n**Examples in Practice:**\n- 📚 **Enterprise Search**: Company knowledge base with AI-powered Q&A\n- 🏥 **Medical Diagnosis**: AI assistant that retrieves medical literature\n- ⚖️ **Legal Research**: AI that finds relevant case law and statutes\n- 🎓 **Educational Tutor**: AI tutor with access to textbooks and papers`,
    
    'Chain-of-Thought': `\n\n**Example Problem:**\n**Question**: If a train travels 60 mph for 2 hours, then 80 mph for 3 hours, what's the average speed?\n\n**Chain-of-Thought Reasoning:**\n1. Calculate distance for first segment: 60 mph × 2 hours = 120 miles\n2. Calculate distance for second segment: 80 mph × 3 hours = 240 miles\n3. Total distance: 120 + 240 = 360 miles\n4. Total time: 2 + 3 = 5 hours\n5. Average speed: 360 miles ÷ 5 hours = 72 mph\n\n**Answer**: 72 mph`
  };
  
  // Find matching concept or add generic examples
  for (const [concept, example] of Object.entries(examples)) {
    if (content.toLowerCase().includes(concept.toLowerCase())) {
      return content + example;
    }
  }
  
  // Generic examples
  return content + `\n\n**Examples:**\n- Example 1: Basic application of this concept in a simple scenario\n- Example 2: More complex use case showing advanced features\n- Example 3: Real-world implementation in production systems`;
}

// AI enhancement: Add technical depth
async function addTechnicalDepth(content) {
  // In production, this would call an AI API
  const technical = {
    'AI Agent': `\n\n**Technical Architecture:**\n\`\`\`\nAgent = (Perception, Reasoning, Action, Learning)\n\`\`\`\n\n**Formal Definition:**\nAn agent is a function mapping percept sequences to actions:\n\\( f: P^* \\rightarrow A \\)\n\n**Key Algorithms:**\n- Reinforcement Learning (Q-learning, Policy Gradient)\n- Planning (A*, MCTS, STRIPS)\n- Multi-agent coordination (Game Theory, Mechanism Design)`,
    
    'Retrieval-Augmented Generation': `\n\n**Mathematical Formulation:**\nGiven query \\( q \\), retrieve top-k documents:\n\\( D_k = \\text{argmax}_{d \\in D} \\text{sim}(\\text{enc}(q), \\text{enc}(d)) \\)\n\n**Retrieval Methods:**\n- Dense retrieval: Bi-encoders with dot-product similarity\n- Sparse retrieval: BM25, TF-IDF\n- Hybrid: Combine dense and sparse methods\n\n**Generation with Context:**\n\\( P(y|x, D_k) = \\text{LM}(y | x \\oplus \\text{concat}(D_k)) \\)`,
    
    'Chain-of-Thought': `\n\n**Prompt Template:**\n\`\`\`\nQ: [question]\nA: Let's think step by step.\n[step 1]\n[step 2]\n...\nTherefore, the answer is [answer].\n\`\`\`\n\n**Self-Consistency Algorithm:**\n1. Sample \\( N \\) reasoning paths: \\( \\{r_1, r_2, ..., r_N\\} \\)\n2. Extract answers: \\( \\{a_1, a_2, ..., a_N\\} \\)\n3. Majority vote: \\( a^* = \\text{mode}(\\{a_i\\}) \\)\n\n**Complexity:**\n- Time: \\( O(N \\cdot L) \\) where \\( L \\) is reasoning length\n- Space: \\( O(N \\cdot L) \\) for storing paths`
  };
  
  // Find matching concept or add generic technical content
  for (const [concept, tech] of Object.entries(technical)) {
    if (content.toLowerCase().includes(concept.toLowerCase())) {
      return content + tech;
    }
  }
  
  // Generic technical depth
  return content + `\n\n**Technical Details:**\n- **Algorithm**: The underlying algorithm operates in \\( O(n \\log n) \\) time complexity\n- **Optimization**: Gradient-based methods are used for parameter tuning\n- **Implementation**: Typically implemented using PyTorch or TensorFlow frameworks`;
}

// Show notification
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 12px 20px;
    background: ${type === 'success' ? '#4caf50' : type === 'error' ? '#f44336' : '#2196f3'};
    color: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    z-index: 10000;
    font-size: 14px;
    font-weight: 600;
    animation: slideIn 0.3s ease-out;
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease-out';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// Add animation styles
if (!document.getElementById('notification-styles')) {
  const style = document.createElement('style');
  style.id = 'notification-styles';
  style.textContent = `
    @keyframes slideIn {
      from { transform: translateX(400px); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
      from { transform: translateX(0); opacity: 1; }
      to { transform: translateX(400px); opacity: 0; }
    }
  `;
  document.head.appendChild(style);
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
});
</script>
<script src="js/stage-navigation.js"></script>
