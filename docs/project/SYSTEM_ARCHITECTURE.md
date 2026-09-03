# System Architecture Documentation

## Overview

The AI Research Tracker is a personalised learning platform powered by AI assistance, built as a static site generation system. It automates the retrieval of research papers and other sources, analyses and builds learning materials, and presents them in an interactive, structured learning pathway. Built on Quarto, it uses Python scripts for data processing and JavaScript for interactive features.

## System Components

### 1. Data Ingestion Layer

**Purpose:** Fetch and process research papers from external sources

#### Components:
- **fetch_arxiv.py** (8.9KB)
  - Queries arXiv API for papers in 4 focus areas
  - Filters by CS categories (cs.AI, cs.CL, cs.CV, cs.LG, cs.MA, cs.IR, cs.SE)
  - Downloads papers from past 7 days
  - Saves as markdown files with metadata
  
- **automate.py** (6.9KB)
  - Master orchestration script
  - Runs complete pipeline: fetch → enhance → generate → build
  - Maintains state in `.automation_state.json`
  - Logs all operations to `automation.log`

### 2. Data Enhancement Layer

**Purpose:** Enrich paper metadata and create cross-references

#### Components:
- **enhance_papers.py** (5.4KB)
  - Extracts key contributions from abstracts
  - Finds related papers based on shared topics
  - Adds structured summaries to paper pages
  
- **enhance_paper_details.py** (7.1KB)
  - Adds Key Findings, Methodology, Limitations
  - Generates citation formats (APA, MLA, BibTeX)
  - Estimates reading time
  
- **inject_wikilinks.py** (5.2KB)
  - Scans all markdown files for wiki terms
  - Injects clickable `<span class="wiki-term">` elements
  - Uses token-based approach to preserve HTML structure
  - Processes 23 wiki terms across 75+ files
  
- **add_bookmark_buttons.py** (3.9KB)
  - Injects bookmark buttons into paper pages
  - Enables reading list functionality

### 3. Data Generation Layer

**Purpose:** Generate dynamic data for interactive features

#### Components:
- **generate_search_index.py** (11KB)
  - Builds comprehensive search index (113 items)
  - Indexes: 77 papers, 14 wiki terms, 4 topics, 2 concepts, 16 pages
  - Outputs: `search-index.json` and `_includes/search-index.js`
  - Extracts keywords, titles, abstracts, metadata
  
- **generate_authors.py** (7.8KB)
  - Creates author profiles from paper metadata
  - Generates 346 author pages
  - Links papers to authors
  
- **generate_statistics.py** (13KB)
  - Computes paper statistics by topic, date, author
  - Generates chart data for visualizations
  
- **generate_tagcloud_data.py** (1.3KB)
  - Injects paper data into tag-cloud.md
  - Enables concept tag visualization
  
- **generate_notes.py** (13KB)
  - Creates reading notes pages for each paper
  - Tracks reading progress
  
- **generate_compare_data.py** (1.3KB)
  - Generates comparison data for papers
  - Enables side-by-side analysis
  
- **generate_rss.py** (4.8KB)
  - Creates RSS feed with 77 papers
  - Includes titles, links, descriptions, topics, authors

### 4. Wiki & Knowledge Management Layer

**Purpose:** Provide Obsidian-style knowledge management

#### Components:
- **wiki.md** (32KB)
  - Interactive wiki with 14 terms
  - Bidirectional linking via `buildBacklinkIndex()`
  - Backlinks panel showing related terms, papers, contributions
  - Version history tracking
  - Export/Import functionality (JSON)
  - Persistent storage in localStorage
  
- **wiki-graph.md** (30KB)
  - D3.js force-directed graph visualization
  - 34 nodes: 4 topics, 18 terms, 12 papers
  - 67 connections (strong/weak links)
  - Interactive: zoom, pan, click-to-focus
  - Filter by node type (term, paper, topic)
  - Search functionality

### 5. Search & Discovery Layer

**Purpose:** Enable comprehensive content discovery

#### Components:
- **global-search.md** (17KB)
  - Fuzzy search algorithm with relevance scoring
  - Multi-term search (all terms must match)
  - Category filters (All, Papers, Wiki, Topics, Concepts, Pages)
  - Keyboard shortcut: Cmd/Ctrl+K
  - Real-time results with 150ms debounce
  - Result highlighting and context snippets
  
- **search-papers.md**
  - Paper-specific search with topic filtering
  - Full-text search across titles, abstracts, keywords

### 6. User Interface Layer

**Purpose:** Provide role-based navigation and interaction

#### Components:
- **dashboard.md**
  - Main navigation hub with 8 sections
  - Role selection interface
  - Quick stats and actions
  
- **researcher-hub.md** (596 lines)
  - Purple gradient theme (#667eea → #764ba2)
  - Paper discovery, reading management, knowledge building
  - Learning paths and must-read papers
  
- **admin-hub.md** (558 lines)
  - Pink/Red gradient theme (#f093fb → #f5576c)
  - Automation pipeline, configuration, monitoring
  - Server management and maintenance
  
- **engineer-hub.md** (638 lines)
  - Blue gradient theme (#4facfe → #00f2fe)
  - Code implementations, benchmarks, getting started guides
  - Architecture patterns and deployment

### 7. Static Site Generation Layer

**Purpose:** Build and serve the website

#### Components:
- **_quarto.yml** (123 lines)
  - Quarto configuration
  - Navigation structure (navbar + sidebar)
  - Theme: cosmo with custom CSS
  - Includes: mermaid.html, custom-head.html, custom-style.html, theme-toggle.html
  
- **_includes/**
  - `mermaid.html` - Mermaid diagram initialization
  - `custom-head.html` - Google Fonts and meta tags
  - `custom-style.html` - 341 lines of custom CSS
  - `theme-toggle.html` - Dark mode toggle
  - `navbar-custom.html` - Custom navigation bar
  - `search-index.js` - Search index for global search

### 8. Automation & Deployment Layer

**Purpose:** Schedule and run automation tasks

#### Components:
- **daily_automation.sh**
  - Master pipeline script
  - Runs: fetch → enhance → generate → build
  
- **start_server.sh** / **stop_server.sh**
  - Web server management
  - PID tracking for clean shutdown
  
- **setup_complete_automation.sh**
  - Installs launchd plists
  - Configures daily paper updates
  - Sets up web server

## Data Flow

```
┌─────────────────┐
│   arXiv API     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ fetch_arxiv.py  │  Fetch papers (past 7 days)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ papers/*.md     │  Raw paper files
└────────┬────────┘
         │
         ├─────────────────────────────────┐
         │                                 │
         ▼                                 ▼
┌─────────────────┐              ┌─────────────────┐
│ enhance_*.py    │              │ inject_*.py     │
│ - contributions │              │ - wiki links    │
│ - related papers│              │ - bookmarks     │
│ - citations     │              └────────┬────────┘
└────────┬────────┘                       │
         │                                │
         └────────────────┬───────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ generate_*.py         │
              │ - search index        │
              │ - author profiles     │
              │ - statistics          │
              │ - RSS feed            │
              └───────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ quarto render         │
              │ - 119 pages           │
              │ - HTML + CSS + JS     │
              └───────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ _site/                │
              │ - Static HTML files   │
              │ - search-index.js     │
              │ - RSS feed            │
              └───────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ python3 http.server   │
              │ - Port 8001           │
              │ - Tailscale IP        │
              └───────────────────────┘
```

## Storage Architecture

### File System Structure
```
research-notes/
├── papers/
│   └── YYYY-MM-DD/
│       └── arxiv-id-title.md
├── topics/
│   ├── ai-agents.qmd
│   ├── llm-reasoning.qmd
│   ├── rag-retrieval.qmd
│   └── multi-modal.qmd
├── concepts/
│   ├── glossary.md
│   ├── connections.qmd
│   └── papers-by-concept.md
├── digests/
│   ├── index.md
│   └── week-YYYY-WW.md
├── _includes/
│   ├── mermaid.html
│   ├── custom-head.html
│   ├── custom-style.html
│   ├── theme-toggle.html
│   ├── navbar-custom.html
│   └── search-index.js
├── _site/              # Generated output
├── *.py                # 15 Python scripts (3.3KB total)
├── *.md / *.qmd        # Content pages
├── _quarto.yml         # Site configuration
├── search-index.json   # Search index data
└── .automation_state.json  # Pipeline state
```

### Client-Side Storage (localStorage)
- **wikiContributions** - User wiki edits and questions
- **termVersions** - Version history for wiki terms
- **bookmarks** - Reading list entries
- **notes** - Per-paper notes
- **readingProgress** - Reading progress tracking
- **settings** - User preferences
- **theme** - Dark/light mode preference

## Technology Stack

### Backend (Build Time)
- **Python 3.9.6** - Data processing scripts
- **Quarto** - Static site generator
- **arXiv API** - Paper source
- **D3.js v7** - Graph visualization (CDN)
- **Mermaid v10** - Diagram rendering (CDN)

### Frontend (Runtime)
- **HTML5** - Structure
- **CSS3** - Styling (custom + cosmo theme)
- **Vanilla JavaScript** - Interactivity
- **localStorage** - Client-side persistence
- **D3.js** - Force-directed graphs
- **Mermaid** - Diagram rendering

### Infrastructure
- **Python HTTP Server** - Development server
- **Tailscale** - Network access (100.64.0.17:8001)
- **macOS launchd** - Automation scheduling (planned)
- **macOS Shortcuts** - Recommended automation method

## Key Design Patterns

### 1. Pipeline Pattern
Sequential processing stages with clear inputs/outputs:
```
fetch → enhance → generate → build → serve
```

### 2. Static Site Generation
- Content stored as markdown
- Build-time processing
- Zero server-side runtime logic
- Fast page loads, CDN-friendly

### 3. Progressive Enhancement
- Base content works without JavaScript
- Interactive features layered on top
- Graceful degradation for older browsers

### 4. Role-Based Navigation
- Three user personas: Researcher, Admin, Engineer
- Dedicated hub pages for each role
- Contextual features and workflows

### 5. Knowledge Graph Pattern
- Wiki terms as nodes
- Papers, topics, concepts as connected entities
- Bidirectional linking
- Graph visualization for exploration

## Performance Characteristics

### Build Time
- **Paper fetch:** ~30 seconds (34 papers)
- **Enhancement:** ~15 seconds (77 papers)
- **Data generation:** ~10 seconds
- **Quarto render:** ~3 seconds (119 pages)
- **Total pipeline:** ~58 seconds

### Runtime Performance
- **Page load:** <100ms (static HTML)
- **Search:** <50ms (fuzzy matching 113 items)
- **Graph render:** ~100ms (34 nodes, 67 links)
- **Wiki backlinks:** ~50ms (index build)

### Scalability
- **Current:** 77 papers, 346 authors, 119 pages
- **Limits:** 
  - Search index: ~1000 items (before performance degradation)
  - Graph: ~200 nodes (D3.js force simulation)
  - Wiki: ~100 terms (localStorage size)

## Security Considerations

### Current State
- **No authentication** - Public access
- **No HTTPS** - HTTP only (Tailscale provides encryption)
- **Client-side storage** - No server-side data
- **No user accounts** - Anonymous usage

### Recommendations
1. Add HTTPS via reverse proxy (nginx/caddy)
2. Implement basic auth for admin features
3. Add rate limiting for API endpoints
4. Sanitize user inputs in wiki contributions
5. Implement CSP headers

## Maintenance & Operations

### Daily Tasks
- Run `daily_automation.sh` to fetch new papers
- Monitor `automation.log` for errors
- Check server health at http://100.64.0.17:8001

### Weekly Tasks
- Review new papers in reading list
- Update wiki with new terms
- Generate weekly digest

### Monthly Tasks
- Backup `research-notes/` directory
- Review and clean up old papers
- Update focus areas in `fetch_arxiv.py`
- Analyze usage statistics

## Future Enhancements

### Phase 5: Advanced Features
- [ ] Real-time collaboration on wiki
- [ ] AI-powered paper summarization
- [ ] Citation network visualization
- [ ] Paper recommendation engine
- [ ] Mobile app with offline support

### Phase 6: Integration
- [ ] Zotero/Mendeley integration
- [ ] Google Scholar alerts
- [ ] Twitter/X research feed
- [ ] Slack/Discord notifications
- [ ] Email digest subscription

### Phase 7: Analytics
- [ ] Page view tracking
- [ ] Search analytics
- [ ] User behavior analysis
- [ ] A/B testing framework
- [ ] Performance monitoring

## Conclusion

The AI Research Tracker is a well-architected personalised learning platform that balances AI-powered automation with interactive learning experiences. The modular design allows for easy extension, while the role-based navigation provides tailored experiences for different user types. The AI-enhanced wiki features enable collaborative knowledge building, and the comprehensive search system ensures content discoverability. The platform systematically retrieves research materials, builds structured learning pathways, and helps users organise their notes — all while AI automation handles the heavy lifting behind the scenes.

The system is production-ready for individual or small team use, with clear paths for scaling and enhancement.
