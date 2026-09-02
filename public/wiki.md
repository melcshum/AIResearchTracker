---
title: "Research Wiki"
---

<div class="wiki-container">
<div class="wiki-header">
<h2>📖 Research Wiki</h2>
<p class="wiki-subtitle">Interactive knowledge building with real paper references and persistent contributions</p>
</div>

<div class="wiki-learning-hero">
<div class="hero-content">
<div class="hero-text">
<h3>🎯 Start Your Learning Journey</h3>
<p>Build deep understanding by explaining concepts in your own words. Click any highlighted term below to begin.</p>
<div class="hero-actions">
<a href="#" class="btn-start-learning" id="startLearningBtn">Start Learning →</a>
<a href="learning-journey.html" class="btn-view-journey">View Learning Path</a>
</div>
</div>
<div class="hero-progress">
<div class="progress-stat">
<div class="stat-icon">📖</div>
<div class="stat-value" id="wikiTermsExplored">0</div>
<div class="stat-label">Terms Explored</div>
</div>
<div class="progress-stat">
<div class="stat-icon">✍️</div>
<div class="stat-value" id="wikiExplanationsWritten">0</div>
<div class="stat-label">Explanations</div>
</div>
<div class="progress-stat">
<div class="stat-icon">🌳</div>
<div class="stat-value" id="wikiMastered">0</div>
<div class="stat-label">Mastered</div>
</div>
</div>
</div>
<div class="hero-ai-companion">
<h4>🤖 AI Learning Companion</h4>
<div class="companion-features">
<div class="companion-feature">
<div class="feature-icon">✍️</div>
<div class="feature-text">
<strong>Write Mode:</strong> AI observes as you construct knowledge
</div>
</div>
<div class="companion-feature">
<div class="feature-icon">🤔</div>
<div class="feature-text">
<strong>Reflect Mode:</strong> Metacognitive prompts guide self-assessment
</div>
</div>
<div class="companion-feature">
<div class="feature-icon">🏗️</div>
<div class="feature-text">
<strong>Scaffold Mode:</strong> Targeted hints without giving answers
</div>
</div>
<div class="companion-feature">
<div class="feature-icon">💬</div>
<div class="feature-text">
<strong>Chat Mode:</strong> Ask questions and get personalized guidance</div>
</div>
</div>
</div>
<div class="hero-last-activity" id="lastActivitySection" style="display: none;">
<h4>📍 Continue Where You Left Off</h4>
<div class="last-activity-content">
<span id="lastActivityText"></span>
<a href="#" id="continueLearningBtn" class="btn-continue">Continue Learning →</a>
</div>
</div>
</div>

<div class="wiki-search-bar">
<input type="text" id="wikiSearch" placeholder="🔍 Search wiki entries, terms, and concepts..." onkeyup="searchWiki()">
<div id="searchResults" class="wiki-search-results"></div>
</div>

<div class="wiki-workflow-guide">
<div class="workflow-step">
<div class="step-icon">✍️</div>
<div class="step-content">
<h4>1. Construct</h4>
<p>Write your initial explanation in your own words. AI observes but doesn't intervene yet, preserving your epistemic agency.</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">🤔</div>
<div class="step-content">
<h4>2. Reflect</h4>
<p>AI generates metacognitive prompts: "Which part are you least confident about?" You examine your understanding before correction.</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">🏗️</div>
<div class="step-content">
<h4>3. Scaffold</h4>
<p>AI provides targeted questions, hints, and connection suggestions. It identifies gaps without rewriting. Prompt Before Provide.</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">💡</div>
<div class="step-content">
<h4>4. Consolidate (Optional)</h4>
<p>Retrieve and apply knowledge independently. Explain without consulting the wiki, then compare to your original explanation.</p>
</div>
</div>
<div class="workflow-step">
<div class="step-icon">🔗</div>
<div class="step-content">
<h4>5. Revisit & Extend</h4>
<p>New concepts integrate with prior knowledge. AI identifies related entries and prompts comparison, integration, or revision.</p>
</div>
</div>
</div>

<div class="wiki-content-area">
<div class="wiki-article">
<h3>AI Agent Systems</h3>
<p>
An AI agent is an autonomous system that can 
<span class="wiki-term" data-term="perception">perceive its environment</span>, 
<span class="wiki-term" data-term="reasoning">reason about actions</span>, and 
<span class="wiki-term" data-term="action">act to achieve goals</span>. Modern AI agents often use 
<span class="wiki-term" data-term="llm">large language models</span> as their reasoning core, combined with 
<span class="wiki-term" data-term="tool-use">tool use capabilities</span> and 
<span class="wiki-term" data-term="planning">planning algorithms</span>.
</p>
<p>
Key components include <span class="wiki-term" data-term="memory">memory systems</span> for maintaining context, 
<span class="wiki-term" data-term="retrieval">retrieval mechanisms</span> for accessing knowledge, and 
<span class="wiki-term" data-term="multi-agent">multi-agent coordination</span> for complex tasks.
</p>

<h3>Retrieval-Augmented Generation</h3>
<p>
<span class="wiki-term" data-term="rag">RAG</span> combines <span class="wiki-term" data-term="retrieval">retrieval</span> with generation by first searching a knowledge base for relevant documents, then using those documents as context for the language model. This approach reduces hallucination and provides verifiable citations.
</p>
<p>
Advanced RAG systems use <span class="wiki-term" data-term="dense-retrieval">dense retrieval</span> with <span class="wiki-term" data-term="embeddings">vector embeddings</span>, <span class="wiki-term" data-term="hybrid-search">hybrid search</span> combining lexical and semantic methods, and <span class="wiki-term" data-term="reranking">reranking</span> to improve result quality.
</p>

<h3>Reasoning & Planning</h3>
<p>
<span class="wiki-term" data-term="reasoning">Reasoning</span> in AI agents involves <span class="wiki-term" data-term="chain-of-thought">chain-of-thought</span> processing, where the model breaks down complex problems into intermediate steps. <span class="wiki-term" data-term="planning">Planning</span> extends this by generating sequences of actions to achieve long-term goals.
</p>
<p>
Modern approaches use <span class="wiki-term" data-term="tree-of-thought">tree-of-thought</span> exploration, where multiple reasoning paths are evaluated in parallel. <span class="wiki-term" data-term="self-consistency">Self-consistency</span> techniques sample multiple solutions and select the most coherent one through voting or verification.
</p>

<h3>Tool Use & Function Calling</h3>
<p>
<span class="wiki-term" data-term="tool-use">Tool use</span> enables agents to interact with external systems through <span class="wiki-term" data-term="function-calling">function calling</span> interfaces. Agents learn to invoke APIs, execute code, query databases, and manipulate files to accomplish tasks beyond text generation.
</p>
<p>
Effective tool use requires <span class="wiki-term" data-term="grounding">grounding</span> — understanding when and how to apply tools appropriately. Agents must reason about tool capabilities, handle errors gracefully, and compose multiple tools into workflows.
</p>

<h3>Multi-Agent Systems</h3>
<p>
<span class="wiki-term" data-term="multi-agent">Multi-agent</span> systems coordinate multiple AI agents to solve complex problems. Agents can specialize in different roles (researcher, critic, executor) and communicate through structured protocols.
</p>
<p>
Coordination strategies include <span class="wiki-term" data-term="debate">debate</span> (agents argue different perspectives), <span class="wiki-term" data-term="consensus">consensus</span> (agents converge on shared understanding), and <span class="wiki-term" data-term="hierarchy">hierarchical</span> structures (manager agents delegate to workers).
</p>

<h3>Safety & Alignment</h3>
<p>
<span class="wiki-term" data-term="safety">Safety</span> in AI systems involves ensuring agents behave reliably and avoid harmful outcomes. <span class="wiki-term" data-term="alignment">Alignment</span> ensures AI systems pursue intended goals and respect human values.
</p>
<p>
Key techniques include <span class="wiki-term" data-term="rlhf">RLHF</span> (Reinforcement Learning from Human Feedback), <span class="wiki-term" data-term="constitutional-ai">Constitutional AI</span> (self-improvement guided by principles), and <span class="wiki-term" data-term="guardrails">guardrails</span> (constraints on agent behavior).
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

<div id="aiCompanionPanel" class="wiki-panel ai-companion">
<h4>🤖 AI Learning Companion</h4>
<p class="companion-intro">Follows the 5-stage knowledge construction cycle. AI scaffolds rather than substitutes.</p>
<div class="ai-companion-modes">
<button class="ai-mode-btn active" onclick="switchAIMode('construct')" title="Write your explanation">✍️ Construct</button>
<button class="ai-mode-btn" onclick="switchAIMode('reflect')" title="Examine your understanding">🤔 Reflect</button>
<button class="ai-mode-btn" onclick="switchAIMode('scaffold')" title="Get targeted support">🏗️ Scaffold</button>
<button class="ai-mode-btn" onclick="switchAIMode('consolidate')" title="Retrieve from memory">💡 Consolidate</button>
<button class="ai-mode-btn" onclick="switchAIMode('revisit')" title="Connect to prior knowledge">🔗 Revisit</button>
</div>

<div id="aiConstructMode" class="ai-mode-content active">
<div class="ai-prompt">
<p class="ai-hint">✍️ Write your initial explanation. I'll observe but won't intervene yet — your understanding comes first.</p>
<button class="ai-action-btn" onclick="aiStartDraft()">📝 Start Draft</button>
<button class="ai-action-btn" onclick="aiSuggestStructure()">🏗️ Suggest Structure</button>
</div>
<div id="aiWritingAssist" class="ai-assist-area"></div>
</div>

<div id="aiReflectMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🤔 Let's examine your understanding. I'll ask questions to help you reflect — no corrections yet.</p>
<button class="ai-action-btn" onclick="aiGenerateReflectionPrompts()">💭 Generate Reflection Questions</button>
<button class="ai-action-btn" onclick="aiConfidenceCheck()">📊 Confidence Check</button>
</div>
<div id="aiReflectResult" class="ai-assist-area"></div>
</div>

<div id="aiScaffoldMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🏗️ I'll provide targeted support based on your explanation. I'll ask before telling — Prompt Before Provide.</p>
<button class="ai-action-btn" onclick="aiDetectGaps()">🕳️ Identify Gaps</button>
<button class="ai-action-btn" onclick="aiChallengeMisconceptions()">❓ Challenge Assumptions</button>
<button class="ai-action-btn" onclick="aiSuggestConnections()">🔗 Suggest Connections (on request)</button>
</div>
<div id="aiScaffoldResult" class="ai-assist-area"></div>
</div>

<div id="aiConsolidateMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">💡 Optional: Test your retrieval. Explain without consulting the wiki, then compare.</p>
<button class="ai-action-btn" onclick="aiStartRetrieval()">🧠 Start Retrieval Practice</button>
<button class="ai-action-btn" onclick="aiCompareExplanations()">⚖️ Compare Explanations</button>
</div>
<div id="aiConsolidateResult" class="ai-assist-area"></div>
</div>

<div id="aiRevisitMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🔗 Connect new learning to prior knowledge. I'll show related entries and prompt revision.</p>
<button class="ai-action-btn" onclick="aiShowRelatedEntries()">📚 Show Related Entries</button>
<button class="ai-action-btn" onclick="aiPromptRevision()">🔄 Prompt Revision</button>
<button class="ai-action-btn" onclick="aiShowVersionHistory()">📜 Version History</button>
</div>
<div id="aiRevisitResult" class="ai-assist-area"></div>
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
/* Import shared AI Companion styles */
@import url('/css/ai-companion.css');

/* Page-specific styles only (no AI Companion duplication) */
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
// Import shared AI Companion
import('/js/ai-companion.js').then(() => {
  // Initialize page-specific AI Companion
  const aiCompanion = new AICompanion({
    apiBase: 'http://localhost:5001/api/wiki',
    currentPage: 'wiki',
    onModeChange: (mode) => {
      console.log('Mode changed to:', mode);
    },
    onFeedbackReceived: (data) => {
      console.log('Feedback received:', data);
    },
    onError: (error) => {
      console.error('AI Companion error:', error);
    }
  });
  
  // Initialize after DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    aiCompanion.init('.companion-mode-container', '.companion-content');
    initWikiLearningHero();
  });
});

// Wiki Learning Hero functionality
function initWikiLearningHero() {
  const contributions = JSON.parse(localStorage.getItem('wikiContributions') || '[]');
  
  // Calculate stats
  const terms = new Set(contributions.map(c => c.termId));
  const explanations = contributions.filter(c => c.type === 'explanation');
  const mastered = contributions.filter(c => c.type === 'explanation' && c.content && c.content.length > 200).length;
  
  // Update progress stats
  document.getElementById('wikiTermsExplored').textContent = terms.size;
  document.getElementById('wikiExplanationsWritten').textContent = explanations.length;
  document.getElementById('wikiMastered').textContent = mastered;
  
  // Show last activity if exists
  if (contributions.length > 0) {
    const lastContribution = contributions[contributions.length - 1];
    const lastActivitySection = document.getElementById('lastActivitySection');
    const lastActivityText = document.getElementById('lastActivityText');
    
    if (lastActivitySection && lastActivityText) {
      const termName = lastContribution.termName || 'a term';
      const timeAgo = getTimeAgo(lastContribution.timestamp);
      lastActivityText.textContent = `You last explored "${termName}" ${timeAgo}`;
      lastActivitySection.style.display = 'block';
      
      // Set continue button to scroll to the term
      document.getElementById('continueLearningBtn').onclick = (e) => {
        e.preventDefault();
        const termElement = document.querySelector(`[data-term="${lastContribution.termId}"]`);
        if (termElement) {
          termElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
          termElement.style.animation = 'pulse 2s';
        }
      };
    }
  }
  
  // Start learning button - scroll to first unexplored term or first term
  document.getElementById('startLearningBtn').onclick = (e) => {
    e.preventDefault();
    const exploredTermIds = new Set(contributions.map(c => c.termId));
    const allTerms = document.querySelectorAll('.wiki-term');
    
    let targetTerm = null;
    for (let term of allTerms) {
      const termId = term.getAttribute('data-term');
      if (!exploredTermIds.has(termId)) {
        targetTerm = term;
        break;
      }
    }
    
    if (!targetTerm && allTerms.length > 0) {
      targetTerm = allTerms[0];
    }
    
    if (targetTerm) {
      targetTerm.scrollIntoView({ behavior: 'smooth', block: 'center' });
      targetTerm.click();
    }
  };
}

function getTimeAgo(timestamp) {
  const now = new Date();
  const then = new Date(timestamp);
  const diffMs = now - then;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);
  
  if (diffMins < 1) return 'just now';
  if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
  return then.toLocaleDateString();
}

</script>

<style>
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
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
  },
  'chain-of-thought': {
    name: 'Chain-of-Thought',
    definition: 'Breaking down complex reasoning into intermediate steps',
    relatedTerms: ['reasoning', 'planning'],
    keywords: ['chain', 'thought', 'reasoning', 'steps']
  },
  'tree-of-thought': {
    name: 'Tree-of-Thought',
    definition: 'Exploring multiple reasoning paths in parallel',
    relatedTerms: ['reasoning', 'chain-of-thought'],
    keywords: ['tree', 'thought', 'parallel', 'exploration']
  },
  'self-consistency': {
    name: 'Self-Consistency',
    definition: 'Sampling multiple solutions and selecting the most coherent through voting',
    relatedTerms: ['reasoning', 'chain-of-thought'],
    keywords: ['consistency', 'voting', 'sampling', 'verification']
  },
  'function-calling': {
    name: 'Function Calling',
    definition: 'Structured interfaces for invoking external APIs and tools',
    relatedTerms: ['tool-use', 'act'],
    keywords: ['function', 'api', 'invoke', 'interface']
  },
  'grounding': {
    name: 'Grounding',
    definition: 'Understanding when and how to apply tools appropriately',
    relatedTerms: ['tool-use', 'reasoning'],
    keywords: ['grounding', 'context', 'appropriateness', 'application']
  },
  'debate': {
    name: 'Multi-Agent Debate',
    definition: 'Agents argue different perspectives to reach better conclusions',
    relatedTerms: ['multi-agent', 'reasoning'],
    keywords: ['debate', 'argument', 'perspective', 'discussion']
  },
  'consensus': {
    name: 'Consensus',
    definition: 'Agents converge on shared understanding through collaboration',
    relatedTerms: ['multi-agent', 'debate'],
    keywords: ['consensus', 'agreement', 'convergence', 'collaboration']
  },
  'hierarchy': {
    name: 'Hierarchical Coordination',
    definition: 'Manager agents delegate tasks to worker agents',
    relatedTerms: ['multi-agent', 'planning'],
    keywords: ['hierarchy', 'delegation', 'manager', 'worker']
  },
  'safety': {
    name: 'AI Safety',
    definition: 'Ensuring AI systems behave reliably and avoid harmful outcomes',
    relatedTerms: ['alignment', 'guardrails'],
    keywords: ['safety', 'reliability', 'harm', 'robustness']
  },
  'alignment': {
    name: 'AI Alignment',
    definition: 'Ensuring AI systems pursue intended goals and respect human values',
    relatedTerms: ['safety', 'rlhf'],
    keywords: ['alignment', 'values', 'goals', 'human']
  },
  'rlhf': {
    name: 'RLHF',
    definition: 'Reinforcement Learning from Human Feedback - training models using human preferences',
    relatedTerms: ['alignment', 'constitutional-ai'],
    keywords: ['rlhf', 'feedback', 'reinforcement', 'preference']
  },
  'constitutional-ai': {
    name: 'Constitutional AI',
    definition: 'Self-improvement guided by a set of principles or constitution',
    relatedTerms: ['alignment', 'safety'],
    keywords: ['constitutional', 'principles', 'self-improvement', 'constitution']
  },
  'guardrails': {
    name: 'Guardrails',
    definition: 'Constraints on agent behavior to prevent harmful actions',
    relatedTerms: ['safety', 'alignment'],
    keywords: ['guardrails', 'constraints', 'limits', 'boundaries']
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

// AI Companion Functions
function switchAIMode(mode) {
  // Update button states
  document.querySelectorAll('.ai-mode-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  
  // Update content visibility
  document.querySelectorAll('.ai-mode-content').forEach(content => content.classList.remove('active'));
  document.getElementById('ai' + mode.charAt(0).toUpperCase() + mode.slice(1) + 'Mode').classList.add('active');
}

function aiStartDraft() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiWritingAssist');
  area.innerHTML = `
<div class="ai-message">
<strong>✍️ Construct mode: Write your initial explanation</strong>
<p>Start by writing what you currently understand about "${currentTerm.name}". I'll observe but won't intervene yet — your understanding comes first.</p>
<div class="ai-suggestion">
<strong>Consider including:</strong><br>
• Your current definition of the concept<br>
• Key components or mechanisms<br>
• How it works or what it does<br>
• An example from your experience<br>
• Connections to related concepts
</div>
<p>Write your explanation in the text area, then move to <strong>Reflect</strong> mode to examine your understanding.</p>
</div>
  `;
}

function aiSuggestStructure() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiWritingAssist');
  const relatedPapers = paperDatabase.filter(p => 
    p.keywords.some(k => currentTerm.keywords.includes(k))
  ).slice(0, 3);
  
  area.innerHTML = `
<div class="ai-message">
<strong>🏗️ Suggested Structure for ${currentTerm.name}</strong>
<p>Based on ${currentTerm.papers?.length || relatedPapers.length} related papers, here's an effective structure:</p>
<div class="ai-suggestion">
<strong>Opening Hook:</strong> Why does this concept matter?<br>
<strong>Core Definition:</strong> ${currentTerm.definition}<br>
<strong>Technical Details:</strong> How is it implemented?<br>
<strong>Real-World Applications:</strong> Where is it used?<br>
<strong>Challenges:</strong> What are the limitations?<br>
<strong>Future Directions:</strong> Where is this heading?
</div>
${relatedPapers.length > 0 ? `
<p><strong>Key papers to reference:</strong></p>
<ul>
${relatedPapers.map(p => `<li>${p.title} (${p.date})</li>`).join('')}
</ul>
` : ''}
</div>
  `;
}

function aiProvideHints() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiWritingAssist');
  const relatedConcepts = currentTerm.relatedTerms.map(id => wikiTerms[id]?.name).filter(Boolean);
  
  area.innerHTML = `
<div class="ai-message">
<strong>💡 Hints for explaining ${currentTerm.name}</strong>
<p>Consider these angles:</p>
<div class="ai-suggestion">
<strong>Analogy:</strong> Think of it like... (create a relatable comparison)<br>
<strong>Contrast:</strong> How is it different from similar concepts?<br>
<strong>History:</strong> When and why was this developed?<br>
<strong>Impact:</strong> What problem does it solve?
</div>
<p><strong>Related concepts to mention:</strong> ${relatedConcepts.join(', ')}</p>
<p><strong>Key terms to include:</strong> ${currentTerm.keywords.slice(0, 5).join(', ')}</p>
</div>
  `;
}

// REFLECT MODE - Metacognitive prompts (using LLM API)
function aiGenerateReflectionPrompts() {
  const textarea = document.getElementById('explanationInput');
  if (!textarea || !textarea.value.trim()) {
    alert('Please write an explanation first in the "Add Explanation" panel');
    return;
  }
  
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const explanation = textarea.value;
  const concept = currentTerm.name;
  const area = document.getElementById('aiReflectResult');
  
  area.innerHTML = '<div class="ai-message"><strong>🤔 Generating reflection prompts...</strong><br><em>Calling local LLM (this may take a moment)</em></div>';
  
  fetch('http://localhost:5001/api/wiki/companion', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      mode: 'reflect',
      explanation: explanation,
      concept: concept
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      area.innerHTML = `<div class="ai-error"><strong>Error:</strong> ${data.error}</div>`;
      return;
    }
    
    let html = '<div class="ai-message"><strong>🤔 Metacognitive Reflection Prompts</strong><p>Based on your explanation, consider these questions:</p><ul>';
    
    if (Array.isArray(data)) {
      data.forEach(q => {
        html += `<li><strong>${q}</strong></li>`;
      });
    } else if (data.questions) {
      data.questions.forEach(q => {
        html += `<li><strong>${q}</strong></li>`;
      });
    } else {
      // Fallback: show whatever structure we got
      Object.keys(data).forEach(key => {
        if (Array.isArray(data[key])) {
          data[key].forEach(item => {
            html += `<li><strong>${item}</strong></li>`;
          });
        }
      });
    }
    
    html += '</ul><p>Take a moment to think about these questions. When you\'re ready, move to <strong>Scaffold</strong> mode for targeted support.</p></div>';
    area.innerHTML = html;
  })
  .catch(error => {
    area.innerHTML = `<div class="ai-error"><strong>Error:</strong> ${error.message}. Make sure the API server is running on port 5001.</div>`;
  });
}

function aiConfidenceCheck() {
  const textarea = document.getElementById('explanationInput');
  if (!textarea || !textarea.value.trim()) {
    alert('Please write an explanation first');
    return;
  }
  
  const area = document.getElementById('aiReflectResult');
  
  area.innerHTML = `
<div class="ai-message">
<strong>📊 Confidence Check</strong>
<p>Rate your confidence in different aspects of your explanation:</p>
<div class="ai-suggestion">
<strong>Definition accuracy:</strong> [1-5] ___<br>
<strong>Mechanism explanation:</strong> [1-5] ___<br>
<strong>Example quality:</strong> [1-5] ___<br>
<strong>Connections to other concepts:</strong> [1-5] ___<br>
<strong>Overall understanding:</strong> [1-5] ___
</div>
<p>Areas with lower scores are good candidates for further exploration in <strong>Scaffold</strong> mode.</p>
</div>
  `;
}

// SCAFFOLD MODE - Targeted support with Prompt Before Provide (using LLM API)
function aiDetectGaps() {
  const textarea = document.getElementById('explanationInput');
  if (!textarea || !textarea.value.trim()) {
    alert('Please write an explanation first');
    return;
  }
  
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const explanation = textarea.value;
  const concept = currentTerm.name;
  const area = document.getElementById('aiScaffoldResult');
  
  area.innerHTML = '<div class="ai-message"><strong>🕳️ Identifying gaps...</strong><br><em>Calling local LLM (this may take a moment)</em></div>';
  
  fetch('http://localhost:5001/api/wiki/companion', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      mode: 'scaffold',
      explanation: explanation,
      concept: concept,
      action: 'detect_gaps'
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      area.innerHTML = `<div class="ai-error"><strong>Error:</strong> ${data.error}</div>`;
      return;
    }
    
    let html = '<div class="ai-message"><strong>🕳️ Identify Gaps</strong>';
    
    if (data.missingTerms && data.missingTerms.length > 0) {
      html += `<div class="ai-warning">Your explanation doesn't mention these key terms: ${data.missingTerms.slice(0, 3).join(', ')}</div>`;
      html += `<div class="ai-suggestion"><strong>Question:</strong> How do these terms relate to ${concept}?</div>`;
    } else {
      html += '<div class="ai-success">✓ You\'ve covered the key terminology</div>';
    }
    
    if (data.suggestions && data.suggestions.length > 0) {
      html += '<div class="ai-suggestion"><strong>Consider:</strong></div><ul>';
      data.suggestions.forEach(s => {
        html += `<li>${s}</li>`;
      });
      html += '</ul>';
    }
    
    html += `<p><strong>Prompt Before Provide:</strong> Think about these gaps before I provide explanations. What do you think is missing?</p>`;
    html += '</div>';
    
    area.innerHTML = html;
  })
  .catch(error => {
    area.innerHTML = `<div class="ai-error"><strong>Error:</strong> ${error.message}. Make sure the API server is running on port 5001.</div>`;
  });
}

function aiChallengeMisconceptions() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiScaffoldResult');
  
  area.innerHTML = `
<div class="ai-message">
<strong>❓ Challenge Assumptions</strong>
<p>Common misconceptions about ${currentTerm.name}:</p>
<div class="ai-suggestion">
<strong>Question 1:</strong> Does ${currentTerm.name} always work the same way in all contexts?<br>
<strong>Question 2:</strong> What are the limitations or edge cases?<br>
<strong>Question 3:</strong> How is this different from similar concepts?
</div>
<p><strong>Your turn:</strong> Review your explanation. Do any of these questions reveal potential misconceptions? Revise if needed.</p>
</div>
  `;
}

function aiSuggestConnections() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiScaffoldResult');
  const relatedNames = currentTerm.relatedTerms.slice(0, 5).map(id => wikiTerms[id]?.name).filter(Boolean);
  
  area.innerHTML = `
<div class="ai-message">
<strong>🔗 Suggest Connections (on request)</strong>
<p>Related concepts you might connect to:</p>
<div class="ai-suggestion">
${relatedNames.map(name => `• ${name}`).join('<br>')}
</div>
<p><strong>Ask yourself:</strong> How do these concepts relate? Can you add these connections to your explanation?</p>
</div>
  `;
}

// CONSOLIDATE MODE - Retrieval practice (optional)
function aiStartRetrieval() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiConsolidateResult');
  
  area.innerHTML = `
<div class="ai-message">
<strong>🧠 Retrieval Practice</strong>
<p><strong>Instructions:</strong></p>
<div class="ai-suggestion">
1. Close or hide the wiki article<br>
2. Write your explanation of ${currentTerm.name} from memory<br>
3. Don't look at your previous explanation or the wiki<br>
4. When done, click "Compare Explanations" to see how your retrieval compares
</div>
<p>This tests your actual understanding, not just your ability to copy information.</p>
<button class="ai-action-btn" onclick="aiShowRetrievalPrompt()">📝 Show Retrieval Prompt</button>
</div>
  `;
}

function aiShowRetrievalPrompt() {
  const area = document.getElementById('aiConsolidateResult');
  
  area.innerHTML = `
<div class="ai-message">
<strong>📝 Write from Memory</strong>
<p>Explain ${currentTerm.name} without looking at any references:</p>
<textarea id="retrievalTextarea" style="width: 100%; min-height: 150px; margin-top: 10px;" placeholder="Write your explanation from memory..."></textarea>
<button class="ai-action-btn" onclick="aiCompareExplanations()" style="margin-top: 10px;">⚖️ Compare with Original</button>
</div>
  `;
}

function aiCompareExplanations() {
  const retrievalTextarea = document.getElementById('retrievalTextarea');
  const originalTextarea = document.getElementById('explanationInput');
  
  if (!retrievalTextarea || !retrievalTextarea.value.trim()) {
    alert('Please write your retrieval explanation first');
    return;
  }
  
  if (!originalTextarea || !originalTextarea.value.trim()) {
    alert('No original explanation found. Please write one first in the "Add Explanation" panel.');
    return;
  }
  
  const original = originalTextarea.value;
  const retrieval = retrievalTextarea.value;
  const area = document.getElementById('aiConsolidateResult');
  
  // Simple comparison: word overlap
  const originalWords = new Set(original.toLowerCase().split(/\s+/));
  const retrievalWords = retrieval.toLowerCase().split(/\s+/);
  const overlap = retrievalWords.filter(w => originalWords.has(w)).length;
  const coverage = Math.round((overlap / retrievalWords.length) * 100);
  
  area.innerHTML = `
<div class="ai-message">
<strong>⚖️ Comparison Results</strong>
<p><strong>Word overlap:</strong> ${coverage}% of your retrieval matches your original explanation</p>
<div class="ai-suggestion">
<strong>What this means:</strong><br>
• High overlap (80%+): Strong retention of key concepts<br>
• Medium overlap (50-80%): Good understanding, some details lost<br>
• Low overlap (<50%): Consider reviewing the concept again
</div>
<p><strong>Reflection:</strong> What did you remember well? What did you forget? This reveals what you truly understand vs. what you were just copying.</p>
</div>
  `;
}

// REVISIT MODE - Connect to prior knowledge and version history
function aiShowRelatedEntries() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiRevisitResult');
  
  // Find user's previous contributions on related terms
  const relatedContributions = wikiContributions.filter(c => 
    currentTerm.relatedTerms.includes(c.termId)
  );
  
  let feedback = '<div class="ai-message"><strong>📚 Related Entries from Your Wiki</strong>';
  
  if (relatedContributions.length > 0) {
    feedback += '<p>You\'ve written about these related concepts:</p>';
    const grouped = {};
    relatedContributions.forEach(c => {
      if (!grouped[c.term]) grouped[c.term] = [];
      grouped[c.term].push(c);
    });
    
    Object.entries(grouped).slice(0, 5).forEach(([term, contribs]) => {
      feedback += `<div class="ai-suggestion"><strong>${term}:</strong> ${contribs.length} contribution(s)<br>`;
      feedback += `<em>${contribs[0].content.substring(0, 80)}...</em></div>`;
    });
    
    feedback += `<p><strong>Question:</strong> Does learning about ${currentTerm.name} change how you understand these related concepts?</p>`;
  } else {
    feedback += `<p>You haven't written about related concepts yet. Consider exploring: ${currentTerm.relatedTerms.slice(0, 3).map(id => wikiTerms[id]?.name).filter(Boolean).join(', ')}</p>`;
  }
  
  feedback += '</div>';
  area.innerHTML = feedback;
}

function aiPromptRevision() {
  const versions = termVersions[currentTerm.id] || [];
  const area = document.getElementById('aiRevisitResult');
  
  if (versions.length === 0) {
    area.innerHTML = `
<div class="ai-message">
<strong>🔄 Prompt Revision</strong>
<p>No previous versions found. Write your first explanation, then revise it as your understanding deepens.</p>
</div>
    `;
    return;
  }
  
  const latestVersion = versions[versions.length - 1];
  
  area.innerHTML = `
<div class="ai-message">
<strong>🔄 Revise Your Understanding</strong>
<p><strong>Latest version:</strong> ${new Date(latestVersion.timestamp).toLocaleDateString()}</p>
<div class="ai-suggestion">
<strong>Consider revising:</strong><br>
• Add new insights from recent papers<br>
• Clarify confusing parts<br>
• Add examples or applications<br>
• Connect to newly learned concepts<br>
• Correct any misconceptions you've discovered
</div>
<p>Each revision deepens your understanding. Your current version has ${latestVersion.content.split(/\s+/).length} words.</p>
</div>
  `;
}

function aiShowVersionHistory() {
  const versions = termVersions[currentTerm.id] || [];
  const area = document.getElementById('aiRevisitResult');
  
  if (versions.length === 0) {
    area.innerHTML = `
<div class="ai-message">
<strong>📜 Version History</strong>
<p>No versions yet. Start writing explanations to track how your understanding evolves!</p>
</div>
    `;
    return;
  }
  
  let feedback = '<div class="ai-message"><strong>📜 Your Understanding Evolution</strong>';
  feedback += `<p>${versions.length} version(s) for ${currentTerm.name}:</p>`;
  
  versions.forEach((v, i) => {
    const wordCount = v.content.split(/\s+/).length;
    const date = new Date(v.timestamp).toLocaleDateString();
    feedback += `<div class="ai-suggestion"><strong>v${i + 1}</strong> (${date}) — ${wordCount} words<br>`;
    feedback += `<em>${v.content.substring(0, 100)}...</em></div>`;
  });
  
  if (versions.length > 1) {
    const first = versions[0].content.split(/\s+/).length;
    const latest = versions[versions.length - 1].content.split(/\s+/).length;
    const growth = latest - first;
    feedback += `<p><strong>Growth:</strong> ${growth > 0 ? '+' : ''}${growth} words from v1 to v${versions.length}</p>`;
  }
  
  feedback += '</div>';
  area.innerHTML = feedback;
}

function aiAssessMastery() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiCoachingResult');
  const contributions = wikiContributions.filter(c => c.termId === currentTerm.id);
  const hasExplanation = contributions.some(c => c.type === 'explanation');
  const hasQuestions = contributions.some(c => c.type === 'question');
  
  let masteryLevel = '🌱 Learning';
  let masteryColor = '#ffc107';
  let suggestions = [];
  
  if (hasExplanation && hasQuestions) {
    masteryLevel = '🌳 Mastered';
    masteryColor = '#28a745';
    suggestions.push('✓ You\'ve written explanations and asked questions');
    suggestions.push('💡 Try teaching this concept to someone else');
    suggestions.push('💡 Explore advanced related topics');
  } else if (hasExplanation) {
    masteryLevel = '🌿 Developing';
    masteryColor = '#17a2b8';
    suggestions.push('✓ You\'ve written an explanation');
    suggestions.push('💡 Ask questions about unclear aspects');
    suggestions.push('💡 Review related papers for deeper understanding');
  } else {
    suggestions.push('💡 Start by writing your own explanation');
    suggestions.push('💡 Ask questions about what confuses you');
    suggestions.push('💡 Review the definition and related papers');
  }
  
  area.innerHTML = `
<div class="ai-message">
<strong>📈 Mastery Assessment for ${currentTerm.name}</strong>
<div class="ai-success" style="background: ${masteryColor}; color: white; font-size: 16px; font-weight: bold; text-align: center;">
${masteryLevel}
</div>
<p><strong>Progress:</strong></p>
<ul>
${suggestions.map(s => `<li>${s}</li>`).join('')}
</ul>
</div>
  `;
}

function aiSuggestNext() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiCoachingResult');
  const relatedTerms = currentTerm.relatedTerms.map(id => wikiTerms[id]).filter(Boolean);
  const unexplored = relatedTerms.filter(t => 
    !wikiContributions.some(c => c.termId === Object.keys(wikiTerms).find(k => wikiTerms[k] === t))
  );
  
  area.innerHTML = `
<div class="ai-message">
<strong>➡️ Suggested Next Steps</strong>
<p>Based on your study of <strong>${currentTerm.name}</strong>, consider exploring:</p>
<div class="ai-suggestion">
${unexplored.length > 0 ? 
  unexplored.slice(0, 3).map(t => `<strong>${t.name}:</strong> ${t.definition.substring(0, 80)}...`).join('<br><br>') :
  'You\'ve explored the related concepts! Try reviewing papers or writing a comprehensive explanation.'
}
</div>
<p><strong>Learning Path:</strong> ${currentTerm.name} → ${relatedTerms.slice(0, 2).map(t => t.name).join(' → ')}</p>
</div>
  `;
}

function aiCreateQuiz() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiCoachingResult');
  const questions = [
    { q: `What is the main purpose of ${currentTerm.name}?`, a: currentTerm.definition },
    { q: `Name two related concepts to ${currentTerm.name}.`, a: currentTerm.relatedTerms.slice(0, 2).map(id => wikiTerms[id]?.name).join(', ') },
    { q: `What problem does ${currentTerm.name} solve?`, a: 'Think about the motivation and use cases' }
  ];
  
  area.innerHTML = `
<div class="ai-message">
<strong>📝 Quick Quiz: ${currentTerm.name}</strong>
<p>Test your understanding:</p>
${questions.map((q, i) => `
<div class="ai-suggestion">
<strong>Q${i+1}:</strong> ${q.q}<br>
<details>
<summary>Show Answer</summary>
${q.a}
</details>
</div>
`).join('')}
</div>
  `;
}

function aiCheckNewPapers() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiUpdateResult');
  const recentPapers = paperDatabase.filter(p => 
    p.keywords.some(k => currentTerm.keywords.includes(k))
  ).sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 5);
  
  area.innerHTML = `
<div class="ai-message">
<strong>📄 Recent Papers on ${currentTerm.name}</strong>
${recentPapers.length > 0 ? `
<p>Found ${recentPapers.length} recent papers:</p>
<ul>
${recentPapers.map(p => `<li><strong>${p.title}</strong> (${p.date})<br><em>${p.abstract.substring(0, 100)}...</em></li>`).join('')}
</ul>
<div class="ai-suggestion">
💡 Do any of these papers challenge or extend your current understanding?
</div>
` : '<p>No recent papers found for this topic.</p>'}
</div>
  `;
}

function aiSuggestUpdates() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiUpdateResult');
  const contributions = wikiContributions.filter(c => c.termId === currentTerm.id);
  const lastUpdate = contributions.length > 0 ? 
    new Date(Math.max(...contributions.map(c => c.timestamp))).toLocaleDateString() : 
    'Never';
  
  area.innerHTML = `
<div class="ai-message">
<strong>💡 Update Suggestions for ${currentTerm.name}</strong>
<p><strong>Last updated:</strong> ${lastUpdate}</p>
<div class="ai-suggestion">
<strong>Consider updating:</strong><br>
• Add new examples or applications<br>
• Incorporate insights from recent papers<br>
• Clarify any confusing explanations<br>
• Add connections to newly learned concepts<br>
• Update based on feedback from review mode
</div>
<p>Regular updates help solidify your understanding and keep knowledge current.</p>
</div>
  `;
}

function aiCompareVersions() {
  if (!currentTerm || !termVersions[currentTerm.id]) {
    alert('No version history available for this term');
    return;
  }
  
  const area = document.getElementById('aiUpdateResult');
  const versions = termVersions[currentTerm.id];
  
  if (versions.length < 2) {
    area.innerHTML = `
<div class="ai-message">
<strong>⚖️ Version Comparison</strong>
<p>Only one version exists. Keep updating your explanation to see how your understanding evolves!</p>
</div>
    `;
    return;
  }
  
  const latest = versions[versions.length - 1];
  const previous = versions[versions.length - 2];
  
  area.innerHTML = `
<div class="ai-message">
<strong>⚖️ Version Comparison</strong>
<p><strong>Previous version:</strong> ${new Date(previous.timestamp).toLocaleDateString()}</p>
<p><strong>Current version:</strong> ${new Date(latest.timestamp).toLocaleDateString()}</p>
<div class="ai-suggestion">
<strong>Changes detected:</strong><br>
• Word count: ${previous.content.split(/\s+/).length} → ${latest.content.split(/\s+/).length}<br>
• ${latest.content.length > previous.content.length ? '✓ More detailed explanation' : '✓ More concise explanation'}<br>
• Your understanding is ${versions.length > 3 ? 'well-developed' : 'developing'}
</div>
<p>Keep refining to deepen your mastery!</p>
</div>
  `;
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
<script src="js/stage-navigation.js"></script>
