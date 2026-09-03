/**
 * Knowledge Construction Tab - 5-Stage Learning Cycle
 * Implements the learner-in-the-loop framework from the conference paper
 */

// Global state
let currentStage = 'construct';
let currentConcept = null;
let stageHistory = [];

// Stage definitions
const STAGES = {
  construct: {
    name: 'Construct',
    icon: '✍️',
    description: 'Write your initial explanation',
    color: '#4a90d9'
  },
  reflect: {
    name: 'Reflect',
    icon: '🤔',
    description: 'Examine your understanding',
    color: '#f59e0b'
  },
  scaffold: {
    name: 'Scaffold',
    icon: '🏗️',
    description: 'Get targeted guidance',
    color: '#10b981'
  },
  consolidate: {
    name: 'Consolidate',
    icon: '💪',
    description: 'Apply your knowledge',
    color: '#8b5cf6'
  },
  revisit: {
    name: 'Revisit',
    icon: '🔄',
    description: 'Connect & extend',
    color: '#ec4899'
  }
};

/**
 * Initialize Knowledge Construction tab
 */
function initKnowledgeConstruction() {
  console.log('Initializing Knowledge Construction tab...');
  
  // Load concepts into selector
  loadConceptsForConstruction();
  
  // Set up stage navigation
  setupStageNavigation();
  
  // Initialize sidebar (collapsed by default)
  updateSidebarState();
}

/**
 * Load concepts into the concept selector
 */
async function loadConceptsForConstruction() {
  try {
    const response = await fetch('/api/concepts');
    const concepts = await response.json();
    
    const select = document.getElementById('knowledgeConceptSelect');
    select.innerHTML = '<option value="">-- Select a Concept --</option>';
    
    concepts.forEach(concept => {
      const option = document.createElement('option');
      option.value = concept.id;
      option.textContent = concept.name;
      select.appendChild(option);
    });
    
    // Add change listener
    select.addEventListener('change', handleConceptSelection);
    
  } catch (error) {
    console.error('Error loading concepts:', error);
    showError('Failed to load concepts. Please try again.');
  }
}

/**
 * Handle concept selection
 */
function handleConceptSelection(event) {
  const conceptId = event.target.value;
  
  if (!conceptId) {
    currentConcept = null;
    hideStageContent();
    showWelcomeMessage();
    return;
  }
  
  currentConcept = conceptId;
  stageHistory = ['construct'];
  currentStage = 'construct';
  
  // Hide welcome message and show stage content
  hideWelcomeMessage();
  showStageContent();
  
  // Update stage progress
  updateStageProgress();
  
  // Render current stage
  renderCurrentStage();
}

/**
 * Set up stage navigation (arrow diagram)
 */
function setupStageNavigation() {
  const arrows = document.querySelectorAll('.stage-arrow');
  
  arrows.forEach(arrow => {
    arrow.addEventListener('click', () => {
      const stage = arrow.dataset.stage;
      
      // Recursive workflow: allow access to any stage
      navigateToStage(stage);
    });
  });
}

/**
 * Navigate to a specific stage
 */
function navigateToStage(stage) {
  if (!currentConcept) {
    showNotification('Please select a concept first.', 'warning');
    return;
  }
  
  currentStage = stage;
  
  // Add to history if not already there
  if (!stageHistory.includes(stage)) {
    stageHistory.push(stage);
  }
  
  // Update UI
  updateStageProgress();
  updateSidebarMode(stage);
  renderCurrentStage();
}

/**
 * Check if a stage is accessible
 */
function canAccessStage(stage) {
  // Recursive workflow: allow access to ANY stage at any time
  // This matches the paper's framework where learners can return to earlier stages
  // when reflection reveals gaps or application exposes misconceptions
  return true;
}

/**
 * Update stage progress indicators
 */
function updateStageProgress() {
  const arrows = document.querySelectorAll('.stage-arrow');
  
  arrows.forEach(arrow => {
    const stage = arrow.dataset.stage;
    const stageIndex = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'].indexOf(stage);
    const currentIndex = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'].indexOf(currentStage);
    
    // Remove all state classes
    arrow.classList.remove('active', 'completed');
    
    // Add appropriate class
    if (stage === currentStage) {
      arrow.classList.add('active');
    } else if (stageHistory.includes(stage)) {
      arrow.classList.add('completed');
    }
  });
}

/**
 * Render current stage content
 */
function renderCurrentStage() {
  const contentDiv = document.getElementById('stageContent');
  
  switch (currentStage) {
    case 'construct':
      renderConstructStage(contentDiv);
      break;
    case 'reflect':
      renderReflectStage(contentDiv);
      break;
    case 'scaffold':
      renderScaffoldStage(contentDiv);
      break;
    case 'consolidate':
      renderConsolidateStage(contentDiv);
      break;
    case 'revisit':
      renderRevisitStage(contentDiv);
      break;
  }
}

/**
 * Render Construct stage
 */
function renderConstructStage(contentDiv) {
  contentDiv.innerHTML = `
    <div class="stage-header">
      <h3>${STAGES.construct.icon} ${STAGES.construct.name}</h3>
      <p>Write your initial explanation of the concept in your own words. Don't worry about being perfect - this is your starting point for learning.</p>
    </div>
    
    <div class="stage-body">
      <label for="constructExplanation">Your Explanation:</label>
      <textarea id="constructExplanation" class="stage-textarea learner-content" placeholder="Explain the concept in your own words..."></textarea>
      
      <div id="promptResponse"></div>
      
      <div class="stage-actions">
        <button onclick="saveConstructAndContinue()" class="btn-primary">
          Save & Proceed
        </button>
        <button onclick="saveConstructOnly()" class="btn-secondary">
          Save Only
        </button>
        <button onclick="askForHelp('construct')" class="btn-tertiary">
          💬 Need help?
        </button>
      </div>
    </div>
  `;
  
  // Load existing explanation if any
  loadExistingExplanation('construct');
}

/**
 * Render Reflect stage
 */
function renderReflectStage(contentDiv) {
  contentDiv.innerHTML = `
    <div class="stage-header">
      <h3>${STAGES.reflect.icon} ${STAGES.reflect.name}</h3>
      <p>Examine your explanation. What are you confident about? What seems unclear? This metacognitive reflection helps you identify gaps in your understanding.</p>
    </div>
    
    <div class="stage-body">
      <div id="reflectionPrompts" class="reflection-prompts">
        <p class="loading">Generating reflection prompts...</p>
      </div>
      
      <label for="reflectionNotes">Your Reflection Notes:</label>
      <textarea id="reflectionNotes" class="stage-textarea learner-content" placeholder="What did you discover about your understanding?"></textarea>
      
      <div id="promptResponse"></div>
      
      <div class="stage-actions">
        <button onclick="saveReflectionAndContinue()" class="btn-primary">
          Save & Proceed
        </button>
        <button onclick="saveReflectionOnly()" class="btn-secondary">
          Save Only
        </button>
        <button onclick="navigateToStage('construct')" class="btn-tertiary">
          ← Return to Construct
        </button>
        <button onclick="askForHelp('reflect')" class="btn-tertiary">
          💬 Need help?
        </button>
      </div>
    </div>
  `;
  
  // Generate reflection prompts
  generateReflectionPrompts();
  
  // Load existing reflection if any
  loadExistingExplanation('reflect');
}

/**
 * Render Scaffold stage
 */
function renderScaffoldStage(contentDiv) {
  contentDiv.innerHTML = `
    <div class="stage-header">
      <h3>${STAGES.scaffold.icon} ${STAGES.scaffold.name}</h3>
      <p>Based on your reflection, the AI will provide targeted guidance to help fill knowledge gaps. Review the suggestions and update your explanation.</p>
    </div>
    
    <div class="stage-body">
      <div id="scaffoldSuggestions" class="scaffold-suggestions">
        <p class="loading">Generating scaffold suggestions...</p>
      </div>
      
      <label for="scaffoldRevision">Revised Explanation:</label>
      <textarea id="scaffoldRevision" class="stage-textarea learner-content" placeholder="Update your explanation based on the guidance..."></textarea>
      
      <div id="promptResponse"></div>
      
      <div class="stage-actions">
        <button onclick="saveScaffoldAndContinue()" class="btn-primary">
          Save & Proceed
        </button>
        <button onclick="saveScaffoldOnly()" class="btn-secondary">
          Save Only
        </button>
        <button onclick="navigateToStage('reflect')" class="btn-tertiary">
          ← Return to Reflect
        </button>
        <button onclick="askForHelp('scaffold')" class="btn-tertiary">
          💬 Need help?
        </button>
      </div>
    </div>
  `;
  
  // Generate scaffold suggestions
  generateScaffoldSuggestions();
  
  // Load existing revision if any
  loadExistingExplanation('scaffold');
}

/**
 * Render Consolidate stage
 */
function renderConsolidateStage(contentDiv) {
  contentDiv.innerHTML = `
    <div class="stage-header">
      <h3>${STAGES.consolidate.icon} ${STAGES.consolidate.name}</h3>
      <p>Apply your knowledge to a new scenario or problem. This helps you test your understanding and transfer learning to new contexts.</p>
    </div>
    
    <div class="stage-body">
      <div id="consolidateTask" class="consolidate-task">
        <p class="loading">Generating application task...</p>
      </div>
      
      <label for="consolidateResponse">Your Response:</label>
      <textarea id="consolidateResponse" class="stage-textarea learner-content" placeholder="Apply the concept to the scenario..."></textarea>
      
      <div id="promptResponse"></div>
      
      <div class="stage-actions">
        <button onclick="saveConsolidateAndContinue()" class="btn-primary">
          Save & Proceed
        </button>
        <button onclick="saveConsolidateOnly()" class="btn-secondary">
          Save Only
        </button>
        <button onclick="navigateToStage('scaffold')" class="btn-tertiary">
          ← Return to Scaffold
        </button>
        <button onclick="askForHelp('consolidate')" class="btn-tertiary">
          💬 Need help?
        </button>
      </div>
    </div>
  `;
  
  // Generate consolidation task
  generateConsolidateTask();
  
  // Load existing response if any
  loadExistingExplanation('consolidate');
}

/**
 * Render Revisit stage
 */
function renderRevisitStage(contentDiv) {
  contentDiv.innerHTML = `
    <div class="stage-header">
      <h3>${STAGES.revisit.icon} ${STAGES.revisit.name}</h3>
      <p>Connect this concept to your prior knowledge. How does it relate to other concepts you've learned? What questions remain?</p>
    </div>
    
    <div class="stage-body">
      <div class="concept-graph-container">
        <h4>🔗 Concept Connections</h4>
        <div id="miniConceptGraph" class="mini-concept-graph">
          <p class="loading">Loading concept graph...</p>
        </div>
      </div>
      
      <div id="revisitConnections" class="revisit-connections">
        <p class="loading">Generating connection suggestions...</p>
      </div>
      
      <label for="revisitNotes">Your Connections & Questions:</label>
      <textarea id="revisitNotes" class="stage-textarea learner-content" placeholder="How does this connect to other concepts? What questions remain?"></textarea>
      
      <div id="promptResponse"></div>
      
      <div class="stage-actions">
        <button onclick="saveRevisit()" class="btn-primary">
          Save & Complete Cycle ✓
        </button>
        <button onclick="navigateToStage('consolidate')" class="btn-tertiary">
          ← Return to Consolidate
        </button>
        <button onclick="askForHelp('revisit')" class="btn-tertiary">
          💬 Need help?
        </button>
      </div>
    </div>
  `;
  
  // Generate mini concept graph
  renderMiniConceptGraph();
  
  // Generate connection suggestions
  generateRevisitConnections();
  
  // Load existing notes if any
  loadExistingExplanation('revisit');
}

/**
 * Revision History Tracking
 */
let revisionHistory = [];

/**
 * Save explanation with history tracking and progress update
 */
async function saveExplanation(stage, content) {
  try {
    const response = await fetch('/api/wiki/construct', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept,
        stage: stage,
        content: content,
        timestamp: new Date().toISOString()
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to save explanation');
    }
    
    // Track revision in history
    addRevisionToHistory(stage, content);
    
    // Update progress
    updateStageCompletion(stage);
    await saveProgress();
    
    // Show save feedback
    showSaveFeedback(stage);
    
    showNotification('Saved successfully!', 'success');
    return true;
    
  } catch (error) {
    console.error('Error saving explanation:', error);
    showError('Failed to save. Please try again.');
    return false;
  }
}

/**
 * Show save feedback animation
 */
function showSaveFeedback(stage) {
  const saveButton = document.querySelector('.stage-actions .btn-primary');
  if (!saveButton) return;
  
  const originalText = saveButton.textContent;
  const originalClass = saveButton.className;
  
  // Show saving state
  saveButton.disabled = true;
  saveButton.innerHTML = '<span class="spinner"></span> Saving...';
  saveButton.classList.add('saving');
  
  // Show success after brief delay
  setTimeout(() => {
    saveButton.innerHTML = '✓ Saved!';
    saveButton.classList.remove('saving');
    saveButton.classList.add('success');
    
    // Restore button after 2 seconds
    setTimeout(() => {
      saveButton.innerHTML = originalText;
      saveButton.className = originalClass;
      saveButton.disabled = false;
    }, 2000);
  }, 500);
}

/**
 * Progress Tracking
 */
let stageCompletionStatus = {
  construct: false,
  reflect: false,
  scaffold: false,
  consolidate: false,
  revisit: false
};

/**
 * Update stage completion status
 */
function updateStageCompletion(stage) {
  stageCompletionStatus[stage] = true;
  updateProgressDisplay();
}

/**
 * Calculate overall progress
 */
function calculateProgress() {
  const completedStages = Object.values(stageCompletionStatus).filter(status => status).length;
  const totalStages = Object.keys(stageCompletionStatus).length;
  return Math.round((completedStages / totalStages) * 100);
}

/**
 * Update progress display
 */
function updateProgressDisplay() {
  const progressPercentage = calculateProgress();
  const progressBar = document.getElementById('progressBar');
  const progressText = document.getElementById('progressText');
  const progressStats = document.getElementById('progressStats');
  
  if (progressBar) {
    progressBar.style.width = `${progressPercentage}%`;
    progressBar.textContent = `${progressPercentage}%`;
  }
  
  if (progressText) {
    progressText.textContent = `${progressPercentage}% Complete`;
  }
  
  if (progressStats) {
    const completed = Object.values(stageCompletionStatus).filter(s => s).length;
    const total = Object.keys(stageCompletionStatus).length;
    progressStats.textContent = `${completed} of ${total} stages completed`;
  }
  
  // Update stage indicators
  updateStageIndicators();
}

/**
 * Update stage completion indicators
 */
function updateStageIndicators() {
  const indicators = document.querySelectorAll('.stage-indicator');
  
  indicators.forEach(indicator => {
    const stage = indicator.dataset.stage;
    indicator.classList.remove('pending', 'in-progress', 'completed');
    
    if (stageCompletionStatus[stage]) {
      indicator.classList.add('completed');
      indicator.textContent = `✓ ${STAGES[stage]?.name || stage}`;
    } else if (stage === currentStage) {
      indicator.classList.add('in-progress');
      indicator.textContent = `→ ${STAGES[stage]?.name || stage}`;
    } else {
      indicator.classList.add('pending');
      indicator.textContent = `○ ${STAGES[stage]?.name || stage}`;
    }
  });
  
  // Update mastery chart if it exists
  updateMasteryChart();
}

/**
 * Render mastery progression chart (SVG-based)
 */
function updateMasteryChart() {
  const container = document.getElementById('masteryChart');
  if (!container) return;
  
  const stages = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
  const stageColors = {
    construct: '#4a90d9',
    reflect: '#f59e0b',
    scaffold: '#10b981',
    consolidate: '#8b5cf6',
    revisit: '#ec4899'
  };
  
  const width = 400;
  const height = 120;
  const barWidth = 60;
  const barGap = 15;
  const startX = 30;
  
  let svg = `<svg width="${width}" height="${height}" class="mastery-chart-svg">`;
  
  // Y-axis
  svg += `<line x1="${startX}" y1="10" x2="${startX}" y2="${height - 25}" stroke="#cbd5e1" stroke-width="1"/>`;
  svg += `<text x="${startX - 5}" y="${height - 15}" text-anchor="end" fill="#94a3b8" font-size="9">0%</text>`;
  svg += `<text x="${startX - 5}" y="15" text-anchor="end" fill="#94a3b8" font-size="9">100%</text>`;
  
  stages.forEach((stage, index) => {
    const x = startX + 10 + index * (barWidth + barGap);
    const completed = stageCompletionStatus[stage];
    const isActive = stage === currentStage;
    const barHeight = completed ? (height - 40) : (isActive ? (height - 40) * 0.5 : 0);
    const y = height - 25 - barHeight;
    const color = stageColors[stage];
    
    // Bar
    if (barHeight > 0) {
      svg += `<rect x="${x}" y="${y}" width="${barWidth}" height="${barHeight}" 
              fill="${color}" rx="4" opacity="${completed ? 1 : 0.6}" class="mastery-bar">
              <title>${STAGES[stage].name}: ${completed ? 'Complete' : 'In Progress'}</title>
            </rect>`;
    } else {
      // Empty bar outline
      svg += `<rect x="${x}" y="10" width="${barWidth}" height="${height - 35}" 
              fill="none" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3" rx="4"/>`;
    }
    
    // Label
    svg += `<text x="${x + barWidth / 2}" y="${height - 8}" text-anchor="middle" 
            fill="#64748b" font-size="9" font-weight="${isActive ? 'bold' : 'normal'}">
            ${STAGES[stage].icon} ${STAGES[stage].name}
            </text>`;
    
    // Status icon
    if (completed) {
      svg += `<text x="${x + barWidth / 2}" y="${y - 5}" text-anchor="middle" fill="${color}" font-size="12">✓</text>`;
    } else if (isActive) {
      svg += `<text x="${x + barWidth / 2}" y="${y - 5}" text-anchor="middle" fill="${color}" font-size="12">→</text>`;
    }
  });
  
  svg += '</svg>';
  container.innerHTML = svg;
}

/**
 * Render timeline visualization for revision history
 */
function renderRevisionTimeline() {
  const container = document.getElementById('revisionHistory');
  if (!container) return;
  
  if (revisionHistory.length === 0) {
    container.innerHTML = '<p class="no-revisions">No revisions yet. Start writing to see your progress!</p>';
    return;
  }
  
  const stageColors = {
    construct: '#4a90d9',
    reflect: '#f59e0b',
    scaffold: '#10b981',
    consolidate: '#8b5cf6',
    revisit: '#ec4899'
  };
  
  // Group revisions by date
  const byDate = {};
  revisionHistory.forEach(rev => {
    const date = new Date(rev.timestamp).toLocaleDateString();
    if (!byDate[date]) byDate[date] = [];
    byDate[date].push(rev);
  });
  
  const dates = Object.keys(byDate).sort((a, b) => new Date(b) - new Date(a));
  
  let html = '<div class="revision-timeline-vertical">';
  
  dates.forEach((date, dateIndex) => {
    const revisions = byDate[date];
    html += `<div class="timeline-date-group">`;
    html += `<div class="timeline-date-marker">${date}</div>`;
    
    revisions.forEach((rev, revIndex) => {
      const time = new Date(rev.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      const color = stageColors[rev.stage] || '#64748b';
      const stageInfo = STAGES[rev.stage];
      const preview = truncateText(rev.content || '', 80);
      
      html += `
        <div class="timeline-entry" data-revision-id="${rev.id}">
          <div class="timeline-connector" style="background: ${color};"></div>
          <div class="timeline-dot" style="background: ${color};"></div>
          <div class="timeline-card">
            <div class="timeline-card-header">
              <span class="timeline-stage-badge" style="background: ${color};">
                ${stageInfo?.icon || '📝'} ${stageInfo?.name || rev.stage}
              </span>
              <span class="timeline-time">${time}</span>
            </div>
            <div class="timeline-card-body">${preview}</div>
            <div class="timeline-card-actions">
              <button class="btn-timeline-view" onclick="viewRevision(${rev.id})">View</button>
            </div>
          </div>
        </div>
      `;
    });
    
    html += `</div>`;
  });
  
  html += '</div>';
  
  // Add summary stats
  const totalRevisions = revisionHistory.length;
  const uniqueStages = new Set(revisionHistory.map(r => r.stage)).size;
  const firstRevision = new Date(revisionHistory[0]?.timestamp);
  const lastRevision = new Date(revisionHistory[revisionHistory.length - 1]?.timestamp);
  const daysActive = Math.max(1, Math.ceil((lastRevision - firstRevision) / 86400000));
  
  html = `
    <div class="timeline-stats">
      <div class="timeline-stat">
        <span class="stat-number">${totalRevisions}</span>
        <span class="stat-desc">Total revisions</span>
      </div>
      <div class="timeline-stat">
        <span class="stat-number">${uniqueStages}</span>
        <span class="stat-desc">Stages active</span>
      </div>
      <div class="timeline-stat">
        <span class="stat-number">${daysActive}</span>
        <span class="stat-desc">Day${daysActive > 1 ? 's' : ''} active</span>
      </div>
    </div>
  ` + html;
  
  container.innerHTML = html;
}

/**
 * Load progress from API
 */
async function loadProgress() {
  try {
    const response = await fetch(`/api/wiki/progress?concept=${currentConcept}`);
    
    if (!response.ok) {
      return;
    }
    
    const data = await response.json();
    
    if (data.stages) {
      stageCompletionStatus = { ...stageCompletionStatus, ...data.stages };
      updateProgressDisplay();
    }
    
  } catch (error) {
    console.error('Error loading progress:', error);
  }
}

/**
 * Save progress to API
 */
async function saveProgress() {
  try {
    await fetch('/api/wiki/progress', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept,
        stages: stageCompletionStatus,
        timestamp: new Date().toISOString()
      })
    });
  } catch (error) {
    console.error('Error saving progress:', error);
  }
}

/**
 * Add revision to history
 */
function addRevisionToHistory(stage, content) {
  const revision = {
    id: Date.now(),
    stage: stage,
    content: content,
    timestamp: new Date().toISOString(),
    concept: currentConcept
  };
  
  revisionHistory.push(revision);
  
  // Keep only last 50 revisions
  if (revisionHistory.length > 50) {
    revisionHistory = revisionHistory.slice(-50);
  }
  
  // Update revision history display
  updateRevisionHistoryDisplay();
}

/**
 * Load revision history from API
 */
async function loadRevisionHistory() {
  try {
    const response = await fetch(`/api/wiki/revisions?concept=${currentConcept}`);
    
    if (!response.ok) {
      return;
    }
    
    const data = await response.json();
    revisionHistory = data.revisions || [];
    updateRevisionHistoryDisplay();
    
  } catch (error) {
    console.error('Error loading revision history:', error);
  }
}

/**
 * Update revision history display
 */
function updateRevisionHistoryDisplay() {
  const container = document.getElementById('revisionHistory');
  if (!container) return;
  
  if (revisionHistory.length === 0) {
    container.innerHTML = '<p class="no-revisions">No revisions yet. Start writing to see your progress!</p>';
    return;
  }
  
  const recentRevisions = revisionHistory.slice(-10).reverse();
  
  container.innerHTML = `
    <div class="revision-timeline">
      ${recentRevisions.map((rev, index) => `
        <div class="revision-item" data-revision-id="${rev.id}">
          <div class="revision-header">
            <span class="revision-stage">${STAGES[rev.stage]?.icon || '📝'} ${STAGES[rev.stage]?.name || rev.stage}</span>
            <span class="revision-time">${formatTimeAgo(rev.timestamp)}</span>
          </div>
          <div class="revision-preview">
            ${truncateText(rev.content, 100)}
          </div>
          <div class="revision-actions">
            <button onclick="viewRevision(${rev.id})" class="btn-small">View</button>
            ${index > 0 ? `<button onclick="compareRevisions(${rev.id}, ${recentRevisions[index-1].id})" class="btn-small">Compare</button>` : ''}
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

/**
 * View a specific revision
 */
function viewRevision(revisionId) {
  const revision = revisionHistory.find(r => r.id === revisionId);
  if (!revision) return;
  
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content">
      <div class="modal-header">
        <h3>Revision from ${formatTimeAgo(revision.timestamp)}</h3>
        <button onclick="closeModal()" class="btn-close">×</button>
      </div>
      <div class="modal-body">
        <div class="revision-stage-badge">
          ${STAGES[revision.stage]?.icon || '📝'} ${STAGES[revision.stage]?.name || revision.stage}
        </div>
        <div class="revision-content">
          ${revision.content}
        </div>
      </div>
      <div class="modal-footer">
        <button onclick="restoreRevision(${revision.id})" class="btn-primary">Restore This Version</button>
        <button onclick="closeModal()" class="btn-secondary">Close</button>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  modal.classList.add('active');
}

/**
 * Compare two revisions
 */
function compareRevisions(revId1, revId2) {
  const rev1 = revisionHistory.find(r => r.id === revId1);
  const rev2 = revisionHistory.find(r => r.id === revId2);
  
  if (!rev1 || !rev2) return;
  
  const diff = generateDiff(rev2.content, rev1.content);
  
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content modal-large">
      <div class="modal-header">
        <h3>Revision Comparison</h3>
        <button onclick="closeModal()" class="btn-close">×</button>
      </div>
      <div class="modal-body">
        <div class="diff-view">
          <div class="diff-header">
            <span class="diff-from">From: ${formatTimeAgo(rev2.timestamp)}</span>
            <span class="diff-to">To: ${formatTimeAgo(rev1.timestamp)}</span>
          </div>
          <div class="diff-content">
            ${diff}
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button onclick="closeModal()" class="btn-secondary">Close</button>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  modal.classList.add('active');
}

/**
 * Generate diff between two texts
 */
function generateDiff(oldText, newText) {
  const oldLines = oldText.split('\n');
  const newLines = newText.split('\n');
  
  let diffHtml = '';
  const maxLines = Math.max(oldLines.length, newLines.length);
  
  for (let i = 0; i < maxLines; i++) {
    const oldLine = oldLines[i] || '';
    const newLine = newLines[i] || '';
    
    if (oldLine === newLine) {
      diffHtml += `<div class="diff-line diff-unchanged">${escapeHtml(oldLine)}</div>`;
    } else {
      if (oldLine) {
        diffHtml += `<div class="diff-line diff-removed">- ${escapeHtml(oldLine)}</div>`;
      }
      if (newLine) {
        diffHtml += `<div class="diff-line diff-added">+ ${escapeHtml(newLine)}</div>`;
      }
    }
  }
  
  return diffHtml || '<p class="no-changes">No changes detected</p>';
}

/**
 * Restore a revision
 */
function restoreRevision(revisionId) {
  const revision = revisionHistory.find(r => r.id === revisionId);
  if (!revision) return;
  
  if (confirm('Are you sure you want to restore this version? This will replace your current content.')) {
    // Navigate to the stage
    navigateToStage(revision.stage);
    
    // Wait for stage to render, then populate
    setTimeout(() => {
      const textarea = document.querySelector(`#${revision.stage}Explanation, #${revision.stage}Notes, #${revision.stage}Revision, #${revision.stage}Response`);
      if (textarea) {
        textarea.value = revision.content;
        showNotification('Revision restored!', 'success');
      }
    }, 100);
    
    closeModal();
  }
}

/**
 * Close modal
 */
function closeModal() {
  const modal = document.querySelector('.modal.active');
  if (modal) {
    modal.classList.remove('active');
    setTimeout(() => modal.remove(), 300);
  }
}

/**
 * Format time ago
 */
function formatTimeAgo(timestamp) {
  const date = new Date(timestamp);
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);
  
  if (diffMins < 1) return 'just now';
  if (diffMins < 60) return `${diffMins} min ago`;
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
  
  return date.toLocaleDateString();
}

/**
 * Truncate text
 */
function truncateText(text, maxLength) {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
}

/**
 * Escape HTML
 */
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/**
 * Load existing explanation for a stage
 */
async function loadExistingExplanation(stage) {
  try {
    const response = await fetch(`/api/wiki/entries?concept=${currentConcept}&stage=${stage}`);
    
    if (!response.ok) {
      return;
    }
    
    const data = await response.json();
    
    if (data.entries && data.entries.length > 0) {
      const latestEntry = data.entries[data.entries.length - 1];
      const textarea = document.querySelector(`#${stage}Explanation, #${stage}Notes, #${stage}Revision, #${stage}Response`);
      
      if (textarea) {
        textarea.value = latestEntry.content;
      }
    }
    
  } catch (error) {
    console.error('Error loading explanation:', error);
  }
}

/**
 * Prompt Before Provide - Core mechanism from the paper
 * Implements hierarchical response: metacognitive prompts → scaffolded hints → direct answer
 */
async function promptBeforeProvide(stage, query) {
  const promptLevels = {
    1: 'metacognitive',    // Ask reflection questions
    2: 'scaffolded',       // Provide hints and guidance
    3: 'direct'           // Give direct answer
  };
  
  // Get current prompt level from user preference or default to 1
  const currentLevel = getUserPromptLevel() || 1;
  
  try {
    const response = await fetch('/api/wiki/prompt-before-provide', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept,
        stage: stage,
        query: query,
        level: promptLevels[currentLevel]
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to generate prompt');
    }
    
    const data = await response.json();
    return {
      level: currentLevel,
      response: data.response,
      nextLevelAvailable: currentLevel < 3
    };
    
  } catch (error) {
    console.error('Error in prompt before provide:', error);
    return {
      level: currentLevel,
      response: 'Unable to generate response. Please try again.',
      nextLevelAvailable: false
    };
  }
}

/**
 * Get user's preferred prompt level
 */
function getUserPromptLevel() {
  const saved = localStorage.getItem('promptLevel');
  return saved ? parseInt(saved) : 1;
}

/**
 * Set user's prompt level preference
 */
function setUserPromptLevel(level) {
  localStorage.setItem('promptLevel', level.toString());
  showNotification(`Prompt level set to ${level}`, 'info');
}

/**
 * Request next level of help
 */
async function requestMoreHelp(stage, query) {
  const currentLevel = getUserPromptLevel();
  if (currentLevel < 3) {
    setUserPromptLevel(currentLevel + 1);
    const result = await promptBeforeProvide(stage, query);
    displayPromptResponse(result);
  } else {
    showNotification('You\'re already at the most direct help level.', 'info');
  }
}

/**
 * Display prompt response with level indicator
 */
function displayPromptResponse(result) {
  const container = document.getElementById('promptResponse');
  if (!container) return;
  
  const levelNames = {
    1: '💭 Metacognitive Prompt',
    2: '💡 Scaffolded Hint',
    3: '✓ Direct Answer'
  };
  
  container.innerHTML = `
    <div class="prompt-response">
      <div class="prompt-level-indicator">
        <span class="level-badge level-${result.level}">${levelNames[result.level]}</span>
        ${result.nextLevelAvailable ? `<button onclick="requestMoreHelp('${currentStage}', '${currentConcept}')" class="btn-more-help">Need more help? →</button>` : ''}
      </div>
      <div class="prompt-content">
        ${result.response}
      </div>
    </div>
  `;
}

/**
 * Ask for help - integrates Prompt Before Provide
 * Called when user clicks "Need help?" button
 */
async function askForHelp(stage) {
  if (!currentConcept) {
    showNotification('Please select a concept first.', 'warning');
    return;
  }
  
  // Reset prompt level for new help request
  setUserPromptLevel(1);
  
  // Get context about what user needs help with
  let query = '';
  const textarea = document.querySelector(`#${stage}Explanation, #${stage}Notes, #${stage}Revision, #${stage}Response`);
  if (textarea && textarea.value) {
    query = textarea.value.substring(0, 500); // First 500 chars for context
  }
  
  // Show loading state
  const container = document.getElementById('promptResponse');
  if (container) {
    container.innerHTML = '<div class="prompt-response"><div class="spinner"></div> Generating helpful response...</div>';
  }
  
  // Call Prompt Before Provide
  const result = await promptBeforeProvide(stage, query);
  displayPromptResponse(result);
}

/**
 * Generate reflection prompts
 */
async function generateReflectionPrompts() {
  try {
    const explanation = document.getElementById('constructExplanation')?.value || '';
    
    const response = await fetch('/api/wiki/reflect', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept,
        explanation: explanation
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to generate prompts');
    }
    
    const data = await response.json();
    displayReflectionPrompts(data.prompts || []);
    
  } catch (error) {
    console.error('Error generating reflection prompts:', error);
    document.getElementById('reflectionPrompts').innerHTML = '<p class="error">Failed to generate prompts. Please try again.</p>';
  }
}

/**
 * Display reflection prompts
 */
function displayReflectionPrompts(prompts) {
  const container = document.getElementById('reflectionPrompts');
  
  if (prompts.length === 0) {
    container.innerHTML = '<p>No prompts available. Try reflecting on your explanation.</p>';
    return;
  }
  
  container.innerHTML = `
    <h4>Reflection Questions:</h4>
    <ul class="prompt-list">
      ${prompts.map(prompt => `<li>${prompt}</li>`).join('')}
    </ul>
  `;
}

/**
 * Generate scaffold suggestions
 */
async function generateScaffoldSuggestions() {
  try {
    const reflection = document.getElementById('reflectionNotes')?.value || '';
    
    const response = await fetch('/api/wiki/scaffold', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept,
        reflection: reflection
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to generate suggestions');
    }
    
    const data = await response.json();
    displayScaffoldSuggestions(data.suggestions || []);
    
  } catch (error) {
    console.error('Error generating scaffold suggestions:', error);
    document.getElementById('scaffoldSuggestions').innerHTML = '<p class="error">Failed to generate suggestions. Please try again.</p>';
  }
}

/**
 * Display scaffold suggestions
 */
function displayScaffoldSuggestions(suggestions) {
  const container = document.getElementById('scaffoldSuggestions');

  if (suggestions.length === 0) {
    container.innerHTML = '<p>No suggestions available. Review your reflection and try again.</p>';
    return;
  }

  container.innerHTML = `
    <h4>🤖 AI Suggestions:</h4>
    <div class="suggestion-list">
      ${suggestions.map((suggestion, index) => `
        <div class="ai-suggestion" data-suggestion-index="${index}">
          <div class="suggestion-content">${suggestion}</div>
          <div class="ai-suggestion-actions">
            <button class="btn-accept" onclick="acceptSuggestion(${index})">✓ Accept</button>
            <button class="btn-modify" onclick="modifySuggestion(${index})">✏️ Modify</button>
            <button class="btn-reject" onclick="rejectSuggestion(${index})">✗ Reject</button>
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

/**
 * Accept an AI suggestion
 */
function acceptSuggestion(index) {
  const suggestionDiv = document.querySelector(`[data-suggestion-index="${index}"]`);
  const suggestionText = suggestionDiv.querySelector('.suggestion-content').textContent;
  const textarea = document.getElementById('scaffoldRevision');
  
  // Append to current revision
  if (textarea.value) {
    textarea.value += '\n\n' + suggestionText;
  } else {
    textarea.value = suggestionText;
  }
  
  // Mark as accepted
  suggestionDiv.classList.add('accepted');
  suggestionDiv.querySelector('.ai-suggestion-actions').innerHTML = '<span class="accepted-label">✓ Accepted</span>';
  
  showNotification('Suggestion accepted and added to your revision', 'success');
}

/**
 * Modify an AI suggestion
 */
function modifySuggestion(index) {
  const suggestionDiv = document.querySelector(`[data-suggestion-index="${index}"]`);
  const suggestionText = suggestionDiv.querySelector('.suggestion-content').textContent;
  
  // Create editable textarea
  suggestionDiv.innerHTML = `
    <textarea class="suggestion-edit" rows="4">${suggestionText}</textarea>
    <div class="ai-suggestion-actions">
      <button class="btn-accept" onclick="saveModifiedSuggestion(${index})">✓ Save</button>
      <button class="btn-reject" onclick="cancelModifySuggestion(${index})">Cancel</button>
    </div>
  `;
  
  suggestionDiv.querySelector('.suggestion-edit').focus();
}

/**
 * Save modified suggestion
 */
function saveModifiedSuggestion(index) {
  const suggestionDiv = document.querySelector(`[data-suggestion-index="${index}"]`);
  const editedText = suggestionDiv.querySelector('.suggestion-edit').value;
  const textarea = document.getElementById('scaffoldRevision');
  
  // Append modified text to revision
  if (textarea.value) {
    textarea.value += '\n\n' + editedText;
  } else {
    textarea.value = editedText;
  }
  
  suggestionDiv.classList.add('accepted');
  suggestionDiv.innerHTML = `<div class="suggestion-content">${editedText}</div><span class="accepted-label">✓ Modified & Accepted</span>`;
  
  showNotification('Modified suggestion added to your revision', 'success');
}

/**
 * Cancel modification
 */
function cancelModifySuggestion(index) {
  // Re-render the suggestion (simplified - just reload the stage)
  renderScaffoldStage(document.getElementById('stageContent'));
}

/**
 * Reject an AI suggestion
 */
function rejectSuggestion(index) {
  const suggestionDiv = document.querySelector(`[data-suggestion-index="${index}"]`);
  suggestionDiv.classList.add('rejected');
  suggestionDiv.querySelector('.ai-suggestion-actions').innerHTML = '<span class="rejected-label">✗ Rejected</span>';
  
  showNotification('Suggestion rejected', 'info');
}

/**
 * Generate consolidation task
 */
async function generateConsolidateTask() {
  try {
    const response = await fetch('/api/wiki/consolidate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to generate task');
    }
    
    const data = await response.json();
    displayConsolidateTask(data.task || 'Apply this concept to a real-world scenario.');
    
  } catch (error) {
    console.error('Error generating consolidation task:', error);
    document.getElementById('consolidateTask').innerHTML = '<p class="error">Failed to generate task. Please try again.</p>';
  }
}

/**
 * Display consolidation task
 */
function displayConsolidateTask(task) {
  const container = document.getElementById('consolidateTask');
  container.innerHTML = `
    <h4>Application Task:</h4>
    <div class="task-box">
      <p>${task}</p>
    </div>
  `;
}

/**
 * Generate revisit connections
 */
async function generateRevisitConnections() {
  try {
    const response = await fetch('/api/wiki/revisit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        concept: currentConcept
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to generate connections');
    }
    
    const data = await response.json();
    displayRevisitConnections(data.connections || []);
    
  } catch (error) {
    console.error('Error generating connections:', error);
    document.getElementById('revisitConnections').innerHTML = '<p class="error">Failed to generate connections. Please try again.</p>';
  }
}

/**
 * Render mini concept graph for Revisit stage
 */
async function renderMiniConceptGraph() {
  const container = document.getElementById('miniConceptGraph');
  if (!container) return;
  
  try {
    const response = await fetch(`/api/wiki/concept-graph?concept=${currentConcept}&depth=1`);
    
    if (!response.ok) {
      throw new Error('Failed to load concept graph');
    }
    
    const data = await response.json();
    const graph = data.graph || { nodes: [], edges: [] };
    
    if (graph.nodes.length === 0) {
      container.innerHTML = '<p class="no-graph">No concept connections found yet. Complete more stages to build connections!</p>';
      return;
    }
    
    // Render simple SVG graph
    const svg = createMiniGraphSVG(graph);
    container.innerHTML = svg;
    
  } catch (error) {
    console.error('Error rendering concept graph:', error);
    container.innerHTML = '<p class="error">Failed to load concept graph. Please try again.</p>';
  }
}

/**
 * Create SVG visualization of mini concept graph
 */
function createMiniGraphSVG(graph) {
  const width = 400;
  const height = 300;
  const centerX = width / 2;
  const centerY = height / 2;
  
  // Position current concept in center
  const currentConceptNode = graph.nodes.find(n => n.id === currentConcept);
  if (!currentConceptNode) return '<p>No graph data</p>';
  
  // Position related concepts in a circle around center
  const relatedNodes = graph.nodes.filter(n => n.id !== currentConcept);
  const radius = 120;
  
  let svg = `<svg width="${width}" height="${height}" class="mini-graph-svg">`;
  
  // Draw edges first (so they appear behind nodes)
  graph.edges.forEach(edge => {
    const sourceNode = graph.nodes.find(n => n.id === edge.source);
    const targetNode = graph.nodes.find(n => n.id === edge.target);
    
    if (!sourceNode || !targetNode) return;
    
    let x1, y1, x2, y2;
    
    if (edge.source === currentConcept) {
      x1 = centerX;
      y1 = centerY;
      const targetIndex = relatedNodes.findIndex(n => n.id === edge.target);
      const angle = (targetIndex / relatedNodes.length) * 2 * Math.PI - Math.PI / 2;
      x2 = centerX + radius * Math.cos(angle);
      y2 = centerY + radius * Math.sin(angle);
    } else if (edge.target === currentConcept) {
      x2 = centerX;
      y2 = centerY;
      const sourceIndex = relatedNodes.findIndex(n => n.id === edge.source);
      const angle = (sourceIndex / relatedNodes.length) * 2 * Math.PI - Math.PI / 2;
      x1 = centerX + radius * Math.cos(angle);
      y1 = centerY + radius * Math.sin(angle);
    } else {
      // Edge between two related concepts
      const sourceIndex = relatedNodes.findIndex(n => n.id === edge.source);
      const targetIndex = relatedNodes.findIndex(n => n.id === edge.target);
      const angle1 = (sourceIndex / relatedNodes.length) * 2 * Math.PI - Math.PI / 2;
      const angle2 = (targetIndex / relatedNodes.length) * 2 * Math.PI - Math.PI / 2;
      x1 = centerX + radius * Math.cos(angle1);
      y1 = centerY + radius * Math.sin(angle1);
      x2 = centerX + radius * Math.cos(angle2);
      y2 = centerY + radius * Math.sin(angle2);
    }
    
    svg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" 
            stroke="#94a3b8" stroke-width="2" class="graph-edge"/>`;
  });
  
  // Draw current concept node (center)
  svg += `<circle cx="${centerX}" cy="${centerY}" r="30" 
          fill="#3b82f6" stroke="#1e40af" stroke-width="3" class="graph-node current-node"/>`;
  svg += `<text x="${centerX}" y="${centerY + 5}" text-anchor="middle" 
          fill="white" font-size="12" font-weight="bold" class="graph-label">
          ${truncateText(currentConcept, 15)}</text>`;
  
  // Draw related concept nodes
  relatedNodes.forEach((node, index) => {
    const angle = (index / relatedNodes.length) * 2 * Math.PI - Math.PI / 2;
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);
    
    const isVisited = stageHistory.some(stage => stage.concept === node.id);
    const fillColor = isVisited ? '#10b981' : '#64748b';
    const strokeColor = isVisited ? '#059669' : '#475569';
    
    svg += `<circle cx="${x}" cy="${y}" r="25" 
            fill="${fillColor}" stroke="${strokeColor}" stroke-width="2" 
            class="graph-node related-node" data-concept="${node.id}"
            onclick="navigateToVisitedConcept('${node.id}')"/>`;
    svg += `<text x="${x}" y="${y + 4}" text-anchor="middle" 
            fill="white" font-size="11" class="graph-label">
            ${truncateText(node.id, 12)}</text>`;
  });
  
  svg += '</svg>';
  
  // Add legend
  svg += `<div class="graph-legend">
    <div class="legend-item">
      <span class="legend-color" style="background: #3b82f6;"></span>
      <span>Current concept</span>
    </div>
    <div class="legend-item">
      <span class="legend-color" style="background: #10b981;"></span>
      <span>Previously visited</span>
    </div>
    <div class="legend-item">
      <span class="legend-color" style="background: #64748b;"></span>
      <span>Related concept</span>
    </div>
  </div>`;
  
  return svg;
}

/**
 * Navigate to a previously visited concept
 */
function navigateToVisitedConcept(conceptId) {
  if (confirm(`Navigate to "${conceptId}"? This will load that concept for review.`)) {
    // Load the concept
    currentConcept = conceptId;
    document.getElementById('knowledgeConceptSelect').value = conceptId;
    
    // Navigate to Revisit stage to review connections
    navigateToStage('revisit');
  }
}

/**
 * Display revisit connections
 */
function displayRevisitConnections(connections) {
  const container = document.getElementById('revisitConnections');
  
  if (connections.length === 0) {
    container.innerHTML = '<p>No connection suggestions available. Think about how this concept relates to others you\'ve learned.</p>';
    return;
  }
  
  container.innerHTML = `
    <h4>Connection Suggestions:</h4>
    <ul class="connection-list">
      ${connections.map(conn => `<li>${conn}</li>`).join('')}
    </ul>
  `;
}

/**
 * Save and continue functions for each stage
 */
async function saveConstructAndContinue() {
  const content = document.getElementById('constructExplanation').value;
  
  if (!content.trim()) {
    showNotification('Please write your explanation first.', 'warning');
    return;
  }
  
  const saved = await saveExplanation('construct', content);
  
  if (saved) {
    navigateToStage('reflect');
  }
}

async function saveConstructOnly() {
  const content = document.getElementById('constructExplanation').value;
  
  if (!content.trim()) {
    showNotification('Please write your explanation first.', 'warning');
    return;
  }
  
  await saveExplanation('construct', content);
}

async function saveReflectionAndContinue() {
  const content = document.getElementById('reflectionNotes').value;
  
  if (!content.trim()) {
    showNotification('Please write your reflection notes first.', 'warning');
    return;
  }
  
  const saved = await saveExplanation('reflect', content);
  
  if (saved) {
    navigateToStage('scaffold');
  }
}

async function saveReflectionOnly() {
  const content = document.getElementById('reflectionNotes').value;
  
  if (!content.trim()) {
    showNotification('Please write your reflection notes first.', 'warning');
    return;
  }
  
  await saveExplanation('reflect', content);
}

async function saveScaffoldAndContinue() {
  const content = document.getElementById('scaffoldRevision').value;
  
  if (!content.trim()) {
    showNotification('Please write your revised explanation first.', 'warning');
    return;
  }
  
  const saved = await saveExplanation('scaffold', content);
  
  if (saved) {
    navigateToStage('consolidate');
  }
}

async function saveScaffoldOnly() {
  const content = document.getElementById('scaffoldRevision').value;
  
  if (!content.trim()) {
    showNotification('Please write your revised explanation first.', 'warning');
    return;
  }
  
  await saveExplanation('scaffold', content);
}

async function saveConsolidateAndContinue() {
  const content = document.getElementById('consolidateResponse').value;
  
  if (!content.trim()) {
    showNotification('Please write your response first.', 'warning');
    return;
  }
  
  const saved = await saveExplanation('consolidate', content);
  
  if (saved) {
    navigateToStage('revisit');
  }
}

async function saveConsolidateOnly() {
  const content = document.getElementById('consolidateResponse').value;
  
  if (!content.trim()) {
    showNotification('Please write your response first.', 'warning');
    return;
  }
  
  await saveExplanation('consolidate', content);
}

async function saveRevisit() {
  const content = document.getElementById('revisitNotes').value;
  
  if (!content.trim()) {
    showNotification('Please write your connections and questions first.', 'warning');
    return;
  }
  
  const saved = await saveExplanation('revisit', content);
  
  if (saved) {
    showNotification('Learning cycle complete! Great work!', 'success');
    showCompletionCelebration();
  }
}

/**
 * Show/hide content areas
 */
function showStageContent() {
  document.getElementById('stageContent').style.display = 'block';
}

function hideStageContent() {
  document.getElementById('stageContent').style.display = 'none';
}

function showWelcomeMessage() {
  document.getElementById('welcomeMessage').style.display = 'block';
}

function hideWelcomeMessage() {
  document.getElementById('welcomeMessage').style.display = 'none';
}

/**
 * Sidebar toggle
 */
function toggleSidebar() {
  const sidebar = document.getElementById('aiCompanionSidebar');
  sidebar.classList.toggle('collapsed');
  
  updateSidebarState();
}

function updateSidebarState() {
  const sidebar = document.getElementById('aiCompanionSidebar');
  const toggleIcon = document.querySelector('.sidebar-toggle span');
  
  if (sidebar.classList.contains('collapsed')) {
    toggleIcon.textContent = '◀';
  } else {
    toggleIcon.textContent = '▶';
  }
}

/**
 * Update sidebar mode to match current stage
 */
function updateSidebarMode(stage) {
  // Update sidebar mode buttons
  const modeButtons = document.querySelectorAll('.companion-mode-btn');
  modeButtons.forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.mode === stage) {
      btn.classList.add('active');
    }
  });
  
  // Open sidebar if collapsed
  const sidebar = document.getElementById('aiCompanionSidebar');
  if (sidebar.classList.contains('collapsed')) {
    toggleSidebar();
  }
}

/**
 * Switch to mode from sidebar
 */
function switchToMode(mode) {
  navigateToStage(mode);
}

/**
 * Notification system
 */
function showNotification(message, type = 'info') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;
  
  // Add to page
  document.body.appendChild(notification);
  
  // Remove after 3 seconds
  setTimeout(() => {
    notification.classList.add('fade-out');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

function showError(message) {
  showNotification(message, 'error');
}

/**
 * Completion celebration
 */
function showCompletionCelebration() {
  // Simple celebration animation
  const celebration = document.createElement('div');
  celebration.className = 'celebration';
  celebration.innerHTML = '🎉 Learning Cycle Complete! 🎉';
  
  document.body.appendChild(celebration);
  
  setTimeout(() => {
    celebration.classList.add('fade-out');
    setTimeout(() => celebration.remove(), 500);
  }, 2000);
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initKnowledgeConstruction);
} else {
  initKnowledgeConstruction();
}

/**
 * Accessibility Features
 */

// Keyboard navigation for stage arrows
document.addEventListener('keydown', (e) => {
  // Number keys 1-5 for direct stage navigation
  if (e.key >= '1' && e.key <= '5' && !e.ctrlKey && !e.altKey) {
    const stageIndex = parseInt(e.key) - 1;
    const stages = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
    if (stageIndex < stages.length) {
      navigateToStage(stages[stageIndex]);
      e.preventDefault();
    }
  }
  
  // Arrow keys for next/previous stage
  if (e.key === 'ArrowRight' && !e.ctrlKey && !e.altKey) {
    const stages = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
    const currentIndex = stages.indexOf(currentStage);
    if (currentIndex < stages.length - 1) {
      navigateToStage(stages[currentIndex + 1]);
      e.preventDefault();
    }
  }
  
  if (e.key === 'ArrowLeft' && !e.ctrlKey && !e.altKey) {
    const stages = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
    const currentIndex = stages.indexOf(currentStage);
    if (currentIndex > 0) {
      navigateToStage(stages[currentIndex - 1]);
      e.preventDefault();
    }
  }
  
  // Ctrl+S to save current stage
  if (e.ctrlKey && e.key === 's') {
    e.preventDefault();
    saveCurrentStage();
  }
  
  // Ctrl+Enter to save and continue
  if (e.ctrlKey && e.key === 'Enter') {
    e.preventDefault();
    saveAndContinue();
  }
  
  // Escape to close sidebar
  if (e.key === 'Escape') {
    const sidebar = document.getElementById('aiCompanionSidebar');
    if (!sidebar.classList.contains('collapsed')) {
      toggleSidebar();
    }
  }
});

/**
 * Save current stage based on currentStage
 */
function saveCurrentStage() {
  switch (currentStage) {
    case 'construct':
      saveConstructOnly();
      break;
    case 'reflect':
      saveReflectionOnly();
      break;
    case 'scaffold':
      saveScaffoldOnly();
      break;
    case 'consolidate':
      saveConsolidateOnly();
      break;
    case 'revisit':
      saveRevisit();
      break;
  }
}

/**
 * Save and continue to next stage
 */
function saveAndContinue() {
  switch (currentStage) {
    case 'construct':
      saveConstructAndContinue();
      break;
    case 'reflect':
      saveReflectionAndContinue();
      break;
    case 'scaffold':
      saveScaffoldAndContinue();
      break;
    case 'consolidate':
      saveConsolidateAndContinue();
      break;
  }
}

/**
 * Add ARIA labels to stage arrows
 */
function addAccessibilityLabels() {
  const stageArrows = document.querySelectorAll('.stage-arrow');
  stageArrows.forEach((arrow, index) => {
    const stage = arrow.dataset.stage;
    const stageInfo = STAGES[stage];
    arrow.setAttribute('role', 'button');
    arrow.setAttribute('tabindex', '0');
    arrow.setAttribute('aria-label', `Stage ${index + 1}: ${stageInfo.name} - ${stageInfo.description}`);
    
    // Add keyboard support for Enter/Space
    arrow.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        navigateToStage(stage);
      }
    });
  });
}

/**
 * Add ARIA labels to mode buttons
 */
function addModeButtonAccessibility() {
  const modeButtons = document.querySelectorAll('.companion-mode-btn');
  modeButtons.forEach((button) => {
    const mode = button.dataset.mode;
    const stageInfo = STAGES[mode];
    button.setAttribute('aria-label', `Switch to ${stageInfo.name} mode`);
  });
}

/**
 * Initialize accessibility features
 */
function initAccessibility() {
  addAccessibilityLabels();
  addModeButtonAccessibility();
  addAriaLiveRegions();
  addKeyboardShortcuts();
  
  // Add skip navigation link
  const skipLink = document.createElement('a');
  skipLink.href = '#main-content';
  skipLink.className = 'skip-link';
  skipLink.textContent = 'Skip to main content';
  skipLink.style.cssText = `
    position: absolute;
    top: -40px;
    left: 0;
    background: #4a90d9;
    color: white;
    padding: 8px;
    text-decoration: none;
    z-index: 9999;
  `;
  skipLink.addEventListener('focus', () => {
    skipLink.style.top = '0';
  });
  skipLink.addEventListener('blur', () => {
    skipLink.style.top = '-40px';
  });
  document.body.insertBefore(skipLink, document.body.firstChild);
  
  // Add main content landmark
  const mainContent = document.querySelector('.knowledge-content');
  if (mainContent && !mainContent.id) {
    mainContent.id = 'main-content';
  }
}

/**
 * Add ARIA live regions for dynamic content
 */
function addAriaLiveRegions() {
  // Add live region for notifications
  let liveRegion = document.getElementById('aria-live-region');
  if (!liveRegion) {
    liveRegion = document.createElement('div');
    liveRegion.id = 'aria-live-region';
    liveRegion.setAttribute('aria-live', 'polite');
    liveRegion.setAttribute('aria-atomic', 'true');
    liveRegion.className = 'sr-only';
    liveRegion.style.cssText = `
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    `;
    document.body.appendChild(liveRegion);
  }
  
  // Add live region for stage changes
  let stageRegion = document.getElementById('stage-live-region');
  if (!stageRegion) {
    stageRegion = document.createElement('div');
    stageRegion.id = 'stage-live-region';
    stageRegion.setAttribute('aria-live', 'assertive');
    stageRegion.setAttribute('aria-atomic', 'true');
    stageRegion.className = 'sr-only';
    stageRegion.style.cssText = `
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    `;
    document.body.appendChild(stageRegion);
  }
}

/**
 * Announce message to screen readers
 */
function announceToScreenReader(message, priority = 'polite') {
  const regionId = priority === 'assertive' ? 'stage-live-region' : 'aria-live-region';
  const region = document.getElementById(regionId);
  if (region) {
    region.textContent = message;
    // Clear after 3 seconds
    setTimeout(() => {
      region.textContent = '';
    }, 3000);
  }
}

/**
 * Add keyboard shortcuts
 */
function addKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    // Ignore if user is typing in input/textarea
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      return;
    }
    
    // Ctrl/Cmd + S: Save current stage
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
      e.preventDefault();
      saveCurrentStage();
      announceToScreenReader('Stage saved');
    }
    
    // Ctrl/Cmd + E: Export learning data
    if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
      e.preventDefault();
      exportLearningData();
    }
    
    // Ctrl/Cmd + I: Import learning data
    if ((e.ctrlKey || e.metaKey) && e.key === 'i') {
      e.preventDefault();
      document.getElementById('import-file-input')?.click();
    }
    
    // ?: Show keyboard shortcuts help
    if (e.key === '?') {
      e.preventDefault();
      showKeyboardShortcutsHelp();
    }
    
    // Arrow keys: Navigate stages
    if (e.key === 'ArrowRight' && e.altKey) {
      e.preventDefault();
      navigateToNextStage();
    }
    if (e.key === 'ArrowLeft' && e.altKey) {
      e.preventDefault();
      navigateToPreviousStage();
    }
  });
}

/**
 * Show keyboard shortcuts help modal
 */
function showKeyboardShortcutsHelp() {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content" style="max-width: 500px;">
      <div class="modal-header">
        <h3>⌨️ Keyboard Shortcuts</h3>
        <button class="btn-icon modal-close" aria-label="Close">×</button>
      </div>
      <div class="modal-body">
        <table class="shortcuts-table">
          <tr>
            <td><kbd>Ctrl/Cmd</kbd> + <kbd>S</kbd></td>
            <td>Save current stage</td>
          </tr>
          <tr>
            <td><kbd>Ctrl/Cmd</kbd> + <kbd>E</kbd></td>
            <td>Export learning data</td>
          </tr>
          <tr>
            <td><kbd>Ctrl/Cmd</kbd> + <kbd>I</kbd></td>
            <td>Import learning data</td>
          </tr>
          <tr>
            <td><kbd>Alt</kbd> + <kbd>→</kbd></td>
            <td>Next stage</td>
          </tr>
          <tr>
            <td><kbd>Alt</kbd> + <kbd>←</kbd></td>
            <td>Previous stage</td>
          </tr>
          <tr>
            <td><kbd>?</kbd></td>
            <td>Show this help</td>
          </tr>
        </table>
      </div>
      <div class="modal-footer">
        <button class="btn-primary modal-close">Close</button>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  
  // Close modal handlers
  modal.querySelectorAll('.modal-close').forEach(btn => {
    btn.addEventListener('click', () => modal.remove());
  });
  
  // Close on escape
  const escapeHandler = (e) => {
    if (e.key === 'Escape') {
      modal.remove();
      document.removeEventListener('keydown', escapeHandler);
    }
  };
  document.addEventListener('keydown', escapeHandler);
}

/**
 * Export learning data to JSON
 */
function exportLearningData() {
  const data = {
    version: '1.0',
    exportDate: new Date().toISOString(),
    currentConcept,
    currentStage,
    stageHistory,
    stageCompletionStatus,
    revisionHistory,
    explanations: {}
  };
  
  // Collect all explanations from localStorage
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key.startsWith('explanation_')) {
      data.explanations[key] = localStorage.getItem(key);
    }
  }
  
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `learning-progress-${new Date().toISOString().split('T')[0]}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  
  showNotification('Learning data exported successfully', 'success');
  announceToScreenReader('Learning data exported');
}

/**
 * Import learning data from JSON
 */
function importLearningData(file) {
  const reader = new FileReader();
  
  reader.onload = (e) => {
    try {
      const data = JSON.parse(e.target.result);
      
      if (data.version !== '1.0') {
        throw new Error('Unsupported file version');
      }
      
      // Restore state
      if (data.currentConcept) {
        currentConcept = data.currentConcept;
        const select = document.getElementById('concept-select');
        if (select) {
          select.value = currentConcept;
        }
      }
      
      if (data.currentStage) {
        currentStage = data.currentStage;
      }
      
      if (data.stageHistory) {
        stageHistory = data.stageHistory;
      }
      
      if (data.stageCompletionStatus) {
        stageCompletionStatus = data.stageCompletionStatus;
      }
      
      if (data.revisionHistory) {
        revisionHistory = data.revisionHistory;
      }
      
      // Restore explanations to localStorage
      if (data.explanations) {
        Object.entries(data.explanations).forEach(([key, value]) => {
          localStorage.setItem(key, value);
        });
      }
      
      // Update UI
      updateStageProgress();
      renderCurrentStage();
      
      showNotification('Learning data imported successfully', 'success');
      announceToScreenReader('Learning data imported');
      
    } catch (error) {
      console.error('Import error:', error);
      showNotification('Failed to import: ' + error.message, 'error');
      announceToScreenReader('Import failed');
    }
  };
  
  reader.readAsText(file);
}

// Initialize accessibility when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAccessibility);
} else {
  initAccessibility();
}
