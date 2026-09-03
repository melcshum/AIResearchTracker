# 5-Stage Knowledge Construction Cycle - Full Audit & Implementation Status

**Date:** September 2, 2026  
**Based on:** Conference paper "From Notes to Knowledge: AI Wiki Companion for Learner-in-the-Loop Knowledge Construction"  
**Status:** Phase 1 & 2 Complete, Phase 3 Pending

---

## Executive Summary

✅ **Completed:**
- Phase 1: UI alignment to 5-stage cycle (Construct → Reflect → Scaffold → Consolidate → Revisit)
- Phase 2: Local LLM integration for Reflect and Scaffold modes
- Core pages updated: `wiki.md`, `ai-agents.md`, `admin.md`, `AGENTS.md`

⚠️ **Critical Violations of DP2 (Scaffold Rather Than Substitute):**
- `spaced-repetition.md` - Shows content instead of requiring recall
- `ai-study-guide.md` - Auto-generates content instead of scaffolding learner construction

📋 **Partially Aligned:**
- `paper-reader.md` - Has concept validation but no AI scaffolding
- `ai-wiki.md` - Partial alignment, missing metacognitive prompts

---

## Detailed Page-by-Page Audit

### 1. ✅ `public/wiki.md` - FULLY ALIGNED

**Status:** Phase 1 & 2 Complete  
**Design Principles:** DP1 ✓, DP2 ✓, DP3 ✓, DP4 ✓

**What's Implemented:**
- ✅ 5-stage workflow guide (Construct → Reflect → Scaffold → Consolidate → Revisit)
- ✅ AI Companion panel with 5 modes
- ✅ LLM integration for Reflect mode (metacognitive questions)
- ✅ LLM integration for Scaffold mode (gap detection)
- ✅ Prompt Before Provide interaction model
- ✅ Connection suggestions (when requested)
- ✅ Version history tracking (UI ready)

**How It Works:**
1. **Construct Mode:** Learner writes explanation in textarea
2. **Reflect Mode:** Click "Generate Reflection Questions" → LLM asks 2-3 metacognitive questions
3. **Scaffold Mode:** Click "Identify Gaps" → LLM detects missing concepts and suggests questions
4. **Consolidate Mode:** UI ready for retrieval practice (not yet implemented)
5. **Revisit Mode:** UI ready for connection suggestions (not yet implemented)

**API Endpoint:** `/api/wiki/companion` (Flask server on port 5001)  
**LLM Model:** gemma4-64k via Ollama (local)

**Test Results:**
- Reflect mode: Successfully generates 3 high-quality questions in ~21 seconds
- Scaffold mode: Detects missing terms (vector database, embeddings, reranking)
- JSON parsing working with strict prompts

---

### 2. ❌ `public/spaced-repetition.md` - CRITICAL DP2 VIOLATION

**Status:** Misaligned  
**Design Principles:** DP1 ✓, DP2 ✗, DP3 ✗, DP4 ✓

**Current Behavior:**
- Shows abstract + notes + AI summary upfront
- Learner sees full content before attempting recall
- No retrieval practice prompt
- Violates "Scaffold Rather Than Substitute" principle

**What Should Happen (5-Stage Cycle):**
1. **Consolidate Mode:** AI hides the paper content
2. **Prompt:** "Explain this paper's main contribution without consulting your notes"
3. **Learner writes** their recall attempt
4. **AI compares** to original and provides feedback
5. **Only then** shows abstract + notes for verification

**Required Changes:**
```diff
- Show abstract + notes + AI summary immediately
+ Show retrieval prompt first
+ Require learner to write recall attempt
+ Compare recall to original
+ Provide formative feedback
+ THEN show content for verification
```

**Implementation Priority:** HIGH (Core to DP2)

---

### 3. ❌ `public/ai-study-guide.md` - CRITICAL DP2 VIOLATION

**Status:** Misaligned  
**Design Principles:** DP1 ✗, DP2 ✗, DP3 ✗, DP4 ✓

**Current Behavior:**
- Auto-generates study materials from papers
- Generates concepts, flashcards, connections automatically
- Learner is passive recipient
- Violates "Learner Ownership" and "Scaffold Rather Than Substitute"

**What Should Happen:**
1. **Construct Mode:** Prompt learner to write their own study guide
2. **Reflect Mode:** AI asks: "What concepts do you think are most important?"
3. **Scaffold Mode:** AI suggests: "Consider adding X, Y, Z based on your papers"
4. **Learner constructs** their own guide with AI support
5. **AI compares** learner's guide to generated one, highlights gaps

**Required Changes:**
```diff
- Auto-generate study guide with AI
+ Prompt learner to create their own guide first
+ AI provides scaffolding questions
+ AI suggests concepts (but learner selects)
+ AI compares learner's guide to reference
+ Learner revises based on feedback
```

**Implementation Priority:** HIGH (Core to DP1 & DP2)

---

### 4. ⚠️ `public/paper-reader.md` - PARTIALLY ALIGNED

**Status:** Partial alignment  
**Design Principles:** DP1 ✓, DP2 Partial, DP3 ✗, DP4 ✓

**Current Features:**
- ✅ Highlighting, notes, questions
- ✅ Concept validation button (🧠)
- ✅ Feedback rating for AI summaries
- ❌ No metacognitive prompts before validation
- ❌ No scaffolded concept extraction

**What Should Happen:**
1. **Before Validation:** Prompt learner: "What key concepts do you see in this paper?"
2. **Learner writes** their concept list
3. **AI compares** to generated concepts
4. **AI asks:** "Why did you include/exclude concept X?"
5. **Learner revises** based on reflection

**Required Changes:**
```diff
- Show AI concepts immediately on validation
+ Prompt learner to identify concepts first
+ Learner writes their list
+ AI compares and asks reflective questions
+ THEN show AI-generated concepts
```

**Implementation Priority:** MEDIUM

---

### 5. ⚠️ `public/ai-wiki.md` - PARTIALLY ALIGNED

**Status:** Partial alignment  
**Design Principles:** DP1 ✓, DP2 Partial, DP3 Partial, DP4 ✓

**Current Features:**
- ✅ "Learn by Building" approach
- ✅ 3 modes (Build, Teach, Compare)
- ✅ Concept selector + textarea
- ❌ Missing AI metacognitive prompts
- ❌ No LLM integration for gap detection

**What Should Happen:**
- Integrate with `wiki.md`'s 5-stage cycle
- Add AI Companion panel with LLM calls
- Implement Reflect and Scaffold modes

**Required Changes:**
```diff
- 3 modes without AI prompts
+ 5-stage cycle with AI Companion
+ LLM integration for Reflect mode
+ LLM integration for Scaffold mode
+ Connection suggestions
```

**Implementation Priority:** MEDIUM

---

### 6. ✅ `public/topics/ai-agents.md` - FULLY ALIGNED

**Status:** Updated  
**Design Principles:** DP1 ✓, DP2 ✓, DP3 ✓, DP4 ✓

**What's Implemented:**
- ✅ Subtitle: "Learner-in-the-loop knowledge construction with AI as metacognitive scaffold"
- ✅ Featured Conference Paper section
- ✅ 5-stage workflow cycle
- ✅ CSS styling for featured paper

**No Changes Needed**

---

### 7. ✅ `private/admin.md` - FULLY ALIGNED

**Status:** Updated  
**Design Principles:** DP1 ✓, DP2 ✓, DP3 ✓, DP4 ✓

**What's Implemented:**
- ✅ Project Aim: "learner-in-the-loop personal knowledge environment"
- ✅ Design Principles (DP1-DP4) documented
- ✅ 5-stage cycle described
- ✅ Prompt Before Provide model

**No Changes Needed**

---

### 8. ✅ `private/AGENTS.md` - FULLY ALIGNED

**Status:** Updated  
**Design Principles:** DP1 ✓, DP2 ✓, DP3 ✓, DP4 ✓

**What's Implemented:**
- ✅ Mission: "learner-in-the-loop personal knowledge environment"
- ✅ Core Philosophy: "AI scaffolds rather than substitutes"
- ✅ 5-stage cycle documented
- ✅ Success Criteria aligned

**No Changes Needed**

---

## Implementation Gap Analysis

### Missing Framework Elements

| Element | Status | Priority | Location |
|---------|--------|----------|----------|
| AI Companion with metacognitive prompts | ✅ Implemented | - | `wiki.md` |
| Prompt Before Provide interaction | ✅ Implemented | - | `wiki.md` |
| Knowledge gap detection | ✅ Implemented | - | `wiki.md` + LLM |
| Connection recommendations | ⚠️ UI Ready | MEDIUM | `wiki.md` |
| **Retrieval practice** | ❌ Missing | HIGH | `spaced-repetition.md` |
| **Learner-constructed study materials** | ❌ Missing | HIGH | `ai-study-guide.md` |
| Knowledge evolution tracking | ⚠️ UI Ready | LOW | `wiki.md` |
| Formative evaluation tracking | ❌ Missing | LOW | - |

### Design Principle Violations

| Page | DP1 (Ownership) | DP2 (Scaffold) | DP3 (Reflection) | DP4 (Integration) |
|------|-----------------|----------------|------------------|-------------------|
| `wiki.md` | ✅ | ✅ | ✅ | ✅ |
| `spaced-repetition.md` | ✅ | ❌ | ❌ | ✅ |
| `ai-study-guide.md` | ❌ | ❌ | ❌ | ✅ |
| `paper-reader.md` | ✅ | ⚠️ | ❌ | ✅ |
| `ai-wiki.md` | ✅ | ⚠️ | ⚠️ | ✅ |

---

## Phase 3 Implementation Plan

### Phase 3A: Fix Critical DP2 Violations (Next Session)

**Goal:** Reframe `spaced-repetition.md` and `ai-study-guide.md` to honor DP2

**Tasks:**

#### Task 1: Reframe Spaced Repetition (2-3 hours)
1. Add "Retrieve First" toggle in review card
2. Show prompt: "Explain this paper's contribution without consulting notes"
3. Require learner to write recall attempt
4. Add "Reveal Notes" button (opt-in)
5. Compare recall to original, provide feedback
6. Track accuracy in `userData.spacedRepetition`

**Expected Behavior:**
```
[Before]
┌─────────────────────────────┐
│ Paper: "RAG for Agents"     │
│ Abstract: [visible]         │
│ Notes: [visible]            │
│ AI Summary: [visible]       │
│ [Rate: Easy/Moderate/Hard]  │
└─────────────────────────────┘

[After]
┌─────────────────────────────┐
│ Paper: "RAG for Agents"     │
│                             │
│ 📝 Recall Prompt:           │
│ "Explain this paper's main  │
│ contribution without        │
│ consulting your notes."     │
│                             │
│ [Textarea for recall]       │
│ [Reveal Notes] [Submit]     │
└─────────────────────────────┘
```

#### Task 2: Reframe AI Study Guide (2-3 hours)
1. Change from "Auto-generate" to "Build Your Guide"
2. Prompt: "What concepts do you want to study?"
3. Learner writes concept list
4. AI suggests: "Consider adding X, Y based on your papers"
5. Learner constructs flashcards (AI provides hints)
6. AI compares learner's guide to reference, highlights gaps

**Expected Behavior:**
```
[Before]
┌─────────────────────────────┐
│ [Generate Study Guide]      │
│                             │
│ AI generates:               │
│ - Key Concepts (auto)       │
│ - Flashcards (auto)         │
│ - Connections (auto)        │
└─────────────────────────────┘

[After]
┌─────────────────────────────┐
│ Build Your Study Guide      │
│                             │
│ 1. What concepts matter?    │
│ [Learner writes list]       │
│ AI suggests: "Consider X"   │
│                             │
│ 2. Create flashcards        │
│ [Learner writes Q/A]        │
│ AI hints: "Try asking..."   │
│                             │
│ [Compare to Reference]      │
└─────────────────────────────┘
```

### Phase 3B: Add Remaining 5-Stage Features (Following Session)

**Goal:** Complete Consolidate and Revisit modes

**Tasks:**

#### Task 3: Implement Consolidate Mode in wiki.md (1-2 hours)
1. Add "Hide Entry" toggle in Consolidate mode
2. Prompt: "Explain this concept without the wiki"
3. Learner writes from memory
4. AI compares to original entry
5. Provide formative feedback
6. Track mastery over time

#### Task 4: Implement Revisit Mode in wiki.md (1-2 hours)
1. When learner adds new concept, trigger Revisit mode
2. AI retrieves related prior entries
3. Prompt: "Does this require revising your earlier entry on X?"
4. Show version history: "v1 → v2 → v3"
5. Track knowledge evolution

#### Task 5: Add Formative Evaluation Tracking (2 hours)
1. Log learner responses to AI (accept/reject/modify)
2. Track time spent in each mode
3. Calculate metacognitive engagement score
4. Display progress dashboard

---

## Technical Architecture Updates

### Current State
```
┌─────────────────┐
│   wiki.md       │ ← 5-stage cycle, LLM integration
└────────┬────────┘
         │
         │ fetch('/api/wiki/companion')
         │
         ▼
┌─────────────────┐
│  api_server.py  │ ← Flask on port 5001
│  /api/wiki/     │
│  companion      │
└────────┬────────┘
         │
         │ requests.post()
         │
         ▼
┌─────────────────┐
│  Ollama         │ ← gemma4-64k (local)
│  localhost:11434│
└─────────────────┘
```

### Required Updates

#### For Spaced Repetition:
```javascript
// Add to spaced-repetition.md
async function showRecallPrompt(paper) {
  // Hide content
  document.getElementById('paperAbstract').style.display = 'none';
  document.getElementById('paperNotes').style.display = 'none';
  
  // Show prompt
  const promptHTML = `
    <div class="recall-prompt">
      <h3>📝 Recall Practice</h3>
      <p>Explain "${paper.title}" without consulting your notes:</p>
      <textarea id="recallAttempt" rows="6"></textarea>
      <button onclick="submitRecall()">Submit Recall</button>
      <button onclick="revealNotes()">Reveal Notes</button>
    </div>
  `;
  document.getElementById('reviewCard').innerHTML = promptHTML;
}

async function submitRecall() {
  const recall = document.getElementById('recallAttempt').value;
  const original = getOriginalNotes(paperId);
  
  // Call LLM to compare
  const response = await fetch('/api/wiki/companion', {
    method: 'POST',
    body: JSON.stringify({
      mode: 'consolidate',
      original: original,
      recall: recall
    })
  });
  
  const feedback = await response.json();
  displayFeedback(feedback);
}
```

#### For AI Study Guide:
```javascript
// Replace auto-generation with scaffolded construction
async function scaffoldStudyGuide() {
  // Step 1: Learner identifies concepts
  const learnerConcepts = await promptConcepts();
  
  // Step 2: AI suggests additions
  const suggestions = await suggestConcepts(learnerConcepts);
  
  // Step 3: Learner creates flashcards
  const flashcards = await scaffoldFlashcards(learnerConcepts);
  
  // Step 4: AI compares to reference
  const gaps = await compareGuides(learnerConcepts, referenceGuide);
  
  displayGuidance(gaps);
}
```

---

## Success Metrics

### Phase 3A Metrics
- [ ] `spaced-repetition.md` requires recall before showing content
- [ ] `ai-study-guide.md` requires learner construction before AI suggestions
- [ ] Both pages honor DP2 (Scaffold Rather Than Substitute)
- [ ] Formative feedback provided for recall attempts

### Phase 3B Metrics
- [ ] Consolidate mode functional in wiki.md
- [ ] Revisit mode suggests connections
- [ ] Version history displayed (v1 → v2 → v3)
- [ ] Formative evaluation tracking implemented
- [ ] Metacognitive engagement dashboard

---

## Known Issues & Risks

### Current Issues
1. **LLM Response Time:** ~15-20 seconds per call
   - **Mitigation:** Add loading states, consider smaller model
   
2. **JSON Parsing:** LLM sometimes repeats text
   - **Mitigation:** Stricter prompts, post-processing

3. **No Fallback:** If Ollama unavailable, features fail
   - **Mitigation:** Add graceful degradation (static prompts)

### Risks
1. **Learner Resistance:** May prefer auto-generation over scaffolded construction
   - **Mitigation:** Explain DP2 rationale, show value of active construction

2. **Complexity:** 5-stage cycle may overwhelm some learners
   - **Mitigation:** Progressive disclosure, optional modes

3. **Performance:** Local LLM may be slow on older hardware
   - **Mitigation:** Offer cloud LLM option (with privacy notice)

---

## Next Steps

### Immediate (This Session)
✅ Phase 1 Complete: UI alignment to 5-stage cycle  
✅ Phase 2 Complete: LLM integration for Reflect/Scaffold modes  
📋 **Review audit report**

### Next Session
🔲 **Phase 3A: Fix Critical DP2 Violations**
- Reframe `spaced-repetition.md` to "retrieve first"
- Reframe `ai-study-guide.md` to "scaffold construction"

### Following Session
🔲 **Phase 3B: Complete 5-Stage Cycle**
- Implement Consolidate mode
- Implement Revisit mode
- Add formative evaluation tracking

---

## References

- Conference paper: `public/conference-papers/ai-wiki-companion-2026.md`
- Design principles: DP1-DP4 (see `private/AGENTS.md`)
- 5-stage cycle: Construct → Reflect → Scaffold → Consolidate → Revisit
- Implementation plan: `private/WIKI_ENHANCEMENT_PLAN.md`
- Phase 1 summary: `private/WIKI_PHASE1_SUMMARY.md`
- Phase 2 summary: `private/WIKI_PHASE2_SUMMARY.md`

---

**Audit Complete.** Ready to proceed with Phase 3A implementation.
