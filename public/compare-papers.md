---
title: "Compare Papers"
---

Select 2-4 papers to compare side-by-side.

<div class="compare-container">
<div class="paper-selector">
<label>Select papers to compare:</label>
<select id="paper1" class="paper-select">
<option value="">-- Select Paper 1 --</option>
</select>
<select id="paper2" class="paper-select">
<option value="">-- Select Paper 2 --</option>
</select>
<select id="paper3" class="paper-select">
<option value="">-- Select Paper 3 (optional) --</option>
</select>
<select id="paper4" class="paper-select">
<option value="">-- Select Paper 4 (optional) --</option>
</select>
<button id="compareBtn" class="compare-button">Compare Papers</button>
</div>
  
<div id="comparisonResults" class="comparison-results"></div>
</div>

<style>
.compare-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.paper-selector {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.paper-selector label {
  display: block;
  font-weight: 600;
  margin-bottom: 10px;
  color: #333;
}

.paper-select {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.compare-button {
  background: #4a90e2;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
}

.compare-button:hover {
  background: #357abd;
}

.comparison-results {
  display: grid;
  gap: 20px;
}

.comparison-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.comparison-card {
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
}

.comparison-card h3 {
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 16px;
  border-bottom: 2px solid #4a90e2;
  padding-bottom: 8px;
}

.comparison-card .field {
  margin-bottom: 15px;
}

.comparison-card .field-label {
  font-weight: 600;
  color: #666;
  font-size: 12px;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.comparison-card .field-value {
  color: #333;
  font-size: 14px;
  line-height: 1.5;
}

.comparison-card .topic-tag {
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-bottom: 4px;
}

.comparison-summary {
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 15px;
  margin-top: 20px;
  border-radius: 4px;
}

.comparison-summary h4 {
  margin-top: 0;
  color: #856404;
}

.comparison-summary ul {
  margin: 10px 0;
  padding-left: 20px;
}

.comparison-summary li {
  margin-bottom: 8px;
  color: #856404;
}
</style>

<script>
const papers = [
  {
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "authors": "Nolasque, T, Grey, J, Pham, C, Vani, A",
    "date": "2026-08-31",
    "abstract": "Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there exists a token-budget threshold, below which the overhead of planning and verification hurts perform",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html"
  },
  {
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "authors": "Dore, D, Damo, G, Cabrio, E, Villata, S",
    "date": "2026-08-31",
    "abstract": "Fallacies are arguments that employ invalid reasoning, making their automatic detection critical in sensitive contexts such as high-stakes political debates, where public opinion is shaped. Spotting a fallacious argument requires contextual knowledge beyond its pure surface text. This entails world ",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html"
  },
  {
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "authors": "Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "date": "2026-08-31",
    "abstract": "Give an agent a human&#39;s credential and it inherits the person&#39;s reach without the judgment that limits its use. It can sweep every reachable record into model context, where hidden instructions steer its next call, and every request stays credential-valid while the agent exceeds its job or a",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a singl",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on smal",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we pr",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html"
  },
  {
    "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
    "authors": "Ghawate, P, Patil, T",
    "date": "2026-08-31",
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html"
  },
  {
    "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
    "authors": "Wang, Y, Du, Y, Liu, Z, Zhang, R, Zhao, B, Yang, B, Kong, M, Qu, L, Wei, H, Liu, J, Zhu, Q",
    "date": "2026-08-31",
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring cau",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit method",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed t",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places",
    "authors": "Armitage, J, Tsochantaridis, I, Mazzone, L, Yan, C, Narayanan, S, Ebling, S",
    "date": "2026-08-31",
    "abstract": "We introduce MAP, the first benchmark to evaluate multimodal AI systems as assistants for users with accessibility requirements when planning visits to places in the real world. In our evaluation, systems are presented with requests to verify or recommend a point of interest meeting an accessibility",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.28384-MAP-A-Benchmark-on-Multimodal-Accessibility-Planni.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterati",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html"
  },
  {
    "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
    "authors": "Tejas, J M, Roy, U B, Goswami, T, Goswami, S, Dhar, M",
    "date": "2026-08-31",
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic e",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents",
    "authors": "Liu, Z, Zhang, H, Niu, L, Cao, Z, Li, H, Liu, J, Chen, W, Zhao, C, Yu, C, Meng, F",
    "date": "2026-08-31",
    "abstract": "Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as text and omit tool-returned images from subsequent context, reducing visually grounded trajectories",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.28062-WeAgent-MMSearch-Native-Text-Vision-Interaction-fo.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to c",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html"
  },
  {
    "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
    "authors": "Liu, R, Gu, N, Ai, M, Li, Y, Fu, P, Lin, Z, Wang, W",
    "date": "2026-08-31",
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA e",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across ",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  }
];

// Populate dropdowns
function populateDropdowns() {
  const selects = ['paper1', 'paper2', 'paper3', 'paper4'];
  selects.forEach(id => {
    const select = document.getElementById(id);
    papers.forEach((paper, index) => {
      const option = document.createElement('option');
      option.value = index;
      option.textContent = paper.title;
      select.appendChild(option);
    });
  });
}

function comparePapers() {
  const indices = [
    document.getElementById('paper1').value,
    document.getElementById('paper2').value,
    document.getElementById('paper3').value,
    document.getElementById('paper4').value
  ].filter(v => v !== '').map(v => parseInt(v));
  
  if (indices.length < 2) {
    alert('Please select at least 2 papers to compare');
    return;
  }
  
  const selectedPapers = indices.map(i => papers[i]);
  
  // Generate comparison
  const resultsDiv = document.getElementById('comparisonResults');
  
  // Create grid of paper cards
  let html = '<div class="comparison-grid">';
  
  selectedPapers.forEach(paper => {
    html +=  PH0 <span class="topic-tag">${t}</span> PH1 ;
  });
  
  html += '</div>';
  
  // Add comparison summary
  const allTopics = new Set();
  const sharedTopics = new Set(selectedPapers[0].topics);
  
  selectedPapers.forEach(paper => {
    paper.topics.forEach(t => allTopics.add(t));
  });
  
  selectedPapers.slice(1).forEach(paper => {
    const paperTopics = new Set(paper.topics);
    for (let topic of sharedTopics) {
      if (!paperTopics.has(topic)) {
        sharedTopics.delete(topic);
      }
    }
  });
  
  html +=  PH2 <p><strong>Shared topics:</strong> ${Array.from(sharedTopics).join(', ')}</p> PH3 ;
  
  resultsDiv.innerHTML = html;
}

// Initialize
populateDropdowns();
document.getElementById('compareBtn').addEventListener('click', comparePapers);
</script>
