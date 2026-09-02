# AI Research Tracker — Agent Guide

## Mission

A learner-in-the-loop personal knowledge environment designed to position GenAI as a metacognitive and formative scaffold rather than as a substitute knowledge producer.

### Core Philosophy

The platform addresses a central tension in educational GenAI: the same cognitive activities that AI can efficiently automate—explaining, organising, connecting, and reformulating information—may themselves constitute important processes through which learning occurs.

**Central Design Challenge:** Determine what the learner should continue to do because doing it is part of learning.

### Design Principles

1. **DP1: Learner Ownership** — Learners author and retain control over knowledge artefacts; AI suggestions require explicit evaluation before incorporation
2. **DP2: Scaffold Rather Than Substitute** — AI supports cognitive activity without automatically performing learning-relevant intellectual work on the learner's behalf
3. **DP3: Reflection Before Correction** — Learners inspect and reconsider their reasoning before direct correction is supplied, supporting metacognitive monitoring
4. **DP4: Continuous Knowledge Integration** — New learning relates to previously constructed knowledge, triggering revision of earlier representations

### Five-Stage Knowledge Construction Cycle

1. **Construct** — Learner develops initial explanation or representation in personal wiki
2. **Reflect** — AI generates metacognitive prompts to examine confidence and completeness
3. **Scaffold** — AI provides targeted questions, hints, and connection suggestions
4. **Consolidate & Apply** — Learner retrieves and applies knowledge independently of stored artefacts
5. **Revisit & Extend** — New concepts integrate with prior knowledge, revising earlier entries

### Key Interaction Model: Prompt Before Provide

When learners request information about a concept, the AI Companion first encourages them to articulate their current understanding before receiving direct explanations. This creates productive cognitive friction that supports retrieval and reflection.

### Primary Objectives

1. **Personalised Learning Journey** — Users enter topics to research and build customised learning paths while maintaining epistemic agency
2. **AI Wiki Companion** — Four modes (Write, Review, Coach, Update) that scaffold rather than substitute cognitive activity
3. **Automated Research Retrieval** — Systematically fetches papers while preserving learner agency in knowledge construction
4. **Concept Graph & Knowledge Base** — Persistent, networked knowledge representation that evolves over time
5. **Formative Evaluation** — Tracks conceptual understanding, knowledge-artefact development, and learner responses to AI scaffolding
6. **Behind-the-Scenes Automation** — AI-driven automation handles paper fetching, metadata enhancement, and content curation so users can focus on learning

## Multi-User Topic Management

The system now supports multiple users, each with their own research topics:

### User Management
```bash
# List all users
python3 user_manager.py list

# Create new user
python3 user_manager.py create <username> [display_name]

# Switch active user
python3 user_manager.py switch <username>

# View available templates
python3 user_manager.py templates
```

### Topic Configuration
Each user has their own topic configuration stored in `_data/users/{username}/config.json`:
- **Hierarchical topics**: Parent topics with sub-topics (e.g., AI Agents → GUI Agents)
- **Custom queries**: arXiv search queries per topic
- **Keywords**: For paper classification
- **arXiv categories**: Filter by CS subcategories
- **Templates**: Pre-built topic packages to import

### Web UI
Access the topic management interface at:
```
http://localhost:8000/topics-management.html
```

Features:
- Switch between users
- Add/edit/delete topics
- Import topic templates
- Toggle topics on/off
- Configure search queries and keywords

### API Server
Start the topic management API:
```bash
python3 api_server.py
```

Provides REST endpoints for user/topic CRUD operations.

### Dynamic Topic Pages
Generate personalized topic pages:
```bash
python3 generate_topic_pages.py
```

Creates:
- Topics index page
- One page per enabled topic
- Filters papers by user's topics
- Supports hierarchical display

## Directory Structure

```
research-notes/
├── papers/              # Daily fetched papers (organized by date)
│   └── YYYY-MM-DD/      # Date-organized paper markdown files
├── topics/              # Curated topic pages
│   ├── ai-agents.qmd
│   ├── llm-reasoning.qmd
│   ├── rag-retrieval.qmd
│   └── multi-modal.qmd
├── concepts/            # Concept reference pages
│   ├── glossary.md
│   ├── connections.qmd
│   └── papers-by-concept.md
├── digests/             # Weekly/monthly summaries
├── _includes/           # HTML/CSS/JS includes
│   ├── mermaid.html
│   ├── custom-head.html
│   ├── custom-style.html
│   ├── theme-toggle.html
│   ├── navbar-custom.html
│   └── search-index.js  # Global search index (113 items)
├── _site/               # Quarto rendered output (served by web server)
├── _quarto.yml          # Quarto site configuration
├── index.qmd            # Landing page (hero section + recent papers)
│
├── # Two-Part Navigation Structure
├── dashboard.md         # Main dashboard with two-part selection
├── external-hub.md      # Research Portal: Researcher + Admin (system settings)
├── internal-hub.md      # Internal Part: System Architecture + Engineering
├── researcher-hub.md    # Legacy researcher hub (superseded by external-hub)
├── admin-hub.md         # Legacy admin hub (superseded by external-hub)
├── engineer-hub.md      # Legacy engineer hub (superseded by internal-hub)
│
├── # Wiki & Knowledge Management
├── wiki.md              # Interactive wiki with bidirectional linking
├── wiki-graph.md        # D3.js force-directed knowledge graph
├── global-search.md     # Fuzzy search across all content
├── research-workflow.md # Research lifecycle guide
│
├── # Paper Management
├── search-papers.md     # Full-text search interface
├── compare-papers.md    # Side-by-side paper comparison
├── reading-list.md      # Bookmarking with status tracking & notes
├── tag-cloud.md         # Concept tag cloud visualization
│
├── # Analytics & Reference
├── statistics.md        # Analytics dashboard (generated)
├── notes.md             # Paper notes & reading progress (generated)
├── authors.md           # Author profiles (generated)
├── learning-paths.md    # Structured reading guides
├── must-read-papers.md  # Curated essential papers
├── concept-explorer.qmd # Interactive concept map
├── comparison-tables.md # Architecture comparison tables
├── resources.md         # External resources
├── faq.md               # FAQ page
├── rss.xml              # RSS feed (generated)
│
├── # Admin & Configuration
├── admin.md             # Behind-the-scenes documentation
├── settings.md          # Project configuration page
├── requirements.md      # User requirements document
├── system-architecture.md # Interactive UML diagrams
│
├── # Automation Scripts (15 Python scripts, 3.3KB total)
├── automate.py          # Master pipeline orchestrator
├── fetch_arxiv.py       # arXiv paper fetcher (CS categories)
├── enhance_papers.py    # Paper enhancement (contributions, related)
├── enhance_paper_details.py  # Structured metadata extraction
├── inject_wikilinks.py  # Wiki link injector (23 terms, 75+ files)
├── add_bookmark_buttons.py  # Bookmark button injector
├── generate_search_index.py # Global search index builder (113 items)
├── generate_authors.py  # Author profile generator (346 authors)
├── generate_statistics.py  # Statistics engine
├── generate_rss.py      # RSS feed generator
├── generate_notes.py    # Notes generator
├── generate_tagcloud_data.py  # Tag cloud builder
├── generate_compare_data.py  # Comparison data generator
├── generate_search_data.py  # Legacy search data generator
├── re_enhance_papers.py  # Paper re-enhancement script
│
├── # Shell Scripts
├── daily_automation.sh  # One-click pipeline runner
├── start_server.sh      # Web server launcher
├── stop_server.sh       # Web server stopper
│
├── # Documentation
├── SYSTEM_ARCHITECTURE.md  # Comprehensive system architecture doc
├── OBSIDIAN_ENHANCEMENTS.md  # Obsidian feature roadmap
├── BACKLINKS_IMPLEMENTATION.md  # Backlinks feature guide
├── AUTOMATION.md        # Automation setup guide
├── COMPLETE_AUTOMATION_GUIDE.md  # Full automation documentation
├── DESIGN_GUIDE.md      # Design system reference
├── UI_ENHANCEMENTS.md   # UI/UX improvements guide
├── SHORTCUTS_SETUP.md   # macOS Shortcuts setup
└── AGENTS.md            # This file
```

## System Architecture

### 8-Layer Architecture

1. **Data Ingestion Layer** — `fetch_arxiv.py`, `automate.py`
2. **Data Enhancement Layer** — `enhance_papers.py`, `inject_wikilinks.py`, etc.
3. **Data Generation Layer** — `generate_search_index.py`, `generate_authors.py`, etc.
4. **Wiki & Knowledge Layer** — `wiki.md`, `wiki-graph.md`, `global-search.md`
5. **Search & Discovery Layer** — Fuzzy search, category filters, keyboard shortcuts
6. **User Interface Layer** — Role-based hubs, dashboard, navigation
7. **Static Site Generation Layer** — Quarto, `_quarto.yml`, `_includes/`
8. **Automation & Deployment Layer** — Shell scripts, launchd, Shortcuts

### Data Flow

```
arXiv API → fetch_arxiv.py → papers/*.md → enhance_papers.py
→ inject_wikilinks.py → generate_*.py → quarto render → _site/
→ http.server:8001 → User Browser
```

### Key Metrics

- **77 papers** from arXiv
- **346 authors** indexed
- **119 pages** rendered
- **113 search index items** (77 papers + 14 wiki terms + 4 topics + 2 concepts + 16 pages)
- **34 graph nodes** (4 topics + 18 terms + 12 papers)
- **67 graph connections** (strong/weak links)
- **23 wiki terms** injected across 75+ files
- **Pipeline time:** ~58 seconds

## UI/UX Features

### Two-Part Navigation
- **Dashboard** — Main hub with Research Portal (Researcher/Admin) and Internal Part (Architecture/Engineering)
- **External Hub** — Researcher tools, admin controls, system settings
- **Internal Hub** — System architecture, engineering documentation, code patterns

### External Hub Enhancements
- **Recent Activity Feed** — Dynamic feed showing bookmarks, status changes, notes, wiki contributions
  - Pulls real data from localStorage (bookmarks, paperNotes, wikiContributions)
  - Smart time formatting ("just now", "5 minutes ago", "2 hours ago")
  - Sorted by recency, shows top 5 activities
  - Empty state handling when no activity exists
- **Quick Actions Panel** — 6 one-click shortcuts (Search, Reading List, Wiki, Statistics, Tag Cloud, Weekly Digest)
- **5-Phase Workflow Visualization** — Interactive research lifecycle (Discovery → Screening → Reading → Synthesis → Citation)
- **Real-Time Stats Dashboard** — Live counts from localStorage (Inbox, Reading, Read, Cited)

### System Health Dashboard
- **Real-Time Monitoring** — Pipeline status, performance metrics, scalability headroom
- **Quick Actions** — One-click pipeline execution, site rebuild, paper fetch
- **Activity Log** — Recent automation events with timestamps
- **System Info** — Server status, versions, resource utilization
- **Visual Indicators** — Progress bars, status badges, color-coded metrics

### Role-Based Access (Legacy)
- **Researcher Hub** — Paper discovery, reading management, knowledge building (purple)
- **Admin Hub** — Automation, configuration, monitoring (pink/red)
- **Engineer Hub** — Code implementations, benchmarks, deployment (blue)

### Dark Mode
- Toggle button (🌙/☀️) in top-right corner
- Persists preference to localStorage
- Full theme support across all pages

### Recent Papers Widget
- Displays 5 latest papers on landing page
- Shows title, date, and topic tags
- Quick access to full paper list

### Enhanced Paper Cards
- Gradient accent bar on hover
- Better metadata display
- Smooth transitions and animations

## Obsidian-Style Wiki Features

### Bidirectional Linking (`wiki.md`)
- **Backlinks panel** — Shows related terms, papers, and contributions
- **Connection count badge** — Displays number of connections per term
- **Auto-indexing** — `buildBacklinkIndex()` builds comprehensive backlink map
- **Grouped display** — Organized by type (terms, papers, contributions)
- **Context previews** — Shows excerpts where terms are mentioned
- **Click-to-navigate** — Jump to any related term instantly

### Knowledge Graph (`wiki-graph.md`)
- **D3.js force-directed graph** — 34 nodes, 67 connections
- **Interactive** — Zoom, pan, click-to-focus, drag nodes
- **Filter by type** — Terms, Papers, Topics, or All
- **Search** — Find nodes by name or definition
- **Detail panel** — Node info, connections, navigation
- **Physics toggle** — Enable/disable force simulation
- **Labels toggle** — Show/hide node labels

### WikiLink Syntax (`inject_wikilinks.py`)
- **Auto-injection** — 23 wiki terms across 75+ files
- **Token-based approach** — Preserves HTML structure
- **Clickable spans** — Click any term to jump to wiki
- **Smart skipping** — Avoids code blocks, headers, existing links

### Global Search (`global-search.md`)
- **Fuzzy search** — Relevance scoring algorithm
- **Multi-term search** — All terms must match
- **Category filters** — All, Papers, Wiki, Topics, Concepts, Pages
- **Keyboard shortcut** — Cmd/Ctrl+K to focus from anywhere
- **Real-time results** — 150ms debounce
- **Result highlighting** — Matches highlighted in yellow
- **Context snippets** — Shows relevant text around matches

## Research Workflow Tools

### Reading List with Status Tracking
- **Status workflow**: Inbox → Reading → Read → Cited → Archived
- **Per-paper notes**: Structured annotations for each paper
- **Status dashboard**: Visual stats showing paper counts by status
- **Status filtering**: Filter papers by reading status
- **BibTeX export**: One-click export for Zotero/Mendeley/EndNote
- **Markdown export**: Export with notes for Obsidian/Notion

### Research Workflow Guide (`research-workflow.md`)
Complete 5-phase research lifecycle:
1. **Discovery** — Find papers via topics, search, digests
2. **Screening** — Assess relevance, update status
3. **Deep Reading** — Extract insights, take structured notes
4. **Synthesis** — Connect ideas across papers
5. **Citation** — Export BibTeX, integrate with reference managers

Includes integration guides for Zotero, Obsidian, LaTeX, and daily/weekly workflow recommendations.

## Interactive Wiki

### Knowledge Construction Workflow (`wiki.md`)
The wiki implements the learner-in-the-loop 5-stage knowledge construction cycle:

1. **Construct** ✍️ — Learner writes initial explanation in their own words
2. **Reflect** 🤔 — AI Companion generates metacognitive prompts: "Which part are you least confident about?"
3. **Scaffold** 🏗️ — AI provides targeted questions, hints, and connection suggestions (Prompt Before Provide)
4. **Consolidate & Apply** 💡 — Learner retrieves and applies knowledge independently
5. **Revisit & Extend** 🔗 — New concepts integrate with prior knowledge, revising earlier entries

### AI Companion Functions

| Function | Intended Learning Role | Example |
|----------|----------------------|---------|
| **Socratic Questioning** | Elicit explanation, justification, comparison | "Why does this relationship hold?" |
| **Knowledge Gap Detection** | Draw attention to incomplete concepts | "Your explanation discusses training but not generalisation" |
| **Connection Recommendation** | Encourage integration of new and existing knowledge | "Could this relate to your earlier entry on bias-variance?" |
| **Misconception Challenge** | Prompt reconsideration of inaccurate reasoning | "Would this claim remain true for unseen data?" |
| **Evidence Prompting** | Encourage verification of knowledge claims | "What source supports this statement?" |
| **Retrieval Questions** | Promote recall and transfer | "Explain without consulting the wiki" |

### Wiki Features

- **Learner-authored entries** — AI suggestions require explicit evaluation before incorporation
- **Bidirectional linking** — Backlinks panel with connection count badge
- **Version history** — Track how conceptual representations evolve over time
- **Concept graph** — D3.js force-directed visualization of knowledge relationships
- **Prompt Before Provide** — AI encourages articulation before direct explanation
- **Export/Import** — JSON export for personal knowledge management

## Quick Commands

```bash
cd /Users/ailcshum/workspace/research-notes

# Run full pipeline (fetch → enhance → generate → build)
./daily_automation.sh

# Start/stop web server
./start_server.sh
./stop_server.sh

# Check logs
tail -f automation.log
tail -f server.log

# Rebuild search index
python3 generate_search_index.py

# Inject wiki links
python3 inject_wikilinks.py
```

## Automation Pipeline

1. **Fetch** — `fetch_arxiv.py` pulls papers from arXiv (filtered to CS.AI, CS.CL, CS.IR, CS.LG, CS.MM)
2. **Enhance** — `enhance_papers.py` + `enhance_paper_details.py` add structured metadata
3. **Inject** — `inject_wikilinks.py` adds wiki links to 75+ files
4. **Generate** — `generate_*.py` scripts produce search data, statistics, tag cloud, RSS, authors, notes
5. **Build** — `quarto render` generates the static site to `_site/`

## Automation Setup

- **Web server**: Running at http://100.64.0.17:8001 (started via `start_server.sh`)
- **Daily pipeline**: `./daily_automation.sh` fetches arXiv papers, enhances them, and rebuilds the site
- **macOS Shortcuts**: Create a shortcut running `./daily_automation.sh` for one-click automation
- **Logs**: All automation runs logged to `automation.log`

## Web Server

- **URL**: http://100.64.0.17:8001
- **Bind**: Tailscale IP (not localhost)
- **Managed by**: `start_server.sh` / `stop_server.sh`

## Research Standards

- Prioritize papers from top venues (NeurIPS, ICML, ICLR, ACL, EMNLP)
- Include code links when available
- Extract key contributions, not just abstracts
- Cross-reference related work
- Flag reproducibility concerns

## Conventions

- Python scripts use `python3` (macOS, M3 Ultra Mac Studio)
- Quarto `.qmd` for files with Mermaid diagrams; `.md` for plain content
- HTML in `.md`/`.qmd` files must NOT be indented (4+ spaces = code block in Quarto)
- User data (notes, bookmarks, progress) stored in browser localStorage
- All generated pages use `generate_*.py` scripts — never edit generated HTML directly
- Wiki terms use `data-term` attribute for linking
- Search index stored in `_includes/search-index.js` for client-side access

## Success Criteria

- **Learner Agency**: Learners remain the primary constructors of knowledge; AI scaffolds without substituting cognitive activity
- **Metacognitive Engagement**: Learners actively monitor, evaluate, and revise their understanding with AI-supported prompts
- **Knowledge Evolution**: Wiki entries show substantive revision over time as understanding deepens
- **Research Automation**: Zero-touch daily paper updates with one-click manual override
- **Knowledge Accessibility**: Searchable, browsable research database with visual analytics
- **Knowledge Graph**: Obsidian-style wiki with bidirectional linking and interactive visualization
- **Documentation Quality**: Self-documenting workflows with comprehensive logs and guides

## Conference Paper

**"From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction"**
- Location: `public/conference-papers/ai-wiki-companion-2026.md`
- Status: Draft (To Be Submitted)
- Date: September 2, 2026
- Keywords: learner-in-the-loop, AI wiki, knowledge construction, writing-to-learn, metacognition, self-regulated learning, cognitive offloading, epistemic agency
- **Core Contribution**: Design framework for educational GenAI that positions AI as metacognitive scaffold rather than substitute knowledge producer
- **Research Questions**: 
  - RQ1: How to design learner-in-the-loop AI wiki supporting knowledge construction while maintaining learner agency?
  - RQ2: To what extent does the AI Wiki Companion support students' knowledge construction and conceptual understanding?
  - RQ3: How do learners evaluate and act upon AI-generated scaffolding during knowledge artefact construction?
  - RQ4: How do students perceive the usefulness of AI-supported reflection, feedback, and knowledge linking?
- **Theoretical Foundation**: Writing-to-learn, metacognition, self-regulated learning, personal knowledge management, human-in-the-loop AI
- **Design Principles**: DP1 Learner Ownership, DP2 Scaffold Rather Than Substitute, DP3 Reflection Before Correction, DP4 Continuous Knowledge Integration
- **Five-Stage Cycle**: Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend
- **Interaction Model**: Prompt Before Provide
- **Evaluation Framework**: Mixed-method formative study examining conceptual understanding, knowledge artefact quality, learner response to AI scaffolding, and perceived usefulness

## Current Stats (Sep 2, 2026)

- **133 papers** tracked from arXiv (47 daily batches)
- **851 authors** indexed
- **123 pages** rendered
- **119 search index items** (77 papers + 27 wiki terms + 4 topics + 2 concepts + 16 pages)
- **34 graph nodes** (4 topics + 18 terms + 12 papers)
- **67 graph connections**
- **23 wiki terms** injected across 75+ files
- **4 focus areas**: AI Agents, LLM Reasoning, RAG, Multi-Modal
- **2 main sections**: Research Portal (Researcher/Admin), Internal Part (Architecture/Engineering)
- **Live at**: http://100.64.0.17:8001

## Recent Enhancements (Sep 2, 2026)

### UI/UX Learning Workflow - All 5 Phases Complete ✅

**Phase 1: Navigation Restructure**
- Updated `_quarto.yml` with learning-centric navigation
- Tested all links work
- Updated landing page

**Phase 2: Learning Journey Page**
- Created `learning-journey.md` with 5-stage visual path
- Added progress tracking and stage completion indicators
- Implemented color-coded stage navigation

**Phase 3: Wiki as Learning Entry Point**
- Added "Start Learning" hero section with progress stats
- Enhanced AI Companion visibility (4 modes: Write/Review/Coach/Update)
- Added learning progress indicators (terms explored, explanations written, mastery levels)
- Implemented "Continue Learning" feature

**Phase 4: Progress Dashboard**
- Enhanced dashboard with 6 learning metrics cards
- Added 5-stage completion visualization with progress bars
- Implemented 28-day learning streak counter with heatmap
- Added achievement badge system (8 unlockable achievements)

**Phase 5: Stage Transition Navigation**
- Created `js/stage-navigation.js` component
- Added breadcrumbs showing current learning stage
- Implemented "Next Step" buttons guiding to next stage
- Added contextual tool recommendations
- Integrated into 6 key pages (wiki, highlights, ai-wiki, spaced-repetition, takeaways, questions)

### System Maintenance
- Rebuilt search index: 119 items (up from 5)
- Updated statistics dashboard: 133 papers
- Generated authors page: 851 authors
- Updated tag cloud: 77 papers indexed

### Conference Paper Alignment
- Updated `AGENTS.md` with full paper details
- Added research questions (RQ1-RQ4)
- Documented design principles and 5-stage cycle
- Linked implementation status to paper framework
- **Total Pages**: 124 (up from 123)
