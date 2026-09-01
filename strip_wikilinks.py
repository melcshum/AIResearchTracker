#!/usr/bin/env python3
"""
Strip all wiki-term spans from markdown files.
"""

import os
import re
from pathlib import Path

def strip_wikilinks(content):
    """Remove all wiki-term spans, keeping the text content."""
    # Replace <span class="wiki-term"...>text</span> with just text
    return re.sub(r'<span class="wiki-term"[^>]*>(.*?)</span>', r'\1', content)

def process_file(filepath):
    """Process a single markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has wiki links
        if 'class="wiki-term"' not in content:
            return False
        
        # Strip wiki links
        new_content = strip_wikilinks(content)
        
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
                    print(f"✓ {rel_path}")
    
    print(f"\n{'='*60}")
    print(f"Processed {total_count} files")
    print(f"Stripped wiki links from {modified_count} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
