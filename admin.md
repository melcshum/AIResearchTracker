---
title: "Admin: About This Project"
---

<div class="admin-container">
<div class="admin-hero">
<h1>🛠️ Behind the Scenes</h1>
<p class="admin-subtitle">Technical documentation and project overview</p>
</div>

<div class="admin-section">
<h2>🎯 Project Aim</h2>
<div class="aim-card">
<p>
The <strong>AI Research Tracker</strong> is a learner-in-the-loop personal knowledge environment designed to position GenAI as a metacognitive and formative scaffold rather than as a substitute knowledge producer.
</p>
<p>
The platform addresses a central tension in educational GenAI: the same cognitive activities that AI can efficiently automate—explaining, organising, connecting, and reformulating information—may themselves constitute important processes through which learning occurs.
</p>
<h3>Core Design Principles</h3>
<ul>
<li><strong>DP1: Learner Ownership</strong> — Learners author and retain control over knowledge artefacts; AI suggestions require explicit evaluation before incorporation</li>
<li><strong>DP2: Scaffold Rather Than Substitute</strong> — AI supports cognitive activity without automatically performing learning-relevant intellectual work on the learner's behalf</li>
<li><strong>DP3: Reflection Before Correction</strong> — Learners inspect and reconsider their reasoning before direct correction is supplied, supporting metacognitive monitoring</li>
<li><strong>DP4: Continuous Knowledge Integration</strong> — New learning relates to previously constructed knowledge, triggering revision of earlier representations</li>
</ul>
<h3>Five-Stage Knowledge Construction Cycle</h3>
<ol>
<li><strong>Construct</strong> — Learner develops initial explanation or representation in personal wiki</li>
<li><strong>Reflect</strong> — AI generates metacognitive prompts to examine confidence and completeness</li>
<li><strong>Scaffold</strong> — AI provides targeted questions, hints, and connection suggestions</li>
<li><strong>Consolidate & Apply</strong> — Learner retrieves and applies knowledge independently of stored artefacts</li>
<li><strong>Revisit & Extend</strong> — New concepts integrate with prior knowledge, revising earlier entries</li>
</ol>
<h3>Key Features</h3>
<ul>
<li><strong>Personalised Learning Journey</strong> — Enter topics to research and build customised learning paths</li>
<li><strong>AI Wiki Companion</strong> — Four modes (Write, Review, Coach, Update) that scaffold rather than substitute</li>
<li><strong>Prompt Before Provide</strong> — AI encourages learners to articulate understanding before receiving explanations</li>
<li><strong>Automated Research Retrieval</strong> — Systematically fetches papers while preserving learner agency in knowledge construction</li>
<li><strong>Concept Graph & Knowledge Base</strong> — Persistent, networked knowledge representation that evolves over time</li>
<li><strong>Formative Evaluation</strong> — Tracks conceptual understanding, knowledge-artefact development, and learner responses to AI scaffolding</li>
</ul>
<p>
The central design challenge is not simply to determine what AI can do for the learner, but to determine <strong>what the learner should continue to do because doing it is part of learning</strong>.
</p>
</div>
</div>

<div class="admin-section">
<h2>🎪 Site Purpose</h2>
<div class="purpose-grid">
<div class="purpose-card">
<div class="purpose-icon">📚</div>
<h3>Knowledge Discovery</h3>
<p>Browse and search 77+ papers with full-text search, topic filtering, and tag-based exploration</p>
</div>
<div class="purpose-card">
<div class="purpose-icon">🔍</div>
<h3>Research Workflow</h3>
<p>Track papers through a 5-stage workflow: Inbox → Reading → Read → Cited → Archived</p>
</div>
<div class="purpose-card">
<div class="purpose-icon">📝</div>
<h3>Annotation & Notes</h3>
<p>Add structured notes to papers, export to BibTeX for Zotero/Mendeley, or Markdown for Obsidian</p>
</div>
<div class="purpose-card">
<div class="purpose-icon">📊</div>
<h3>Visual Analytics</h3>
<p>Explore statistics, tag clouds, author profiles, and topic distributions</p>
</div>
<div class="purpose-card">
<div class="purpose-icon">🎓</div>
<h3>Learning Paths</h3>
<p>Structured reading guides from beginner to expert, with curated must-read papers</p>
</div>
<div class="purpose-card">
<div class="purpose-icon">📖</div>
<h3>Interactive Wiki</h3>
<p>5-step knowledge building: Select terms → Ask questions → Search sources → Explain → Review</p>
</div>
</div>
</div>

<div class="admin-section">
<h2>⚙️ Technical Stack</h2>
<div class="tech-stack">
<div class="tech-category">
<h3>🌐 Static Site Generation</h3>
<div class="tech-item">
<strong>Quarto</strong> — Scientific and technical publishing system
<ul>
<li>Renders Markdown/Quarto Markdown to HTML</li>
<li>Supports Mermaid diagrams for visualizations</li>
<li>Custom themes with SCSS/CSS</li>
<li>Includes system for reusable HTML/CSS/JS components</li>
</ul>
</div>
</div>

<div class="tech-category">
<h3>🐍 Python Automation</h3>
<div class="tech-item">
<strong>Data Pipeline Scripts</strong>
<ul>
<li><code>fetch_arxiv.py</code> — Fetches papers from arXiv API (filtered to CS.AI, CS.CL, CS.IR, CS.LG, CS.MM)</li>
<li><code>enhance_papers.py</code> — Extracts key contributions and related papers</li>
<li><code>enhance_paper_details.py</code> — Adds structured metadata (reading time, methodology, citations)</li>
<li><code>generate_*.py</code> — Generates search data, statistics, tag cloud, RSS, authors, notes</li>
<li><code>automate.py</code> — Master orchestrator for the full pipeline</li>
</ul>
</div>
</div>

<div class="tech-category">
<h3>🎨 Frontend Technologies</h3>
<div class="tech-item">
<strong>HTML/CSS/JavaScript</strong>
<ul>
<li><strong>Bootstrap 5</strong> — Responsive grid system and components</li>
<li><strong>Custom CSS</strong> — Gradient themes, animations, dark mode support</li>
<li><strong>Vanilla JavaScript</strong> — Interactive features (search, filtering, localStorage)</li>
<li><strong>Mermaid.js</strong> — Diagram rendering (flowcharts, sequence diagrams)</li>
<li><strong>localStorage</strong> — Client-side data persistence (bookmarks, notes, preferences)</li>
</ul>
</div>
</div>

<div class="tech-category">
<h3>🔄 Automation & Deployment</h3>
<div class="tech-item">
<strong>Shell Scripts & Scheduling</strong>
<ul>
<li><code>daily_automation.sh</code> — One-click pipeline runner</li>
<li><code>start_server.sh</code> / <code>stop_server.sh</code> — Web server management</li>
<li><strong>macOS Shortcuts</strong> — Menu bar automation (recommended over cron/launchd)</li>
<li><strong>Python HTTP Server</strong> — Serves static site on port 8001</li>
</ul>
</div>
</div>
</div>
</div>

<div class="admin-section">
<h2>🔄 Automation Workflow</h2>
<div class="workflow-diagram">
<div class="workflow-step-admin">
<div class="step-number-admin">1</div>
<div class="step-content-admin">
<h4>Fetch Papers</h4>
<p><code>fetch_arxiv.py</code> queries arXiv API for papers in focus areas (past 7 days)</p>
<ul>
<li>Filters by CS categories: cs.AI, cs.CL, cs.IR, cs.LG, cs.MM</li>
<li>Downloads metadata: title, authors, abstract, arXiv ID, date</li>
<li>Organizes into date-based directories: <code>papers/YYYY-MM-DD/</code></li>
</ul>
</div>
</div>

<div class="workflow-step-admin">
<div class="step-number-admin">2</div>
<div class="step-content-admin">
<h4>Enhance Papers</h4>
<p><code>enhance_papers.py</code> + <code>enhance_paper_details.py</code> add structured metadata</p>
<ul>
<li>Extracts key contributions from abstracts</li>
<li>Identifies related papers by topic overlap</li>
<li>Adds reading time estimates, methodology tags, citation formats</li>
<li>Generates BibTeX, APA, MLA citations</li>
</ul>
</div>
</div>

<div class="workflow-step-admin">
<div class="step-number-admin">3</div>
<div class="step-content-admin">
<h4>Generate Data Pages</h4>
<p><code>generate_*.py</code> scripts produce dynamic content</p>
<ul>
<li><code>generate_search_data.py</code> — JSON for full-text search</li>
<li><code>generate_statistics.py</code> — Analytics dashboard with charts</li>
<li><code>generate_tagcloud_data.py</code> — Tag cloud visualization</li>
<li><code>generate_authors.py</code> — Author profiles from paper data</li>
<li><code>generate_notes.py</code> — Paper notes and reading progress</li>
<li><code>generate_rss.py</code> — RSS feed for paper updates</li>
</ul>
</div>
</div>

<div class="workflow-step-admin">
<div class="step-number-admin">4</div>
<div class="step-content-admin">
<h4>Build Site</h4>
<p><code>quarto render</code> generates static HTML</p>
<ul>
<li>Processes all .md and .qmd files</li>
<li>Renders Mermaid diagrams to SVG</li>
<li>Applies custom themes and includes</li>
<li>Outputs to <code>_site/</code> directory</li>
</ul>
</div>
</div>

<div class="workflow-step-admin">
<div class="step-number-admin">5</div>
<div class="step-content-admin">
<h4>Serve & Access</h4>
<p>Python HTTP server serves the static site</p>
<ul>
<li>Runs on <code>http://100.64.0.17:8001</code> (Tailscale IP)</li>
<li>Managed by <code>start_server.sh</code> / <code>stop_server.sh</code></li>
<li>Zero-downtime updates (just rebuild and refresh)</li>
</ul>
</div>
</div>
</div>
</div>

<div class="admin-section">
<h2>📁 File Structure</h2>
<div class="file-structure">
<pre><code>research-notes/
├── papers/                    # 77 papers organized by date
│   └── YYYY-MM-DD/            # Each day's papers in separate folder
├── topics/                    # 4 curated topic pages
│   ├── ai-agents.qmd
│   ├── llm-reasoning.qmd
│   ├── rag-retrieval.qmd
│   └── multi-modal.qmd
├── concepts/                  # Concept reference pages
│   ├── glossary.md            # 40+ term glossary
│   ├── connections.qmd        # Cross-topic concept map
│   └── papers-by-concept.md   # Papers tagged by concept
├── digests/                   # Weekly summaries
├── _includes/                 # Reusable HTML/CSS/JS
│   ├── mermaid.html           # Mermaid.js initialization
│   ├── custom-head.html       # Font preloads, meta tags
│   ├── custom-style.html      # All custom CSS (465 lines)
│   ├── theme-toggle.html      # Dark mode toggle script
│   └── navbar-custom.html     # Enhanced navigation
├── _site/                     # Quarto output (served by web server)
├── _quarto.yml                # Site configuration
├── index.qmd                  # Landing page with hero + recent papers
├── wiki.md                    # Interactive knowledge wiki
├── research-workflow.md       # Research lifecycle guide
├── search-papers.md           # Full-text search interface
├── reading-list.md            # Bookmarking with status tracking
├── statistics.md              # Analytics dashboard
├── tag-cloud.md               # Concept tag cloud
├── authors.md                 # 346 author profiles
├── automate.py                # Master pipeline orchestrator
├── fetch_arxiv.py             # arXiv paper fetcher
├── enhance_papers.py          # Paper enhancement
├── generate_*.py              # 6 data generator scripts
├── daily_automation.sh        # One-click pipeline runner
├── start_server.sh            # Web server launcher
└── stop_server.sh             # Web server stopper</code></pre>
</div>
</div>

<div class="admin-section">
<h2>📊 Current Statistics</h2>
<div class="stats-grid-admin">
<div class="stat-card-admin">
<div class="stat-value">77</div>
<div class="stat-label">Papers Tracked</div>
</div>
<div class="stat-card-admin">
<div class="stat-value">346</div>
<div class="stat-label">Authors Indexed</div>
</div>
<div class="stat-card-admin">
<div class="stat-value">108</div>
<div class="stat-label">Pages Rendered</div>
</div>
<div class="stat-card-admin">
<div class="stat-value">4</div>
<div class="stat-label">Focus Areas</div>
</div>
<div class="stat-card-admin">
<div class="stat-value">17</div>
<div class="stat-label">Weeks Tracked</div>
</div>
<div class="stat-card-admin">
<div class="stat-value">Daily</div>
<div class="stat-label">Update Frequency</div>
</div>
</div>
</div>

<div class="admin-section">
<h2>📚 Internal Publications</h2>
<div class="publications-panel">
<p>Access internal project papers, conference submissions, and research documentation:</p>
<div class="publication-links">
<a href="papers/index.html" class="pub-link all-papers">
<span class="pub-icon">📚</span>
<div class="pub-info">
<strong>All Publications</strong>
<span>Browse conference papers, journal articles, and white papers</span>
</div>
</a>
<a href="papers/conference/index.html" class="pub-link conference">
<span class="pub-icon">🎤</span>
<div class="pub-info">
<strong>Conference Papers</strong>
<span>Peer-reviewed conference proceedings</span>
</div>
</a>
<a href="papers/journal/index.html" class="pub-link journal">
<span class="pub-icon">📖</span>
<div class="pub-info">
<strong>Journal Publications</strong>
<span>Extended peer-reviewed journal articles</span>
</div>
</a>
<a href="papers/white-papers/index.html" class="pub-link whitepaper">
<span class="pub-icon">📄</span>
<div class="pub-info">
<strong>White Papers</strong>
<span>Technical reports and preprints</span>
</div>
</a>
</div>
</div>
</div>

<div class="admin-section">
<h2>🚀 Quick Start</h2>
<div class="quick-start">
<div class="command-block">
<h4>Run Full Pipeline</h4>
<code>./daily_automation.sh</code>
<p>Fetches papers, enhances metadata, generates data pages, rebuilds site</p>
</div>
<div class="command-block">
<h4>Start Web Server</h4>
<code>./start_server.sh</code>
<p>Starts Python HTTP server on port 8001</p>
</div>
<div class="command-block">
<h4>Check Logs</h4>
<code>tail -f automation.log</code>
<p>View real-time automation logs</p>
</div>
<div class="command-block">
<h4>Access Site</h4>
<code>http://100.64.0.17:8001</code>
<p>Open in browser (Tailscale IP)</p>
</div>
</div>
</div>

<div class="admin-section">
<h2>🔧 Development Notes</h2>
<div class="dev-notes">
<h3>Quarto Configuration</h3>
<p>The site uses Quarto for static site generation with custom includes:</p>
<ul>
<li><strong>Theme</strong>: Cosmo (Bootstrap-based)</li>
<li><strong>Custom CSS</strong>: <code>_includes/custom-style.html</code> (465 lines)</li>
<li><strong>Mermaid</strong>: v10 via CDN for diagram rendering</li>
<li><strong>Fonts</strong>: Inter (Google Fonts) for modern typography</li>
</ul>

<h3>Important Conventions</h3>
<ul>
<li><strong>HTML indentation</strong>: Do NOT indent HTML in .md/.qmd files (4+ spaces = code block in Quarto)</li>
<li><strong>File extensions</strong>: Use .qmd for files with Mermaid diagrams, .md for plain content</li>
<li><strong>Generated pages</strong>: Never edit _site/ directly — always regenerate via pipeline</li>
<li><strong>User data</strong>: Stored in browser localStorage (notes, bookmarks, preferences)</li>
</ul>

<h3>Known Limitations</h3>
<ul>
<li>macOS cron/launchd blocked by security restrictions — use macOS Shortcuts instead</li>
<li>Web server bound to Tailscale IP (not localhost) — requires Tailscale for remote access</li>
<li>No backend database — all data in markdown files and localStorage</li>
</ul>
</div>
</div>

<div class="admin-section">
<h2>📚 Documentation</h2>
<div class="doc-links">
<a href="AGENTS.md" class="doc-link">📋 AGENTS.md — Complete project documentation</a>
<a href="AUTOMATION.md" class="doc-link">🤖 AUTOMATION.md — Automation setup guide</a>
<a href="DESIGN_GUIDE.md" class="doc-link">🎨 DESIGN_GUIDE.md — UI/UX design system</a>
<a href="UI_ENHANCEMENTS.md" class="doc-link">✨ UI_ENHANCEMENTS.md — Visual improvements</a>
<a href="research-workflow.md" class="doc-link">🔬 research-workflow.md — Research lifecycle guide</a>
</div>
</div>
</div>

<style>
.admin-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.admin-hero {
  text-align: center;
  padding: 40px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px;
  margin-bottom: 40px;
}

.admin-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.admin-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
}

.admin-section {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 30px;
}

.admin-section h2 {
  color: #2c3e50;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e0e0e0;
}

.aim-card {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.aim-card ul {
  margin: 15px 0;
  padding-left: 20px;
}

.aim-card li {
  margin: 10px 0;
  line-height: 1.6;
}

.purpose-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.purpose-card {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  transition: all 0.3s;
}

.purpose-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.purpose-icon {
  font-size: 3rem;
  margin-bottom: 10px;
}

.purpose-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.purpose-card p {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.tech-stack {
  display: grid;
  gap: 20px;
}

.tech-category {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.tech-category h3 {
  color: #2c3e50;
  margin-bottom: 15px;
}

.tech-item {
  background: white;
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 10px;
}

.tech-item ul {
  margin: 10px 0 0 0;
  padding-left: 20px;
}

.tech-item li {
  margin: 5px 0;
  font-size: 14px;
  line-height: 1.5;
}

.tech-item code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 13px;
}

.workflow-diagram {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.workflow-step-admin {
  display: flex;
  gap: 20px;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.step-number-admin {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 24px;
  flex-shrink: 0;
}

.step-content-admin {
  flex: 1;
}

.step-content-admin h4 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.step-content-admin p {
  color: #666;
  margin-bottom: 10px;
}

.step-content-admin ul {
  margin: 10px 0;
  padding-left: 20px;
}

.step-content-admin li {
  margin: 5px 0;
  font-size: 14px;
  line-height: 1.5;
}

.step-content-admin code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 13px;
}

.file-structure {
  background: #2d3748;
  color: #e2e8f0;
  padding: 20px;
  border-radius: 8px;
  overflow-x: auto;
}

.file-structure pre {
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.6;
}

.file-structure code {
  color: #e2e8f0;
}

.stats-grid-admin {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.stat-card-admin {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 14px;
  opacity: 0.9;
}

.quick-start {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.command-block {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.command-block h4 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.command-block code {
  display: block;
  background: #2d3748;
  color: #e2e8f0;
  padding: 10px;
  border-radius: 6px;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  margin-bottom: 10px;
}

.command-block p {
  color: #666;
  font-size: 13px;
  margin: 0;
}

.dev-notes {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.dev-notes h3 {
  color: #2c3e50;
  margin-top: 20px;
  margin-bottom: 10px;
}

.dev-notes h3:first-child {
  margin-top: 0;
}

.dev-notes ul {
  margin: 10px 0;
  padding-left: 20px;
}

.dev-notes li {
  margin: 8px 0;
  line-height: 1.6;
}

.doc-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.doc-link {
  display: block;
  background: #f8f9fa;
  padding: 15px 20px;
  border-radius: 8px;
  text-decoration: none;
  color: #2c3e50;
  transition: all 0.2s;
  border-left: 4px solid #667eea;
}

.doc-link:hover {
  background: #e9ecef;
  transform: translateX(4px);
}

/* Publications Panel Styles */
.publications-panel {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.publications-panel p {
  color: #4a5568;
  margin-bottom: 20px;
  font-size: 15px;
}

.publication-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 15px;
}

.pub-link {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 15px;
  background: white;
  border-radius: 8px;
  text-decoration: none;
  color: #2c3e50;
  transition: all 0.2s;
  border-left: 4px solid #667eea;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.pub-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.pub-link.all-papers {
  border-left-color: #667eea;
}

.pub-link.conference {
  border-left-color: #3182ce;
}

.pub-link.journal {
  border-left-color: #38a169;
}

.pub-link.whitepaper {
  border-left-color: #d69e2e;
}

.pub-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.pub-info {
  flex: 1;
}

.pub-info strong {
  display: block;
  color: #2c3e50;
  font-size: 15px;
  margin-bottom: 4px;
}

.pub-info span {
  color: #718096;
  font-size: 13px;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .publication-links {
    grid-template-columns: 1fr;
  }
}
</style>
