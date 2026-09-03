---
title: "System Health Dashboard"
---

<div class="health-container">

<div class="health-hero">
<div class="hero-icon">📊</div>
<h1>System Health Dashboard</h1>
<p class="hero-subtitle">Real-time monitoring of automation pipeline and system status</p>
</div>

<!-- Quick Stats -->
<div class="stats-grid">
<div class="stat-card">
<div class="stat-icon">📥</div>
<div class="stat-content">
<div class="stat-label">Papers Fetched</div>
<div class="stat-value" id="papersFetched">77</div>
<div class="stat-change">+34 this week</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">⚡</div>
<div class="stat-content">
<div class="stat-label">Pipeline Duration</div>
<div class="stat-value" id="pipelineDuration">58s</div>
<div class="stat-change">Target: <60s</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">🕐</div>
<div class="stat-content">
<div class="stat-label">Last Run</div>
<div class="stat-value" id="lastRun">Just now</div>
<div class="stat-change">Status: Success</div>
</div>
</div>

<div class="stat-card">
<div class="stat-icon">📄</div>
<div class="stat-content">
<div class="stat-label">Pages Rendered</div>
<div class="stat-value" id="pagesRendered">124</div>
<div class="stat-change">All successful</div>
</div>
</div>
</div>

<!-- Pipeline Status -->
<div class="section-card">
<h2>🔄 Automation Pipeline Status</h2>
<div class="pipeline-stages">
<div class="stage" id="stage-fetch">
<div class="stage-icon">📥</div>
<div class="stage-name">Fetch</div>
<div class="stage-status success">✓ Complete</div>
<div class="stage-time">30s</div>
<div class="stage-detail">34 papers from arXiv</div>
</div>

<div class="stage-connector">→</div>

<div class="stage" id="stage-enhance">
<div class="stage-icon">✨</div>
<div class="stage-name">Enhance</div>
<div class="stage-status success">✓ Complete</div>
<div class="stage-time">15s</div>
<div class="stage-detail">77 papers processed</div>
</div>

<div class="stage-connector">→</div>

<div class="stage" id="stage-generate">
<div class="stage-icon">🔧</div>
<div class="stage-name">Generate</div>
<div class="stage-status success">✓ Complete</div>
<div class="stage-time">10s</div>
<div class="stage-detail">6 data pages</div>
</div>

<div class="stage-connector">→</div>

<div class="stage" id="stage-build">
<div class="stage-icon">🏗️</div>
<div class="stage-name">Build</div>
<div class="stage-status success">✓ Complete</div>
<div class="stage-time">3s</div>
<div class="stage-detail">124 pages rendered</div>
</div>
</div>
</div>

<!-- Performance Metrics -->
<div class="metrics-grid">
<div class="section-card">
<h2>⚡ Runtime Performance</h2>
<div class="metric-row">
<div class="metric-label">Page Load Time</div>
<div class="metric-value">
<span class="metric-bar" style="width: 10%; background: #10b981;"></span>
<span class="metric-text"><100ms</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Search Response</div>
<div class="metric-value">
<span class="metric-bar" style="width: 5%; background: #10b981;"></span>
<span class="metric-text"><50ms</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Graph Render</div>
<div class="metric-value">
<span class="metric-bar" style="width: 10%; background: #10b981;"></span>
<span class="metric-text">~100ms</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Wiki Backlinks</div>
<div class="metric-value">
<span class="metric-bar" style="width: 5%; background: #10b981;"></span>
<span class="metric-text">~50ms</span>
</div>
</div>
</div>

<div class="section-card">
<h2>📈 Scalability Headroom</h2>
<div class="metric-row">
<div class="metric-label">Search Index</div>
<div class="metric-value">
<span class="metric-bar" style="width: 11%; background: #3b82f6;"></span>
<span class="metric-text">113 / 1,000</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Graph Nodes</div>
<div class="metric-value">
<span class="metric-bar" style="width: 17%; background: #3b82f6;"></span>
<span class="metric-text">34 / 200</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Wiki Terms</div>
<div class="metric-value">
<span class="metric-bar" style="width: 23%; background: #f59e0b;"></span>
<span class="metric-text">23 / 100</span>
</div>
</div>
<div class="metric-row">
<div class="metric-label">Papers</div>
<div class="metric-value">
<span class="metric-bar" style="width: 23%; background: #3b82f6;"></span>
<span class="metric-text">77 / 300</span>
</div>
</div>
</div>
</div>

<!-- Error Log -->
<div class="section-card">
<h2>📋 Recent Activity Log</h2>
<div class="log-entries" id="activityLog">
<div class="log-entry success">
<div class="log-time">2026-09-01 14:32:15</div>
<div class="log-message">Pipeline completed successfully - 77 papers processed</div>
</div>
<div class="log-entry success">
<div class="log-time">2026-09-01 14:31:45</div>
<div class="log-message">Site rebuilt - 124 pages rendered</div>
</div>
<div class="log-entry success">
<div class="log-time">2026-09-01 14:31:35</div>
<div class="log-message">Data generation complete - 6 pages created</div>
</div>
<div class="log-entry success">
<div class="log-time">2026-09-01 14:31:20</div>
<div class="log-message">Paper enhancement complete - 77 papers</div>
</div>
<div class="log-entry success">
<div class="log-time">2026-09-01 14:30:50</div>
<div class="log-message">arXiv fetch complete - 34 new papers</div>
</div>
<div class="log-entry info">
<div class="log-time">2026-09-01 14:30:20</div>
<div class="log-message">Pipeline started</div>
</div>
</div>
</div>

<!-- Quick Actions -->
<div class="section-card">
<h2>⚡ Quick Actions</h2>
<div class="actions-grid">
<button class="action-btn primary" onclick="runPipeline()">
<span class="btn-icon">🔄</span>
<span class="btn-text">Run Pipeline Now</span>
</button>
<button class="action-btn secondary" onclick="rebuildSite()">
<span class="btn-icon">🏗️</span>
<span class="btn-text">Rebuild Site</span>
</button>
<button class="action-btn secondary" onclick="fetchPapers()">
<span class="btn-icon">📥</span>
<span class="btn-text">Fetch New Papers</span>
</button>
<button class="action-btn secondary" onclick="viewLogs()">
<span class="btn-icon">📋</span>
<span class="btn-text">View Full Logs</span>
</button>
</div>
</div>

<!-- System Info -->
<div class="section-card">
<h2>ℹ️ System Information</h2>
<div class="info-grid">
<div class="info-item">
<div class="info-label">Server Status</div>
<div class="info-value">
<span class="status-badge online">● Online</span>
</div>
</div>
<div class="info-item">
<div class="info-label">Server URL</div>
<div class="info-value">http://100.64.0.17:8001</div>
</div>
<div class="info-item">
<div class="info-label">Python Version</div>
<div class="info-value">3.9.6</div>
</div>
<div class="info-item">
<div class="info-label">Quarto Version</div>
<div class="info-value">1.10.18</div>
</div>
<div class="info-item">
<div class="info-label">OS</div>
<div class="info-value">macOS (M3 Ultra)</div>
</div>
<div class="info-item">
<div class="info-label">Total Scripts</div>
<div class="info-value">15 Python + 3 Shell</div>
</div>
</div>
</div>

</div>

<style>
.health-container {
max-width: 1400px;
margin: 0 auto;
padding: 2rem;
}

.health-hero {
text-align: center;
padding: 3rem 2rem;
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
border-radius: 16px;
color: white;
margin-bottom: 2rem;
}

.hero-icon {
font-size: 4rem;
margin-bottom: 1rem;
}

.health-hero h1 {
font-size: 2.5rem;
margin: 0 0 0.5rem 0;
}

.hero-subtitle {
font-size: 1.1rem;
opacity: 0.95;
margin: 0;
}

.stats-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 1.5rem;
margin-bottom: 2rem;
}

.stat-card {
background: white;
border-radius: 12px;
padding: 1.5rem;
box-shadow: 0 2px 8px rgba(0,0,0,0.08);
display: flex;
align-items: center;
gap: 1rem;
transition: all 0.3s ease;
}

.stat-card:hover {
transform: translateY(-4px);
box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.stat-icon {
font-size: 2.5rem;
}

.stat-content {
flex: 1;
}

.stat-label {
font-size: 0.85rem;
color: #6b7280;
text-transform: uppercase;
letter-spacing: 0.5px;
margin-bottom: 0.25rem;
}

.stat-value {
font-size: 2rem;
font-weight: 700;
color: #1f2937;
line-height: 1;
}

.stat-change {
font-size: 0.85rem;
color: #10b981;
margin-top: 0.25rem;
}

.section-card {
background: white;
border-radius: 12px;
padding: 2rem;
box-shadow: 0 2px 8px rgba(0,0,0,0.08);
margin-bottom: 2rem;
}

.section-card h2 {
font-size: 1.5rem;
margin: 0 0 1.5rem 0;
color: #1f2937;
}

.pipeline-stages {
display: flex;
align-items: center;
justify-content: space-between;
gap: 1rem;
overflow-x: auto;
padding: 1rem 0;
}

.stage {
flex: 1;
min-width: 150px;
text-align: center;
padding: 1.5rem;
background: #f9fafb;
border-radius: 12px;
border: 2px solid #e5e7eb;
transition: all 0.3s ease;
}

.stage:hover {
border-color: #667eea;
background: #f0f4ff;
}

.stage-icon {
font-size: 2rem;
margin-bottom: 0.5rem;
}

.stage-name {
font-size: 1.1rem;
font-weight: 600;
color: #1f2937;
margin-bottom: 0.5rem;
}

.stage-status {
font-size: 0.9rem;
font-weight: 600;
margin-bottom: 0.5rem;
}

.stage-status.success {
color: #10b981;
}

.stage-time {
font-size: 0.85rem;
color: #6b7280;
margin-bottom: 0.25rem;
}

.stage-detail {
font-size: 0.8rem;
color: #9ca3af;
}

.stage-connector {
font-size: 2rem;
color: #d1d5db;
font-weight: bold;
}

.metrics-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
gap: 2rem;
margin-bottom: 2rem;
}

.metric-row {
display: flex;
align-items: center;
justify-content: space-between;
padding: 1rem 0;
border-bottom: 1px solid #e5e7eb;
}

.metric-row:last-child {
border-bottom: none;
}

.metric-label {
font-size: 0.95rem;
color: #4b5563;
font-weight: 500;
}

.metric-value {
display: flex;
align-items: center;
gap: 1rem;
flex: 1;
max-width: 300px;
margin-left: 2rem;
}

.metric-bar {
height: 8px;
border-radius: 4px;
transition: width 0.3s ease;
}

.metric-text {
font-size: 0.9rem;
font-weight: 600;
color: #1f2937;
white-space: nowrap;
}

.log-entries {
max-height: 400px;
overflow-y: auto;
}

.log-entry {
padding: 1rem;
border-left: 3px solid #e5e7eb;
margin-bottom: 0.5rem;
background: #f9fafb;
border-radius: 4px;
}

.log-entry.success {
border-left-color: #10b981;
background: #f0fdf4;
}

.log-entry.info {
border-left-color: #3b82f6;
background: #eff6ff;
}

.log-entry.error {
border-left-color: #ef4444;
background: #fef2f2;
}

.log-time {
font-size: 0.8rem;
color: #6b7280;
font-family: monospace;
margin-bottom: 0.25rem;
}

.log-message {
font-size: 0.95rem;
color: #1f2937;
}

.actions-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
gap: 1rem;
}

.action-btn {
display: flex;
align-items: center;
justify-content: center;
gap: 0.5rem;
padding: 1rem 1.5rem;
border: none;
border-radius: 8px;
font-size: 1rem;
font-weight: 600;
cursor: pointer;
transition: all 0.3s ease;
}

.action-btn.primary {
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
color: white;
}

.action-btn.primary:hover {
transform: translateY(-2px);
box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.action-btn.secondary {
background: #f3f4f6;
color: #1f2937;
}

.action-btn.secondary:hover {
background: #e5e7eb;
}

.btn-icon {
font-size: 1.2rem;
}

.info-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 1.5rem;
}

.info-item {
padding: 1rem;
background: #f9fafb;
border-radius: 8px;
}

.info-label {
font-size: 0.85rem;
color: #6b7280;
text-transform: uppercase;
letter-spacing: 0.5px;
margin-bottom: 0.5rem;
}

.info-value {
font-size: 1rem;
font-weight: 600;
color: #1f2937;
}

.status-badge {
display: inline-flex;
align-items: center;
gap: 0.5rem;
padding: 0.25rem 0.75rem;
border-radius: 12px;
font-size: 0.9rem;
font-weight: 600;
}

.status-badge.online {
background: #d1fae5;
color: #059669;
}

@media (max-width: 768px) {
.health-container {
  padding: 1rem;
}

.health-hero h1 {
  font-size: 1.8rem;
}

.pipeline-stages {
  flex-direction: column;
}

.stage-connector {
  transform: rotate(90deg);
}

.metrics-grid {
  grid-template-columns: 1fr;
}

.metric-value {
  max-width: 200px;
}
}
</style>

<script>
// Load system health data
function loadSystemHealth() {
// In a real implementation, this would fetch from a backend API
// For now, we'll simulate with localStorage
const lastRun = localStorage.getItem('lastPipelineRun');
if (lastRun) {
  const timeDiff = Math.floor((Date.now() - parseInt(lastRun)) / 1000 / 60);
  document.getElementById('lastRun').textContent = 
    timeDiff < 60 ?  PH0  :  PH1 ;
}

// Simulate live updates
setInterval(() => {
  // Update last run time
  const lastRun = localStorage.getItem('lastPipelineRun');
  if (lastRun) {
    const timeDiff = Math.floor((Date.now() - parseInt(lastRun)) / 1000 / 60);
    document.getElementById('lastRun').textContent = 
      timeDiff < 60 ?  PH2  :  PH3 ;
  }
}, 60000); // Update every minute
}

// Quick actions
function runPipeline() {
if (confirm('Run the full automation pipeline now?')) {
  alert('Pipeline execution would be triggered here.\n\nIn production, this would call:\n./daily_automation.sh');
}
}

function rebuildSite() {
if (confirm('Rebuild the Quarto site now?')) {
  alert('Site rebuild would be triggered here.\n\nIn production, this would call:\nquarto render --to html');
}
}

function fetchPapers() {
if (confirm('Fetch new papers from arXiv now?')) {
  alert('Paper fetch would be triggered here.\n\nIn production, this would call:\npython3 fetch_arxiv.py');
}
}

function viewLogs() {
alert('Full logs would be displayed here.\n\nIn production, this would show:\ntail -100 automation.log');
}

// Initialize
loadSystemHealth();
</script>
