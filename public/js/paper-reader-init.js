/**
 * Paper Reader Page Initialization
 * 
 * Sets up page-specific integration for AI Companion on paper-reader.md
 * This file handles paper-specific features (text selection, annotations)
 * while delegating AI Companion functionality to the shared component.
 */

// Initialize AI Companion after shared component loads
document.addEventListener('DOMContentLoaded', () => {
  // Wait for AI Companion to be available
  const checkAICompanion = setInterval(() => {
    if (typeof AICompanion !== 'undefined') {
      clearInterval(checkAICompanion);
      initPaperReaderAICompanion();
    }
  }, 100);
});

function initPaperReaderAICompanion() {
  // Create AI Companion instance
  const aiCompanion = new AICompanion({
    currentPage: 'paper-reader',
    onModeChange: (mode) => {
      console.log('Paper Reader: Mode changed to:', mode);
    },
    onFeedbackReceived: (data) => {
      console.log('Paper Reader: Feedback received:', data);
    },
    onError: (error) => {
      console.error('Paper Reader: AI Companion error:', error);
    }
  });
  
  // Initialize UI
  aiCompanion.init('.companion-modes', '#companionContent');
  
  // Store reference globally for concept selection handler
  window.paperReaderAICompanion = aiCompanion;
  
  // Set up concept selection handler
  setupPaperConceptSelection(aiCompanion);
}

function setupPaperConceptSelection(aiCompanion) {
  // Add click handlers to highlighted/concept elements in paper
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('highlight') || e.target.classList.contains('concept-link')) {
      const concept = e.target.dataset.concept || e.target.textContent;
      
      // Prompt learner for explanation
      const explanation = prompt('Explain this concept in your own words:', '');
      if (explanation) {
        // Set concept in AI Companion
        aiCompanion.setConcept(concept);
        
        // Switch to Reflect mode by default
        aiCompanion.switchMode('reflect');
        
        // Show companion sidebar
        const sidebar = document.getElementById('aiCompanionSidebar');
        if (sidebar) {
          sidebar.style.display = 'block';
        }
      }
    }
  });
}

// Export for use in other scripts
window.initPaperReaderAICompanion = initPaperReaderAICompanion;
