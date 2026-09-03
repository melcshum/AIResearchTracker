#!/usr/bin/env python3
"""
Pilot Study Data Analysis Script
Analyzes feedback forms and interaction logs from AI Wiki Companion pilot study
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import statistics

# Configuration
PILOT_DATA_DIR = Path("/Users/ailcshum/workspace/research-notes/pilot-data")
FEEDBACK_FORMS_DIR = PILOT_DATA_DIR / "feedback-forms"
INTERACTION_LOGS_DIR = PILOT_DATA_DIR / "interaction-logs"
OUTPUT_DIR = PILOT_DATA_DIR / "analysis"

# Ensure directories exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class FeedbackAnalyzer:
    """Analyzes feedback form responses"""
    
    def __init__(self):
        self.responses = []
        self.section_scores = {
            'A': {'name': 'Usability', 'questions': 4, 'scores': []},
            'B': {'name': 'Learning Experience', 'questions': 5, 'scores': []},
            'C': {'name': 'Epistemic Agency', 'questions': 4, 'scores': []}
        }
        self.open_responses = []
        self.behavioral_data = []
    
    def parse_feedback_form(self, form_path):
        """Parse a single feedback form (JSON format)"""
        with open(form_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        response = {
            'participant_id': data.get('participant_id', 'unknown'),
            'date': data.get('date', ''),
            'concept': data.get('concept', ''),
            'session_number': data.get('session_number', 1),
            'sections': {}
        }
        
        # Parse Section A: Usability (Q1-Q4)
        section_a_scores = []
        for q_num in range(1, 5):
            score = data.get(f'q{q_num}', None)
            if score is not None:
                section_a_scores.append(score)
        response['sections']['A'] = section_a_scores
        self.section_scores['A']['scores'].extend(section_a_scores)
        
        # Parse Section B: Learning Experience (Q5-Q9)
        section_b_scores = []
        for q_num in range(5, 10):
            score = data.get(f'q{q_num}', None)
            if score is not None:
                section_b_scores.append(score)
        response['sections']['B'] = section_b_scores
        self.section_scores['B']['scores'].extend(section_b_scores)
        
        # Parse Section C: Epistemic Agency (Q10-Q13)
        section_c_scores = []
        for q_num in range(10, 14):
            score = data.get(f'q{q_num}', None)
            if score is not None:
                section_c_scores.append(score)
        response['sections']['C'] = section_c_scores
        self.section_scores['C']['scores'].extend(section_c_scores)
        
        # Parse open-ended responses (Q14-Q18)
        open_responses = {}
        for q_num in range(14, 19):
            response_text = data.get(f'q{q_num}', '')
            if response_text.strip():
                open_responses[f'q{q_num}'] = response_text
        response['open_responses'] = open_responses
        self.open_responses.append(open_responses)
        
        # Parse behavioral data (Section E)
        behavioral = {
            'participant_id': response['participant_id'],
            'time_construct': data.get('time_construct', 0),
            'time_reflect': data.get('time_reflect', 0),
            'time_scaffold': data.get('time_scaffold', 0),
            'time_consolidate': data.get('time_consolidate', 0),
            'time_revisit': data.get('time_revisit', 0),
            'time_total': data.get('time_total', 0),
            'revisions': data.get('revisions', 0),
            'feedback_requests': data.get('feedback_requests', 0),
            'concepts_explored': data.get('concepts_explored', 0)
        }
        response['behavioral'] = behavioral
        self.behavioral_data.append(behavioral)
        
        self.responses.append(response)
        return response
    
    def load_all_forms(self):
        """Load all feedback forms from directory"""
        if not FEEDBACK_FORMS_DIR.exists():
            print(f"Warning: {FEEDBACK_FORMS_DIR} does not exist")
            return
        
        form_files = list(FEEDBACK_FORMS_DIR.glob("*.json"))
        print(f"Found {len(form_files)} feedback forms")
        
        for form_file in form_files:
            try:
                self.parse_feedback_form(form_file)
            except Exception as e:
                print(f"Error parsing {form_file}: {e}")
    
    def calculate_statistics(self):
        """Calculate summary statistics for each section"""
        stats = {}
        
        for section_key, section_data in self.section_scores.items():
            scores = section_data['scores']
            if scores:
                stats[section_key] = {
                    'name': section_data['name'],
                    'n': len(scores),
                    'mean': statistics.mean(scores),
                    'median': statistics.median(scores),
                    'stdev': statistics.stdev(scores) if len(scores) > 1 else 0,
                    'min': min(scores),
                    'max': max(scores)
                }
            else:
                stats[section_key] = {
                    'name': section_data['name'],
                    'n': 0,
                    'mean': 0,
                    'median': 0,
                    'stdev': 0,
                    'min': 0,
                    'max': 0
                }
        
        return stats
    
    def calculate_behavioral_stats(self):
        """Calculate behavioral statistics"""
        if not self.behavioral_data:
            return {}
        
        stats = {
            'n_participants': len(self.behavioral_data),
            'time': {},
            'interactions': {}
        }
        
        # Time spent in each stage
        for stage in ['construct', 'reflect', 'scaffold', 'consolidate', 'revisit', 'total']:
            times = [b[f'time_{stage}'] for b in self.behavioral_data if b[f'time_{stage}'] > 0]
            if times:
                stats['time'][stage] = {
                    'mean': statistics.mean(times),
                    'median': statistics.median(times),
                    'min': min(times),
                    'max': max(times)
                }
        
        # Interaction patterns
        revisions = [b['revisions'] for b in self.behavioral_data]
        feedback_requests = [b['feedback_requests'] for b in self.behavioral_data]
        concepts_explored = [b['concepts_explored'] for b in self.behavioral_data]
        
        stats['interactions']['revisions'] = {
            'mean': statistics.mean(revisions) if revisions else 0,
            'total': sum(revisions)
        }
        stats['interactions']['feedback_requests'] = {
            'mean': statistics.mean(feedback_requests) if feedback_requests else 0,
            'total': sum(feedback_requests)
        }
        stats['interactions']['concepts_explored'] = {
            'mean': statistics.mean(concepts_explored) if concepts_explored else 0,
            'total': sum(concepts_explored)
        }
        
        return stats
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        report = []
        report.append("# Pilot Study Analysis Report")
        report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Participants:** {len(self.responses)}")
        report.append("")
        
        # Section statistics
        report.append("## Quantitative Results")
        report.append("")
        
        stats = self.calculate_statistics()
        
        report.append("### Section A: Usability")
        report.append(f"- **N responses:** {stats['A']['n']}")
        report.append(f"- **Mean score:** {stats['A']['mean']:.2f} / 5.0")
        report.append(f"- **Median:** {stats['A']['median']:.1f}")
        report.append(f"- **Std Dev:** {stats['A']['stdev']:.2f}")
        report.append(f"- **Range:** {stats['A']['min']} - {stats['A']['max']}")
        report.append("")
        
        report.append("### Section B: Learning Experience")
        report.append(f"- **N responses:** {stats['B']['n']}")
        report.append(f"- **Mean score:** {stats['B']['mean']:.2f} / 5.0")
        report.append(f"- **Median:** {stats['B']['median']:.1f}")
        report.append(f"- **Std Dev:** {stats['B']['stdev']:.2f}")
        report.append(f"- **Range:** {stats['B']['min']} - {stats['B']['max']}")
        report.append("")
        
        report.append("### Section C: Epistemic Agency")
        report.append(f"- **N responses:** {stats['C']['n']}")
        report.append(f"- **Mean score:** {stats['C']['mean']:.2f} / 5.0")
        report.append(f"- **Median:** {stats['C']['median']:.1f}")
        report.append(f"- **Std Dev:** {stats['C']['stdev']:.2f}")
        report.append(f"- **Range:** {stats['C']['min']} - {stats['C']['max']}")
        report.append("")
        
        # Behavioral statistics
        report.append("## Behavioral Observations")
        report.append("")
        
        behavioral_stats = self.calculate_behavioral_stats()
        
        if behavioral_stats:
            report.append("### Time Spent (minutes)")
            for stage, times in behavioral_stats['time'].items():
                report.append(f"- **{stage.capitalize()}:** Mean {times['mean']:.1f}, Median {times['median']:.1f}, Range {times['min']}-{times['max']}")
            report.append("")
            
            report.append("### Interaction Patterns")
            report.append(f"- **Revisions:** Mean {behavioral_stats['interactions']['revisions']['mean']:.1f}, Total {behavioral_stats['interactions']['revisions']['total']}")
            report.append(f"- **Feedback requests:** Mean {behavioral_stats['interactions']['feedback_requests']['mean']:.1f}, Total {behavioral_stats['interactions']['feedback_requests']['total']}")
            report.append(f"- **Concepts explored:** Mean {behavioral_stats['interactions']['concepts_explored']['mean']:.1f}, Total {behavioral_stats['interactions']['concepts_explored']['total']}")
            report.append("")
        
        # Open-ended responses
        report.append("## Qualitative Feedback")
        report.append("")
        
        for i, open_resp in enumerate(self.open_responses, 1):
            report.append(f"### Participant {i}")
            for q_num, response_text in open_resp.items():
                question_map = {
                    'q14': 'Most helpful part',
                    'q15': 'Least helpful / confusing',
                    'q16': 'Unnecessary stages',
                    'q17': 'Comparison to other learning methods',
                    'q18': 'Suggested improvements'
                }
                question = question_map.get(q_num, q_num)
                report.append(f"**{question}:**")
                report.append(f"> {response_text}")
                report.append("")
        
        # Success metrics
        report.append("## Success Metrics")
        report.append("")
        
        if stats['A']['n'] > 0:
            usability_pass = stats['A']['mean'] >= 3.5
            report.append(f"- **Usability (≥3.5/5.0):** {'✅ PASS' if usability_pass else '❌ FAIL'} ({stats['A']['mean']:.2f})")
        
        if stats['B']['n'] > 0:
            learning_pass = stats['B']['mean'] >= 3.5
            report.append(f"- **Learning Value (≥3.5/5.0):** {'✅ PASS' if learning_pass else '❌ FAIL'} ({stats['B']['mean']:.2f})")
        
        if stats['C']['n'] > 0:
            agency_pass = stats['C']['mean'] >= 4.0
            report.append(f"- **Epistemic Agency (≥4.0/5.0):** {'✅ PASS' if agency_pass else '❌ FAIL'} ({stats['C']['mean']:.2f})")
        
        report.append("")
        
        return "\n".join(report)
    
    def export_results(self):
        """Export results to JSON and Markdown"""
        # Export JSON
        results = {
            'timestamp': datetime.now().isoformat(),
            'n_participants': len(self.responses),
            'section_statistics': self.calculate_statistics(),
            'behavioral_statistics': self.calculate_behavioral_stats(),
            'individual_responses': self.responses
        }
        
        json_path = OUTPUT_DIR / "analysis-results.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✓ Exported JSON results to {json_path}")
        
        # Export Markdown report
        report = self.generate_report()
        md_path = OUTPUT_DIR / "analysis-report.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✓ Exported Markdown report to {md_path}")
        
        return results


class InteractionLogAnalyzer:
    """Analyzes interaction logs from wiki_data.json files"""
    
    def __init__(self):
        self.logs = []
    
    def load_logs(self, participant_id):
        """Load interaction logs for a participant"""
        log_path = INTERACTION_LOGS_DIR / f"{participant_id}.json"
        if not log_path.exists():
            print(f"Warning: {log_path} does not exist")
            return
        
        with open(log_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.logs.append({
            'participant_id': participant_id,
            'data': data
        })
    
    def analyze_concepts(self):
        """Analyze which concepts were explored"""
        concept_counts = defaultdict(int)
        
        for log in self.logs:
            for concept in log['data'].keys():
                concept_counts[concept] += 1
        
        return dict(concept_counts)
    
    def analyze_revisions(self):
        """Analyze revision patterns"""
        revision_counts = []
        
        for log in self.logs:
            for concept, entry in log['data'].items():
                if 'revisions' in entry:
                    revision_counts.append(len(entry['revisions']))
        
        if revision_counts:
            return {
                'mean': statistics.mean(revision_counts),
                'median': statistics.median(revision_counts),
                'total': sum(revision_counts)
            }
        return None


def create_sample_feedback_form():
    """Create a sample feedback form for testing"""
    sample = {
        "participant_id": "P001",
        "date": "2026-09-10",
        "concept": "overfitting",
        "session_number": 1,
        "q1": 4,  # Usability: navigation
        "q2": 5,  # Usability: instructions
        "q3": 4,  # Usability: intuitive cycle
        "q4": 4,  # Usability: helpful sidebar
        "q5": 5,  # Learning: writing explanation
        "q6": 4,  # Learning: reflection questions
        "q7": 4,  # Learning: AI feedback
        "q8": 5,  # Learning: consolidation task
        "q9": 3,  # Learning: revisiting concepts
        "q10": 5,  # Agency: in control
        "q11": 4,  # Agency: AI guided without taking over
        "q12": 5,  # Agency: thinking valued
        "q13": 2,  # Agency: prefer prompts over direct answers (low = prefer prompts)
        "q14": "The reflection questions made me think more deeply about what I actually understood.",
        "q15": "The consolidation task was a bit confusing at first, but helpful once I understood it.",
        "q16": "",
        "q17": "This was much more engaging than just reading a textbook. I actually had to think about the concepts.",
        "q18": "Maybe add more examples in the consolidation stage?",
        "time_construct": 8,
        "time_reflect": 6,
        "time_scaffold": 5,
        "time_consolidate": 12,
        "time_revisit": 4,
        "time_total": 40,
        "revisions": 2,
        "feedback_requests": 3,
        "concepts_explored": 1
    }
    
    # Save sample
    FEEDBACK_FORMS_DIR.mkdir(parents=True, exist_ok=True)
    sample_path = FEEDBACK_FORMS_DIR / "sample-P001.json"
    with open(sample_path, 'w', encoding='utf-8') as f:
        json.dump(sample, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Created sample feedback form: {sample_path}")
    return sample_path


def main():
    """Main analysis pipeline"""
    print("=" * 60)
    print("AI Wiki Companion - Pilot Study Analysis")
    print("=" * 60)
    print()
    
    # Check if data exists
    if not FEEDBACK_FORMS_DIR.exists() or not list(FEEDBACK_FORMS_DIR.glob("*.json")):
        print("No feedback forms found. Creating sample data for testing...")
        create_sample_feedback_form()
        print()
    
    # Initialize analyzer
    analyzer = FeedbackAnalyzer()
    
    # Load all feedback forms
    print("Loading feedback forms...")
    analyzer.load_all_forms()
    print()
    
    if not analyzer.responses:
        print("No data to analyze. Please add feedback forms to:")
        print(f"  {FEEDBACK_FORMS_DIR}")
        return
    
    # Generate analysis
    print("Analyzing data...")
    results = analyzer.export_results()
    print()
    
    # Print summary
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print()
    print(f"Participants: {results['n_participants']}")
    print()
    
    stats = results['section_statistics']
    for section_key, section_stats in stats.items():
        print(f"{section_stats['name']}:")
        print(f"  Mean: {section_stats['mean']:.2f} / 5.0")
        print(f"  N: {section_stats['n']}")
        print()
    
    print("Results exported to:")
    print(f"  {OUTPUT_DIR / 'analysis-results.json'}")
    print(f"  {OUTPUT_DIR / 'analysis-report.md'}")
    print()


if __name__ == "__main__":
    main()
