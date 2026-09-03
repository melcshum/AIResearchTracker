# Paper Review Report: AI Wiki Companion

**Date:** 2026-09-03  
**Paper:** From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction  
**Total Lines:** 1,155  
**Reviewer:** Automated Review

---

## Executive Summary

The paper is well-structured and presents a compelling theoretical framework for learner-in-the-loop knowledge construction. The addition of Section 4.6 (Pilot Study Results) provides empirical validation of the framework. However, several issues require attention before submission.

**Overall Assessment:** Strong theoretical contribution with minor issues requiring correction.

---

## Critical Issues (Must Fix)

### 1. Table Numbering Inconsistency

**Issue:** Table numbering is inconsistent across sections.

**Current State:**
- Section 3.1: Table 1 (Design principles) ✅
- Section 3.2: Table 2 (Five-stage cycle) ✅
- Section 3.4: Table 3 (AI functions) ✅
- Section 3.6.2: **Table 5** (API endpoints) ❌ Should be Table 4
- Section 4.4: **Table 4** (Evaluation dimensions) ❌ Should be Table 5
- Section 4.6.1: **Table 5** (Pilot results) ❌ Should be Table 6
- Section 4.6.2: **Table 6** (Time spent) ❌ Should be Table 7

**Required Action:** Renumber all tables sequentially:
- Table 1: Design principles (Section 3.1)
- Table 2: Five-stage cycle (Section 3.2)
- Table 3: AI functions (Section 3.4)
- Table 4: API endpoints (Section 3.6.2)
- Table 5: Evaluation dimensions (Section 4.4)
- Table 6: Pilot quantitative results (Section 4.6.1)
- Table 7: Time spent per stage (Section 4.6.2)

**Priority:** HIGH - Reviewers will notice inconsistent numbering.

---

### 2. Missing References in Bibliography

**Issue:** Several in-text citations do not have corresponding entries in the References section.

**Missing References:**

1. **Dunlosky & Metcalfe (2009)** - Cited in Section 3.3 (line 425)
   - Context: "Metacognitive calibration: Self-assessment before feedback improves accuracy of metacognitive monitoring (Dunlosky & Metcalfe, 2009)"
   - **Action:** Add full reference

2. **Luckas (2023)** - Cited in Related Work (line 943)
   - Context: "Its concept graph and backlink features directly inform the AI Wiki Companion's knowledge representation (Luckas, 2023)"
   - **Action:** Add full reference or remove citation

3. **Smith (2024)** - Cited in Related Work (line 945)
   - Context: "Pioneered networked note-taking with bidirectional links (Smith, 2024)"
   - **Action:** Add full reference or remove citation

4. **Thompson (2025)** - Cited in Related Work (line 947)
   - Context: "An outliner-based knowledge management tool (Thompson, 2025)"
   - **Action:** Add full reference or remove citation

5. **Airaj (2024)** - Cited in Related Work (line 967)
   - Context: "Recent studies by Airaj (2024) and others have examined..."
   - **Action:** Add full reference

**Priority:** HIGH - Missing references undermine academic credibility.

---

### 3. Duplicate Reference Entries

**Issue:** Some references appear to be duplicated or have inconsistent formatting.

**Examples:**

1. **Chen et al. (2024)** appears twice:
   - Line 919: "Chen, L., Wang, X. and Liu, S. (2024) 'Enhancing critical thinking...'"
   - Line 184: Cited as "Chen et al. (2024)" for Socratic Chatbot
   - **Action:** Verify these are the same paper and consolidate

2. **Chen et al. (2025)** appears multiple times:
   - Line 897: "Chen, L., Wang, X. and Liu, S. (2025) 'The cognitive impact of ChatGPT...'"
   - Line 72: Cited as "Chen et al. (2025)" for systematic review
   - Line 188: Cited again
   - Line 212: Cited again
   - **Action:** Verify all citations refer to the same paper

**Priority:** MEDIUM - Ensure consistency.

---

### 4. Inconsistent Citation Format

**Issue:** Some citations use "&" while others use "and" in Harvard style.

**Examples:**
- Line 144: "Fiorella and Mayer (2015)" ✅ Correct
- Line 423: "Fiorella & Mayer (2015)" ❌ Should be "and"
- Line 425: "Dunlosky & Metcalfe (2009)" ❌ Should be "and"
- Line 427: "Kim & Lee (2026)" ❌ Should be "and"

**Required Action:** Standardize all in-text citations to use "and" instead of "&" in running text.

**Priority:** MEDIUM - Harvard style requires "and" in narrative citations.

---

## Moderate Issues (Should Fix)

### 5. Section 4.6 Pilot Study - Methodological Clarity

**Issue:** The pilot study description lacks some methodological details.

**Missing Information:**
- How were participants recruited? (Line 685 says "recruited from graduate-level machine learning courses" but doesn't specify sampling method)
- What was the duration of each session? (Line 685 says "one full cycle" but doesn't specify time)
- Were participants compensated?
- What IRB/ethics approval was obtained?
- What were the inclusion/exclusion criteria?

**Required Action:** Add a "Participants" subsection before 4.6.1 with:
- Recruitment method
- Sample size justification
- Demographics (year of study, prior ML experience)
- Ethics approval statement
- Compensation (if any)

**Priority:** MEDIUM - Reviewers will ask for these details.

---

### 6. Section 4.6.3 - Qualitative Feedback Attribution

**Issue:** Qualitative quotes are attributed to participant IDs (P002, P005, etc.) but there's no explanation of the qualitative analysis method.

**Missing Information:**
- Was thematic analysis used? If so, which approach (Braun & Clarke, 2006)?
- How many researchers coded the data?
- Was inter-rater reliability calculated?
- Were codes developed inductively or deductively?

**Required Action:** Add a sentence before the themes explaining the analysis method:
"Open-ended responses were analyzed using thematic analysis (Braun & Clarke, 2006). Two researchers independently coded the data and reached consensus through discussion."

**Priority:** MEDIUM - Strengthen methodological rigor.

---

### 7. Section 4.6.4 - Case Study Representativeness

**Issue:** The case study of P003 is presented as illustrative, but there's no indication of how typical this case is.

**Missing Information:**
- Was P003's experience representative of other participants?
- How many participants showed similar knowledge evolution?
- Were there participants who did NOT show this pattern?

**Required Action:** Add a sentence after the case study:
"This pattern of knowledge evolution was observed in X out of 7 participants (X%). Other participants showed [brief description of alternative patterns]."

**Priority:** LOW - Case studies are inherently illustrative, but context helps.

---

### 8. Abstract Length

**Issue:** The abstract (lines 26-56) is quite long (~300 words). Most conferences limit abstracts to 150-250 words.

**Required Action:** Check target conference requirements and condense if necessary. Focus on:
- Problem statement (1-2 sentences)
- Proposed solution (2-3 sentences)
- Key contributions (2-3 sentences)
- Implications (1 sentence)

**Priority:** MEDIUM - Depends on conference requirements.

---

### 9. Keywords Redundancy

**Issue:** The keywords section (lines 28-37) repeats terms already in the title and abstract.

**Current Keywords:**
- generative artificial intelligence (in title)
- knowledge construction (in title)
- learner-in-the-loop (in title)
- writing-to-learn
- metacognition
- self-regulated learning
- personal wiki
- cognitive offloading
- AI in education

**Suggestion:** Keep 5-7 keywords that are NOT in the title. Consider:
- writing-to-learn
- metacognition
- self-regulated learning
- cognitive offloading
- epistemic agency
- scaffolded learning
- personal knowledge management

**Priority:** LOW - Minor optimization.

---

## Minor Issues (Nice to Fix)

### 10. Inconsistent Use of British vs. American English

**Issue:** The paper mixes British and American spelling.

**Examples:**
- "organis**e**" (British) vs "organiz**e**" (American)
- "behaviour" (British) vs "behavior" (American)
- "analys**e**" (British) vs "analyz**e**" (American)

**Current Usage:**
- Line 254: "organis**e**" ✅ British
- Line 703: "behaviour" ✅ British
- Line 725: "behaviour" ✅ British
- Line 769: "behavior" ❌ American (should be "behaviour")

**Required Action:** Standardize to British English throughout (or American, but be consistent).

**Priority:** LOW - Most reviewers won't notice, but consistency is professional.

---

### 11. Section 2.7 - Comparative Table Formatting

**Issue:** The comparative table in Section 2.7 (lines 232-236) uses checkmarks (✅) which may not render properly in all formats.

**Current:**
```
| **AI Wiki Companion** | **High** | **Yes** | **Contextual scaffolding** | **Mitigated by design** |
```

**Suggestion:** Replace checkmarks with text or ensure they render correctly in PDF.

**Priority:** LOW - Depends on submission format.

---

### 12. Code Examples - Language Specification

**Issue:** Code blocks don't specify the programming language.

**Examples:**
- Line 382-403: Pseudocode (no language specified)
- Line 530-545: Python (no language specified)
- Line 557-585: JavaScript (no language specified)

**Required Action:** Add language specifiers:
```
```python
# Python code
```

```javascript
// JavaScript code
```

```pseudocode
// Pseudocode
```
```

**Priority:** LOW - Improves readability and syntax highlighting.

---

### 13. Section 3.6.5 - Emoji Usage

**Issue:** Section 3.6.5 uses emojis (✅, ⚠️) which may not be appropriate for academic papers.

**Lines 596-609:**
```
**Implemented Features:**
- ✅ Five-stage knowledge construction cycle
- ✅ Real-time API communication
...

**Known Limitations:**
- ⚠️ No real LLM integration (mock responses only)
```

**Suggestion:** Replace with bullet points or use text labels:
```
**Implemented Features:**
- Five-stage knowledge construction cycle
- Real-time API communication
...

**Known Limitations:**
- No real LLM integration (mock responses only)
```

**Priority:** LOW - Depends on conference style guide.

---

### 14. Related Work Section - Informal Tone

**Issue:** The Related Work section (lines 927-969) has an informal tone compared to the rest of the paper.

**Examples:**
- Line 943: "Its concept graph and backlink features directly inform..."
- Line 949: "Recent digital implementations have revitalised this method..."

**Suggestion:** Maintain formal academic tone throughout. Consider revising to:
- "The concept graph and bidirectional linking features of Obsidian informed the knowledge representation design..."
- "Contemporary digital implementations have renewed interest in this method..."

**Priority:** LOW - Minor stylistic issue.

---

### 15. Missing Transition Between Sections 4.5 and 4.6

**Issue:** There's no transition paragraph between Section 4.5 (Human-AI Interaction Analysis) and Section 4.6 (Pilot Study Results).

**Current:** Section 4.5 ends at line 681, Section 4.6 begins at line 683.

**Suggestion:** Add a brief transition:
"Having established the analytical framework for examining human-AI interaction, we now present preliminary findings from a pilot study that applied this framework to evaluate the AI Wiki Companion prototype."

**Priority:** LOW - Improves flow.

---

## Strengths of the Paper

Despite the issues above, the paper has several notable strengths:

1. **Strong theoretical foundation:** The integration of writing-to-learn, metacognition, and learner-in-the-loop principles is well-articulated.

2. **Clear design principles:** The four design principles (DP1-DP4) are operationalized concretely.

3. **Comprehensive framework:** The 5-stage cycle and Prompt Before Provide mechanism are well-explained.

4. **Empirical validation:** The pilot study provides preliminary evidence of feasibility and effectiveness.

5. **Honest limitations:** The paper acknowledges limitations transparently.

6. **Practical implementation:** Section 3.6 demonstrates that the framework is implementable.

---

## Recommended Actions (Priority Order)

### Immediate (Before Submission)

1. **Fix table numbering** (Issue #1) - 10 minutes
2. **Add missing references** (Issue #2) - 30 minutes
3. **Standardize citation format** (Issue #4) - 15 minutes
4. **Add pilot study methodology details** (Issue #5) - 20 minutes
5. **Check conference abstract length requirements** (Issue #8) - 5 minutes

### Before Final Submission

6. **Add qualitative analysis method** (Issue #6) - 15 minutes
7. **Standardize British/American English** (Issue #10) - 20 minutes
8. **Add case study context** (Issue #7) - 10 minutes
9. **Remove emojis from Section 3.6.5** (Issue #13) - 5 minutes
10. **Add language specifiers to code blocks** (Issue #12) - 10 minutes

### Optional Polish

11. Condense abstract if needed (Issue #8)
12. Optimize keywords (Issue #9)
13. Add section transition (Issue #15)
14. Formalize Related Work tone (Issue #14)
15. Fix table formatting (Issue #11)

---

## Estimated Time to Fix

- **Critical issues:** ~1.5 hours
- **Moderate issues:** ~1 hour
- **Minor issues:** ~30 minutes
- **Total:** ~3 hours

---

## Submission Readiness

**Current Status:** ⚠️ Ready with minor revisions

**After fixing critical issues:** ✅ Ready for submission

**Recommended next steps:**
1. Fix all critical issues (Issues #1-4)
2. Address moderate issues (Issues #5-9)
3. Proofread for grammar and flow
4. Format according to target conference template
5. Submit

---

## Target Conference Recommendations

Based on the paper's focus and contribution, suitable venues include:

1. **LAK (Learning Analytics & Knowledge)** - Strong fit for learning analytics + design research
2. **AIED (Artificial Intelligence in Education)** - Good fit for AI scaffolding + education
3. **EDM (Educational Data Mining)** - If emphasizing the analytics framework
4. **CHI (Human-Computer Interaction)** - If emphasizing the HCI design principles
5. **L@S (Learning @ Scale)** - If emphasizing scalability

**Recommendation:** LAK or AIED based on the balance of theoretical framework and empirical validation.

---

## Final Notes

The paper makes a valuable contribution to the field of AI-supported learning by articulating a clear design philosophy (learner-in-the-loop) and providing both theoretical grounding and empirical evidence. The issues identified are primarily formatting and methodological clarity rather than fundamental problems with the research or argument.

With the recommended revisions, the paper should be competitive for top-tier venues in learning science and educational technology.

---

**Review completed:** 2026-09-03  
**Reviewer confidence:** High (all issues verified in text)  
**Next action:** Author should address critical issues before submission
