---
title: "📚 My Research Topics"
---

<div class="topics-index">
<h1>📚 My Research Topics</h1>
<p class="index-description">Browse your personalized research topics and discover relevant papers.</p>

<div class="topics-grid">

<div class="topic-card">
<a href="ai-agents.html">
<div class="topic-icon">🤖</div>
<div class="topic-name">AI Agents</div>
<div class="topic-description">Autonomous systems with tool use, planning, and multi-agent coordination</div>
</a>
</div>

<div class="topic-card">
<a href="llm-reasoning.html">
<div class="topic-icon">🧠</div>
<div class="topic-name">LLM Reasoning</div>
<div class="topic-description">Chain-of-thought, self-consistency, tree-of-thought, and verification techniques</div>
</a>
</div>

<div class="topic-card">
<a href="rag-retrieval.html">
<div class="topic-icon">🔍</div>
<div class="topic-name">RAG & Retrieval</div>
<div class="topic-description">Dense retrieval, hybrid search, knowledge grounding, and citation systems</div>
</a>
</div>

<div class="topic-card">
<a href="multi-modal.html">
<div class="topic-icon">🎨</div>
<div class="topic-name">Multi-Modal Models</div>
<div class="topic-description">Vision-language models, audio processing, and cross-modal reasoning</div>
</a>
</div>

</div>
</div>

<style>
.topics-index {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.topics-index h1 {
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.index-description {
  color: var(--text-secondary, #666);
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.topic-card {
  background: var(--bg-secondary, #f8f9fa);
  border: 1px solid var(--border-color, #e0e0e0);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}

.topic-card:hover {
  border-color: var(--accent-color, #667eea);
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.topic-card a {
  text-decoration: none;
  color: inherit;
  display: block;
}

.topic-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.topic-name {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text-primary, #2c3e50);
  margin-bottom: 0.5rem;
}

.topic-description {
  color: var(--text-secondary, #666);
  font-size: 0.95rem;
  line-height: 1.5;
}
</style>
