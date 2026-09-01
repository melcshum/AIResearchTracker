---
title: "Paper Recommendations"
---

<div class="recommendations-container">

<div class="recommendations-hero">
<div class="hero-icon">💡</div>
<h1>Paper Recommendations</h1>
<p class="hero-subtitle">AI-powered suggestions based on your reading history and interests</p>
</div>

<!-- Recommendation Summary -->
<div class="summary-grid">
<div class="summary-card">
<div class="summary-icon">📊</div>
<div class="summary-content">
<div class="summary-label">Papers Analyzed</div>
<div class="summary-value" id="papersAnalyzed">0</div>
</div>
</div>
<div class="summary-card">
<div class="summary-icon">🎯</div>
<div class="summary-content">
<div class="summary-label">Topics Identified</div>
<div class="summary-value" id="topicsIdentified">0</div>
</div>
</div>
<div class="summary-card">
<div class="summary-icon">💡</div>
<div class="summary-content">
<div class="summary-label">Recommendations</div>
<div class="summary-value" id="recommendationsCount">0</div>
</div>
</div>
<div class="summary-card">
<div class="summary-icon">📈</div>
<div class="summary-content">
<div class="summary-label">Match Score</div>
<div class="summary-value" id="matchScore">0%</div>
</div>
</div>
</div>

<!-- Your Interests -->
<div class="section-card">
<h2>🎯 Your Research Interests</h2>
<p class="section-desc">Based on your reading history, these are your top research areas</p>
<div class="interests-grid" id="interestsGrid">
<!-- Populated by JavaScript -->
</div>
</div>

<!-- Recommended Papers -->
<div class="section-card">
<h2>💡 Recommended for You</h2>
<p class="section-desc">Papers you haven't read yet that match your interests</p>
<div class="recommendations-list" id="recommendationsList">
<!-- Populated by JavaScript -->
</div>
</div>

<!-- Recently Read -->
<div class="section-card">
<h2>📖 Based on Recently Read</h2>
<p class="section-desc">Papers similar to what you've recently finished</p>
<div class="recent-papers" id="recentPapers">
<!-- Populated by JavaScript -->
</div>
</div>

</div>

<style>
.recommendations-container {
max-width: 1400px;
margin: 0 auto;
padding: 2rem;
}

.recommendations-hero {
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

.recommendations-hero h1 {
font-size: 2.5rem;
margin: 0 0 0.5rem 0;
}

.hero-subtitle {
font-size: 1.1rem;
opacity: 0.95;
margin: 0;
}

.summary-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
gap: 1.5rem;
margin-bottom: 2rem;
}

.summary-card {
background: white;
border-radius: 12px;
padding: 1.5rem;
box-shadow: 0 2px 8px rgba(0,0,0,0.08);
display: flex;
align-items: center;
gap: 1rem;
transition: all 0.3s ease;
}

.summary-card:hover {
transform: translateY(-4px);
box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.summary-icon {
font-size: 2.5rem;
}

.summary-content {
flex: 1;
}

.summary-label {
font-size: 0.85rem;
color: #6b7280;
text-transform: uppercase;
letter-spacing: 0.5px;
margin-bottom: 0.25rem;
}

.summary-value {
font-size: 2rem;
font-weight: 700;
color: #1f2937;
line-height: 1;
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
margin: 0 0 0.5rem 0;
color: #1f2937;
}

.section-desc {
color: #6b7280;
margin: 0 0 1.5rem 0;
}

.interests-grid {
display: grid;
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
gap: 1rem;
}

.interest-tag {
padding: 1rem;
background: linear-gradient(135deg, #f0f4ff 0%, #e0e7ff 100%);
border-radius: 8px;
border-left: 4px solid #667eea;
transition: all 0.2s ease;
}

.interest-tag:hover {
transform: translateX(4px);
box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
}

.interest-name {
font-weight: 600;
color: #1f2937;
margin-bottom: 0.25rem;
}

.interest-count {
font-size: 0.85rem;
color: #6b7280;
}

.recommendations-list {
display: flex;
flex-direction: column;
gap: 1rem;
}

.recommendation-item {
padding: 1.5rem;
background: #f9fafb;
border-radius: 8px;
border-left: 4px solid #10b981;
transition: all 0.2s ease;
}

.recommendation-item:hover {
background: #f0fdf4;
transform: translateX(4px);
}

.recommendation-header {
display: flex;
justify-content: space-between;
align-items: start;
margin-bottom: 0.75rem;
}

.recommendation-title {
font-size: 1.1rem;
font-weight: 600;
color: #1f2937;
margin: 0;
flex: 1;
}

.match-badge {
background: #10b981;
color: white;
padding: 0.25rem 0.75rem;
border-radius: 12px;
font-size: 0.85rem;
font-weight: 600;
white-space: nowrap;
}

.recommendation-meta {
display: flex;
gap: 1rem;
margin-bottom: 0.75rem;
font-size: 0.85rem;
color: #6b7280;
}

.recommendation-reason {
font-size: 0.9rem;
color: #4b5563;
margin-bottom: 0.75rem;
}

.recommendation-actions {
display: flex;
gap: 0.5rem;
}

.btn {
padding: 0.5rem 1rem;
border-radius: 6px;
text-decoration: none;
font-size: 0.9rem;
font-weight: 600;
transition: all 0.2s ease;
border: none;
cursor: pointer;
}

.btn-primary {
background: #667eea;
color: white;
}

.btn-primary:hover {
background: #764ba2;
}

.btn-secondary {
background: #e5e7eb;
color: #1f2937;
}

.btn-secondary:hover {
background: #d1d5db;
}

.recent-papers {
display: grid;
grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
gap: 1rem;
}

.recent-paper-card {
padding: 1rem;
background: #f9fafb;
border-radius: 8px;
border-left: 4px solid #3b82f6;
transition: all 0.2s ease;
}

.recent-paper-card:hover {
background: #eff6ff;
transform: translateY(-2px);
}

.recent-paper-title {
font-weight: 600;
color: #1f2937;
margin-bottom: 0.5rem;
font-size: 0.95rem;
}

.recent-paper-meta {
font-size: 0.8rem;
color: #6b7280;
}

.empty-state {
text-align: center;
padding: 3rem;
color: #6b7280;
}

.empty-state-icon {
font-size: 3rem;
margin-bottom: 1rem;
opacity: 0.5;
}

@media (max-width: 768px) {
.recommendations-container {
  padding: 1rem;
}

.recommendations-hero h1 {
  font-size: 1.8rem;
}

.summary-grid {
  grid-template-columns: repeat(2, 1fr);
}

.interests-grid {
  grid-template-columns: 1fr;
}
}
</style>

<script>
// Paper recommendation engine
function generateRecommendations() {
const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
const allPapers = window.PAPERS_DATA || [];

// Analyze reading history
const readPapers = bookmarks.filter(b => b.status === 'Read' || b.status === 'Cited');
const readingPapers = bookmarks.filter(b => b.status === 'Reading');

// Extract topics from read papers
const topicCounts = {};
readPapers.forEach(paper => {
  if (paper.topics) {
    paper.topics.forEach(topic => {
      topicCounts[topic] = (topicCounts[topic] || 0) + 1;
    });
  }
});

// Sort topics by frequency
const topTopics = Object.entries(topicCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 10);

// Find unread papers matching interests
const readPaperIds = new Set(bookmarks.map(b => b.id));
const recommendations = allPapers
  .filter(paper => !readPaperIds.has(paper.id))
  .map(paper => {
    let matchScore = 0;
    let matchReasons = [];
    
    if (paper.topics) {
      paper.topics.forEach(topic => {
        if (topicCounts[topic]) {
          matchScore += topicCounts[topic];
          matchReasons.push(topic);
        }
      });
    }
    
    return {
      ...paper,
      matchScore,
      matchReasons: matchReasons.slice(0, 3)
    };
  })
  .filter(paper => paper.matchScore > 0)
  .sort((a, b) => b.matchScore - a.matchScore)
  .slice(0, 10);

// Calculate average match score
const avgMatchScore = recommendations.length > 0
  ? Math.round(recommendations.reduce((sum, r) => sum + r.matchScore, 0) / recommendations.length * 10)
  : 0;

// Update summary
document.getElementById('papersAnalyzed').textContent = allPapers.length;
document.getElementById('topicsIdentified').textContent = topTopics.length;
document.getElementById('recommendationsCount').textContent = recommendations.length;
document.getElementById('matchScore').textContent = avgMatchScore + '%';

// Render interests
const interestsGrid = document.getElementById('interestsGrid');
if (topTopics.length === 0) {
  interestsGrid.innerHTML = '<div class="empty-state"><div class="empty-state-icon">🎯</div><p>Start reading papers to see your interests</p></div>';
} else {
  interestsGrid.innerHTML = topTopics.map(([topic, count]) =>  PH0 ).join('');
}

// Render recommendations
const recommendationsList = document.getElementById('recommendationsList');
if (recommendations.length === 0) {
  recommendationsList.innerHTML = '<div class="empty-state"><div class="empty-state-icon">💡</div><p>No recommendations yet. Read more papers to get personalized suggestions!</p></div>';
} else {
  recommendationsList.innerHTML = recommendations.map(rec =>  PH1 ).join('');
}

// Render recently read
const recentPapers = document.getElementById('recentPapers');
const recentlyRead = readPapers.slice(-6).reverse();
if (recentlyRead.length === 0) {
  recentPapers.innerHTML = '<div class="empty-state"><div class="empty-state-icon">📖</div><p>No recently read papers yet</p></div>';
} else {
  recentPapers.innerHTML = recentlyRead.map(paper =>  PH2 ).join('');
}
}

function bookmarkPaper(paperId) {
const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
if (!bookmarks.find(b => b.id === paperId)) {
  bookmarks.push({
    id: paperId,
    status: 'Inbox',
    timestamp: new Date().toISOString()
  });
  localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
  alert('Paper bookmarked! Refresh to see updated recommendations.');
}
}

// Load paper data (would be injected by generate script in production)
window.PAPERS_DATA = [
  {
    "id": "2510.02816",
    "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
    "date": "",
    "topics": [],
    "authors": "** Yulong Zhang, Li Wang, Wei Du, Peilin Li, Yuqin Dai Zhiyuan Zhao, Lingyong Fang, Ziniu Liu, Ru Zhang, Huijia Zhu, Gongshen Liu",
    "url": "https://arxiv.org/abs/2510.02816"
  },
  {
    "id": "2605.30003",
    "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
    "date": "",
    "topics": [],
    "authors": "** V\u00edctor Gallego",
    "url": "https://arxiv.org/abs/2605.30003"
  },
  {
    "id": "2608.22688",
    "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
    "date": "",
    "topics": [],
    "authors": "** Yujuan Ding, Linyin Luo, Shijie Wang, Xu Yuan, Yunshan Ma, Yi Bin, Wenqi Fan, Qing Li",
    "url": "https://arxiv.org/abs/2608.22688"
  },
  {
    "id": "2608.22634",
    "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
    "date": "",
    "topics": [],
    "authors": "** Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib, Yordanos Tessema, Chang-Tien Lu",
    "url": "https://arxiv.org/abs/2608.22634"
  },
  {
    "id": "2608.15012",
    "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
    "date": "",
    "topics": [],
    "authors": "** Yuhan Meng, Shaofei Li, Jionghao Huang, Jiandong Jin, Puyi Wang, Hanlin Jiang, Anis Yusof, Peng Jiang, Zhenkai Liang, Yao Guo, Ding Li",
    "url": "https://arxiv.org/abs/2608.15012"
  },
  {
    "id": "2608.27506",
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "date": "",
    "topics": [],
    "authors": "** Nolasque, T, Grey, J, Pham, C, Vani, A",
    "url": "https://arxiv.org/abs/2608.27506"
  },
  {
    "id": "2608.27471",
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "date": "",
    "topics": [],
    "authors": "** Dore, D, Damo, G, Cabrio, E, Villata, S",
    "url": "https://arxiv.org/abs/2608.27471"
  },
  {
    "id": "2608.27646",
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "date": "",
    "topics": [],
    "authors": "** Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "url": "https://arxiv.org/abs/2608.27646"
  },
  {
    "id": "2608.27475",
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "date": "",
    "topics": [],
    "authors": "** Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "url": "https://arxiv.org/abs/2608.27475"
  },
  {
    "id": "2608.27840",
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "date": "",
    "topics": [],
    "authors": "** Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "url": "https://arxiv.org/abs/2608.27840"
  },
  {
    "id": "2608.27508",
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "date": "",
    "topics": [],
    "authors": "** Han, Y, Qian, T",
    "url": "https://arxiv.org/abs/2608.27508"
  },
  {
    "id": "2608.27484",
    "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
    "date": "",
    "topics": [],
    "authors": "** Ghawate, P, Patil, T",
    "url": "https://arxiv.org/abs/2608.27484"
  },
  {
    "id": "2608.27953",
    "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
    "date": "",
    "topics": [],
    "authors": "** Wang, Y, Du, Y, Liu, Z, Zhang, R, Zhao, B, Yang, B, Kong, M, Qu, L, Wei, H, Liu, J, Zhu, Q",
    "url": "https://arxiv.org/abs/2608.27953"
  },
  {
    "id": "2608.27963",
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "date": "",
    "topics": [],
    "authors": "** Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "url": "https://arxiv.org/abs/2608.27963"
  },
  {
    "id": "2608.27945",
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "date": "",
    "topics": [],
    "authors": "** Liao, D, Wang, Y, Shi, F, Yu, Y",
    "url": "https://arxiv.org/abs/2608.27945"
  },
  {
    "id": "2608.27869",
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "date": "",
    "topics": [],
    "authors": "** Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "url": "https://arxiv.org/abs/2608.27869"
  },
  {
    "id": "2608.27524",
    "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
    "date": "",
    "topics": [],
    "authors": "** Tejas, J M, Roy, U B, Goswami, T, Goswami, S, Dhar, M",
    "url": "https://arxiv.org/abs/2608.27524"
  },
  {
    "id": "2608.27548",
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "date": "",
    "topics": [],
    "authors": "** Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "url": "https://arxiv.org/abs/2608.27548"
  },
  {
    "id": "2608.27867",
    "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
    "date": "",
    "topics": [],
    "authors": "** Liu, R, Gu, N, Ai, M, Li, Y, Fu, P, Lin, Z, Wang, W",
    "url": "https://arxiv.org/abs/2608.27867"
  },
  {
    "id": "2608.27919",
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "date": "",
    "topics": [],
    "authors": "** Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "url": "https://arxiv.org/abs/2608.27919"
  },
  {
    "id": "2607.22319",
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "date": "",
    "topics": [],
    "authors": "** Chuangtao Ma, Arijit Khan",
    "url": "https://arxiv.org/abs/2607.22319"
  },
  {
    "id": "2601.01126",
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "date": "",
    "topics": [],
    "authors": "** Andrew Borthwick, Stephen Ash",
    "url": "https://arxiv.org/abs/2601.01126"
  },
  {
    "id": "2602.20426",
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "date": "",
    "topics": [],
    "authors": "** Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "url": "https://arxiv.org/abs/2602.20426"
  },
  {
    "id": "2608.28543",
    "title": "Rational torsion on simple genus two Jacobians",
    "date": "",
    "topics": [],
    "authors": "** Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "url": "https://arxiv.org/abs/2608.28543"
  },
  {
    "id": "2608.28246",
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "date": "",
    "topics": [],
    "authors": "** Marin Maletic, Goran Vasiljevic",
    "url": "https://arxiv.org/abs/2608.28246"
  },
  {
    "id": "2608.28567",
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "date": "",
    "topics": [],
    "authors": "** Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "url": "https://arxiv.org/abs/2608.28567"
  },
  {
    "id": "2608.28577",
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "date": "",
    "topics": [],
    "authors": "** Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "url": "https://arxiv.org/abs/2608.28577"
  },
  {
    "id": "2608.28581",
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "date": "",
    "topics": [],
    "authors": "** Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "url": "https://arxiv.org/abs/2608.28581"
  },
  {
    "id": "2608.28584",
    "title": "Bounds for inertialess dynamo",
    "date": "",
    "topics": [],
    "authors": "** Ali Arslan, Hezekiah Grayer",
    "url": "https://arxiv.org/abs/2608.28584"
  },
  {
    "id": "2608.28583",
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "date": "",
    "topics": [],
    "authors": "** Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "url": "https://arxiv.org/abs/2608.28583"
  },
  {
    "id": "2608.28553",
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "date": "",
    "topics": [],
    "authors": "** Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "url": "https://arxiv.org/abs/2608.28553"
  },
  {
    "id": "2608.28514",
    "title": "Fast and efficient nested sampling with BEST",
    "date": "",
    "topics": [],
    "authors": "** Andreas Nygaard",
    "url": "https://arxiv.org/abs/2608.28514"
  },
  {
    "id": "2608.28541",
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "date": "",
    "topics": [],
    "authors": "** Javier Aguilar Mart\u00edn",
    "url": "https://arxiv.org/abs/2608.28541"
  },
  {
    "id": "2608.28503",
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "date": "",
    "topics": [],
    "authors": "** Xinyi Zhang, Yutong Li, Peijie Sun",
    "url": "https://arxiv.org/abs/2608.28503"
  },
  {
    "id": "2608.28579",
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "date": "",
    "topics": [],
    "authors": "** Lukas M\u00fcller, Lukas Woike",
    "url": "https://arxiv.org/abs/2608.28579"
  },
  {
    "id": "2608.28248",
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "date": "",
    "topics": [],
    "authors": "** Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "url": "https://arxiv.org/abs/2608.28248"
  },
  {
    "id": "2608.28572",
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "date": "",
    "topics": [],
    "authors": "** Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "url": "https://arxiv.org/abs/2608.28572"
  },
  {
    "id": "2608.28588",
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "date": "",
    "topics": [],
    "authors": "** Akshay Pal, Andrew Lucas, Umang Mehta",
    "url": "https://arxiv.org/abs/2608.28588"
  },
  {
    "id": "2608.28566",
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "date": "",
    "topics": [],
    "authors": "** Yuansi Chen, Yunbum Kook",
    "url": "https://arxiv.org/abs/2608.28566"
  },
  {
    "id": "2608.28576",
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "date": "",
    "topics": [],
    "authors": "** Chengpiao Huang, Kaizheng Wang",
    "url": "https://arxiv.org/abs/2608.28576"
  },
  {
    "id": "2608.28403",
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "date": "",
    "topics": [],
    "authors": "** Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "url": "https://arxiv.org/abs/2608.28403"
  },
  {
    "id": "2608.28542",
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "date": "",
    "topics": [],
    "authors": "** Adil Alshammari, Hayretdin Bahsi",
    "url": "https://arxiv.org/abs/2608.28542"
  },
  {
    "id": "2608.28216",
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "date": "",
    "topics": [],
    "authors": "** Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "url": "https://arxiv.org/abs/2608.28216"
  },
  {
    "id": "2608.28547",
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "date": "",
    "topics": [],
    "authors": "** Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "url": "https://arxiv.org/abs/2608.28547"
  },
  {
    "id": "2608.28578",
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "date": "",
    "topics": [],
    "authors": "** Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "url": "https://arxiv.org/abs/2608.28578"
  },
  {
    "id": "2608.28534",
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "date": "",
    "topics": [],
    "authors": "** Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "url": "https://arxiv.org/abs/2608.28534"
  },
  {
    "id": "2608.28144",
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "date": "",
    "topics": [],
    "authors": "** Farah Atif, Sougata Saha, Monojit Choudhury",
    "url": "https://arxiv.org/abs/2608.28144"
  },
  {
    "id": "2608.28580",
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "date": "",
    "topics": [],
    "authors": "** Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "url": "https://arxiv.org/abs/2608.28580"
  },
  {
    "id": "2608.28570",
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "date": "",
    "topics": [],
    "authors": "** Seungyeon Kim, No\u00e9mie Jaquier",
    "url": "https://arxiv.org/abs/2608.28570"
  },
  {
    "id": "2608.28589",
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "date": "",
    "topics": [],
    "authors": "** Vaibhav Mehandiratta, Saket Ramchandra",
    "url": "https://arxiv.org/abs/2608.28589"
  },
  {
    "id": "2608.28218",
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "date": "",
    "topics": [],
    "authors": "** Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "url": "https://arxiv.org/abs/2608.28218"
  },
  {
    "id": "2608.28554",
    "title": "Machine learned designs of functional colloidal foldamers",
    "date": "",
    "topics": [],
    "authors": "** Ryan van Mastrigt, Zorana Zeravcic",
    "url": "https://arxiv.org/abs/2608.28554"
  },
  {
    "id": "2608.28551",
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "date": "",
    "topics": [],
    "authors": "** Viet-Hoang Tran, Tan M. Nguyen",
    "url": "https://arxiv.org/abs/2608.28551"
  },
  {
    "id": "2608.28399",
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "date": "",
    "topics": [],
    "authors": "** Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "url": "https://arxiv.org/abs/2608.28399"
  },
  {
    "id": "2608.28549",
    "title": "Video Generative Models as Geometry Learner",
    "date": "",
    "topics": [],
    "authors": "** Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "url": "https://arxiv.org/abs/2608.28549"
  },
  {
    "id": "2608.28529",
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "date": "",
    "topics": [],
    "authors": "** Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "url": "https://arxiv.org/abs/2608.28529"
  },
  {
    "id": "2608.27809",
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "date": "",
    "topics": [],
    "authors": "** Akito Hattori",
    "url": "https://arxiv.org/abs/2608.27809"
  },
  {
    "id": "2608.28532",
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "date": "",
    "topics": [],
    "authors": "** Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "url": "https://arxiv.org/abs/2608.28532"
  },
  {
    "id": "2608.28563",
    "title": "Exact quantification of nonlocal magic",
    "date": "",
    "topics": [],
    "authors": "** Piotr Sierant",
    "url": "https://arxiv.org/abs/2608.28563"
  },
  {
    "id": "2608.28383",
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "date": "",
    "topics": [],
    "authors": "** Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "url": "https://arxiv.org/abs/2608.28383"
  },
  {
    "id": "2608.28586",
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "date": "",
    "topics": [],
    "authors": "** Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "url": "https://arxiv.org/abs/2608.28586"
  },
  {
    "id": "2608.28389",
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "date": "",
    "topics": [],
    "authors": "** Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "url": "https://arxiv.org/abs/2608.28389"
  },
  {
    "id": "2608.27101",
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "date": "",
    "topics": [],
    "authors": "** Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "url": "https://arxiv.org/abs/2608.27101"
  },
  {
    "id": "2608.27036",
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "date": "",
    "topics": [],
    "authors": "** Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "url": "https://arxiv.org/abs/2608.27036"
  },
  {
    "id": "2608.27046",
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "date": "",
    "topics": [],
    "authors": "** Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "url": "https://arxiv.org/abs/2608.27046"
  },
  {
    "id": "2608.27661",
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "date": "",
    "topics": [],
    "authors": "** Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "url": "https://arxiv.org/abs/2608.27661"
  },
  {
    "id": "2608.26921",
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "date": "",
    "topics": [],
    "authors": "** Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "url": "https://arxiv.org/abs/2608.26921"
  },
  {
    "id": "2608.26870",
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "date": "",
    "topics": [],
    "authors": "** Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "url": "https://arxiv.org/abs/2608.26870"
  },
  {
    "id": "2608.27121",
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "date": "",
    "topics": [],
    "authors": "** Corey D. C. Heath",
    "url": "https://arxiv.org/abs/2608.27121"
  },
  {
    "id": "2608.26856",
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "date": "",
    "topics": [],
    "authors": "** Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "url": "https://arxiv.org/abs/2608.26856"
  },
  {
    "id": "2608.26623",
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "date": "",
    "topics": [],
    "authors": "** Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "url": "https://arxiv.org/abs/2608.26623"
  },
  {
    "id": "2607.03233",
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "date": "",
    "topics": [],
    "authors": "** Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "url": "https://arxiv.org/abs/2607.03233"
  },
  {
    "id": "2604.04820",
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "date": "",
    "topics": [],
    "authors": "** Xu Mingze",
    "url": "https://arxiv.org/abs/2604.04820"
  },
  {
    "id": "2607.14642",
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "date": "",
    "topics": [],
    "authors": "** Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "url": "https://arxiv.org/abs/2607.14642"
  },
  {
    "id": "2606.20041",
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "date": "",
    "topics": [],
    "authors": "** Masahiro Kato",
    "url": "https://arxiv.org/abs/2606.20041"
  },
  {
    "id": "2605.04637",
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "date": "",
    "topics": [],
    "authors": "** Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "url": "https://arxiv.org/abs/2605.04637"
  },
  {
    "id": "2510.20036",
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "date": "",
    "topics": [],
    "authors": "** Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "url": "https://arxiv.org/abs/2510.20036"
  }
];

// Initialize
generateRecommendations();
</script>
