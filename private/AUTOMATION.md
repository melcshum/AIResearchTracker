# AI Research Tracker - Automation Guide

## Overview

The automation system runs the complete pipeline: fetch papers → enhance → generate data → build site.

## Quick Start

### Manual Run
```bash
cd /Users/ailcshum/workspace/research-notes
python3 automate.py
```

### Check Status
```bash
python3 automate.py --status
```

## Automated Scheduling

### Option 1: Manual Script (Recommended for macOS)

Run the automation anytime:
```bash
cd /Users/ailcshum/workspace/research-notes
./run_automation.sh
```

### Option 2: macOS Shortcuts App

1. Open **Shortcuts** app
2. Create new shortcut: "Run Research Automation"
3. Add action: **Run Shell Script**
4. Paste:
```bash
cd /Users/ailcshum/workspace/research-notes && ./run_automation.sh
```
5. Save and add to **Today Widget** or **Menu Bar**

### Option 3: Cron Job (if enabled)

1. **Set up cron job** (runs daily at 6 AM):
```bash
crontab -e
```

Add this line:
```cron
0 6 * * * cd /Users/ailcshum/workspace/research-notes && python3 automate.py >> automation.log 2>&1
```

2. **Verify cron is running**:
```bash
crontab -l
```

### Option 4: launchd (macOS native)

1. **Create plist file**:
```bash
mkdir -p ~/Library/LaunchAgents
nano ~/Library/LaunchAgents/com.research-tracker.automation.plist
```

2. **Add content from `com.ailcshum.research-tracker.plist`**

3. **Load the agent**:
```bash
launchctl bootstrap gui $HOME/Library/LaunchAgents/com.ailcshum.research-tracker.plist
```

**Note**: launchd GUI domain may require additional permissions on newer macOS versions.

## Logs

All automation runs are logged to `automation.log`:
```bash
tail -f automation.log
```

## Pipeline Steps

1. **Fetch Papers** - Searches arXiv for new papers in focus areas
2. **Enhance Papers** - Extracts key contributions and finds related papers
3. **Enhance Details** - Adds reading time, methodology, limitations, citations
4. **Generate Data** - Updates search, compare, notes, authors, statistics, tag cloud, RSS
5. **Build Site** - Renders the Quarto website

## Troubleshooting

### Check if automation ran
```bash
python3 automate.py --status
```

### View recent logs
```bash
tail -100 automation.log
```

### Test pipeline manually
```bash
python3 automate.py
```

### Check cron logs
```bash
grep CRON /var/log/system.log
```

## Customization

### Change schedule
Edit the cron job or LaunchAgent plist to change the time.

### Change focus areas
Edit `fetch_arxiv.py` and modify the `FOCUS_AREAS` dictionary.

### Add new data generators
1. Create `generate_yourdata.py`
2. Add to the `scripts` list in `automate.py` step 4

## Files

- `automate.py` - Master automation script
- `automation.log` - Execution logs
- `.automation_state.json` - Last run state
- `fetch_arxiv.py` - Paper fetcher
- `enhance_papers.py` - Paper enhancement
- `enhance_paper_details.py` - Detail enhancement
- `generate_*.py` - Data generators
