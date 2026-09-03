# Multi-User Topic Management System

## ✅ Completed Components

### 1. Multi-User Backend (`user_manager.py`)
- User creation and switching
- Per-user topic configuration stored in `_data/users/{username}/config.json`
- Shared papers directory (all users see the same papers)
- Hierarchical topic support (parent topics with children)
- Topic templates system

**Data Structure:**
```
_data/
├── users/
│   ├── default/
│   │   └── config.json
│   └── melcshum/
│       └── config.json
├── current-user.txt
└── shared/
    └── topic-templates.json
```

**CLI Commands:**
```bash
python3 user_manager.py list              # List all users
python3 user_manager.py create <name>     # Create new user
python3 user_manager.py switch <name>     # Switch active user
python3 user_manager.py templates         # List available templates
```

### 2. Updated Paper Fetching (`fetch_arxiv.py`)
- Now reads topics from active user's config
- Uses `user_manager` module instead of hardcoded `FOCUS_AREAS`
- Fetches papers based on user's enabled topics
- Classifies papers against user's topic keywords

**Usage:**
```bash
# Fetch papers for current user
python3 fetch_arxiv.py

# Switch user and fetch
python3 user_manager.py switch melcshum
python3 fetch_arxiv.py
```

### 3. Topic Management UI (`public/topics-management.md`)
- User switcher dropdown
- Topic list with enable/disable toggles
- Add/edit/delete topics
- Import from templates
- Modal form for topic editing

**Features:**
- Real-time topic management
- Visual topic cards with metadata
- Template import system
- Responsive design

### 4. API Server (`api_server.py`)
Flask REST API providing endpoints for:
- User management (list, create, switch)
- Topic CRUD operations
- Template listing and import
- Topic toggle enable/disable

**Endpoints:**
```
GET  /api/user/config          # Get current user config
GET  /api/user/list            # List all users
POST /api/user/switch          # Switch active user
POST /api/user/create          # Create new user

POST /api/topic                # Create topic
PUT  /api/topic/<id>           # Update topic
DELETE /api/topic/<id>         # Delete topic
POST /api/topic/<id>/toggle    # Toggle topic enabled

GET  /api/templates            # List templates
POST /api/template/import      # Import template
```

**Run Server:**
```bash
python3 api_server.py
# Server runs on http://localhost:5001
```

## ⏳ Next Steps

### Phase 5: Dynamic Topic Pages
Generate topic pages dynamically based on user's topics:
- Create `generate_topic_pages.py` script
- Generate one page per enabled topic
- Filter papers by topic keywords
- Support hierarchical display (parent + children)
- Integrate with Quarto build process

### Phase 6: Migration & Documentation
- Migrate existing hardcoded topics to default user
- Update documentation (README, AGENTS.md)
- Add user guide for topic management
- Create video tutorial or screenshots

### Phase 7: Testing & Polish
- End-to-end testing of full workflow
- Error handling and edge cases
- UI/UX improvements
- Performance optimization

## 🎯 Current Workflow

1. **Start API Server:**
   ```bash
   python3 api_server.py
   ```

2. **Open Topic Management UI:**
   ```
   http://localhost:8000/topics-management.html
   ```

3. **Manage Topics:**
   - Switch between users
   - Add/edit/delete topics
   - Import templates
   - Toggle topics on/off

4. **Fetch Papers:**
   ```bash
   python3 fetch_arxiv.py
   ```

5. **View Results:**
   Papers are fetched based on active user's topics and stored in shared `papers/` directory.

## 📊 Architecture Summary

```
User (melcshum)
    ↓
User Config (_data/users/melcshum/config.json)
    ↓
fetch_arxiv.py reads topics
    ↓
arXiv API query
    ↓
Papers stored in shared papers/
    ↓
All users can view papers
    ↓
Each user filters by their topics
```

## 🔧 Technical Details

### Topic Schema
```json
{
  "id": "ai-agents",
  "name": "AI Agents",
  "icon": "🤖",
  "description": "...",
  "queries": ["AI agent autonomous", "LLM agent tool use"],
  "keywords": ["agent", "autonomous", "tool use"],
  "categories": ["cs.AI", "cs.MA"],
  "enabled": true,
  "children": [
    {
      "id": "ai-agents.gui",
      "name": "GUI Agents",
      ...
    }
  ]
}
```

### User Config Schema
```json
{
  "username": "melcshum",
  "displayName": "Mel",
  "created": "2026-09-01",
  "lastActive": "2026-09-01",
  "topics": [...],
  "preferences": {
    "daysBack": 7,
    "maxPapersPerTopic": 10
  }
}
```

## 🚀 Quick Start

```bash
# 1. Initialize data structure
python3 -c "from user_manager import init_data_structure; init_data_structure()"

# 2. Start API server
python3 api_server.py &

# 3. Start web server (if not running)
./start_server.sh

# 4. Open browser
open http://localhost:8000/topics-management.html

# 5. Fetch papers
python3 fetch_arxiv.py
```
