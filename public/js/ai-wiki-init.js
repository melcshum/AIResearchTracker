/**
 * AI Wiki Page Initialization
 * 
 * Sets up page-specific integration for AI Companion on ai-wiki.md
 * This file handles wiki-specific features (concept selection, learning modes)
 * while delegating AI Companion functionality to the shared component.
 */

// Initialize AI Companion after shared component loads
document.addEventListener('DOMContentLoaded', () => {
  // Wait for AI Companion to be available
  const checkAICompanion = setInterval(() => {
    if (typeof AICompanion !== 'undefined') {
      clearInterval(checkAICompanion);
      initAIWikiAICompanion();
    }
  }, 100);
});

function initAIWikiAICompanion() {
  // Create AI Companion instance
  const aiCompanion = new AICompanion({
    currentPage: 'ai-wiki',
    onModeChange: (mode) => {
      console.log('AI Wiki: Mode changed to:', mode);
    },
    onFeedbackReceived: (data) => {
      console.log('AI Wiki: Feedback received:', data);
    },
    onError: (error) => {
      console.error('AI Wiki: AI Companion error:', error);
    }
  });
  
  // Initialize UI
  aiCompanion.init('.companion-modes', '#companionContent');
  
  // Store reference globally for concept selection handler
  window.aiWikiAICompanion = aiCompanion;
  
  // Set up concept selection handler
  setupWikiConceptSelection(aiCompanion);
}

function setupWikiConceptSelection(aiCompanion) {
  // Add click handlers to concept cards and related concepts
  document.addEventListener('click', (e) => {
    const conceptCard = e.target.closest('.concept-card, .related-concept');
    if (!conceptCard) return;
    
    const conceptName = conceptCard.dataset.concept || conceptCard.textContent.trim();
    if (!conceptName) return;
    
    // Get concept data from the page's concept database
    const conceptData = window.concepts?.[conceptName];
    if (!conceptData) {
      console.warn('Concept not found:', conceptName);
      return;
    }
    
    // Prompt learner for explanation (Construct mode)
    const explanation = prompt(
      `Explain "${conceptName}" in your own words:\n\n` +
      'Tip: Include what it is, why it matters, and how it relates to other concepts.',
      conceptData.userExplanation || ''
    );
    
    if (explanation) {
      // Store explanation in concept data
      if (window.concepts && window.concepts[conceptName]) {
        window.concepts[conceptName].userExplanation = explanation;
      }
      
      // Set concept in AI Companion
      aiCompanion.setConcept(conceptName, explanation);
      
      // Switch to Reflect mode automatically (Prompt Before Provide)
      aiCompanion.switchMode('reflect');
      
      // Show companion panel
      const panel = document.getElementById('aiCompanionPanel');
      if (panel) {
        panel.style.display = 'block';
      }
    }
  });
}

// Export for use in other scripts
window.initAIWikiAICompanion = initAIWikiAICompanion;
