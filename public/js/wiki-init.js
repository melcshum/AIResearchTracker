/**
 * Wiki Page Initialization
 * 
 * Sets up page-specific integration for AI Companion on wiki.md
 * This file handles wiki-specific features (term selection, contributions)
 * while delegating AI Companion functionality to the shared component.
 */

// Initialize AI Companion after shared component loads
document.addEventListener('DOMContentLoaded', () => {
  // Wait for AI Companion to be available
  const checkAICompanion = setInterval(() => {
    if (typeof AICompanion !== 'undefined') {
      clearInterval(checkAICompanion);
      initWikiAICompanion();
    }
  }, 100);
});

function initWikiAICompanion() {
  // Create AI Companion instance
  const aiCompanion = new AICompanion({
    currentPage: 'wiki',
    onModeChange: (mode) => {
      console.log('Wiki: Mode changed to:', mode);
    },
    onFeedbackReceived: (data) => {
      console.log('Wiki: Feedback received:', data);
    },
    onError: (error) => {
      console.error('Wiki: AI Companion error:', error);
    }
  });
  
  // Initialize UI
  aiCompanion.init('.companion-mode-container', '.companion-content');
  
  // Store reference globally for term selection handler
  window.wikiAICompanion = aiCompanion;
  
  // Set up term selection handler
  setupWikiTermSelection(aiCompanion);
}

function setupWikiTermSelection(aiCompanion) {
  // Add click handlers to wiki terms
  document.querySelectorAll('.wiki-term').forEach(term => {
    term.addEventListener('click', () => {
      const concept = term.dataset.term;
      
      // Update current term
      window.currentTerm = {
        name: concept,
        id: concept.toLowerCase().replace(/\s+/g, '-'),
        keywords: [],
        relatedTerms: []
      };
      
      // Set concept in AI Companion
      aiCompanion.setConcept(concept);
      
      // Switch to Construct mode
      aiCompanion.switchMode('construct');
      
      // Update term display
      document.querySelectorAll('.wiki-term').forEach(t => t.classList.remove('selected'));
      term.classList.add('selected');
    });
  });
}

// Export for use in other scripts
window.initWikiAICompanion = initWikiAICompanion;
