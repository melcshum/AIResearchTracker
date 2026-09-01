# AI Research Tracker - Feature Summary

## 🎯 Project Overview

A **personalised learning platform powered by AI assistance** that helps users research topics, organise papers, and build knowledge through AI-powered tools.

---

## ✅ Completed Features

### 1. Multi-User System
- **User Management**: Create, switch, and manage multiple users
- **Per-User Topics**: Each user has their own research topics and preferences
- **Shared Paper Pool**: All users access the same papers but filter by their topics
- **Hierarchical Topics**: Parent-child topic relationships for better organisation

**Files**: `user_manager.py`, `_data/users/*/config.json`

### 2. Topic Management
- **Web UI**: Interactive interface at `/topics-management.html`
- **Topic Templates**: Pre-built packages for AI Agents, LLM Reasoning, RAG, Multi-Modal
- **Dynamic Page Generation**: Auto-generates topic pages based on user config
- **API Server**: Flask REST API for topic management (port 5001)

**Files**: `topics-management.md`, `api_server.py`, `generate_topic_pages.py`

### 3. Paper Management
- **arXiv Integration**: Fetches papers based on user's enabled topics
- **Paper Storage**: Markdown files in `papers/YYYY-MM-DD/` structure
- **Metadata Extraction**: Authors, abstract, topics, URLs
- **Shared Pool**: 102+ papers across 6 enabled topics

**Files**: `fetch_arxiv.py`, `papers/`

### 4. Search & Discovery
- **Full-Text Search**: Search across all papers
- **Topic Filtering**: Filter papers by user's enabled topics
- **Global Search**: Cmd/Ctrl+K shortcut for quick search
- **Author Profiles**: Browse papers by author

**Files**: `public/search-papers.md`, `public/authors.md`

### 5. Reading List & Progress Tracking
- **Bookmarks**: Save papers for later reading
- **Reading Status**: Track inbox/reading/read/archived
- **Personal Notes**: Add notes to each paper
- **API Persistence**: All data stored per-user via API

**Files**: `public/reading-list.md`, `api_server.py`

### 6. Learning Dashboard
- **Overview Stats**: Total papers, read count, notes count, active topics
- **Topic Progress**: Visual progress bars per topic
- **Recent Activity**: Latest bookmarks and notes
- **Reading Activity**: 7-day activity chart

**Files**: `public/dashboard.md`

### 7. Personalised Learning Path
- **AI-Generated Pathway**: Creates learning sequence based on saved papers
- **Step-by-Step Progress**: Visual learning steps with completion status
- **Knowledge Map**: Shows topic connections
- **Recommendations**: AI-powered next steps

**Files**: `public/my-learning-path.md`

### 8. AI Paper Summaries
- **Auto-Generation**: Extracts key points from abstracts
- **Per-Paper Summaries**: One-liner + key points
- **Batch Generation**: Generate all summaries at once
- **API Storage**: Persists summaries per user

**Files**: `public/ai-summaries.md`, `api_server.py`

### 9. AI Study Guide
- **Concept Extraction**: Identifies 12 key AI/ML concepts
- **Flashcards**: Auto-generates Q&A from notes
- **Key Insights**: Extracts important points from user notes
- **Export**: Download as Markdown

**Files**: `public/ai-study-guide.md`

### 10. Weekly Digest
- **Auto-Generation**: Creates weekly summary of new papers
- **Theme Analysis**: Identifies top research themes
- **Highlight Papers**: Shows most relevant papers
- **Learning Insights**: Personalised progress report

**Files**: `generate_weekly_digest.py`, `public/digests/week-2026-36.md`

### 11. AI Wiki Assistant
- **Concept Extraction**: 12 AI/ML concepts with definitions
- **AI Explanations**: Context-aware explanations
- **Paper Linking**: Connects concepts to related papers
- **Persistent Storage**: Wiki data per user

**Files**: `public/ai-wiki.md`, `api_server.py`

### 12. Wiki with Bidirectional Links
- **Interactive Wiki**: Click terms to explore
- **Backlinks**: See what links to each concept
- **Knowledge Graph**: D3.js force-directed visualization
- **Concept Explorer**: Tag cloud and concept mapping

**Files**: `public/wiki.md`, `public/wiki-graph.md`

---

## 📊 Current Statistics

- **Total Papers**: 102+
- **Authors**: 346+
- **Enabled Topics**: 6 (AI Agents, GUI Agents, Multi-Agent, LLM Reasoning, RAG, Multi-Modal)
- **Weekly Papers**: 47 (last 7 days)
- **Users**: 2 (default, melcshum)

---

## 🚀 Quick Start

```bash
# 1. Start API server
python3 api_server.py &

# 2. Start web server
python3 -m http.server 8001 --bind 100.64.0.17

# 3. Open in browser
open http://100.64.0.17:8001

# 4. Manage topics
open http://100.64.0.17:8001/topics-management.html
```

---

## 📁 Key Files

### Backend
- `user_manager.py` - Multi-user system
- `api_server.py` - REST API (port 5001)
- `fetch_arxiv.py` - Paper fetcher
- `generate_topic_pages.py` - Topic page generator
- `generate_weekly_digest.py` - Weekly digest generator

### Frontend (public/)
- `dashboard.md` - Learning dashboard
- `my-learning-path.md` - Personalised learning path
- `ai-summaries.md` - AI paper summaries
- `ai-study-guide.md` - AI study materials
- `ai-wiki.md` - AI wiki assistant
- `reading-list.md` - Reading list with notes
- `search-papers.md` - Paper search
- `wiki.md` - Interactive wiki

### Data
- `_data/users/*/config.json` - User configs
- `_data/users/*/user-data.json` - User data (bookmarks, notes, etc.)
- `papers/` - Shared paper pool
- `public/digests/` - Weekly digests

---

## 🎨 Navigation Structure

```
🌐 Research Portal
├── 📊 Dashboard
├── 🎯 My Learning Path
├── 📰 Weekly Digest
├── 🤖 AI Wiki Assistant
└── 🔧 Admin Dashboard
```

---

## 🔧 API Endpoints

### User Management
- `GET /api/user/config` - Get user config
- `POST /api/user/switch` - Switch user
- `GET /api/user/list` - List users

### Topics
- `GET /api/user/topics` - Get topics
- `POST /api/user/topics` - Add topic
- `PUT /api/user/topics/<id>` - Update topic
- `DELETE /api/user/topics/<id>` - Delete topic

### User Data
- `GET /api/user/data` - Get all user data
- `POST /api/user/bookmarks` - Add bookmark
- `DELETE /api/user/bookmarks/<id>` - Remove bookmark
- `POST /api/user/notes/<id>` - Save note
- `POST /api/user/reading-progress/<id>` - Update progress
- `GET /api/user/summaries` - Get summaries
- `POST /api/user/summaries/<id>` - Save summary
- `GET /api/user/wiki-data` - Get wiki data
- `POST /api/user/wiki-data` - Save wiki data

---

## 🎯 Project Aims (Achieved)

✅ **Personalise the learning platform with AI assistance**
✅ **Enter topics to research and save them to create a personalised learning journey**
✅ **Offer a structured learning pathway**
✅ **Utilise AI tools to aid learning and help users organise their notes**
✅ **Systematically retrieve and include research papers or other sources periodically**
✅ **Analyse and build learning materials**
✅ **Enhance wiki support with AI-powered features**
✅ **AI support for learning automation behind the scenes**

---

## 📝 Next Steps (Optional Enhancements)

1. **Automated Weekly Digest**: Set up cron job to auto-generate digests
2. **AI-Powered Recommendations**: Suggest papers based on reading history
3. **Collaborative Features**: Share notes and bookmarks between users
4. **Mobile App**: React Native or Flutter app
5. **Advanced Analytics**: Citation networks, co-author graphs
6. **Export Options**: BibTeX, CSV, PDF reports
7. **Integration**: Zotero, Mendeley, Notion sync

---

## 🎉 Summary

The AI Research Tracker is now a **complete personalised learning platform** with:
- Multi-user support with per-user topics
- AI-powered learning tools (summaries, study guides, wiki)
- Progress tracking and personalised pathways
- Weekly digests and automated paper fetching
- Interactive wiki with knowledge graphs
- Full REST API for data management

All features are **working and deployed** to GitHub: https://github.com/melcshum/AIResearchTracker
