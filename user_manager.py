#!/usr/bin/env python3
"""
User Manager — handles multi-user support with data isolation.
Each user has their own topics, preferences, and papers directory.
"""

import json
from pathlib import Path
from datetime import date
import shutil

DATA_DIR = Path(__file__).parent / '_data'
USERS_DIR = DATA_DIR / 'users'
SHARED_DIR = DATA_DIR / 'shared'
CURRENT_USER_FILE = DATA_DIR / 'current-user.txt'
TEMPLATES_FILE = SHARED_DIR / 'topic-templates.json'

# Default user template
DEFAULT_USER_TEMPLATE = {
    "profile": {
        "username": "",
        "displayName": "",
        "created": "",
        "lastActive": "",
        "avatar": "👤",
        "bio": ""
    },
    "topics": [
        {
            "id": "ai-agents",
            "name": "AI Agents",
            "icon": "🤖",
            "enabled": True,
            "queries": [
                "AI agent autonomous",
                "LLM agent tool use",
                "multi-agent systems"
            ],
            "keywords": ["agent", "autonomous", "tool use", "planning", "multi-agent"],
            "categories": ["cs.AI", "cs.MA", "cs.CL", "cs.LG"],
            "description": "Autonomous systems with tool use, planning, and multi-agent coordination",
            "color": "#667eea",
            "children": [
                {
                    "id": "ai-agents.gui",
                    "name": "GUI Agents",
                    "icon": "🖥️",
                    "enabled": True,
                    "queries": ["GUI agent", "web automation", "UI navigation agent"],
                    "keywords": ["GUI", "web agent", "browser", "UI automation"],
                    "categories": ["cs.AI", "cs.HC"],
                    "description": "Agents that interact with graphical user interfaces"
                },
                {
                    "id": "ai-agents.multi-agent",
                    "name": "Multi-Agent Systems",
                    "icon": "👥",
                    "enabled": True,
                    "queries": ["multi-agent coordination", "agent collaboration"],
                    "keywords": ["multi-agent", "coordination", "collaboration"],
                    "categories": ["cs.MA", "cs.AI"],
                    "description": "Systems with multiple cooperating agents"
                }
            ]
        },
        {
            "id": "llm-reasoning",
            "name": "LLM Reasoning",
            "icon": "🧠",
            "enabled": True,
            "queries": [
                "chain of thought reasoning",
                "LLM reasoning verification",
                "large language model reasoning"
            ],
            "keywords": ["reasoning", "chain of thought", "self-consistency", "verification", "LLM"],
            "categories": ["cs.CL", "cs.AI", "cs.LG"],
            "description": "Chain-of-thought, self-consistency, tree-of-thought, and verification techniques",
            "color": "#f093fb",
            "children": []
        },
        {
            "id": "rag-retrieval",
            "name": "RAG & Retrieval",
            "icon": "🔍",
            "enabled": True,
            "queries": [
                "retrieval augmented generation",
                "RAG knowledge graphs",
                "dense retrieval embeddings"
            ],
            "keywords": ["retrieval", "RAG", "knowledge graph", "embedding", "dense retrieval"],
            "categories": ["cs.IR", "cs.CL", "cs.AI"],
            "description": "Dense retrieval, hybrid search, knowledge grounding, and citation systems",
            "color": "#4facfe",
            "children": []
        },
        {
            "id": "multi-modal",
            "name": "Multi-Modal Models",
            "icon": "🎨",
            "enabled": True,
            "queries": [
                "vision language model",
                "multimodal LLM",
                "image text understanding"
            ],
            "keywords": ["vision", "multimodal", "multi-modal", "image", "document", "OCR"],
            "categories": ["cs.CV", "cs.AI", "cs.CL", "cs.MM"],
            "description": "Vision-language models, audio processing, and cross-modal reasoning",
            "color": "#43e97b",
            "children": []
        }
    ],
    "preferences": {
        "defaultCategories": ["cs.AI", "cs.CL", "cs.IR", "cs.LG", "cs.CV", "cs.MM"],
        "maxPapersPerTopic": 10,
        "daysBack": 7,
        "autoEnhance": True,
        "includeCrossListed": True
    }
}

# Pre-built topic templates
DEFAULT_TEMPLATES = {
    "version": "1.0",
    "templates": [
        {
            "id": "ai-agents-complete",
            "name": "AI Agents (Complete)",
            "description": "Comprehensive AI agents topic with GUI, multi-agent, and planning sub-topics",
            "icon": "🤖",
            "topic": {
                "id": "ai-agents",
                "name": "AI Agents",
                "icon": "🤖",
                "queries": [
                    "AI agent autonomous",
                    "LLM agent tool use",
                    "multi-agent systems",
                    "agentic AI planning",
                    "GUI agent reinforcement learning"
                ],
                "keywords": ["agent", "autonomous", "tool use", "planning", "multi-agent", "agentic"],
                "categories": ["cs.AI", "cs.MA", "cs.CL", "cs.LG"],
                "description": "Autonomous systems with tool use, planning, and multi-agent coordination",
                "children": [
                    {
                        "id": "ai-agents.gui",
                        "name": "GUI Agents",
                        "icon": "🖥️",
                        "queries": ["GUI agent", "web automation", "UI navigation"],
                        "keywords": ["GUI", "web agent", "browser", "UI automation"],
                        "categories": ["cs.AI", "cs.HC"],
                        "description": "Agents that interact with graphical user interfaces"
                    },
                    {
                        "id": "ai-agents.multi-agent",
                        "name": "Multi-Agent Systems",
                        "icon": "👥",
                        "queries": ["multi-agent coordination", "agent collaboration", "swarm intelligence"],
                        "keywords": ["multi-agent", "coordination", "collaboration", "swarm"],
                        "categories": ["cs.MA", "cs.AI"],
                        "description": "Systems with multiple cooperating agents"
                    }
                ]
            }
        },
        {
            "id": "llm-reasoning-complete",
            "name": "LLM Reasoning (Complete)",
            "description": "Comprehensive LLM reasoning with chain-of-thought, verification, and efficiency",
            "icon": "🧠",
            "topic": {
                "id": "llm-reasoning",
                "name": "LLM Reasoning",
                "icon": "🧠",
                "queries": [
                    "chain of thought reasoning",
                    "LLM reasoning verification",
                    "large language model reasoning",
                    "reasoning efficiency tokens"
                ],
                "keywords": ["reasoning", "chain of thought", "self-consistency", "verification", "LLM", "thinking"],
                "categories": ["cs.CL", "cs.AI", "cs.LG"],
                "description": "Chain-of-thought, self-consistency, tree-of-thought, and verification techniques",
                "children": [
                    {
                        "id": "llm-reasoning.cot",
                        "name": "Chain-of-Thought",
                        "icon": "⛓️",
                        "queries": ["chain of thought", "step-by-step reasoning"],
                        "keywords": ["chain of thought", "CoT", "step-by-step"],
                        "categories": ["cs.CL", "cs.AI"],
                        "description": "Step-by-step reasoning approaches"
                    },
                    {
                        "id": "llm-reasoning.verification",
                        "name": "Reasoning Verification",
                        "icon": "✅",
                        "queries": ["reasoning verification", "self-consistency"],
                        "keywords": ["verification", "self-consistency", "validation"],
                        "categories": ["cs.CL", "cs.AI"],
                        "description": "Methods for verifying LLM reasoning"
                    }
                ]
            }
        },
        {
            "id": "rag-complete",
            "name": "RAG & Retrieval (Complete)",
            "description": "Comprehensive RAG with dense retrieval, knowledge graphs, and hybrid search",
            "icon": "🔍",
            "topic": {
                "id": "rag-retrieval",
                "name": "RAG & Retrieval",
                "icon": "🔍",
                "queries": [
                    "retrieval augmented generation",
                    "RAG knowledge graphs",
                    "dense retrieval embeddings",
                    "hybrid search retrieval"
                ],
                "keywords": ["retrieval", "RAG", "knowledge graph", "embedding", "dense retrieval", "hybrid search"],
                "categories": ["cs.IR", "cs.CL", "cs.AI"],
                "description": "Dense retrieval, hybrid search, knowledge grounding, and citation systems",
                "children": [
                    {
                        "id": "rag-retrieval.kg",
                        "name": "Knowledge Graphs",
                        "icon": "🕸️",
                        "queries": ["knowledge graph", "graph neural network"],
                        "keywords": ["knowledge graph", "GNN", "graph"],
                        "categories": ["cs.AI", "cs.IR"],
                        "description": "Knowledge graph-based retrieval"
                    }
                ]
            }
        },
        {
            "id": "multi-modal-complete",
            "name": "Multi-Modal Models (Complete)",
            "description": "Comprehensive multi-modal with vision-language, document understanding, and OCR",
            "icon": "🎨",
            "topic": {
                "id": "multi-modal",
                "name": "Multi-Modal Models",
                "icon": "🎨",
                "queries": [
                    "vision language model",
                    "multimodal LLM",
                    "image text understanding",
                    "document understanding OCR"
                ],
                "keywords": ["vision", "multimodal", "multi-modal", "image", "document", "OCR", "visual"],
                "categories": ["cs.CV", "cs.AI", "cs.CL", "cs.MM"],
                "description": "Vision-language models, audio processing, and cross-modal reasoning",
                "children": [
                    {
                        "id": "multi-modal.vision-language",
                        "name": "Vision-Language Models",
                        "icon": "👁️",
                        "queries": ["vision language model", "VLM", "image text"],
                        "keywords": ["vision language", "VLM", "image text"],
                        "categories": ["cs.CV", "cs.CL"],
                        "description": "Models combining vision and language"
                    },
                    {
                        "id": "multi-modal.document",
                        "name": "Document Understanding",
                        "icon": "📄",
                        "queries": ["document understanding", "OCR", "document AI"],
                        "keywords": ["document", "OCR", "layout", "table"],
                        "categories": ["cs.CV", "cs.CL"],
                        "description": "Document analysis and understanding"
                    }
                ]
            }
        }
    ]
}


def init_data_structure():
    """Initialize data directory structure."""
    USERS_DIR.mkdir(parents=True, exist_ok=True)
    SHARED_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create default user if doesn't exist
    default_user_dir = USERS_DIR / 'default'
    if not default_user_dir.exists():
        create_user('default', 'Default User', is_template=True)
    
    # Create templates file if doesn't exist
    if not TEMPLATES_FILE.exists():
        with open(TEMPLATES_FILE, 'w') as f:
            json.dump(DEFAULT_TEMPLATES, f, indent=2, ensure_ascii=False)


def create_user(username, display_name=None, is_template=False):
    """Create a new user with default config."""
    user_dir = USERS_DIR / username
    if user_dir.exists():
        raise ValueError(f"User '{username}' already exists")
    
    user_dir.mkdir(parents=True, exist_ok=True)
    
    # Create user config
    config = DEFAULT_USER_TEMPLATE.copy()
    config['profile']['username'] = username
    config['profile']['displayName'] = display_name or username
    config['profile']['created'] = str(date.today())
    config['profile']['lastActive'] = str(date.today())
    
    # Save config
    with open(user_dir / 'config.json', 'w') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    # Papers are shared — stored in root papers/ directory
    # User-specific data (notes, bookmarks, reading progress) can be added later
    # in _data/users/{username}/user-data.json
    
    print(f"✅ Created user: {username}")
    return user_dir


def get_current_user():
    """Get current active username."""
    if not CURRENT_USER_FILE.exists():
        # Default to 'default' user
        set_current_user('default')
        return 'default'
    
    username = CURRENT_USER_FILE.read_text().strip()
    if not (USERS_DIR / username).exists():
        print(f"⚠️  Current user '{username}' not found, switching to 'default'")
        set_current_user('default')
        return 'default'
    
    return username


def set_current_user(username):
    """Set current active username."""
    user_dir = USERS_DIR / username
    if not user_dir.exists():
        raise ValueError(f"User '{username}' does not exist")
    
    CURRENT_USER_FILE.write_text(username)
    
    # Update lastActive
    config = load_user_config(username)
    config['profile']['lastActive'] = str(date.today())
    save_user_config(username, config)
    
    print(f"✅ Switched to user: {username}")


def list_users():
    """List all users."""
    if not USERS_DIR.exists():
        return []
    
    users = []
    for user_dir in USERS_DIR.iterdir():
        if user_dir.is_dir() and (user_dir / 'config.json').exists():
            config = load_user_config(user_dir.name)
            users.append({
                'username': user_dir.name,
                'displayName': config['profile']['displayName'],
                'created': config['profile']['created'],
                'lastActive': config['profile']['lastActive'],
                'avatar': config['profile']['avatar']
            })
    
    return sorted(users, key=lambda u: u['lastActive'], reverse=True)


def load_user_config(username=None):
    """Load user config. Uses current user if username not specified."""
    if username is None:
        username = get_current_user()
    
    config_file = USERS_DIR / username / 'config.json'
    if not config_file.exists():
        raise ValueError(f"User '{username}' config not found")
    
    with open(config_file, 'r') as f:
        return json.load(f)


def save_user_config(username, config):
    """Save user config."""
    config_file = USERS_DIR / username / 'config.json'
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def get_user_papers_dir(username=None):
    """Get shared papers directory (same for all users)."""
    # Papers are shared across all users
    return Path(__file__).parent / 'papers'


def get_enabled_topics(username=None):
    """Get enabled topics for user (flattened, including children)."""
    config = load_user_config(username)
    topics = {}
    
    def flatten_topic(topic, parent_id=None):
        """Recursively flatten topic and children."""
        topic_id = topic['id']
        if topic.get('enabled', True):
            topics[topic_id] = topic
        
        for child in topic.get('children', []):
            flatten_topic(child, parent_id=topic_id)
    
    for topic in config['topics']:
        flatten_topic(topic)
    
    return topics


def get_topic_keywords(username=None):
    """Get {topic_id: [keywords]} for classification."""
    enabled = get_enabled_topics(username)
    return {tid: t['keywords'] for tid, t in enabled.items()}


def get_topic_queries(username=None):
    """Get {topic_id: [queries]} for fetching."""
    enabled = get_enabled_topics(username)
    return {tid: t['queries'] for tid, t in enabled.items()}


def load_templates():
    """Load topic templates."""
    if not TEMPLATES_FILE.exists():
        return DEFAULT_TEMPLATES
    
    with open(TEMPLATES_FILE, 'r') as f:
        return json.load(f)


def import_template(username, template_id):
    """Import a topic template into user's config."""
    templates = load_templates()
    template = None
    
    for t in templates['templates']:
        if t['id'] == template_id:
            template = t
            break
    
    if not template:
        raise ValueError(f"Template '{template_id}' not found")
    
    config = load_user_config(username)
    
    # Check if topic already exists
    existing_ids = {t['id'] for t in config['topics']}
    if template['topic']['id'] in existing_ids:
        raise ValueError(f"Topic '{template['topic']['id']}' already exists for user '{username}'")
    
    # Add topic
    config['topics'].append(template['topic'])
    save_user_config(username, config)
    
    print(f"✅ Imported template '{template['name']}' for user '{username}'")


def list_templates():
    """List available topic templates."""
    templates = load_templates()
    print(f"\n📚 Available Topic Templates ({len(templates['templates'])})")
    print("=" * 60)
    for t in templates['templates']:
        print(f"  {t['icon']} {t['name']} ({t['id']})")
        print(f"     {t['description']}")
        print()


def load_user_data(username=None):
    """Load user-specific data (bookmarks, notes, reading progress)."""
    if username is None:
        username = get_current_user()
    
    user_dir = USERS_DIR / username
    data_file = user_dir / 'user-data.json'
    
    # Default structure
    default_data = {
        'bookmarks': [],
        'notes': {},
        'readingProgress': {}
    }
    
    if not data_file.exists():
        return default_data
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Ensure all keys exist
            for key in default_data:
                if key not in data:
                    data[key] = default_data[key]
            return data
    except Exception as e:
        print(f"Warning: Could not load user data for {username}: {e}")
        return default_data


def save_user_data(username, data):
    """Save user-specific data."""
    user_dir = USERS_DIR / username
    data_file = user_dir / 'user-data.json'
    
    try:
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error: Could not save user data for {username}: {e}")
        return False


if __name__ == '__main__':
    import sys
    
    init_data_structure()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == 'list':
            users = list_users()
            current = get_current_user()
            print(f"\n👥 Users ({len(users)})")
            print("=" * 60)
            for u in users:
                marker = " ← current" if u['username'] == current else ""
                print(f"  {u['avatar']} {u['displayName']} (@{u['username']}){marker}")
                print(f"     Created: {u['created']}, Last active: {u['lastActive']}")
                print()
        
        elif cmd == 'create' and len(sys.argv) > 2:
            username = sys.argv[2]
            display_name = sys.argv[3] if len(sys.argv) > 3 else None
            create_user(username, display_name)
        
        elif cmd == 'switch' and len(sys.argv) > 2:
            username = sys.argv[2]
            set_current_user(username)
        
        elif cmd == 'templates':
            list_templates()
        
        else:
            print("Usage:")
            print("  python3 user_manager.py list")
            print("  python3 user_manager.py create <username> [display_name]")
            print("  python3 user_manager.py switch <username>")
            print("  python3 user_manager.py templates")
    else:
        # Default: show current user and topics
        current = get_current_user()
        print(f"Current user: {current}")
        config = load_user_config(current)
        print(f"Display name: {config['profile']['displayName']}")
        print(f"Topics: {len(config['topics'])}")
        enabled = get_enabled_topics(current)
        print(f"Enabled topics (including children): {len(enabled)}")
