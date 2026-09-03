# Implementation Plan: AI Wiki Companion UI/UX Enhancement

**Date:** 2026-09-03  
**Status:** Implementation Phase

---

## Decisions Made

1. ✅ **New Tab:** "Knowledge Construction" (replaces "Learn by Building")
2. ✅ **Sidebar:** Collapsible AI Companion sidebar
3. ✅ **Flow:** Flexible stage navigation (can skip stages)
4. ✅ **Progress:** Visual arrow diagram showing 5 stages

---

## Phase 1: HTML Restructuring

### Task 1.1: Add Knowledge Construction Tab

**Location:** ai-wiki.html (after Browse tab, before Graph tab)

**Structure:**
```html
<!-- Knowledge Construction Tab -->
<div id="knowledgeConstructionTab" class="tab-content">
  <!-- Stage Progress Arrow Diagram -->
  <div class="stage-progress-container">
    <div class="stage-arrow" data-stage="construct">
      <span class="stage-number">1</span>
      <span class="stage-label">Construct</span>
    </div>
    <div class="stage-arrow" data-stage="reflect">
      <span class="stage-number">2</span>
      <span class="stage-label">Reflect</span>
    </div>
    <div class="stage-arrow" data-stage="scaffold">
      <span class="stage-number">3</span>
      <span class="stage-label">Scaffold</span>
    </div>
    <div class="stage-arrow" data-stage="consolidate">
      <span class="stage-number">4</span>
      <span class="stage-label">Consolidate</span>
    </div>
    <div class="stage-arrow" data-stage="revisit">
      <span class="stage-number">5</span>
      <span class="stage-label">Revisit</span>
    </div>
  </div>
  
  <!-- Main Content Area -->
  <div class="knowledge-construction-main">
    <!-- Concept Selector -->
    <div class="concept-selector-section">
      <label>Select a concept:</label>
      <select id="kcConceptSelect">
        <option value="">– Choose a concept –</option>
      </select>
    </div>
    
    <!-- Stage Content Container -->
    <div id="stageContent" class="stage-content">
      <!-- Dynamic content based on current stage -->
    </div>
  </div>
  
  <!-- Collapsible AI Companion Sidebar -->
  <div id="aiCompanionSidebar" class="ai-companion-sidebar">
    <button class="sidebar-toggle" onclick="toggleSidebar()">
      <span class="toggle-icon">◀</span>
    </button>
    <div class="sidebar-content">
      <!-- AI Companion content (from ai-companion.js) -->
    </div>
  </div>
</div>
```

### Task 1.2: Remove "Learn by Building" Tab

**Action:** Delete or comment out the existing "Learn by Building" tab (lines 329-436)

### Task 1.3: Add Sidebar Toggle Button

**Location:** Inside the AI Companion sidebar

**Functionality:**
- Toggle sidebar open/closed
- Change icon direction (◀ when open, ▶ when closed)
- Smooth transition animation

---

## Phase 2: CSS Enhancements

### Task 2.1: Stage Progress Arrow Diagram

**Styles needed:**
```css
.stage-progress-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 20px;
}

.stage-arrow {
  position: relative;
  padding: 12px 24px 12px 40px;
  background: #e0e0e0;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  clip-path: polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%, 20px 50%);
}

.stage-arrow:first-child {
  clip-path: polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%);
  padding-left: 24px;
}

.stage-arrow.active {
  background: #4a90d9;
  color: white;
}

.stage-arrow.completed {
  background: #4caf50;
  color: white;
}

.stage-number {
  font-weight: bold;
  margin-right: 8px;
}

.stage-label {
  font-size: 14px;
}
```

### Task 2.2: Collapsible Sidebar

**Styles needed:**
```css
.ai-companion-sidebar {
  position: fixed;
  right: 0;
  top: 60px;
  width: 350px;
  height: calc(100vh - 60px);
  background: white;
  border-left: 2px solid #e0e0e0;
  box-shadow: -2px 0 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  z-index: 1000;
  display: flex;
  flex-direction: column;
}

.ai-companion-sidebar.collapsed {
  transform: translateX(310px); /* Only show toggle button */
}

.sidebar-toggle {
  position: absolute;
  left: -40px;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 60px;
  background: #4a90d9;
  color: white;
  border: none;
  border-radius: 8px 0 0 8px;
  cursor: pointer;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar-toggle:hover {
  background: #3a7bc8;
}

.sidebar-content {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}
```

### Task 2.3: Stage Content Area

**Styles needed:**
```css
.knowledge-construction-main {
  flex: 1;
  padding: 20px;
  margin-right: 350px; /* Account for sidebar */
  transition: margin-right 0.3s ease;
}

.ai-companion-sidebar.collapsed ~ .knowledge-construction-main {
  margin-right: 40px; /* Only toggle button width */
}

.stage-content {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 24px;
  min-height: 400px;
}

.concept-selector-section {
  margin-bottom: 20px;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 8px;
}
```

### Task 2.4: Responsive Design

**Mobile styles:**
```css
@media (max-width: 768px) {
  .stage-progress-container {
    flex-direction: column;
    gap: 8px;
  }
  
  .stage-arrow {
    width: 100%;
    clip-path: polygon(0 0, calc(100% - 15px) 0, 100% 50%, calc(100% - 15px) 100%, 0 100%, 15px 50%);
  }
  
  .ai-companion-sidebar {
    width: 100%;
    height: 50vh;
    top: auto;
    bottom: 0;
  }
  
  .knowledge-construction-main {
    margin-right: 0;
  }
}
```

---

## Phase 3: JavaScript Integration

### Task 3.1: Initialize AI Companion

**Code:**
```javascript
// Initialize AI Companion when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  const aiCompanion = new AICompanion({
    currentPage: 'ai-wiki',
    onModeChange: (mode) => {
      updateStageProgress(mode);
      updateStageContent(mode);
    }
  });
  
  // Initialize with DOM elements
  aiCompanion.init(
    '#aiCompanionModes',      // Mode buttons container
    '#aiCompanionContent',    // Content container
    '#aiCompanionLoading'     // Loading indicator
  );
  
  // Load concepts into selector
  loadConceptsForKC();
});
```

### Task 3.2: Stage Progress Update

**Code:**
```javascript
function updateStageProgress(currentStage) {
  const stages = ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit'];
  const currentIndex = stages.indexOf(currentStage);
  
  document.querySelectorAll('.stage-arrow').forEach((arrow, index) => {
    arrow.classList.remove('active', 'completed');
    
    if (index < currentIndex) {
      arrow.classList.add('completed');
    } else if (index === currentIndex) {
      arrow.classList.add('active');
    }
  });
}
```

### Task 3.3: Stage Content Update

**Code:**
```javascript
function updateStageContent(stage) {
  const contentDiv = document.getElementById('stageContent');
  
  switch(stage) {
    case 'construct':
      contentDiv.innerHTML = `
        <h3>✍️ Construct: Write Your Explanation</h3>
        <p>Start by explaining this concept in your own words. Don't worry about being perfect - this is your starting point.</p>
        <textarea id="constructTextarea" class="stage-textarea" placeholder="Explain the concept in your own words..."></textarea>
        <button onclick="saveConstruct()" class="btn-primary">Save & Continue to Reflect</button>
      `;
      break;
      
    case 'reflect':
      contentDiv.innerHTML = `
        <h3>🤔 Reflect: Examine Your Understanding</h3>
        <p>Review your explanation and consider these questions:</p>
        <div id="reflectionPrompts"></div>
        <button onclick="continueToScaffold()" class="btn-primary">Continue to Scaffold</button>
      `;
      break;
      
    // ... other stages
  }
}
```

### Task 3.4: Sidebar Toggle

**Code:**
```javascript
function toggleSidebar() {
  const sidebar = document.getElementById('aiCompanionSidebar');
  const toggleIcon = sidebar.querySelector('.toggle-icon');
  
  sidebar.classList.toggle('collapsed');
  
  if (sidebar.classList.contains('collapsed')) {
    toggleIcon.textContent = '▶';
  } else {
    toggleIcon.textContent = '◀';
  }
}
```

### Task 3.5: Flexible Stage Navigation

**Code:**
```javascript
// Allow clicking on any stage arrow to navigate
document.querySelectorAll('.stage-arrow').forEach(arrow => {
  arrow.addEventListener('click', () => {
    const stage = arrow.dataset.stage;
    aiCompanion.switchMode(stage);
  });
});
```

---

## Phase 4: Workflow Alignment

### Task 4.1: Concept Loading

**Code:**
```javascript
async function loadConceptsForKC() {
  const select = document.getElementById('kcConceptSelect');
  
  // Fetch concepts from API or use existing data
  const concepts = await fetchConcepts();
  
  concepts.forEach(concept => {
    const option = document.createElement('option');
    option.value = concept.id;
    option.textContent = concept.name;
    select.appendChild(option);
  });
  
  // Handle concept selection
  select.addEventListener('change', (e) => {
    const conceptId = e.target.value;
    if (conceptId) {
      aiCompanion.currentConcept = conceptId;
      updateStageContent('construct');
    }
  });
}
```

### Task 4.2: Stage Validation

**Code:**
```javascript
function saveConstruct() {
  const textarea = document.getElementById('constructTextarea');
  const explanation = textarea.value.trim();
  
  if (!explanation) {
    alert('Please write your explanation first');
    return;
  }
  
  aiCompanion.userExplanation = explanation;
  aiCompanion.switchMode('reflect');
}

function continueToScaffold() {
  // Optional: validate that reflection was completed
  aiCompanion.switchMode('scaffold');
}
```

---

## Phase 5: Testing & Refinement

### Test Checklist

- [ ] All 5 stages are clickable in the arrow diagram
- [ ] Sidebar opens/closes smoothly
- [ ] Stage progress updates correctly
- [ ] Content updates for each stage
- [ ] Concept selector works
- [ ] Flexible navigation (can skip stages)
- [ ] Mobile responsive design works
- [ ] No CSS conflicts with existing styles
- [ ] AI Companion integrates properly
- [ ] All API calls work correctly

---

## Implementation Order

1. **HTML:** Add Knowledge Construction tab structure
2. **HTML:** Remove/comment out "Learn by Building" tab
3. **CSS:** Add stage progress arrow styles
4. **CSS:** Add collapsible sidebar styles
5. **CSS:** Add stage content styles
6. **CSS:** Add responsive styles
7. **JS:** Initialize AI Companion
8. **JS:** Add stage progress update function
9. **JS:** Add stage content update function
10. **JS:** Add sidebar toggle function
11. **JS:** Add flexible navigation
12. **JS:** Add concept loading
13. **JS:** Add stage validation
14. **Test:** All features
15. **Refine:** Based on testing

---

## Estimated Time

- Phase 1 (HTML): 30 minutes
- Phase 2 (CSS): 45 minutes
- Phase 3 (JS): 60 minutes
- Phase 4 (Workflow): 30 minutes
- Phase 5 (Testing): 30 minutes

**Total:** ~3 hours

---

## Next Steps

**Ready to proceed?** I'll start with Phase 1: HTML restructuring.

**Questions:**
1. Should I proceed with the implementation now?
2. Any specific preferences for the arrow diagram style?
3. Should the sidebar default to open or closed?
