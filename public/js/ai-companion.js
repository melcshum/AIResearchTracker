/**
 * AI Companion - Shared Component
 * 
 * Unified AI Companion class for all pages (wiki.md, paper-reader.md, ai-wiki.md)
 * Implements the 5-stage knowledge construction cycle from conference paper
 * 
 * Design Principles:
 * - DP1: Learner Ownership
 * - DP2: Scaffold Rather Than Substitute
 * - DP3: Reflection Before Correction
 * - DP4: Continuous Knowledge Integration
 */

class AICompanion {
  constructor(config = {}) {
    // Configuration
    this.apiBase = config.apiBase || 'http://localhost:5001/api/wiki';
    this.currentPage = config.currentPage || 'wiki';
    
    // State
    this.currentMode = 'construct'; // construct, reflect, scaffold, consolidate, revisit
    this.currentConcept = null;
    this.userExplanation = '';
    this.knowledgeContext = [];
    this.conversationHistory = [];
    this.isLoading = false;
    
    // DOM elements (set by init)
    this.modeContainer = null;
    this.contentContainer = null;
    this.loadingIndicator = null;
    
    // Callbacks
    this.onModeChange = config.onModeChange || null;
    this.onFeedbackReceived = config.onFeedbackReceived || null;
    this.onError = config.onError || null;
  }

  /**
   * Initialize the AI Companion with DOM elements
   */
  init(modeContainerSelector, contentContainerSelector, loadingIndicatorSelector = null) {
    this.modeContainer = document.querySelector(modeContainerSelector);
    this.contentContainer = document.querySelector(contentContainerSelector);
    this.loadingIndicator = loadingIndicatorSelector ? document.querySelector(loadingIndicatorSelector) : null;
    
    if (!this.modeContainer || !this.contentContainer) {
      console.error('AI Companion: DOM elements not found');
      return false;
    }
    
    // Set up mode buttons
    this._setupModeButtons();
    
    // Set up loading indicator
    if (this.loadingIndicator) {
      this.loadingIndicator.style.display = 'none';
    }
    
    console.log('AI Companion initialized');
    return true;
  }

  /**
   * Set up mode button event listeners
   */
  _setupModeButtons() {
    const buttons = this.modeContainer.querySelectorAll('.companion-mode-btn');
    
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        const mode = button.dataset.mode || button.textContent.toLowerCase().trim();
        this.switchMode(mode);
      });
    });
  }

  /**
   * Switch to a different mode in the 5-stage cycle
   */
  async switchMode(mode) {
    const validModes = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
    
    if (!validModes.includes(mode)) {
      console.error('AI Companion: Invalid mode', mode);
      return;
    }
    
    this.currentMode = mode;
    
    // Update UI
    this._updateModeButtons(mode);
    
    // Clear previous content
    this._clearContent();
    
    // Show mode-specific UI
    await this._showModeUI(mode);
    
    // Callback
    if (this.onModeChange) {
      this.onModeChange(mode);
    }
  }

  /**
   * Update mode button active states
   */
  _updateModeButtons(activeMode) {
    const buttons = this.modeContainer.querySelectorAll('.companion-mode-btn');
    
    buttons.forEach(button => {
      const mode = button.dataset.mode || button.textContent.toLowerCase().trim();
      if (mode === activeMode) {
        button.classList.add('active');
      } else {
        button.classList.remove('active');
      }
    });
  }

  /**
   * Clear content container
   */
  _clearContent() {
    if (this.contentContainer) {
      this.contentContainer.innerHTML = '';
    }
  }

  /**
   * Show mode-specific UI
   */
  async _showModeUI(mode) {
    const modeInfo = this._getModeInfo(mode);
    
    // Show intro text
    const intro = document.createElement('div');
    intro.className = 'companion-intro';
    intro.innerHTML = `
      <h4>${modeInfo.icon} ${modeInfo.title}</h4>
      <p>${modeInfo.description}</p>
    `;
    this.contentContainer.appendChild(intro);
    
    // Mode-specific setup
    switch (mode) {
      case 'construct':
        await this._setupConstructMode();
        break;
      case 'reflect':
        await this._setupReflectMode();
        break;
      case 'scaffold':
        await this._setupScaffoldMode();
        break;
      case 'consolidate':
        await this._setupConsolidateMode();
        break;
      case 'revisit':
        await this._setupRevisitMode();
        break;
    }
  }

  /**
   * Get mode information
   */
  _getModeInfo(mode) {
    const modes = {
      construct: {
        icon: '✍️',
        title: 'Construct',
        description: 'Write your initial explanation in your own words. AI will help you reflect afterward.',
        prompt: 'Start by explaining this concept in your own words...'
      },
      reflect: {
        icon: '🤔',
        title: 'Reflect',
        description: 'Examine your explanation. AI will generate metacognitive prompts to help you think deeper.',
        prompt: 'Review your explanation and consider:'
      },
      scaffold: {
        icon: '🏗️',
        title: 'Scaffold',
        description: 'AI provides targeted questions and hints to fill gaps in your understanding.',
        prompt: 'Let\'s build on your explanation:'
      },
      consolidate: {
        icon: '💪',
        title: 'Consolidate & Apply',
        description: 'Test your understanding by retrieving knowledge independently.',
        prompt: 'Try to explain this without looking at your notes:'
      },
      revisit: {
        icon: '🔄',
        title: 'Revisit & Extend',
        description: 'Integrate new concepts with your prior knowledge.',
        prompt: 'How does this relate to what you\'ve learned before?'
      }
    };
    
    return modes[mode] || modes.construct;
  }

  /**
   * Set Construct mode UI
   */
  async _setupConstructMode() {
    const textarea = document.createElement('textarea');
    textarea.id = 'userExplanationInput';
    textarea.className = 'companion-textarea';
    textarea.placeholder = 'Explain this concept in your own words...';
    textarea.rows = 8;
    
    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn-primary';
    submitBtn.textContent = 'Save & Reflect';
    submitBtn.onclick = () => this._handleConstructSubmit();
    
    this.contentContainer.appendChild(textarea);
    this.contentContainer.appendChild(submitBtn);
  }

  /**
   * Handle Construct mode submission
   */
  async _handleConstructSubmit() {
    const textarea = document.getElementById('userExplanationInput');
    
    if (!textarea || !textarea.value.trim()) {
      alert('Please write your explanation first');
      return;
    }
    
    this.userExplanation = textarea.value.trim();
    
    // Save to knowledge base
    await this._saveToKnowledgeBase();
    
    // Auto-switch to Reflect mode
    await this.switchMode('reflect');
    
    // Generate reflection prompts
    await this.generateReflectionPrompts(this.userExplanation);
  }

  /**
   * Set Reflect mode UI
   */
  async _setupReflectMode() {
    if (!this.userExplanation) {
      this._showMessage('Please complete Construct mode first', 'warning');
      return;
    }
    
    // Show user's explanation
    const explanationDiv = document.createElement('div');
    explanationDiv.className = 'user-explanation';
    explanationDiv.innerHTML = `
      <h5>Your Explanation:</h5>
      <p>${this._escapeHtml(this.userExplanation)}</p>
    `;
    this.contentContainer.appendChild(explanationDiv);
    
    // Button to generate prompts
    const generateBtn = document.createElement('button');
    generateBtn.className = 'btn-secondary';
    generateBtn.textContent = '🤖 Generate Reflection Prompts';
    generateBtn.onclick = () => this.generateReflectionPrompts(this.userExplanation);
    
    this.contentContainer.appendChild(generateBtn);
    
    // Auto-generate prompts
    await this.generateReflectionPrompts(this.userExplanation);
  }

  /**
   * Generate reflection prompts (DP3: Reflection Before Correction)
   */
  async generateReflectionPrompts(explanation) {
    await this._callAPI('reflect', {
      concept: this.currentConcept,
      explanation: explanation
    }, (response) => {
      this._displayReflectionPrompts(response);
    });
  }

  /**
   * Display reflection prompts
   */
  _displayReflectionPrompts(response) {
    const prompts = response.prompts || response.questions || [];
    
    if (prompts.length === 0) {
      this._showMessage('No reflection prompts generated', 'info');
      return;
    }
    
    const promptsDiv = document.createElement('div');
    promptsDiv.className = 'reflection-prompts';
    
    const title = document.createElement('h5');
    title.textContent = 'Reflection Questions:';
    promptsDiv.appendChild(title);
    
    prompts.forEach((prompt, index) => {
      const promptEl = document.createElement('div');
      promptEl.className = 'prompt-item';
      promptEl.innerHTML = `
        <span class="prompt-number">${index + 1}.</span>
        <span class="prompt-text">${this._escapeHtml(prompt)}</span>
      `;
      promptsDiv.appendChild(promptEl);
    });
    
    this.contentContainer.appendChild(promptsDiv);
  }

  /**
   * Set Scaffold mode UI
   */
  async _setupScaffoldMode() {
    if (!this.userExplanation) {
      this._showMessage('Please complete Construct mode first', 'warning');
      return;
    }
    
    // Show user's explanation
    const explanationDiv = document.createElement('div');
    explanationDiv.className = 'user-explanation';
    explanationDiv.innerHTML = `
      <h5>Your Explanation:</h5>
      <p>${this._escapeHtml(this.userExplanation)}</p>
    `;
    this.contentContainer.appendChild(explanationDiv);
    
    // Button to detect gaps
    const detectBtn = document.createElement('button');
    detectBtn.className = 'btn-secondary';
    detectBtn.textContent = '🏗️ Detect Knowledge Gaps';
    detectBtn.onclick = () => this.detectGaps(this.userExplanation);
    
    this.contentContainer.appendChild(detectBtn);
    
    // Auto-detect gaps
    await this.detectGaps(this.userExplanation);
  }

  /**
   * Detect knowledge gaps (DP2: Scaffold Rather Than Substitute)
   */
  async detectGaps(explanation) {
    await this._callAPI('scaffold', {
      action: 'detect_gaps',
      concept: this.currentConcept,
      explanation: explanation
    }, (response) => {
      this._displayGapAnalysis(response);
    });
  }

  /**
   * Display gap analysis
   */
  _displayGapAnalysis(response) {
    const missingConcepts = response.missing_concepts || response.missing_concept || [];
    const suggestions = response.suggestions || [];
    const connections = response.connections || [];
    
    if (missingConcepts.length === 0 && suggestions.length === 0) {
      this._showMessage('Your explanation looks comprehensive!', 'success');
      return;
    }
    
    // Missing concepts
    if (missingConcepts.length > 0) {
      const missingDiv = document.createElement('div');
      missingDiv.className = 'gap-analysis';
      
      const title = document.createElement('h5');
      title.textContent = 'Missing Concepts:';
      missingDiv.appendChild(title);
      
      missingConcepts.forEach((concept, index) => {
        const conceptEl = document.createElement('div');
        conceptEl.className = 'gap-item';
        conceptEl.innerHTML = `
          <span class="gap-icon">⚠️</span>
          <span class="gap-text">${this._escapeHtml(concept)}</span>
        `;
        missingDiv.appendChild(conceptEl);
      });
      
      this.contentContainer.appendChild(missingDiv);
    }
    
    // Suggestions
    if (suggestions.length > 0) {
      const suggestionsDiv = document.createElement('div');
      suggestionsDiv.className = 'scaffold-suggestions';
      
      const title = document.createElement('h5');
      title.textContent = 'Suggestions:';
      suggestionsDiv.appendChild(title);
      
      suggestions.forEach((suggestion, index) => {
        const suggestionEl = document.createElement('div');
        suggestionEl.className = 'suggestion-item';
        suggestionEl.innerHTML = `
          <span class="suggestion-icon">💡</span>
          <span class="suggestion-text">${this._escapeHtml(suggestion)}</span>
        `;
        suggestionsDiv.appendChild(suggestionEl);
      });
      
      this.contentContainer.appendChild(suggestionsDiv);
    }
    
    // Connection recommendations (DP4)
    if (connections.length > 0) {
      const connectionsDiv = document.createElement('div');
      connectionsDiv.className = 'connection-recommendations';
      
      const title = document.createElement('h5');
      title.textContent = 'Related Concepts:';
      connectionsDiv.appendChild(title);
      
      connections.forEach((connection, index) => {
        const connectionEl = document.createElement('div');
        connectionEl.className = 'connection-item';
        connectionEl.innerHTML = `
          <span class="connection-icon">🔗</span>
          <span class="connection-text">${this._escapeHtml(connection)}</span>
        `;
        connectionEl.onclick = () => this._navigateToConcept(connection);
        connectionEl.style.cursor = 'pointer';
        connectionsDiv.appendChild(connectionEl);
      });
      
      this.contentContainer.appendChild(connectionsDiv);
    }
  }

  /**
   * Set Consolidate mode UI
   */
  async _setupConsolidateMode() {
    if (!this.currentConcept) {
      this._showMessage('Please select a concept first', 'warning');
      return;
    }
    
    // Show retrieval task
    const taskDiv = document.createElement('div');
    taskDiv.className = 'consolidate-task';
    taskDiv.innerHTML = `
      <h5>Retrieval Practice:</h5>
      <p>Explain <strong>${this.currentConcept}</strong> without looking at your notes.</p>
      <textarea id="recallInput" class="companion-textarea" rows="6" placeholder="Write your explanation from memory..."></textarea>
      <button class="btn-secondary" onclick="aiCompanion.generateConsolidateFeedback()">📊 Get Feedback</button>
    `;
    
    this.contentContainer.appendChild(taskDiv);
  }

  /**
   * Generate consolidation feedback
   */
  async generateConsolidateFeedback() {
    const recallInput = document.getElementById('recallInput');
    
    if (!recallInput || !recallInput.value.trim()) {
      alert('Please write your explanation first');
      return;
    }
    
    const recall = recallInput.value.trim();
    
    await this._callAPI('consolidate', {
      concept: this.currentConcept,
      original: this.userExplanation,
      retrieval_attempt: recall
    }, (response) => {
      this._displayConsolidateFeedback(response);
    });
  }

  /**
   * Display consolidation feedback
   */
  _displayConsolidateFeedback(response) {
    const accuracy = response.accuracy || response.score || 0;
    const feedback = response.feedback || response.comments || [];
    
    // Accuracy score
    const scoreDiv = document.createElement('div');
    scoreDiv.className = 'accuracy-score';
    scoreDiv.innerHTML = `
      <div class="score-circle">
        <span class="score-number">${accuracy}%</span>
      </div>
      <p>Retrieval Accuracy</p>
    `;
    this.contentContainer.appendChild(scoreDiv);
    
    // Feedback
    if (feedback.length > 0) {
      const feedbackDiv = document.createElement('div');
      feedbackDiv.className = 'consolidate-feedback';
      
      const title = document.createElement('h5');
      title.textContent = 'Feedback:';
      feedbackDiv.appendChild(title);
      
      feedback.forEach((item, index) => {
        const feedbackEl = document.createElement('div');
        feedbackEl.className = 'feedback-item';
        feedbackEl.innerHTML = `<p>${this._escapeHtml(item)}</p>`;
        feedbackDiv.appendChild(feedbackEl);
      });
      
      this.contentContainer.appendChild(feedbackDiv);
    }
  }

  /**
   * Set Revisit mode UI
   */
  async _setupRevisitMode() {
    if (!this.currentConcept) {
      this._showMessage('Please select a concept first', 'warning');
      return;
    }
    
    // Get knowledge context
    await this._loadKnowledgeContext();
    
    // Show revisit suggestions
    if (this.knowledgeContext.length > 0) {
      const revisitDiv = document.createElement('div');
      revisitDiv.className = 'revisit-suggestions';
      
      const title = document.createElement('h5');
      title.textContent = 'Related Prior Knowledge:';
      revisitDiv.appendChild(title);
      
      this.knowledgeContext.forEach((entry, index) => {
        const entryEl = document.createElement('div');
        entryEl.className = 'revisit-item';
        entryEl.innerHTML = `
          <span class="revisit-icon">📚</span>
          <span class="revisit-text"><strong>${this._escapeHtml(entry.concept)}</strong>: ${this._escapeHtml(entry.summary || '')}</span>
        `;
        entryEl.onclick = () => this._navigateToConcept(entry.concept);
        entryEl.style.cursor = 'pointer';
        revisitDiv.appendChild(entryEl);
      });
      
      this.contentContainer.appendChild(revisitDiv);
    } else {
      this._showMessage('No prior knowledge found to revisit', 'info');
    }
  }

  /**
   * Load knowledge context (DP4: Continuous Knowledge Integration)
   */
  async _loadKnowledgeContext() {
    try {
      const response = await fetch(`${this.apiBase}/context`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ concept: this.currentConcept })
      });
      
      const data = await response.json();
      this.knowledgeContext = data.context || [];
    } catch (error) {
      console.error('AI Companion: Failed to load knowledge context', error);
    }
  }

  /**
   * Call AI Companion API
   */
  async _callAPI(mode, payload, callback) {
    this._setLoading(true);
    
    try {
      const response = await fetch(`${this.apiBase}/companion`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode, ...payload })
      });
      
      const data = await response.json();
      
      if (callback) {
        callback(data);
      }
      
      // Add to conversation history
      this.conversationHistory.push({
        mode,
        payload,
        response: data,
        timestamp: new Date().toISOString()
      });
      
      if (this.onFeedbackReceived) {
        this.onFeedbackReceived(data);
      }
    } catch (error) {
      console.error('AI Companion: API call failed', error);
      
      if (this.onError) {
        this.onError(error);
      } else {
        this._showMessage('API call failed. Please try again.', 'error');
      }
    } finally {
      this._setLoading(false);
    }
  }

  /**
   * Set loading state
   */
  _setLoading(loading) {
    this.isLoading = loading;
    
    if (this.loadingIndicator) {
      this.loadingIndicator.style.display = loading ? 'block' : 'none';
    }
  }

  /**
   * Save to knowledge base
   */
  async _saveToKnowledgeBase() {
    // This would integrate with the Personal Knowledge Base
    // For now, just log
    console.log('AI Companion: Saving to knowledge base', {
      concept: this.currentConcept,
      explanation: this.userExplanation,
      mode: this.currentMode
    });
  }

  /**
   * Navigate to concept
   */
  _navigateToConcept(concept) {
    // This would integrate with page-specific navigation
    console.log('AI Companion: Navigate to concept', concept);
    
    // Try to trigger page-specific navigation
    if (typeof window.navigateToConcept === 'function') {
      window.navigateToConcept(concept);
    }
  }

  /**
   * Show message
   */
  _showMessage(message, type = 'info') {
    const messageEl = document.createElement('div');
    messageEl.className = `companion-message companion-message-${type}`;
    messageEl.textContent = message;
    
    this.contentContainer.appendChild(messageEl);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
      messageEl.remove();
    }, 5000);
  }

  /**
   * Escape HTML
   */
  _escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Set current concept
   */
  setConcept(concept) {
    this.currentConcept = concept;
    console.log('AI Companion: Concept set to', concept);
  }

  /**
   * Get conversation history
   */
  getConversationHistory() {
    return this.conversationHistory;
  }
}

// Global instance (for backward compatibility)
let aiCompanion = null;

// Initialize global instance
function initAICompanion(config = {}) {
  aiCompanion = new AICompanion(config);
  return aiCompanion;
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { AICompanion, initAICompanion };
}
