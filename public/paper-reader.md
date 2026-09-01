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
  </div>

  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar">
    <div class="progress-fill" id="progressFill"></div>
    <span class="progress-text" id="progressText">0%</span>
  </div>
</div>

<style>
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
loadPaper();
</script>
