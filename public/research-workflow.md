---
title: "Research Workflow Guide"
---

# Research Workflow Guide

This guide explains how to use the AI Research Tracker effectively throughout your research process, from discovery to citation.

## The Research Lifecycle

### 1. Discovery Phase 📥

**Goal:** Find relevant papers for your research

**How to use:**
- Browse papers by topic (AI Agents, LLM Reasoning, RAG, Multi-Modal)
- Use the [Search Papers](search-papers.md) page with keywords
- Check [Weekly Digests](digests/index.md) for latest updates
- Explore [Tag Cloud](tag-cloud.md) for trending concepts

**Action:** Bookmark interesting papers → they appear in your [Reading List](reading-list.md) with "Inbox" status

---

### 2. Screening Phase 📖

**Goal:** Quickly assess paper relevance

**How to use:**
- Open your [Reading List](reading-list.md)
- Filter by "Inbox" status to see unreviewed papers
- Read abstracts and check topics
- Update status to "Reading" for papers worth deeper review

**Tip:** Use the status dropdown on each paper to track progress:
- 📥 **Inbox** → Newly bookmarked, not yet reviewed
- 📖 **Reading** → Currently reviewing
- ✅ **Read** → Completed reading
- 📝 **Cited** → Used in your research
- 🗄️ **Archived** → No longer active

---

### 3. Deep Reading Phase 📚

**Goal:** Extract key insights and methodology

**How to use:**
- Filter your Reading List by "Reading" status
- For each paper, use the notes section to capture:
  - **Key contributions** - What's novel?
  - **Methodology** - How did they do it?
  - **Results** - What did they find?
  - **Limitations** - What are the gaps?
  - **Questions** - What do you want to explore?

**Best practices:**
- Take notes while reading (don't rely on memory)
- Highlight connections to other papers
- Note potential applications to your work
- Mark papers for follow-up reading

---

### 4. Synthesis Phase 🧠

**Goal:** Connect ideas across papers

**How to use:**
- Review notes from multiple papers in your Reading List
- Use [Concept Explorer](concept-explorer.qmd) to visualize relationships
- Check [How Concepts Connect](concepts/connections.qmd) for cross-topic links
- Compare papers using [Compare Papers](compare-papers.md)

**Synthesis questions:**
- What patterns emerge across papers?
- Which methods appear repeatedly?
- Where are the research gaps?
- How do different approaches compare?

---

### 5. Citation Phase 📝

**Goal:** Organize references for writing

**How to use:**
- Update paper status to "Cited" when you reference them
- Export your Reading List as BibTeX:
  - Click "Export BibTeX" in your Reading List
  - Import the .bib file into Zotero, Mendeley, or EndNote
  - Citations include all metadata (authors, title, arXiv ID, etc.)

**Alternative exports:**
- **Markdown** → Includes your notes, status, and full paper details
- Perfect for literature review documents
- Can be imported into Obsidian, Notion, or other note-taking apps

---

## Workflow Tips

### Daily Workflow
1. Check [Weekly Digests](digests/index.md) for new papers
2. Bookmark relevant papers (auto-added to Reading List as "Inbox")
3. Review Inbox papers → update status to "Reading" or skip
4. Take notes on papers you're actively reading
5. Export BibTeX when ready to cite

### Weekly Review
1. Review all papers in "Reading" status
2. Update status to "Read" or "Cited" as appropriate
3. Archive papers that are no longer relevant
4. Export your Reading List as backup
5. Check [Statistics](statistics.md) to see your reading patterns

### Literature Review Process
1. Start with [Learning Paths](learning-paths.md) for foundational papers
2. Use [Must-Read Papers](must-read-papers.md) as a starting point
3. Expand using "Related Papers" sections on each paper page
4. Track your progress with status updates
5. Export to BibTeX when writing your paper

---

## Integration with External Tools

### Zotero / Mendeley / EndNote
1. Bookmark papers in the AI Research Tracker
2. When ready to cite, export as BibTeX
3. Import .bib file into your reference manager
4. Use reference manager for in-document citations

### Obsidian / Notion
1. Export Reading List as Markdown
2. Includes your notes and paper metadata
3. Import into your note-taking system
4. Link to related notes and concepts

### LaTeX / Overleaf
1. Export as BibTeX
2. Add .bib file to your LaTeX project
3. Use \cite{arxiv_id} in your document
4. Bibliography auto-generated from your Reading List

---

## Keyboard Shortcuts (Coming Soon)

We're working on keyboard shortcuts for power users:
- `b` → Bookmark current paper
- `n` → Add note to current paper
- `s` → Cycle through status (Inbox → Reading → Read → Cited)
- `e` → Export Reading List

---

## Getting Help

- [FAQ](faq.md) - Common questions and answers
- [Glossary](concepts/glossary.md) - Research terminology
- [External Resources](resources.md) - Additional tools and guides

---

**Pro Tip:** The Reading List stores everything in your browser's localStorage. Clear your browser data = lose your list. Export regularly as backup!
