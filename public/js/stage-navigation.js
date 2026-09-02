// Stage Navigation Component
// Provides breadcrumbs, next step buttons, and contextual guidance

const STAGE_CONFIG = {
  write: {
    name: 'Write & Build',
    icon: '✍️',
    color: '#3498db',
    next: 'review',
    nextLabel: 'Review & Reflect',
    nextIcon: '🔍',
    relatedTools: [
      { name: 'Paper Reader', href: 'paper-reader.html', icon: '📄' },
      { name: 'Research Workspace', href: 'workspace.html', icon: '🔬' }
    ]
  },
  review: {
    name: 'Review & Reflect',
    icon: '🔍',
    color: '#f39c12',
    next: 'enhance',
    nextLabel: 'AI Enhancement',
    nextIcon: '🤖',
    relatedTools: [
      { name: 'Takeaways', href: 'takeaways.html', icon: '💡' },
      { name: 'Questions', href: 'questions.html', icon: '❓' }
    ]
  },
  enhance: {
    name: 'AI Enhancement',
    icon: '🤖',
    color: '#9b59b6',
    next: 'attain',
    nextLabel: 'Attain Mastery',
    nextIcon: '🧠',
    relatedTools: [
      { name: 'AI Study Guide', href: 'ai-study-guide.html', icon: '🎓' },
      { name: 'Feedback Dashboard', href: 'feedback-dashboard.html', icon: '📊' }
    ]
  },
  attain: {
    name: 'Attain Mastery',
    icon: '🧠',
    color: '#27ae60',
    next: 'update',
    nextLabel: 'Stay Updated',
    nextIcon: '📈',
    relatedTools: [
      { name: 'Spaced Repetition', href: 'spaced-repetition.html', icon: '🔄' },
      { name: 'Learning Path', href: 'my-learning-path.html', icon: '🎯' }
    ]
  },
  update: {
    name: 'Stay Updated',
    icon: '📈',
    color: '#e74c3c',
    next: 'write',
    nextLabel: 'Write & Build',
    nextIcon: '✍️',
    relatedTools: [
      { name: 'Weekly Digest', href: 'digests/index.html', icon: '📰' },
      { name: 'Timeline', href: 'timeline.html', icon: '📅' }
    ]
  }
};

const PAGE_STAGE_MAP = {
  'wiki.html': 'write',
  'paper-reader.html': 'write',
  'workspace.html': 'write',
  'highlights.html': 'review',
  'takeaways.html': 'review',
  'questions.html': 'review',
  'ai-wiki.html': 'enhance',
  'ai-study-guide.html': 'enhance',
  'feedback-dashboard.html': 'enhance',
  'spaced-repetition.html': 'attain',
  'my-learning-path.html': 'attain',
  'recommendations.html': 'attain',
  'digests/index.html': 'update',
  'search-papers.html': 'update',
  'timeline.html': 'update'
};

function initStageNavigation() {
  const currentPage = window.location.pathname.split('/').pop();
  const stageKey = PAGE_STAGE_MAP[currentPage];
  
  if (!stageKey || !STAGE_CONFIG[stageKey]) return;
  
  const stage = STAGE_CONFIG[stageKey];
  const container = document.createElement('div');
  container.className = 'stage-navigation-container';
  container.innerHTML = `
    <div class="stage-breadcrumb">
      <a href="learning-journey.html" class="breadcrumb-link">🎓 Learning Journey</a>
      <span class="breadcrumb-separator">›</span>
      <span class="breadcrumb-current" style="color: ${stage.color}">
        ${stage.icon} ${stage.name}
      </span>
    </div>
    
    <div class="stage-next-step">
      <div class="next-step-content">
        <div class="next-step-text">
          <div class="next-step-label">Next Step</div>
          <div class="next-step-title">
            ${stage.nextIcon} ${stage.nextLabel}
          </div>
          <div class="next-step-hint">
            Continue your learning journey
          </div>
        </div>
        <a href="${getNextPageUrl(stage.next)}" class="next-step-button" style="background: ${stage.color}">
          Continue →
        </a>
      </div>
    </div>
    
    <div class="stage-related-tools">
      <div class="related-tools-label">Related Tools</div>
      <div class="related-tools-grid">
        ${stage.relatedTools.map(tool => `
          <a href="${tool.href}" class="related-tool-card">
            <span class="tool-icon">${tool.icon}</span>
            <span class="tool-name">${tool.name}</span>
          </a>
        `).join('')}
      </div>
    </div>
  `;
  
  // Add styles
  const styles = document.createElement('style');
  styles.textContent = `
    .stage-navigation-container {
      margin: 3rem 0 2rem;
      padding: 2rem;
      background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
      border-radius: 12px;
      border: 1px solid #e0e0e0;
    }
    
    .stage-breadcrumb {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
    }
    
    .breadcrumb-link {
      color: #2c5aa0;
      text-decoration: none;
      transition: color 0.2s;
    }
    
    .breadcrumb-link:hover {
      color: #4a90e2;
      text-decoration: underline;
    }
    
    .breadcrumb-separator {
      color: #95a5a6;
    }
    
    .breadcrumb-current {
      font-weight: 600;
    }
    
    .stage-next-step {
      background: white;
      border: 2px solid #e0e0e0;
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      transition: all 0.3s;
    }
    
    .stage-next-step:hover {
      border-color: #4a90e2;
      box-shadow: 0 4px 12px rgba(74, 144, 226, 0.1);
    }
    
    .next-step-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
    }
    
    .next-step-text {
      flex: 1;
    }
    
    .next-step-label {
      font-size: 0.85rem;
      color: #7f8c8d;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
    }
    
    .next-step-title {
      font-size: 1.3rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 0.25rem;
    }
    
    .next-step-hint {
      font-size: 0.9rem;
      color: #95a5a6;
    }
    
    .next-step-button {
      padding: 0.75rem 2rem;
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 600;
      transition: all 0.2s;
      white-space: nowrap;
    }
    
    .next-step-button:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.2);
      color: white;
    }
    
    .stage-related-tools {
      margin-top: 1.5rem;
    }
    
    .related-tools-label {
      font-size: 0.9rem;
      color: #7f8c8d;
      margin-bottom: 0.75rem;
      font-weight: 600;
    }
    
    .related-tools-grid {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }
    
    .related-tool-card {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.25rem;
      background: white;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      text-decoration: none;
      color: #2c3e50;
      transition: all 0.2s;
    }
    
    .related-tool-card:hover {
      border-color: #4a90e2;
      background: #f8f9fa;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }
    
    .related-tool-card .tool-icon {
      font-size: 1.2rem;
    }
    
    .related-tool-card .tool-name {
      font-size: 0.9rem;
      font-weight: 500;
    }
    
    @media (max-width: 768px) {
      .next-step-content {
        flex-direction: column;
        align-items: stretch;
        text-align: center;
      }
      
      .next-step-button {
        text-align: center;
      }
      
      .related-tools-grid {
        flex-direction: column;
      }
    }
  `;
  
  document.head.appendChild(styles);
  
  // Insert at the end of main content
  const mainContent = document.querySelector('.dashboard-container, .wiki-container, .highlights-container, .workspace-container') || document.querySelector('main') || document.body;
  mainContent.appendChild(container);
}

function getNextPageUrl(stageKey) {
  const stagePages = {
    write: 'wiki.html',
    review: 'highlights.html',
    enhance: 'ai-wiki.html',
    attain: 'spaced-repetition.html',
    update: 'digests/index.html'
  };
  return stagePages[stageKey] || 'learning-journey.html';
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initStageNavigation);
} else {
  initStageNavigation();
}
