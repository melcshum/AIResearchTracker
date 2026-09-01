# macOS Shortcuts Setup Guide

## Quick Setup (2 minutes)

### Step 1: Open Shortcuts App
1. Press `Cmd + Space` to open Spotlight
2. Type "Shortcuts" and press Enter

### Step 2: Create New Shortcut
1. Click the **+** button (top right)
2. Name it: **"Run Research Automation"**

### Step 3: Add Run Shell Script Action
1. In the search bar (right panel), type "shell"
2. Drag **"Run Shell Script"** into your shortcut
3. The action will appear with default text

### Step 4: Configure the Script
Replace the default script with:
```bash
cd /Users/ailcshum/workspace/research-notes
./run_automation.sh
```

### Step 5: Customize (Optional)
- **Show in Share Sheet**: Enable to run from any app's share menu
- **Ask Before Running**: Disable to run immediately
- **Icon**: Click the icon to choose a custom icon (e.g., 🤖 robot)

### Step 6: Add to Menu Bar (Optional)
1. Click the **i** (info) button on your shortcut
2. Enable **"Show in Menu Bar"**
3. Now you can run it from the top menu bar anytime

## Usage

### From Shortcuts App
1. Open Shortcuts app
2. Click "Run Research Automation"
3. Watch it run in real-time

### From Menu Bar
1. Click the Shortcuts icon in menu bar
2. Select "Run Research Automation"

### From Siri
Say: **"Hey Siri, run Research Automation"**

### From Today Widget
1. Swipe right to Today view
2. Add Shortcuts widget
3. Pin "Run Research Automation"

## Advanced: Add Notifications

To get notified when automation completes:

1. Add **"Show Notification"** action after "Run Shell Script"
2. Configure:
   - **Title**: "Research Automation Complete"
   - **Message**: "Papers updated and site rebuilt"

## Advanced: Save Logs

To save automation output to a file:

```bash
cd /Users/ailcshum/workspace/research-notes
./run_automation.sh 2>&1 | tee ~/Library/Logs/research-automation-$(date +%Y%m%d).log
```

## Troubleshooting

### "Permission Denied" Error
Make scripts executable:
```bash
cd /Users/ailcshum/workspace/research-notes
chmod +x *.sh
```

### "Command Not Found"
Shortcuts may not have your PATH. Use full paths:
```bash
cd /Users/ailcshum/workspace/research-notes
/usr/local/bin/python3 automate.py
```

### Shortcuts App Not Found
- macOS 12.0+ (Monterey) required
- Download from Mac App Store if missing

## Tips

1. **Test First**: Run the shortcut manually before relying on it
2. **Check Logs**: Always verify `automation.log` after running
3. **Backup**: Export shortcuts regularly (File → Export)
4. **Share**: Export as `.shortcut` file to share with others

## Example: Automated Daily Run

For truly automated daily runs (no manual trigger):

### Option A: Use Cron (if enabled)
```bash
crontab -e
```
Add:
```cron
0 6 * * * cd /Users/ailcshum/workspace/research-notes && ./run_automation.sh
```

### Option B: Use launchd
See `AUTOMATION.md` for launchd setup instructions.

## Keyboard Shortcut

To run from keyboard:
1. Open Shortcuts app
2. Go to Settings (gear icon)
3. Add keyboard shortcut to "Run Research Automation"

---

**Need Help?** Check `AUTOMATION.md` for more options.
