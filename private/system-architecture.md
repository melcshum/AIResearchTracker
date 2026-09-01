---
title: "System Architecture"
---

<div class="arch-container">
<div class="arch-header">
<h2>🏗️ System Architecture</h2>
<p class="arch-subtitle">Interactive UML diagrams showing system design, components, and data flow</p>
<div class="arch-tabs">
<button class="arch-tab active" data-tab="component" onclick="switchTab('component')">📦 Component</button>
<button class="arch-tab" data-tab="sequence" onclick="switchTab('sequence')">🔄 Sequence</button>
<button class="arch-tab" data-tab="class" onclick="switchTab('class')">📐 Class</button>
<button class="arch-tab" data-tab="dataflow" onclick="switchTab('dataflow')">🌊 Data Flow</button>
<button class="arch-tab" data-tab="deployment" onclick="switchTab('deployment')">🚀 Deployment</button>
</div>
</div>

<div id="component-diagram" class="arch-panel active">
<h3>Component Diagram</h3>
<p class="diagram-desc">Shows the high-level system components and their relationships</p>
<div class="mermaid-diagram">
```mermaid
graph TB
    subgraph External["External Sources"]
        ARXIV["arXiv API"]
        USER["User Browser"]
    end

    subgraph Ingestion["Data Ingestion Layer"]
        FETCH["fetch_arxiv.py<br/><i>Paper Fetcher</i>"]
        AUTO["automate.py<br/><i>Pipeline Orchestrator</i>"]
    end

    subgraph Enhancement["Data Enhancement Layer"]
        ENHANCE["enhance_papers.py<br/><i>Contribution Extractor</i>"]
        DETAIL["enhance_paper_details.py<br/><i>Metadata Enricher</i>"]
        WIKILINK["inject_wikilinks.py<br/><i>Wiki Link Injector</i>"]
        BOOKMARK["add_bookmark_buttons.py<br/><i>Bookmark Injector</i>"]
    end

    subgraph Generation["Data Generation Layer"]
        SEARCH_IDX["generate_search_index.py<br/><i>Search Index Builder</i>"]
        AUTHORS["generate_authors.py<br/><i>Author Profiler</i>"]
        STATS["generate_statistics.py<br/><i>Statistics Engine</i>"]
        RSS["generate_rss.py<br/><i>RSS Generator</i>"]
        NOTES["generate_notes.py<br/><i>Notes Generator</i>"]
        TAGCLOUD["generate_tagcloud_data.py<br/><i>Tag Cloud Builder</i>"]
    end

    subgraph Wiki["Wiki & Knowledge Layer"]
        WIKI["wiki.md<br/><i>Interactive Wiki</i>"]
        GRAPH["wiki-graph.md<br/><i>Knowledge Graph</i>"]
        GSEARCH["global-search.md<br/><i>Fuzzy Search</i>"]
    end

    subgraph UI["User Interface Layer"]
        DASH["dashboard.md<br/><i>Navigation Hub</i>"]
        RHUB["researcher-hub.md<br/><i>Researcher Portal</i>"]
        AHUB["admin-hub.md<br/><i>Admin Portal</i>"]
        EHUB["engineer-hub.md<br/><i>Engineer Portal</i>"]
    end

    subgraph Build["Build & Deploy Layer"]
        QUARTO["_quarto.yml<br/><i>Site Configuration</i>"]
        RENDER["quarto render<br/><i>Static Site Generator</i>"]
        SERVER["http.server<br/><i>Web Server :8001</i>"]
    end

    subgraph Storage["Storage"]
        PAPERS["papers/*.md<br/><i>77 Papers</i>"]
        TOPICS["topics/*.qmd<br/><i>4 Topics</i>"]
        INCLUDES["_includes/<br/><i>Templates & Assets</i>"]
        SITE["_site/<br/><i>Generated HTML</i>"]
        LS["localStorage<br/><i>Client State</i>"]
    end

    ARXIV -->|"XML/Atom"| FETCH
    FETCH -->|"Markdown"| PAPERS
    AUTO -->|"orchestrates"| FETCH
    AUTO -->|"orchestrates"| ENHANCE
    AUTO -->|"orchestrates"| RENDER

    PAPERS --> ENHANCE
    PAPERS --> DETAIL
    PAPERS --> WIKILINK
    PAPERS --> BOOKMARK
    PAPERS --> AUTHORS
    PAPERS --> STATS
    PAPERS --> SEARCH_IDX

    ENHANCE -->|"Enhanced MD"| PAPERS
    DETAIL -->|"Citations"| PAPERS
    WIKILINK -->|"Wiki Spans"| PAPERS
    BOOKMARK -->|"Buttons"| PAPERS

    SEARCH_IDX -->|"search-index.js"| INCLUDES
    AUTHORS -->|"Author Pages"| SITE
    STATS -->|"Chart Data"| SITE
    RSS -->|"rss.xml"| SITE

    WIKI -->|"Backlinks"| LS
    GRAPH -->|"D3.js Viz"| SITE
    GSEARCH -->|"Fuzzy Search"| INCLUDES

    DASH --> RHUB
    DASH --> AHUB
    DASH --> EHUB

    PAPERS --> RENDER
    TOPICS --> RENDER
    INCLUDES --> RENDER
    RENDER -->|"119 HTML pages"| SITE
    QUARTO -->|"config"| RENDER
    SITE --> SERVER
    SERVER -->|"HTTP"| USER
```
</div>
</div>

<div id="sequence-diagram" class="arch-panel">
<h3>Sequence Diagram — Automation Pipeline</h3>
<p class="diagram-desc">Shows the step-by-step execution flow of the daily automation pipeline</p>
<div class="mermaid-diagram">
```mermaid
sequenceDiagram
    participant Cron as Cron/Scheduler
    participant Auto as automate.py
    participant Fetch as fetch_arxiv.py
    participant ArXiv as arXiv API
    participant Enhance as enhance_papers.py
    participant Wiki as inject_wikilinks.py
    participant Gen as generate_*.py
    participant Quarto as quarto render
    participant Server as http.server
    participant User as User Browser

    Cron->>Auto: Trigger daily run
    Auto->>Auto: Load state (.automation_state.json)
    
    rect rgb(230, 240, 255)
        Note over Auto,ArXiv: Phase 1: Fetch Papers
        Auto->>Fetch: python3 fetch_arxiv.py
        Fetch->>ArXiv: GET /api/query (20 queries)
        ArXiv-->>Fetch: XML/Atom response
        Fetch->>Fetch: Parse & filter CS categories
        Fetch->>Fetch: Save papers/*.md
        Fetch-->>Auto: 34 new papers saved
    end

    rect rgb(255, 240, 230)
        Note over Auto,Enhance: Phase 2: Enhance Papers
        Auto->>Enhance: python3 enhance_papers.py
        Enhance->>Enhance: Extract key contributions
        Enhance->>Enhance: Find related papers
        Enhance->>Enhance: Add citations (APA/MLA/BibTeX)
        Enhance-->>Auto: 77 papers enhanced
    end

    rect rgb(230, 255, 230)
        Note over Auto,Wiki: Phase 3: Inject Wiki Links
        Auto->>Wiki: python3 inject_wikilinks.py
        Wiki->>Wiki: Scan 75+ files for 23 terms
        Wiki->>Wiki: Token-based replacement
        Wiki-->>Auto: 75 files modified
    end

    rect rgb(255, 230, 255)
        Note over Auto,Gen: Phase 4: Generate Data
        Auto->>Gen: python3 generate_search_index.py
        Gen-->>Auto: 113 items indexed
        Auto->>Gen: python3 generate_authors.py
        Gen-->>Auto: 346 authors profiled
        Auto->>Gen: python3 generate_statistics.py
        Gen-->>Auto: Stats computed
        Auto->>Gen: python3 generate_rss.py
        Gen-->>Auto: RSS feed generated
    end

    rect rgb(255, 255, 220)
        Note over Auto,Quarto: Phase 5: Build Site
        Auto->>Quarto: quarto render
        Quarto->>Quarto: Process 119 pages
        Quarto->>Quarto: Apply theme + includes
        Quarto-->>Auto: _site/ generated
    end

    Auto->>Auto: Save state
    Auto-->>Cron: Pipeline complete (58s)

    Note over Server,User: Runtime (continuous)
    User->>Server: GET /global-search.html
    Server-->>User: HTML + search-index.js
    User->>User: Fuzzy search (client-side)
    User->>User: localStorage persistence
```
</div>
</div>

<div id="class-diagram" class="arch-panel">
<h3>Class Diagram — Python Module Architecture</h3>
<p class="diagram-desc">Shows the class structure and relationships between Python modules</p>
<div class="mermaid-diagram">
```mermaid
classDiagram
    class AutomationPipeline {
        +Path base_dir
        +Path state_file
        +load_state() dict
        +save_state(state) void
        +run_command(cmd, desc) tuple
        +step_fetch_papers() tuple
        +step_enhance_papers() tuple
        +step_inject_wikilinks() tuple
        +step_generate_data() tuple
        +step_build_site() tuple
        +run() void
    }

    class ArXivFetcher {
        +dict FOCUS_AREAS
        +search_arxiv(query, max, days) str
        +parse_arxiv_response(xml) list
        +save_paper(paper, date_dir) void
        +fetch_all() int
    }

    class PaperEnhancer {
        +split_sentences(text) list
        +extract_key_contributions(abstract) list
        +find_related_papers(paper, all) list
        +parse_paper_file(filepath) dict
        +enhance_paper(content, all_papers) str
        +enhance_all() int
    }

    class WikiLinkInjector {
        +dict WIKI_TERMS
        +list SKIP_PATTERNS
        +should_skip(filepath) bool
        +inject_wikilinks(content) str
        +process_file(filepath) bool
        +main() void
    }

    class SearchIndexBuilder {
        +extract_frontmatter(content) str
        +clean_markdown(content) str
        +extract_keywords(text, max) list
        +build_search_index() dict
        +main() void
    }

    class AuthorProfiler {
        +parse_authors(author_str) list
        +extract_paper_metadata(filepath) dict
        +build_author_index() dict
        +generate_author_pages() int
    }

    class StatisticsEngine {
        +count_papers_by_topic() dict
        +count_papers_by_date() dict
        +count_papers_by_author() dict
        +generate_charts() void
    }

    class WikiSystem {
        +dict wikiTerms
        +dict backlinkIndex
        +list wikiContributions
        +dict termVersions
        +buildBacklinkIndex() void
        +selectTerm(element) void
        +viewBacklinks() void
        +getBacklinkCount(termId) int
        +exportWiki() void
        +importWiki() void
    }

    class KnowledgeGraph {
        +list graphNodes
        +list graphLinks
        +object simulation
        +buildGraphData() object
        +initGraph() void
        +selectNode(d) void
        +focusNode(nodeId) void
        +filterGraph(filter) void
        +searchGraph() void
    }

    class GlobalSearch {
        +object SEARCH_INDEX
        +fuzzyMatch(text, query) object
        +searchIndex(query, filter) object
        +highlightText(text, query) str
        +getContextSnippet(text, query) str
        +renderResults(results, query) void
        +performSearch() void
    }

    AutomationPipeline --> ArXivFetcher : calls
    AutomationPipeline --> PaperEnhancer : calls
    AutomationPipeline --> WikiLinkInjector : calls
    AutomationPipeline --> SearchIndexBuilder : calls
    AutomationPipeline --> AuthorProfiler : calls
    AutomationPipeline --> StatisticsEngine : calls

    ArXivFetcher --> PaperEnhancer : feeds papers
    PaperEnhancer --> WikiLinkInjector : enhanced papers
    WikiLinkInjector --> SearchIndexBuilder : linked content
    SearchIndexBuilder --> GlobalSearch : search index

    WikiSystem --> KnowledgeGraph : term data
    WikiSystem --> GlobalSearch : wiki terms
    KnowledgeGraph --> GlobalSearch : graph nodes
```
</div>
</div>

<div id="dataflow-diagram" class="arch-panel">
<h3>Data Flow Diagram</h3>
<p class="diagram-desc">Shows how data transforms through the system</p>
<div class="mermaid-diagram">
```mermaid
graph LR
    subgraph Input["Input"]
        A1["arXiv API<br/>(XML/Atom)"]
        A2["User Actions<br/>(Wiki, Bookmarks)"]
    end

    subgraph Process["Processing"]
        B1["Parse & Filter<br/>(CS categories)"]
        B2["Extract Metadata<br/>(title, authors, abstract)"]
        B3["Enhance Content<br/>(contributions, citations)"]
        B4["Inject Links<br/>(wiki terms, bookmarks)"]
        B5["Build Index<br/>(search, authors, stats)"]
        B6["Render Site<br/>(119 pages → HTML)"]
    end

    subgraph Output["Output"]
        C1["Paper Pages<br/>(77 markdown files)"]
        C2["Author Profiles<br/>(346 pages)"]
        C3["Search Index<br/>(113 items)"]
        C4["RSS Feed<br/>(rss.xml)"]
        C5["Static HTML<br/>(_site/ — 119 pages)"]
        C6["Client State<br/>(localStorage)"]
    end

    subgraph Storage["Persistent Storage"]
        D1["papers/*.md"]
        D2["topics/*.qmd"]
        D3["_includes/*.js"]
        D4["_site/*.html"]
        D5["localStorage"]
    end

    A1 --> B1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> B5
    B5 --> B6

    B2 --> C1
    B3 --> C1
    B4 --> C1
    B5 --> C2
    B5 --> C3
    B5 --> C4
    B6 --> C5

    C1 --> D1
    C2 --> D2
    C3 --> D3
    C5 --> D4

    A2 --> C6
    C6 --> D5
    D5 -->|"restore"| C6
```
</div>

<div class="dataflow-stats">
<h4>📊 Data Transformation Summary</h4>
<table class="stats-table">
<tr><th>Stage</th><th>Input</th><th>Output</th><th>Transform</th></tr>
<tr><td>Fetch</td><td>arXiv XML</td><td>77 .md files</td><td>Parse, filter, format</td></tr>
<tr><td>Enhance</td><td>Raw abstracts</td><td>Structured summaries</td><td>NLP extraction</td></tr>
<tr><td>Wiki Links</td><td>75 markdown files</td><td>75 linked files</td><td>Token replacement</td></tr>
<tr><td>Search Index</td><td>All content</td><td>113 indexed items</td><td>Keyword extraction</td></tr>
<tr><td>Authors</td><td>77 papers</td><td>346 profiles</td><td>Author parsing</td></tr>
<tr><td>Render</td><td>119 .md/.qmd</td><td>119 .html files</td><td>Quarto processing</td></tr>
</table>
</div>
</div>

<div id="deployment-diagram" class="arch-panel">
<h3>Deployment Diagram</h3>
<p class="diagram-desc">Shows the runtime infrastructure and deployment topology</p>
<div class="mermaid-diagram">
```mermaid
graph TB
    subgraph DevMachine["Developer Machine (macOS)"]
        subgraph Workspace["Workspace: ~/workspace/research-notes/"]
            SRC["Source Files<br/>*.md, *.qmd, *.py"]
            QUARTO_CFG["_quarto.yml<br/>Configuration"]
            INCLUDES["_includes/<br/>Templates"]
        end

        subgraph Build["Build Pipeline"]
            PYTHON["Python 3.9.6<br/>15 Scripts (3.3KB)"]
            QUARTO["Quarto CLI<br/>Static Site Generator"]
        end

        subgraph Output["Generated Output"]
            SITE["_site/<br/>119 HTML Pages"]
            SEARCH_JS["search-index.js<br/>113 Items"]
            RSS_XML["rss.xml<br/>77 Papers"]
        end

        subgraph Runtime["Runtime Services"]
            HTTP["python3 http.server<br/>:8001 on Tailscale IP"]
            CRON["launchd / Shortcuts<br/>Daily Automation"]
        end

        subgraph ClientStore["Client Storage"]
            LS["localStorage<br/>Wiki, Bookmarks, Notes<br/>Theme, Settings"]
        end
    end

    subgraph Network["Network Layer"]
        TAILSCALE["Tailscale Mesh<br/>100.64.0.17"]
    end

    subgraph External["External"]
        ARXIV_EXT["arXiv API<br/>export.arxiv.org"]
        CDN["CDN (Mermaid, D3)<br/>cdn.jsdelivr.net"]
        BROWSER["User Browser<br/>(Any Device)"]
    end

    SRC --> PYTHON
    QUARTO_CFG --> QUARTO
    INCLUDES --> QUARTO
    PYTHON -->|"Process"| SRC
    PYTHON -->|"Generate"| SEARCH_JS
    PYTHON -->|"Generate"| RSS_XML
    QUARTO -->|"Render"| SITE
    SITE --> HTTP
    HTTP --> TAILSCALE
    TAILSCALE --> BROWSER
    CRON -->|"Daily 6AM"| PYTHON
    BROWSER --> LS
    BROWSER --> CDN
    ARXIV_EXT -->|"XML/Atom"| PYTHON
```
</div>

<div class="deployment-info">
<h4>🖥️ Runtime Environment</h4>
<table class="stats-table">
<tr><th>Component</th><th>Technology</th><th>Details</th></tr>
<tr><td>OS</td><td>macOS 26.6.2</td><td>Host machine</td></tr>
<tr><td>Python</td><td>3.9.6</td><td>/usr/bin/python3</td></tr>
<tr><td>Quarto</td><td>Latest</td><td>Static site generator</td></tr>
<tr><td>Web Server</td><td>python3 http.server</td><td>Port 8001, Tailscale IP</td></tr>
<tr><td>Network</td><td>Tailscale</td><td>100.64.0.17:8001</td></tr>
<tr><td>Automation</td><td>launchd / Shortcuts</td><td>Daily pipeline</td></tr>
<tr><td>Client Storage</td><td>localStorage</td><td>~5MB limit</td></tr>
<tr><td>CDN</td><td>jsdelivr</td><td>Mermaid v10, D3 v7</td></tr>
</table>
</div>
</div>

</div>

<style>
.arch-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.arch-header {
  text-align: center;
  margin-bottom: 30px;
}

.arch-header h2 {
  font-size: 2rem;
  color: #1a1a2e;
  margin-bottom: 8px;
}

.arch-subtitle {
  color: #666;
  font-size: 1.05rem;
  margin-bottom: 24px;
}

.arch-tabs {
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
  background: #f0f2f5;
  padding: 6px;
  border-radius: 12px;
  display: inline-flex;
}

.arch-tab {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #555;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.2s;
}

.arch-tab:hover {
  background: rgba(255,255,255,0.6);
  color: #333;
}

.arch-tab.active {
  background: white;
  color: #667eea;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.arch-panel {
  display: none;
  animation: fadeIn 0.3s ease;
}

.arch-panel.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.arch-panel h3 {
  color: #1a1a2e;
  font-size: 1.4rem;
  margin-bottom: 8px;
}

.diagram-desc {
  color: #666;
  font-size: 0.95rem;
  margin-bottom: 20px;
}

.mermaid-diagram {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  margin-bottom: 24px;
  overflow-x: auto;
}

.mermaid-diagram svg {
  max-width: 100%;
  height: auto;
}

.dataflow-stats, .deployment-info {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  margin-top: 20px;
}

.dataflow-stats h4, .deployment-info h4 {
  color: #1a1a2e;
  margin-bottom: 16px;
  font-size: 1.1rem;
}

.stats-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.stats-table th {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 10px 14px;
  text-align: left;
  font-weight: 600;
}

.stats-table td {
  padding: 10px 14px;
  border-bottom: 1px solid #eee;
  color: #444;
}

.stats-table tr:hover td {
  background: #f8f9ff;
}

.stats-table tr:last-child td {
  border-bottom: none;
}

@media (max-width: 768px) {
  .arch-tabs {
    flex-direction: column;
    width: 100%;
  }
  
  .arch-tab {
    width: 100%;
    text-align: center;
  }
  
  .stats-table {
    font-size: 12px;
  }
  
  .stats-table th, .stats-table td {
    padding: 8px 10px;
  }
}
</style>

<script>
function switchTab(tabName) {
  // Update tab buttons
  document.querySelectorAll('.arch-tab').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabName);
  });
  
  // Update panels
  document.querySelectorAll('.arch-panel').forEach(panel => {
    panel.classList.remove('active');
  });
  
  const targetPanel = document.getElementById(tabName + '-diagram');
  if (targetPanel) {
    targetPanel.classList.add('active');
    
    // Re-render mermaid diagrams in the active panel
    const mermaidDiv = targetPanel.querySelector('.mermaid-diagram pre.mermaid');
    if (mermaidDiv && typeof mermaid !== 'undefined') {
      // Force re-render
      mermaidDiv.removeAttribute('data-processed');
      mermaid.run({ nodes: [mermaidDiv] });
    }
  }
}

// Initialize mermaid with better settings
document.addEventListener('DOMContentLoaded', () => {
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: { useMaxWidth: true, htmlLabels: true },
      sequence: { useMaxWidth: true, wrap: true }
    });
    
    // Render only the active panel's diagram
    const activePanel = document.querySelector('.arch-panel.active');
    if (activePanel) {
      const diagrams = activePanel.querySelectorAll('.mermaid-diagram pre.mermaid');
      if (diagrams.length > 0) {
        mermaid.run({ nodes: Array.from(diagrams) });
      }
    }
  }
});
</script>
