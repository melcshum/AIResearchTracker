# AI Research Tracker

A personalised learning platform powered by AI assistance. Users enter topics to research and save them to create customised learning journeys, while AI tools help organise notes and build learning materials. Built with Quarto and Python.

## Navigation Structure

The site is organized into two main parts:

### 🌐 Research Portal (public/*)
- **Researcher Section**: Paper discovery, reading management, knowledge building, wiki, concept exploration
- **Admin Section**: System settings, automation control, configuration, monitoring

### 🔧 Internal Part (Architecture + Engineering)
- **Architecture Section**: System design, UML diagrams, data flow, component relationships
- **Engineering Section**: Implementation details, code patterns, benchmarks, deployment

## Features

- 📄 **Paper Management**: Fetch, enhance, and organize papers from arXiv
- 🔍 **Search & Filter**: Full-text search with topic filtering and global search (Cmd/Ctrl+K)
- 📊 **Analytics Dashboard**: Statistics, author profiles, and trends
- 🏷️ **Concept Explorer**: Tag cloud and concept mapping with interactive knowledge graph
- 📚 **Reading List**: Bookmark and track reading progress with status tracking
- 📰 **RSS Feed**: Stay updated with latest papers
- 📝 **Notes System**: Add personal notes to papers
- 🔄 **Automation**: Daily paper updates and site rebuilds
- 🕸️ **Knowledge Graph**: D3.js force-directed visualization of concept relationships
- 🔗 **Bidirectional Linking**: Wiki with backlinks and connection tracking

## Quick Start

### View the Site

```bash
cd /Users/ailcshum/workspace/research-notes
python3 -m http.server 8001 --bind 100.64.0.17
```

Access at: `http://100.64.0.17:8001`

### Run Automation

```bash
./run_automation.sh
```

This will:
1. Fetch new papers from arXiv
2. Enhance paper details
3. Generate search data, statistics, and analytics
4. Rebuild the site

## Structure

```
research-notes/
├── papers/              # Daily fetched papers
│   └── YYYY-MM-DD/      # Date-organized
├── topics/              # Curated topic pages
│   ├── ai-agents.qmd
│   ├── llm-reasoning.qmd
│   ├── rag-retrieval.qmd
│   └── multi-modal.qmd
├── concepts/            # Concept glossary and connections
├── digests/             # Weekly/monthly summaries
├── _site/               # Quarto output
├── dashboard.md         # Main dashboard with two-part selection
├── external-hub.md      # Research Portal: Researcher + Admin (system settings)
├── internal-hub.md      # Internal Part: Architecture + Engineering
├── automate.py          # Master automation script
├── run_automation.sh    # Quick automation runner
├── AUTOMATION.md        # Automation guide
└── README.md            # This file
```

## Focus Areas

- **AI Agents**: Autonomous systems, tool use, planning, multi-agent coordination
- **LLM Reasoning**: Chain-of-thought, self-consistency, tree-of-thought, verification
- **RAG & Retrieval**: Dense retrieval, hybrid search, knowledge grounding, citation
- **Multi-modal**: Vision-language models, audio processing, cross-modal reasoning

## Automation Options

### Option 1: Manual Run (Recommended)
```bash
./run_automation.sh
```

### Option 2: macOS Shortcuts App
Create a shortcut that runs `./run_automation.sh`

### Option 3: Cron Job
Add to crontab:
```cron
0 6 * * * cd /Users/ailcshum/workspace/research-notes && python3 automate.py >> automation.log 2>&1
```

See [AUTOMATION.md](AUTOMATION.md) for detailed setup instructions.

## Scripts

- `fetch_arxiv.py` - Fetch papers from arXiv
- `enhance_papers.py` - Extract key contributions and related papers
- `enhance_paper_details.py` - Add structured metadata
- `generate_*.py` - Data generators for various features
- `automate.py` - Master pipeline orchestrator

## Logs

All automation runs are logged to `automation.log`:
```bash
tail -f automation.log
```

## Status

Check automation status:
```bash
python3 automate.py --status
```

## Requirements

- Python 3.9+
- Quarto CLI
- macOS (for launchd integration)

## License

MIT License
