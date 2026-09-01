---
title: "Admin Hub"
---

<div class="role-hub admin-hub">
<div class="hub-hero">
<div class="hub-icon">🛠️</div>
<h1>Admin Hub</h1>
<p class="hub-subtitle">System management, automation, and configuration</p>
</div>

<div class="system-overview">
<h2>📊 System Overview</h2>
<div class="stats-grid">
<div class="stat-card">
<div class="stat-icon">📄</div>
<div class="stat-content">
<div class="stat-number">112</div>
<div class="stat-label">Pages</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">📚</div>
<div class="stat-content">
<div class="stat-number">77</div>
<div class="stat-label">Papers</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">👥</div>
<div class="stat-content">
<div class="stat-number">346</div>
<div class="stat-label">Authors</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">🏷️</div>
<div class="stat-content">
<div class="stat-number">4</div>
<div class="stat-label">Topics</div>
</div>
</div>
<div class="stat-card">
<div class="stat-icon">⚙️</div>
<div class="stat-content">
<div class="stat-number">Daily</div>
<div class="stat-label">Automation</div>
</div>
</div>
</div>
</div>

<div class="hub-sections">
<section class="hub-section">
<div class="section-header">
<h2>🤖 Automation & Pipeline</h2>
<span class="section-badge">Critical</span>
</div>
<p class="section-desc">Manage the automated paper fetching and processing pipeline</p>
<div class="feature-grid">
<a href="AUTOMATION.html" class="feature-card primary">
<div class="feature-icon">🔄</div>
<h3>Automation Guide</h3>
<p>Complete guide to setting up and managing the automation pipeline</p>
<div class="feature-tags">
<span class="tag">Setup</span>
<span class="tag">Cron</span>
<span class="tag">Shortcuts</span>
</div>
</a>
<a href="admin.html" class="feature-card">
<div class="feature-icon">📋</div>
<h3>Admin Dashboard</h3>
<p>System status, recent activity, and health checks</p>
<div class="feature-tags">
<span class="tag">Status</span>
<span class="tag">Logs</span>
<span class="tag">Health</span>
</div>
</a>
<div class="feature-card">
<div class="feature-icon">⚡</div>
<h3>Quick Commands</h3>
<p>Essential shell commands for daily operations</p>
<div class="feature-tags">
<span class="tag">CLI</span>
<span class="tag">Scripts</span>
</div>
<div class="command-list">
<code>./daily_automation.sh</code>
<code>./start_server.sh</code>
<code>./stop_server.sh</code>
</div>
</div>
</div>
</section>

<section class="hub-section">
<div class="section-header">
<h2>⚙️ Configuration</h2>
<span class="section-badge">Settings</span>
</div>
<p class="section-desc">Configure system behavior and preferences</p>
<div class="feature-grid">
<a href="settings.html" class="feature-card primary">
<div class="feature-icon">⚙️</div>
<h3>System Settings</h3>
<p>Configure fetch frequency, sources, topics, display options, and automation</p>
<div class="feature-tags">
<span class="tag">Ingestion</span>
<span class="tag">Sources</span>
<span class="tag">Topics</span>
<span class="tag">Display</span>
</div>
</a>
<a href="AGENTS.html" class="feature-card">
<div class="feature-icon">📖</div>
<h3>Agent Documentation</h3>
<p>Complete project documentation and technical specifications</p>
<div class="feature-tags">
<span class="tag">Technical</span>
<span class="tag">Architecture</span>
</div>
</a>
<a href="DESIGN_GUIDE.html" class="feature-card">
<div class="feature-icon">🎨</div>
<h3>Design System</h3>
<p>UI/UX design guidelines, components, and styling</p>
<div class="feature-tags">
<span class="tag">UI</span>
<span class="tag">CSS</span>
<span class="tag">Components</span>
</div>
</a>
</div>
</section>

<section class="hub-section">
<div class="section-header">
<h2>📊 Monitoring & Analytics</h2>
<span class="section-badge">Operations</span>
</div>
<p class="section-desc">Monitor system health and usage patterns</p>
<div class="feature-grid">
<a href="statistics.html" class="feature-card primary">
<div class="feature-icon">📈</div>
<h3>Research Statistics</h3>
<p>Paper distribution, author metrics, and topic analysis</p>
<div class="feature-tags">
<span class="tag">Charts</span>
<span class="tag">Metrics</span>
</div>
</a>
<a href="tag-cloud.html" class="feature-card">
<div class="feature-icon">🏷️</div>
<h3>Tag Cloud</h3>
<p>Visual overview of trending concepts and keywords</p>
<div class="feature-tags">
<span class="tag">Visual</span>
<span class="tag">Trends</span>
</div>
</a>
<div class="feature-card">
<div class="feature-icon">📝</div>
<h3>System Logs</h3>
<p>View automation logs and error reports</p>
<div class="feature-tags">
<span class="tag">Logs</span>
<span class="tag">Debug</span>
</div>
<div class="command-list">
<code>tail -f automation.log</code>
<code>tail -f server.log</code>
</div>
</div>
</div>
</section>

<section class="hub-section">
<div class="section-header">
<h2>🔧 Maintenance</h2>
<span class="section-badge">Tasks</span>
</div>
<p class="section-desc">Routine maintenance and troubleshooting</p>
<div class="feature-grid">
<div class="feature-card">
<div class="feature-icon">🗄️</div>
<h3>Data Management</h3>
<p>Backup, restore, and manage paper database</p>
<div class="feature-tags">
<span class="tag">Backup</span>
<span class="tag">Export</span>
<span class="tag">Import</span>
</div>
<div class="command-list">
<code># Backup papers</code>
<code>tar -czf papers-backup.tar.gz papers/</code>
<code># Restore</code>
<code>tar -xzf papers-backup.tar.gz</code>
</div>
</div>
<div class="feature-card">
<div class="feature-icon">🧹</div>
<h3>Cleanup Tasks</h3>
<p>Remove old data, optimize storage, clear caches</p>
<div class="feature-tags">
<span class="tag">Cleanup</span>
<span class="tag">Optimize</span>
</div>
<div class="command-list">
<code># Clear Quarto cache</code>
<code>rm -rf _site/</code>
<code>quarto render</code>
</div>
</div>
<div class="feature-card">
<div class="feature-icon">🔍</div>
<h3>Troubleshooting</h3>
<p>Common issues and solutions</p>
<div class="feature-tags">
<span class="tag">Help</span>
<span class="tag">FAQ</span>
</div>
<ul class="issue-list">
<li><strong>Server won't start:</strong> Check port 8001 availability</li>
<li><strong>Papers not fetching:</strong> Verify arXiv API access</li>
<li><strong>Site not rendering:</strong> Run <code>quarto render</code> manually</li>
</ul>
</div>
</div>
</section>

<section class="hub-section">
<div class="section-header">
<h2>📚 Documentation</h2>
<span class="section-badge">Reference</span>
</div>
<p class="section-desc">Technical documentation and guides</p>
<div class="feature-grid">
<a href="COMPLETE_AUTOMATION_GUIDE.html" class="feature-card">
<div class="feature-icon">📘</div>
<h3>Complete Automation Guide</h3>
<p>Detailed automation setup and configuration</p>
<div class="feature-tags">
<span class="tag">Guide</span>
<span class="tag">Step-by-step</span>
</div>
</a>
<a href="SHORTCUTS_SETUP.html" class="feature-card">
<div class="feature-icon">⌨️</div>
<h3>Shortcuts Setup</h3>
<p>Configure macOS Shortcuts for one-click automation</p>
<div class="feature-tags">
<span class="tag">macOS</span>
<span class="tag">Shortcuts</span>
</div>
</a>
<a href="UI_ENHANCEMENTS.html" class="feature-card">
<div class="feature-icon">✨</div>
<h3>UI Enhancements</h3>
<p>Recent UI/UX improvements and design changes</p>
<div class="feature-tags">
<span class="tag">Changelog</span>
<span class="tag">Design</span>
</div>
</a>
<a href="requirements.html" class="feature-card">
<div class="feature-icon">📋</div>
<h3>User Requirements</h3>
<p>System requirements and feature specifications</p>
<div class="feature-tags">
<span class="tag">Specs</span>
<span class="tag">Roadmap</span>
</div>
</a>
</div>
</section>

<section class="hub-section">
<div class="section-header">
<h2>🔐 Server Management</h2>
<span class="section-badge">Infrastructure</span>
</div>
<p class="section-desc">Web server configuration and access</p>
<div class="feature-grid">
<div class="feature-card primary">
<div class="feature-icon">🌐</div>
<h3>Server Status</h3>
<p>Current server configuration and access details</p>
<div class="server-info">
<div class="info-row">
<span class="label">URL:</span>
<code>http://100.64.0.17:8001</code>
</div>
<div class="info-row">
<span class="label">Bind:</span>
<code>Tailscale IP</code>
</div>
<div class="info-row">
<span class="label">Port:</span>
<code>8001</code>
</div>
<div class="info-row">
<span class="label">Status:</span>
<span class="status-badge active">Active</span>
</div>
</div>
</div>
<div class="feature-card">
<div class="feature-icon">🚀</div>
<h3>Server Control</h3>
<p>Start, stop, and restart the web server</p>
<div class="command-list">
<code># Start server</code>
<code>./start_server.sh</code>
<code># Stop server</code>
<code>./stop_server.sh</code>
<code># Check status</code>
<code>lsof -i :8001</code>
</div>
</div>
<div class="feature-card">
<div class="feature-icon">🔒</div>
<h3>Security</h3>
<p>Access control and security considerations</p>
<div class="feature-tags">
<span class="tag">Tailscale</span>
<span class="tag">Local</span>
</div>
<ul class="issue-list">
<li>Server bound to Tailscale IP (not public)</li>
<li>HTTP only (consider HTTPS for production)</li>
<li>No authentication (local network only)</li>
</ul>
</div>
</div>
</section>
</div>

<div class="quick-actions">
<h2>⚡ Admin Quick Actions</h2>
<div class="action-grid">
<button class="action-btn" onclick="window.location.href='settings.html'">
<span class="action-icon">⚙️</span>
<span>Settings</span>
</button>
<button class="action-btn" onclick="window.location.href='AUTOMATION.html'">
<span class="action-icon">🔄</span>
<span>Automation</span>
</button>
<button class="action-btn" onclick="window.location.href='admin.html'">
<span class="action-icon">📋</span>
<span>Dashboard</span>
</button>
<button class="action-btn" onclick="window.location.href='AGENTS.html'">
<span class="action-icon">📖</span>
<span>Docs</span>
</button>
</div>
</div>

<div class="admin-tips">
<h2>💡 Admin Tips</h2>
<div class="tips-grid">
<div class="tip-card">
<h4>🔄 Daily Automation</h4>
<p>Set up <code>daily_automation.sh</code> to run automatically via cron or macOS Shortcuts. This fetches new papers, enhances metadata, and rebuilds the site.</p>
</div>
<div class="tip-card">
<h4>📊 Monitor Logs</h4>
<p>Regularly check <code>automation.log</code> and <code>server.log</code> for errors. Use <code>tail -f</code> for real-time monitoring during troubleshooting.</p>
</div>
<div class="tip-card">
<h4>💾 Backup Regularly</h4>
<p>The paper database is in <code>papers/</code> directory. Back up regularly with <code>tar -czf</code>. User data (notes, reading lists) is in browser localStorage.</p>
</div>
<div class="tip-card">
<h4>🔧 Test Changes</h4>
<p>After modifying configuration or scripts, test the full pipeline: fetch → enhance → generate → render. Check logs for errors.</p>
</div>
</div>
</div>
</div>

<style>
.admin-hub .hub-hero {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.admin-hub .step-number,
.admin-hub .section-badge,
.admin-hub .action-btn {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.admin-hub .feature-card.primary {
  border-color: #f5576c;
}

.admin-hub .feature-card:hover {
  border-color: #f5576c;
}

.admin-hub .tag {
  color: #f5576c;
}

.admin-hub .tip-card {
  border-left-color: #f5576c;
}

.system-overview {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 40px;
}

.system-overview h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 20px;
  background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
  border-radius: 12px;
  border: 2px solid #f5576c;
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(245, 87, 108, 0.2);
}

.stat-icon {
  font-size: 2.5rem;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #f5576c;
  line-height: 1;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  margin-top: 5px;
}

.command-list {
  margin-top: 15px;
  padding: 12px;
  background: #2d3748;
  border-radius: 6px;
  font-family: 'Courier New', monospace;
  font-size: 0.85rem;
  color: #e2e8f0;
  overflow-x: auto;
}

.command-list code {
  display: block;
  margin: 4px 0;
  color: #68d391;
}

.issue-list {
  margin-top: 15px;
  padding-left: 20px;
  color: #666;
  font-size: 0.9rem;
  line-height: 1.8;
}

.issue-list li {
  margin: 8px 0;
}

.issue-list strong {
  color: #2c3e50;
}

.server-info {
  margin-top: 15px;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid #e0e0e0;
}

.info-row:last-child {
  border-bottom: none;
}

.info-row .label {
  font-weight: 600;
  color: #2c3e50;
}

.info-row code {
  padding: 4px 8px;
  background: #2d3748;
  color: #68d391;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  font-size: 0.85rem;
}

.status-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 600;
}

.status-badge.active {
  background: #48bb78;
  color: white;
}

.status-badge.inactive {
  background: #f56565;
  color: white;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
