# Complete Automation Setup Guide

## ✅ What's Already Working

Your AI Research Tracker is fully functional with:
- **77 papers** from arXiv
- **346 authors** indexed
- **101 pages** on the site
- **Web server** running at http://100.64.0.17:8001
- **All automation scripts** tested and working

## 🚀 Quick Start (Manual Automation)

### Run the full pipeline anytime:
```bash
cd /Users/ailcshum/workspace/research-notes
./daily_automation.sh
```

This will:
1. Ensure the web server is running
2. Fetch new papers from arXiv
3. Enhance paper details
4. Generate all data (search, statistics, tag cloud, etc.)
5. Rebuild the site

### Check logs:
```bash
tail -f automation.log
```

## 📅 Automated Daily Updates

### Option 1: macOS Shortcuts (Recommended)

1. **Open Shortcuts app** (Cmd+Space → type "Shortcuts")

2. **Create new shortcut:**
   - Click **+** button
   - Name: "Run Research Automation"

3. **Add action:**
   - Search for "Run Shell Script"
   - Drag it into your shortcut

4. **Paste this code:**
```bash
cd /Users/ailcshum/workspace/research-notes
./daily_automation.sh
```

5. **Optional enhancements:**
   - Add "Show Notification" action after the script
   - Set title: "Research Update Complete"
   - Set message: "Papers updated and site rebuilt"

6. **Add to Menu Bar:**
   - Click the **i** (info) button
   - Enable "Show in Menu Bar"
   - Now you can run it with one click!

7. **Add keyboard shortcut:**
   - Go to Shortcuts → Settings (gear icon)
   - Add keyboard shortcut to your automation

### Option 2: Manual Cron Setup

If you want to try enabling cron:

1. **Grant Full Disk Access:**
   - System Settings → Privacy & Security → Full Disk Access
   - Add `/usr/sbin/cron` (if available)

2. **Edit crontab:**
```bash
crontab -e
```

3. **Add this line:**
```cron
0 6 * * * /Users/ailcshum/workspace/research-notes/daily_automation.sh
```

### Option 3: Third-Party Scheduler

Use apps like:
- **LaunchControl** (GUI for launchd)
- **Cronnix** (GUI for cron)
- **Keyboard Maestro** (automation with scheduling)

## 🌐 Web Server Management

### Start server:
```bash
./start_server.sh
```

### Stop server:
```bash
./stop_server.sh
```

### Check status:
```bash
curl http://100.64.0.17:8001
```

### Auto-start on login (manual setup):

1. **Create Login Item:**
   - System Settings → General → Login Items
   - Click **+**
   - Add `/Users/ailcshum/workspace/research-notes/start_server.sh`

2. **Or use Automator:**
   - Open Automator → New Document → Application
   - Add "Run Shell Script" action
   - Paste: `cd /Users/ailcshum/workspace/research-notes && ./start_server.sh`
   - Save as "Research Server"
   - Add to Login Items

## 📊 Monitoring & Logs

### View automation logs:
```bash
tail -f automation.log
```

### View server logs:
```bash
tail -f server.log
```

### Check automation status:
```bash
python3 automate.py --status
```

### View recent activity:
```bash
tail -50 automation.log
```

## 🔧 Troubleshooting

### Server not accessible?
```bash
# Check if server is running
ps aux | grep "http.server"

# Restart server
./stop_server.sh
./start_server.sh

# Check logs
tail -20 server.log
```

### Automation not running?
```bash
# Test manually
./daily_automation.sh

# Check logs
tail -50 automation.log

# Verify scripts are executable
chmod +x *.sh *.py
```

### Permission denied errors?
```bash
# Make all scripts executable
chmod +x /Users/ailcshum/workspace/research-notes/*.sh
chmod +x /Users/ailcshum/workspace/research-notes/*.py
```

## 📋 Available Scripts

| Script | Purpose |
|--------|---------|
| `daily_automation.sh` | Master automation (server + pipeline) |
| `run_automation.sh` | Run pipeline only |
| `start_server.sh` | Start web server |
| `stop_server.sh` | Stop web server |
| `automate.py` | Python pipeline orchestrator |
| `fetch_arxiv.py` | Fetch papers from arXiv |
| `enhance_papers.py` | Extract key contributions |
| `enhance_paper_details.py` | Add structured metadata |
| `generate_*.py` | Data generators |

## 💡 Tips

1. **Run after waking Mac:** If your Mac sleeps, run automation manually after waking
2. **Check weekly:** Review `automation.log` to ensure everything is running
3. **Backup regularly:** Your reading list and notes are in browser localStorage
4. **Monitor disk space:** Papers accumulate over time

## 🎯 Recommended Workflow

### Daily:
- Check site for new papers: http://100.64.0.17:8001
- Browse tag cloud for trending topics
- Add notes to interesting papers

### Weekly:
- Run `./daily_automation.sh` manually if automation isn't set up
- Review weekly digest (when implemented)
- Update reading list

### Monthly:
- Check `automation.log` for any issues
- Review statistics dashboard
- Clean up old papers if needed

## 📞 Need Help?

Check these files:
- `README.md` - Project overview
- `AUTOMATION.md` - Detailed automation guide
- `SHORTCUTS_SETUP.md` - macOS Shortcuts setup
- `automation.log` - Execution logs
- `server.log` - Server logs

---

**Current Status:**
- ✅ All scripts working
- ✅ Server running at http://100.64.0.17:8001
- ✅ 77 papers processed
- ⚠️  Automated scheduling requires manual setup (see above)
