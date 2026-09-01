#!/bin/bash
# Start web server in background
# Usage: ./start_server.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PORT=8001
BIND="100.64.0.17"
PIDFILE="$SCRIPT_DIR/.server.pid"
LOGFILE="$SCRIPT_DIR/server.log"

# Check if already running
if [ -f "$PIDFILE" ]; then
    PID=$(cat "$PIDFILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "✅ Server already running (PID $PID)"
        echo "   URL: http://$BIND:$PORT"
        exit 0
    else
        rm -f "$PIDFILE"
    fi
fi

# Start server
echo "🚀 Starting web server..."
nohup python3 -m http.server $PORT --bind $BIND > "$LOGFILE" 2>&1 &
echo $! > "$PIDFILE"

sleep 2

# Verify
if curl -s "http://$BIND:$PORT" > /dev/null 2>&1; then
    echo "✅ Server started successfully"
    echo "   URL: http://$BIND:$PORT"
    echo "   PID: $(cat $PIDFILE)"
    echo "   Logs: tail -f $LOGFILE"
else
    echo "⚠️  Server starting..."
    echo "   Check logs: tail -f $LOGFILE"
fi
