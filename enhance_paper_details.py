#!/usr/bin/env python3
"""
Enhance paper detail pages with structured metadata:
- Key findings
- Methodology
- Limitations
- Code/data links
- Citation formats (BibTeX, APA)
- Reading time estimate
"""

import re
from pathlib import Path

def estimate_reading_time(text):
    """Estimate reading time in minutes (avg 200-250 words per minute).
    For academic papers, assume 3000-5000 words total."""
    # Abstract is just a summary; estimate full paper length
    words = len(text.split())
    # Assume abstract is ~10% of paper, so multiply by 10
    estimated_paper_words = words * 10
    minutes = max(5, estimated_paper_words // 225)
    return min(minutes, 30)  # Cap at 30 minutes

def extract_key_findings(abstract):
    """Extract key findings from abstract."""
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    findings = []
    
    # Look for result/finding indicators
    indicators = [
        'achieve', 'demonstrate', 'show', 'outperform', 'improve',
        'reduce', 'increase', 'result', 'finding', 'experiment',
        'evaluation', 'benchmark', 'accuracy', 'performance'
    ]
    
    for sentence in sentences:
        if any(ind in sentence.lower() for ind in indicators):
            findings.append(sentence.strip())
    
    return findings[:3] if findings else sentences[:2]

def extract_methodology(abstract):
    """Extract methodology description from abstract."""
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    method_sentences = []
    
    # Look for methodology indicators
    indicators = [
        'propose', 'introduce', 'present', 'develop', 'method',
        'approach', 'framework', 'system', 'model', 'algorithm',
        'technique', 'architecture', 'design', 'implement'
    ]
    
    for sentence in sentences:
        if any(ind in sentence.lower() for ind in indicators):
            method_sentences.append(sentence.strip())
    
    return method_sentences[:2] if method_sentences else []

def extract_limitations(abstract):
    """Extract limitations or future work from abstract."""
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    limitations = []
    
    # Look for limitation indicators
    indicators = [
        'limitation', 'future work', 'challenge', 'difficult',
        'however', 'although', 'while', 'constraint', 'issue'
    ]
    
    for sentence in sentences:
        if any(ind in sentence.lower() for ind in indicators):
            limitations.append(sentence.strip())
    
    return limitations[:2] if limitations else []

def parse_authors(authors_str):
    """Parse authors string like 'Han, Y, Qian, T' into list of author names."""
    parts = [p.strip() for p in authors_str.split(',')]
    authors = []
    i = 0
    while i < len(parts):
        # Check if this looks like "Lastname, Initial" pattern
        if i + 1 < len(parts) and len(parts[i+1]) <= 3 and parts[i+1].isupper():
            authors.append(f"{parts[i]}, {parts[i+1]}")
            i += 2
        else:
            authors.append(parts[i])
            i += 1
    return authors

def generate_bibtex(paper):
    """Generate BibTeX citation."""
    authors = parse_authors(paper['authors'])
    authors_bibtex = ' and '.join(authors)
    year = paper['date'][:4]
    title = paper['title'].replace('{', '\\{').replace('}', '\\}')
    
    bibtex = f"""@article{{{paper['arxiv_id'].replace('.', '')},
  title={{{title}}},
  author={{{authors_bibtex}}},
  year={{{year}}},
  eprint={{{paper['arxiv_id']}}},
  archivePrefix={{arXiv}},
  primaryClass={{cs.AI}},
  url={{https://arxiv.org/abs/{paper['arxiv_id']}}}
}}"""
    return bibtex

def generate_apa_citation(paper):
    """Generate APA format citation."""
    authors = parse_authors(paper['authors'])
    if len(authors) == 1:
        authors_str = authors[0]
    elif len(authors) == 2:
        authors_str = f"{authors[0]} & {authors[1]}"
    else:
        authors_str = ', '.join(authors[:-1]) + f", & {authors[-1]}"
    
    year = paper['date'][:4]
    title = paper['title']
    
    return f"{authors_str} ({year}). {title}. arXiv:{paper['arxiv_id']}"

def enhance_paper_page(filepath):
    """Enhance a single paper page with structured metadata."""
    content = filepath.read_text()
    
    # Check if already enhanced
    if '## Key Findings' in content:
        return False
    
    # Extract metadata
    arxiv_m = re.search(r'\*\*arXiv ID:\*\* (.+)', content)
    authors_m = re.search(r'\*\*Authors:\*\* (.+)', content)
    date_m = re.search(r'\*\*Date:\*\* (.+)', content)
    abstract_m = re.search(r'## Abstract\n\n(.+?)(?=\n\n## |\Z)', content, re.DOTALL)
    
    if not all([arxiv_m, authors_m, date_m, abstract_m]):
        return False
    
    paper = {
        'arxiv_id': arxiv_m.group(1).strip(),
        'authors': authors_m.group(1).strip(),
        'date': date_m.group(1).strip(),
        'abstract': abstract_m.group(1).strip(),
        'title': re.search(r'^# (.+)$', content, re.MULTILINE).group(1)
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
            if enhance_paper_page(filepath):
                print(f'✓ Enhanced: {filepath.stem[:50]}...')
                count += 1
    
    print(f'\nEnhanced {count} papers with structured metadata')

if __name__ == '__main__':
    main()
