---
title: "Your Learning Journey"
format: html
---

<style>
.journey-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.journey-hero {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 16px;
  margin-bottom: 3rem;
}

.journey-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: white;
}

.journey-hero p {
  font-size: 1.2rem;
  opacity: 0.95;
  max-width: 700px;
  margin: 0 auto;
}

.journey-progress {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 3rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.progress-header h2 {
  margin: 0;
  color: #2c3e50;
}

.progress-stats {
  display: flex;
  gap: 2rem;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #667eea;
}

.stat-label {
  font-size: 0.9rem;
  color: #7f8c8d;
}

.journey-path {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.journey-stage {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  border-left: 6px solid;
  position: relative;
}

.journey-stage.write { border-left-color: #3498db; }
.journey-stage.review { border-left-color: #f39c12; }
.journey-stage.enhance { border-left-color: #9b59b6; }
.journey-stage.attain { border-left-color: #27ae60; }
.journey-stage.update { border-left-color: #e74c3c; }

.stage-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.stage-icon {
  font-size: 2.5rem;
}

.stage-title {
  flex: 1;
}

.stage-title h3 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
  font-size: 1.5rem;
}

.stage-title p {
  margin: 0;
  color: #7f8c8d;
  font-size: 1rem;
}

.stage-progress {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 1rem;
}

.progress-bar {
  flex: 1;
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.9rem;
  color: #7f8c8d;
  min-width: 60px;
}

.stage-tools {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.tool-card {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  text-decoration: none;
  color: #2c3e50;
  transition: all 0.2s;
  border: 2px solid transparent;
}

.tool-card:hover {
  background: white;
  border-color: #667eea;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

.tool-icon {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.tool-name {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.tool-desc {
  font-size: 0.85rem;
  color: #7f8c8d;
}

.stage-action {
  margin-top: 1.5rem;
  text-align: center;
}

.btn-primary {
  display: inline-block;
  padding: 0.75rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.journey-connector {
  text-align: center;
  font-size: 2rem;
  color: #bdc3c7;
  margin: -1rem 0;
}

@media (max-width: 768px) {
  .journey-hero h1 {
    font-size: 1.8rem;
  }
  
  .progress-stats {
    flex-direction: column;
    gap: 1rem;
  }
  
  .stage-tools {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="journey-container">

<div class="journey-hero">
<h1>🎓 Your Learning Journey</h1>
<p>Build deep understanding through an active learning cycle: write, review, enhance, attain, and stay current</p>
</div>

<div class="journey-progress">
<div class="progress-header">
<h2>📊 Your Progress</h2>
<div class="progress-stats">
<div class="stat-item">
<div class="stat-value" id="termsExplored">0</div>
<div class="stat-label">Terms Explored</div>
</div>
<div class="stat-item">
<div class="stat-value" id="explanationsWritten">0</div>
<div class="stat-label">Explanations Written</div>
</div>
<div class="stat-item">
<div class="stat-value" id="masteredConcepts">0</div>
<div class="stat-label">Concepts Mastered</div>
</div>
</div>
</div>
</div>

<div class="journey-path">

<!-- Stage 1: WRITE -->
<div class="journey-stage write">
<div class="stage-header">
<div class="stage-icon">✍️</div>
<div class="stage-title">
<h3>1. Write & Build Understanding</h3>
<p>Actively construct knowledge by explaining concepts in your own words</p>
</div>
</div>
<div class="stage-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 0%"></div>
</div>
<div class="progress-text">0%</div>
</div>
<div class="stage-tools">
<a href="wiki.html" class="tool-card">
<div class="tool-icon">📖</div>
<div class="tool-name">AI Wiki</div>
<div class="tool-desc">Click terms, write explanations, build understanding</div>
</a>
<a href="paper-reader.html" class="tool-card">
<div class="tool-icon">📄</div>
<div class="tool-name">Paper Reader</div>
<div class="tool-desc">Read papers and extract key insights</div>
</a>
<a href="workspace.html" class="tool-card">
<div class="tool-icon">🔬</div>
<div class="tool-name">Research Workspace</div>
<div class="tool-desc">Organize your reading and annotations</div>
</a>
</div>
<div class="stage-action">
<a href="wiki.html" class="btn-primary">Start Writing →</a>
</div>
</div>

<div class="journey-connector">↓</div>

<!-- Stage 2: REVIEW -->
<div class="journey-stage review">
<div class="stage-header">
<div class="stage-icon">🔍</div>
<div class="stage-title">
<h3>2. Review & Reflect</h3>
<p>Re-examine your explanations, identify gaps, and refine understanding</p>
</div>
</div>
<div class="stage-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 0%"></div>
</div>
<div class="progress-text">0%</div>
</div>
<div class="stage-tools">
<a href="highlights.html" class="tool-card">
<div class="tool-icon">✨</div>
<div class="tool-name">Highlights</div>
<div class="tool-desc">Review key passages from papers</div>
</a>
<a href="takeaways.html" class="tool-card">
<div class="tool-icon">💡</div>
<div class="tool-name">Takeaways</div>
<div class="tool-desc">Your key insights and learnings</div>
</a>
<a href="questions.html" class="tool-card">
<div class="tool-icon">❓</div>
<div class="tool-name">Questions</div>
<div class="tool-desc">Track unclear points and research questions</div>
</a>
</div>
<div class="stage-action">
<a href="highlights.html" class="btn-primary">Start Reviewing →</a>
</div>
</div>

<div class="journey-connector">↓</div>

<!-- Stage 3: ENHANCE -->
<div class="journey-stage enhance">
<div class="stage-header">
<div class="stage-icon">🤖</div>
<div class="stage-title">
<h3>3. AI Enhancement</h3>
<p>Get intelligent feedback and suggestions to improve your understanding</p>
</div>
</div>
<div class="stage-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 0%"></div>
</div>
<div class="progress-text">0%</div>
</div>
<div class="stage-tools">
<a href="ai-wiki.html" class="tool-card">
<div class="tool-icon">💬</div>
<div class="tool-name">AI Wiki Assistant</div>
<div class="tool-desc">Get AI feedback on your explanations</div>
</a>
<a href="ai-study-guide.html" class="tool-card">
<div class="tool-icon">🎓</div>
<div class="tool-name">AI Study Guide</div>
<div class="tool-desc">Personalized learning recommendations</div>
</a>
<a href="feedback-dashboard.html" class="tool-card">
<div class="tool-icon">📊</div>
<div class="tool-name">Feedback Dashboard</div>
<div class="tool-desc">Track your AI interactions and improvements</div>
</a>
</div>
<div class="stage-action">
<a href="ai-wiki.html" class="btn-primary">Get AI Feedback →</a>
</div>
</div>

<div class="journey-connector">↓</div>

<!-- Stage 4: ATTAIN -->
<div class="journey-stage attain">
<div class="stage-header">
<div class="stage-icon">🧠</div>
<div class="stage-title">
<h3>4. Attain Mastery</h3>
<p>Internalize knowledge through spaced repetition and practice</p>
</div>
</div>
<div class="stage-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 0%"></div>
</div>
<div class="progress-text">0%</div>
</div>
<div class="stage-tools">
<a href="spaced-repetition.html" class="tool-card">
<div class="tool-icon">🔄</div>
<div class="tool-name">Spaced Repetition</div>
<div class="tool-desc">Review at optimal intervals for retention</div>
</a>
<a href="my-learning-path.html" class="tool-card">
<div class="tool-icon">🎯</div>
<div class="tool-name">Learning Path</div>
<div class="tool-desc">Track your progress and mastery levels</div>
</a>
<a href="recommendations.html" class="tool-card">
<div class="tool-icon">💡</div>
<div class="tool-name">Recommendations</div>
<div class="tool-desc">What to learn next based on your progress</div>
</a>
</div>
<div class="stage-action">
<a href="spaced-repetition.html" class="btn-primary">Start Practicing →</a>
</div>
</div>

<div class="journey-connector">↓</div>

<!-- Stage 5: UPDATE -->
<div class="journey-stage update">
<div class="stage-header">
<div class="stage-icon">📈</div>
<div class="stage-title">
<h3>5. Stay Updated</h3>
<p>Monitor new research and continuously refine your understanding</p>
</div>
</div>
<div class="stage-progress">
<div class="progress-bar">
<div class="progress-fill" style="width: 0%"></div>
</div>
<div class="progress-text">0%</div>
</div>
<div class="stage-tools">
<a href="digests/index.html" class="tool-card">
<div class="tool-icon">📰</div>
<div class="tool-name">Weekly Digest</div>
<div class="tool-desc">Latest papers and developments</div>
</a>
<a href="search-papers.html" class="tool-card">
<div class="tool-icon">📚</div>
<div class="tool-name">Paper Library</div>
<div class="tool-desc">Browse and discover new research</div>
</a>
<a href="timeline.html" class="tool-card">
<div class="tool-icon">📅</div>
<div class="tool-name">Timeline</div>
<div class="tool-desc">Track research evolution over time</div>
</a>
</div>
<div class="stage-action">
<a href="digests/index.html" class="btn-primary">Check Updates →</a>
</div>
</div>

</div>

</div>

<script>
// Load progress from localStorage
function loadJourneyProgress() {
  const contributions = JSON.parse(localStorage.getItem('wikiContributions') || '[]');
  const terms = new Set(contributions.map(c => c.termId));
  const explanations = contributions.filter(c => c.type === 'explanation');
  
  document.getElementById('termsExplored').textContent = terms.size;
  document.getElementById('explanationsWritten').textContent = explanations.length;
  
  // Calculate mastery (simplified for now)
  const mastered = contributions.filter(c => c.type === 'explanation' && c.content.length > 200).length;
  document.getElementById('masteredConcepts').textContent = mastered;
  
  // Update progress bars (simplified)
  const stages = document.querySelectorAll('.journey-stage');
  stages.forEach((stage, index) => {
    const progress = Math.min(100, (contributions.length / (index + 1)) * 20);
    const fill = stage.querySelector('.progress-fill');
    const text = stage.querySelector('.progress-text');
    fill.style.width = progress + '%';
    text.textContent = Math.round(progress) + '%';
  });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', loadJourneyProgress);
</script>
