---
title: "Paper Reader"
---

<div class="reader-container">
<!-- Reader Header -->
<div class="reader-header">
<div class="reader-controls">
<button id="backBtn" class="btn-icon" title="Back to Workspace">← Back</button>
<div class="reader-title" id="paperTitle">Select a paper to read</div>
<div class="reader-actions">
<button id="bookmarkBtn" class="btn-icon" title="Bookmark">🔖</button>
<button id="highlightBtn" class="btn-icon" title="Highlight">🖍️</button>
<button id="noteBtn" class="btn-icon" title="Add Note">📝</button>
<button id="questionBtn" class="btn-icon" title="Add Question">❓</button>
<button id="conceptValidationBtn" class="btn-icon" title="Validate AI Concepts">🧠</button>
<button id="feedbackBtn" class="btn-icon" title="Rate AI Summary">⭐</button>
<button id="exportAnnotationsBtn" class="btn-icon" title="Export Annotations">💾</button>
<button id="fullScreenBtn" class="btn-icon" title="Full Screen">⛶</button>
</div>
</div>
</div>

<!-- Reader Content -->
<div class="reader-content">
<!-- Left Sidebar: Table of Contents -->
<aside class="reader-sidebar" id="tocSidebar">
<h3>📑 Contents</h3>
<nav id="tableOfContents"></nav>
</aside>

<!-- Main Reading Area -->
<main class="reader-main" id="readingArea">
<div class="paper-metadata" id="paperMetadata"></div>
<div class="paper-content" id="paperContent">
<div class="empty-state">
<h2>📖 Ready to Read</h2>
<p>Select a paper from your reading queue or search to begin</p>
<button onclick="window.location.href='workspace.html'" class="btn-primary">Go to Workspace</button>
</div>
</div>
</main>

<!-- Right Sidebar: Annotations -->
<aside class="reader-sidebar" id="annotationsSidebar">
<h3>📝 Annotations</h3>
<div class="annotations-list" id="annotationsList">
<div class="empty-annotations">
<p>No annotations yet</p>
<p class="hint">Select text to highlight or add notes</p>
</div>
</div>
</aside>

<!-- AI Companion Panel (Right Sidebar) -->
<aside class="reader-sidebar ai-companion-sidebar" id="aiCompanionSidebar" style="display: none;">
<h3>🤖 AI Companion</h3>
<div class="companion-modes">
<button class="companion-mode-btn active" onclick="switchCompanionMode('reflect')">Reflect</button>
<button class="companion-mode-btn" onclick="switchCompanionMode('scaffold')">Scaffold</button>
<button class="companion-mode-btn" onclick="switchCompanionMode('consolidate')">Consolidate</button>
</div>
<div class="companion-content" id="companionContent">
<div class="companion-intro">
<p>Select a concept in the paper and choose a mode:</p>
<ul>
<li><strong>Reflect:</strong> Metacognitive questions</li>
<li><strong>Scaffold:</strong> Gap detection & hints</li>
<li><strong>Consolidate:</strong> Recall practice</li>
</ul>
</div>
</div>
</aside>
</div>

<!-- Reading Progress Bar -->
<div class="reading-progress-bar">
<div class="progress-fill" id="progressFill"></div>
<span class="progress-text" id="progressText">0%</span>
</div>
</div>

<style>
/* Import shared AI Companion styles */
@import url('/css/ai-companion.css');

/* Page-specific styles only (no AI Companion duplication) */
.reader-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 60px);
  background: #ffffff;
}

.reader-header {
  background: #2c5aa0;
  color: white;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.reader-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.reader-title {
  flex: 1;
  font-size: 1.2rem;
  font-weight: 600;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.reader-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-icon {
  background: rgba(255,255,255,0.2);
  border: none;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.2s;
}

.btn-icon:hover {
  background: rgba(255,255,255,0.3);
  transform: translateY(-1px);
}

.reader-content {
  display: grid;
  grid-template-columns: 250px 1fr 300px;
  flex: 1;
  overflow: hidden;
}

.reader-sidebar {
  background: #f8f9fa;
  padding: 1.5rem;
  overflow-y: auto;
  border-right: 1px solid #e0e0e0;
}

.reader-sidebar h3 {
  margin-top: 0;
  color: #2c5aa0;
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.reader-main {
  padding: 2rem 3rem;
  overflow-y: auto;
  line-height: 1.8;
}

.paper-metadata {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  border-left: 4px solid #2c5aa0;
}

.paper-metadata h1 {
  margin-top: 0;
  color: #2c5aa0;
  font-size: 1.8rem;
}

.paper-metadata .authors {
  color: #666;
  font-size: 0.95rem;
  margin: 0.5rem 0;
}

.paper-metadata .abstract {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #ddd;
}

.paper-content {
  font-size: 1.05rem;
}

.paper-content h2 {
  color: #2c5aa0;
  margin-top: 2rem;
  border-bottom: 2px solid #2c5aa0;
  padding-bottom: 0.5rem;
}

.paper-content h3 {
  color: #333;
  margin-top: 1.5rem;
}

.paper-content p {
  margin-bottom: 1rem;
  text-align: justify;
}

/* Text selection and highlighting */
.paper-content ::selection {
  background: #ffd54f;
  color: #000;
}

.highlight {
  background: #ffd54f;
  padding: 2px 4px;
  border-radius: 3px;
  cursor: pointer;
  position: relative;
}

.highlight:hover {
  background: #ffca28;
}

.highlight-note {
  background: #81c784;
}

/* Annotations */
.annotations-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.annotation-item {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  border-left: 3px solid #2c5aa0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.annotation-item.highlight {
  border-left-color: #ffd54f;
}

.annotation-item.note {
  border-left-color: #81c784;
}

.annotation-item.question {
  border-left-color: #e57373;
}

.annotation-text {
  font-size: 0.9rem;
  color: #333;
  margin-bottom: 0.5rem;
  font-style: italic;
}

.annotation-note {
  font-size: 0.85rem;
  color: #666;
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid #eee;
}

.annotation-actions {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.annotation-actions button {
  background: none;
  border: none;
  color: #2c5aa0;
  cursor: pointer;
  font-size: 0.85rem;
  padding: 0.25rem 0.5rem;
}

.annotation-actions button:hover {
  text-decoration: underline;
}

.empty-annotations {
  text-align: center;
  color: #999;
  padding: 2rem;
}

.empty-annotations .hint {
  font-size: 0.85rem;
  color: #bbb;
}

/* Feedback Modal Styles */
.feedback-modal {
  max-width: 600px;
  padding: 2rem;
}

.feedback-modal h2 {
  margin-top: 0;
  color: #2c5aa0;
}

.feedback-section {
  margin: 1.5rem 0;
}

.feedback-section h3 {
  font-size: 1rem;
  color: #333;
  margin-bottom: 0.75rem;
}

.rating-stars {
  display: flex;
  gap: 0.5rem;
  font-size: 2rem;
}

.rating-stars .star {
  cursor: pointer;
  color: #ddd;
  transition: color 0.2s;
}

.rating-stars .star.active,
.rating-stars .star:hover,
.rating-stars .star:hover ~ .star {
  color: #ffd700;
}

.accuracy-options,
.improvement-tags {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.radio-option,
.tag-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 4px;
  transition: background 0.2s;
}

.radio-option:hover,
.tag-option:hover {
  background: #f5f5f5;
}

.radio-option input,
.tag-option input {
  cursor: pointer;
}

.feedback-modal textarea {
  width: 100%;
  min-height: 100px;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.95rem;
  resize: vertical;
}

.feedback-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
}

.btn-primary,
.btn-secondary {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: #2c5aa0;
  color: white;
}

.btn-primary:hover {
  background: #1e4a8f;
}

.btn-secondary {
  background: #e0e0e0;
  color: #333;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

/* Notification Styles */
@keyframes slideIn {
  from {
    transform: translateX(400px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOut {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(400px);
    opacity: 0;
  }
}

/* Concept Validation Modal */
.concept-validation-modal {
  max-width: 700px;
  padding: 2rem;
}

.concept-validation-list {
  max-height: 400px;
  overflow-y: auto;
  margin: 1.5rem 0;
}

.concept-validation-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  background: #f8f9fa;
}

.concept-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.concept-confidence {
  font-size: 0.85rem;
  color: #666;
}

.concept-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-validate {
  padding: 0.5rem 1rem;
  border: 2px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 500;
}

.btn-validate:hover {
  border-color: #999;
}

.btn-confirm.active {
  background: #4caf50;
  color: white;
  border-color: #4caf50;
}

.btn-reject.active {
  background: #f44336;
  color: white;
  border-color: #f44336;
}

.validation-summary {
  padding: 1rem;
  background: #e3f2fd;
  border-radius: 6px;
  margin: 1rem 0;
}

/* Recommendation Rating */
.recommendation-rating {
  margin-top: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  border: 1px solid #e0e0e0;
}

.recommendation-rating p {
  margin: 0 0 0.75rem 0;
  font-weight: 500;
}

.rating-buttons {
  display: flex;
  gap: 0.5rem;
}

.btn-rate {
  flex: 1;
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 1rem;
}

.btn-rate:hover {
  border-color: #2c5aa0;
  background: #e3f2fd;
}

.btn-thumbs-up:hover {
  border-color: #4caf50;
  background: #e8f5e9;
}

.btn-thumbs-down:hover {
  border-color: #f44336;
  background: #ffebee;
}

.rating-feedback {
  margin-top: 0.75rem;
}

.rating-feedback textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  resize: vertical;
  margin-bottom: 0.5rem;
}

.btn-small {
  padding: 0.4rem 0.8rem;
  background: #2c5aa0;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

.btn-small:hover {
  background: #1e4a8f;
}

/* Table of Contents */
#tableOfContents {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

#tableOfContents a {
  color: #333;
  text-decoration: none;
  padding: 0.5rem;
  border-radius: 4px;
  transition: all 0.2s;
  font-size: 0.9rem;
}

#tableOfContents a:hover {
  background: #e3f2fd;
  color: #2c5aa0;
}

#tableOfContents a.active {
  background: #2c5aa0;
  color: white;
}

/* Reading Progress */
.reading-progress-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  background: #f8f9fa;
  border-top: 1px solid #e0e0e0;
  display: flex;
  align-items: center;
  padding: 0 2rem;
}

.progress-fill {
  height: 6px;
  background: #2c5aa0;
  border-radius: 3px;
  transition: width 0.3s;
  flex: 1;
  margin-right: 1rem;
}

.progress-text {
  font-weight: 600;
  color: #2c5aa0;
  min-width: 50px;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #999;
}

.empty-state h2 {
  color: #2c5aa0;
  margin-bottom: 1rem;
}

/* Full Screen Mode */
.reader-container.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  height: 100vh;
}

.reader-container.fullscreen .reader-header {
  display: none;
}

/* Responsive */
@media (max-width: 1200px) {
  .reader-content {
    grid-template-columns: 200px 1fr 250px;
  }
}

@media (max-width: 900px) {
  .reader-content {
    grid-template-columns: 1fr;
  }
  
  .reader-sidebar {
    display: none;
  }
  
  .reader-main {
    padding: 1rem;
  }
}

/* Context Menu */
.context-menu {
  position: absolute;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  padding: 0.5rem;
  z-index: 1000;
  display: none;
}

.context-menu.show {
  display: block;
}

.context-menu button {
  display: block;
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 4px;
  font-size: 0.9rem;
}

.context-menu button:hover {
  background: #f0f4f8;
}
</style>

<script>
let currentPaper = null;
let annotations = [];
let selectedText = '';
let selectionRange = null;

// Load paper from URL parameter or workspace
async function loadPaper() {
  const urlParams = new URLSearchParams(window.location.search);
  const paperId = urlParams.get('paper');
  
  if (paperId) {
    // Load paper data
    const response = await fetch(`${API_BASE}/api/papers`);
    const papers = await response.json();
    currentPaper = papers.find(p => p.id === paperId);
    
    if (currentPaper) {
      displayPaper(currentPaper);
      loadAnnotations(paperId);
    }
  }
}

function displayPaper(paper) {
  document.getElementById('paperTitle').textContent = paper.title;
  
  // Display metadata
  const metadataHtml = `
<h1>${paper.title}</h1>
<div class="authors">${paper.authors || 'Unknown authors'}</div>
<div class="date">📅 ${paper.date || 'Unknown date'}</div>
<div class="abstract">
<strong>Abstract:</strong>
<p>${paper.abstract || 'No abstract available'}</p>
</div>
  `;
  document.getElementById('paperMetadata').innerHTML = metadataHtml;
  
  // Display content (in real implementation, this would load the full paper markdown)
  const contentHtml = `
<h2>Introduction</h2>
<p>${paper.abstract || 'Paper content would be loaded here...'}</p>
    
<h2>Methodology</h2>
<p>Detailed methodology section would appear here with full paper content.</p>
    
<h2>Results</h2>
<p>Results and findings would be displayed here.</p>
    
<h2>Conclusion</h2>
<p>Conclusion and future work would be shown here.</p>
  `;
  document.getElementById('paperContent').innerHTML = contentHtml;
  
  // Generate table of contents
  generateTOC();
  
  // Enable text selection for annotations
  enableTextSelection();
}

function generateTOC() {
  const headings = document.querySelectorAll('.paper-content h2, .paper-content h3');
  const toc = document.getElementById('tableOfContents');
  
  toc.innerHTML = '';
  headings.forEach((heading, index) => {
    const id = `heading-${index}`;
    heading.id = id;
    
    const link = document.createElement('a');
    link.href = `#${id}`;
    link.textContent = heading.textContent;
    link.onclick = (e) => {
      e.preventDefault();
      heading.scrollIntoView({ behavior: 'smooth' });
      updateActiveTOC(id);
    };
    
    toc.appendChild(link);
  });
}

function updateActiveTOC(activeId) {
  const links = document.querySelectorAll('#tableOfContents a');
  links.forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === `#${activeId}`);
  });
}

function enableTextSelection() {
  const content = document.getElementById('paperContent');
  
  content.addEventListener('mouseup', () => {
    const selection = window.getSelection();
    selectedText = selection.toString().trim();
    
    if (selectedText) {
      selectionRange = selection.getRangeAt(0);
      showContextMenu();
    }
  });
  
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.context-menu')) {
      hideContextMenu();
    }
  });
}

function showContextMenu() {
  let menu = document.getElementById('contextMenu');
  if (!menu) {
    menu = document.createElement('div');
    menu.id = 'contextMenu';
    menu.className = 'context-menu';
    menu.innerHTML = `
<button onclick="addHighlight()">🖍️ Highlight</button>
<button onclick="addNote()">📝 Add Note</button>
<button onclick="addQuestion()">❓ Add Question</button>
    `;
    document.body.appendChild(menu);
  }
  
  const rect = selectionRange.getBoundingClientRect();
  menu.style.left = `${rect.left + window.scrollX}px`;
  menu.style.top = `${rect.bottom + window.scrollY + 5}px`;
  menu.classList.add('show');
}

function hideContextMenu() {
  const menu = document.getElementById('contextMenu');
  if (menu) {
    menu.classList.remove('show');
  }
}

function addHighlight() {
  if (!selectedText || !selectionRange) return;
  
  const annotation = {
    id: Date.now(),
    paperId: currentPaper.id,
    type: 'highlight',
    text: selectedText,
    note: '',
    timestamp: new Date().toISOString()
  };
  
  annotations.push(annotation);
  wrapSelection('highlight');
  displayAnnotations();
  hideContextMenu();
  saveAnnotations();
}

function addNote() {
  if (!selectedText || !selectionRange) return;
  
  const note = prompt('Add your note:');
  if (!note) return;
  
  const annotation = {
    id: Date.now(),
    paperId: currentPaper.id,
    type: 'note',
    text: selectedText,
    note: note,
    timestamp: new Date().toISOString()
  };
  
  annotations.push(annotation);
  wrapSelection('highlight-note');
  displayAnnotations();
  hideContextMenu();
  saveAnnotations();
}

function addQuestion() {
  if (!selectedText || !selectionRange) return;
  
  const question = prompt('Add your question:');
  if (!question) return;
  
  const annotation = {
    id: Date.now(),
    paperId: currentPaper.id,
    type: 'question',
    text: selectedText,
    note: question,
    timestamp: new Date().toISOString()
  };
  
  annotations.push(annotation);
  wrapSelection('highlight');
  displayAnnotations();
  hideContextMenu();
  saveAnnotations();
}

function wrapSelection(className) {
  const span = document.createElement('span');
  span.className = className;
  span.dataset.annotationId = annotations[annotations.length - 1].id;
  
  selectionRange.surroundContents(span);
}

function displayAnnotations() {
  const list = document.getElementById('annotationsList');
  
  if (annotations.length === 0) {
    list.innerHTML = `
<div class="empty-annotations">
<p>No annotations yet</p>
<p class="hint">Select text to highlight or add notes</p>
</div>
    `;
    return;
  }
  
  list.innerHTML = annotations.map(ann => `
<div class="annotation-item ${ann.type}">
<div class="annotation-text">"${ann.text}"</div>
      ${ann.note ? `<div class="annotation-note">${ann.note}</div>` : ''}
<div class="annotation-actions">
<button onclick="editAnnotation(${ann.id})">Edit</button>
<button onclick="deleteAnnotation(${ann.id})">Delete</button>
</div>
</div>
  `).join('');
}

function editAnnotation(id) {
  const annotation = annotations.find(a => a.id === id);
  if (!annotation) return;
  
  const newNote = prompt('Edit note:', annotation.note);
  if (newNote !== null) {
    annotation.note = newNote;
    displayAnnotations();
    saveAnnotations();
  }
}

function deleteAnnotation(id) {
  if (!confirm('Delete this annotation?')) return;
  
  annotations = annotations.filter(a => a.id !== id);
  
  // Remove highlight from text
  const highlight = document.querySelector(`[data-annotation-id="${id}"]`);
  if (highlight) {
    const parent = highlight.parentNode;
    while (highlight.firstChild) {
      parent.insertBefore(highlight.firstChild, highlight);
    }
    parent.removeChild(highlight);
  }
  
  displayAnnotations();
  saveAnnotations();
}

function loadAnnotations(paperId) {
  // Load from localStorage or API
  const stored = localStorage.getItem(`annotations_${paperId}`);
  if (stored) {
    annotations = JSON.parse(stored);
    displayAnnotations();
  }
}

function saveAnnotations() {
  if (!currentPaper) return;
  localStorage.setItem(`annotations_${currentPaper.id}`, JSON.stringify(annotations));
}

// Reading progress tracking
function updateReadingProgress() {
  const readingArea = document.getElementById('readingArea');
  const scrollTop = readingArea.scrollTop;
  const scrollHeight = readingArea.scrollHeight - readingArea.clientHeight;
  const progress = (scrollTop / scrollHeight) * 100;
  
  document.getElementById('progressFill').style.width = `${progress}%`;
  document.getElementById('progressText').textContent = `${Math.round(progress)}%`;
}

// HITL Phase 1: AI Feedback System
document.getElementById('feedbackBtn').addEventListener('click', showFeedbackModal);

function showFeedbackModal() {
  if (!currentPaper) {
    alert('Please load a paper first');
    return;
  }

  const modal = document.createElement('div');
  modal.className = 'modal show';
  modal.innerHTML = `
<div class="modal-content feedback-modal">
<span class="modal-close" onclick="closeFeedbackModal()">&times;</span>
<h2>⭐ Rate AI Summary</h2>
<p>Help us improve AI-generated summaries by providing feedback</p>
      
<div class="feedback-section">
<h3>Summary Quality</h3>
<div class="rating-stars" data-rating="summary">
<span class="star" data-value="1">★</span>
<span class="star" data-value="2">★</span>
<span class="star" data-value="3">★</span>
<span class="star" data-value="4">★</span>
<span class="star" data-value="5">★</span>
</div>
</div>

<div class="feedback-section">
<h3>Accuracy</h3>
<div class="accuracy-options">
<label class="radio-option">
<input type="radio" name="accuracy" value="accurate">
<span>✓ Accurate - captures key points well</span>
</label>
<label class="radio-option">
<input type="radio" name="accuracy" value="partially">
<span>◐ Partially accurate - misses some details</span>
</label>
<label class="radio-option">
<input type="radio" name="accuracy" value="inaccurate">
<span>✗ Inaccurate - misrepresents content</span>
</label>
</div>
</div>

<div class="feedback-section">
<h3>What could be improved?</h3>
<div class="improvement-tags">
<label class="tag-option">
<input type="checkbox" value="too-brief">
<span>Too brief</span>
</label>
<label class="tag-option">
<input type="checkbox" value="too-verbose">
<span>Too verbose</span>
</label>
<label class="tag-option">
<input type="checkbox" value="missing-methods">
<span>Missing methods</span>
</label>
<label class="tag-option">
<input type="checkbox" value="missing-results">
<span>Missing results</span>
</label>
<label class="tag-option">
<input type="checkbox" value="unclear">
<span>Unclear language</span>
</label>
</div>
</div>

<div class="feedback-section">
<h3>Additional Comments (Optional)</h3>
<textarea id="feedbackComments" placeholder="Share specific feedback about the summary..."></textarea>
</div>

<div class="feedback-actions">
<button class="btn-secondary" onclick="closeFeedbackModal()">Cancel</button>
<button class="btn-primary" onclick="submitFeedback()">Submit Feedback</button>
</div>
</div>
  `;
  
  document.body.appendChild(modal);
  setupStarRating();
}

function setupStarRating() {
  const stars = document.querySelectorAll('.rating-stars .star');
  stars.forEach(star => {
    star.addEventListener('click', function() {
      const rating = parseInt(this.dataset.value);
      const container = this.parentElement;
      container.dataset.rating = rating;
      
      // Update star appearance
      container.querySelectorAll('.star').forEach((s, idx) => {
        s.classList.toggle('active', idx < rating);
      });
    });
  });
}

function closeFeedbackModal() {
  const modal = document.querySelector('.feedback-modal');
  if (modal) {
    modal.parentElement.remove();
  }
}

function submitFeedback() {
  const modal = document.querySelector('.feedback-modal');
  const summaryRating = parseInt(modal.querySelector('.rating-stars').dataset.rating) || 0;
  const accuracy = modal.querySelector('input[name="accuracy"]:checked')?.value || '';
  const improvements = Array.from(modal.querySelectorAll('.improvement-tags input:checked'))
    .map(cb => cb.value);
  const comments = document.getElementById('feedbackComments').value;

  if (!summaryRating && !accuracy) {
    alert('Please provide at least a rating or accuracy assessment');
    return;
  }

  const feedback = {
    paperId: currentPaper.id,
    timestamp: new Date().toISOString(),
    summaryRating,
    accuracy,
    improvements,
    comments
  };

  // Save feedback
  saveFeedback(feedback);
  
  // Show success message
  showNotification('✓ Feedback submitted! Thank you for helping improve AI summaries.', 'success');
  closeFeedbackModal();
}

function saveFeedback(feedback) {
  const key = `feedback_${feedback.paperId}`;
  const existing = JSON.parse(localStorage.getItem(key) || '[]');
  existing.push(feedback);
  localStorage.setItem(key, JSON.stringify(existing));

  // Also save to global feedback log
  const globalKey = 'ai_feedback_log';
  const globalLog = JSON.parse(localStorage.getItem(globalKey) || '[]');
  globalLog.push(feedback);
  localStorage.setItem(globalKey, JSON.stringify(globalLog));
}

// HITL Phase 1: Annotation Export
document.getElementById('exportAnnotationsBtn').addEventListener('click', exportAnnotations);

function exportAnnotations() {
  if (!currentPaper) {
    alert('Please load a paper first');
    return;
  }

  if (annotations.length === 0) {
    alert('No annotations to export');
    return;
  }

  const format = prompt('Export format:\n1. JSON\n2. Markdown\n3. Plain Text\n\nEnter number (1-3):', '1');
  
  if (!format) return;

  let content, filename, mimeType;

  switch(format) {
    case '1':
      content = JSON.stringify({
        paper: {
          id: currentPaper.id,
          title: currentPaper.title,
          authors: currentPaper.authors
        },
        annotations: annotations,
        exportedAt: new Date().toISOString()
      }, null, 2);
      filename = `${currentPaper.id}_annotations.json`;
      mimeType = 'application/json';
      break;

    case '2':
      content = generateMarkdownExport();
      filename = `${currentPaper.id}_annotations.md`;
      mimeType = 'text/markdown';
      break;

    case '3':
      content = generateTextExport();
      filename = `${currentPaper.id}_annotations.txt`;
      mimeType = 'text/plain';
      break;

    default:
      alert('Invalid format selection');
      return;
  }

  downloadFile(content, filename, mimeType);
  showNotification(`✓ Exported ${annotations.length} annotations as ${format === '1' ? 'JSON' : format === '2' ? 'Markdown' : 'Text'}`, 'success');
}

function generateMarkdownExport() {
  let md = `# Annotations for: ${currentPaper.title}\n\n`;
  md += `**Authors:** ${currentPaper.authors?.join(', ') || 'Unknown'}\n\n`;
  md += `**Exported:** ${new Date().toLocaleString()}\n\n`;
  md += `---\n\n`;

  const highlights = annotations.filter(a => a.type === 'highlight');
  const notes = annotations.filter(a => a.type === 'note');
  const questions = annotations.filter(a => a.type === 'question');

  if (highlights.length > 0) {
    md += `## 🖍️ Highlights (${highlights.length})\n\n`;
    highlights.forEach((h, i) => {
      md += `${i + 1}. > ${h.text}\n\n`;
    });
  }

  if (notes.length > 0) {
    md += `## 📝 Notes (${notes.length})\n\n`;
    notes.forEach((n, i) => {
      md += `### Note ${i + 1}\n`;
      md += `**Text:** ${n.text}\n\n`;
      md += `**Note:** ${n.note}\n\n`;
    });
  }

  if (questions.length > 0) {
    md += `## ❓ Questions (${questions.length})\n\n`;
    questions.forEach((q, i) => {
      md += `### Question ${i + 1}\n`;
      md += `**Context:** ${q.text}\n\n`;
      md += `**Question:** ${q.note}\n\n`;
    });
  }

  return md;
}

function generateTextExport() {
  let text = `ANNOTATIONS FOR: ${currentPaper.title}\n`;
  text += `Authors: ${currentPaper.authors?.join(', ') || 'Unknown'}\n`;
  text += `Exported: ${new Date().toLocaleString()}\n`;
  text += `${'='.repeat(80)}\n\n`;

  annotations.forEach((ann, i) => {
    text += `[${i + 1}] ${ann.type.toUpperCase()}\n`;
    text += `Text: "${ann.text}"\n`;
    if (ann.note) {
      text += `${ann.type === 'question' ? 'Question' : 'Note'}: ${ann.note}\n`;
    }
    text += `Time: ${new Date(ann.timestamp).toLocaleString()}\n`;
    text += `${'-'.repeat(80)}\n\n`;
  });

  return text;
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 1rem 1.5rem;
    background: ${type === 'success' ? '#4caf50' : type === 'error' ? '#f44336' : '#2196f3'};
    color: white;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    z-index: 10000;
    font-weight: 500;
    animation: slideIn 0.3s ease-out;
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease-out';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}
  document.getElementById('progressFill').style.width = `${progress}%`;
  document.getElementById('progressText').textContent = `${Math.round(progress)}%`;
}

// HITL Phase 2: Concept Validation
document.getElementById('conceptValidationBtn')?.addEventListener('click', showConceptValidation);

function showConceptValidation() {
  if (!currentPaper) {
    alert('Please load a paper first');
    return;
  }

  // Extract concepts from paper (simplified version)
  const concepts = extractConceptsFromPaper(currentPaper);
  
  if (concepts.length === 0) {
    showNotification('No concepts detected in this paper', 'info');
    return;
  }

  const modal = document.createElement('div');
  modal.className = 'modal show';
  modal.innerHTML = `
<div class="modal-content concept-validation-modal">
<span class="modal-close" onclick="closeConceptValidation()">&times;</span>
<h2>🧠 Validate AI-Extracted Concepts</h2>
<p>Help improve concept extraction by confirming or rejecting detected concepts</p>
      
<div class="concept-validation-list">
        ${concepts.map((concept, idx) => `
<div class="concept-validation-item" data-concept="${concept.name}" data-index="${idx}">
<div class="concept-info">
<strong>${concept.name}</strong>
<span class="concept-confidence">${concept.confidence}% confidence</span>
</div>
<div class="concept-actions">
<button class="btn-validate btn-confirm" onclick="validateConcept(${idx}, true)">✓ Confirm</button>
<button class="btn-validate btn-reject" onclick="validateConcept(${idx}, false)">✗ Reject</button>
</div>
</div>
        `).join('')}
</div>

<div class="validation-summary">
<p><strong>Progress:</strong> <span id="validationProgress">0</span> / ${concepts.length} validated</p>
</div>

<div class="feedback-actions">
<button class="btn-secondary" onclick="closeConceptValidation()">Close</button>
<button class="btn-primary" onclick="saveConceptValidation()">Save All</button>
</div>
</div>
  `;
  
  document.body.appendChild(modal);
}

function extractConceptsFromPaper(paper) {
  // Simplified concept extraction - in production, this would use NLP
  const text = `${paper.title} ${paper.abstract || ''}`.toLowerCase();
  const concepts = [];
  
  // Common AI/ML concepts to detect
  const conceptPatterns = [
    { name: 'Machine Learning', pattern: /machine learning|ml\b/i, confidence: 85 },
    { name: 'Deep Learning', pattern: /deep learning|neural network/i, confidence: 90 },
    { name: 'Natural Language Processing', pattern: /nlp|natural language|text processing/i, confidence: 88 },
    { name: 'Computer Vision', pattern: /computer vision|image|visual/i, confidence: 85 },
    { name: 'Reinforcement Learning', pattern: /reinforcement learning|reward|policy/i, confidence: 90 },
    { name: 'Transformer', pattern: /transformer|attention mechanism/i, confidence: 92 },
    { name: 'GAN', pattern: /\bgan\b|generative adversarial/i, confidence: 95 },
    { name: 'Transfer Learning', pattern: /transfer learning|pretrain/i, confidence: 87 },
    { name: 'Few-shot Learning', pattern: /few.?shot|zero.?shot/i, confidence: 89 },
    { name: 'Meta-Learning', pattern: /meta.?learning|learning to learn/i, confidence: 88 }
  ];
  
  conceptPatterns.forEach(cp => {
    if (cp.pattern.test(text)) {
      concepts.push({
        name: cp.name,
        confidence: cp.confidence,
        validated: null
      });
    }
  });
  
  return concepts;
}

function validateConcept(index, isValid) {
  const item = document.querySelector(`[data-index="${index}"]`);
  const buttons = item.querySelectorAll('.btn-validate');
  
  buttons.forEach(btn => btn.classList.remove('active'));
  
  if (isValid) {
    buttons[0].classList.add('active');
  } else {
    buttons[1].classList.add('active');
  }
  
  // Update progress
  const validated = document.querySelectorAll('.concept-validation-item .btn-validate.active').length;
  document.getElementById('validationProgress').textContent = validated;
}

function saveConceptValidation() {
  const items = document.querySelectorAll('.concept-validation-item');
  const validations = [];
  
  items.forEach((item, idx) => {
    const concept = item.dataset.concept;
    const confirmBtn = item.querySelector('.btn-confirm.active');
    const rejectBtn = item.querySelector('.btn-reject.active');
    
    if (confirmBtn || rejectBtn) {
      validations.push({
        concept,
        validated: confirmBtn ? true : false,
        timestamp: new Date().toISOString()
      });
    }
  });
  
  if (validations.length === 0) {
    showNotification('Please validate at least one concept', 'warning');
    return;
  }
  
  // Save to localStorage
  const key = `concept_validation_${currentPaper.id}`;
  localStorage.setItem(key, JSON.stringify(validations));
  
  // Save to global log
  const globalKey = 'concept_validation_log';
  const globalLog = JSON.parse(localStorage.getItem(globalKey) || '[]');
  globalLog.push({
    paperId: currentPaper.id,
    validations,
    timestamp: new Date().toISOString()
  });
  localStorage.setItem(globalKey, JSON.stringify(globalLog));
  
  showNotification(`✓ Saved ${validations.length} concept validations`, 'success');
  closeConceptValidation();
}

function closeConceptValidation() {
  const modal = document.querySelector('.concept-validation-modal');
  if (modal) {
    modal.parentElement.remove();
  }
}

// HITL Phase 2: Recommendation Rating
function addRecommendationRating(paperId) {
  const ratingContainer = document.createElement('div');
  ratingContainer.className = 'recommendation-rating';
  ratingContainer.innerHTML = `
<p>Was this recommendation helpful?</p>
<div class="rating-buttons">
<button class="btn-rate btn-thumbs-up" onclick="rateRecommendation('${paperId}', true)">👍 Yes</button>
<button class="btn-rate btn-thumbs-down" onclick="rateRecommendation('${paperId}', false)">👎 No</button>
</div>
<div class="rating-feedback" style="display: none;">
<textarea placeholder="Why? (optional)" rows="2"></textarea>
<button class="btn-small" onclick="submitRatingFeedback('${paperId}')">Submit</button>
</div>
  `;
  return ratingContainer;
}

function rateRecommendation(paperId, isHelpful) {
  const rating = {
    paperId,
    isHelpful,
    timestamp: new Date().toISOString()
  };
  
  // Save to localStorage
  const key = `recommendation_rating_${paperId}`;
  localStorage.setItem(key, JSON.stringify(rating));
  
  // Save to global log
  const globalKey = 'recommendation_rating_log';
  const globalLog = JSON.parse(localStorage.getItem(globalKey) || '[]');
  globalLog.push(rating);
  localStorage.setItem(globalKey, JSON.stringify(globalLog));
  
  // Show feedback form
  const container = document.querySelector(`[data-paper-id="${paperId}"] .recommendation-rating`);
  if (container) {
    container.querySelector('.rating-buttons').style.display = 'none';
    container.querySelector('.rating-feedback').style.display = 'block';
  }
  
  showNotification('✓ Thanks for your feedback!', 'success');
}

function submitRatingFeedback(paperId) {
  const container = document.querySelector(`[data-paper-id="${paperId}"] .recommendation-rating`);
  const feedback = container.querySelector('textarea').value;
  
  if (feedback) {
    const key = `recommendation_rating_${paperId}`;
    const rating = JSON.parse(localStorage.getItem(key) || '{}');
    rating.feedback = feedback;
    localStorage.setItem(key, JSON.stringify(rating));
  }
  
  container.innerHTML = '<p>✓ Thank you for your feedback!</p>';
}

// Full screen mode
document.getElementById('fullScreenBtn')?.addEventListener('click', () => {
  document.querySelector('.reader-container').classList.toggle('fullscreen');
});

// Back button
document.getElementById('backBtn')?.addEventListener('click', () => {
  window.location.href = 'workspace.html';
});

// Initialize
document.getElementById('readingArea')?.addEventListener('scroll', updateReadingProgress);

// Event listener for concept selection in paper text
document.addEventListener('click', function(e) {
  if (e.target.classList.contains('highlight') || e.target.classList.contains('concept-link')) {
    const concept = e.target.dataset.concept || e.target.textContent;
    const explanation = prompt('Explain this concept in your own words:', '');
    if (explanation) {
      selectConceptForCompanion(concept, explanation);
    }
  }
});

loadPaper();
</script>
