# Conference Paper Submission Preparation

**Paper:** From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction  
**Target Venues:** LAK 2027 or AIED 2027  
**Date:** 2026-09-03

---

## Pre-Submission Checklist

### Paper Content ✓
- [x] Title and abstract (updated with pilot findings)
- [x] Introduction (Sections 1.1-1.4)
- [x] Theoretical background (Section 2)
- [x] Proposed framework (Section 3, including 3.6 Prototype)
- [x] Formative evaluation (Section 4, including 4.6 Pilot results)
- [x] Discussion (Section 5)
- [x] Limitations (Section 6)
- [x] Conclusion (Section 7)
- [x] References (complete with all citations)
- [x] Two figures (framework diagram, learning cycle)
- [x] Seven tables (properly numbered)

### Formatting Requirements
- [ ] Convert to conference template (LaTeX or Word)
- [ ] Check page limits (typically 8-10 pages)
- [ ] Verify figure resolution (300 DPI minimum)
- [ ] Check reference format (APA or conference-specific)
- [ ] Ensure all figures/tables are referenced in text
- [ ] Add keywords (5-6 keywords)
- [ ] Verify author information and affiliations
- [ ] Check accessibility (alt text for figures)

### Supplementary Materials
- [ ] Create cover letter
- [ ] Prepare author biographies (if required)
- [ ] Prepare conflict of interest statement
- [ ] Prepare data availability statement
- [ ] Prepare ethics approval statement
- [ ] Create supplementary appendix (if needed)

### Final Checks
- [ ] Proofread for grammar and spelling
- [ ] Check all citations match references
- [ ] Verify all figures are clear and readable
- [ ] Test all links (if any)
- [ ] Check file naming conventions
- [ ] Verify submission platform requirements

---

## Cover Letter Template

```
[Date]

Program Committee
[Conference Name] 2027

Dear Program Committee,

We are pleased to submit our paper "From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction" for consideration at [Conference Name] 2027.

This paper addresses a critical challenge in educational AI: how to leverage generative AI capabilities while preserving learner agency and promoting deep knowledge construction. We present a learner-in-the-loop framework that positions AI as a metacognitive scaffold rather than a knowledge substitute, implemented through a five-stage knowledge construction cycle.

Our key contributions include:
1. A theoretical framework extending human-in-the-loop concepts to educational theory
2. Four operational design principles for AI-supported learning
3. A functional prototype implementing the complete framework
4. Formative evaluation results from a pilot study (N=7) demonstrating preserved epistemic agency (M=4.36/5.0) and iterative knowledge revision

This work aligns with [Conference Name]'s focus on [specific track/theme], as it bridges learning analytics, human-computer interaction, and educational AI design.

We confirm that this submission is original work, has not been published previously, and is not under consideration elsewhere. All authors have approved the submission and have no conflicts of interest to declare.

Thank you for considering our submission. We look forward to your feedback.

Sincerely,
[Author Names]
[Affiliations]
[Contact Information]
```

---

## Venue-Specific Requirements

### LAK 2027 (Learning Analytics & Knowledge)
- **Track:** Design and Development
- **Page limit:** Typically 10 pages + references
- **Format:** ACM template (LaTeX preferred)
- **Double-blind:** Yes (anonymize submission)
- **Key dates:** Check conference website
- **Focus areas:** Learning analytics, knowledge construction, educational data mining

**LAK-specific considerations:**
- Emphasize learning analytics aspects (interaction logs, revision tracking)
- Highlight data collection methods and analysis
- Include learning outcome measures
- Discuss scalability and deployment

### AIED 2027 (Artificial Intelligence in Education)
- **Track:** Full Paper or Design Paper
- **Page limit:** Typically 12 pages + references
- **Format:** IOS Press template
- **Double-blind:** Yes
- **Key dates:** Check conference website
- **Focus areas:** AI in education, intelligent tutoring, adaptive learning

**AIED-specific considerations:**
- Emphasize AI scaffolding mechanisms
- Detail the Prompt Before Provide algorithm
- Discuss AI response quality and limitations
- Include user study methodology details

---

## Paper Formatting Guide

### Converting to LaTeX

1. **Download conference template**
   - LAK: ACM template from https://www.acm.org/publications/proceedings-template
   - AIED: IOS Press template from conference website

2. **Structure the LaTeX document**
   ```latex
   \documentclass{sigconf} % or appropriate class
   
   \title{From Notes to Knowledge...}
   \author{...}
   
   \begin{document}
   \maketitle
   
   \begin{abstract}
   [Abstract text]
   \end{abstract}
   
   \begin{CCSXML}
   [CCS concepts if required]
   \end{CCSXML}
   
   \keywords{AI in education, knowledge construction, learner-in-the-loop, metacognition, scaffolding}
   
   \section{Introduction}
   [Content]
   
   % ... remaining sections ...
   
   \bibliographystyle{ACM-Reference-Format}
   \bibliography{references}
   
   \end{document}
   ```

3. **Convert figures**
   - Export ASCII diagrams to PDF/SVG (300 DPI)
   - Or recreate in TikZ/PGFPlots for LaTeX
   - Ensure figures are referenced in text

4. **Convert references**
   - Create BibTeX file from reference list
   - Ensure all citations have corresponding entries

### Converting to Word

1. **Download conference template**
   - Use provided Word template

2. **Apply styles**
   - Use template styles for headings, body text, captions
   - Maintain consistent formatting

3. **Insert figures**
   - Insert as high-resolution images
   - Add captions below figures

4. **Manage references**
   - Use Word's reference manager or manual formatting
   - Ensure consistent citation format

---

## Anonymization Checklist (for double-blind review)

- [ ] Remove author names from title page
- [ ] Remove affiliations
- [ ] Remove acknowledgments
- [ ] Check self-citations (use "Author et al." or anonymize)
- [ ] Remove URLs that reveal identity
- [ ] Check file metadata (author info in PDF properties)
- [ ] Remove supplementary materials with identifying info
- [ ] Check code repositories (if mentioned)
- [ ] Anonymize institutional review board references

---

## Submission Platform Preparation

### Common Platforms
- **HotCRP:** Most common for CS conferences
- **EasyChair:** Used by some education conferences
- **OpenReview:** Used by some AI/ML venues

### Account Setup
- [ ] Create account on submission platform
- [ ] Verify email address
- [ ] Complete profile information
- [ ] Add co-authors (if required)

### Submission Process
1. Log in to submission platform
2. Create new submission
3. Select track/category
4. Upload paper (PDF)
5. Upload supplementary materials (if any)
6. Enter metadata (title, abstract, keywords, authors)
7. Confirm compliance with policies
8. Submit and confirm receipt

---

## Post-Submission Timeline

### Immediate (Day of submission)
- [ ] Save submission confirmation
- [ ] Notify all co-authors
- [ ] Back up submission files
- [ ] Add to calendar: notification date

### Waiting Period (2-4 months)
- [ ] Continue related work
- [ ] Prepare presentation (if accepted)
- [ ] Plan travel arrangements (if in-person)
- [ ] Prepare camera-ready version (if accepted)

### After Notification
**If accepted:**
- [ ] Prepare camera-ready version
- [ ] Address reviewer comments
- [ ] Register for conference
- [ ] Prepare presentation/poster
- [ ] Arrange travel and accommodation

**If rejected:**
- [ ] Review feedback carefully
- [ ] Revise paper based on comments
- [ ] Submit to alternative venue
- [ ] Consider workshop submission

---

## Alternative Venues (if needed)

### Education & Technology
- EDM (Educational Data Mining)
- ITS (Intelligent Tutoring Systems)
- ICER (International Computing Education Research)
- SIGCSE (Technical Symposium on CS Education)

### HCI & Interaction
- CHI (Human Factors in Computing Systems)
- CSCW (Computer-Supported Cooperative Work)
- DIS (Designing Interactive Systems)

### AI & Learning
- AIEd (AI in Education)
- EDM (Educational Data Mining)
- L@S (Learning @ Scale)

### Workshops
- LAK Workshop on Learning Analytics
- AIED Workshop on AI-Supported Learning
- CHI Workshop on Educational HCI

---

## Estimated Timeline

| Task | Time Required | Status |
|------|---------------|--------|
| Convert to LaTeX/Word | 2-3 hours | ⏳ Pending |
| Format figures | 1-2 hours | ⏳ Pending |
| Format references | 1 hour | ⏳ Pending |
| Proofread | 2-3 hours | ⏳ Pending |
| Create cover letter | 30 minutes | ⏳ Pending |
| Prepare supplementary | 1-2 hours | ⏳ Pending |
| Submit | 30 minutes | ⏳ Pending |
| **Total** | **8-12 hours** | |

---

## Quick Start Guide

**If submitting this week:**

1. **Choose venue** (LAK or AIED)
2. **Download template** (LaTeX or Word)
3. **Convert paper** (2-3 hours)
4. **Format figures** (1 hour)
5. **Proofread** (2 hours)
6. **Create cover letter** (30 minutes)
7. **Submit** (30 minutes)

**Total time:** 6-7 hours

---

## Support Resources

### Template Help
- Overleaf (online LaTeX editor): https://www.overleaf.com
- Conference template documentation
- LaTeX forums: https://tex.stackexchange.com

### Writing Help
- Grammarly: https://www.grammarly.com
- Hemingway Editor: http://www.hemingwayapp.com
- Academic writing guides

### Submission Help
- Conference website FAQs
- Program committee contacts
- Academic mentorship networks

---

## Final Recommendations

1. **Start early:** Don't wait until the deadline
2. **Test formatting:** Compile PDF and check on different devices
3. **Get feedback:** Ask colleagues to proofread
4. **Backup everything:** Keep copies of all files
5. **Follow guidelines:** Strictly adhere to formatting requirements
6. **Check twice:** Verify all requirements before submitting

---

**Next Action:** Choose your target venue (LAK or AIED) and begin formatting the paper to their template.
