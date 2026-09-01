# AI Research Tracker — Agent Guide

## Mission

A personalised learning platform powered by AI assistance, helping users create their own learning journey.

### Primary Objectives

1. **Personalised Learning Journey** — Users enter topics to research and save them to build a customised learning path tailored to their interests
2. **Structured Learning Pathway** — Offers a clear, organised progression through topics from foundational concepts to advanced material
3. **AI-Powered Note Organisation** — Utilises AI tools to aid learning and help users organise, summarise, and connect their notes
4. **Automated Research Retrieval** — Systematically retrieves and includes research papers and other sources on a periodic basis
5. **AI-Built Learning Materials** — Analyses retrieved content and builds structured learning materials, summaries, and study aids
6. **Enhanced Wiki with AI Features** — AI-powered wiki support for knowledge building, concept linking, and interactive exploration
7. **Behind-the-Scenes Automation** — AI-driven automation handles paper fetching, metadata enhancement, and content curation so users can focus on learning

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

### Knowledge Building Workflow (`wiki.md`)
5-step interactive process for exploring and contributing to the wiki:

1. **Select** 👆 — Click any highlighted term to explore
2. **Question** ❓ — Ask what you want to know
3. **Search** 🔍 — Find reliable academic sources
4. **Explain** 💡 — Build explanations with examples and citations
5. **Review** ✅ — Review and approve contributions

Features:
- Interactive term highlighting with hover effects
- Visual workflow guide with gradient background
- Source search with citation tracking
- Explanation tools (simplify, add examples, add citations)
- Review and approval workflow
- Recent contributions feed
- Bidirectional linking with backlinks panel
- Version history tracking
- Export/Import (JSON)

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

- **Research Automation**: Zero-touch daily paper updates with one-click manual override
- **Knowledge Accessibility**: Searchable, browsable research database with visual analytics
- **Knowledge Graph**: Obsidian-style wiki with bidirectional linking and interactive visualization
- **Role-Based UX**: Tailored experiences for researchers, admins, and engineers
- **Documentation Quality**: Self-documenting workflows with comprehensive logs and guides

## Current Stats (Sep 1, 2026)

- **77 papers** tracked from arXiv
- **346 authors** indexed
- **123 pages** rendered (up from 119)
- **113 search index items** (77 papers + 14 wiki terms + 4 topics + 2 concepts + 16 pages)
- **34 graph nodes** (4 topics + 18 terms + 12 papers)
- **67 graph connections**
- **23 wiki terms** injected across 75+ files
- **4 focus areas**: AI Agents, LLM Reasoning, RAG, Multi-Modal
- **2 main sections**: Research Portal (Researcher/Admin), Internal Part (Architecture/Engineering)
- **Live at**: http://100.64.0.17:8001

## Recent Enhancements (Sep 1, 2026)

### Navigation Reorganization ✅
- **Two-Part Structure**: Research Portal (Researcher/Admin) + Internal Part (Architecture/Engineering)
- **Dashboard**: Unified hub with External + Internal selection cards
- **External Hub**: Consolidated Researcher and Admin tools with clear sections
- **Internal Hub**: System architecture documentation with interactive UML diagrams
- **Link Verification**: All 36 internal links confirmed accessible (HTTP 200)

### Phase 1: Bidirectional Linking ✅
- Backlinks panel with connection count badge
- Auto-indexing of term relationships
- Grouped display (terms, papers, contributions)
- Context previews and click-to-navigate

### Phase 2: Interactive Knowledge Graph ✅
- D3.js force-directed graph (34 nodes, 67 links)
- Zoom, pan, click-to-focus, drag
- Filter by type (term, paper, topic)
- Search and detail panel

### Phase 3: WikiLink Syntax ✅
- Auto-injection of 23 wiki terms
- Token-based approach (preserves HTML)
- Clickable spans across 75+ files

### Phase 4: Global Search ✅
- Fuzzy search with relevance scoring
- Multi-term search with category filters
- Cmd/Ctrl+K keyboard shortcut
- 113 items indexed (papers, wiki, topics, concepts, pages)

### System Architecture Documentation ✅
- Comprehensive `SYSTEM_ARCHITECTURE.md` (14KB)
- Interactive UML diagrams (`system-architecture.md`)
  - Component diagram
  - Sequence diagram (automation pipeline)
  - Class diagram (Python modules)
  - Data flow diagram
  - Deployment diagram

### UI/UX Refinement (Sep 1, 2026) ✅
- **External Hub**: Interactive 5-phase workflow visualization (Discovery → Screening → Reading → Synthesis → Citation)
- **Internal Hub**: 8-layer architecture diagram, component relationships, data flow pipeline, tech stack visualization
- **Dashboard**: Enhanced with feature highlights and quick stats
- **UI Refinement Summary**: Comprehensive documentation of all refinements
- **Total Pages**: 124 (up from 123)
