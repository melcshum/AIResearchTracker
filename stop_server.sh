#!/bin/bash
# Stop web server
# Usage: ./stop_server.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PIDFILE="$SCRIPT_DIR/.server.pid"

if [ ! -f "$PIDFILE" ]; then
    echo "⚠️  Server not running (no PID file)"
    exit 0
fi

PID=$(cat "$PIDFILE")

if ps -p "$PID" > /dev/null 2>&1; then
    echo "🛑 Stopping server (PID $PID)..."
    kill "$PID"
    rm -f "$PIDFILE"
    echo "✅ Server stopped"
else
    echo "⚠️  Server not running (stale PID file)"
    rm -f "$PIDFILE"
fi
