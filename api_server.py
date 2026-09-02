#!/usr/bin/env python3
"""
API Server for Topic Management
Provides REST API endpoints for user and topic management.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import date
from user_manager import (
    get_current_user, set_current_user, create_user, list_users,
    load_user_config, save_user_config, get_enabled_topics,
    load_templates, import_template, load_user_data, save_user_data
)
import json

app = Flask(__name__)
CORS(app)

# User endpoints
@app.route('/api/user/config', methods=['GET'])
def get_user_config():
    """Get current user's configuration."""
    try:
        username = get_current_user()
        config = load_user_config(username)
        return jsonify(config)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/list', methods=['GET'])
def get_user_list():
    """List all users."""
    try:
        users = list_users()
        current = get_current_user()
        return jsonify({'users': users, 'current': current})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/switch', methods=['POST'])
def switch_user():
    """Switch to a different user."""
    try:
        data = request.json
        username = data.get('username')
        if not username:
            return jsonify({'error': 'Username required'}), 400
        
        set_current_user(username)
        return jsonify({'success': True, 'username': username})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/create', methods=['POST'])
def create_new_user():
    """Create a new user."""
    try:
        data = request.json
        username = data.get('username')
        displayName = data.get('displayName', username)
        
        if not username:
            return jsonify({'error': 'Username required'}), 400
        
        create_user(username, displayName)
        return jsonify({'success': True, 'username': username})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Topic endpoints
@app.route('/api/topic', methods=['POST'])
def create_topic():
    """Create a new topic."""
    try:
        username = get_current_user()
        config = load_user_config(username)
        data = request.json
        
        # Generate topic ID from name
        topic_id = data['name'].lower().replace(' ', '-')
        topic_id = ''.join(c for c in topic_id if c.isalnum() or c == '-')
        
        # Check if topic already exists
        existing_ids = {t['id'] for t in config['topics']}
        if topic_id in existing_ids:
            return jsonify({'error': 'Topic already exists'}), 400
        
        # Create topic
        topic = {
            'id': topic_id,
            'name': data['name'],
            'icon': data.get('icon', '📄'),
            'description': data.get('description', ''),
            'queries': data.get('queries', []),
            'keywords': data.get('keywords', []),
            'categories': data.get('categories', []),
            'enabled': data.get('enabled', True),
            'children': []
        }
        
        config['topics'].append(topic)
        save_user_config(username, config)
        
        return jsonify({'success': True, 'topic': topic})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/topic/<topic_id>', methods=['PUT'])
def update_topic(topic_id):
    """Update an existing topic."""
    try:
        username = get_current_user()
        config = load_user_config(username)
        data = request.json
        
        # Find topic
        topic = None
        for t in config['topics']:
            if t['id'] == topic_id:
                topic = t
                break
        
        if not topic:
            return jsonify({'error': 'Topic not found'}), 404
        
        # Update fields
        topic['name'] = data.get('name', topic['name'])
        topic['icon'] = data.get('icon', topic['icon'])
        topic['description'] = data.get('description', topic['description'])
        topic['queries'] = data.get('queries', topic['queries'])
        topic['keywords'] = data.get('keywords', topic['keywords'])
        topic['categories'] = data.get('categories', topic['categories'])
        topic['enabled'] = data.get('enabled', topic['enabled'])
        
        save_user_config(username, config)
        
        return jsonify({'success': True, 'topic': topic})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/topic/<topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    """Delete a topic."""
    try:
        username = get_current_user()
        config = load_user_config(username)
        
        # Remove topic
        config['topics'] = [t for t in config['topics'] if t['id'] != topic_id]
        save_user_config(username, config)
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/topic/<topic_id>/toggle', methods=['POST'])
def toggle_topic(topic_id):
    """Toggle topic enabled state."""
    try:
        username = get_current_user()
        config = load_user_config(username)
        data = request.json
        
        # Find topic
        topic = None
        for t in config['topics']:
            if t['id'] == topic_id:
                topic = t
                break
        
        if not topic:
            return jsonify({'error': 'Topic not found'}), 404
        
        topic['enabled'] = data.get('enabled', not topic.get('enabled', True))
        save_user_config(username, config)
        
        return jsonify({'success': True, 'enabled': topic['enabled']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Template endpoints
@app.route('/api/templates', methods=['GET'])
def get_templates():
    """Get available topic templates."""
    try:
        templates_data = load_templates()
        return jsonify(templates_data['templates'])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/template/import', methods=['POST'])
def import_template_endpoint():
    """Import a topic template."""
    try:
        username = get_current_user()
        data = request.json
        template_id = data.get('templateId')
        
        if not template_id:
            return jsonify({'error': 'Template ID required'}), 400
        
        import_template(username, template_id)
        return jsonify({'success': True})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User data endpoints (bookmarks, notes, reading progress)
@app.route('/api/user/data', methods=['GET'])
def get_user_data():
    """Get current user's data (bookmarks, notes, reading progress)."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/data', methods=['POST'])
def update_user_data():
    """Update current user's data."""
    try:
        username = get_current_user()
        data = request.json
        save_user_data(username, data)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/bookmarks', methods=['GET'])
def get_bookmarks():
    """Get user's bookmarks."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify({'bookmarks': data.get('bookmarks', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/bookmarks', methods=['POST'])
def add_bookmark():
    """Add a bookmark."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        paper_id = request.json.get('paperId')
        
        if not paper_id:
            return jsonify({'error': 'paperId required'}), 400
        
        # Add if not exists
        if paper_id not in data['bookmarks']:
            data['bookmarks'].append(paper_id)
            save_user_data(username, data)
        
        return jsonify({'success': True, 'bookmarks': data['bookmarks']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/bookmarks/<paper_id>', methods=['DELETE'])
def remove_bookmark(paper_id):
    """Remove a bookmark."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        
        if paper_id in data['bookmarks']:
            data['bookmarks'].remove(paper_id)
            save_user_data(username, data)
        
        return jsonify({'success': True, 'bookmarks': data['bookmarks']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/notes', methods=['GET'])
def get_notes():
    """Get user's notes."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify({'notes': data.get('notes', {})})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/notes/<paper_id>', methods=['GET'])
def get_paper_note(paper_id):
    """Get note for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        note = data.get('notes', {}).get(paper_id, '')
        return jsonify({'note': note})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/notes/<paper_id>', methods=['POST'])
def save_paper_note(paper_id):
    """Save note for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        note = request.json.get('note', '')
        
        if 'notes' not in data:
            data['notes'] = {}
        
        data['notes'][paper_id] = note
        save_user_data(username, data)
        
        return jsonify({'success': True, 'note': note})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/reading-progress', methods=['GET'])
def get_reading_progress():
    """Get user's reading progress."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify({'readingProgress': data.get('readingProgress', {})})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/reading-progress/<paper_id>', methods=['POST'])
def update_reading_progress(paper_id):
    """Update reading progress for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        status = request.json.get('status')  # 'unread', 'reading', 'read'
        
        if 'readingProgress' not in data:
            data['readingProgress'] = {}
        
        data['readingProgress'][paper_id] = {
            'status': status,
            'updatedAt': date.today().isoformat()
        }
        save_user_data(username, data)
        
        return jsonify({'success': True, 'progress': data['readingProgress'][paper_id]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# AI Summaries endpoints
@app.route('/api/user/summaries', methods=['GET'])
def get_summaries():
    """Get user's AI-generated summaries."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify({'summaries': data.get('summaries', {})})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/summaries/<paper_id>', methods=['GET'])
def get_paper_summary(paper_id):
    """Get AI summary for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        summary = data.get('summaries', {}).get(paper_id)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/summaries/<paper_id>', methods=['POST'])
def save_paper_summary(paper_id):
    """Save AI summary for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        summary = request.json.get('summary', {})
        
        if 'summaries' not in data:
            data['summaries'] = {}
        
        data['summaries'][paper_id] = summary
        save_user_data(username, data)
        
        return jsonify({'success': True, 'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/summaries/<paper_id>', methods=['DELETE'])
def delete_paper_summary(paper_id):
    """Delete AI summary for a specific paper."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        
        if 'summaries' in data and paper_id in data['summaries']:
            del data['summaries'][paper_id]
            save_user_data(username, data)
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Wiki data endpoints
@app.route('/api/user/wiki-data', methods=['GET'])
def get_wiki_data():
    """Get user's wiki data (concepts, explanations, links)."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        return jsonify({
            'wikiConcepts': data.get('wikiConcepts', {}),
            'wikiExplanations': data.get('wikiExplanations', {}),
            'wikiLinks': data.get('wikiLinks', {})
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/wiki-data', methods=['POST'])
def save_wiki_data():
    """Save user's wiki data."""
    try:
        username = get_current_user()
        data = load_user_data(username)
        
        wiki_data = request.json
        data['wikiConcepts'] = wiki_data.get('wikiConcepts', {})
        data['wikiExplanations'] = wiki_data.get('wikiExplanations', {})
        data['wikiLinks'] = wiki_data.get('wikiLinks', {})
        
        save_user_data(username, data)
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Wiki Companion endpoints (LLM-powered)
@app.route('/api/wiki/companion', methods=['POST'])
def wiki_companion():
    """AI Learning Companion for knowledge construction."""
    try:
        import requests
        import json
        
        data = request.json
        mode = data.get('mode')  # 'construct', 'reflect', 'scaffold', 'consolidate', 'revisit'
        explanation = data.get('explanation', '')
        concept = data.get('concept', '')
        prior_explanations = data.get('prior_explanations', [])
        retrieval_attempt = data.get('retrieval_attempt', '')
        
        if not explanation and mode != 'consolidate' and mode != 'revisit':
            return jsonify({'error': 'Explanation required'}), 400
        
        # Build prompt based on mode
        if mode == 'reflect':
            prompt = f"""You are a metacognitive coach. The learner wrote this explanation of {concept}:
"{explanation}"

Generate 2-3 reflective questions that help them examine their understanding.
Focus on: confidence, completeness, assumptions, explanatory adequacy.
Do NOT provide answers. Only ask questions.

Format your response as a JSON array of strings:
["Question 1?", "Question 2?", "Question 3?"]"""
        
        elif mode == 'scaffold':
            action = data.get('action', 'detect_gaps')
            if action == 'detect_gaps':
                prompt = f"""You are a knowledge construction scaffold. The learner wrote this explanation of {concept}:
"{explanation}"

Analyze for missing key concepts and provide suggestions as questions.

Respond ONLY with valid JSON in this exact format:
{{
  "missingTerms": ["term1", "term2"],
  "suggestions": ["Question about concept A?", "Consider how B relates?"]
}}

Do not include any text before or after the JSON. No markdown. No explanations."""
            else:
                prompt = f"""You are a knowledge construction scaffold. The learner wrote this explanation of {concept}:
"{explanation}"

Analyze for:
1. Missing concepts (concepts they should mention but didn't)
2. Potential misconceptions (statements that might be inaccurate)
3. Connection opportunities (related concepts they could link to)

Provide feedback as questions, not corrections.
Example: "You discussed X but not Y. How are they related?"

Format your response as JSON:
{{
  "missing_concepts": ["Concept A", "Concept B"],
  "misconceptions": ["Question about potential misconception"],
  "connections": ["Could this relate to Concept C?"]
}}"""
        
        elif mode == 'consolidate':
            prompt = f"""The learner's original explanation of {concept}:
"{explanation}"

Their retrieval attempt (from memory):
"{retrieval_attempt}"

Compare and provide formative feedback:
- What did they recall correctly?
- What did they miss?
- What misconceptions emerged?

Format your response as JSON:
{{
  "correct_recall": ["Point 1", "Point 2"],
  "missed_points": ["Point 1", "Point 2"],
  "misconceptions": ["Misconception 1"],
  "feedback": "Encouraging summary with targeted questions"
}}"""
        
        elif mode == 'revisit':
            related_concepts = data.get('related_concepts', [])
            prompt = f"""The learner is learning about {concept}.
Their explanation: "{explanation}"

Related concepts they've learned before: {related_concepts}

Generate questions that help them:
1. Integrate this new concept with prior knowledge
2. Identify if earlier explanations need revision
3. Build meaningful connections

Format your response as JSON:
{{
  "integration_questions": ["Question 1", "Question 2"],
  "revision_suggestions": ["Concept X may need revision because..."],
  "connections": ["How {concept} relates to Concept Y"]
}}"""
        
        else:
            return jsonify({'error': f'Unknown mode: {mode}'}), 400
        
        # Call Ollama
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'gemma4-64k',
                'prompt': prompt,
                'stream': False,
                'format': 'json'
            },
            timeout=30
        )
        
        if response.status_code != 200:
            return jsonify({'error': f'Ollama error: {response.status_code}'}), 500
        
        result = response.json()
        response_text = result.get('response', '{}')
        
        # Parse JSON response
        try:
            parsed = json.loads(response_text)
        except json.JSONDecodeError:
            # Try to extract JSON from text
            import re
            match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if match:
                parsed = json.loads(match.group())
            else:
                parsed = {'error': 'Failed to parse LLM response', 'raw': response_text}
        
        return jsonify(parsed)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# Knowledge Context endpoint (DP4: Continuous Knowledge Integration)
@app.route('/api/wiki/context', methods=['POST'])
def get_knowledge_context():
    """Select relevant wiki entries for AI interaction."""
    try:
        import json
        from user_manager import load_user_data
        
        data = request.json
        concept = data.get('concept', '')
        username = get_current_user()
        
        if not concept:
            return jsonify({'error': 'Concept required'}), 400
        
        # Load user's wiki data
        user_data = load_user_data(username)
        wiki_data = user_data.get('wiki', {})
        
        # Find related concepts
        related_concepts = []
        concept_lower = concept.lower()
        
        for entry_concept, entry_data in wiki_data.items():
            if entry_concept.lower() == concept_lower:
                continue  # Skip self
            
            # Check for connections, related concepts, keywords
            connections = entry_data.get('connections', [])
            keywords = entry_data.get('keywords', [])
            
            # Simple relevance scoring
            relevance_score = 0
            if concept_lower in ' '.join(connections).lower():
                relevance_score += 2
            if concept_lower in ' '.join(keywords).lower():
                relevance_score += 1
            
            # Check if this concept is mentioned in the current concept's data
            current_entry = wiki_data.get(concept, {})
            current_connections = current_entry.get('connections', [])
            if entry_concept in current_connections:
                relevance_score += 3
            
            if relevance_score > 0:
                related_concepts.append({
                    'concept': entry_concept,
                    'summary': entry_data.get('explanation', '')[:100] + '...',
                    'relevance': relevance_score,
                    'connections': connections[:3]
                })
        
        # Sort by relevance
        related_concepts.sort(key=lambda x: x['relevance'], reverse=True)
        
        # Return top 5
        return jsonify({
            'context': related_concepts[:5],
            'total_related': len(related_concepts)
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Topic Management API Server...")
    print("Current user:", get_current_user())
    app.run(host='0.0.0.0', port=5001, debug=True)
