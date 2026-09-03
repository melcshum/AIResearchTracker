# Wiki Enhancement Plan: 5-Stage Knowledge Construction Cycle

**Date:** September 2, 2026  
**Status:** Phase 1 In Progress  
**Based on:** Conference paper "From Notes to Knowledge: AI Wiki Companion for Learner-in-the-Loop Knowledge Construction"

---

## Executive Summary

Transform the wiki from a **knowledge repository** (lookup-based) into a **knowledge construction environment** (write-reflect-scaffold-revise) aligned with the learner-in-the-loop framework.

---

## Current State Analysis

### What Exists
- **wiki.md**: Static article with highlighted terms, 5-step workflow (Select → Question → Search → Explain → Review), bidirectional linking, concept graph
- **ai-wiki.md**: "Learn by Building" with 3 modes (Build Understanding, Teaching Mode, Compare & Reflect), concept selector, textarea, mastery indicator
- **paper-reader.md**: Annotation tools (highlight, note, question, validate)
- **spaced-repetition.md**: Shows abstract + notes + AI summary (violates DP2)
- **ai-study-guide.md**: Auto-generates study materials (violates DP2)

### Critical Gaps
1. **No AI Companion with metacognitive prompts** — No Socratic questioning, gap detection, or misconception challenges
2. **No Prompt Before Provide** — No interaction model asking learners to articulate understanding first
3. **No connection recommendations** — No system suggesting relationships between wiki entries
4. **No retrieval practice** — Spaced repetition shows content instead of requiring recall
5. **No knowledge evolution tracking** — No version history showing understanding changes
6. **No formative evaluation** — No tracking of learner responses to AI scaffolding

---

## Design Decisions (User Confirmed)

1. **LLM Provider:** Local LLM (no cloud API dependency)
2. **Consolidation Mode:** Optional (not mandatory)
3. **Version History:** Yes, full diff tracking
4. **Connection Suggestions:** Ask before suggesting (not automatic)

---

## Proposed 5-Mode AI Companion

### Mode 1: Construct (✍️ Write)
- Learner selects concept and writes initial explanation
- AI observes but doesn't intervene yet
- Captures baseline understanding
- **Current:** ai-wiki.md's "Build Understanding" partially does this

### Mode 2: Reflect (🤔 Inspect)
- After writing, AI generates metacognitive prompts:
  - "Which part of this explanation are you least confident about?"
  - "Can you restate this without referring to your notes?"
  - "What assumptions underpin this explanation?"
- Learner self-evaluates confidence (1-5 scale per section)
- **Missing:** No AI prompts currently

### Mode 3: Scaffold (🏗️ Support)
- AI analyzes learner's explanation using local LLM
- Identifies gaps: "Your explanation discusses X but not Y"
- Challenges misconceptions: "Would this hold for unseen data?"
- Recommends connections (only when asked): "This relates to your earlier entry on Z"
- Uses **Prompt Before Provide**: asks learner to think before giving answer
- **Missing:** No LLM integration currently

### Mode 4: Consolidate (💡 Retrieve) — OPTIONAL
- AI hides the wiki entry
- Prompts: "Explain this concept without consulting the wiki"
- Learner writes from memory
- AI compares to original entry, provides feedback
- **Missing:** No retrieval practice currently

### Mode 5: Revisit (🔗 Connect)
- When learner adds new concept, AI retrieves related prior entries
- Prompts: "Does what you just learned require your earlier entry on X to be revised?"
- Shows version history: "Your understanding has evolved from v1 to v3"
- **Missing:** No longitudinal integration currently

---

## Technical Architecture

### Current Stack
- Static HTML + localStorage + Python scripts
- No backend API for LLM calls

### Proposed: Local LLM Integration

**Option A: Flask API Server** (extend existing api_server.py on port 5001)
- Add `/api/wiki/companion` endpoint
- Accepts: learner's explanation, concept, prior entries
- Calls local LLM (Ollama, llama.cpp, or similar)
- Returns: metacognitive prompts, gap detection, connection suggestions

**Option B: Serverless Functions** (if deploying to Vercel/Netlify)
- Each mode is a separate function
- More scalable but more complex

**Decision:** Option A (Flask) — simpler, already have api_server.py running

---

## LLM Prompt Design

### Reflect Mode Prompt
```
You are a metacognitive coach. The learner wrote this explanation of [concept]:
"{learner_explanation}"

Generate 2-3 reflective questions that help them examine their understanding.
Focus on: confidence, completeness, assumptions, explanatory adequacy.
Do NOT provide answers. Only ask questions.
```

### Scaffold Mode Prompt
```
You are a knowledge construction scaffold. The learner wrote:
"{learner_explanation}"

Analyze for:
1. Missing concepts (concepts they should mention but didn't)
2. Potential misconceptions (statements that might be inaccurate)
3. Connection opportunities (related concepts they could link to)

Provide feedback as questions, not corrections.
Example: "You discussed X but not Y. How are they related?"
```

### Consolidate Mode Prompt
```
The learner's original explanation:
"{original_explanation}"

Their retrieval attempt (from memory):
"{retrieval_attempt}"

Compare and provide formative feedback:
- What did they recall correctly?
- What did they miss?
- What misconceptions emerged?

Frame as encouragement + targeted questions.
```

---

## Implementation Plan (Phased)

### Phase 1: Align Core Pages ✅ COMPLETED
**Goal:** Update UI to reflect 5-stage cycle (no LLM yet)

**Tasks:**
1. ✅ Update wiki.md workflow to 5-stage cycle
2. ✅ Add mode selector tabs (Construct/Reflect/Scaffold/Consolidate/Revisit)
3. ✅ Keep existing functionality, just reframe labels
4. ✅ Update ai-wiki.md to align with 5-mode cycle
5. ✅ Add AI Companion panel with 5 modes

**Status:** ✅ COMPLETED (September 2, 2026)

**Changes Made:**
- Updated workflow guide from old 5-step (Select → Question → Search → Explain → Review) to new 5-stage cycle (Construct → Reflect → Scaffold → Consolidate → Revisit)
- Replaced old 4-mode AI Companion (Write/Review/Coach/Update) with new 5-mode system
- Added CSS for companion intro text
- Implemented all 5 mode functions with appropriate UI and interactions
- Site rebuilt successfully (266 pages)

### Phase 2: Add Local LLM Backend (Next Session)
**Goal:** Implement LLM calls for Reflect and Scaffold modes

**Tasks:**
1. Install local LLM (Ollama recommended for macOS)
2. Extend api_server.py with `/api/wiki/companion` endpoint
3. Implement LLM calls for Reflect mode (metacognitive prompts)
4. Implement LLM calls for Scaffold mode (gap detection, connection suggestions)
5. Add prompt templates
6. Test with sample explanations

**Estimated Time:** 2-3 hours

### Phase 3: Add Consolidate Mode (Session After Next)
**Goal:** Implement retrieval practice

**Tasks:**
1. Add "hide wiki" toggle in Consolidate mode
2. Implement retrieval prompt UI
3. Add comparison logic (original vs. retrieval attempt)
4. Track accuracy over time in localStorage

**Estimated Time:** 1-2 hours

### Phase 4: Formative Evaluation (Later Session)
**Goal:** Track learner responses and knowledge evolution

**Tasks:**
1. Track learner responses (accept/reject/modify AI suggestions)
2. Add version history visualization with full diff
3. Add metacognitive engagement metrics
4. Add knowledge evolution timeline

**Estimated Time:** 2-3 hours

---

## Wiki Enhancement: Specific Changes

### wiki.md Changes
- ✅ Replace old 5-step workflow with new 5-mode cycle (DONE)
- Add mode selector tabs at top
- Each mode has different UI:
  - **Construct:** textarea + concept selector
  - **Reflect:** AI prompts panel + confidence slider
  - **Scaffold:** AI feedback panel + connection suggestions
  - **Consolidate:** hide wiki, show retrieval prompt
  - **Revisit:** show related entries + version history

### ai-wiki.md Changes
- Keep "Learn by Building" but align with 5-mode cycle
- Add AI Companion panel (right sidebar)
- Integrate LLM calls when learner submits explanation

### New File: wiki-companion.js
- Handles mode switching
- Calls LLM API
- Renders AI prompts and feedback
- Manages localStorage for version history

---

## Success Criteria

1. **Learner Agency:** Learners remain primary constructors; AI scaffolds without substituting
2. **Metacognitive Engagement:** Learners actively monitor and revise understanding
3. **Knowledge Evolution:** Wiki entries show substantive revision over time
4. **Prompt Before Provide:** AI asks before telling
5. **Connection Recommendations:** Only when learner asks (not automatic)

---

## Open Questions

1. **Local LLM choice:** Ollama vs. llama.cpp vs. other? (Recommendation: Ollama for ease of use)
2. **Model size:** 7B vs. 13B vs. 70B? (Recommendation: Start with 7B for speed, upgrade if needed)
3. **Confidence slider:** 1-5 scale or 1-10? (Recommendation: 1-5 for simplicity)
4. **Version diff format:** Side-by-side or inline? (Recommendation: Inline with color coding)

---

## Next Steps

1. ✅ Update wiki.md workflow (DONE)
2. Update ai-wiki.md to align with 5-mode cycle
3. Add mode selector UI
4. Test current implementation
5. Rebuild site with Quarto

---

## References

- Conference paper: `public/conference-papers/ai-wiki-companion-2026.md`
- Design principles: DP1 (Learner Ownership), DP2 (Scaffold Rather Than Substitute), DP3 (Reflection Before Correction), DP4 (Continuous Knowledge Integration)
- 5-stage cycle: Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend
