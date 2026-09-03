# Phase 3A Implementation Plan: Fix Critical DP2 Violations

**Date:** September 2, 2026  
**Goal:** Reframe `spaced-repetition.md` and `ai-study-guide.md` to honor DP2 (Scaffold Rather Than Substitute)  
**Duration:** 2-3 hours  
**Status:** Ready to Execute

---

## Phase 3A Overview

### Problem Statement
Two core pages violate the "Scaffold Rather Than Substitute" principle:
1. **Spaced Repetition** - Shows abstract + notes + AI summary upfront instead of requiring recall first
2. **AI Study Guide** - Auto-generates content instead of scaffolding learner construction

### Success Criteria
- ✅ Spaced Repetition requires learner to write recall attempt before showing content
- ✅ AI Study Guide requires learner to construct concepts before AI suggests additions
- ✅ Both pages provide formative feedback on learner's construction
- ✅ All changes tracked in version history

---

## Task 1: Reframe Spaced Repetition (Priority: HIGH)

### Current Behavior (DP2 Violation)
```
┌─────────────────────────────────────────────┐
│ Spaced Repetition                           │
├─────────────────────────────────────────────┤
│ Paper: "RAG for GUI Agents"                 │
│                                             │
│ 📄 Abstract: [ALWAYS VISIBLE]              │
│ "This paper proposes..."                    │
│                                             │
│ 📝 Your Notes: [ALWAYS VISIBLE]            │
│ "Key contribution is..."                    │
│                                             │
│ 🤖 AI Summary: [ALWAYS VISIBLE]            │
│ "Main points: 1)... 2)..."                  │
│                                             │
│ [Rate: Easy | Moderate | Hard]              │
└─────────────────────────────────────────────┘
```

### Target Behavior (DP2 Aligned)
```
┌─────────────────────────────────────────────┐
│ Spaced Repetition                           │
├─────────────────────────────────────────────┤
│ Paper: "RAG for GUI Agents"                 │
│                                             │
│ 📝 RECALL PROMPT:                           │
│ "Explain this paper's main contribution     │
│ without consulting your notes."             │
│                                             │
│ [TEXTAREA FOR RECALL ATTEMPT]               │
│                                             │
│ [Submit Recall]  [Reveal Notes]             │
└─────────────────────────────────────────────┘
         ↓ After Submit ↓
┌─────────────────────────────────────────────┐
│ 📊 Formative Feedback:                      │
│ "You mentioned: retrieval, RAG, agents      │
│ Missing: contrastive learning, length-aware │
│ Accuracy: 70%                               │
│                                             │
│ [Reveal Original] [Mark as Learned]         │
└─────────────────────────────────────────────┘
```

### Implementation Steps

#### Step 1.1: Add Recall Mode Toggle
- Add `recallMode` state variable
- Add toggle button to switch between "Recall First" and "Review" modes
- Default to "Recall First" (DP2 aligned)

#### Step 1.2: Create Recall Prompt UI
- Hide abstract, notes, AI summary in Recall mode
- Show prompt text + textarea
- Add "Submit Recall" and "Reveal Notes" buttons

#### Step 1.3: Implement Recall Comparison
- Call LLM API with learner's recall + original notes
- Get formative feedback (accuracy, missing concepts)
- Display feedback to learner

#### Step 1.4: Track Recall Performance
- Save recall attempts to `userData.spacedRepetition`
- Track accuracy over time
- Show progress dashboard

### Code Changes Required

**File:** `public/spaced-repetition.md`

**Changes:**
1. Add recall mode state:
```javascript
let recallMode = true; // Default to DP2-aligned mode
let currentRecallAttempt = null;
let currentFeedback = null;
```

2. Modify review card rendering:
```javascript
function renderReviewCard(paper) {
  if (recallMode) {
    // Show recall prompt
    return createRecallPrompt(paper);
  } else {
    // Show traditional review
    return createTraditionalReview(paper);
  }
}
```

3. Add recall submission handler:
```javascript
async function submitRecall() {
  const recall = document.getElementById('recallInput').value;
  const original = getOriginalNotes(paperId);
  
  // Call LLM for feedback
  const feedback = await fetch('/api/wiki/companion', {
    method: 'POST',
    body: JSON.stringify({
      mode: 'consolidate',
      original: original,
      recall: recall,
      concept: paper.title
    })
  });
  
  displayFeedback(feedback);
  saveRecallAttempt(paperId, recall, feedback);
}
```

4. Add API endpoint for consolidate mode (if not exists)

### Acceptance Criteria
- [ ] Spaced repetition defaults to recall-first mode
- [ ] Abstract/notes hidden until learner submits recall
- [ ] LLM provides formative feedback on recall attempt
- [ ] Recall performance tracked over time
- [ ] Traditional review mode still available (opt-in)

---

## Task 2: Reframe AI Study Guide (Priority: HIGH)

### Current Behavior (DP2 Violation)
```
┌─────────────────────────────────────────────┐
│ AI Study Guide                              │
├─────────────────────────────────────────────┤
│ [Generate Study Guide] [Export]             │
│                                             │
│ AI generates everything:                    │
│                                             │
│ 🎯 Key Concepts:                            │
│ - AI Agents (auto-extracted)               │
│ - RAG (auto-extracted)                     │
│ - Reasoning (auto-extracted)               │
│                                             │
│ 📝 Flashcards:                              │
│ Q: What is RAG? (auto-generated)           │
│ A: RAG is...                               │
│                                             │
│ 🔗 Connections:                             │
│ - AI Agents ↔ RAG (auto-detected)          │
└─────────────────────────────────────────────┘
```

### Target Behavior (DP2 Aligned)
```
┌─────────────────────────────────────────────┐
│ Build Your Study Guide                      │
├─────────────────────────────────────────────┤
│ Step 1: What concepts matter to you?        │
│                                             │
│ [Learner writes concept list]               │
│                                             │
│ AI Suggestion: "Consider adding             │
│ 'contrastive learning' based on your        │
│ saved papers."                              │
│                                             │
│ [Add Suggestion] [Skip]                     │
│                                             │
│ [Next: Create Flashcards]                   │
└─────────────────────────────────────────────┘
         ↓ After Construction ↓
┌─────────────────────────────────────────────┐
│ 📊 Your Guide vs Reference:                 │
│                                             │
│ You included: 5 concepts                    │
│ Reference has: 8 concepts                   │
│                                             │
│ Missing: contrastive learning,              │
│          length-aware,                      │
│          GUI evaluation                     │
│                                             │
│ [Review Gaps] [Finalize Guide]              │
└─────────────────────────────────────────────┘
```

### Implementation Steps

#### Step 2.1: Change Entry Flow
- Replace "Generate Study Guide" with "Build Your Guide"
- Add multi-step wizard (Concepts → Flashcards → Connections)
- Each step requires learner input before AI suggestions

#### Step 2.2: Scaffold Concept Identification
- Prompt: "What 3-5 concepts do you want to study?"
- Learner writes list
- AI suggests: "Based on your papers, consider X, Y"
- Learner accepts/rejects suggestions

#### Step 2.3: Scaffold Flashcard Creation
- For each concept, prompt: "Write a question about X"
- Learner writes question + answer
- AI hints: "Consider asking about Y"
- AI compares to reference flashcards

#### Step 2.4: Compare to Reference
- Generate reference guide (existing code)
- Compare learner's guide to reference
- Show gaps and recommendations
- Learner revises if desired

### Code Changes Required

**File:** `public/ai-study-guide.md`

**Changes:**
1. Replace auto-generation with wizard:
```javascript
function startStudyGuide() {
  showStep1_Concepts();
}

function showStep1_Concepts() {
  content.innerHTML = `
    <h3>Step 1: Identify Key Concepts</h3>
    <p>What concepts do you want to study? (3-5 concepts)</p>
    <textarea id="conceptInput" rows="4"></textarea>
    <button onclick="submitConcepts()">Next: Flashcards</button>
  `;
}
```

2. Add AI suggestion handler:
```javascript
async function suggestConcepts(learnerConcepts) {
  const response = await fetch('/api/wiki/companion', {
    method: 'POST',
    body: JSON.stringify({
      mode: 'scaffold',
      action: 'suggest_concepts',
      learnerInput: learnerConcepts,
      papers: savedPapers
    })
  });
  
  const suggestions = await response.json();
  displaySuggestions(suggestions);
}
```

3. Add comparison function:
```javascript
function compareGuides(learnerGuide, referenceGuide) {
  const missing = referenceGuide.concepts.filter(c => 
    !learnerGuide.concepts.includes(c)
  );
  
  return {
    accuracy: calculateAccuracy(learnerGuide, referenceGuide),
    missing: missing,
    recommendations: generateRecommendations(missing)
  };
}
```

### Acceptance Criteria
- [ ] Study guide requires learner to identify concepts first
- [ ] AI provides suggestions (not auto-generation)
- [ ] Learner must write flashcards (AI provides hints)
- [ ] Comparison shows gaps between learner's guide and reference
- [ ] Learner can revise based on feedback

---

## Task 3: Add Consolidate Mode to wiki.md (Priority: MEDIUM)

### Current Behavior
- Consolidate mode UI exists but not functional
- No retrieval practice implementation

### Target Behavior
1. Learner clicks "Consolidate" mode
2. AI hides the wiki entry
3. Prompt: "Explain this concept without the wiki"
4. Learner writes from memory
5. AI compares to original, provides feedback
6. Track mastery over time

### Code Changes Required

**File:** `public/wiki.md`

**Changes:**
1. Implement consolidate mode handler:
```javascript
async function aiConsolidateKnowledge() {
  if (!currentTerm) {
    alert('Please select a term first');
    return;
  }
  
  // Hide wiki content
  document.getElementById('wikiContent').style.display = 'none';
  
  // Show recall prompt
  const prompt = `Explain "${currentTerm}" without consulting the wiki.`;
  showRecallInput(prompt, currentTerm);
}
```

2. Add comparison to LLM:
```javascript
async function compareRecall(term, recall, original) {
  const response = await fetch('/api/wiki/companion', {
    method: 'POST',
    body: JSON.stringify({
      mode: 'consolidate',
      concept: term,
      recall: recall,
      original: original
    })
  });
  
  const feedback = await response.json();
  displayConsolidationFeedback(feedback);
}
```

### Acceptance Criteria
- [ ] Consolidate mode hides wiki content
- [ ] Learner writes recall attempt
- [ ] AI provides formative feedback
- [ ] Mastery tracked over time

---

## Task 4: Add Formative Evaluation Tracking (Priority: LOW)

### Goal
Track learner responses to AI scaffolding to measure metacognitive engagement

### Data to Track
- Time spent in each mode (Construct, Reflect, Scaffold, Consolidate)
- Accept/reject/modify rates for AI suggestions
- Recall accuracy over time
- Number of revisions per entry
- Version history (v1 → v2 → v3)

### Schema
```javascript
userData.metacognitiveTracking = {
  wikiInteractions: [
    {
      term: "RAG",
      timestamp: "2026-09-02T10:30:00Z",
      mode: "reflect",
      action: "accept_suggestion",
      duration: 45, // seconds
      revision: 2
    }
  ],
  recallPerformance: [
    {
      concept: "RAG",
      timestamp: "2026-09-02T11:00:00Z",
      accuracy: 0.75,
      feedback: "Good coverage of retrieval, missing embeddings"
    }
  ],
  masteryProgress: {
    "RAG": { level: 3, lastReviewed: "2026-09-02", accuracy: 0.85 },
    "Agents": { level: 2, lastReviewed: "2026-08-30", accuracy: 0.70 }
  }
};
```

### Implementation
1. Add tracking middleware to API server
2. Log interactions on each mode switch
3. Calculate mastery scores
4. Display progress dashboard

---

## Execution Checklist

### Task 1: Spaced Repetition Reframe
- [ ] Add recall mode state variables
- [ ] Create recall prompt UI (hide content, show textarea)
- [ ] Implement recall submission handler
- [ ] Add LLM comparison call
- [ ] Track recall performance in userData
- [ ] Test recall flow end-to-end
- [ ] Rebuild site and verify

### Task 2: AI Study Guide Reframe
- [ ] Replace "Generate" with "Build Your Guide"
- [ ] Create multi-step wizard (Concepts → Flashcards → Compare)
- [ ] Add concept suggestion handler
- [ ] Implement guide comparison
- [ ] Show gaps and recommendations
- [ ] Test wizard flow end-to-end
- [ ] Rebuild site and verify

### Task 3: Consolidate Mode
- [ ] Implement consolidate mode handler in wiki.md
- [ ] Add recall input UI
- [ ] Add LLM comparison call
- [ ] Display consolidation feedback
- [ ] Track mastery in userData
- [ ] Test consolidate flow
- [ ] Rebuild site and verify

### Task 4: Formative Tracking
- [ ] Add tracking schema to userData
- [ ] Add logging middleware to API server
- [ ] Calculate mastery scores
- [ ] Create progress dashboard UI
- [ ] Test tracking end-to-end
- [ ] Rebuild site and verify

---

## Testing Plan

### Unit Tests
1. Recall prompt hides content correctly
2. LLM comparison returns valid feedback
3. Guide comparison calculates accuracy correctly
4. Tracking data saves to userData

### Integration Tests
1. Complete spaced repetition flow (recall → feedback → reveal)
2. Complete study guide flow (concepts → flashcards → compare)
3. Complete wiki consolidate flow (hide → recall → feedback)

### User Acceptance Tests
1. Verify DP2 alignment (no content shown before recall)
2. Verify formative feedback is helpful
3. Verify tracking doesn't impede workflow

---

## Risk Mitigation

### Risk 1: LLM Slow Response
- **Mitigation:** Add loading states, show "Analyzing..." message
- **Fallback:** Use static feedback if LLM times out

### Risk 2: Learner Resistance
- **Mitigation:** Explain DP2 rationale in onboarding
- **Option:** Keep traditional mode available (opt-in)

### Risk 3: Data Persistence
- **Mitigation:** Save to userData.json immediately
- **Backup:** Export tracking data periodically

---

## Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Spaced Repetition DP2 Compliance | 100% | 0% |
| Study Guide DP2 Compliance | 100% | 0% |
| Consolidate Mode Functional | Yes | No |
| Formative Tracking Implemented | Yes | No |
| Learner Recall Accuracy | Track over time | N/A |
| Metacognitive Engagement Score | Track over time | N/A |

---

## Dependencies

- ✅ Phase 1 Complete (UI alignment)
- ✅ Phase 2 Complete (LLM integration)
- ✅ API server running on port 5001
- ✅ Ollama running with gemma4-64k
- ⏳ Phase 3A (this plan)
- 🔲 Phase 3B (Revisit mode, version history)

---

## Rollback Plan

If issues arise:
1. Keep original files in `private/backups/`
2. Git commit before each major change
3. Revert with `git checkout HEAD -- <file>`
4. Rebuild site to verify rollback

---

## Next Steps After Phase 3A

1. **User Testing:** Have 2-3 learners test the new flows
2. **Feedback Collection:** Gather feedback on DP2 alignment
3. **Iterate:** Refine based on feedback
4. **Phase 3B:** Implement Revisit mode and version history
5. **Formative Evaluation:** Measure learning outcomes

---

**Plan Status:** Ready to Execute  
**Estimated Duration:** 2-3 hours  
**Next Action:** Begin Task 1 (Spaced Repetition Reframe)
