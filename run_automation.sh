#!/bin/bash
# Simple automation: Run pipeline and log results
# Can be triggered manually, via shortcut, or scheduled

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🤖 AI Research Tracker - Automation"
echo "Started at: $(date)"
echo ""

# Run the pipeline
python3 automate.py

echo ""
echo "Completed at: $(date)"
echo "Check logs: tail -f automation.log"
