---
title: "Paper Collections"
---

# 📁 Paper Collections

Create custom curated lists of papers around specific topics, projects, or research questions.

<div class="collections-container">
  <div class="collections-header">
    <button id="createCollectionBtn" class="btn-primary">+ Create Collection</button>
    <div class="collections-stats">
      <span class="stat">📁 <span id="totalCollections">0</span> Collections</span>
      <span class="stat">📄 <span id="totalPapersInCollections">0</span> Papers</span>
    </div>
  </div>
  
  <div id="collectionsList" class="collections-list"></div>
</div>

<!-- Create Collection Modal -->
<div id="createCollectionModal" class="modal" style="display: none;">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Create New Collection</h2>
      <button class="close-btn" onclick="closeCreateModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="form-group">
        <label>Collection Name</label>
        <input type="text" id="collectionName" placeholder="e.g., GUI Agents for Mobile Apps">
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea id="collectionDescription" placeholder="What is this collection about?"></textarea>
      </div>
      <div class="form-group">
        <label>Tags (comma-separated)</label>
        <input type="text" id="collectionTags" placeholder="e.g., mobile, gui, automation">
      </div>
      <div class="form-group">
        <label>Color</label>
        <div class="color-picker">
          <input type="color" id="collectionColor" value="#2c5aa0">
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn-secondary" onclick="closeCreateModal()">Cancel</button>
      <button class="btn-primary" onclick="createCollection()">Create Collection</button>
    </div>
  </div>
</div>

<!-- Collection Detail Modal -->
<div id="collectionDetailModal" class="modal" style="display: none;">
  <div class="modal-content modal-large">
    <div class="modal-header">
      <h2 id="detailCollectionName">Collection Name</h2>
      <button class="close-btn" onclick="closeDetailModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="collection-meta">
        <p id="detailCollectionDescription"></p>
        <div class="collection-tags" id="detailCollectionTags"></div>
        <div class="collection-actions">
          <button class="btn-secondary" onclick="addPapersToCollection()">+ Add Papers</button>
          <button class="btn-secondary" onclick="exportCollection()">📤 Export</button>
          <button class="btn-danger" onclick="deleteCollection()">🗑️ Delete Collection</button>
        </div>
      </div>
      
      <div class="add-papers-section" id="addPapersSection" style="display: none;">
        <h3>Add Papers to Collection</h3>
        <input type="text" id="paperSearch" placeholder="Search papers..." oninput="filterPapersForCollection()">
        <div id="papersList" class="papers-list"></div>
      </div>
      
      <div class="collection-papers">
        <h3>Papers in this Collection (<span id="collectionPaperCount">0</span>)</h3>
        <div id="collectionPapersList" class="collection-papers-list"></div>
      </div>
    </div>
  </div>
</div>

<style>
.collections-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.collections-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.collections-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  font-size: 1rem;
  color: #666;
}

.collections-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.collection-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: all 0.2s;
  border-left: 4px solid #2c5aa0;
}

.collection-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.collection-card-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.collection-card-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
  flex: 1;
}

.collection-card-count {
  background: #e8f4f8;
  color: #2c5aa0;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
}

.collection-card-description {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.collection-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: #f0f0f0;
  color: #666;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.85rem;
}

.collection-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e0e0e0;
  font-size: 0.9rem;
  color: #999;
}

/* Modal Styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  max-width: 600px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-large {
  max-width: 900px;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
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

.modal-body {
  padding: 1.5rem;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #e0e0e0;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.color-picker {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.color-picker input[type="color"] {
  width: 60px;
  height: 40px;
  border: 1px solid #ddd;
  border-radius: 6px;
  cursor: pointer;
}

.btn-primary, .btn-secondary, .btn-danger {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
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

.btn-danger {
  background: #e74c3c;
  color: white;
}

.btn-danger:hover {
  background: #c0392b;
}

.collection-meta {
  margin-bottom: 2rem;
}

.collection-meta p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.collection-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.collection-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.add-papers-section {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.add-papers-section h3 {
  margin-top: 0;
  color: #2c3e50;
}

#paperSearch {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  margin-bottom: 1rem;
}

.papers-list {
  max-height: 300px;
  overflow-y: auto;
}

.paper-item {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 0.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.paper-item-info {
  flex: 1;
}

.paper-item-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.3rem;
}

.paper-item-meta {
  font-size: 0.9rem;
  color: #666;
}

.collection-papers h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.collection-papers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.collection-paper-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: start;
}

.collection-paper-info {
  flex: 1;
}

.collection-paper-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.collection-paper-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.collection-paper-notes {
  font-size: 0.9rem;
  color: #555;
  font-style: italic;
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid #e0e0e0;
}

.remove-paper-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

.remove-paper-btn:hover {
  background: #c0392b;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #999;
}

.empty-state-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}
</style>

<script>
let collections = [];
let allPapers = [];
let currentCollectionId = null;

async function loadData() {
  try {
    // Load papers
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    // Load collections from user data
    const userResponse = await fetch('http://localhost:5001/api/user/data');
    const userData = await userResponse.json();
    collections = userData.collections || [];
    
    renderCollections();
    updateStats();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function renderCollections() {
  const container = document.getElementById('collectionsList');
  
  if (collections.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">📁</div>
        <p>No collections yet. Create your first collection to organize papers!</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = collections.map(collection => {
    const paperCount = collection.papers ? collection.papers.length : 0;
    const tags = collection.tags || [];
    const createdDate = new Date(collection.createdAt).toLocaleDateString();
    
    return `
      <div class="collection-card" style="border-left-color: ${collection.color || '#2c5aa0'}" onclick="openCollectionDetail('${collection.id}')">
        <div class="collection-card-header">
          <h3 class="collection-card-title">${collection.name}</h3>
          <span class="collection-card-count">${paperCount} papers</span>
        </div>
        <p class="collection-card-description">${collection.description || 'No description'}</p>
        <div class="collection-card-tags">
          ${tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
        </div>
        <div class="collection-card-footer">
          <span>Created ${createdDate}</span>
          <span>Last updated ${new Date(collection.updatedAt).toLocaleDateString()}</span>
        </div>
      </div>
    `;
  }).join('');
}

function updateStats() {
  document.getElementById('totalCollections').textContent = collections.length;
  const totalPapers = collections.reduce((sum, c) => sum + (c.papers?.length || 0), 0);
  document.getElementById('totalPapersInCollections').textContent = totalPapers;
}

function openCreateModal() {
  document.getElementById('createCollectionModal').style.display = 'flex';
}

function closeCreateModal() {
  document.getElementById('createCollectionModal').style.display = 'none';
  document.getElementById('collectionName').value = '';
  document.getElementById('collectionDescription').value = '';
  document.getElementById('collectionTags').value = '';
  document.getElementById('collectionColor').value = '#2c5aa0';
}

async function createCollection() {
  const name = document.getElementById('collectionName').value.trim();
  const description = document.getElementById('collectionDescription').value.trim();
  const tags = document.getElementById('collectionTags').value.split(',').map(t => t.trim()).filter(t => t);
  const color = document.getElementById('collectionColor').value;
  
  if (!name) {
    alert('Please enter a collection name');
    return;
  }
  
  const newCollection = {
    id: 'collection_' + Date.now(),
    name,
    description,
    tags,
    color,
    papers: [],
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  };
  
  collections.push(newCollection);
  await saveCollections();
  
  closeCreateModal();
  renderCollections();
  updateStats();
}

async function saveCollections() {
  try {
    const userResponse = await fetch('http://localhost:5001/api/user/data');
    const userData = await userResponse.json();
    userData.collections = collections;
    
    await fetch('http://localhost:5001/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving collections:', error);
  }
}

function openCollectionDetail(collectionId) {
  currentCollectionId = collectionId;
  const collection = collections.find(c => c.id === collectionId);
  
  if (!collection) return;
  
  document.getElementById('detailCollectionName').textContent = collection.name;
  document.getElementById('detailCollectionDescription').textContent = collection.description || 'No description';
  document.getElementById('detailCollectionTags').innerHTML = (collection.tags || []).map(tag => `<span class="tag">${tag}</span>`).join('');
  
  renderCollectionPapers(collection);
  
  document.getElementById('collectionDetailModal').style.display = 'flex';
}

function closeDetailModal() {
  document.getElementById('collectionDetailModal').style.display = 'none';
  document.getElementById('addPapersSection').style.display = 'none';
  currentCollectionId = null;
}

function renderCollectionPapers(collection) {
  const container = document.getElementById('collectionPapersList');
  const papers = collection.papers || [];
  
  document.getElementById('collectionPaperCount').textContent = papers.length;
  
  if (papers.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <p>No papers in this collection yet. Click "Add Papers" to get started!</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = papers.map(item => {
    const paper = allPapers.find(p => p.arxiv_id === item.arxiv_id);
    if (!paper) return '';
    
    return `
      <div class="collection-paper-item">
        <div class="collection-paper-info">
          <div class="collection-paper-title">${paper.title}</div>
          <div class="collection-paper-meta">${paper.authors} • ${paper.date}</div>
          ${item.notes ? `<div class="collection-paper-notes">📝 ${item.notes}</div>` : ''}
        </div>
        <button class="remove-paper-btn" onclick="removePaperFromCollection('${item.arxiv_id}')">Remove</button>
      </div>
    `;
  }).join('');
}

function addPapersToCollection() {
  const section = document.getElementById('addPapersSection');
  section.style.display = section.style.display === 'none' ? 'block' : 'none';
  
  if (section.style.display === 'block') {
    renderPapersForCollection();
  }
}

function renderPapersForCollection(filter = '') {
  const container = document.getElementById('papersList');
  const collection = collections.find(c => c.id === currentCollectionId);
  const existingPaperIds = (collection.papers || []).map(p => p.arxiv_id);
  
  let filteredPapers = allPapers;
  if (filter) {
    const lowerFilter = filter.toLowerCase();
    filteredPapers = allPapers.filter(p => 
      p.title.toLowerCase().includes(lowerFilter) ||
      p.authors.toLowerCase().includes(lowerFilter) ||
      (p.abstract && p.abstract.toLowerCase().includes(lowerFilter))
    );
  }
  
  const availablePapers = filteredPapers.filter(p => !existingPaperIds.includes(p.arxiv_id));
  
  if (availablePapers.length === 0) {
    container.innerHTML = '<p style="text-align: center; color: #999;">No papers available to add</p>';
    return;
  }
  
  container.innerHTML = availablePapers.slice(0, 20).map(paper => `
    <div class="paper-item">
      <div class="paper-item-info">
        <div class="paper-item-title">${paper.title}</div>
        <div class="paper-item-meta">${paper.authors} • ${paper.date}</div>
      </div>
      <button class="btn-secondary" onclick="addPaperToCollection('${paper.arxiv_id}')">Add</button>
    </div>
  `).join('');
}

function filterPapersForCollection() {
  const filter = document.getElementById('paperSearch').value;
  renderPapersForCollection(filter);
}

async function addPaperToCollection(arxivId) {
  const collection = collections.find(c => c.id === currentCollectionId);
  if (!collection) return;
  
  if (!collection.papers) {
    collection.papers = [];
  }
  
  const notes = prompt('Add notes for this paper (optional):');
  
  collection.papers.push({
    arxiv_id: arxivId,
    notes: notes || '',
    addedAt: new Date().toISOString()
  });
  
  collection.updatedAt = new Date().toISOString();
  
  await saveCollections();
  renderCollectionPapers(collection);
  renderPapersForCollection(document.getElementById('paperSearch').value);
  renderCollections();
  updateStats();
}

async function removePaperFromCollection(arxivId) {
  if (!confirm('Remove this paper from the collection?')) return;
  
  const collection = collections.find(c => c.id === currentCollectionId);
  if (!collection) return;
  
  collection.papers = collection.papers.filter(p => p.arxiv_id !== arxivId);
  collection.updatedAt = new Date().toISOString();
  
  await saveCollections();
  renderCollectionPapers(collection);
  renderCollections();
  updateStats();
}

async function deleteCollection() {
  if (!confirm('Are you sure you want to delete this collection? This cannot be undone.')) return;
  
  collections = collections.filter(c => c.id !== currentCollectionId);
  await saveCollections();
  
  closeDetailModal();
  renderCollections();
  updateStats();
}

function exportCollection() {
  const collection = collections.find(c => c.id === currentCollectionId);
  if (!collection) return;
  
  const exportData = {
    name: collection.name,
    description: collection.description,
    tags: collection.tags,
    papers: collection.papers.map(item => {
      const paper = allPapers.find(p => p.arxiv_id === item.arxiv_id);
      return {
        arxiv_id: item.arxiv_id,
        title: paper?.title,
        authors: paper?.authors,
        date: paper?.date,
        notes: item.notes,
        addedAt: item.addedAt
      };
    }),
    exportedAt: new Date().toISOString()
  };
  
  const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${collection.name.replace(/[^a-z0-9]/gi, '_')}_collection.json`;
  a.click();
  URL.revokeObjectURL(url);
}

document.getElementById('createCollectionBtn').addEventListener('click', openCreateModal);

// Initialize
loadData();
</script>
