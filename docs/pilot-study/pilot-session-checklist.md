# Pilot Session Execution Checklist

**Use this checklist for each pilot session to ensure consistency and completeness.**

---

## Pre-Session Preparation (15 minutes before)

### Technical Setup
- [ ] Verify backend API is running: `curl http://localhost:5001/api/wiki/construct`
- [ ] Verify frontend is accessible: `curl http://localhost:8000/ai-wiki.html`
- [ ] Test one complete flow with dummy data (overfitting concept)
- [ ] Check that data is being saved to `_data/users/{username}/wiki_data.json`
- [ ] Ensure backup laptop is charged and ready (if available)

### Materials Preparation
- [ ] Print participant guide (1 copy)
- [ ] Print feedback form (1 copy)
- [ ] Prepare observation notebook or digital note-taking app
- [ ] Have pen/pencil ready for notes
- [ ] Prepare consent form (if required by IRB/ethics board)
- [ ] Set up screen recording software (optional, if consent obtained)

### Environment Setup
- [ ] Quiet room with minimal distractions
- [ ] Comfortable seating for participant
- [ ] Good lighting for observation
- [ ] Power outlets available for laptops
- [ ] Water/snacks available (optional)

---

## Session Start (5 minutes)

### Welcome and Introduction
- [ ] Greet participant warmly
- [ ] Introduce yourself and your role
- [ ] Explain study purpose: "We're testing a tool that helps you learn ML concepts by writing your own explanations and getting AI feedback"
- [ ] Emphasize: "There are no right or wrong answers—we're testing the tool, not you"
- [ ] Explain time commitment: "This will take about 45 minutes"
- [ ] Obtain informed consent (if required)
- [ ] Answer any initial questions

### Technical Instructions
- [ ] Ask participant to open browser to `http://localhost:8000/ai-wiki.html`
- [ ] Verify page loads correctly
- [ ] Point out the AI Companion sidebar on the right
- [ ] Explain they'll see instructions in the participant guide
- [ ] Offer to answer questions during the session

---

## Session 1: Knowledge Construction (30 minutes)

### Step 1: Access the AI Wiki (2 minutes)
- [ ] Participant navigates to wiki page
- [ ] Confirm page loads correctly
- [ ] Participant sees AI Companion sidebar

### Step 2: Select a Concept (2 minutes)
- [ ] Participant chooses concept (overfitting, regularisation, or cross-validation)
- [ ] Note which concept they chose: _______________
- [ ] Participant clicks on concept name

### Step 3: Construct - Write Explanation (10 minutes)
- [ ] Participant clicks "Construct" button
- [ ] Participant writes explanation in their own words
- [ ] Observe: How long do they spend writing? _____ minutes
- [ ] Observe: Do they seem confident or uncertain? ☐ Confident ☐ Uncertain ☐ Mixed
- [ ] Participant clicks "Save & Reflect"
- [ ] Confirm they see: ✅ "Entry saved to your knowledge base"

### Step 4: Reflect - Answer Questions (5 minutes)
- [ ] System generates reflection prompts automatically
- [ ] Participant reads each question
- [ ] Observe: Do they answer thoughtfully or quickly? ☐ Thoughtful ☐ Quick ☐ Mixed
- [ ] Note any interesting responses or behaviors:
  - _________________________________________________
  - _________________________________________________
- [ ] Participant clicks "Continue to Scaffold"

### Step 5: Scaffold - Receive AI Feedback (5 minutes)
- [ ] Participant clicks "Detect Knowledge Gaps"
- [ ] System shows missing concepts and suggestions
- [ ] Observe: Do they read carefully or skim? ☐ Careful ☐ Skim ☐ Mixed
- [ ] Note their reaction to feedback:
  - _________________________________________________
  - _________________________________________________
- [ ] Ask (if appropriate): "Does this feedback make sense?"

### Step 6: Consolidate - Apply Knowledge (10 minutes)
- [ ] Participant clicks "Consolidate"
- [ ] System presents application scenario
- [ ] Participant writes response
- [ ] Observe: How long do they spend? _____ minutes
- [ ] Observe: Do they seem to understand the task? ☐ Yes ☐ Unsure ☐ Confused
- [ ] Participant clicks "Get Feedback"
- [ ] Note their reaction to consolidation task:
  - _________________________________________________
  - _________________________________________________

### Step 7: Revisit - Connect Concepts (5 minutes)
- [ ] Participant clicks "Revisit"
- [ ] System shows related concepts (if any)
- [ ] Observe: Do they explore connections? ☐ Yes ☐ No ☐ Limited
- [ ] Note any insights or comments:
  - _________________________________________________
  - _________________________________________________

---

## Feedback Form (5 minutes)

### Completion
- [ ] Hand participant the feedback form
- [ ] Explain: "Please answer all questions honestly—there are no right or wrong answers"
- [ ] Allow them to complete independently
- [ ] Be available for questions but don't influence responses
- [ ] Collect completed form

### Quick Debrief (Optional, 5 minutes)
- [ ] Ask: "What was the most helpful part?"
  - Response: _________________________________________________
- [ ] Ask: "What was confusing or didn't work well?"
  - Response: _________________________________________________
- [ ] Ask: "What would you change or add?"
  - Response: _________________________________________________
- [ ] Ask: "How does this compare to other ways you've learned ML?"
  - Response: _________________________________________________

---

## Post-Session (10 minutes)

### Data Collection
- [ ] Collect feedback form (check all sections are completed)
- [ ] Save observation notes
- [ ] Export interaction logs from `_data/users/{username}/wiki_data.json`
- [ ] Save screen recording (if applicable)
- [ ] Note any technical issues encountered:
  - _________________________________________________
  - _________________________________________________

### Researcher Notes (Fill in feedback form Section F)
- [ ] Participant's engagement level: ☐ Low ☐ Medium ☐ High
- [ ] Key insights or quotes:
  - _________________________________________________
  - _________________________________________________
  - _________________________________________________
- [ ] Notable behaviors:
  - _________________________________________________
  - _________________________________________________
- [ ] Technical issues:
  - _________________________________________________
  - _________________________________________________
- [ ] Recommendations for next iteration:
  - _________________________________________________
  - _________________________________________________

### Time Tracking (Fill in feedback form Section E)
- [ ] Construct: _____ minutes
- [ ] Reflect: _____ minutes
- [ ] Scaffold: _____ minutes
- [ ] Consolidate: _____ minutes
- [ ] Revisit: _____ minutes
- [ ] Feedback form: _____ minutes
- [ ] Total session time: _____ minutes

### Interaction Patterns (Fill in feedback form Section E)
- [ ] Number of revisions to explanation: _____
- [ ] Number of times AI feedback was requested: _____
- [ ] Number of related concepts explored: _____

---

## Session End

### Wrap-Up
- [ ] Thank participant for their time
- [ ] Answer any final questions
- [ ] Provide contact information for follow-up questions
- [ ] Offer incentive (if applicable): ☐ Gift card ☐ Course credit ☐ Other: _____
- [ ] Schedule Session 2 (if applicable): Date: _______________

### Cleanup
- [ ] Clear browser data (if using shared computer)
- [ ] Close all tabs and windows
- [ ] Put away materials
- [ ] Prepare for next session (if applicable)

---

## Troubleshooting Guide

### Common Issues

**Issue: Page doesn't load**
- Check URL: `http://localhost:8000/ai-wiki.html`
- Verify web server is running: `ps aux | grep "http.server"`
- Restart if needed: `cd /Users/ailcshum/workspace/research-notes/public && python -m http.server 8000`

**Issue: "Save failed" error**
- Check API server is running: `curl http://localhost:5001/api/wiki/construct`
- Verify backend is running: `ps aux | grep "api_server.py"`
- Restart if needed: `cd /Users/ailcshum/workspace/research-notes && python api_server.py`

**Issue: No reflection prompts appear**
- Refresh the page (Ctrl+R or Cmd+R)
- Try a different concept
- Check browser console for errors (F12 → Console tab)

**Issue: AI Companion sidebar not visible**
- Scroll to right side of page
- Check if sidebar is collapsed (look for expand button)
- Refresh the page

**Issue: Participant confused by instructions**
- Read instructions aloud together
- Walk through first step together
- Offer to stay nearby for questions
- Reassure them there are no wrong answers

---

## Data Backup (After Each Session)

### Immediate Backup
- [ ] Copy feedback form to secure location
- [ ] Copy observation notes to secure location
- [ ] Export interaction logs: `cp _data/users/{username}/wiki_data.json ~/pilot-data/session-{N}-{date}.json`
- [ ] Copy screen recording (if applicable): `cp ~/screen-recording-{N}.mov ~/pilot-data/`

### Organize Files
```
~/pilot-data/
├── session-1-2026-09-05/
│   ├── feedback-form.pdf
│   ├── observation-notes.md
│   ├── interaction-logs.json
│   └── screen-recording.mov (optional)
├── session-2-2026-09-06/
│   └── ...
└── summary/
    └── (created after all sessions complete)
```

---

## Post-Session Reflection (Researcher)

### What Went Well?
- _________________________________________________
- _________________________________________________
- _________________________________________________

### What Could Be Improved?
- _________________________________________________
- _________________________________________________
- _________________________________________________

### Unexpected Observations
- _________________________________________________
- _________________________________________________
- _________________________________________________

### Questions for Next Session
- _________________________________________________
- _________________________________________________
- _________________________________________________

---

## Quick Reference

### Server Commands
```bash
# Start backend API
cd /Users/ailcshum/workspace/research-notes
python api_server.py

# Start frontend web server
cd /Users/ailcshum/workspace/research-notes/public
python -m http.server 8000

# Check if servers are running
ps aux | grep -E "api_server|http.server"
```

### Access URLs
- Frontend: `http://localhost:8000/ai-wiki.html`
- Backend API: `http://localhost:5001/api/wiki/`

### Test Commands
```bash
# Test backend
curl -X POST http://localhost:5001/api/wiki/construct \
  -H "Content-Type: application/json" \
  -d '{"concept":"test","explanation":"test"}'

# Expected response:
# {"success":true,"entry_id":"test","message":"Entry saved successfully"}
```

---

## Session Summary Template

**Participant ID:** _____  
**Date:** _______________  
**Session Number:** ☐ 1 ☐ 2  
**Concept Explored:** _______________  
**Total Time:** _____ minutes  

**Engagement Level:** ☐ Low ☐ Medium ☐ High  
**Technical Issues:** ☐ None ☐ Minor ☐ Major  

**Key Findings:**
- _________________________________________________
- _________________________________________________
- _________________________________________________

**Action Items:**
- _________________________________________________
- _________________________________________________
- _________________________________________________

---

**Print this checklist for each session. Check off items as you complete them.**
