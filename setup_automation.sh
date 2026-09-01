#!/bin/bash
# Setup launchd automation for AI Research Tracker

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PLIST_NAME="com.ailcshum.research-tracker.plist"
PLIST_SRC="$SCRIPT_DIR/$PLIST_NAME"
PLIST_DST="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo "🤖 Setting up launchd automation for AI Research Tracker"
echo ""

# Make scripts executable
chmod +x automate.py fetch_arxiv.py enhance_papers.py enhance_paper_details.py generate_*.py 2>/dev/null || true
echo "✅ Made all Python scripts executable"

# Create LaunchAgents directory if needed
mkdir -p "$HOME/Library/LaunchAgents"

# Unload if already loaded
if launchctl list | grep -q "com.ailcshum.research-tracker"; then
    echo "⚠️  Unloading existing automation..."
    launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# Copy plist
cp "$PLIST_SRC" "$PLIST_DST"
echo "✅ Installed launchd plist"

# Load the agent
launchctl load "$PLIST_DST"
echo "✅ Loaded automation agent"

# Verify
echo ""
echo "📋 Status:"
launchctl list | grep research-tracker || echo "⚠️  Agent not found in launchctl"

# Create log file
touch automation.log
echo ""
echo "✅ Log file ready: automation.log"

echo ""
echo "✨ Setup complete!"
echo ""
echo "📖 Automation details:"
echo "   • Schedule: Daily at 6:00 AM"
echo "   • Plist: $PLIST_DST"
echo "   • Logs: tail -f automation.log"
echo ""
echo "🔧 Management commands:"
echo "   • Check status: python3 automate.py --status"
echo "   • Manual run: python3 automate.py"
echo "   • Stop automation: launchctl unload $PLIST_DST"
echo "   • Restart automation: launchctl load $PLIST_DST"
echo "   • View logs: tail -f automation.log"
