---
title: "Search Papers"
---

<div class="search-container">
<input type="text" id="searchInput" placeholder="Search papers by title, author, or keyword..." class="search-box">
  
<div class="filter-section">
<label>Filter by topic:</label>
<select id="topicFilter" class="filter-select">
<option value="">All Topics</option>
<!-- Topics will be loaded dynamically from user config -->
</select>
    
<label>Sort by:</label>
<select id="sortBy" class="filter-select">
<option value="date">Date (Newest First)</option>
<option value="title">Title (A-Z)</option>
<option value="authors">Authors (A-Z)</option>
</select>
</div>
  
<div id="resultsCount" class="results-count"></div>
<div id="searchResults" class="search-results"></div>
</div>

<style>
.search-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.search-box {
  width: 100%;
  padding: 12px 20px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  margin-bottom: 20px;
}

.search-box:focus {
  outline: none;
  border-color: #4a90e2;
}

.filter-section {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  align-items: center;
}

.filter-section label {
  font-weight: 600;
  color: #333;
}

.filter-select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  background: white;
  cursor: pointer;
}

.results-count {
  color: #666;
  margin-bottom: 15px;
  font-size: 14px;
}

.search-results {
  display: grid;
  gap: 20px;
}

.paper-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  transition: box-shadow 0.2s;
}

.paper-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.paper-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #2c3e50;
}

.paper-title a {
  color: #2c3e50;
  text-decoration: none;
}

.paper-title a:hover {
  color: #4a90e2;
}

.paper-meta {
  color: #666;
  font-size: 14px;
  margin-bottom: 12px;
}

.paper-authors {
  margin-bottom: 4px;
}

.paper-date {
  margin-bottom: 4px;
}

.paper-abstract {
  color: #444;
  line-height: 1.6;
  margin-top: 12px;
  font-size: 14px;
}

.paper-topics {
  margin-top: 12px;
}

.topic-tag {
  display: inline-block;
  padding: 4px 10px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 12px;
  margin-right: 6px;
  margin-bottom: 6px;
}

.paper-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.bookmark-btn {
  background: none;
  border: none;
  font-size: 1.5em;
  cursor: pointer;
  color: #ccc;
  transition: color 0.2s;
  padding: 0;
  width: 30px;
  height: 30px;
}

.bookmark-btn:hover {
  color: #ffc107;
}

.bookmark-btn.bookmarked {
  color: #ffc107;
}

.reading-status {
  margin-top: 8px;
  padding: 6px 12px;
  background: #fff3e0;
  border-left: 3px solid #ff9800;
  font-size: 0.9em;
}

.paper-note {
  margin-top: 8px;
  padding: 8px 12px;
  background: #f1f8e9;
  border-left: 3px solid #8bc34a;
  font-size: 0.9em;
  font-style: italic;
}

.add-note-btn {
  margin-top: 8px;
  padding: 6px 12px;
  background: #e8eaf6;
  border: 1px solid #c5cae9;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9em;
  transition: background 0.2s;
}

.add-note-btn:hover {
  background: #c5cae9;
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
// Load user topics dynamically from API
let userEnabledTopics = new Set(); // Store enabled topic IDs

async function loadUserTopics() {
  try {
    const response = await fetch(API_BASE + '/api/user/config');
    const config = await response.json();
    const topicFilter = document.getElementById('topicFilter');
    
    // Clear existing options except "All Topics"
    topicFilter.innerHTML = '<option value="">All Topics</option>';
    
    // Build set of enabled topics (including children)
    userEnabledTopics.clear();
    
    // Add topics from user config
    config.topics.forEach(topic => {
      if (topic.enabled) {
        userEnabledTopics.add(topic.id);
        
        const option = document.createElement('option');
        option.value = topic.id;
        option.textContent = `${topic.icon || '📄'} ${topic.name}`;
        topicFilter.appendChild(option);
        
        // Add child topics if any
        if (topic.children && topic.children.length > 0) {
          topic.children.forEach(child => {
            if (child.enabled !== false) { // enabled by default
              userEnabledTopics.add(child.id);
              
              const childOption = document.createElement('option');
              childOption.value = child.id;
              childOption.textContent = `  └ ${child.icon || '📄'} ${child.name}`;
              topicFilter.appendChild(childOption);
            }
          });
        }
      }
    });
    
    console.log('✅ Loaded user topics:', userEnabledTopics.size, 'enabled topics');
    console.log('Enabled topics:', Array.from(userEnabledTopics));
    
    // Re-render papers with user filter
    filterAndSearch();
    
  } catch (error) {
    console.warn('⚠️ Could not load user topics from API, showing all papers');
    // Fallback: show all papers with default topic list
    const defaultTopics = [
      { id: 'ai-agents', name: 'AI Agents', icon: '🤖' },
      { id: 'llm-reasoning', name: 'LLM Reasoning', icon: '🧠' },
      { id: 'rag-retrieval', name: 'RAG & Retrieval', icon: '🔍' },
      { id: 'multi-modal', name: 'Multi-Modal', icon: '🎨' }
    ];
    
    const topicFilter = document.getElementById('topicFilter');
    defaultTopics.forEach(topic => {
      userEnabledTopics.add(topic.id);
      const option = document.createElement('option');
      option.value = topic.id;
      option.textContent = `${topic.icon} ${topic.name}`;
      topicFilter.appendChild(option);
    });
    
    filterAndSearch();
  }
}

// Load topics on page load
loadUserTopics();

// Paper data will be injected here
const papers = [
  {
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "arxiv_id": "2608.27506",
    "url": "https://arxiv.org/abs/2608.27506",
    "date": "2026-08-31",
    "authors": "Nolasque, T, Grey, J, Pham, C, Vani, A",
    "abstract": "Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there exists a token-budget threshold, below which the overhead of planning and verification hurts performance and above which it helps. We evaluate two systems on FinQA and TAT-QA financial reasoning tasks, using GPT-5.4 mini across 14 budget tiers ranging from 250 to 42,000 output-equivalent tokens. The first system is a monolith, which is a single LLM call. The second is a verified search architecture that adds planning, label-blind checking, and repair capabilities. We run 1,000 cases for a total of 28,000 completed cells. Both systems score 0% at the two lowest tiers, where neither can fit a complete prompt. At 1,000 tokens, the monolith reaches 18% accuracy while verified search scores near 0%, since the planning overhead leaves no room for an answer. From 1,500 tokens onward, verified search surpasses the monolith and maintains a consistent advantage, reaching approximately 44% at the highest tiers while the monolith reaches approximately 40%. The crossover occurs between 1,000 and 1,500 output-equivalent tokens, confirmed by a strict intersection-union test ($p \\le 0.001$ at both endpoints).",
    "topics": [
      "llm-reasoning"
    ]
  },
  {
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "arxiv_id": "2608.27471",
    "url": "https://arxiv.org/abs/2608.27471",
    "date": "2026-08-31",
    "authors": "Dore, D, Damo, G, Cabrio, E, Villata, S",
    "abstract": "Fallacies are arguments that employ invalid reasoning, making their automatic detection critical in sensitive contexts such as high-stakes political debates, where public opinion is shaped. Spotting a fallacious argument requires contextual knowledge beyond its pure surface text. This entails world knowledge pertaining to the subject matter under discussion, as well as knowledge of the relationships that exist between arguments within the argumentative discourse. Prior work on fallacy analysis has shown that argumentative discourse structure can beneficially improve classification performance. However, such structure is typically encoded only as static classifier features, limiting its flexibility. Building on this intuition while addressing this limitation, we introduce a guided retrieval-augmented methodology for fallacy detection and classification that leverages argumentative relations of support and attack to dynamically steer the extraction of relevant documents. We evaluate our approach on the ElecDeb60to20 benchmark across 42 retrieval configurations and 14 models, performing retrieval over a 15GB knowledge base of collected political-related documents. Our approach improves macro-F1 up to 0.864 for fallacy detection and up to 0.725 for classification over non-retrieval baselines. These results show that incorporating external knowledge significantly enhances fallacy detection and classification when retrieval is argumentatively guided.",
    "topics": [
      "rag-retrieval"
    ]
  },
  {
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "arxiv_id": "2608.27646",
    "url": "https://arxiv.org/abs/2608.27646",
    "date": "2026-08-31",
    "authors": "Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "abstract": "Give an agent a human&#39;s credential and it inherits the person&#39;s reach without the judgment that limits its use. It can sweep every reachable record into model context, where hidden instructions steer its next call, and every request stays credential-valid while the agent exceeds its job or absorbs a secret. Prompts are a brittle guardrail: one fallible reasoner interprets the task and enforces its limits.\nWe present Out-of-Band Policy Enforcement (OBPE), a trusted boundary outside agent reasoning. It authorizes the typed operation and resource, narrows the query before the backend call, then filters records and fields or masks values in the response. Semantic gating can deny or hold an authorized call on argument values or external state. A data policy owner sets the maximum grant; agent policy can only narrow it. We prove, under stated conditions, that the policy plan is order-independent and agent policy cannot widen the ceiling. Field removal covers one execution; masking and history rules claim less.\nWe release an HTTP proxy prototype simplified from our production system, with conformance tests tying its typed Cedar policy core to the model. Against Jira and ServiceNow mocks, our benchmark compares prompted agents with and without OBPE on four models, including 20 adaptive red-team tasks. A trace failure means protected data entered agent context, an exact value appeared in the answer, or a forbidden effect completed. In 3,621 trials it fell from 57.6% to 0.2%, a cluster-weighted reduction of 41.2 points [95% CI: 27.7, 54.9]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ]
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "arxiv_id": "2608.27475",
    "url": "https://arxiv.org/abs/2608.27475",
    "date": "2026-08-31",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ]
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "arxiv_id": "2608.27840",
    "url": "https://arxiv.org/abs/2608.27840",
    "date": "2026-08-31",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ]
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "arxiv_id": "2608.27508",
    "url": "https://arxiv.org/abs/2608.27508",
    "date": "2026-08-31",
    "authors": "Han, Y, Qian, T",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ]
  },
  {
    "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
    "arxiv_id": "2608.27484",
    "url": "https://arxiv.org/abs/2608.27484",
    "date": "2026-08-31",
    "authors": "Ghawate, P, Patil, T",
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ]
  },
  {
    "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
    "arxiv_id": "2608.27953",
    "url": "https://arxiv.org/abs/2608.27953",
    "date": "2026-08-31",
    "authors": "Wang, Y, Du, Y, Liu, Z, Zhang, R, Zhao, B, Yang, B, Kong, M, Qu, L, Wei, H, Liu, J, Zhu, Q",
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ]
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "arxiv_id": "2608.27963",
    "url": "https://arxiv.org/abs/2608.27963",
    "date": "2026-08-31",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ]
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "arxiv_id": "2608.27945",
    "url": "https://arxiv.org/abs/2608.27945",
    "date": "2026-08-31",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ]
  },
  {
    "title": "MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places",
    "arxiv_id": "2608.28384",
    "url": "https://arxiv.org/abs/2608.28384",
    "date": "2026-08-31",
    "authors": "Armitage, J, Tsochantaridis, I, Mazzone, L, Yan, C, Narayanan, S, Ebling, S",
    "abstract": "We introduce MAP, the first benchmark to evaluate multimodal AI systems as assistants for users with accessibility requirements when planning visits to places in the real world. In our evaluation, systems are presented with requests to verify or recommend a point of interest meeting an accessibility requirement. MAP contains two novel assessments: Claim verification for accessibility planning assesses if information on places and stated accessibility features is supported and identifies places that satisfy requested accessibility features. Visual evidence retrieval for accessibility planning checks if a multimodal AI system can select visual evidence for the requested place and accessibility feature. Our methodology supports comparison of AI systems in a setting where place information and accessibility information can change over time by evaluating systems and refreshing ground truth data at scheduled times. The benchmark is based on automatic rating and human rating for a proportion of responses.",
    "topics": [
      "ai-agents",
      "multi-modal"
    ]
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "arxiv_id": "2608.27869",
    "url": "https://arxiv.org/abs/2608.27869",
    "date": "2026-08-31",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
    "topics": [
      "ai-agents",
      "multi-modal"
    ]
  },
  {
    "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
    "arxiv_id": "2608.27524",
    "url": "https://arxiv.org/abs/2608.27524",
    "date": "2026-08-31",
    "authors": "Tejas, J M, Roy, U B, Goswami, T, Goswami, S, Dhar, M",
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ]
  },
  {
    "title": "WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents",
    "arxiv_id": "2608.28062",
    "url": "https://arxiv.org/abs/2608.28062",
    "date": "2026-08-31",
    "authors": "Liu, Z, Zhang, H, Niu, L, Cao, Z, Li, H, Liu, J, Chen, W, Zhao, C, Yu, C, Meng, F",
    "abstract": "Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as text and omit tool-returned images from subsequent context, reducing visually grounded trajectories to text-only reasoning. Long-horizon interaction also compounds tool-call, response-length, timeout, and budget failures, which can discard salvageable trajectories, waste rollout computation, and disturb policy updates. To address these issues, we introduce WeAgent-Harness, a multimodal agentic harness that supports native text-vision interaction and runtime recovery. Retrieved images receive persistent disk references, allowing the model to inspect, process, and cite them throughout the trajectory. Based on this harness, we develop WeAgent-MMSearch, an integrated system spanning data construction, agentic post-training, and multimodal rollout. For data construction, a strong MLLM uses WeAgent-Harness to discover, synthesize, and verify MMSearch-style tasks and collect expert trajectories. During post-training, our Failure-Aware GSPO (FA-GSPO) recovers salvageable abnormal rollouts and filters invalid ones to improve bounded multimodal planning and this http URL also introduce VisTarget-Bench, a 150-task human-verified benchmark that pairs each question with a held-out target image, distinguishing image-retrieval failures from visual-perception failures. Evaluation on VisTarget-Bench and seven public benchmarks shows that agentic post-training improves the average score by 19.22 points, enabling our model to outperform similarly sized open-source models and rival models with roughly ten times its parameter count.",
    "topics": [
      "ai-agents",
      "multi-modal"
    ]
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "arxiv_id": "2608.27548",
    "url": "https://arxiv.org/abs/2608.27548",
    "date": "2026-08-31",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ]
  },
  {
    "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
    "arxiv_id": "2608.27867",
    "url": "https://arxiv.org/abs/2608.27867",
    "date": "2026-08-31",
    "authors": "Liu, R, Gu, N, Ai, M, Li, Y, Fu, P, Lin, Z, Wang, W",
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ]
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "arxiv_id": "2608.27919",
    "url": "https://arxiv.org/abs/2608.27919",
    "date": "2026-08-31",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.\nIn this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ]
  }
];

function renderPapers(filteredPapers) {
  const resultsDiv = document.getElementById('searchResults');
  const countDiv = document.getElementById('resultsCount');
  
  countDiv.textContent = `Found ${filteredPapers.length} paper${filteredPapers.length !== 1 ? 's' : ''}`;
  
  if (filteredPapers.length === 0) {
    resultsDiv.innerHTML = '<p style="text-align: center; color: #666; padding: 40px;">No papers found matching your criteria.</p>';
    return;
  }
  
  resultsDiv.innerHTML = filteredPapers.map(paper => {
    const isBookmarked = userBookmarks.has(paper.arxiv_id);
    const note = userNotes.get(paper.arxiv_id) || '';
    const readingStatus = userReadingProgress.get(paper.arxiv_id)?.status || '';
    
    return `
<div class="paper-card" data-arxiv-id="${paper.arxiv_id}">
<div class="paper-header">
<h3 class="paper-title">
<a href="${paper.url}" target="_blank">${paper.title}</a>
</h3>
<button class="bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleBookmark('${paper.arxiv_id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Add bookmark'}">
            ${isBookmarked ? '★' : '☆'}
</button>
</div>
<div class="paper-meta">
<span class="paper-authors">${paper.authors}</span>
<span class="paper-date">${paper.date}</span>
<span class="paper-arxiv">arXiv:${paper.arxiv_id}</span>
</div>
<div class="paper-abstract">${paper.abstract}</div>
<div class="paper-topics">
          ${paper.topics.map(topic => `<span class="topic-tag">${topic}</span>`).join('')}
</div>
        ${readingStatus ? `<div class="reading-status">Status: <strong>${readingStatus}</strong></div>` : ''}
        ${note ? `<div class="paper-note"><strong>Your note:</strong> ${note}</div>` : ''}
<button class="add-note-btn" onclick="showNoteDialog('${paper.arxiv_id}')">
          ${note ? 'Edit Note' : 'Add Note'}
</button>
</div>
    `;
  }).join('');
}

function filterAndSearch() {
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();
  const topicFilter = document.getElementById('topicFilter').value;
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = papers.filter(paper => {
    const matchesSearch = !searchTerm || 
      paper.title.toLowerCase().includes(searchTerm) ||
      paper.authors.toLowerCase().includes(searchTerm) ||
      paper.abstract.toLowerCase().includes(searchTerm);
    
    // Filter by selected topic in dropdown
    const matchesTopicDropdown = !topicFilter || paper.topics.includes(topicFilter);
    
    // Filter by user's enabled topics (only show papers matching at least one enabled topic)
    const matchesUserTopics = userEnabledTopics.size === 0 || 
      paper.topics.some(topic => userEnabledTopics.has(topic));
    
    return matchesSearch && matchesTopicDropdown && matchesUserTopics;
  });
  
  // Sort
  filtered.sort((a, b) => {
    if (sortBy === 'date') {
      return new Date(b.date) - new Date(a.date);
    } else if (sortBy === 'title') {
      return a.title.localeCompare(b.title);
    } else if (sortBy === 'authors') {
      return a.authors.localeCompare(b.authors);
    }
    return 0;
  });
  
  renderPapers(filtered);
}

// User data storage
let userBookmarks = new Set();
let userNotes = new Map();
let userReadingProgress = new Map();

// Load user data from API
async function loadUserData() {
  try {
    const response = await fetch(API_BASE + '/api/user/data');
    const data = await response.json();
    
    userBookmarks = new Set(data.bookmarks || []);
    userNotes = new Map(Object.entries(data.notes || {}));
    userReadingProgress = new Map(Object.entries(data.readingProgress || {}));
    
    console.log('✅ Loaded user data:', {
      bookmarks: userBookmarks.size,
      notes: userNotes.size,
      readingProgress: userReadingProgress.size
    });
  } catch (error) {
    console.warn('⚠️ Could not load user data:', error);
  }
}

// Toggle bookmark
async function toggleBookmark(arxivId) {
  const isBookmarked = userBookmarks.has(arxivId);
  
  try {
    const response = await fetch(`${API_BASE}/api/user/bookmarks/${arxivId}`, {
      method: isBookmarked ? 'DELETE' : 'POST'
    });
    
    if (response.ok) {
      const data = await response.json();
      userBookmarks = new Set(data.bookmarks);
      filterAndSearch(); // Re-render to show updated bookmark state
    }
  } catch (error) {
    console.error('Failed to toggle bookmark:', error);
  }
}

// Show note dialog
function showNoteDialog(arxivId) {
  const currentNote = userNotes.get(arxivId) || '';
  const newNote = prompt('Enter your note for this paper:', currentNote);
  
  if (newNote !== null) {
    saveNote(arxivId, newNote);
  }
}

// Save note
async function saveNote(arxivId, note) {
  try {
    const response = await fetch(`${API_BASE}/api/user/notes/${arxivId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ note })
    });
    
    if (response.ok) {
      if (note) {
        userNotes.set(arxivId, note);
      } else {
        userNotes.delete(arxivId);
      }
      filterAndSearch(); // Re-render to show updated note
    }
  } catch (error) {
    console.error('Failed to save note:', error);
  }
}

// Event listeners
document.getElementById('searchInput').addEventListener('input', filterAndSearch);
document.getElementById('topicFilter').addEventListener('change', filterAndSearch);
document.getElementById('sortBy').addEventListener('change', filterAndSearch);

// Initial load
loadUserTopics();
loadUserData();
</script>
