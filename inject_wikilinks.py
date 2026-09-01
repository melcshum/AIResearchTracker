#!/usr/bin/env python3
"""
Inject wiki links into all markdown files.
Uses token-based approach to avoid regex lookbehind issues.
"""

import os
import re
import json
from pathlib import Path

# Wiki terms database
WIKI_TERMS = {
    'ai agent': 'ai-agent',
    'ai agents': 'ai-agent',
    'llm': 'llm',
    'large language model': 'llm',
    'rag': 'rag',
    'retrieval-augmented generation': 'rag',
    'reasoning': 'reasoning',
    'tool use': 'tool-use',
    'planning': 'planning',
    'retrieval': 'retrieval',
    'dense retrieval': 'dense-retrieval',
    'multi-agent': 'multi-agent',
    'memory': 'memory',
    'chain-of-thought': 'cot',
    'chain of thought': 'cot',
    'self-consistency': 'self-consistency',
    'verification': 'verification',
    'embedding': 'embedding',
    'embeddings': 'embedding',
    'reranking': 'reranking',
    'hallucination': 'hallucination',
    'grounding': 'grounding',
    'vision-language': 'vision-lang',
}

# Files to skip
SKIP_PATTERNS = [
    'wiki.md',
    'wiki-graph.md',
    'index.qmd',
    'index.md',
    'dashboard.md',
    '_quarto.yml',
    'AGENTS.md',
    'README.md',
    'OBSIDIAN_ENHANCEMENTS.md',
    'BACKLINKS_IMPLEMENTATION.md',
    'WIKILINK_IMPLEMENTATION.md',
    'inject_wikilinks.py',
    'requirements.md',
    'admin.md',
    'settings.md',
    'AUTOMATION.md',
    'COMPLETE_AUTOMATION_GUIDE.md',
    'SHORTCUTS_SETUP.md',
    'DESIGN_GUIDE.md',
    'UI_ENHANCEMENTS.md',
    'faq.md',
    'resources.md',
    'comparison-tables.md',
]

def should_skip(filepath):
    """Check if file should be skipped."""
    filename = os.path.basename(filepath)
    return any(pattern in filename for pattern in SKIP_PATTERNS)

def inject_wikilinks(content):
    """Inject wiki links using token-based approach."""
    # Step 1: Protect existing HTML tags and code blocks
    placeholders = {}
    counter = [0]
    
    def make_placeholder(match):
        key = f'\x00PH{counter[0]}\x00'
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    # Protect code blocks
    content = re.sub(r'```[\s\S]*?```', make_placeholder, content)
    content = re.sub(r'`[^`]+`', make_placeholder, content)
    
    # Protect script blocks (JavaScript/CSS)
    content = re.sub(r'<script[\s\S]*?</script>', make_placeholder, content)
    
    # Protect existing wiki-term spans
    content = re.sub(r'<span class="wiki-term"[^>]*>.*?</span>', make_placeholder, content)
    
    # Protect HTML tags
    content = re.sub(r'<[^>]+>', make_placeholder, content)
    
    # Protect YAML frontmatter
    content = re.sub(r'^---[\s\S]*?---\n', make_placeholder, content, count=1)
    
    # Protect markdown links [text](url)
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', make_placeholder, content)
    
    # Protect headers (# ## ### etc)
    content = re.sub(r'^#{1,6}\s+.*$', make_placeholder, content, flags=re.MULTILINE)
    
    # Step 2: Find and replace wiki terms in remaining text
    sorted_terms = sorted(WIKI_TERMS.keys(), key=len, reverse=True)
    
    for term in sorted_terms:
        term_id = WIKI_TERMS[term]
        # Use word boundary matching
        pattern = rf'\b({re.escape(term)})\b'
        
        def replace_func(match):
            original = match.group(1)
            return f'<span class="wiki-term" data-term="{term_id}" onclick="window.location.href=\'wiki.html\'">{original}</span>'
        
        content = re.sub(pattern, replace_func, content, flags=re.IGNORECASE)
    
    # Step 3: Restore all placeholders
    for key, value in placeholders.items():
        content = content.replace(key, value)
    
    return content

def process_file(filepath):
    """Process a single markdown file."""
    if should_skip(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has wiki links
        if 'class="wiki-term"' in content:
            return False
        
        # Inject wiki links
        new_content = inject_wikilinks(content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function."""
    base_dir = Path(__file__).parent
    modified_count = 0
    total_count = 0
    modified_files = []
    
    # Find all markdown files
    for root, dirs, files in os.walk(base_dir):
        # Skip _site directory
        if '_site' in root:
            continue
        
        for filename in files:
            if filename.endswith('.md') or filename.endswith('.qmd'):
                filepath = os.path.join(root, filename)
                total_count += 1
                
                if process_file(filepath):
                    modified_count += 1
                    rel_path = os.path.relpath(filepath, base_dir)
                    modified_files.append(rel_path)
                    print(f"✓ {rel_path}")
    
    print(f"\n{'='*60}")
    print(f"Processed {total_count} files")
    print(f"Modified {modified_count} files")
    if modified_files:
        print(f"\nModified files:")
        for f in modified_files:
            print(f"  • {f}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
