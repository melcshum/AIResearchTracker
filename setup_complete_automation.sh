#!/bin/bash
# Complete automation setup for AI Research Tracker
# Sets up: web server (always-on) + daily paper updates

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PLIST_DIR="$HOME/Library/LaunchAgents"
mkdir -p "$PLIST_DIR"

echo "🤖 AI Research Tracker - Complete Automation Setup"
echo "=================================================="
echo ""

# Make all scripts executable
chmod +x *.sh *.py 2>/dev/null || true
echo "✅ Made scripts executable"

# Function to install a plist
install_plist() {
    local src="$1"
    local name=$(basename "$src")
    local dst="$PLIST_DIR/$name"
    local label=$(basename "$name" .plist)
    
    # Unload if exists
    if launchctl list | grep -q "$label" 2>/dev/null; then
        echo "⚠️  Unloading existing: $label"
        launchctl unload "$dst" 2>/dev/null || true
        sleep 1
    fi
    
    # Copy plist
    cp "$src" "$dst"
    
    # Load
    if launchctl load "$dst" 2>&1; then
        echo "✅ Loaded: $label"
        return 0
    else
        echo "❌ Failed to load: $label"
        return 1
    fi
}

# Install web server
echo ""
echo "📡 Installing web server (always-on)..."
if install_plist "com.ailcshum.research-tracker.server.plist"; then
    echo "   Server will auto-start on login"
    echo "   URL: http://100.64.0.17:8001"
fi

# Install daily automation
echo ""
echo "📅 Installing daily automation (6:00 AM)..."
if install_plist "com.ailcshum.research-tracker.plist"; then
    echo "   Daily paper fetch and site rebuild"
fi

# Create log files
touch automation.log server.log
echo ""
echo "✅ Log files ready"

# Verify installation
echo ""
echo "📋 Verification:"
echo "   Web server:"
if launchctl list | grep -q "com.ailcshum.research-tracker.server"; then
    echo "   ✅ Running"
    sleep 2
    if curl -s http://100.64.0.17:8001 > /dev/null 2>&1; then
        echo "   ✅ Accessible at http://100.64.0.17:8001"
    else
        echo "   ⚠️  Starting up..."
    fi
else
    echo "   ❌ Not running"
fi

echo ""
echo "   Daily automation:"
if launchctl list | grep -q "com.ailcshum.research-tracker"; then
    echo "   ✅ Installed"
else
    echo "   ❌ Not installed"
fi

echo ""
echo "=================================================="
echo "✨ Setup complete!"
echo ""
echo "📖 Management commands:"
echo "   • Check status: python3 automate.py --status"
echo "   • Manual run: ./run_automation.sh"
echo "   • View logs: tail -f automation.log"
echo "   • Server logs: tail -f server.log"
echo ""
echo "🔧 Advanced:"
echo "   • Stop server: launchctl unload ~/Library/LaunchAgents/com.ailcshum.research-tracker.server.plist"
echo "   • Stop automation: launchctl unload ~/Library/LaunchAgents/com.ailcshum.research-tracker.plist"
echo "   • Restart all: ./setup_complete_automation.sh"
echo ""
echo "🌐 Access your site at: http://100.64.0.17:8001"
