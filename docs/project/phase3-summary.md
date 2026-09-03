# Phase 3: Pilot Study Preparation Summary

**Date:** 2026-09-03  
**Status:** ✅ Complete  
**Component:** Pilot Study Materials + Paper Section 3.6  

---

## What Was Accomplished

### 1. Pilot Study Materials Created

#### Participant Guide (`pilot-study-participant-guide.md`)
- **Length:** 4,708 characters (115 lines)
- **Sections:**
  - Study overview and purpose
  - Step-by-step instructions for 5-stage cycle
  - Session 1 and Session 2 procedures
  - Troubleshooting guide
  - Contact information

#### Feedback Form (`pilot-study-feedback-form.md`)
- **Length:** 5,385 characters (135 lines)
- **Sections:**
  - Section A: Usability (4 questions, 5-point scale)
  - Section B: Learning Experience (5 questions, 5-point scale)
  - Section C: Epistemic Agency (4 questions, 5-point scale)
  - Section D: Open-Ended Questions (5 questions)
  - Section E: Behavioral Observations (researcher fills)
  - Section F: Researcher Notes

### 2. Paper Section 3.6 Written

#### Section 3.6: Prototype Implementation
- **Length:** 158 lines added (paper now 1,063 lines total)
- **Subsections:**
  - 3.6.1 System Architecture (frontend, backend, data persistence)
  - 3.6.2 API Design (5 endpoints table)
  - 3.6.3 Mock Scaffolding Implementation (code example)
  - 3.6.4 Frontend-Backend Integration (JavaScript code)
  - 3.6.5 Current Capabilities and Limitations
  - 3.6.6 Deployment and Access

**Key Contributions:**
- Detailed technical architecture description
- API endpoint table with request/response schemas
- Code examples showing implementation
- Honest discussion of limitations
- Clear deployment instructions

---

## Current Status Summary

| Phase | Status | Progress | Deliverable |
|-------|--------|----------|-------------|
| **Phase 1:** Theoretical Framework | ✅ Complete | 100% | Enhanced Sections 2.7, 3.1-3.3 |
| **Phase 2:** Backend API | ✅ Complete | 100% | 5 functional endpoints |
| **Phase 2.5:** Frontend Integration | ✅ Complete | 100% | Real API calls, error handling |
| **Phase 3:** Pilot Study Materials | ✅ Complete | 100% | Participant guide + feedback form |
| **Phase 3.5:** Paper Section 3.6 | ✅ Complete | 100% | Prototype implementation description |
| **Phase 4:** Run Pilot Study | ⏳ Next | 0% | Need to recruit participants |
| **Phase 5:** Write Section 4.6 | ⏳ Pending | 0% | Pilot results and discussion |
| **Phase 6:** Final Submission | ⏳ Pending | 0% | Conference submission |

---

## Files Created/Modified

### New Files (3)
1. `/Users/ailcshum/workspace/research-notes/pilot-study-participant-guide.md` (115 lines)
2. `/Users/ailcshum/workspace/research-notes/pilot-study-feedback-form.md` (135 lines)
3. `/Users/ailcshum/workspace/research-notes/phase3-summary.md` (this file)

### Modified Files (1)
1. `/Users/ailcshum/workspace/research-notes/public/conference-papers/ai-wiki-companion-2026.md`
   - Added Section 3.6 (158 lines)
   - Total lines: 905 → 1,063 (+158 lines)

---

## Pilot Study Execution Plan

### Week 1: Recruitment and Setup

#### Day 1-2: Participant Recruitment
- [ ] Identify 5-8 potential participants
- [ ] Send invitation emails with study overview
- [ ] Schedule individual 45-minute sessions
- [ ] Prepare consent forms (if required by IRB)

#### Day 3: Technical Setup
- [ ] Verify API server is running (`python api_server.py`)
- [ ] Verify web server is running (`python -m http.server 8000`)
- [ ] Test complete flow with dummy data
- [ ] Prepare backup laptop in case of technical issues

#### Day 4-5: Materials Preparation
- [ ] Print participant guides (one per participant)
- [ ] Print feedback forms (one per participant)
- [ ] Prepare observation notebook
- [ ] Set up screen recording software (optional)

### Week 2: Pilot Sessions

#### Session Protocol (45 minutes per participant)

**Pre-Session (5 minutes):**
1. Welcome participant
2. Explain study purpose and obtain consent
3. Answer any questions
4. Start screen recording (if applicable)

**Session 1: Initial Knowledge Construction (30 minutes):**
1. Participant follows guide (Session 1 steps)
2. Researcher observes and takes notes
3. Researcher fills Section E of feedback form
4. Participant completes feedback form (5 minutes)

**Post-Session (10 minutes):**
1. Brief interview (optional):
   - "What was most helpful?"
   - "What was confusing?"
   - "What would you change?"
2. Thank participant
3. Save observation notes

#### Data Collection Checklist

For each participant, collect:
- [ ] Completed feedback form
- [ ] Observation notes (Section E + F)
- [ ] Interaction logs (from `_data/users/{username}/wiki_data.json`)
- [ ] Screen recording (if applicable)
- [ ] Interview notes (if conducted)

### Week 3: Analysis and Paper Writing

#### Day 1-2: Data Analysis
- [ ] Compile feedback form responses
- [ ] Calculate average scores for each section
- [ ] Identify common themes in open-ended responses
- [ ] Analyze interaction logs (time spent, revision frequency)
- [ ] Create summary tables and figures

#### Day 3-4: Write Section 4.6 (Pilot Results)
- [ ] Describe participant demographics
- [ ] Present quantitative results (usability, learning, agency scores)
- [ ] Present qualitative findings (themes from open-ended questions)
- [ ] Discuss implications for framework refinement
- [ ] Address limitations and future work

#### Day 5: Final Paper Review
- [ ] Read entire paper for coherence
- [ ] Check all citations and references
- [ ] Verify figures and tables
- [ ] Proofread for grammar and style
- [ ] Format according to conference guidelines

---

## Success Metrics for Pilot Study

### Quantitative Targets
- **Usability Score:** Average ≥ 3.5/5.0 across all usability questions
- **Learning Value:** Average ≥ 3.5/5.0 for learning experience questions
- **Epistemic Agency:** Average ≥ 4.0/5.0 for agency questions (critical for framework validation)
- **Completion Rate:** ≥ 80% of participants complete full 5-stage cycle

### Qualitative Targets
- **Positive Feedback:** ≥ 70% of participants report tool is "helpful" or "very helpful"
- **Constructive Criticism:** Collect at least 3 actionable improvement suggestions
- **Behavioral Observations:** Document at least 5 notable interaction patterns

### Technical Targets
- **System Stability:** Zero crashes during pilot sessions
- **API Response Time:** Average < 200ms for mock responses
- **Data Integrity:** All participant data saved correctly

---

## Risk Mitigation

### Risk 1: Low Participant Recruitment
**Mitigation:**
- Expand recruitment to multiple courses/programs
- Offer incentives (e.g., gift cards, course credit)
- Reduce session length to 30 minutes

### Risk 2: Technical Issues During Sessions
**Mitigation:**
- Test system thoroughly before each session
- Have backup laptop ready
- Prepare paper-based alternative (printouts of wiki pages)

### Risk 3: Negative Feedback
**Mitigation:**
- Frame as "formative evaluation" (not summative)
- Emphasize that criticism is valuable for improvement
- Be prepared to iterate on design based on feedback

### Risk 4: Insufficient Data for Paper
**Mitigation:**
- Extend pilot period by 1 week if needed
- Combine with additional informal user testing
- Focus paper on design framework rather than empirical results

---

## Next Steps

### Immediate Actions (Today)
1. ✅ Review pilot study materials (participant guide, feedback form)
2. ✅ Review Section 3.6 in paper
3. ⏳ Identify potential participants
4. ⏳ Schedule first pilot session

### This Week
1. ⏳ Recruit 5-8 participants
2. ⏳ Conduct 2-3 pilot sessions
3. ⏳ Collect feedback and observations

### Next Week
1. ⏳ Complete remaining pilot sessions
2. ⏳ Analyze data
3. ⏳ Write Section 4.6 (Pilot Results)

### Week After
1. ⏳ Final paper review and revisions
2. ⏳ Format according to conference guidelines
3. ⏳ Submit to LAK 2027 or AIED 2027

---

## Summary

✅ **All preparation complete:**
- Theoretical framework enhanced (Phase 1)
- Backend API implemented (Phase 2)
- Frontend integrated (Phase 2.5)
- Pilot materials created (Phase 3)
- Paper Section 3.6 written (Phase 3.5)

⏳ **Ready to proceed:**
- Recruit participants
- Run pilot study
- Analyze results
- Write Section 4.6
- Submit paper

**Estimated time to submission:** 2-3 weeks (assuming smooth pilot execution)

---

## Appendix: Quick Reference

### Server Commands
```bash
# Start backend API
cd /Users/ailcshum/workspace/research-notes
python api_server.py

# Start frontend web server
cd /Users/ailcshum/workspace/research-notes/public
python -m http.server 8000

# Access URL
http://localhost:8000/ai-wiki.html
```

### API Test Commands
```bash
# Test construct endpoint
curl -X POST http://localhost:5001/api/wiki/construct \
  -H "Content-Type: application/json" \
  -d '{"concept":"overfitting","explanation":"test"}'

# Test reflect endpoint
curl -X POST http://localhost:5001/api/wiki/reflect \
  -H "Content-Type: application/json" \
  -d '{"concept":"overfitting","explanation":"test","use_llm":false}'
```

### File Locations
- **Paper:** `/Users/ailcshum/workspace/research-notes/public/conference-papers/ai-wiki-companion-2026.md`
- **Participant Guide:** `/Users/ailcshum/workspace/research-notes/pilot-study-participant-guide.md`
- **Feedback Form:** `/Users/ailcshum/workspace/research-notes/pilot-study-feedback-form.md`
- **Development Plan:** `/Users/ailcshum/workspace/research-notes/development-plan.md`
- **Backend Code:** `/Users/ailcshum/workspace/research-notes/api_server.py`
- **Frontend Code:** `/Users/ailcshum/workspace/research-notes/public/js/ai-companion.js`
