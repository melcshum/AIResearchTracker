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
<div class="ai-companion-modes">
<button class="ai-mode-btn active" onclick="switchAIMode('write')" title="Help me write">✍️ Write</button>
<button class="ai-mode-btn" onclick="switchAIMode('review')" title="Review my explanation">🔍 Review</button>
<button class="ai-mode-btn" onclick="switchAIMode('coach')" title="Guide my learning">🎯 Coach</button>
<button class="ai-mode-btn" onclick="switchAIMode('update')" title="Suggest updates">🔄 Update</button>
</div>

<div id="aiWriteMode" class="ai-mode-content active">
<div class="ai-prompt">
<p class="ai-hint">💡 I'll help you explain this concept. Start typing, and I'll provide suggestions.</p>
<button class="ai-action-btn" onclick="aiStartDraft()">📝 Start Draft</button>
<button class="ai-action-btn" onclick="aiSuggestStructure()">🏗️ Suggest Structure</button>
<button class="ai-action-btn" onclick="aiProvideHints()">💡 Give Hints</button>
</div>
<div id="aiWritingAssist" class="ai-assist-area"></div>
</div>

<div id="aiReviewMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🔍 I'll review your explanation and identify gaps or unclear parts.</p>
<button class="ai-action-btn" onclick="aiReviewExplanation()">📊 Review Now</button>
<button class="ai-action-btn" onclick="aiCheckAccuracy()">✓ Check Accuracy</button>
<button class="ai-action-btn" onclick="aiFindGaps()">🕳️ Find Gaps</button>
</div>
<div id="aiReviewResult" class="ai-assist-area"></div>
</div>

<div id="aiCoachMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🎯 I'll track your progress and suggest what to learn next.</p>
<button class="ai-action-btn" onclick="aiAssessMastery()">📈 Assess Mastery</button>
<button class="ai-action-btn" onclick="aiSuggestNext()">➡️ What's Next?</button>
<button class="ai-action-btn" onclick="aiCreateQuiz()">📝 Quick Quiz</button>
</div>
<div id="aiCoachingResult" class="ai-assist-area"></div>
</div>

<div id="aiUpdateMode" class="ai-mode-content">
<div class="ai-prompt">
<p class="ai-hint">🔄 I'll monitor new research and suggest updates to your understanding.</p>
<button class="ai-action-btn" onclick="aiCheckNewPapers()">📄 Check New Papers</button>
<button class="ai-action-btn" onclick="aiSuggestUpdates()">💡 Suggest Updates</button>
<button class="ai-action-btn" onclick="aiCompareVersions()">⚖️ Compare Versions</button>
</div>
<div id="aiUpdateResult" class="ai-assist-area"></div>
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

/* AI Companion Styles */
.ai-companion {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border: 2px solid #667eea;
  border-radius: 12px;
  padding: 15px;
  margin-top: 15px;
}

.ai-companion h4 {
  margin: 0 0 12px 0;
  color: #2c3e50;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.ai-companion-modes {
  display: flex;
  gap: 8px;
  margin-bottom: 15px;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 10px;
}

.ai-mode-btn {
  flex: 1;
  padding: 8px 12px;
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s;
  color: #666;
}

.ai-mode-btn:hover {
  background: #f0f4f8;
  border-color: #667eea;
  transform: translateY(-2px);
}

.ai-mode-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: #667eea;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.ai-mode-content {
  display: none;
}

.ai-mode-content.active {
  display: block;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.ai-prompt {
  background: white;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 12px;
}

.ai-hint {
  color: #666;
  font-size: 13px;
  margin: 0 0 10px 0;
  line-height: 1.5;
}

.ai-action-btn {
  display: inline-block;
  padding: 6px 12px;
  margin: 4px 4px 4px 0;
  background: white;
  border: 1px solid #667eea;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  color: #667eea;
  transition: all 0.2s;
}

.ai-action-btn:hover {
  background: #667eea;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(102, 126, 234, 0.3);
}

.ai-assist-area {
  background: white;
  border-radius: 8px;
  padding: 12px;
  min-height: 80px;
  font-size: 13px;
  line-height: 1.6;
  color: #333;
}

.ai-assist-area:empty {
  display: none;
}

.ai-assist-area .ai-message {
  padding: 10px;
  background: #f8f9fa;
  border-left: 3px solid #667eea;
  border-radius: 4px;
  margin-bottom: 8px;
}

.ai-assist-area .ai-suggestion {
  padding: 8px;
  background: #fff3cd;
  border-left: 3px solid #ffc107;
  border-radius: 4px;
  margin: 6px 0;
}

.ai-assist-area .ai-warning {
  padding: 8px;
  background: #f8d7da;
  border-left: 3px solid #dc3545;
  border-radius: 4px;
  margin: 6px 0;
}

.ai-assist-area .ai-success {
  padding: 8px;
  background: #d4edda;
  border-left: 3px solid #28a745;
  border-radius: 4px;
  margin: 6px 0;
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
<strong>📝 Starting draft for "${currentTerm.name}"</strong>
<p>Here's a structure to help you explain this concept:</p>
<div class="ai-suggestion">
<strong>1. Definition:</strong> Start with a clear, concise definition<br>
<strong>2. Key Components:</strong> What are the main parts?<br>
<strong>3. How it Works:</strong> Explain the mechanism<br>
<strong>4. Example:</strong> Provide a concrete example<br>
<strong>5. Related Concepts:</strong> Connect to ${currentTerm.relatedTerms.slice(0, 3).join(', ')}
</div>
<p>Try writing your explanation, then use "Review" mode to get feedback!</p>
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

function aiReviewExplanation() {
  const textarea = document.getElementById('explanationInput');
  if (!textarea || !textarea.value.trim()) {
    alert('Please write an explanation first in the "Add Explanation" panel');
    return;
  }
  
  const explanation = textarea.value;
  const area = document.getElementById('aiReviewResult');
  const wordCount = explanation.split(/\s+/).length;
  const sentenceCount = explanation.split(/[.!?]+/).length;
  
  // Check for key terms
  const missingTerms = currentTerm.keywords.filter(k => 
    !explanation.toLowerCase().includes(k.toLowerCase())
  );
  
  // Check for related concepts
  const mentionedRelated = currentTerm.relatedTerms.filter(id => {
    const term = wikiTerms[id];
    return term && explanation.toLowerCase().includes(term.name.toLowerCase());
  });
  
  let feedback = '<div class="ai-message"><strong>📊 Explanation Review</strong>';
  
  // Length feedback
  if (wordCount < 50) {
    feedback += '<div class="ai-warning">⚠️ Your explanation is quite brief (' + wordCount + ' words). Consider adding more detail.</div>';
  } else if (wordCount > 300) {
    feedback += '<div class="ai-suggestion">💡 Your explanation is comprehensive (' + wordCount + ' words). Consider breaking it into paragraphs for readability.</div>';
  } else {
    feedback += '<div class="ai-success">✓ Good length: ' + wordCount + ' words</div>';
  }
  
  // Missing terms
  if (missingTerms.length > 0) {
    feedback += '<div class="ai-warning">⚠️ Consider including these key terms: ' + missingTerms.slice(0, 5).join(', ') + '</div>';
  } else {
    feedback += '<div class="ai-success">✓ You\'ve covered the key terminology</div>';
  }
  
  // Related concepts
  if (mentionedRelated.length === 0) {
    feedback += '<div class="ai-suggestion">💡 Try connecting this to related concepts like: ' + 
      currentTerm.relatedTerms.slice(0, 3).map(id => wikiTerms[id]?.name).filter(Boolean).join(', ') + '</div>';
  } else {
    feedback += '<div class="ai-success">✓ Good connections to: ' + 
      mentionedRelated.map(id => wikiTerms[id]?.name).join(', ') + '</div>';
  }
  
  feedback += '</div>';
  area.innerHTML = feedback;
}

function aiCheckAccuracy() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiReviewResult');
  area.innerHTML = `
<div class="ai-message">
<strong>✓ Accuracy Check for ${currentTerm.name}</strong>
<p><strong>Official Definition:</strong> ${currentTerm.definition}</p>
<div class="ai-suggestion">
<strong>Key points to verify:</strong><br>
• Does your explanation match this definition?<br>
• Are the technical details correct?<br>
• Have you cited reliable sources?<br>
• Are there any common misconceptions to address?
</div>
<p>Compare your explanation with the definition above to ensure accuracy.</p>
</div>
  `;
}

function aiFindGaps() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  const area = document.getElementById('aiReviewResult');
  const questions = [
    'What problem does this solve?',
    'How does it work technically?',
    'What are the limitations?',
    'How does it compare to alternatives?',
    'What are real-world applications?',
    'What are common misconceptions?'
  ];
  
  area.innerHTML = `
<div class="ai-message">
<strong>🕳️ Potential Gaps to Address</strong>
<p>Consider if your explanation answers these questions:</p>
<div class="ai-suggestion">
${questions.map(q => `□ ${q}`).join('<br>')}
</div>
<p>Check off what you've covered and add details for missing areas.</p>
</div>
  `;
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
