#!/usr/bin/env python3
"""
User Topics Manager — loads, validates, and manages user-defined research topics.

Reads from _data/user-topics.json. Falls back to DEFAULT_TOPICS if the file
doesn't exist. All pipeline scripts should use this module instead of
hardcoded FOCUS_AREAS.
"""

import json
from pathlib import Path
from datetime import date

TOPICS_FILE = Path(__file__).parent / '_data' / 'user-topics.json'

DEFAULT_TOPICS = {
    "version": "1.0",
    "user": {"name": "Researcher", "created": str(date.today()), "lastUpdated": str(date.today())},
    "topics": [
        {
            "id": "ai-agents",
            "name": "AI Agents",
            "enabled": True,
            "queries": [
                "AI agent autonomous", "LLM agent tool use",
                "multi-agent systems", "agentic AI planning",
                "GUI agent reinforcement learning"
            ],
            "keywords": [
                "agent", "autonomous", "tool use", "planning",
                "multi-agent", "agentic", "reinforcement learning"
            ],
            "categories": ["cs.AI", "cs.MA", "cs.CL", "cs.LG"],
            "description": "Autonomous systems with tool use, planning, and multi-agent coordination",
            "color": "#667eea",
            "icon": "🤖"
        },
        {
            "id": "llm-reasoning",
            "name": "LLM Reasoning",
            "enabled": True,
            "queries": [
                "chain of thought reasoning", "LLM reasoning verification",
                "large language model reasoning", "reasoning efficiency tokens",
                "self-consistency reasoning"
            ],
            "keywords": [
                "reasoning", "chain of thought", "self-consistency",
                "verification", "language model", "LLM", "thinking"
            ],
            "categories": ["cs.CL", "cs.AI", "cs.LG"],
            "description": "Chain-of-thought, self-consistency, tree-of-thought, and verification techniques",
            "color": "#f093fb",
            "icon": "🧠"
        },
        {
            "id": "rag-retrieval",
            "name": "RAG & Retrieval",
            "enabled": True,
            "queries": [
                "retrieval augmented generation", "RAG knowledge graphs",
                "dense retrieval embeddings", "hybrid search retrieval",
                "retrieval augmented LLM"
            ],
            "keywords": [
                "retrieval", "RAG", "knowledge graph", "embedding",
                "dense retrieval", "hybrid search", "information retrieval"
            ],
            "categories": ["cs.IR", "cs.CL", "cs.AI"],
            "description": "Dense retrieval, hybrid search, knowledge grounding, and citation systems",
            "color": "#4facfe",
            "icon": "🔍"
        },
        {
            "id": "multi-modal",
            "name": "Multi-Modal Models",
            "enabled": True,
            "queries": [
                "vision language model", "multimodal LLM",
                "image text understanding", "multimodal reasoning",
                "document understanding OCR"
            ],
            "keywords": [
                "vision", "multimodal", "multi-modal", "image",
                "document", "OCR", "visual"
            ],
            "categories": ["cs.CV", "cs.AI", "cs.CL", "cs.MM"],
            "description": "Vision-language models, audio processing, and cross-modal reasoning",
            "color": "#43e97b",
            "icon": "🎨"
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


def load_topics_config():
    """Load user topics config from JSON file. Falls back to defaults."""
    if TOPICS_FILE.exists():
        try:
            with open(TOPICS_FILE, 'r') as f:
                config = json.load(f)
            _validate_config(config)
            return config
        except (json.JSONDecodeError, ValueError) as e:
            print(f"⚠️  Warning: Invalid user-topics.json ({e}), using defaults")
            return DEFAULT_TOPICS.copy()
    else:
        print("ℹ️  No user-topics.json found, using default topics")
        return DEFAULT_TOPICS.copy()


def _validate_config(config):
    """Validate config structure. Raises ValueError on invalid config."""
    if 'topics' not in config:
        raise ValueError("Missing 'topics' key")
    if not isinstance(config['topics'], list):
        raise ValueError("'topics' must be a list")
    for i, topic in enumerate(config['topics']):
        if 'id' not in topic:
            raise ValueError(f"Topic {i} missing 'id'")
        if 'name' not in topic:
            raise ValueError(f"Topic '{topic.get('id', i)}' missing 'name'")
        if 'queries' not in topic or not isinstance(topic['queries'], list):
            raise ValueError(f"Topic '{topic['id']}' missing 'queries' list")
        if 'keywords' not in topic or not isinstance(topic['keywords'], list):
            raise ValueError(f"Topic '{topic['id']}' missing 'keywords' list")


def get_enabled_topics(config=None):
    """Return dict of enabled topics {id: topic_config}. Legacy FOCUS_AREAS replacement."""
    if config is None:
        config = load_topics_config()
    return {
        t['id']: t for t in config['topics']
        if t.get('enabled', True)
    }


def get_focus_areas(config=None):
    """Return legacy-compatible FOCUS_AREAS dict {id: [queries]}.
    Drop-in replacement for the old hardcoded FOCUS_AREAS."""
    enabled = get_enabled_topics(config)
    return {tid: t['queries'] for tid, t in enabled.items()}


def get_topic_keywords(config=None):
    """Return {topic_id: [keywords]} for classification."""
    enabled = get_enabled_topics(config)
    return {tid: t['keywords'] for tid, t in enabled.items()}


def get_topic_categories(topic_id, config=None):
    """Return arXiv categories for a specific topic."""
    if config is None:
        config = load_topics_config()
    for t in config['topics']:
        if t['id'] == topic_id:
            return t.get('categories', config.get('preferences', {}).get('defaultCategories', []))
    return config.get('preferences', {}).get('defaultCategories', [])


def get_preferences(config=None):
    """Return user preferences dict."""
    if config is None:
        config = load_topics_config()
    return config.get('preferences', DEFAULT_TOPICS['preferences'])


def save_topics_config(config):
    """Save config to JSON file."""
    config['user']['lastUpdated'] = str(date.today())
    TOPICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TOPICS_FILE, 'w') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved topics config to {TOPICS_FILE}")


def add_topic(config, topic):
    """Add a new topic to config. Validates and appends."""
    required = ['id', 'name', 'queries', 'keywords']
    for key in required:
        if key not in topic:
            raise ValueError(f"Topic missing required field: {key}")
    # Check for duplicate ID
    existing_ids = {t['id'] for t in config['topics']}
    if topic['id'] in existing_ids:
        raise ValueError(f"Topic ID '{topic['id']}' already exists")
    # Set defaults
    topic.setdefault('enabled', True)
    topic.setdefault('categories', config.get('preferences', {}).get('defaultCategories', []))
    topic.setdefault('description', '')
    topic.setdefault('color', '#667eea')
    topic.setdefault('icon', '📌')
    config['topics'].append(topic)
    return config


def remove_topic(config, topic_id):
    """Remove a topic by ID."""
    config['topics'] = [t for t in config['topics'] if t['id'] != topic_id]
    return config


def toggle_topic(config, topic_id, enabled):
    """Enable or disable a topic."""
    for t in config['topics']:
        if t['id'] == topic_id:
            t['enabled'] = enabled
            return config
    raise ValueError(f"Topic '{topic_id}' not found")


def list_topics_summary(config=None):
    """Print a human-readable summary of topics."""
    if config is None:
        config = load_topics_config()
    print(f"\n📚 Research Topics ({len(config['topics'])} total)")
    print("=" * 60)
    for t in config['topics']:
        status = "✅" if t.get('enabled', True) else "❌"
        queries = len(t.get('queries', []))
        keywords = len(t.get('keywords', []))
        cats = ', '.join(t.get('categories', []))
        print(f"  {status} {t.get('icon', '📌')} {t['name']} ({t['id']})")
        print(f"     {queries} queries, {keywords} keywords")
        print(f"     Categories: {cats}")
        if t.get('description'):
            print(f"     {t['description']}")
        print()


if __name__ == '__main__':
    config = load_topics_config()
    list_topics_summary(config)
    print(f"Preferences: {get_preferences(config)}")
