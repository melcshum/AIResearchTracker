#!/usr/bin/env python3
"""
API Server for Topic Management
Provides REST API endpoints for user and topic management.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from user_manager import (
    get_current_user, set_current_user, create_user, list_users,
    load_user_config, save_user_config, get_enabled_topics,
    load_templates, import_template
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

if __name__ == '__main__':
    print("Starting Topic Management API Server...")
    print("Current user:", get_current_user())
    app.run(host='0.0.0.0', port=5001, debug=True)
