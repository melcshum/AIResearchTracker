#!/bin/bash
# Master automation script
# Runs daily paper fetch, enhancement, and site rebuild

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

LOGFILE="$SCRIPT_DIR/automation.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting automation..." >> "$LOGFILE"

# Ensure server is running
if ! curl -s http://100.64.0.17:8001 > /dev/null 2>&1; then
    echo "[$DATE] Server not running, starting..." >> "$LOGFILE"
    ./start_server.sh >> "$LOGFILE" 2>&1
fi

# Run the pipeline
echo "[$DATE] Running paper pipeline..." >> "$LOGFILE"
python3 automate.py >> "$LOGFILE" 2>&1

DATE=$(date '+%Y-%m-%d %H:%M:%S')
echo "[$DATE] Automation complete" >> "$LOGFILE"
echo "" >> "$LOGFILE"
