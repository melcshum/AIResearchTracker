#!/usr/bin/env python3
"""Re-enhance papers: strip old enhancements and re-apply with fixed logic."""

import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

from enhance_paper_details import (
    estimate_reading_time,
    extract_key_findings,
    extract_methodology,
    extract_limitations,
    parse_authors,
    generate_bibtex,
    generate_apa_citation
)

def strip_enhancements(content):
    """Remove previously added enhancement sections."""
    # Remove Reading Time
    content = re.sub(r'\n\*\*Reading Time:\*\* ~\d+ min\n', '', content)
    
    # Remove Key Findings section
    content = re.sub(r'\n## Key Findings\n\n(?:- .+\n?)+', '', content)
    
    # Remove Methodology section
    content = re.sub(r'\n## Methodology\n\n(?:- .+\n?)+', '', content)
    
    # Remove Limitations section
    content = re.sub(r'\n## Limitations & Future Work\n\n(?:- .+\n?)+', '', content)
    
    # Remove Citation section (APA + BibTeX)
    content = re.sub(r'\n## Citation\n\n\*\*APA:\*\* .+?\n\n\n\*\*BibTeX:\*\*\n\n```bibtex\n.+?\n```\n', '', content, flags=re.DOTALL)
    
    return content

def re_enhance_paper(filepath):
    """Strip old enhancements and re-apply with fixed logic."""
    content = filepath.read_text()
    
    # Strip old enhancements
    content = strip_enhancements(content)
    
    # Extract metadata
    arxiv_m = re.search(r'\*\*arXiv ID:\*\* (.+)', content)
    authors_m = re.search(r'\*\*Authors:\*\* (.+)', content)
    date_m = re.search(r'\*\*Date:\*\* (.+)', content)
    abstract_m = re.search(r'## Abstract\n\n(.+?)(?=\n\n## |\Z)', content, re.DOTALL)
    title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
    
    if not all([arxiv_m, authors_m, date_m, abstract_m, title_m]):
        print(f"  ⚠ Skipping {filepath.name}: missing metadata")
        return False
    
    paper = {
        'arxiv_id': arxiv_m.group(1).strip(),
        'authors': authors_m.group(1).strip(),
        'date': date_m.group(1).strip(),
        'abstract': abstract_m.group(1).strip(),
        'title': title_m.group(1)
    }
    
    # Extract structured information
    findings = extract_key_findings(paper['abstract'])
    methodology = extract_methodology(paper['abstract'])
    limitations = extract_limitations(paper['abstract'])
    reading_time = estimate_reading_time(paper['abstract'])
    
    # Generate citations
    bibtex = generate_bibtex(paper)
    apa = generate_apa_citation(paper)
    
    # Build enhanced content
    enhanced_sections = []
    
    # Add reading time after metadata
    enhanced_sections.append(f"\n**Reading Time:** ~{reading_time} min\n")
    
    # Add Key Findings
    if findings:
        enhanced_sections.append("\n## Key Findings\n")
        for finding in findings:
            enhanced_sections.append(f"- {finding}")
        enhanced_sections.append("")
    
    # Add Methodology
    if methodology:
        enhanced_sections.append("\n## Methodology\n")
        for method in methodology:
            enhanced_sections.append(f"- {method}")
        enhanced_sections.append("")
    
    # Add Limitations
    if limitations:
        enhanced_sections.append("\n## Limitations & Future Work\n")
        for limit in limitations:
            enhanced_sections.append(f"- {limit}")
        enhanced_sections.append("")
    
    # Add Citation section
    enhanced_sections.append("\n## Citation\n")
    enhanced_sections.append(f"**APA:** {apa}\n")
    enhanced_sections.append("\n**BibTeX:**\n")
    enhanced_sections.append(f"```bibtex\n{bibtex}\n```\n")
    
    # Insert enhanced sections before Related Papers or at end
    enhanced_text = '\n'.join(enhanced_sections)
    
    if '## Related Papers' in content:
        content = content.replace('## Related Papers', f"{enhanced_text}\n## Related Papers")
    else:
        content += enhanced_text
    
    filepath.write_text(content)
    return True

def main():
    papers_dir = Path('papers')
    count = 0
    
    for date_dir in papers_dir.iterdir():
        if not date_dir.is_dir():
            continue
        for filepath in date_dir.glob('*.md'):
            if re_enhance_paper(filepath):
                print(f'✓ Re-enhanced: {filepath.stem[:50]}...')
                count += 1
    
    print(f'\nRe-enhanced {count} papers with fixed logic')

if __name__ == '__main__':
    main()
