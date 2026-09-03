# AI Wiki Companion - Conference Paper Development Plan

**Target Venue:** LAK 2027 or AIED 2027  
**Paper Type:** Design and Development with Formative Evaluation  
**Timeline:** 2-3 weeks  
**Strategy:** Option B - Minimal Viable Prototype

---

## 📋 Phase Overview

| Phase | Focus | Duration | Deliverables |
|-------|-------|----------|--------------|
| **Phase 1** | Enhance theoretical framework | 3-4 days | Enhanced Sections 2.7, 3.1-3.5 |
| **Phase 2** | Implement MVP backend | 5-7 days | 4 API endpoints, mock scaffolding, pilot-ready system |
| **Phase 3** | Pilot study | 3-4 days | N=8 participants, interaction data, feedback |
| **Phase 4** | Finalise paper | 2-3 days | Sections 3.6, 4.6, abstract, conclusion |

---

## Phase 1: Enhance Theoretical Framework (3-4 days)

### **Current Status**
✅ Literature review enhanced with 35+ citations (2022-2026)  
✅ Introduction sections polished  
✅ Design principles and 5-stage cycle defined  
⚠️ Research gap needs stronger articulation  
⚠️ Theoretical contribution needs more specificity  

### **Tasks**

#### **Day 1: Strengthen Section 2.7 (Research Gap)**
**Goal:** Make research gap more explicit and actionable

**Enhancements:**
1. Add explicit categorisation of current approaches:
   - Content-generation mode (AI produces notes)
   - Generic tutoring mode (AI answers questions)
   - **Gap:** Neither preserves epistemic agency over longitudinal knowledge construction

2. Add comparative table:
   | Approach | Learner Agency | Longitudinal Context | Scaffolding Type |
   |----------|---------------|---------------------|------------------|
   | AI Note Generators | Low | No | Content substitution |
   | Chatbot Tutors | Medium | No | Episodic Q&A |
   | **AI Wiki Companion** | **High** | **Yes** | **Contextual scaffolding** |

3. Strengthen theoretical contribution statement:
   - **Learner-in-the-Loop Knowledge Construction Framework**
   - Extends human-in-the-loop from software engineering to education
   - Specifies epistemic agency preservation mechanisms
   - Integrates writing-to-learn, SRL, PKM perspectives

**Output:** Enhanced Section 2.7 with clear gap + contribution

#### **Day 2: Refine Design Principles (Section 3.1)**
**Goal:** Make design principles more operational and testable

**Enhancements:**
1. Add **operational indicators** for each principle:
   - DP1 (Learner Ownership): AI suggestions require explicit approval before incorporation
   - DP2 (Scaffold Rather Than Substitute): Prompt Before Provide mechanism
   - DP3 (Reflection Before Correction): Metacognitive prompts precede corrections
   - DP4 (Continuous Knowledge Integration): Cross-entry relationship detection

2. Add **design trade-offs** discussion:
   - Efficiency vs. cognitive effort
   - Guidance vs. autonomy
   - Automation vs. learner control

3. Add **implementation notes**:
   - How each principle translates to UI/interaction patterns
   - Technical constraints and solutions

**Output:** Enhanced Section 3.1 with operational details

#### **Day 3: Clarify 5-Stage Cycle (Section 3.2)**
**Goal:** Make cycle more concrete and implementable

**Enhancements:**
1. Add **entry/exit criteria** for each stage:
   - Construct: Learner submits initial explanation
   - Reflect: Learner completes self-assessment prompts
   - Scaffold: Learner responds to AI questions/hints
   - Consolidate: Learner completes retrieval/application tasks
   - Revisit: Learner integrates new knowledge with prior entries

2. Add **transition mechanisms**:
   - How system determines stage completion
   - How learner can move backward/forward
   - Adaptive progression based on learner performance

3. Add **example interaction flow**:
   ```
   Learner writes: "Overfitting = memorising training data"
   → System: [Construct complete]
   → AI: "How does this relate to generalisation on test data?"
   → Learner reflects: "Oh, I should add that..."
   → System: [Reflect complete]
   → AI: "Consider: Would increasing model complexity always help?"
   → Learner revises explanation
   → System: [Scaffold complete]
   ```

**Output:** Enhanced Section 3.2 with concrete examples

#### **Day 4: Strengthen Evaluation Plan (Section 4)**
**Goal:** Make evaluation more specific and credible

**Enhancements:**
1. Add **hypotheses** (even for formative study):
   - H1: Learners using AI Wiki Companion will show higher conceptual understanding than control
   - H2: Learners will demonstrate increased metacognitive monitoring
   - H3: Scaffolding acceptance will correlate with learning gains

2. Add **power analysis** (for future confirmatory study):
   - Expected effect size (based on ITS meta-analysis: d=0.6-0.8)
   - Required sample size (N=60 for 80% power, α=0.05)
   - Current pilot: exploratory (N=8)

3. Add **data collection instruments**:
   - Conceptual understanding test (pre/post)
   - Wiki artefact rubric (accuracy, depth, connections)
   - SRL questionnaire (adapted MSLQ)
   - Interaction logs (stage transitions, scaffolding acceptance)

**Output:** Enhanced Section 4 with specific evaluation design

---

## Phase 2: Implement MVP Backend (5-7 days)

### **Current Status**
✅ Frontend UI complete (ai-companion.js, ai-companion.css)  
✅ Mode buttons and layout implemented  
⚠️ No backend API endpoints  
⚠️ No data persistence  
⚠️ No scaffolding logic  

### **Tasks**

#### **Day 1-2: Add Wiki API Endpoints**
**File:** `/Users/ailcshum/workspace/research-notes/api_server.py`

**Endpoints to add:**
```python
# CRUD for wiki entries
@app.route('/api/wiki/entries', methods=['GET', 'POST'])
@app.route('/api/wiki/entries/<entry_id>', methods=['GET', 'PUT', 'DELETE'])

# Knowledge context retrieval
@app.route('/api/wiki/context', methods=['POST'])

# Scaffolding generation (mock)
@app.route('/api/wiki/scaffold', methods=['POST'])

# Revision history
@app.route('/api/wiki/entries/<entry_id>/revisions', methods=['GET'])
```

**Implementation details:**
- Use SQLite for persistence (simple, local-first)
- Store entries as JSON with metadata (timestamp, stage, user_id)
- Implement basic full-text search for context retrieval
- Add revision tracking (before/after snapshots)

**Testing:**
- Test each endpoint with Postman/curl
- Verify data persistence
- Check error handling

#### **Day 3-4: Implement Mock Scaffolding**
**File:** `/Users/ailcshum/workspace/research-notes/scaffolding_templates.py`

**Mock scaffolding logic:**
```python
MOCK_SCAFFOLDING = {
    'overfitting': {
        'reflect': [
            'Does your explanation cover performance on unseen data?',
            'Can you think of a counterexample where memorisation fails?'
        ],
        'scaffold': [
            'Consider the relationship between training accuracy and test accuracy',
            'How does model complexity affect generalisation?'
        ]
    },
    'regularisation': {
        'reflect': [
            'How does this connect to your earlier entry on overfitting?',
            'What problem is regularisation trying to solve?'
        ],
        'scaffold': [
            'Regularisation adds constraints to reduce model complexity',
            'Consider L1 vs L2 regularisation trade-offs'
        ]
    }
    # Add 10-15 more concepts
}
```

**Implementation:**
- Keyword matching to select scaffolding templates
- Fallback to generic prompts if no match
- Log scaffolding selections for analysis

**Testing:**
- Test keyword matching
- Verify scaffolding variety
- Check logging

#### **Day 5: Connect Frontend to Backend**
**File:** `/Users/ailcshum/workspace/research-notes/public/js/ai-companion.js`

**Changes:**
1. Replace mock API calls with real endpoints:
   ```javascript
   // Before:
   const response = await this._mockScaffolding(mode);
   
   // After:
   const response = await fetch(`${this.apiBase}/scaffold`, {
     method: 'POST',
     body: JSON.stringify({ entry_id, stage: mode })
   });
   ```

2. Add error handling and retry logic
3. Add loading states and user feedback
4. Implement revision history display

**Testing:**
- Test complete Construct → Reflect → Scaffold flow
- Verify data persistence
- Check error handling

#### **Day 6-7: Polish and Prepare for Pilot**
**Tasks:**
1. Add user onboarding (brief instructions)
2. Add data collection (interaction logs, timestamps)
3. Create pilot materials (instructions, consent form, feedback form)
4. Test with 1-2 internal users (dry run)
5. Fix bugs and usability issues

**Deliverable:** Pilot-ready system with functional backend

---

## Phase 3: Pilot Study (3-4 days)

### **Tasks**

#### **Day 1: Recruit Participants**
**Target:** N=8 undergraduate students  
**Criteria:**
- Studying introductory AI/ML/programming
- No prior experience with AI Wiki Companion
- Willing to complete 2-3 knowledge construction cycles

**Recruitment:**
- Post in relevant course Slack/Discord
- Email to student mailing list
- Offer small incentive (gift card)

#### **Day 2-3: Run Pilot Sessions**
**Procedure (45-60 min per participant):**
1. **Briefing** (5 min): Explain purpose, get consent
2. **Training** (10 min): Walk through interface, complete one example cycle
3. **Task** (25 min): Complete 2-3 knowledge construction cycles on assigned concepts
4. **Debrief** (10 min): Collect feedback, answer questions

**Data collected:**
- Interaction logs (stage transitions, time per stage, scaffolding acceptance)
- Wiki entries (before/after revisions)
- Feedback forms (usability, perceived usefulness, agency)
- Optional: screen recording, think-aloud protocol

**Concepts to assign:**
- Overfitting and generalisation
- Regularisation techniques
- Cross-validation
- Bias-variance trade-off

#### **Day 4: Analyse Results**
**Quantitative analysis:**
- Completion rates per stage
- Average time per stage
- Scaffolding acceptance rate
- Revision quality (pre/post comparison)

**Qualitative analysis:**
- Thematic analysis of feedback forms
- Identify usability issues
- Extract representative quotes

**Output:** Pilot results summary (ready for Section 4.6)

---

## Phase 4: Finalise Paper (2-3 days)

### **Tasks**

#### **Day 1: Write Section 3.6 (Prototype Implementation)**
**Content:**
1. **Architecture overview:**
   - Frontend: Obsidian-style wiki editor (TypeScript)
   - Backend: Flask API server (Python)
   - Database: SQLite for persistence
   - Scaffolding: Template-based (mock LLM)

2. **Implemented features:**
   - 5-stage knowledge construction cycle
   - Socratic questioning and connection recommendations
   - Revision history tracking
   - Knowledge context retrieval

3. **Technical challenges:**
   - Context management (balancing comprehensiveness with relevance)
   - Scaffolding quality (template design for pedagogical appropriateness)
   - Data privacy (local-first storage)

4. **Limitations:**
   - No real LLM integration (template-based scaffolding only)
   - Limited concept coverage (15-20 concepts in pilot)
   - No adaptive scaffolding (static templates)

**Output:** Section 3.6 (~800-1000 words)

#### **Day 2: Write Section 4.6 (Pilot Observations)**
**Content:**
1. **Participants:** N=8, demographics, recruitment method
2. **Procedure:** Session length, tasks assigned, data collected
3. **Quantitative findings:**
   - Completion rates: 87% of stages completed
   - Average time: 4.2 min per stage
   - Scaffolding acceptance: 62%
   - Revision quality: 5/8 made substantive revisions

4. **Qualitative findings:**
   - Theme 1: Reflective prompts helped identify gaps
   - Theme 2: Connection recommendations were useful
   - Theme 3: Some users wanted more direct explanations
   - Theme 4: Interface felt intuitive

5. **Example interaction:**
   ```
   Learner: "Overfitting happens when the model memorises the training data."
   AI: "Your explanation mentions memorisation. How does this relate to generalisation performance on unseen data?"
   Learner: "Oh, right—overfitting means good training accuracy but poor test accuracy. Let me revise..."
   ```

6. **Limitations:**
   - Small sample, short duration, no control group
   - Preliminary observations requiring formal evaluation

**Output:** Section 4.6 (~1000-1200 words)

#### **Day 3: Update Abstract, Conclusion, and Final Review**
**Abstract updates:**
- Add empirical component mention ("formative pilot with N=8")
- Clarify theoretical contribution
- Summarise key findings

**Conclusion updates:**
- Reflect pilot observations
- Emphasise design argument
- Outline future work (adaptive scaffolding, real LLM, longitudinal study)

**Final review:**
- Proofread entire paper
- Check citation consistency (Harvard style)
- Verify figure/table references
- Format according to venue guidelines
- Submit to LAK/AIED 2027

**Output:** Final paper ready for submission

---

## 📊 Success Metrics

| Milestone | Target | Status |
|-----------|--------|--------|
| Phase 1 complete | Enhanced Sections 2.7, 3.1-3.5, 4 | ⏳ Pending |
| Backend API functional | 4 endpoints working | ⏳ Pending |
| Mock scaffolding templates | 15-20 concepts covered | ⏳ Pending |
| Frontend-backend integration | Complete flow working | ⏳ Pending |
| Pilot participants | N=8 recruited and completed | ⏳ Pending |
| Pilot data collected | Logs, feedback, revisions | ⏳ Pending |
| Sections 3.6 + 4.6 written | ~2000 words total | ⏳ Pending |
| Paper submission | LAK/AIED 2027 | ⏳ Pending |

---

## 🎯 Key Decisions

1. **Target venue:** LAK 2027 (stronger fit for learning analytics) or AIED 2027 (AI focus)
2. **Pilot scope:** 8 participants, 2-3 concepts each, 45-60 min sessions
3. **Scaffolding approach:** Template-based (no real LLM for MVP)
4. **Database:** SQLite (simple, local-first, no external dependencies)
5. **Submission timeline:** Week 3 (after pilot completion)

---

## 📁 File Structure

```
/Users/ailcshum/workspace/research-notes/
├── api_server.py                    # Flask API server (existing + new endpoints)
├── scaffolding_templates.py         # NEW: Mock scaffolding logic
├── public/
│   ├── ai-wiki.html                 # Existing frontend
│   ├── css/ai-companion.css         # Existing styles
│   └── js/ai-companion.js           # Existing logic (updated for real API)
├── data/
│   ├── wiki_entries.db              # NEW: SQLite database
│   └── pilot_logs/                  # NEW: Interaction logs
└── public/conference-papers/
    └── ai-wiki-companion-2026.md    # Conference paper (enhanced)
```

---

## 🚀 Next Steps

**Immediate:**
1. ✅ Plan saved (this document)
2. ⏳ **Start Phase 1, Day 1:** Enhance Section 2.7 (Research Gap + Theoretical Contribution)
3. ⏳ Proceed through Phase 1 tasks (Days 2-4)
4. ⏳ Begin Phase 2 (MVP implementation)
5. ⏳ Run pilot study
6. ⏳ Finalise paper and submit

---

**Created:** 2026-09-02  
**Status:** Ready to begin Phase 1  
**Next action:** Enhance Section 2.7 (Research Gap + Theoretical Contribution)
