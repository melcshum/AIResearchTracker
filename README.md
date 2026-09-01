# AI Research Tracker

A personalised learning platform powered by AI assistance. Users enter topics to research and save them to create customised learning journeys, while AI tools help organise notes and build learning materials. Built with Quarto and Python.

## 🚀 Quick Start

```bash
# 1. Start the API server (for topic management)
python3 api_server.py &

# 2. Start the web server
./start_server.sh

# 3. Open topic management UI
open http://localhost:8000/topics-management.html

# 4. Fetch papers for your topics
python3 fetch_arxiv.py

# 5. Generate dynamic topic pages
python3 generate_topic_pages.py

# 6. Rebuild the site
quarto render
```

## 👥 Multi-User System

The platform supports multiple users, each with their own research topics:

```bash
# List all users
python3 user_manager.py list

# Create a new user
python3 user_manager.py create alice "Alice Smith"

# Switch active user
python3 user_manager.py switch alice

# Import topic templates
python3 user_manager.py templates
```

Each user has:
- Custom research topics (hierarchical)
- Personalised search queries and keywords
- arXiv category preferences
- Shared access to the paper pool

## 📚 Topic Management

### Web Interface
Visit `/topics-management.html` to:
- Switch between users
- Add/edit/delete topics
- Import pre-built templates
- Toggle topics on/off
- Configure search queries

### Hierarchical Topics
Topics support parent-child relationships:
```
AI Agents
├── GUI Agents
└── Multi-Agent Systems

LLM Reasoning
├── Chain-of-Thought
└── Reasoning Verification
```

### Templates
Pre-built topic packages available:
- AI Agents (Complete)
- LLM Reasoning (Complete)
- RAG & Retrieval (Complete)
- Multi-Modal Models (Complete)

## 🔄 Automation Pipeline

```bash
# Run full pipeline
./daily_automation.sh

# Or step-by-step:
python3 fetch_arxiv.py              # Fetch papers
python3 enhance_papers.py           # Enhance metadata
python3 generate_topic_pages.py     # Generate topic pages
python3 generate_search_data.py     # Update search index
quarto render                       # Build site
```

## 📁 Project Structure

```
research-notes/
├── papers/                    # Shared paper pool (all users)
├── _data/
│   ├── users/                 # Per-user configurations
│   │   ├── default/
│   │   │   └── config.json
│   │   └── {username}/
│   │       └── config.json
│   ├── current-user.txt       # Active user
│   └── shared/
│       └── topic-templates.json
├── public/
│   └── topics/                # Generated topic pages
├── user_manager.py            # Multi-user management
├── api_server.py              # Topic management API
├── generate_topic_pages.py    # Dynamic page generator
├── fetch_arxiv.py             # User-aware paper fetcher
└── topics-management.md       # Web UI
```

## 🛠️ Key Components

### Backend
- **user_manager.py**: Multi-user system with per-user configs
- **api_server.py**: Flask REST API for topic management
- **fetch_arxiv.py**: Fetches papers based on active user's topics
- **generate_topic_pages.py**: Creates personalized topic pages

### Frontend
- **topics-management.html**: User/topic management UI
- **topics-index.html**: Browse all your topics
- **{topic}.html**: Individual topic pages with filtered papers

### Data Storage
- Papers: Shared `papers/` directory
- User configs: `_data/users/{username}/config.json`
- Templates: `_data/shared/topic-templates.json`

## 📖 Documentation

- [MULTI_USER_SYSTEM.md](MULTI_USER_SYSTEM.md) - Complete system architecture
- [private/AGENTS.md](private/AGENTS.md) - Agent guide and conventions
- [private/admin.md](private/admin.md) - Project overview and aims
- [private/requirements.md](private/requirements.md) - User requirements

## 🎯 Project Aim

Personalise the learning platform with AI assistance:
- Enter topics to research and save them to create a personalised learning journey
- Offer a structured learning pathway
- Utilise AI tools to aid learning and help users organise their notes
- Systematically retrieve and include research papers or other sources periodically
- Analyse and build learning materials
- Enhance wiki support with AI-powered features
- AI support for learning automation behind the scenes

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
