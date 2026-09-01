#!/usr/bin/env python3
"""
Master automation script for AI Research Tracker.
Runs the complete pipeline: fetch papers, enhance, generate data, rebuild site.
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
import json
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AutomationPipeline:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.state_file = self.base_dir / '.automation_state.json'
        
    def load_state(self):
        """Load last run state."""
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {'last_run': None, 'papers_count': 0}
    
    def save_state(self, state):
        """Save current run state."""
        state['last_run'] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def run_command(self, cmd, description):
        """Run a command and log output."""
        logger.info(f"Running: {description}")
        logger.info(f"Command: {cmd}")
        
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=self.base_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode != 0:
                logger.error(f"Command failed with return code {result.returncode}")
                logger.error(f"STDOUT: {result.stdout}")
                logger.error(f"STDERR: {result.stderr}")
                return False, result.stdout + result.stderr
            
            logger.info(f"Success: {description}")
            if result.stdout:
                logger.debug(f"Output: {result.stdout}")
            
            return True, result.stdout
            
        except subprocess.TimeoutExpired:
            logger.error(f"Command timed out: {description}")
            return False, "Timeout"
        except Exception as e:
            logger.error(f"Exception running command: {e}")
            return False, str(e)
    
    def step_fetch_papers(self):
        """Step 1: Fetch new papers from arXiv."""
        success, output = self.run_command(
            'python3 fetch_arxiv.py',
            'Fetching papers from arXiv'
        )
        
        if not success:
            return False, 0
        
        # Count new papers from output
        lines = output.split('\n')
        saved_count = 0
        for line in lines:
            if 'Saved:' in line:
                saved_count += 1
        
        logger.info(f"Fetched {saved_count} new papers")
        return True, saved_count
    
    def step_enhance_papers(self):
        """Step 2: Enhance paper detail pages."""
        success, _ = self.run_command(
            'python3 enhance_papers.py',
            'Enhancing paper pages'
        )
        return success
    
    def step_enhance_details(self):
        """Step 3: Add structured metadata to papers."""
        success, _ = self.run_command(
            'python3 enhance_paper_details.py',
            'Adding structured metadata'
        )
        return success
    
    def step_generate_data(self):
        """Step 4: Generate all data-driven pages."""
        scripts = [
            ('generate_search_data.py', 'Search data'),
            ('generate_compare_data.py', 'Compare data'),
            ('generate_notes.py', 'Notes data'),
            ('generate_authors.py', 'Authors data'),
            ('generate_statistics.py', 'Statistics data'),
            ('generate_tagcloud_data.py', 'Tag cloud data'),
            ('generate_rss.py', 'RSS feed'),
        ]
        
        for script, description in scripts:
            success, _ = self.run_command(
                f'python3 {script}',
                f'Generating {description}'
            )
            if not success:
                logger.warning(f"Failed to generate {description}, continuing...")
        
        return True
    
    def step_build_site(self):
        """Step 5: Build the Quarto site."""
        success, _ = self.run_command(
            'quarto render',
            'Building Quarto site'
        )
        return success
    
    def run_full_pipeline(self):
        """Run the complete automation pipeline."""
        logger.info("=" * 60)
        logger.info("Starting AI Research Tracker automation pipeline")
        logger.info("=" * 60)
        
        state = self.load_state()
        start_time = datetime.now()
        
        # Step 1: Fetch papers
        success, new_papers = self.step_fetch_papers()
        if not success:
            logger.error("Failed to fetch papers, aborting pipeline")
            return False
        
        # Step 2: Enhance papers
        if not self.step_enhance_papers():
            logger.warning("Paper enhancement had issues, continuing...")
        
        # Step 3: Enhance details
        if not self.step_enhance_details():
            logger.warning("Detail enhancement had issues, continuing...")
        
        # Step 4: Generate data
        if not self.step_generate_data():
            logger.warning("Data generation had issues, continuing...")
        
        # Step 5: Build site
        if not self.step_build_site():
            logger.error("Failed to build site")
            return False
        
        # Update state
        state['papers_count'] += new_papers
        state['last_run'] = datetime.now().isoformat()
        state['run_duration'] = (datetime.now() - start_time).total_seconds()
        self.save_state(state)
        
        logger.info("=" * 60)
        logger.info("Pipeline completed successfully")
        logger.info(f"New papers: {new_papers}")
        logger.info(f"Total papers: {state['papers_count']}")
        logger.info(f"Duration: {state['run_duration']:.1f}s")
        logger.info("=" * 60)
        
        return True

def main():
    """Main entry point."""
    base_dir = Path(__file__).parent
    pipeline = AutomationPipeline(base_dir)
    
    # Parse arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--status':
            state = pipeline.load_state()
            print(json.dumps(state, indent=2))
            return
        elif sys.argv[1] == '--help':
            print("Usage: automate.py [OPTIONS]")
            print("\nOptions:")
            print("  --status    Show last run status")
            print("  --help      Show this help message")
            print("\nNo options: Run the full automation pipeline")
            return
    
    # Run full pipeline
    success = pipeline.run_full_pipeline()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
