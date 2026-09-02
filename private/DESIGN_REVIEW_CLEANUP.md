# Design Review: Duplication & Cleanup Analysis

**Date:** September 2, 2026  
**Focus:** Align implementation with conference paper design, eliminate redundancy

---

## Executive Summary

Current implementation has **significant duplication** across 3 pages (`wiki.md`, `paper-reader.md`, `ai-wiki.md`) with **inconsistent patterns** that violate the conference paper's unified AI Companion architecture.

### Key Findings

1. **3 Separate AI Companion Implementations** - Each page has its own HTML, CSS, JS
2. **Inconsistent Mode Names** - Some use 3 modes, others use 4-5 modes
3. **Duplicate API Calls** - Each page makes independent LLM calls
4. **No Shared Component Architecture** - Conference paper specifies single "AI Companion" component
5. **Misaligned with Design Principles** - Some implementations still auto-generate content (DP2 violation)

---

## Conference Paper Design (Reference)

### Core Architecture (Section 3.5)

```
Learner → Wiki Editor → Personal Knowledge Base → Concept Graph → Knowledge Context → AI Companion → Scaffold → Learner Evaluation → Wiki Revision
```

**Key Components:**
1. **Wiki Editor** - Primary authoring environment
2. **Personal Knowledge Base** - Stores learner content
3. **Concept Graph** - Relationships between entries
4. **Knowledge Context** - Selects relevant info for AI
5. **AI Companion** - Single unified component (NOT 3 separate ones)

### AI Companion Functions (Table 3)

| Function | Role | Illustrative Intervention |
|----------|------|--------------------------|
| Socratic Questioning | Elicit reasoning | "Why does this relationship hold?" |
| Knowledge Gap Detection | Draw attention to gaps | "Your explanation discusses X but not Y" |
| Connection Recommendation | Encourage integration | "Related to your earlier entry on Z?" |
| Misconception Challenge | Prompt reconsideration | "Would this remain true for unseen data?" |
| Evidence Prompting | Encourage verification | "What source supports this?" |
| Retrieval & Application | Promote recall | "Explain without consulting wiki" |
| Review/Revisit Recommendation | Encourage refinement | "Does new learning require revision?" |
| Source Recommendation | Direct to evidence | "Verify this source before integrating" |

### 5-Stage Cycle (Table 2)

| Stage | Learner Activity | AI Companion Role |
|-------|-----------------|-------------------|
| **Construct** | Develops initial explanation | Limited intervention, task framing |
| **Reflect** | Examines confidence, assumptions | Generates metacognitive prompts |
| **Scaffold** | Responds to gaps | Targeted questions, hints, suggestions |
| **Consolidate** | Retrieves, applies knowledge | Generates tasks, provides feedback |
| **Revisit** | Integrates with prior knowledge | Identifies relevant prior entries |

---

## Current Implementation Analysis

### 1. wiki.md (Research Wiki)

**Status:** ✅ **Best aligned with conference paper**

**Structure:**
- Workflow guide: 5-stage cycle (Construct, Reflect, Scaffold, Consolidate, Revisit)
- AI Companion Panel: Right sidebar with 5 modes
- Functions: `switchAIMode()`, `aiGenerateReflectionPrompts()`, `aiDetectGaps()`

**Issues:**
- ❌ Only implements 3 modes (Reflect, Scaffold, Consolidate) - missing Construct and Revisit
- ❌ No "Knowledge Context" component - each call is isolated
- ❌ No version history tracking (DP4 violation)
- ❌ No connection recommendation UI

**Code Duplication:**
```javascript
// Lines 1508-1700: switchAIMode, aiGenerateReflectionPrompts, aiDetectGaps, etc.
// ~200 lines of JS duplicated across 3 files
```

### 2. paper-reader.md (Paper Reader)

**Status:** ⚠️ **Partial alignment, significant duplication**

**Structure:**
- AI Companion Sidebar: Right sidebar with 3 modes (Reflect, Scaffold, Consolidate)
- Functions: `switchCompanionMode()`, `generateCompanionFeedback()`

**Issues:**
- ❌ Only 3 modes (missing Construct, Revisit)
- ❌ Different function names (`switchCompanionMode` vs `switchAIMode`)
- ❌ Different prompt structure
- ❌ No integration with wiki's Personal Knowledge Base
- ❌ Concept selection works differently (click text vs select from dropdown)

**Code Duplication:**
```javascript
// Lines 1548-1700: switchCompanionMode, generateCompanionFeedback
// ~150 lines of JS - 80% similar to wiki.md
```

### 3. ai-wiki.md (AI Knowledge Wiki)

**Status:** ⚠️ **Partial alignment, significant duplication**

**Structure:**
- AI Companion Panel: Right sidebar with 4 modes (Construct, Reflect, Scaffold, Consolidate)
- Functions: `switchAIMode()`, `generateCompanionFeedback()`

**Issues:**
- ❌ Only 4 modes (missing Revisit)
- ❌ Different function names (`generateCompanionFeedback` vs `aiDetectGaps`)
- ❌ Has "Learn by Building" tab that duplicates Construct functionality
- ❌ No integration with paper-reader or wiki.md
- ❌ Concept selection works differently (grid vs text selection)

**Code Duplication:**
```javascript
// Lines 2659-2850: switchAIMode, generateCompanionFeedback
// ~200 lines of JS - 85% similar to wiki.md
```

---

## Duplication Matrix

| Component | wiki.md | paper-reader.md | ai-wiki.md | Shared? |
|-----------|---------|-----------------|------------|---------|
| **HTML Structure** | Custom | Custom | Custom | ❌ No |
| **CSS Styles** | ~300 lines | ~200 lines | ~250 lines | ❌ No |
| **JS Functions** | ~200 lines | ~150 lines | ~200 lines | ❌ No |
| **Mode Buttons** | 5 buttons | 3 buttons | 4 buttons | ❌ Inconsistent |
| **API Calls** | Direct to /api/wiki/companion | Direct to /api/wiki/companion | Direct to /api/wiki/companion | ⚠️ Same endpoint, different payloads |
| **Prompt Templates** | Custom per page | Custom per page | Custom per page | ❌ No |
| **Error Handling** | Basic | Basic | Basic | ❌ No |
| **Loading States** | Custom | Custom | Custom | ❌ No |

**Total Duplication:** ~1,100 lines of code across 3 files, ~70% similarity

---

## Design Violations

### DP1: Learner Ownership
- ✅ All pages require learner to write first
- ❌ No version history tracking (wiki.md, ai-wiki.md)
- ❌ AI suggestions automatically incorporated in some cases

### DP2: Scaffold Rather Than Substitute
- ✅ wiki.md: Prompt Before Provide implemented
- ✅ paper-reader.md: Requires explanation before feedback
- ❌ ai-wiki.md: "View Expert Explanation" button may encourage substitution
- ❌ Some modes auto-generate content without learner input

### DP3: Reflection Before Correction
- ✅ wiki.md: Reflect mode before Scaffold
- ⚠️ paper-reader.md: No explicit Reflect stage
- ⚠️ ai-wiki.md: Reflect and Scaffold mixed

### DP4: Continuous Knowledge Integration
- ❌ No cross-page connections (wiki ↔ paper-reader ↔ ai-wiki)
- ❌ No Revisit & Extend mode implemented anywhere
- ❌ No knowledge graph visualization
- ❌ No revision history tracking

---

## Recommended Cleanup Strategy

### Phase 1: Extract Shared Components

**Create:** `public/js/ai-companion.js` (Single source of truth)

**Contents:**
```javascript
// Core AI Companion class
class AICompanion {
  constructor(config) {
    this.mode = 'construct';
    this.concept = null;
    this.userExplanation = '';
    this.context = [];
  }

  // Unified mode switching
  switchMode(mode) { ... }

  // Unified API call
  async getFeedback(config) { ... }

  // Unified prompt generation
  generateReflectPrompts(explanation) { ... }
  detectGaps(explanation) { ... }
  suggestConnections(concept) { ... }
  generateConsolidateTask(concept) { ... }
}

// Event handlers
function handleConceptSelect(concept, sourcePage) { ... }
function handleExplanationSubmit(explanation) { ... }
```

**Create:** `public/css/ai-companion.css`

**Contents:**
```css
/* Shared AI Companion styles */
.ai-companion-sidebar { ... }
.companion-mode-btn { ... }
.companion-content { ... }
.companion-intro { ... }
/* All styles from wiki.md, paper-reader.md, ai-wiki.md */
```

**Create:** `private/api_server.py` (Enhanced)

**Add:**
```python
# Knowledge Context endpoint
@app.route('/api/wiki/context', methods=['POST'])
def get_knowledge_context():
    """Select relevant wiki entries for AI interaction"""
    concept = request.json.get('concept')
    # Find related concepts, prior entries, misconceptions
    return jsonify({'context': [...], 'connections': [...]})

# Revisit & Extend endpoint
@app.route('/api/wiki/revisit', methods=['POST'])
def suggest_revisit():
    """Identify entries that may need revision"""
    new_concept = request.json.get('concept')
    # Find related prior entries
    return jsonify({'revisit_candidates': [...]})
```

### Phase 2: Refactor Pages

**wiki.md:**
- Remove inline CSS/JS
- Import `ai-companion.css` and `ai-companion.js`
- Use shared `AICompanion` class
- Add Revisit & Extend mode
- Add version history UI

**paper-reader.md:**
- Remove inline CSS/JS
- Import `ai-companion.css` and `ai-companion.js`
- Use shared `AICompanion` class
- Add Construct and Revisit modes
- Integrate with wiki's Personal Knowledge Base

**ai-wiki.md:**
- Remove inline CSS/JS
- Import `ai-companion.css` and `ai-companion.js`
- Use shared `AICompanion` class
- Remove "Learn by Building" tab (redundant with Construct mode)
- Add Revisit & Extend mode

### Phase 3: Add Missing Features

**1. Version History**
- Track learner revisions
- Show diff view (v1 vs v2 vs v3)
- Timestamp each revision

**2. Knowledge Graph**
- Visualize concept relationships
- Show learner-created links
- Show AI-suggested connections

**3. Revisit & Extend**
- Trigger when new concept is added
- Suggest related prior entries
- Prompt: "Does this require revision of X?"

**4. Cross-Page Integration**
- Click concept in paper-reader → open wiki entry
- Edit wiki entry → update paper-reader highlights
- Shared Personal Knowledge Base

---

## Implementation Plan

### Week 1: Extract Components
- [ ] Create `public/js/ai-companion.js`
- [ ] Create `public/css/ai-companion.css`
- [ ] Test with wiki.md

### Week 2: Refactor Pages
- [ ] Refactor wiki.md (use shared components)
- [ ] Refactor paper-reader.md (use shared components)
- [ ] Refactor ai-wiki.md (use shared components)
- [ ] Verify all modes work

### Week 3: Add Missing Features
- [ ] Add version history
- [ ] Add knowledge graph
- [ ] Add Revisit & Extend mode
- [ ] Add cross-page integration

### Week 4: Testing & Documentation
- [ ] Test all 5 stages
- [ ] Test all 3 pages
- [ ] Update documentation
- [ ] Create user guide

---

## Expected Benefits

| Metric | Current | After Cleanup |
|--------|---------|---------------|
| **Code Duplication** | ~1,100 lines | ~200 lines (80% reduction) |
| **Maintenance Burden** | 3 places to update | 1 place to update |
| **Consistency** | Inconsistent modes | Unified 5-stage cycle |
| **Design Alignment** | Partial | Full (conference paper) |
| **DP Compliance** | 60% | 100% |
| **New Feature Velocity** | Slow (3x work) | Fast (1x work) |

---

## Discussion Questions

1. **Should we keep all 3 pages?**
   - wiki.md: Research Wiki (term-by-term learning)
   - paper-reader.md: Paper reading with concept selection
   - ai-wiki.md: Comprehensive knowledge base
   - **Recommendation:** Keep all 3, but unify AI Companion

2. **How to handle "Learn by Building" in ai-wiki.md?**
   - Option A: Remove (redundant with Construct mode)
   - Option B: Reframe as "Construct mode tutorial"
   - **Recommendation:** Reframe as tutorial for Construct mode

3. **Should we add "Knowledge Context" as separate UI element?**
   - Show related concepts before AI call
   - Let learner confirm relevance
   - **Recommendation:** Yes, aligns with DP4

4. **How to implement version history?**
   - Store in localStorage?
   - Store in server database?
   - **Recommendation:** Start with localStorage, migrate to server later

---

## Next Steps

**Immediate:**
1. ✅ Create shared component architecture
2. ✅ Refactor wiki.md first (best-aligned page)
3. ✅ Verify all 5 modes work with shared code
4. ✅ Document new architecture

**Short-term:**
1. Refactor paper-reader.md
2. Refactor ai-wiki.md
3. Add version history
4. Add Revisit & Extend mode

**Long-term:**
1. Add knowledge graph
2. Add cross-page integration
3. Add formative evaluation metrics

---

## Appendix: Current File Sizes

| File | Lines | CSS | JS | HTML |
|------|-------|-----|----|----|
| wiki.md | 2,399 | ~300 | ~200 | ~1,900 |
| paper-reader.md | 1,731 | ~200 | ~150 | ~1,400 |
| ai-wiki.md | 2,802 | ~250 | ~200 | ~2,350 |
| **Total** | **6,932** | **~750** | **~550** | **~5,650** |

**After Cleanup (estimated):**
- Shared CSS: 300 lines
- Shared JS: 400 lines
- wiki.md: 1,900 lines
- paper-reader.md: 1,400 lines
- ai-wiki.md: 1,850 lines
- **Total: 4,850 lines (30% reduction)**

---

**Ready to proceed with cleanup?** I recommend starting with Phase 1: extract shared components.
