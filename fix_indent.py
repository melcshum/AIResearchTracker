#!/usr/bin/env python3
"""Remove leading whitespace from HTML tag lines in markdown files."""
import re
import sys

def fix_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    fixed = []
    for line in lines:
        # If line starts with whitespace followed by <, strip the whitespace
        if re.match(r'^\s+<', line):
            fixed.append(line.lstrip())
        else:
            fixed.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(fixed)
    
    print(f"Fixed: {filepath}")

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        fix_file(filepath)
