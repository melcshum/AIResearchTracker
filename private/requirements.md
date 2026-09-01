---
title: "User Requirements"
---

# User Requirements Document

## Executive Summary

The AI Research Tracker is a personalised learning platform powered by AI assistance, designed to help users create their own learning journey. Users enter topics to research and save them to build customised learning paths, while AI tools aid learning and help organise notes. The platform offers structured learning pathways, systematically retrieves research papers and other sources periodically, analyses and builds learning materials, and enhances wiki support with AI-powered features. Behind the scenes, AI-driven automation handles the heavy lifting — fetching papers, enhancing metadata, generating insights, and curating content — so users can focus on learning.

**Current Status:** 111 pages rendered, 77 papers tracked, 346 authors indexed across 4 research domains.

---

## 1. User Personas

### 1.1 New Researcher (Beginner)
**Profile:** Graduate student or professional transitioning into AI research
**Goals:**
- Understand foundational concepts in AI agents, reasoning, RAG, and multi-modal systems
- Build a structured learning path
- Identify key papers and authors in the field

**Pain Points:**
- Overwhelmed by volume of research
- Unclear where to start
- Difficulty understanding technical jargon
- No clear progression path

**Key Needs:**
- ✅ Learning paths (exists)
- ✅ Glossary of terms (exists)
- ⚠️ Guided tutorials (partial)
- ❌ Concept difficulty indicators (missing)
- ❌ Prerequisite mapping (missing)

### 1.2 Active Researcher
**Profile:** PhD student, postdoc, or faculty publishing in AI
**Goals:**
- Stay current with latest papers in their specialization
- Track reading progress across multiple papers
- Identify gaps in literature
- Build citation networks
- Collaborate with peers

**Pain Points:**
- Too many papers to read manually
- Hard to track what they've already read
- Missing connections between papers
- No way to see citation impact
- Difficult to organize papers by project

**Key Needs:**
- ✅ Paper search and filtering (exists)
- ✅ Reading list with status tracking (exists)
- ✅ Notes and annotations (exists)
- ✅ BibTeX export (exists)
- ❌ Paper recommendations (missing)
- ❌ Citation network visualization (missing)
- ❌ Reading progress analytics (missing)
- ❌ Collaboration features (missing)
- ❌ Code repository links (missing)

### 1.3 Practitioner/Engineer
**Profile:** Industry professional applying AI techniques
**Goals:**
- Find practical implementations of research
- Identify state-of-the-art methods for specific problems
- Access code and benchmarks
- Understand trade-offs between approaches

**Pain Points:**
- Research papers lack implementation details
- Hard to find working code
- No benchmarks or comparisons
- Unclear which methods work in practice

**Key Needs:**
- ✅ Comparison tables (exists)
- ⚠️ Code links (partial)
- ❌ Implementation summaries (missing)
- ❌ Benchmark results (missing)
- ❌ "How to use this" guides (missing)
- ❌ Production readiness indicators (missing)

### 1.4 Admin/Maintainer
**Profile:** System administrator or project maintainer
**Goals:**
- Ensure system reliability
- Monitor usage and performance
- Manage content quality
- Configure automation

**Pain Points:**
- Limited visibility into system health
- No usage analytics
- Hard to track data quality
- Manual intervention required for updates

**Key Needs:**
- ✅ Admin dashboard (exists)
- ✅ Settings page (exists)
- ✅ Automation scripts (exists)
- ❌ Usage analytics (missing)
- ❌ Error monitoring (missing)
- ❌ Content quality metrics (missing)

---

## 2. Functional Requirements

### 2.1 Paper Discovery & Search

#### FR-1: Advanced Search
**Priority:** P0 (Critical)
**Status:** ✅ Implemented

Users can search papers by:
- Full-text search across titles, abstracts, authors
- Filter by topic, date range, author
- Filter by keywords and concepts

**Current Implementation:**
- `search-papers.html` with full-text search
- Topic-based filtering
- Date range selection

**Gaps:**
- No semantic search (only keyword matching)
- No search history
- No saved searches

#### FR-2: Paper Recommendations
**Priority:** P1 (High)
**Status:** ❌ Not Implemented

System should recommend related papers based on:
- User's reading history
- Papers in reading list
- Topic interests
- Citation relationships

**Acceptance Criteria:**
- "You might also like" section on each paper
- Personalized recommendations on dashboard
- "More like this" button

#### FR-3: Paper Alerts
**Priority:** P1 (High)
**Status:** ❌ Not Implemented

Users can subscribe to alerts for:
- New papers in specific topics
- Papers by specific authors
- Papers matching custom queries

**Acceptance Criteria:**
- Email notification option
- In-app notification center
- Alert management interface

### 2.2 Reading & Annotation

#### FR-4: Reading Progress Tracking
**Priority:** P0 (Critical)
**Status:** ⚠️ Partially Implemented

Users can track reading progress with:
- Visual progress indicators
- Status: To Read → Reading → Read → Archived
- Time spent reading
- Completion percentage

**Current Implementation:**
- Reading list with status tracking
- Notes per paper

**Gaps:**
- No visual progress bars
- No time tracking
- No reading statistics
- No integration with dashboard

#### FR-5: Enhanced Annotations
**Priority:** P1 (High)
**Status:** ⚠️ Partially Implemented

Users can annotate papers with:
- Highlighted text
- Comments and notes
- Tags and categories
- Structured summaries (TL;DR, key findings, methodology)

**Current Implementation:**
- Basic notes field per paper

**Gaps:**
- No text highlighting
- No structured note templates
- No note search
- No note export

#### FR-6: Reading Time Estimates
**Priority:** P2 (Medium)
**Status:** ❌ Not Implemented

Display estimated reading time for each paper based on:
- Abstract length
- Paper length (if available)
- Technical complexity

**Acceptance Criteria:**
- Display "X min read" on paper cards
- Account for user's reading speed preference

### 2.3 Knowledge Management

#### FR-7: Paper Collections
**Priority:** P1 (High)
**Status:** ⚠️ Partially Implemented

Users can create custom paper collections:
- Named lists (e.g., "PhD Thesis Papers", "Project X")
- Public or private visibility
- Shareable links
- Collection descriptions

**Current Implementation:**
- Reading list (single list only)

**Gaps:**
- Only one reading list
- No custom collections
- No sharing capability

#### FR-8: Citation Network Visualization
**Priority:** P1 (High)
**Status:** ❌ Not Implemented

Visualize citation relationships:
- Interactive graph of papers and citations
- Click to navigate between papers
- Filter by citation direction (cites/cited by)
- Highlight key papers

**Acceptance Criteria:**
- Interactive D3.js or similar visualization
- Zoom and pan controls
- Search within graph

#### FR-9: Code & Implementation Links
**Priority:** P0 (Critical)
**Status:** ⚠️ Partially Implemented

Each paper should link to:
- GitHub repositories
- Demo websites
- Colab notebooks
- Benchmark results

**Current Implementation:**
- Some papers have code links in metadata

**Gaps:**
- Not systematically extracted
- No validation of links
- No UI for browsing code

### 2.4 Analytics & Insights

#### FR-10: Personal Analytics Dashboard
**Priority:** P1 (High)
**Status:** ❌ Not Implemented

Users can view their personal statistics:
- Papers read per week/month
- Time spent reading
- Topic distribution
- Reading velocity trends
- Most productive reading days

**Acceptance Criteria:**
- Personal dashboard section
- Charts and graphs
- Exportable reports

#### FR-11: Research Trends
**Priority:** P2 (Medium)
**Status:** ⚠️ Partially Implemented

Display trends across the research corpus:
- Topic popularity over time
- Emerging keywords
- Author collaboration networks
- Citation impact metrics

**Current Implementation:**
- Basic statistics page
- Tag cloud

**Gaps:**
- No time-series analysis
- No trend detection
- No collaboration networks

### 2.5 Collaboration

#### FR-12: Shared Reading Lists
**Priority:** P2 (Medium)
**Status:** ❌ Not Implemented

Users can share reading lists with:
- Read-only access
- Collaborative editing
- Comments and discussions
- Version history

**Acceptance Criteria:**
- Share via link
- Permission management
- Activity feed

#### FR-13: Social Features
**Priority:** P3 (Low)
**Status:** ❌ Not Implemented

Social features include:
- Follow authors
- Follow topics
- See what others are reading
- Public profiles

**Acceptance Criteria:**
- User profiles
- Follow/unfollow functionality
- Activity feed

### 2.6 Integration & Export

#### FR-14: Reference Manager Integration
**Priority:** P1 (High)
**Status:** ⚠️ Partially Implemented

Direct integration with:
- Zotero (browser extension)
- Mendeley
- EndNote
- Papers

**Current Implementation:**
- BibTeX export

**Gaps:**
- No direct API integration
- No browser extension
- No automatic sync

#### FR-15: Multiple Export Formats
**Priority:** P2 (Medium)
**Status:** ⚠️ Partially Implemented

Export papers in multiple formats:
- BibTeX (✅ exists)
- RIS
- EndNote XML
- CSV
- JSON
- Markdown summary

**Current Implementation:**
- BibTeX export
- Markdown export

**Gaps:**
- No RIS format
- No CSV export
- No JSON export

### 2.7 Accessibility & Usability

#### FR-16: Mobile Responsiveness
**Priority:** P0 (Critical)
**Status:** ⚠️ Partially Implemented

Full mobile support:
- Responsive layout
- Touch-friendly interactions
- Mobile-optimized navigation
- Offline reading capability

**Current Implementation:**
- Basic responsive CSS

**Gaps:**
- Not fully tested on mobile
- No offline mode
- Touch interactions not optimized

#### FR-17: Accessibility Compliance
**Priority:** P0 (Critical)
**Status:** ⚠️ Partially Implemented

WCAG 2.1 AA compliance:
- Keyboard navigation
- Screen reader support
- Color contrast ratios
- Alt text for images
- ARIA labels

**Current Implementation:**
- Semantic HTML
- Some ARIA labels

**Gaps:**
- No accessibility audit
- Missing keyboard shortcuts
- Inconsistent ARIA labels

#### FR-18: Multi-language Support
**Priority:** P3 (Low)
**Status:** ❌ Not Implemented

Support for multiple languages:
- UI localization
- Paper title/abstract translation
- Language preference

**Acceptance Criteria:**
- Language selector
- Translation API integration
- Localized UI strings

---

## 3. Non-Functional Requirements

### 3.1 Performance

#### NFR-1: Page Load Time
**Target:** < 2 seconds for initial load
**Status:** ✅ Likely met (static site)

#### NFR-2: Search Response Time
**Target:** < 500ms for search results
**Status:** ✅ Likely met (client-side search)

#### NFR-3: Scalability
**Target:** Support 10,000+ papers without degradation
**Status:** ⚠️ Needs testing

**Concerns:**
- Client-side search may slow with large datasets
- Consider server-side search for scale

### 3.2 Security & Privacy

#### NFR-4: Data Privacy
**Target:** No personal data leaves browser
**Status:** ✅ Met (localStorage only)

#### NFR-5: HTTPS
**Target:** All traffic encrypted
**Status:** ⚠️ Currently HTTP only

**Action Required:**
- Enable HTTPS for production deployment

### 3.3 Reliability

#### NFR-6: Uptime
**Target:** 99.9% availability
**Status:** ⚠️ Depends on hosting

#### NFR-7: Data Backup
**Target:** Automated backups of user data
**Status:** ❌ Not implemented

**Action Required:**
- Export/import functionality for user data
- Cloud sync option

### 3.4 Maintainability

#### NFR-8: Code Quality
**Target:** Modular, documented code
**Status:** ⚠️ Mixed

**Concerns:**
- Large monolithic HTML files
- Inline JavaScript
- Limited documentation

### 3.5 SEO & Discoverability

#### NFR-9: Search Engine Optimization
**Target:** High visibility in search engines
**Status:** ⚠️ Partially implemented

**Current:**
- Semantic HTML
- Meta descriptions

**Gaps:**
- No sitemap.xml
- No structured data (JSON-LD)
- Limited social media metadata

---

## 4. Current Feature Audit

### 4.1 Implemented Features ✅

| Feature | Page | Status | Quality |
|---------|------|--------|---------|
| Paper Discovery | search-papers.html | ✅ Complete | Good |
| Topic Browsing | topics/*.html | ✅ Complete | Good |
| Reading List | reading-list.html | ✅ Complete | Good |
| Paper Notes | notes.html | ✅ Complete | Basic |
| Paper Comparison | compare-papers.html | ✅ Complete | Good |
| BibTeX Export | reading-list.html | ✅ Complete | Good |
| Statistics | statistics.html | ✅ Complete | Good |
| Tag Cloud | tag-cloud.html | ✅ Complete | Good |
| Author Profiles | authors.html | ✅ Complete | Good |
| Learning Paths | learning-paths.html | ✅ Complete | Good |
| Glossary | concepts/glossary.html | ✅ Complete | Good |
| Concept Explorer | concept-explorer.html | ✅ Complete | Good |
| Weekly Digests | digests/*.html | ✅ Complete | Good |
| Wiki | wiki.html | ✅ Complete | Good |
| Settings | settings.html | ✅ Complete | Good |
| Admin Dashboard | admin.html | ✅ Complete | Good |
| Dashboard | dashboard.html | ✅ Complete | Good |
| Dark Mode | All pages | ✅ Complete | Good |

### 4.2 Partially Implemented Features ⚠️

| Feature | Current State | Missing Components |
|---------|---------------|-------------------|
| Reading Progress | Status tracking only | Visual progress, time tracking, analytics |
| Annotations | Basic notes field | Highlighting, templates, search |
| Code Links | Some papers have links | Systematic extraction, validation, UI |
| Paper Collections | Single reading list | Multiple lists, sharing, descriptions |
| Research Trends | Basic statistics | Time-series, trend detection |
| Reference Manager | BibTeX export only | Direct API integration |
| Export Formats | BibTeX, Markdown | RIS, CSV, JSON |
| Mobile Support | Basic responsive CSS | Full testing, offline mode |
| Accessibility | Semantic HTML | Audit, keyboard nav, ARIA |

### 4.3 Missing Features ❌

| Feature | Priority | Effort | Impact |
|---------|----------|--------|--------|
| Paper Recommendations | P1 | Medium | High |
| Paper Alerts | P1 | Medium | High |
| Citation Network | P1 | High | High |
| Personal Analytics | P1 | Medium | High |
| Shared Reading Lists | P2 | Medium | Medium |
| Reading Time Estimates | P2 | Low | Medium |
| Social Features | P3 | High | Low |
| Multi-language Support | P3 | High | Low |
| Data Backup | P1 | Low | High |
| HTTPS | P0 | Low | High |

---

## 5. Gap Analysis

### 5.1 Critical Gaps (P0)

1. **HTTPS Support**
   - **Impact:** Security risk, browser warnings
   - **Effort:** Low (configure hosting)
   - **Recommendation:** Implement immediately

2. **Code Repository Links**
   - **Impact:** Users can't find implementations
   - **Effort:** Medium (enhance paper enhancement script)
   - **Recommendation:** High priority for practitioners

3. **Mobile Optimization**
   - **Impact:** Poor mobile experience
   - **Effort:** Medium (testing and fixes)
   - **Recommendation:** Essential for accessibility

4. **Accessibility Audit**
   - **Impact:** Excludes users with disabilities
   - **Effort:** Medium (audit and fixes)
   - **Recommendation:** Legal and ethical requirement

### 5.2 High Priority Gaps (P1)

1. **Paper Recommendations**
   - **Impact:** Users miss relevant papers
   - **Effort:** Medium (algorithm + UI)
   - **Recommendation:** Key differentiator

2. **Citation Network Visualization**
   - **Impact:** Hard to see research connections
   - **Effort:** High (D3.js integration)
   - **Recommendation:** Powerful research tool

3. **Personal Analytics**
   - **Impact:** Users can't track progress
   - **Effort:** Medium (charts + data aggregation)
   - **Recommendation:** Engages users

4. **Paper Alerts**
   - **Impact:** Users miss new papers
   - **Effort:** Medium (notification system)
   - **Recommendation:** Retention feature

5. **Data Backup**
   - **Impact:** Users lose data if browser cleared
   - **Effort:** Low (export/import)
   - **Recommendation:** Essential for trust

### 5.3 Medium Priority Gaps (P2)

1. **Reading Time Estimates**
2. **Multiple Export Formats**
3. **Shared Reading Lists**
4. **Research Trends**
5. **Enhanced Annotations**

### 5.4 Low Priority Gaps (P3)

1. **Social Features**
2. **Multi-language Support**
3. **Advanced Collaboration**

---

## 6. User Journeys

### 6.1 New Researcher Journey

**Scenario:** Graduate student starting AI research

1. **Discovery**
   - Lands on dashboard
   - Sees learning paths
   - Chooses "Beginner Path"

2. **Learning**
   - Reads foundational papers
   - Uses glossary for terms
   - Tracks progress in reading list

3. **Deep Dive**
   - Explores specific topic
   - Uses concept explorer
   - Takes notes on papers

4. **Organization**
   - Creates custom reading list
   - Exports BibTeX for thesis
   - Shares list with advisor

**Current Support:** ✅ Mostly supported
**Gaps:** ❌ No progress visualization, ❌ no sharing

### 6.2 Active Researcher Journey

**Scenario:** PhD student writing literature review

1. **Search**
   - Searches for specific topic
   - Filters by date and author
   - Saves search for alerts

2. **Reading**
   - Adds papers to reading list
   - Tracks reading progress
   - Takes structured notes

3. **Analysis**
   - Views citation network
   - Identifies key papers
   - Finds gaps in literature

4. **Writing**
   - Exports citations
   - Generates summary
   - Integrates with LaTeX

**Current Support:** ⚠️ Partially supported
**Gaps:** ❌ No citation network, ❌ no alerts, ❌ no structured notes

### 6.3 Practitioner Journey

**Scenario:** Engineer looking for RAG implementations

1. **Discovery**
   - Searches for "RAG"
   - Filters for practical papers
   - Looks for code links

2. **Evaluation**
   - Reads TL;DR summaries
   - Checks benchmarks
   - Reviews code quality

3. **Implementation**
   - Downloads code
   - Reads implementation guides
   - Checks production readiness

4. **Application**
   - Adapts code to project
   - Tracks performance
   - Contributes back

**Current Support:** ⚠️ Minimally supported
**Gaps:** ❌ No TL;DR, ❌ no benchmarks, ❌ no implementation guides

---

## 7. Roadmap & Priorities

### Phase 1: Foundation (Q1 2026)
**Focus:** Critical gaps and core UX improvements

**Deliverables:**
1. ✅ HTTPS support
2. ✅ Code repository link extraction
3. ✅ Reading progress visualization
4. ✅ Data backup (export/import)
5. ✅ Accessibility audit and fixes
6. ✅ Mobile optimization

**Success Metrics:**
- 100% HTTPS coverage
- 80% of papers have code links
- 50% reduction in accessibility issues
- Mobile Lighthouse score > 90

### Phase 2: Intelligence (Q2 2026)
**Focus:** Smart features and personalization

**Deliverables:**
1. Paper recommendations engine
2. Citation network visualization
3. Personal analytics dashboard
4. Paper alerts (email/in-app)
5. Reading time estimates
6. Enhanced annotations (highlighting, templates)

**Success Metrics:**
- 30% increase in paper discovery via recommendations
- 1000+ citation network interactions/month
- 50% of users check personal analytics weekly
- 20% of users subscribe to alerts

### Phase 3: Collaboration (Q3 2026)
**Focus:** Social features and sharing

**Deliverables:**
1. Multiple reading lists (collections)
2. Shared reading lists
3. User profiles
4. Activity feed
5. Comments and discussions
6. Follow authors/topics

**Success Metrics:**
- 25% of users create custom collections
- 10% of users share reading lists
- 100+ active user profiles
- 500+ comments/month

### Phase 4: Integration (Q4 2026)
**Focus:** External integrations and advanced features

**Deliverables:**
1. Zotero browser extension
2. Multiple export formats (RIS, CSV, JSON)
3. Research trend analysis
4. Benchmark results integration
5. Implementation summaries
6. API for third-party tools

**Success Metrics:**
- 500+ Zotero extension installs
- 30% of users use multiple export formats
- 10+ third-party integrations
- API usage: 1000+ requests/day

### Phase 5: Scale (2027)
**Focus:** Performance, scale, and advanced features

**Deliverables:**
1. Server-side search (if needed)
2. Multi-language support
3. Advanced collaboration tools
4. Machine learning features
5. Mobile app (iOS/Android)
6. Offline reading mode

**Success Metrics:**
- Support 10,000+ papers
- 5+ language options
- 1000+ mobile app users
- 99.9% uptime

---

## 8. Success Metrics

### 8.1 User Engagement

| Metric | Current | Target (6 months) | Target (12 months) |
|--------|---------|-------------------|-------------------|
| Daily Active Users | ? | 100 | 500 |
| Papers Read/User/Week | ? | 5 | 10 |
| Notes Created/User/Week | ? | 3 | 5 |
| Reading List Size (avg) | ? | 20 | 50 |

### 8.2 Content Quality

| Metric | Current | Target (6 months) | Target (12 months) |
|--------|---------|-------------------|-------------------|
| Papers with Code Links | ~30% | 80% | 95% |
| Papers with TL;DR | 0% | 50% | 90% |
| Citation Network Coverage | 0% | 60% | 90% |

### 8.3 Technical Performance

| Metric | Current | Target |
|--------|---------|--------|
| Page Load Time | < 2s | < 1s |
| Search Response | < 500ms | < 200ms |
| Lighthouse Score | ? | > 90 |
| Accessibility Score | ? | > 95 |

### 8.4 User Satisfaction

| Metric | Target |
|--------|--------|
| Net Promoter Score | > 50 |
| User Satisfaction | > 4.5/5 |
| Feature Request Completion | > 80% |

---

## 9. Technical Debt & Risks

### 9.1 Technical Debt

1. **Monolithic HTML Files**
   - **Issue:** Large files with inline JavaScript
   - **Impact:** Hard to maintain, slow development
   - **Recommendation:** Modularize into components

2. **Client-Side Search**
   - **Issue:** Search runs in browser
   - **Impact:** Won't scale beyond ~5000 papers
   - **Recommendation:** Plan for server-side search

3. **No Testing**
   - **Issue:** No automated tests
   - **Impact:** Regressions, bugs
   - **Recommendation:** Add unit and integration tests

4. **Limited Documentation**
   - **Issue:** Code not well documented
   - **Impact:** Hard for new contributors
   - **Recommendation:** Add JSDoc, README files

### 9.2 Risks

1. **Data Loss**
   - **Risk:** Users lose data if browser cleared
   - **Mitigation:** Implement data backup (Phase 1)

2. **Scalability**
   - **Risk:** Performance degrades with more papers
   - **Mitigation:** Plan for server-side search (Phase 5)

3. **Security**
   - **Risk:** HTTP only, no encryption
   - **Mitigation:** Enable HTTPS (Phase 1)

4. **Dependency on arXiv**
   - **Risk:** arXiv API changes or rate limits
   - **Mitigation:** Add fallback sources, cache aggressively

---

## 10. Conclusion

The AI Research Tracker has a solid foundation with comprehensive paper discovery, reading management, and knowledge building features. However, significant gaps remain in:

1. **Intelligence** (recommendations, alerts, analytics)
2. **Collaboration** (sharing, social features)
3. **Integration** (reference managers, export formats)
4. **Accessibility** (mobile, WCAG compliance)

The proposed 5-phase roadmap addresses these gaps systematically, prioritizing critical security and accessibility issues first, then building intelligence features, followed by collaboration and integration capabilities.

**Key Success Factors:**
- Focus on user needs (researchers, students, practitioners)
- Maintain data privacy (localStorage-first approach)
- Ensure performance and scalability
- Build community through collaboration features

**Next Steps:**
1. Review and prioritize requirements with stakeholders
2. Begin Phase 1 implementation (HTTPS, code links, progress tracking)
3. Establish metrics and monitoring
4. Create feedback loop with users
5. Iterate based on usage data

---

## Appendix A: Glossary

- **P0:** Critical priority - must have
- **P1:** High priority - should have
- **P2:** Medium priority - nice to have
- **P3:** Low priority - future consideration
- **WCAG:** Web Content Accessibility Guidelines
- **RIS:** Research Information Systems (citation format)
- **TL;DR:** Too Long; Didn't Read (summary)

## Appendix B: References

- [Current Website](http://100.64.0.17:8001)
- [AGENTS.md](AGENTS.md) - Project documentation
- [Admin Dashboard](admin.html) - System overview
- [Settings](settings.html) - Configuration options

---

**Document Version:** 1.0  
**Last Updated:** August 31, 2026  
**Author:** System Design Team  
**Status:** Draft for Review
