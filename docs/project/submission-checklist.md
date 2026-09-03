# Conference Paper Submission Checklist

**Target Venue:** LAK 2027 or AIED 2027  
**Paper Title:** From Notes to Knowledge: AI Wiki Companion for Learner-in-the-Loop Knowledge Construction  
**Current Status:** Phase 1-3 Complete, Ready for Pilot Study

---

## Pre-Pilot Study Checklist

### Technical Preparation
- [ ] Backend API tested and running (`python api_server.py`)
- [ ] Frontend web server tested (`python -m http.server 8000`)
- [ ] All 5 API endpoints verified working
- [ ] Mock scaffolding tested for 3 ML concepts
- [ ] Data persistence verified (JSON files saving correctly)
- [ ] Error handling tested (network failures, invalid inputs)
- [ ] Backup laptop prepared (if needed)

### Materials Preparation
- [ ] Participant guide printed (1 per participant)
- [ ] Feedback form printed (1 per participant)
- [ ] Session checklist printed (1 per session)
- [ ] Consent forms prepared (if required by IRB)
- [ ] Incentives purchased (gift cards, etc.)
- [ ] Observation notebook ready
- [ ] Screen recording software tested (optional)

### Recruitment
- [ ] Recruitment emails sent to 15-20 potential participants
- [ ] Follow-up emails sent to non-responders
- [ ] 5-8 participants recruited and scheduled
- [ ] Reminder emails sent (day before each session)
- [ ] Tracking spreadsheet created and maintained

---

## During Pilot Study Checklist

### For Each Session
- [ ] Technical setup verified (servers running, page loads)
- [ ] Participant guide and feedback form ready
- [ ] Session checklist followed step-by-step
- [ ] Observation notes taken (Section E + F of feedback form)
- [ ] Feedback form collected and checked for completeness
- [ ] Interaction logs exported from `_data/users/{username}/wiki_data.json`
- [ ] Screen recording saved (if applicable)
- [ ] Thank-you email sent
- [ ] Incentive distributed
- [ ] Data backed up to `~/pilot-data/session-{N}-{date}/`

### Data Collection
- [ ] All feedback forms collected (quantitative + qualitative)
- [ ] All interaction logs exported
- [ ] All observation notes completed
- [ ] All screen recordings saved (if applicable)
- [ ] Participant demographics recorded

---

## Post-Pilot Study Checklist

### Data Analysis (Week 3, Days 1-2)
- [ ] All feedback forms entered into JSON format
- [ ] Analysis script run (`python analyze-pilot-data.py`)
- [ ] Quantitative results calculated (Section A, B, C scores)
- [ ] Behavioral statistics computed (time spent, revisions, etc.)
- [ ] Qualitative responses coded and themed
- [ ] Success metrics evaluated (usability, learning, agency targets)
- [ ] Case study selected and analyzed
- [ ] Results exported to `pilot-data/analysis/`

### Paper Writing (Week 3, Days 3-5)
- [ ] Section 4.6 completed using template (`section-4-6-template.md`)
  - [ ] 4.6.1 Participants and Setting
  - [ ] 4.6.2 Quantitative Results (tables + statistics)
  - [ ] 4.6.3 Behavioral Observations (time + interaction patterns)
  - [ ] 4.6.4 Qualitative Findings (themes + quotes)
  - [ ] 4.6.5 Case Study (detailed example)
  - [ ] 4.6.6 Summary of Findings (success metrics + implications)
- [ ] Tables created and formatted
- [ ] Figures created (if needed)
- [ ] All citations verified
- [ ] References section updated

### Paper Review (Week 4, Days 1-2)
- [ ] Read entire paper for coherence and flow
- [ ] Check all section transitions
- [ ] Verify all tables and figures are referenced in text
- [ ] Proofread for grammar, spelling, clarity
- [ ] Check citation format (Harvard style)
- [ ] Verify all references are cited in text
- [ ] Check word count (conference limit)
- [ ] Verify all author information complete

### Formatting (Week 4, Day 3)
- [ ] Convert to conference template (LaTeX or Word)
- [ ] Check margins, fonts, spacing
- [ ] Verify figure resolution (300 DPI minimum)
- [ ] Check table formatting
- [ ] Verify page numbers
- [ ] Add headers/footers if required
- [ ] Generate PDF
- [ ] Check PDF for formatting issues

### Final Checks (Week 4, Day 4)
- [ ] PDF opens correctly on multiple devices
- [ ] All figures visible and readable
- [ ] All links work (if applicable)
- [ ] File size within limits
- [ ] Supplementary materials prepared (if needed)
- [ ] Cover letter written (if required)
- [ ] Author bios complete
- [ ] Conflict of interest statement (if required)

### Submission (Week 4, Day 5)
- [ ] Create account on conference submission system
- [ ] Upload paper PDF
- [ ] Upload supplementary materials (if any)
- [ ] Enter all author information
- [ ] Select track/topic area
- [ ] Enter keywords
- [ ] Write abstract (if separate from paper)
- [ ] Review submission preview
- [ ] Submit paper
- [ ] Save confirmation email
- [ ] Notify all co-authors

---

## Post-Submission Checklist

### Immediate (Day of Submission)
- [ ] Confirmation email received
- [ ] Submission ID recorded
- [ ] All co-authors notified
- [ ] Backup copy of submission saved

### Follow-Up (Weeks After Submission)
- [ ] Check email regularly for reviewer questions
- [ ] Prepare presentation (if accepted)
- [ ] Register for conference (if accepted)
- [ ] Book travel/accommodation (if in-person)
- [ ] Prepare camera-ready version (if accepted)
- [ ] Update CV/publication list

---

## Timeline Summary

| Week | Focus | Key Deliverables |
|------|-------|------------------|
| **Week 1** | Recruitment + Setup | 5-8 participants scheduled, materials ready |
| **Week 2** | Pilot Sessions | 5-8 sessions completed, data collected |
| **Week 3** | Analysis + Writing | Section 4.6 complete, results analyzed |
| **Week 4** | Review + Submission | Paper formatted, submitted to conference |

---

## Critical Path Items

**Must Complete Before Submission:**
1. ✅ Run pilot study (5-8 participants)
2. ✅ Analyze data and write Section 4.6
3. ✅ Format paper according to conference guidelines
4. ✅ Submit before deadline

**Conference Deadlines:**
- **LAK 2027:** [Check website for exact date]
- **AIED 2027:** [Check website for exact date]

---

## Risk Mitigation

### If Pilot Study Fails
- **Risk:** Low participation, technical issues, negative feedback
- **Mitigation:** 
  - Extend pilot period by 1 week
  - Simplify prototype if needed
  - Focus paper on design framework rather than empirical results
  - Submit to workshop instead of main conference

### If Analysis Takes Too Long
- **Risk:** Not enough time to write Section 4.6
- **Mitigation:**
  - Use analysis script to automate calculations
  - Focus on key findings (don't try to report everything)
  - Use template to speed up writing
  - Ask co-authors for help with writing

### If Formatting Issues Arise
- **Risk:** Paper doesn't meet conference requirements
- **Mitigation:**
  - Start formatting early (don't leave to last day)
  - Use conference template from the start
  - Check requirements carefully before submission
  - Ask colleagues to review formatting

---

## Quick Reference

### File Locations
- **Paper:** `/Users/ailcshum/workspace/research-notes/public/conference-papers/ai-wiki-companion-2026.md`
- **Section 4.6 Template:** `/Users/ailcshum/workspace/research-notes/section-4-6-template.md`
- **Analysis Script:** `/Users/ailcshum/workspace/research-notes/analyze-pilot-data.py`
- **Pilot Data:** `/Users/ailcshum/workspace/research-notes/pilot-data/`
- **Backend Code:** `/Users/ailcshum/workspace/research-notes/api_server.py`
- **Frontend Code:** `/Users/ailcshum/workspace/research-notes/public/js/ai-companion.js`

### Server Commands
```bash
# Start backend API
cd /Users/ailcshum/workspace/research-notes
python api_server.py

# Start frontend web server
cd /Users/ailcshum/workspace/research-notes/public
python -m http.server 8000

# Run analysis script
cd /Users/ailcshum/workspace/research-notes
python analyze-pilot-data.py
```

### Access URLs
- **Frontend:** http://localhost:8000/ai-wiki.html
- **Backend API:** http://localhost:5001/api/wiki/

---

## Success Criteria

**Paper Submission Success:**
- [ ] Paper submitted before deadline
- [ ] All authors approve final version
- [ ] Formatting meets conference requirements
- [ ] All required sections complete

**Pilot Study Success:**
- [ ] 5-8 participants complete sessions
- [ ] Usability score ≥ 3.5/5.0
- [ ] Learning value ≥ 3.5/5.0
- [ ] Epistemic agency ≥ 4.0/5.0
- [ ] Completion rate ≥ 80%

**System Success:**
- [ ] Zero crashes during pilot
- [ ] All 5 API endpoints working
- [ ] Data persistence verified
- [ ] Response time < 200ms

---

## Notes Section

Use this space to track important details:

**Conference Name:** _______________________  
**Submission Deadline:** _______________________  
**Submission Portal URL:** _______________________  
**Submission ID (after submission):** _______________________  

**Co-Authors:**
1. _______________________
2. _______________________
3. _______________________

**Key Contacts:**
- Conference Chair: _______________________
- Technical Support: _______________________
- Co-author contact: _______________________

---

## Final Reminder

**You've got this!** 🎉

All preparation is complete:
- ✅ Theoretical framework enhanced
- ✅ Backend API implemented
- ✅ Frontend integrated
- ✅ Pilot materials ready
- ✅ Analysis script tested
- ✅ Paper Section 3.6 written
- ✅ Section 4.6 template ready

**Next steps:**
1. Recruit participants
2. Run pilot sessions
3. Analyze data
4. Write Section 4.6
5. Submit paper

**Good luck!** 🚀
