---
title: "Concept Tag Cloud"
---

<div class="tagcloud-container">
<div class="tagcloud-controls">
<select id="topicFilter" class="filter-select">
<option value="all">All Topics</option>
<option value="ai-agents">AI Agents</option>
<option value="llm-reasoning">LLM Reasoning</option>
<option value="rag-retrieval">RAG & Retrieval</option>
<option value="multi-modal">Multi-Modal</option>
</select>
<div class="view-toggle">
<button id="cloudView" class="view-btn active">Cloud View</button>
<button id="listView" class="view-btn">List View</button>
</div>
</div>
  
<div id="tagCloud" class="tag-cloud"></div>
<div id="tagList" class="tag-list" style="display:none"></div>
  
<div id="tagDetails" class="tag-details"></div>
</div>

<style>
.tagcloud-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.tagcloud-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 15px;
}

.filter-select {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  background: white;
}

.view-toggle {
  display: flex;
  gap: 5px;
}

.view-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 14px;
}

.view-btn:first-child {
  border-radius: 6px 0 0 6px;
}

.view-btn:last-child {
  border-radius: 0 6px 6px 0;
}

.view-btn.active {
  background: #4a90e2;
  color: white;
  border-color: #4a90e2;
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 15px;
  padding: 40px 20px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 12px;
  min-height: 400px;
}

.tag-item {
  display: inline-block;
  padding: 8px 16px;
  background: white;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  font-weight: 500;
}

.tag-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.tag-item.size-1 { font-size: 12px; }
.tag-item.size-2 { font-size: 14px; }
.tag-item.size-3 { font-size: 16px; }
.tag-item.size-4 { font-size: 18px; }
.tag-item.size-5 { font-size: 22px; }
.tag-item.size-6 { font-size: 26px; }
.tag-item.size-7 { font-size: 32px; }
.tag-item.size-8 { font-size: 38px; }
.tag-item.size-9 { font-size: 44px; }
.tag-item.size-10 { font-size: 52px; }

.tag-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 15px;
}

.tag-list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: all 0.2s;
}

.tag-list-item:hover {
  transform: translateX(5px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.tag-list-name {
  font-weight: 600;
  color: #2c3e50;
}

.tag-list-count {
  background: #4a90e2;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
}

.tag-details {
  margin-top: 30px;
  padding: 25px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.1);
  display: none;
}

.tag-details.active {
  display: block;
}

.tag-details h3 {
  margin-top: 0;
  color: #2c3e50;
  border-bottom: 2px solid #4a90e2;
  padding-bottom: 10px;
}

.tag-details-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 15px;
  color: #666;
  font-size: 14px;
}

.tag-details-papers {
  list-style: none;
  padding: 0;
}

.tag-details-papers li {
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.tag-details-papers li:last-child {
  border-bottom: none;
}

.tag-details-papers a {
  color: #4a90e2;
  text-decoration: none;
  font-weight: 500;
}

.tag-details-papers a:hover {
  text-decoration: underline;
}

.tag-details-date {
  color: #999;
  font-size: 13px;
  margin-left: 10px;
}
</style>

<script>
const papers = [
  {
    "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
    "authors": "Yulong Zhang, Li Wang, Wei Du, Peilin Li, Yuqin Dai Zhiyuan Zhao, Lingyong Fang, Ziniu Liu, Ru Zhang, Huijia Zhu, Gongshen Liu",
    "date": "2025-10-03",
    "abstract": "Verifying multi-step reasoning in large language models is difficult due to imprecise error localization and high token costs. Existing methods either assess entire reasoning chains, suffering attention dilution, or rely on expensive multi-sampling. We introduce Node-wise Consistency Verification (NCV), a training-free framework that recasts verification as lightweight binary consistency checks at the node level. By decomposing the chain of thought into interconnected verification nodes, NCV precisely localizes errors and avoids unnecessary long-form generation. Experiments demonstrate that our approach enhances interpretability and efficiency, presenting a scalable solution for reliable LLM reasoning verification. On public datasets, NCV achieves a 10\\% to 25\\% improvement in F1 scores over baselines while utilizing $6\\times$~$58\\times$ fewer tokens than traditional methods like CoT-based verifiers.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html"
  },
  {
    "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
    "authors": "V\u00edctor Gallego",
    "date": "2026-05-28",
    "abstract": "We study two-level autoresearch for cooperation: an outer-loop AI agent autonomously redesigns the inner-loop pipeline of an LLM policy-synthesis system for multi-agent Sequential Social Dilemmas (SSDs). A researcher agent $\\mathcal{R}$ (run as a coding agent) reads the inner-loop source code, edits system prompts, feedback functions, helper libraries, and iteration logic, runs evaluations, and decides what to keep, following the autoresearch paradigm. Across two games (Cleanup and Gathering), two policy-synthesizer LLMs, and two welfare objectives (utilitarian efficiency and Rawlsian maximin), the researcher reliably exceeds hand-designed baselines, sharply tightens run-to-run variance, and outperforms prompt-only optimization. The discovered pipelines are objective-dependent: only under maximin does the researcher inject an explicit fairness mechanism into synthesizer pipelines, a class of mechanism that is absent from its own objective-agnostic system prompt and from every efficiency-optimized pipeline. This supports an information-design reading in which the researcher chooses what to reveal to the boundedly rational synthesizer as a function of the welfare objective. Code at https://github.com/vicgalle/autoresearch-social-dilemmas.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-28/2605.30003v1-Discovering-Cooperative-Pipelines-Autoresearch-for-Sequential-Social-Dilemmas.html"
  },
  {
    "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
    "authors": "Yujuan Ding, Linyin Luo, Shijie Wang, Xu Yuan, Yunshan Ma, Yi Bin, Wenqi Fan, Qing Li",
    "date": "2026-08-24",
    "abstract": "Fashion is a knowledge-intensive domain in which effective decision-making depends on integrating multiple types of knowledge. Although Large Language Models (LLMs) have transformed many areas, their application in fashion remains limited by hallucinations and weak domain specialization. Knowledge Graph (KG)-based ragragRetrieval-Augmented Generation (RAG) offers a promising way to add structured knowledge to LLMs. However, existing fashion KGs are typically restricted to product-level attributes or item relations, and fail to capture the broader fashion ecosystem. To bridge these gaps, we propose \\textbf{FashionEcoKG}, a comprehensive, domain-wide knowledge graph built with expert-level precision and professionalism. It is constructed through a three-stage agentic pipeline that extracts high-fidelity knowledge cores from authoritative textbooks and strengthens structural connectivity through cross-domain augmentation and generative expansion. To leverage this resource, we further develop \\textbf{PG-RAG} (Pruning-Grounding RAG), a training-free framework designed to handle the conceptual density and linguistic noise of fashion queries. Specifically, we introduce a Dual-Granularity Path Re-Ranking (DGPR) module of two stages. The Pruning-based Semantic Ranking (PSR) module distills each query into a skeleton form to improve retrieval recall, while the Grounding-based Agentic Ranking (GAR) performs point-wise scrutiny of candidate paths against the original full query to ensure global relevance. Experiments on a curated fashion QA dataset show that PG-RAG effectively leverages FashionEcoKG to improve retrieval and answer accuracy, outperforming both non-RAG and existing KG-RAG baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html"
  },
  {
    "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
    "authors": "Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib, Yordanos Tessema, Chang-Tien Lu",
    "date": "2026-08-23",
    "abstract": "Current work on improving reliability in llmllmlarge language model (LLM)- generated answers has primarily leveraged ragragRetrieval-Augmented Generation (RAG), knowledge-graph augmentation, and reinforcement learning. While these methods are adept at enhancing and measuring reliability through semantic similarity and faithfulness, they often struggle to distinguish semantic similarity from geographic validity. This is especially critical in natural hazard management domains where geographic granularity (i.e., town vs. city vs. state) is significant for decision-making, as responses valid in one municipality may not transfer to another. In such domains, a confidently wrong answer carries greater risk than abstaining. We present GeoRisk-RAG, a novel hierarchy-aware framework that addresses this geographic-validity gap through selective answering. This framework explicitly estimates geographic applicability using a Directed Acyclic Graph (DAG)-based distance for context retrieval before response generation. Experiments on a novel held-out wildfire-related question-answering (QA) dataset show that GeoRisk-RAG significantly reduces false confidence rates for location-dependent questions, lowering the rate to 0.009 compared with ~0.090 for standard semantic similarity and reranking baselines, while consistently achieving higher human preference alignment. This work provides a more comprehensive assessment of end-to-end RAG pipelines by integrating geographic validity and selective-answering behavior for safer decision-making in geospatial domains.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html"
  },
  {
    "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
    "authors": "Yuhan Meng, Shaofei Li, Jionghao Huang, Jiandong Jin, Puyi Wang, Hanlin Jiang, Anis Yusof, Peng Jiang, Zhenkai Liang, Yao Guo, Ding Li",
    "date": "2026-08-15",
    "abstract": "The rapid advancement of large language models (LLMs) has created a growing asymmetry in cybersecurity, where attack accelerates toward autonomous execution while defense remains predominantly human-intensive. Despite substantial prior work across cyber ranges, AI-driven attack, and AI-driven defense, this asymmetry persists. We trace it to a deeper root cause, that evolution itself has stalled on both sides at three layers. To overcome this, we propose co-evolution as the integrating insight, where attack and defense AI agents autonomously and safely drive each other's evolution through adversarial confrontation. Based on this insight, we present \\sysevolve, comprising three co-designed components, \\sysfield, \\sysspear, and \\sysarmor. \\sysfield constructs realistic multi-host ranges. \\sysspear generates efficient, safe attack schemes. \\sysarmor performs real-time, interpretable defense. Together they form a self-driven adversarial loop restoring evolution at all three layers. In evaluation, \\sysfield achieves zero-loss collection at 2.1\\% overhead and orchestrates 257 CVEs into 1,148 ranges, \\sysspear improves attack success by over 25\\% over baseline LLMs, and \\sysarmor achieves 10--1000$\\times$ greater precision than prior systems and detects real APT attacks in production at Huawei and Sangfor. Our evaluation also reveals three findings about LLM agent capabilities. First, multi-step composition and larger topologies expose agent capability gaps hidden by single-step evaluations. Second, the bottleneck lies after initial access in post-compromise state utilization. Third, LLM agents are susceptible to environmental interference. When decoy endpoints are deployed in the range, agent timeouts triple and downstream completion disappears despite the success rates of initial accesses are unchanged.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html"
  },
  {
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "authors": "Nolasque, T, Grey, J, Pham, C, Vani, A",
    "date": "2026-08-31",
    "abstract": "Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there exists a token-budget threshold, below which the overhead of planning and verification hurts performance and above which it helps. We evaluate two systems on FinQA and TAT-QA financial reasoning tasks, using GPT-5.4 mini across 14 budget tiers ranging from 250 to 42,000 output-equivalent tokens. The first system is a monolith, which is a single LLM call. The second is a verified search architecture that adds planning, label-blind checking, and repair capabilities. We run 1,000 cases for a total of 28,000 completed cells. Both systems score 0% at the two lowest tiers, where neither can fit a complete prompt. At 1,000 tokens, the monolith reaches 18% accuracy while verified search scores near 0%, since the planning overhead leaves no room for an answer. From 1,500 tokens onward, verified search surpasses the monolith and maintains a consistent advantage, reaching approximately 44% at the highest tiers while the monolith reaches approximately 40%. The crossover occurs between 1,000 and 1,500 output-equivalent tokens, confirmed by a strict intersection-union test ($p \\le 0.001$ at both endpoints).",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html"
  },
  {
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "authors": "Dore, D, Damo, G, Cabrio, E, Villata, S",
    "date": "2026-08-31",
    "abstract": "Fallacies are arguments that employ invalid reasoning, making their automatic detection critical in sensitive contexts such as high-stakes political debates, where public opinion is shaped. Spotting a fallacious argument requires contextual knowledge beyond its pure surface text. This entails world knowledge pertaining to the subject matter under discussion, as well as knowledge of the relationships that exist between arguments within the argumentative discourse. Prior work on fallacy analysis has shown that argumentative discourse structure can beneficially improve classification performance. However, such structure is typically encoded only as static classifier features, limiting its flexibility. Building on this intuition while addressing this limitation, we introduce a guided retrieval-augmented methodology for fallacy detection and classification that leverages argumentative relations of support and attack to dynamically steer the extraction of relevant documents. We evaluate our approach on the ElecDeb60to20 benchmark across 42 retrieval configurations and 14 models, performing retrieval over a 15GB knowledge base of collected political-related documents. Our approach improves macro-F1 up to 0.864 for fallacy detection and up to 0.725 for classification over non-retrieval baselines. These results show that incorporating external knowledge significantly enhances fallacy detection and classification when retrieval is argumentatively guided.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html"
  },
  {
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "authors": "Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "date": "2026-08-31",
    "abstract": "Give an agent a human&#39;s credential and it inherits the person&#39;s reach without the judgment that limits its use. It can sweep every reachable record into model context, where hidden instructions steer its next call, and every request stays credential-valid while the agent exceeds its job or absorbs a secret. Prompts are a brittle guardrail: one fallible reasoner interprets the task and enforces its limits. We present Out-of-Band Policy Enforcement (OBPE), a trusted boundary outside agent reasoning. It authorizes the typed operation and resource, narrows the query before the backend call, then filters records and fields or masks values in the response. Semantic gating can deny or hold an authorized call on argument values or external state. A data policy owner sets the maximum grant; agent policy can only narrow it. We prove, under stated conditions, that the policy plan is order-independent and agent policy cannot widen the ceiling. Field removal covers one execution; masking and history rules claim less. We release an HTTP proxy prototype simplified from our production system, with conformance tests tying its typed Cedar policy core to the model. Against Jira and ServiceNow mocks, our benchmark compares prompted agents with and without OBPE on four models, including 20 adaptive red-team tasks. A trace failure means protected data entered agent context, an exact value appeared in the answer, or a forbidden effect completed. In 3,621 trials it fell from 57.6% to 0.2%, a cluster-weighted reduction of 41.2 points [95% CI: 27.7, 54.9]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments. In this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a ragragretrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ``perfect blocking'' construction supplies equilibrated long-distance modes, while a conditional normalizing flow reconstructs short-distance details and brief rethermalization removes residual errors. In 2D $\u03c6^4$ theory at criticality, a flow trained at $L\\le32$ is reused recursively in cascades reaching $L=2048$ with correct long-distance physics.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "abstract": "We derive necessary conditions for instantaneous dynamo action for rotating convection. A magnetohydrodynamic model is considered in two settings: the rapidly rotating plane layer where inertia and viscosity are absent, and at an arbitrary rotation rate where viscosity is finite. In contrast to kinematic dynamo bounds, the evolution of the magnetic field is coupled via an inertialess force balance. The buoyancy-driven part of the flow $\\mathbf{u}^{\\mathrm{A}}$ in the event of dynamo action must in fact satisfy, for $3\\leq p \\leq \\infty$ $$ Rm\\, A_p\\| \\mathbf{u}^{\\mathrm{A}}\\|_{L^p} \\geq 1 $$ where $A_p$ is an explicit constant, and $Rm$ is the magnetic Reynolds number. In the inviscid model, $\\mathbf{u}^{\\mathrm{A}}$ depends only on the horizontal gradients of the vertical primitive of temperature. A refinement via the poloidal-toroidal decomposition allows us to replace $L^p$ in our constraint with an anisotropic norm for $L^{\\infty}_z \\dot{H}^1_{x,y}$. For the viscous model, we also derive necessary conditions for the growth of magnetic enstrophy and a combined thermo-magnetic energy. One branch of our constraints implies that the scaling $Ra_\u03bd\\gtrsim Ek^{-3/2}$ is necessary for dynamo action, where $Ra_\u03bd$ is the classical Rayleigh number and $Ek$ is the Ekman number.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "abstract": "Crystalline C$_{60}$ is a molecular solid whose electronic properties emerge from the interplay of intermolecular hopping, electron correlations, and electron-vibration coupling. Unlike moir$\\rm\\acute{e}$ van der Waals heterostructures, where interaction strength is commonly tuned by twist angle, molecular materials offer a complementary route in which layer number, molecular orientation, and substrate registry provide experimentally accessible control parameters. Here we present a systematic thickness-dependent angle-resolved photoemission study of C$_{60}$ films, spanning the monolayer to the bulk limit. The HOMO-derived band exhibits a non-monotonic evolution: the intermediate-thickness film shows larger bandwidth, reduced effective mass, and pronounced gap-like and sub-band features. The experimental trends, together with Holstein-model simulations, point to strengthened effective intermolecular electronic coupling and enhanced electron-phonon-induced spectral renormalization in the intermediate-thickness regime. These results identify a dimensional crossover in C$_{60}$ films and establish layer number as an effective knob for engineering electronic structure and many-body interactions in molecular thin films.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "abstract": "Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "abstract": "Nested sampling is widely used for Bayesian evidence computation, but its intrinsically sequential structure limits how efficiently it can exploit modern vectorised likelihoods and emulators. We present a new nested-sampling implementation in \\textsc{best}, written entirely in TensorFlow and designed for efficient XLA compilation on both CPUs and GPUs. The sampler combines clustering and slice sampling with the possibility of updating several live points simultaneously. Since batching breaks the strict ordering of conventional nested sampling, we introduce sorting and history-based corrections to reduce the resulting bias in the evidence estimate. We test the sampler on Gaussian, Rosenbrock, and multimodal likelihoods and compare its performance with JAXNS and UltraNest. The results show that accurate evidence estimates can be retained for moderate batch sizes, with $m/N_{\\rm live}\\lesssim 0.1$ providing a useful practical regime. Finally, using a 27-dimensional cosmological likelihood emulator, we show that batched live-point updates can substantially reduce the wall-clock time while remaining consistent with sequential sampling within the reported uncertainties. The new implementation therefore extends \\textsc{best} with an efficient nested-sampling method tailored to fast, vectorised likelihoods and emulator-based inference.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "abstract": "A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "abstract": "Multimodal sequential recommendation (MSR) improves recommendation by incorporating heterogeneous information such as text, images, and user interactions. However, existing MSR methods often fail to capture user-level preference heterogeneity and dataset-level modality bias, limiting their adaptability across users and datasets. To address this issue, we propose \\textbf{S}equence-\\textbf{G}uided \\textbf{U}niversal \\textbf{M}ultimodal \\textbf{P}rioritization Calculation Framework (\\textbf{SG-UMP}), a plug-and-play plugin for enhancing multimodal information processing in MSR. SG-UMP includes a Module Combiner for flexible multimodal processing and a Module Router for dynamic module ordering, enabling adaptation to both user preferences and dataset characteristics. Experiments on four real-world datasets show that SG-UMP consistently improves recommendation performance across different backbones and multimodal settings. The code is available at https://github.com/esemsc-xz524/SG-UMP .",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "abstract": "For a vertex operator algebra $V$ and a suitable category of its modules, we propose a construction for spaces of conformal blocks organized into an open-closed modular functor with singularities. This is inspired by the idea of implementing directly from the start the principle of holomorphic factorization. More precisely, using the strategy of modular extension introduced by Costello and developed further in our previous work, we build for each surface $\u03a3$ with at least one boundary component per path component and specified boundary labels attached to marked intervals or boundary circles a representation $\u03a9_V(\u03a3;-)$ of the mapping class group of $\u03a3$. The construction can be described explicitly on generating Dehn twists. This approach is a priori independent from other constructions based on algebraic geometry or topological techniques involving e.g. surgery, but we include an overview over the available comparisons. In the special case in which the module category of $V$ is a not necessarily semisimple modular category $\\mathcal{A}$, the spaces $\u03a9_V(\u03a3)$ are equivalent to the string-net spaces for $\\mathcal{A}$ and hence to the modular functor for the Drinfeld center $Z(\\mathcal{A})\\simeq \\bar{\\mathcal{A}}\\boxtimes\\mathcal{A}$. However, the construction of $\u03a9_V$ in this paper has the advantage of being available beyond rationality, rigidity, self-contragredience and finiteness. Moreover, we prove that $\u03a9_V$ satisfies excision, is finite-dimensional in the $C_2$-cofinite case and produces representations of surface braid groups generalizing the ones of Brochier-Jordan. We prove for the triplet $\\mathcal{W}_{2,3}$ with non-exact fusion product that the boundary conditions introduced by Gaberdiel-Runkel-Wood produce correlation functions, provided that one uses the notion of a modular functor with singularities that we develop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "abstract": "The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images. To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (https://github.com/llm-jp/synth-jdoc).",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "abstract": "Institutional investors search visually dense pitch decks, board packs, and diligence materials that change hourly near deal closing. OCR followed by figure verbalisation is costly to refresh at this scale and can lose chart detail. We present PULSAR, a production vision-first retrieval system deployed at Mubadala Investment Company. PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3, this design reduces median vector-search latency by 15.1 times against an unpooled configuration with less than 0.01 absolute NDCG@10 and Recall@10 loss; production median vector-search latency is 156 ms. Under concurrent load, the pooled index sustains approximately 88 times higher QPS than an unpooled index. The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced. Since March 2026, PULSAR has served 78 thousand documents and approximately 2.4 million pages across more than 3,000 deals. At the production top K, it more than doubles answer-fact recall over the OCR+verbalisation baseline.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "abstract": "Density three-point correlations are known to probe the topology of the Fermi sea in two-dimensional noninteracting systems. Here, we study how these correlations are modified by interactions using the coadjoint-orbit effective field theory. A key advantage of the coadjoint-orbit formulation is that it provides a systematic way to incorporate generalized Landau interactions in terms of bosonized degrees of freedom, mapping fermionic loop contributions onto simpler tree-level diagrams. We show that, for a general isotropic dispersion $\u03b5(p)$, even at linear order in the generalized Landau interaction, $\\mathcal{O}(\\mathcal{F}^{(2,0)})$, there exists a contribution proportional to the band curvature $\u03b5''(p_F)$ that changes the nonanalytic structure of the free density three-point correlation function. This contribution introduces a distinct nonanalytic structure beyond that found in either the noninteracting case or an interacting Galilean-invariant system, showing that interaction effects can modify the topology-detecting density three-point correlation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "abstract": "We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\\bar\u03bd$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $\u03c7^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\\widetilde O(d^2)$ mixing bound in $\u03c7^2$-divergence, improving on the previous $\\widetilde O(d^{9/4})$ bound.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "abstract": "Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using llmllmlarge language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "abstract": "Software architecture is often only partially captured in code, while much of the design intent lives in evolving project artifacts. In agile projects, work items, user stories, and related tracking documents preserve valuable traces of that intent, but they rarely support direct architectural analysis. This work investigates the recovery of C4 architecture diagrams from historical agile work items using an LLM-based pipeline. The semi-automatic five-step workflow employs a prompt chain, bidirectional traceability, and Chain-of-Thought reasoning to transform unstructured Azure DevOps work items into visual artifacts. Evaluated on two industry projects, we use a mixed-methods design combining qualitative expert interviews with a quantitative stability analysis. Practitioners perceive the generated architectural baselines as accurate and highly useful for system comprehension. Strictly bound by their input data, the artifacts mirror the documented intent, thereby surfacing discrepancies and architectural drift when compared to the implemented reality. Quantitatively, the workflow exhibits high stability for architectural entities but lower stability for their relationships, with relative variance compounding across generation steps. The proposed workflow demonstrates the practical viability of LLM-assisted architectural recovery based on development process artifacts.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "abstract": "Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "abstract": "Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "abstract": "Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\\%$ of total parameters).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "abstract": "Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "abstract": "Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "abstract": "Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We propose an algorithm for generating lattice field configurations based on the approximate inversion of a renormalization-group blocking transformation. We optimize the blocking transformation using a ``perfect blocking'' condition so that the blocked lattice distribution is well approximated by a simple coarse action. The blocking is separated into an invertible smoothing transformation followed by decimation. Machine learning, in the form of a conditional normalizing flow, is used to reconstruct the short-distance degrees of freedom removed by the decimation. A short fine-action rethermalization then removes the residual mismatch. Because the coarse ensemble supplies the long-distance modes, the same blocking transformation and conditional flow can be reused recursively on larger lattices, producing a cascade of configurations from an initial small-volume ensemble. We test the method in two-dimensional $\u03c6^4$ theory with $\u03bb=1$ at criticality and demonstrate stable cascade upscaling from $16^2$ to $2048^2$ lattices on local computational resources. Controlled rethermalization tests show that short-distance mismatches relax rapidly, whereas a deliberately introduced mismatch in the relevant thermal direction relaxes much more slowly. The construction uses ingredients that admit natural extensions to higher-dimensional systems and, ultimately, to gauge and fermionic degrees of freedom.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "abstract": "Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "abstract": "We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embeddingembeddingembeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "abstract": "Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: https://github.com/topo-focus/Topofocus",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "abstract": "A protein's function follows from the structure it adopts, and which structure that is depends on the pathway taken. In programmable matter the target is fixed before assembly, and whatever else forms is treated as error. Here we show that pathways themselves form a design space. Using reinforcement learning, we fold model DNA-coated droplet chains into rigid two-dimensional geometries, uncovering two classes of pathways: downhill, in which bonds are only added, and detour, in which bonds are broken and remade before the target is reached: for some the only route that exists. Coarse-graining pathways by interactions gives experimentally realizable protocols. Some produce one geometry, others several: structures sharing a detour route can be cycled between, while those that coexist assemble into superstructures inaccessible to a uniform product. Function emerges from the pathways rather than being designed. Designing the process instead of the components could give colloidal materials that reconfigure and repair themselves on demand.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "abstract": "We prove that the six-vertex graph with edge set $\\{ab,bc,cd,de,af,bf,df\\}$ has the Erd\u0151s-Hajnal property. The proof adapts the iterative-sparsification method of Nguyen, Scott, and Seymour within the comb-based framework of Huang, Ju, and Zhou.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "abstract": "In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether llmllmlarge language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "abstract": "Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "abstract": "Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "abstract": "As an initial step toward personal memory ragragretrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "abstract": "The open radio access network (O-RAN) is evolving toward agentic operation, where llmllmlarge language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "abstract": "Magic, or nonstabilizerness, is the resource that lifts Clifford circuits to universal quantum computation and has become a standard diagnostic of many-body states. For a state shared between two parties, however, a basic question has remained open: how much of the magic resides in the correlations between the parties rather than in their local bases? Isolating this nonlocal magic requires minimizing over all local bases, an optimization that has so far resisted exact solution. Here we solve it for the stabilizer fidelity: the nonlocal magic of every pure multiqubit state is the distance of its entanglement spectrum from the closest spectrum of Bell pairs. The same quantity governs an apparently unrelated task: a family of states universally embezzles entanglement under local operations and classical communication if and only if its nonlocal magic diverges. The deciding property is not the amount of entanglement but the way the entanglement spectrum spreads its weight across factor-of-two windows of rank, so that critical chains and random-singlet states, with identical logarithmic entanglement scaling, carry unbounded and vanishing nonlocal magic, respectively. Nonlocal magic thereby becomes an operationally meaningful property of quantum correlations, directly accessible to tensor-network simulations and, through entanglement spectroscopy, to experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "abstract": "Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "abstract": "We introduce a notion of continuity equation on metric spaces that is capable of describing curves of probability measures which are absolutely continuous, and more generally of bounded variation (BV), with respect to the 1-Wasserstein distance. This continuity equation is based on a notion of measure-valued derivations, whose basic theory is also developed in this paper. On $\\mathbb{R}^n$, our formulation is consistent with the continuity equation with singular flux introduced by Almi--Rossi--Savar\u00e9 (arXiv:2506.15333), including the corresponding notion of minimal solutions. In this work, we characterize BV-curves in the space of probability measures equipped with the (extended) 1-Wasserstein distance as those curves satisfying the continuity equation with a measure-valued derivation of finite mass. To this aim, we extend our previous work (Calc.Var.(2024)63:16) on probabilistic representations on BV-curves and construct from them measure-valued derivations (resp. flux measures) on geodesic metric spaces (resp. on $\\mathbb{R}^n$).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "abstract": "ragragRetrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddingembeddingembeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "abstract": "Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "abstract": "Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "abstract": "Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training (\"RL-for-LLMs\") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "abstract": "In ragragRetrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "abstract": "We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "abstract": "Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "abstract": "Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for ragragRetrieval-Augmented Generation (RAG), and automated data labeling.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "abstract": "Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \\textsc{\\textsc{MedREAL}} (\\textbf{Med}ical \\textbf{RE}asoning-driven \\textbf{A}nswering and \\textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \\textsc{MedREAL} introduces \\textbf{S}eg \\textbf{A}nchored \\textbf{R}easoning \\textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \\texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \\textbf{R}easoning-to-\\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \\textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\\% gIoU and 70.47\\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \\textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "abstract": "LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "abstract": "The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, ragragretrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "abstract": "AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "abstract": "As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \\textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\\% and 14.4\\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "abstract": "We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "abstract": "The emergence of \"vibe coding\" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native). Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps. Code and benchmark resources are available at: https://github.com/snowmountainAi/webdevbench and https://webdevbench.com/.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "abstract": "llmllmLarge language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope's effectiveness in enhancing LLM tool use.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments. In this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a ragragretrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ``perfect blocking'' construction supplies equilibrated long-distance modes, while a conditional normalizing flow reconstructs short-distance details and brief rethermalization removes residual errors. In 2D $\u03c6^4$ theory at criticality, a flow trained at $L\\le32$ is reused recursively in cascades reaching $L=2048$ with correct long-distance physics.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "abstract": "We derive necessary conditions for instantaneous dynamo action for rotating convection. A magnetohydrodynamic model is considered in two settings: the rapidly rotating plane layer where inertia and viscosity are absent, and at an arbitrary rotation rate where viscosity is finite. In contrast to kinematic dynamo bounds, the evolution of the magnetic field is coupled via an inertialess force balance. The buoyancy-driven part of the flow $\\mathbf{u}^{\\mathrm{A}}$ in the event of dynamo action must in fact satisfy, for $3\\leq p \\leq \\infty$ $$ Rm\\, A_p\\| \\mathbf{u}^{\\mathrm{A}}\\|_{L^p} \\geq 1 $$ where $A_p$ is an explicit constant, and $Rm$ is the magnetic Reynolds number. In the inviscid model, $\\mathbf{u}^{\\mathrm{A}}$ depends only on the horizontal gradients of the vertical primitive of temperature. A refinement via the poloidal-toroidal decomposition allows us to replace $L^p$ in our constraint with an anisotropic norm for $L^{\\infty}_z \\dot{H}^1_{x,y}$. For the viscous model, we also derive necessary conditions for the growth of magnetic enstrophy and a combined thermo-magnetic energy. One branch of our constraints implies that the scaling $Ra_\u03bd\\gtrsim Ek^{-3/2}$ is necessary for dynamo action, where $Ra_\u03bd$ is the classical Rayleigh number and $Ek$ is the Ekman number.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "abstract": "Crystalline C$_{60}$ is a molecular solid whose electronic properties emerge from the interplay of intermolecular hopping, electron correlations, and electron-vibration coupling. Unlike moir$\\rm\\acute{e}$ van der Waals heterostructures, where interaction strength is commonly tuned by twist angle, molecular materials offer a complementary route in which layer number, molecular orientation, and substrate registry provide experimentally accessible control parameters. Here we present a systematic thickness-dependent angle-resolved photoemission study of C$_{60}$ films, spanning the monolayer to the bulk limit. The HOMO-derived band exhibits a non-monotonic evolution: the intermediate-thickness film shows larger bandwidth, reduced effective mass, and pronounced gap-like and sub-band features. The experimental trends, together with Holstein-model simulations, point to strengthened effective intermolecular electronic coupling and enhanced electron-phonon-induced spectral renormalization in the intermediate-thickness regime. These results identify a dimensional crossover in C$_{60}$ films and establish layer number as an effective knob for engineering electronic structure and many-body interactions in molecular thin films.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "abstract": "Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "abstract": "Nested sampling is widely used for Bayesian evidence computation, but its intrinsically sequential structure limits how efficiently it can exploit modern vectorised likelihoods and emulators. We present a new nested-sampling implementation in \\textsc{best}, written entirely in TensorFlow and designed for efficient XLA compilation on both CPUs and GPUs. The sampler combines clustering and slice sampling with the possibility of updating several live points simultaneously. Since batching breaks the strict ordering of conventional nested sampling, we introduce sorting and history-based corrections to reduce the resulting bias in the evidence estimate. We test the sampler on Gaussian, Rosenbrock, and multimodal likelihoods and compare its performance with JAXNS and UltraNest. The results show that accurate evidence estimates can be retained for moderate batch sizes, with $m/N_{\\rm live}\\lesssim 0.1$ providing a useful practical regime. Finally, using a 27-dimensional cosmological likelihood emulator, we show that batched live-point updates can substantially reduce the wall-clock time while remaining consistent with sequential sampling within the reported uncertainties. The new implementation therefore extends \\textsc{best} with an efficient nested-sampling method tailored to fast, vectorised likelihoods and emulator-based inference.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "abstract": "A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "abstract": "Multimodal sequential recommendation (MSR) improves recommendation by incorporating heterogeneous information such as text, images, and user interactions. However, existing MSR methods often fail to capture user-level preference heterogeneity and dataset-level modality bias, limiting their adaptability across users and datasets. To address this issue, we propose \\textbf{S}equence-\\textbf{G}uided \\textbf{U}niversal \\textbf{M}ultimodal \\textbf{P}rioritization Calculation Framework (\\textbf{SG-UMP}), a plug-and-play plugin for enhancing multimodal information processing in MSR. SG-UMP includes a Module Combiner for flexible multimodal processing and a Module Router for dynamic module ordering, enabling adaptation to both user preferences and dataset characteristics. Experiments on four real-world datasets show that SG-UMP consistently improves recommendation performance across different backbones and multimodal settings. The code is available at https://github.com/esemsc-xz524/SG-UMP .",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "abstract": "For a vertex operator algebra $V$ and a suitable category of its modules, we propose a construction for spaces of conformal blocks organized into an open-closed modular functor with singularities. This is inspired by the idea of implementing directly from the start the principle of holomorphic factorization. More precisely, using the strategy of modular extension introduced by Costello and developed further in our previous work, we build for each surface $\u03a3$ with at least one boundary component per path component and specified boundary labels attached to marked intervals or boundary circles a representation $\u03a9_V(\u03a3;-)$ of the mapping class group of $\u03a3$. The construction can be described explicitly on generating Dehn twists. This approach is a priori independent from other constructions based on algebraic geometry or topological techniques involving e.g. surgery, but we include an overview over the available comparisons. In the special case in which the module category of $V$ is a not necessarily semisimple modular category $\\mathcal{A}$, the spaces $\u03a9_V(\u03a3)$ are equivalent to the string-net spaces for $\\mathcal{A}$ and hence to the modular functor for the Drinfeld center $Z(\\mathcal{A})\\simeq \\bar{\\mathcal{A}}\\boxtimes\\mathcal{A}$. However, the construction of $\u03a9_V$ in this paper has the advantage of being available beyond rationality, rigidity, self-contragredience and finiteness. Moreover, we prove that $\u03a9_V$ satisfies excision, is finite-dimensional in the $C_2$-cofinite case and produces representations of surface braid groups generalizing the ones of Brochier-Jordan. We prove for the triplet $\\mathcal{W}_{2,3}$ with non-exact fusion product that the boundary conditions introduced by Gaberdiel-Runkel-Wood produce correlation functions, provided that one uses the notion of a modular functor with singularities that we develop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "abstract": "The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images. To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (https://github.com/llm-jp/synth-jdoc).",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "abstract": "Institutional investors search visually dense pitch decks, board packs, and diligence materials that change hourly near deal closing. OCR followed by figure verbalisation is costly to refresh at this scale and can lose chart detail. We present PULSAR, a production vision-first retrieval system deployed at Mubadala Investment Company. PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3, this design reduces median vector-search latency by 15.1 times against an unpooled configuration with less than 0.01 absolute NDCG@10 and Recall@10 loss; production median vector-search latency is 156 ms. Under concurrent load, the pooled index sustains approximately 88 times higher QPS than an unpooled index. The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced. Since March 2026, PULSAR has served 78 thousand documents and approximately 2.4 million pages across more than 3,000 deals. At the production top K, it more than doubles answer-fact recall over the OCR+verbalisation baseline.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "abstract": "Density three-point correlations are known to probe the topology of the Fermi sea in two-dimensional noninteracting systems. Here, we study how these correlations are modified by interactions using the coadjoint-orbit effective field theory. A key advantage of the coadjoint-orbit formulation is that it provides a systematic way to incorporate generalized Landau interactions in terms of bosonized degrees of freedom, mapping fermionic loop contributions onto simpler tree-level diagrams. We show that, for a general isotropic dispersion $\u03b5(p)$, even at linear order in the generalized Landau interaction, $\\mathcal{O}(\\mathcal{F}^{(2,0)})$, there exists a contribution proportional to the band curvature $\u03b5''(p_F)$ that changes the nonanalytic structure of the free density three-point correlation function. This contribution introduces a distinct nonanalytic structure beyond that found in either the noninteracting case or an interacting Galilean-invariant system, showing that interaction effects can modify the topology-detecting density three-point correlation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "abstract": "We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\\bar\u03bd$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $\u03c7^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\\widetilde O(d^2)$ mixing bound in $\u03c7^2$-divergence, improving on the previous $\\widetilde O(d^{9/4})$ bound.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "abstract": "Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using llmllmlarge language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "abstract": "Software architecture is often only partially captured in code, while much of the design intent lives in evolving project artifacts. In agile projects, work items, user stories, and related tracking documents preserve valuable traces of that intent, but they rarely support direct architectural analysis. This work investigates the recovery of C4 architecture diagrams from historical agile work items using an LLM-based pipeline. The semi-automatic five-step workflow employs a prompt chain, bidirectional traceability, and Chain-of-Thought reasoning to transform unstructured Azure DevOps work items into visual artifacts. Evaluated on two industry projects, we use a mixed-methods design combining qualitative expert interviews with a quantitative stability analysis. Practitioners perceive the generated architectural baselines as accurate and highly useful for system comprehension. Strictly bound by their input data, the artifacts mirror the documented intent, thereby surfacing discrepancies and architectural drift when compared to the implemented reality. Quantitatively, the workflow exhibits high stability for architectural entities but lower stability for their relationships, with relative variance compounding across generation steps. The proposed workflow demonstrates the practical viability of LLM-assisted architectural recovery based on development process artifacts.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "abstract": "Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "abstract": "Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "abstract": "Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\\%$ of total parameters).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "abstract": "Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "abstract": "Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "abstract": "Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We propose an algorithm for generating lattice field configurations based on the approximate inversion of a renormalization-group blocking transformation. We optimize the blocking transformation using a ``perfect blocking'' condition so that the blocked lattice distribution is well approximated by a simple coarse action. The blocking is separated into an invertible smoothing transformation followed by decimation. Machine learning, in the form of a conditional normalizing flow, is used to reconstruct the short-distance degrees of freedom removed by the decimation. A short fine-action rethermalization then removes the residual mismatch. Because the coarse ensemble supplies the long-distance modes, the same blocking transformation and conditional flow can be reused recursively on larger lattices, producing a cascade of configurations from an initial small-volume ensemble. We test the method in two-dimensional $\u03c6^4$ theory with $\u03bb=1$ at criticality and demonstrate stable cascade upscaling from $16^2$ to $2048^2$ lattices on local computational resources. Controlled rethermalization tests show that short-distance mismatches relax rapidly, whereas a deliberately introduced mismatch in the relevant thermal direction relaxes much more slowly. The construction uses ingredients that admit natural extensions to higher-dimensional systems and, ultimately, to gauge and fermionic degrees of freedom.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "abstract": "Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "abstract": "We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embeddingembeddingembeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "abstract": "Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: https://github.com/topo-focus/Topofocus",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "abstract": "A protein's function follows from the structure it adopts, and which structure that is depends on the pathway taken. In programmable matter the target is fixed before assembly, and whatever else forms is treated as error. Here we show that pathways themselves form a design space. Using reinforcement learning, we fold model DNA-coated droplet chains into rigid two-dimensional geometries, uncovering two classes of pathways: downhill, in which bonds are only added, and detour, in which bonds are broken and remade before the target is reached: for some the only route that exists. Coarse-graining pathways by interactions gives experimentally realizable protocols. Some produce one geometry, others several: structures sharing a detour route can be cycled between, while those that coexist assemble into superstructures inaccessible to a uniform product. Function emerges from the pathways rather than being designed. Designing the process instead of the components could give colloidal materials that reconfigure and repair themselves on demand.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "abstract": "We prove that the six-vertex graph with edge set $\\{ab,bc,cd,de,af,bf,df\\}$ has the Erd\u0151s-Hajnal property. The proof adapts the iterative-sparsification method of Nguyen, Scott, and Seymour within the comb-based framework of Huang, Ju, and Zhou.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "abstract": "In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether llmllmlarge language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "abstract": "Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "abstract": "Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "abstract": "As an initial step toward personal memory ragragretrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "abstract": "The open radio access network (O-RAN) is evolving toward agentic operation, where llmllmlarge language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "abstract": "Magic, or nonstabilizerness, is the resource that lifts Clifford circuits to universal quantum computation and has become a standard diagnostic of many-body states. For a state shared between two parties, however, a basic question has remained open: how much of the magic resides in the correlations between the parties rather than in their local bases? Isolating this nonlocal magic requires minimizing over all local bases, an optimization that has so far resisted exact solution. Here we solve it for the stabilizer fidelity: the nonlocal magic of every pure multiqubit state is the distance of its entanglement spectrum from the closest spectrum of Bell pairs. The same quantity governs an apparently unrelated task: a family of states universally embezzles entanglement under local operations and classical communication if and only if its nonlocal magic diverges. The deciding property is not the amount of entanglement but the way the entanglement spectrum spreads its weight across factor-of-two windows of rank, so that critical chains and random-singlet states, with identical logarithmic entanglement scaling, carry unbounded and vanishing nonlocal magic, respectively. Nonlocal magic thereby becomes an operationally meaningful property of quantum correlations, directly accessible to tensor-network simulations and, through entanglement spectroscopy, to experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "abstract": "Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "abstract": "We introduce a notion of continuity equation on metric spaces that is capable of describing curves of probability measures which are absolutely continuous, and more generally of bounded variation (BV), with respect to the 1-Wasserstein distance. This continuity equation is based on a notion of measure-valued derivations, whose basic theory is also developed in this paper. On $\\mathbb{R}^n$, our formulation is consistent with the continuity equation with singular flux introduced by Almi--Rossi--Savar\u00e9 (arXiv:2506.15333), including the corresponding notion of minimal solutions. In this work, we characterize BV-curves in the space of probability measures equipped with the (extended) 1-Wasserstein distance as those curves satisfying the continuity equation with a measure-valued derivation of finite mass. To this aim, we extend our previous work (Calc.Var.(2024)63:16) on probabilistic representations on BV-curves and construct from them measure-valued derivations (resp. flux measures) on geodesic metric spaces (resp. on $\\mathbb{R}^n$).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "abstract": "ragragRetrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddingembeddingembeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "abstract": "Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "abstract": "Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "abstract": "Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training (\"RL-for-LLMs\") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "abstract": "In ragragRetrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "abstract": "We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "abstract": "Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "abstract": "Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for ragragRetrieval-Augmented Generation (RAG), and automated data labeling.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "abstract": "Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \\textsc{\\textsc{MedREAL}} (\\textbf{Med}ical \\textbf{RE}asoning-driven \\textbf{A}nswering and \\textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \\textsc{MedREAL} introduces \\textbf{S}eg \\textbf{A}nchored \\textbf{R}easoning \\textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \\texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \\textbf{R}easoning-to-\\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \\textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\\% gIoU and 70.47\\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \\textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "abstract": "LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "abstract": "The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, ragragretrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "abstract": "AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "abstract": "As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \\textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\\% and 14.4\\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "abstract": "We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "abstract": "The emergence of \"vibe coding\" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native). Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps. Code and benchmark resources are available at: https://github.com/snowmountainAi/webdevbench and https://webdevbench.com/.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "abstract": "llmllmLarge language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope's effectiveness in enhancing LLM tool use.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments. In this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a ragragretrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ``perfect blocking'' construction supplies equilibrated long-distance modes, while a conditional normalizing flow reconstructs short-distance details and brief rethermalization removes residual errors. In 2D $\u03c6^4$ theory at criticality, a flow trained at $L\\le32$ is reused recursively in cascades reaching $L=2048$ with correct long-distance physics.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "abstract": "We derive necessary conditions for instantaneous dynamo action for rotating convection. A magnetohydrodynamic model is considered in two settings: the rapidly rotating plane layer where inertia and viscosity are absent, and at an arbitrary rotation rate where viscosity is finite. In contrast to kinematic dynamo bounds, the evolution of the magnetic field is coupled via an inertialess force balance. The buoyancy-driven part of the flow $\\mathbf{u}^{\\mathrm{A}}$ in the event of dynamo action must in fact satisfy, for $3\\leq p \\leq \\infty$ $$ Rm\\, A_p\\| \\mathbf{u}^{\\mathrm{A}}\\|_{L^p} \\geq 1 $$ where $A_p$ is an explicit constant, and $Rm$ is the magnetic Reynolds number. In the inviscid model, $\\mathbf{u}^{\\mathrm{A}}$ depends only on the horizontal gradients of the vertical primitive of temperature. A refinement via the poloidal-toroidal decomposition allows us to replace $L^p$ in our constraint with an anisotropic norm for $L^{\\infty}_z \\dot{H}^1_{x,y}$. For the viscous model, we also derive necessary conditions for the growth of magnetic enstrophy and a combined thermo-magnetic energy. One branch of our constraints implies that the scaling $Ra_\u03bd\\gtrsim Ek^{-3/2}$ is necessary for dynamo action, where $Ra_\u03bd$ is the classical Rayleigh number and $Ek$ is the Ekman number.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "abstract": "Crystalline C$_{60}$ is a molecular solid whose electronic properties emerge from the interplay of intermolecular hopping, electron correlations, and electron-vibration coupling. Unlike moir$\\rm\\acute{e}$ van der Waals heterostructures, where interaction strength is commonly tuned by twist angle, molecular materials offer a complementary route in which layer number, molecular orientation, and substrate registry provide experimentally accessible control parameters. Here we present a systematic thickness-dependent angle-resolved photoemission study of C$_{60}$ films, spanning the monolayer to the bulk limit. The HOMO-derived band exhibits a non-monotonic evolution: the intermediate-thickness film shows larger bandwidth, reduced effective mass, and pronounced gap-like and sub-band features. The experimental trends, together with Holstein-model simulations, point to strengthened effective intermolecular electronic coupling and enhanced electron-phonon-induced spectral renormalization in the intermediate-thickness regime. These results identify a dimensional crossover in C$_{60}$ films and establish layer number as an effective knob for engineering electronic structure and many-body interactions in molecular thin films.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "abstract": "Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "abstract": "Nested sampling is widely used for Bayesian evidence computation, but its intrinsically sequential structure limits how efficiently it can exploit modern vectorised likelihoods and emulators. We present a new nested-sampling implementation in \\textsc{best}, written entirely in TensorFlow and designed for efficient XLA compilation on both CPUs and GPUs. The sampler combines clustering and slice sampling with the possibility of updating several live points simultaneously. Since batching breaks the strict ordering of conventional nested sampling, we introduce sorting and history-based corrections to reduce the resulting bias in the evidence estimate. We test the sampler on Gaussian, Rosenbrock, and multimodal likelihoods and compare its performance with JAXNS and UltraNest. The results show that accurate evidence estimates can be retained for moderate batch sizes, with $m/N_{\\rm live}\\lesssim 0.1$ providing a useful practical regime. Finally, using a 27-dimensional cosmological likelihood emulator, we show that batched live-point updates can substantially reduce the wall-clock time while remaining consistent with sequential sampling within the reported uncertainties. The new implementation therefore extends \\textsc{best} with an efficient nested-sampling method tailored to fast, vectorised likelihoods and emulator-based inference.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "abstract": "A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "abstract": "Multimodal sequential recommendation (MSR) improves recommendation by incorporating heterogeneous information such as text, images, and user interactions. However, existing MSR methods often fail to capture user-level preference heterogeneity and dataset-level modality bias, limiting their adaptability across users and datasets. To address this issue, we propose \\textbf{S}equence-\\textbf{G}uided \\textbf{U}niversal \\textbf{M}ultimodal \\textbf{P}rioritization Calculation Framework (\\textbf{SG-UMP}), a plug-and-play plugin for enhancing multimodal information processing in MSR. SG-UMP includes a Module Combiner for flexible multimodal processing and a Module Router for dynamic module ordering, enabling adaptation to both user preferences and dataset characteristics. Experiments on four real-world datasets show that SG-UMP consistently improves recommendation performance across different backbones and multimodal settings. The code is available at https://github.com/esemsc-xz524/SG-UMP .",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "abstract": "For a vertex operator algebra $V$ and a suitable category of its modules, we propose a construction for spaces of conformal blocks organized into an open-closed modular functor with singularities. This is inspired by the idea of implementing directly from the start the principle of holomorphic factorization. More precisely, using the strategy of modular extension introduced by Costello and developed further in our previous work, we build for each surface $\u03a3$ with at least one boundary component per path component and specified boundary labels attached to marked intervals or boundary circles a representation $\u03a9_V(\u03a3;-)$ of the mapping class group of $\u03a3$. The construction can be described explicitly on generating Dehn twists. This approach is a priori independent from other constructions based on algebraic geometry or topological techniques involving e.g. surgery, but we include an overview over the available comparisons. In the special case in which the module category of $V$ is a not necessarily semisimple modular category $\\mathcal{A}$, the spaces $\u03a9_V(\u03a3)$ are equivalent to the string-net spaces for $\\mathcal{A}$ and hence to the modular functor for the Drinfeld center $Z(\\mathcal{A})\\simeq \\bar{\\mathcal{A}}\\boxtimes\\mathcal{A}$. However, the construction of $\u03a9_V$ in this paper has the advantage of being available beyond rationality, rigidity, self-contragredience and finiteness. Moreover, we prove that $\u03a9_V$ satisfies excision, is finite-dimensional in the $C_2$-cofinite case and produces representations of surface braid groups generalizing the ones of Brochier-Jordan. We prove for the triplet $\\mathcal{W}_{2,3}$ with non-exact fusion product that the boundary conditions introduced by Gaberdiel-Runkel-Wood produce correlation functions, provided that one uses the notion of a modular functor with singularities that we develop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "abstract": "The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images. To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (https://github.com/llm-jp/synth-jdoc).",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "abstract": "Institutional investors search visually dense pitch decks, board packs, and diligence materials that change hourly near deal closing. OCR followed by figure verbalisation is costly to refresh at this scale and can lose chart detail. We present PULSAR, a production vision-first retrieval system deployed at Mubadala Investment Company. PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3, this design reduces median vector-search latency by 15.1 times against an unpooled configuration with less than 0.01 absolute NDCG@10 and Recall@10 loss; production median vector-search latency is 156 ms. Under concurrent load, the pooled index sustains approximately 88 times higher QPS than an unpooled index. The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced. Since March 2026, PULSAR has served 78 thousand documents and approximately 2.4 million pages across more than 3,000 deals. At the production top K, it more than doubles answer-fact recall over the OCR+verbalisation baseline.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "abstract": "Density three-point correlations are known to probe the topology of the Fermi sea in two-dimensional noninteracting systems. Here, we study how these correlations are modified by interactions using the coadjoint-orbit effective field theory. A key advantage of the coadjoint-orbit formulation is that it provides a systematic way to incorporate generalized Landau interactions in terms of bosonized degrees of freedom, mapping fermionic loop contributions onto simpler tree-level diagrams. We show that, for a general isotropic dispersion $\u03b5(p)$, even at linear order in the generalized Landau interaction, $\\mathcal{O}(\\mathcal{F}^{(2,0)})$, there exists a contribution proportional to the band curvature $\u03b5''(p_F)$ that changes the nonanalytic structure of the free density three-point correlation function. This contribution introduces a distinct nonanalytic structure beyond that found in either the noninteracting case or an interacting Galilean-invariant system, showing that interaction effects can modify the topology-detecting density three-point correlation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "abstract": "We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\\bar\u03bd$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $\u03c7^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\\widetilde O(d^2)$ mixing bound in $\u03c7^2$-divergence, improving on the previous $\\widetilde O(d^{9/4})$ bound.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "abstract": "Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using llmllmlarge language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "abstract": "Software architecture is often only partially captured in code, while much of the design intent lives in evolving project artifacts. In agile projects, work items, user stories, and related tracking documents preserve valuable traces of that intent, but they rarely support direct architectural analysis. This work investigates the recovery of C4 architecture diagrams from historical agile work items using an LLM-based pipeline. The semi-automatic five-step workflow employs a prompt chain, bidirectional traceability, and Chain-of-Thought reasoning to transform unstructured Azure DevOps work items into visual artifacts. Evaluated on two industry projects, we use a mixed-methods design combining qualitative expert interviews with a quantitative stability analysis. Practitioners perceive the generated architectural baselines as accurate and highly useful for system comprehension. Strictly bound by their input data, the artifacts mirror the documented intent, thereby surfacing discrepancies and architectural drift when compared to the implemented reality. Quantitatively, the workflow exhibits high stability for architectural entities but lower stability for their relationships, with relative variance compounding across generation steps. The proposed workflow demonstrates the practical viability of LLM-assisted architectural recovery based on development process artifacts.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "abstract": "Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "abstract": "Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "abstract": "Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\\%$ of total parameters).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "abstract": "Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "abstract": "Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "abstract": "Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We propose an algorithm for generating lattice field configurations based on the approximate inversion of a renormalization-group blocking transformation. We optimize the blocking transformation using a ``perfect blocking'' condition so that the blocked lattice distribution is well approximated by a simple coarse action. The blocking is separated into an invertible smoothing transformation followed by decimation. Machine learning, in the form of a conditional normalizing flow, is used to reconstruct the short-distance degrees of freedom removed by the decimation. A short fine-action rethermalization then removes the residual mismatch. Because the coarse ensemble supplies the long-distance modes, the same blocking transformation and conditional flow can be reused recursively on larger lattices, producing a cascade of configurations from an initial small-volume ensemble. We test the method in two-dimensional $\u03c6^4$ theory with $\u03bb=1$ at criticality and demonstrate stable cascade upscaling from $16^2$ to $2048^2$ lattices on local computational resources. Controlled rethermalization tests show that short-distance mismatches relax rapidly, whereas a deliberately introduced mismatch in the relevant thermal direction relaxes much more slowly. The construction uses ingredients that admit natural extensions to higher-dimensional systems and, ultimately, to gauge and fermionic degrees of freedom.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "abstract": "Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "abstract": "We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embeddingembeddingembeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "abstract": "Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: https://github.com/topo-focus/Topofocus",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "abstract": "A protein's function follows from the structure it adopts, and which structure that is depends on the pathway taken. In programmable matter the target is fixed before assembly, and whatever else forms is treated as error. Here we show that pathways themselves form a design space. Using reinforcement learning, we fold model DNA-coated droplet chains into rigid two-dimensional geometries, uncovering two classes of pathways: downhill, in which bonds are only added, and detour, in which bonds are broken and remade before the target is reached: for some the only route that exists. Coarse-graining pathways by interactions gives experimentally realizable protocols. Some produce one geometry, others several: structures sharing a detour route can be cycled between, while those that coexist assemble into superstructures inaccessible to a uniform product. Function emerges from the pathways rather than being designed. Designing the process instead of the components could give colloidal materials that reconfigure and repair themselves on demand.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "abstract": "We prove that the six-vertex graph with edge set $\\{ab,bc,cd,de,af,bf,df\\}$ has the Erd\u0151s-Hajnal property. The proof adapts the iterative-sparsification method of Nguyen, Scott, and Seymour within the comb-based framework of Huang, Ju, and Zhou.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "abstract": "In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether llmllmlarge language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "abstract": "Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "abstract": "Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "abstract": "As an initial step toward personal memory ragragretrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "abstract": "The open radio access network (O-RAN) is evolving toward agentic operation, where llmllmlarge language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "abstract": "Magic, or nonstabilizerness, is the resource that lifts Clifford circuits to universal quantum computation and has become a standard diagnostic of many-body states. For a state shared between two parties, however, a basic question has remained open: how much of the magic resides in the correlations between the parties rather than in their local bases? Isolating this nonlocal magic requires minimizing over all local bases, an optimization that has so far resisted exact solution. Here we solve it for the stabilizer fidelity: the nonlocal magic of every pure multiqubit state is the distance of its entanglement spectrum from the closest spectrum of Bell pairs. The same quantity governs an apparently unrelated task: a family of states universally embezzles entanglement under local operations and classical communication if and only if its nonlocal magic diverges. The deciding property is not the amount of entanglement but the way the entanglement spectrum spreads its weight across factor-of-two windows of rank, so that critical chains and random-singlet states, with identical logarithmic entanglement scaling, carry unbounded and vanishing nonlocal magic, respectively. Nonlocal magic thereby becomes an operationally meaningful property of quantum correlations, directly accessible to tensor-network simulations and, through entanglement spectroscopy, to experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "abstract": "Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "abstract": "We introduce a notion of continuity equation on metric spaces that is capable of describing curves of probability measures which are absolutely continuous, and more generally of bounded variation (BV), with respect to the 1-Wasserstein distance. This continuity equation is based on a notion of measure-valued derivations, whose basic theory is also developed in this paper. On $\\mathbb{R}^n$, our formulation is consistent with the continuity equation with singular flux introduced by Almi--Rossi--Savar\u00e9 (arXiv:2506.15333), including the corresponding notion of minimal solutions. In this work, we characterize BV-curves in the space of probability measures equipped with the (extended) 1-Wasserstein distance as those curves satisfying the continuity equation with a measure-valued derivation of finite mass. To this aim, we extend our previous work (Calc.Var.(2024)63:16) on probabilistic representations on BV-curves and construct from them measure-valued derivations (resp. flux measures) on geodesic metric spaces (resp. on $\\mathbb{R}^n$).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "abstract": "ragragRetrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddingembeddingembeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "abstract": "Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "abstract": "Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "abstract": "Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training (\"RL-for-LLMs\") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "abstract": "In ragragRetrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "abstract": "We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "abstract": "Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "abstract": "Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for ragragRetrieval-Augmented Generation (RAG), and automated data labeling.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "abstract": "Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \\textsc{\\textsc{MedREAL}} (\\textbf{Med}ical \\textbf{RE}asoning-driven \\textbf{A}nswering and \\textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \\textsc{MedREAL} introduces \\textbf{S}eg \\textbf{A}nchored \\textbf{R}easoning \\textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \\texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \\textbf{R}easoning-to-\\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \\textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\\% gIoU and 70.47\\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \\textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "abstract": "LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "abstract": "The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, ragragretrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "abstract": "AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "abstract": "As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \\textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\\% and 14.4\\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "abstract": "We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "abstract": "The emergence of \"vibe coding\" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native). Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps. Code and benchmark resources are available at: https://github.com/snowmountainAi/webdevbench and https://webdevbench.com/.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "abstract": "llmllmLarge language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope's effectiveness in enhancing LLM tool use.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.\nIn this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ``perfect blocking'' construction supplies equilibrated long-distance modes, while a conditional normalizing flow reconstructs short-distance details and brief rethermalization removes residual errors. In 2D $\u03c6^4$ theory at criticality, a flow trained at $L\\le32$ is reused recursively in cascades reaching $L=2048$ with correct long-distance physics.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "abstract": "We derive necessary conditions for instantaneous dynamo action for rotating convection. A magnetohydrodynamic model is considered in two settings: the rapidly rotating plane layer where inertia and viscosity are absent, and at an arbitrary rotation rate where viscosity is finite. In contrast to kinematic dynamo bounds, the evolution of the magnetic field is coupled via an inertialess force balance. The buoyancy-driven part of the flow $\\mathbf{u}^{\\mathrm{A}}$ in the event of dynamo action must in fact satisfy, for $3\\leq p \\leq \\infty$ $$ Rm\\, A_p\\| \\mathbf{u}^{\\mathrm{A}}\\|_{L^p} \\geq 1 $$ where $A_p$ is an explicit constant, and $Rm$ is the magnetic Reynolds number. In the inviscid model, $\\mathbf{u}^{\\mathrm{A}}$ depends only on the horizontal gradients of the vertical primitive of temperature. A refinement via the poloidal-toroidal decomposition allows us to replace $L^p$ in our constraint with an anisotropic norm for $L^{\\infty}_z \\dot{H}^1_{x,y}$. For the viscous model, we also derive necessary conditions for the growth of magnetic enstrophy and a combined thermo-magnetic energy. One branch of our constraints implies that the scaling $Ra_\u03bd\\gtrsim Ek^{-3/2}$ is necessary for dynamo action, where $Ra_\u03bd$ is the classical Rayleigh number and $Ek$ is the Ekman number.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "abstract": "Crystalline C$_{60}$ is a molecular solid whose electronic properties emerge from the interplay of intermolecular hopping, electron correlations, and electron-vibration coupling. Unlike moir$\\rm\\acute{e}$ van der Waals heterostructures, where interaction strength is commonly tuned by twist angle, molecular materials offer a complementary route in which layer number, molecular orientation, and substrate registry provide experimentally accessible control parameters. Here we present a systematic thickness-dependent angle-resolved photoemission study of C$_{60}$ films, spanning the monolayer to the bulk limit. The HOMO-derived band exhibits a non-monotonic evolution: the intermediate-thickness film shows larger bandwidth, reduced effective mass, and pronounced gap-like and sub-band features. The experimental trends, together with Holstein-model simulations, point to strengthened effective intermolecular electronic coupling and enhanced electron-phonon-induced spectral renormalization in the intermediate-thickness regime. These results identify a dimensional crossover in C$_{60}$ films and establish layer number as an effective knob for engineering electronic structure and many-body interactions in molecular thin films.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "abstract": "Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "abstract": "Nested sampling is widely used for Bayesian evidence computation, but its intrinsically sequential structure limits how efficiently it can exploit modern vectorised likelihoods and emulators. We present a new nested-sampling implementation in \\textsc{best}, written entirely in TensorFlow and designed for efficient XLA compilation on both CPUs and GPUs. The sampler combines clustering and slice sampling with the possibility of updating several live points simultaneously. Since batching breaks the strict ordering of conventional nested sampling, we introduce sorting and history-based corrections to reduce the resulting bias in the evidence estimate. We test the sampler on Gaussian, Rosenbrock, and multimodal likelihoods and compare its performance with JAXNS and UltraNest. The results show that accurate evidence estimates can be retained for moderate batch sizes, with $m/N_{\\rm live}\\lesssim 0.1$ providing a useful practical regime. Finally, using a 27-dimensional cosmological likelihood emulator, we show that batched live-point updates can substantially reduce the wall-clock time while remaining consistent with sequential sampling within the reported uncertainties. The new implementation therefore extends \\textsc{best} with an efficient nested-sampling method tailored to fast, vectorised likelihoods and emulator-based inference.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "abstract": "A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "abstract": "Multimodal sequential recommendation (MSR) improves recommendation by incorporating heterogeneous information such as text, images, and user interactions. However, existing MSR methods often fail to capture user-level preference heterogeneity and dataset-level modality bias, limiting their adaptability across users and datasets. To address this issue, we propose \\textbf{S}equence-\\textbf{G}uided \\textbf{U}niversal \\textbf{M}ultimodal \\textbf{P}rioritization Calculation Framework (\\textbf{SG-UMP}), a plug-and-play plugin for enhancing multimodal information processing in MSR. SG-UMP includes a Module Combiner for flexible multimodal processing and a Module Router for dynamic module ordering, enabling adaptation to both user preferences and dataset characteristics. Experiments on four real-world datasets show that SG-UMP consistently improves recommendation performance across different backbones and multimodal settings. The code is available at https://github.com/esemsc-xz524/SG-UMP .",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "abstract": "For a vertex operator algebra $V$ and a suitable category of its modules, we propose a construction for spaces of conformal blocks organized into an open-closed modular functor with singularities. This is inspired by the idea of implementing directly from the start the principle of holomorphic factorization. More precisely, using the strategy of modular extension introduced by Costello and developed further in our previous work, we build for each surface $\u03a3$ with at least one boundary component per path component and specified boundary labels attached to marked intervals or boundary circles a representation $\u03a9_V(\u03a3;-)$ of the mapping class group of $\u03a3$. The construction can be described explicitly on generating Dehn twists. This approach is a priori independent from other constructions based on algebraic geometry or topological techniques involving e.g. surgery, but we include an overview over the available comparisons. In the special case in which the module category of $V$ is a not necessarily semisimple modular category $\\mathcal{A}$, the spaces $\u03a9_V(\u03a3)$ are equivalent to the string-net spaces for $\\mathcal{A}$ and hence to the modular functor for the Drinfeld center $Z(\\mathcal{A})\\simeq \\bar{\\mathcal{A}}\\boxtimes\\mathcal{A}$. However, the construction of $\u03a9_V$ in this paper has the advantage of being available beyond rationality, rigidity, self-contragredience and finiteness. Moreover, we prove that $\u03a9_V$ satisfies excision, is finite-dimensional in the $C_2$-cofinite case and produces representations of surface braid groups generalizing the ones of Brochier-Jordan. We prove for the triplet $\\mathcal{W}_{2,3}$ with non-exact fusion product that the boundary conditions introduced by Gaberdiel-Runkel-Wood produce correlation functions, provided that one uses the notion of a modular functor with singularities that we develop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "abstract": "The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images. To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (https://github.com/llm-jp/synth-jdoc).",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "abstract": "Institutional investors search visually dense pitch decks, board packs, and diligence materials that change hourly near deal closing. OCR followed by figure verbalisation is costly to refresh at this scale and can lose chart detail. We present PULSAR, a production vision-first retrieval system deployed at Mubadala Investment Company. PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3, this design reduces median vector-search latency by 15.1 times against an unpooled configuration with less than 0.01 absolute NDCG@10 and Recall@10 loss; production median vector-search latency is 156 ms. Under concurrent load, the pooled index sustains approximately 88 times higher QPS than an unpooled index. The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced. Since March 2026, PULSAR has served 78 thousand documents and approximately 2.4 million pages across more than 3,000 deals. At the production top K, it more than doubles answer-fact recall over the OCR+verbalisation baseline.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "abstract": "Density three-point correlations are known to probe the topology of the Fermi sea in two-dimensional noninteracting systems. Here, we study how these correlations are modified by interactions using the coadjoint-orbit effective field theory. A key advantage of the coadjoint-orbit formulation is that it provides a systematic way to incorporate generalized Landau interactions in terms of bosonized degrees of freedom, mapping fermionic loop contributions onto simpler tree-level diagrams. We show that, for a general isotropic dispersion $\u03b5(p)$, even at linear order in the generalized Landau interaction, $\\mathcal{O}(\\mathcal{F}^{(2,0)})$, there exists a contribution proportional to the band curvature $\u03b5''(p_F)$ that changes the nonanalytic structure of the free density three-point correlation function. This contribution introduces a distinct nonanalytic structure beyond that found in either the noninteracting case or an interacting Galilean-invariant system, showing that interaction effects can modify the topology-detecting density three-point correlation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "abstract": "We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\\bar\u03bd$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $\u03c7^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\\widetilde O(d^2)$ mixing bound in $\u03c7^2$-divergence, improving on the previous $\\widetilde O(d^{9/4})$ bound.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "abstract": "Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "abstract": "Software architecture is often only partially captured in code, while much of the design intent lives in evolving project artifacts. In agile projects, work items, user stories, and related tracking documents preserve valuable traces of that intent, but they rarely support direct architectural analysis. This work investigates the recovery of C4 architecture diagrams from historical agile work items using an LLM-based pipeline. The semi-automatic five-step workflow employs a prompt chain, bidirectional traceability, and Chain-of-Thought reasoning to transform unstructured Azure DevOps work items into visual artifacts. Evaluated on two industry projects, we use a mixed-methods design combining qualitative expert interviews with a quantitative stability analysis. Practitioners perceive the generated architectural baselines as accurate and highly useful for system comprehension. Strictly bound by their input data, the artifacts mirror the documented intent, thereby surfacing discrepancies and architectural drift when compared to the implemented reality. Quantitatively, the workflow exhibits high stability for architectural entities but lower stability for their relationships, with relative variance compounding across generation steps. The proposed workflow demonstrates the practical viability of LLM-assisted architectural recovery based on development process artifacts.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "abstract": "Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "abstract": "Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "abstract": "Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\\%$ of total parameters).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "abstract": "Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "abstract": "Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "abstract": "Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We propose an algorithm for generating lattice field configurations based on the approximate inversion of a renormalization-group blocking transformation. We optimize the blocking transformation using a ``perfect blocking'' condition so that the blocked lattice distribution is well approximated by a simple coarse action. The blocking is separated into an invertible smoothing transformation followed by decimation. Machine learning, in the form of a conditional normalizing flow, is used to reconstruct the short-distance degrees of freedom removed by the decimation. A short fine-action rethermalization then removes the residual mismatch. Because the coarse ensemble supplies the long-distance modes, the same blocking transformation and conditional flow can be reused recursively on larger lattices, producing a cascade of configurations from an initial small-volume ensemble. We test the method in two-dimensional $\u03c6^4$ theory with $\u03bb=1$ at criticality and demonstrate stable cascade upscaling from $16^2$ to $2048^2$ lattices on local computational resources. Controlled rethermalization tests show that short-distance mismatches relax rapidly, whereas a deliberately introduced mismatch in the relevant thermal direction relaxes much more slowly. The construction uses ingredients that admit natural extensions to higher-dimensional systems and, ultimately, to gauge and fermionic degrees of freedom.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "abstract": "Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "abstract": "We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embedding\" onclick=\"window.location.href='wiki.html'\">embedding\" onclick=\"window.location.href='wiki.html'\">embeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "abstract": "Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: https://github.com/topo-focus/Topofocus",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "abstract": "A protein's function follows from the structure it adopts, and which structure that is depends on the pathway taken. In programmable matter the target is fixed before assembly, and whatever else forms is treated as error. Here we show that pathways themselves form a design space. Using reinforcement learning, we fold model DNA-coated droplet chains into rigid two-dimensional geometries, uncovering two classes of pathways: downhill, in which bonds are only added, and detour, in which bonds are broken and remade before the target is reached: for some the only route that exists. Coarse-graining pathways by interactions gives experimentally realizable protocols. Some produce one geometry, others several: structures sharing a detour route can be cycled between, while those that coexist assemble into superstructures inaccessible to a uniform product. Function emerges from the pathways rather than being designed. Designing the process instead of the components could give colloidal materials that reconfigure and repair themselves on demand.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "abstract": "We prove that the six-vertex graph with edge set $\\{ab,bc,cd,de,af,bf,df\\}$ has the Erd\u0151s-Hajnal property. The proof adapts the iterative-sparsification method of Nguyen, Scott, and Seymour within the comb-based framework of Huang, Ju, and Zhou.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "abstract": "In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "abstract": "Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image  geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "abstract": "Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "abstract": "As an initial step toward personal memory rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "abstract": "The open radio access network (O-RAN) is evolving toward agentic operation, where llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "abstract": "Magic, or nonstabilizerness, is the resource that lifts Clifford circuits to universal quantum computation and has become a standard diagnostic of many-body states. For a state shared between two parties, however, a basic question has remained open: how much of the magic resides in the correlations between the parties rather than in their local bases? Isolating this nonlocal magic requires minimizing over all local bases, an optimization that has so far resisted exact solution. Here we solve it for the stabilizer fidelity: the nonlocal magic of every pure multiqubit state is the distance of its entanglement spectrum from the closest spectrum of Bell pairs. The same quantity governs an apparently unrelated task: a family of states universally embezzles entanglement under local operations and classical communication if and only if its nonlocal magic diverges. The deciding property is not the amount of entanglement but the way the entanglement spectrum spreads its weight across factor-of-two windows of rank, so that critical chains and random-singlet states, with identical logarithmic entanglement scaling, carry unbounded and vanishing nonlocal magic, respectively. Nonlocal magic thereby becomes an operationally meaningful property of quantum correlations, directly accessible to tensor-network simulations and, through entanglement spectroscopy, to experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "abstract": "Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "abstract": "We introduce a notion of continuity equation on metric spaces that is capable of describing curves of probability measures which are absolutely continuous, and more generally of bounded variation (BV), with respect to the 1-Wasserstein distance. This continuity equation is based on a notion of measure-valued derivations, whose basic theory is also developed in this paper. On $\\mathbb{R}^n$, our formulation is consistent with the continuity equation with singular flux introduced by Almi--Rossi--Savar\u00e9 (arXiv:2506.15333), including the corresponding notion of minimal solutions. In this work, we characterize BV-curves in the space of probability measures equipped with the (extended) 1-Wasserstein distance as those curves satisfying the continuity equation with a measure-valued derivation of finite mass. To this aim, we extend our previous work (Calc.Var.(2024)63:16) on probabilistic representations on BV-curves and construct from them measure-valued derivations (resp. flux measures) on geodesic metric spaces (resp. on $\\mathbb{R}^n$).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "abstract": "rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embedding\" onclick=\"window.location.href='wiki.html'\">embedding\" onclick=\"window.location.href='wiki.html'\">embeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "abstract": "Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "abstract": "Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "abstract": "Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training (\"RL-for-LLMs\") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "abstract": "In rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "abstract": "We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "abstract": "Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "abstract": "Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-Augmented Generation (RAG), and automated data labeling.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "abstract": "Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \\textsc{\\textsc{MedREAL}} (\\textbf{Med}ical \\textbf{RE}asoning-driven \\textbf{A}nswering and \\textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \\textsc{MedREAL} introduces \\textbf{S}eg \\textbf{A}nchored \\textbf{R}easoning \\textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \\texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \\textbf{R}easoning-to-\\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \\textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\\% gIoU and 70.47\\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \\textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "abstract": "LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "abstract": "The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "abstract": "AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "abstract": "As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \\textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\\% and 14.4\\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "abstract": "We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "abstract": "The emergence of \"vibe coding\" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native). Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps. Code and benchmark resources are available at: https://github.com/snowmountainAi/webdevbench and https://webdevbench.com/.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "abstract": "llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">Large language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope's effectiveness in enhancing LLM tool use.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.\nIn this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ``perfect blocking'' construction supplies equilibrated long-distance modes, while a conditional normalizing flow reconstructs short-distance details and brief rethermalization removes residual errors. In 2D $\u03c6^4$ theory at criticality, a flow trained at $L\\le32$ is reused recursively in cascades reaching $L=2048$ with correct long-distance physics.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "abstract": "We derive necessary conditions for instantaneous dynamo action for rotating convection. A magnetohydrodynamic model is considered in two settings: the rapidly rotating plane layer where inertia and viscosity are absent, and at an arbitrary rotation rate where viscosity is finite. In contrast to kinematic dynamo bounds, the evolution of the magnetic field is coupled via an inertialess force balance. The buoyancy-driven part of the flow $\\mathbf{u}^{\\mathrm{A}}$ in the event of dynamo action must in fact satisfy, for $3\\leq p \\leq \\infty$ $$ Rm\\, A_p\\| \\mathbf{u}^{\\mathrm{A}}\\|_{L^p} \\geq 1 $$ where $A_p$ is an explicit constant, and $Rm$ is the magnetic Reynolds number. In the inviscid model, $\\mathbf{u}^{\\mathrm{A}}$ depends only on the horizontal gradients of the vertical primitive of temperature. A refinement via the poloidal-toroidal decomposition allows us to replace $L^p$ in our constraint with an anisotropic norm for $L^{\\infty}_z \\dot{H}^1_{x,y}$. For the viscous model, we also derive necessary conditions for the growth of magnetic enstrophy and a combined thermo-magnetic energy. One branch of our constraints implies that the scaling $Ra_\u03bd\\gtrsim Ek^{-3/2}$ is necessary for dynamo action, where $Ra_\u03bd$ is the classical Rayleigh number and $Ek$ is the Ekman number.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "abstract": "Crystalline C$_{60}$ is a molecular solid whose electronic properties emerge from the interplay of intermolecular hopping, electron correlations, and electron-vibration coupling. Unlike moir$\\rm\\acute{e}$ van der Waals heterostructures, where interaction strength is commonly tuned by twist angle, molecular materials offer a complementary route in which layer number, molecular orientation, and substrate registry provide experimentally accessible control parameters. Here we present a systematic thickness-dependent angle-resolved photoemission study of C$_{60}$ films, spanning the monolayer to the bulk limit. The HOMO-derived band exhibits a non-monotonic evolution: the intermediate-thickness film shows larger bandwidth, reduced effective mass, and pronounced gap-like and sub-band features. The experimental trends, together with Holstein-model simulations, point to strengthened effective intermolecular electronic coupling and enhanced electron-phonon-induced spectral renormalization in the intermediate-thickness regime. These results identify a dimensional crossover in C$_{60}$ films and establish layer number as an effective knob for engineering electronic structure and many-body interactions in molecular thin films.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "abstract": "Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "abstract": "Nested sampling is widely used for Bayesian evidence computation, but its intrinsically sequential structure limits how efficiently it can exploit modern vectorised likelihoods and emulators. We present a new nested-sampling implementation in \\textsc{best}, written entirely in TensorFlow and designed for efficient XLA compilation on both CPUs and GPUs. The sampler combines clustering and slice sampling with the possibility of updating several live points simultaneously. Since batching breaks the strict ordering of conventional nested sampling, we introduce sorting and history-based corrections to reduce the resulting bias in the evidence estimate. We test the sampler on Gaussian, Rosenbrock, and multimodal likelihoods and compare its performance with JAXNS and UltraNest. The results show that accurate evidence estimates can be retained for moderate batch sizes, with $m/N_{\\rm live}\\lesssim 0.1$ providing a useful practical regime. Finally, using a 27-dimensional cosmological likelihood emulator, we show that batched live-point updates can substantially reduce the wall-clock time while remaining consistent with sequential sampling within the reported uncertainties. The new implementation therefore extends \\textsc{best} with an efficient nested-sampling method tailored to fast, vectorised likelihoods and emulator-based inference.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "abstract": "A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "abstract": "Multimodal sequential recommendation (MSR) improves recommendation by incorporating heterogeneous information such as text, images, and user interactions. However, existing MSR methods often fail to capture user-level preference heterogeneity and dataset-level modality bias, limiting their adaptability across users and datasets. To address this issue, we propose \\textbf{S}equence-\\textbf{G}uided \\textbf{U}niversal \\textbf{M}ultimodal \\textbf{P}rioritization Calculation Framework (\\textbf{SG-UMP}), a plug-and-play plugin for enhancing multimodal information processing in MSR. SG-UMP includes a Module Combiner for flexible multimodal processing and a Module Router for dynamic module ordering, enabling adaptation to both user preferences and dataset characteristics. Experiments on four real-world datasets show that SG-UMP consistently improves recommendation performance across different backbones and multimodal settings. The code is available at https://github.com/esemsc-xz524/SG-UMP .",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "abstract": "For a vertex operator algebra $V$ and a suitable category of its modules, we propose a construction for spaces of conformal blocks organized into an open-closed modular functor with singularities. This is inspired by the idea of implementing directly from the start the principle of holomorphic factorization. More precisely, using the strategy of modular extension introduced by Costello and developed further in our previous work, we build for each surface $\u03a3$ with at least one boundary component per path component and specified boundary labels attached to marked intervals or boundary circles a representation $\u03a9_V(\u03a3;-)$ of the mapping class group of $\u03a3$. The construction can be described explicitly on generating Dehn twists. This approach is a priori independent from other constructions based on algebraic geometry or topological techniques involving e.g. surgery, but we include an overview over the available comparisons. In the special case in which the module category of $V$ is a not necessarily semisimple modular category $\\mathcal{A}$, the spaces $\u03a9_V(\u03a3)$ are equivalent to the string-net spaces for $\\mathcal{A}$ and hence to the modular functor for the Drinfeld center $Z(\\mathcal{A})\\simeq \\bar{\\mathcal{A}}\\boxtimes\\mathcal{A}$. However, the construction of $\u03a9_V$ in this paper has the advantage of being available beyond rationality, rigidity, self-contragredience and finiteness. Moreover, we prove that $\u03a9_V$ satisfies excision, is finite-dimensional in the $C_2$-cofinite case and produces representations of surface braid groups generalizing the ones of Brochier-Jordan. We prove for the triplet $\\mathcal{W}_{2,3}$ with non-exact fusion product that the boundary conditions introduced by Gaberdiel-Runkel-Wood produce correlation functions, provided that one uses the notion of a modular functor with singularities that we develop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "abstract": "The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images. To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (https://github.com/llm-jp/synth-jdoc).",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "abstract": "Institutional investors search visually dense pitch decks, board packs, and diligence materials that change hourly near deal closing. OCR followed by figure verbalisation is costly to refresh at this scale and can lose chart detail. We present PULSAR, a production vision-first retrieval system deployed at Mubadala Investment Company. PULSAR indexes page images with a frozen ColPali-style backbone and uses a pooled two-stage late-interaction index: compact page summaries support initial retrieval, followed by exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3, this design reduces median vector-search latency by 15.1 times against an unpooled configuration with less than 0.01 absolute NDCG@10 and Recall@10 loss; production median vector-search latency is 156 ms. Under concurrent load, the pooled index sustains approximately 88 times higher QPS than an unpooled index. The event-driven ingestion path is estimated to be approximately 20 times cheaper per page than the OCR+verbalisation baseline it replaced. Since March 2026, PULSAR has served 78 thousand documents and approximately 2.4 million pages across more than 3,000 deals. At the production top K, it more than doubles answer-fact recall over the OCR+verbalisation baseline.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "abstract": "Density three-point correlations are known to probe the topology of the Fermi sea in two-dimensional noninteracting systems. Here, we study how these correlations are modified by interactions using the coadjoint-orbit effective field theory. A key advantage of the coadjoint-orbit formulation is that it provides a systematic way to incorporate generalized Landau interactions in terms of bosonized degrees of freedom, mapping fermionic loop contributions onto simpler tree-level diagrams. We show that, for a general isotropic dispersion $\u03b5(p)$, even at linear order in the generalized Landau interaction, $\\mathcal{O}(\\mathcal{F}^{(2,0)})$, there exists a contribution proportional to the band curvature $\u03b5''(p_F)$ that changes the nonanalytic structure of the free density three-point correlation function. This contribution introduces a distinct nonanalytic structure beyond that found in either the noninteracting case or an interacting Galilean-invariant system, showing that interaction effects can modify the topology-detecting density three-point correlation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "abstract": "We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\\bar\u03bd$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $\u03c7^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\\widetilde O(d^2)$ mixing bound in $\u03c7^2$-divergence, improving on the previous $\\widetilde O(d^{9/4})$ bound.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "abstract": "Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "abstract": "Software architecture is often only partially captured in code, while much of the design intent lives in evolving project artifacts. In agile projects, work items, user stories, and related tracking documents preserve valuable traces of that intent, but they rarely support direct architectural analysis. This work investigates the recovery of C4 architecture diagrams from historical agile work items using an LLM-based pipeline. The semi-automatic five-step workflow employs a prompt chain, bidirectional traceability, and Chain-of-Thought reasoning to transform unstructured Azure DevOps work items into visual artifacts. Evaluated on two industry projects, we use a mixed-methods design combining qualitative expert interviews with a quantitative stability analysis. Practitioners perceive the generated architectural baselines as accurate and highly useful for system comprehension. Strictly bound by their input data, the artifacts mirror the documented intent, thereby surfacing discrepancies and architectural drift when compared to the implemented reality. Quantitatively, the workflow exhibits high stability for architectural entities but lower stability for their relationships, with relative variance compounding across generation steps. The proposed workflow demonstrates the practical viability of LLM-assisted architectural recovery based on development process artifacts.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "abstract": "Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "abstract": "Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "abstract": "Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\\%$ of total parameters).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "abstract": "Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "abstract": "Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "abstract": "Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We propose an algorithm for generating lattice field configurations based on the approximate inversion of a renormalization-group blocking transformation. We optimize the blocking transformation using a ``perfect blocking'' condition so that the blocked lattice distribution is well approximated by a simple coarse action. The blocking is separated into an invertible smoothing transformation followed by decimation. Machine learning, in the form of a conditional normalizing flow, is used to reconstruct the short-distance degrees of freedom removed by the decimation. A short fine-action rethermalization then removes the residual mismatch. Because the coarse ensemble supplies the long-distance modes, the same blocking transformation and conditional flow can be reused recursively on larger lattices, producing a cascade of configurations from an initial small-volume ensemble. We test the method in two-dimensional $\u03c6^4$ theory with $\u03bb=1$ at criticality and demonstrate stable cascade upscaling from $16^2$ to $2048^2$ lattices on local computational resources. Controlled rethermalization tests show that short-distance mismatches relax rapidly, whereas a deliberately introduced mismatch in the relevant thermal direction relaxes much more slowly. The construction uses ingredients that admit natural extensions to higher-dimensional systems and, ultimately, to gauge and fermionic degrees of freedom.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "abstract": "Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "abstract": "We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embedding\" onclick=\"window.location.href='wiki.html'\">embedding\" onclick=\"window.location.href='wiki.html'\">embeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "abstract": "Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: https://github.com/topo-focus/Topofocus",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "abstract": "A protein's function follows from the structure it adopts, and which structure that is depends on the pathway taken. In programmable matter the target is fixed before assembly, and whatever else forms is treated as error. Here we show that pathways themselves form a design space. Using reinforcement learning, we fold model DNA-coated droplet chains into rigid two-dimensional geometries, uncovering two classes of pathways: downhill, in which bonds are only added, and detour, in which bonds are broken and remade before the target is reached: for some the only route that exists. Coarse-graining pathways by interactions gives experimentally realizable protocols. Some produce one geometry, others several: structures sharing a detour route can be cycled between, while those that coexist assemble into superstructures inaccessible to a uniform product. Function emerges from the pathways rather than being designed. Designing the process instead of the components could give colloidal materials that reconfigure and repair themselves on demand.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "abstract": "We prove that the six-vertex graph with edge set $\\{ab,bc,cd,de,af,bf,df\\}$ has the Erd\u0151s-Hajnal property. The proof adapts the iterative-sparsification method of Nguyen, Scott, and Seymour within the comb-based framework of Huang, Ju, and Zhou.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "abstract": "In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "abstract": "Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image  geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "abstract": "Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "abstract": "As an initial step toward personal memory rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG) for large language models (LLMs), this study presents a retrieval-only case study over one user's LINE conversation history. We segmented 358,896 messages into 22,329 temporally coherent chunks and constructed three search representations: raw_text, a generated summary, and embedding_text, which combines a summary with a raw-text excerpt and other fixed text. We compared BM25, dense vector retrieval, and linear hybrid retrieval on 100 evaluation questions verified by a single annotator. Among individual retrievers, embedding_text_bm25 achieved the highest point estimate, with Recall@5 of 0.584. We then explored six retriever pairings and 21 weights, for 126 configurations on the same evaluation set. The selected combination of embedding_text_bm25 and embedding_text_vector at beta = 0.45 achieved Recall@5 = 0.697, MRR@5 = 0.595, and nDCG@5 = 0.575. Its Recall@5 exceeded that of embedding_text_bm25 by 0.113, with a question-level paired percentile-bootstrap 95% confidence interval of [0.048, 0.184]. This interval is conditional on fixing the configuration selected on the same 100 questions and does not account for uncertainty from configuration selection or weight search. The difference from a summary-based hybrid at beta = 0.50 was 0.050, with a 95% confidence interval of [-0.013, 0.115], so no clear difference could be established. The 17 aggregate questions also yielded lower point estimates than the other question types, suggesting that flat chunk-level retrieval struggles when evidence is distributed across multiple times and conversations. This evaluation is an exploratory single-user, single-annotator study conducted on the same question set used for configuration search; it does not evaluate final answer generation or generalization to unseen questions.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "abstract": "The open radio access network (O-RAN) is evolving toward agentic operation, where llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">large language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "abstract": "Magic, or nonstabilizerness, is the resource that lifts Clifford circuits to universal quantum computation and has become a standard diagnostic of many-body states. For a state shared between two parties, however, a basic question has remained open: how much of the magic resides in the correlations between the parties rather than in their local bases? Isolating this nonlocal magic requires minimizing over all local bases, an optimization that has so far resisted exact solution. Here we solve it for the stabilizer fidelity: the nonlocal magic of every pure multiqubit state is the distance of its entanglement spectrum from the closest spectrum of Bell pairs. The same quantity governs an apparently unrelated task: a family of states universally embezzles entanglement under local operations and classical communication if and only if its nonlocal magic diverges. The deciding property is not the amount of entanglement but the way the entanglement spectrum spreads its weight across factor-of-two windows of rank, so that critical chains and random-singlet states, with identical logarithmic entanglement scaling, carry unbounded and vanishing nonlocal magic, respectively. Nonlocal magic thereby becomes an operationally meaningful property of quantum correlations, directly accessible to tensor-network simulations and, through entanglement spectroscopy, to experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "abstract": "Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "abstract": "We introduce a notion of continuity equation on metric spaces that is capable of describing curves of probability measures which are absolutely continuous, and more generally of bounded variation (BV), with respect to the 1-Wasserstein distance. This continuity equation is based on a notion of measure-valued derivations, whose basic theory is also developed in this paper. On $\\mathbb{R}^n$, our formulation is consistent with the continuity equation with singular flux introduced by Almi--Rossi--Savar\u00e9 (arXiv:2506.15333), including the corresponding notion of minimal solutions. In this work, we characterize BV-curves in the space of probability measures equipped with the (extended) 1-Wasserstein distance as those curves satisfying the continuity equation with a measure-valued derivation of finite mass. To this aim, we extend our previous work (Calc.Var.(2024)63:16) on probabilistic representations on BV-curves and construct from them measure-valued derivations (resp. flux measures) on geodesic metric spaces (resp. on $\\mathbb{R}^n$).",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "abstract": "rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embedding\" onclick=\"window.location.href='wiki.html'\">embedding\" onclick=\"window.location.href='wiki.html'\">embeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "abstract": "Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "abstract": "Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "abstract": "Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training (\"RL-for-LLMs\") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "abstract": "In rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "abstract": "We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "abstract": "Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "abstract": "Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">Retrieval-Augmented Generation (RAG), and automated data labeling.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "abstract": "Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \\textsc{\\textsc{MedREAL}} (\\textbf{Med}ical \\textbf{RE}asoning-driven \\textbf{A}nswering and \\textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \\textsc{MedREAL} introduces \\textbf{S}eg \\textbf{A}nchored \\textbf{R}easoning \\textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \\texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \\textbf{R}easoning-to-\\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \\textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\\% gIoU and 70.47\\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \\textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "abstract": "LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, evaluated with five generators (3B-70B open-weight models and GPT-5.4) and six judges (20B to frontier scale) under paired with- and without-ground-truth conditions. Judge alignment degrades monotonically with task difficulty, 1.5x faster without ground truth, and on hard queries without ground truth all six judges converge to a narrow 77-82% band regardless of scale, revealing a structural ceiling driven primarily by task difficulty, though its height is partly prompt-dependent for weaker generators, that model capacity alone cannot overcome. Ground-truth exposure is not uniformly beneficial: it reduces alignment for GPT-5.4 (1.5 pp) and Gemini-2.5-Pro (3.9 pp), consistent with over-anchoring. Among mitigation strategies, chain-of-thought reasoning and judge temperature both have negligible effect, while structured evaluation rubrics improve alignment by up to 6.5 pp but do not generalize uniformly across judge-generator pairs. With ground truth, QwQ-32B best matches the programmatic reference, while a human validation study identifies GPT-OSS-120B as the most human-aligned judge; without it, frontier judges lead only marginally within the shared ceiling. These results expose fundamental limitations of current LLM judges and yield practical guidelines for reliable evaluation in agentic systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "abstract": "The rapid growth of publicly available digital information has rendered manual open-source intelligence (OSINT) analysis insufficient for modern intelligence, cybersecurity, and cyber investigation. Large language models (LLMs) and agentic AI systems, capable of tool use, multi-step reasoning, and iterative intelligence generation, have emerged as promising solutions, yet evaluation frameworks have not kept pace with reported capabilities. This survey systematically reviews 74 studies and makes four contributions. First, it establishes agentic AI as a distinct analytical category rather than an extension of LLM prompting, organising the literature through an 11-category taxonomy covering LLM foundations, agentic architectures, rag\" onclick=\"window.location.href='wiki.html'\">rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG), knowledge graphs, prompt engineering, domain adaptation, evaluation benchmarks, and risk. Second, it identifies the hallucination-validation gap as a corpus-level finding: although hallucination is recognised as a major reliability concern in over twenty studies, end-to-end hallucination is empirically measured in only one OSINT-specific RAG-based system, non-reproducible conditions, while related reasoning and factual-correction studies evaluate general-domain question answering rather than OSINT. Third, it maps existing research to the OSINT lifecycle, showing strong support for collection and analysis but limited coverage of verification, reporting, dissemination, and decision support. Fourth, it derives a ten-point research agenda addressing evaluation, benchmarking, hallucination measurement, adversarial robustness, dark-web coverage, multimodal intelligence, and governance. It concludes that a human-AI co-pilot model, where LLMs assist collection and triage while analysts retain responsibility for verification and decision-making, represents the most defensible near-term deployment architecture.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "abstract": "AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "abstract": "As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \\textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\\% and 14.4\\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "abstract": "We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "abstract": "The emergence of \"vibe coding\" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native). Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps. Code and benchmark resources are available at: https://github.com/snowmountainAi/webdevbench and https://webdevbench.com/.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "abstract": "llm\" onclick=\"window.location.href='wiki.html'\">llm\" onclick=\"window.location.href='wiki.html'\">Large language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope's effectiveness in enhancing LLM tool use.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
]; fulfillment fell from 79.1% to 60.9%, while paired safe-useful completion rose 21.8 points [9.5, 35.2]. Some answers reconstructed a value that never entered context or used filtered row counts as an oracle: shaping one execution is not noninterference. Write controls, durable approval, and temporal and aggregate policies lie outside this evaluation.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "abstract": "Discovering PDEs in heterogeneous media requires jointly identifying the governing operator and the unknown spatial fields that parameterize it. These tasks are coupled: changing field placement changes the differential law, while a sufficiently flexible field can conceal structural error on a single trajectory. We present Hypothesize, Evaluate, Refine for PDE Discovery (HER-PDE), a scientific-agent framework that discovers compositional PDE structure together with nonparametric, time-invariant coefficient fields. The Agent analyzes two noisy trajectories generated by different excitations, proposes complete expression-tree hypotheses, and combines creative structural exploration with local candidate refinement. Its Hypothesis Evaluation Interface (HEI) estimates only the fields explicitly declared in each hypothesis, never adds missing terms, and scores structures by bidirectional cross-excitation transfer. The selected law is subsequently audited on a sealed temporal interval. Across five controlled two-dimensional systems observed with 5 percent relative Gaussian state noise, the Agent recovers the generating operator in all five cases, including equivalent signed-field and product-rule parameterizations. Across nine unknown coefficient fields, the recovered fields attain a median Pearson correlation of approximately 0.85 and a median relative L2 error of approximately 0.28. These results show that agent-guided hypothesis refinement can recover heterogeneous governing laws without prescribing a parametric form for their spatial coefficients.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "abstract": "Cross-city point-of-interest (POI) recommendation is crucial for navigating unfamiliar urban environments, yet its progress has historically been constrained by data limitations. Using the recently proposed large-scale benchmark Trip World, we empirically re-examine whether conclusions drawn on small prior benchmarks still hold under worldwide coverage, low home-destination region overlap, and large, semantically rich POI inventories. Our evaluation surfaces three bottlenecks of representative state-of-the-art methods: (1) hometown-aware models appear to rely more on destination-region priors than on user-specific preference transfer; (2) their accuracy-efficiency trade-off degrades at this scale, where the simplest model is among the strongest; and (3) existing mechanisms for integrating semantic metadata yield little benefit. We further include a diagnostic pilot on agentic methods adapted from next-POI recommendation, finding that naive adaptation trails a simple popularity prior even though the relevant semantic signal is present in the data. These results highlight the need for task-specific designs that support cross-city preference transfer, semantic grounding, and scalable reasoning over unseen destination inventories.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "abstract": "GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .",
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
    "abstract": "Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.",
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
    "abstract": "Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\\href{this https URL}{WhatIfBench}$.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "abstract": "Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\\%--39.8\\% on average while maintaining competitive accuracy with full-length reasoning.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "abstract": "Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \\emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \\emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model&#39;s excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \\href{this https URL}{our GitHub repository}.",
    "topics": [
      "rag-retrieval"
    ],
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "abstract": "Discovering governing partial differential equations (PDEs) from observational data remains a core challenge across the sciences. Existing sparse-regression, symbolic-regression, and LLM-based approaches can be constrained by predefined libraries, noise sensitivity, hallucination, or limited iterative refinement. We introduce \\textbf{MAGE} (\\textbf{M}ultimodal \\textbf{A}gentic \\textbf{G}overning \\textbf{E}quation Discovery), an agentic framework that organizes PDE discovery as a \\textit{confidence governed hypothesis validation loop} inspired by the scientific cycle of observation, hypothesis, and falsification. Four role-specialized agents collaborate: a \\textit{Differential Observer} computing derivatives and diagnostic visualizations; a VLM-powered \\textit{Phenomenology Extractor} distilling qualitative cues from multimodal diagnostics; an LLM-driven \\textit{Governing Law Synthesizer} proposing candidates without a predefined library; and an \\textit{Equation Arbiter} fitting coefficients and assigning confidence scores. Discovery iterates until the top candidate clears a user-specified threshold, providing a structured process with an explicit accept-reject protocol. On the evaluated canonical PDE suite, MAGE obtains \\textbf{8/8} exact structural recovery and the lowest coefficient error among the compared methods on \\textbf{7/8} systems, with improvements of up to \\textbf{4 orders of magnitude} and a geometric-mean improvement of approximately \\textbf{3 orders of magnitude}. The pipeline also recovers the expected operators in two complex geometries and, on one laboratory sensor record, selects a cubic restoring-force model with held-out $R^2=0.98538$. These results support further study of structured agentic reasoning for library-free governing-law discovery, while broader generalization remains to be evaluated.",
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
    "abstract": "Corporate training teams need scalable and explainable tools to improve workforce communication in multilingual settings. Existing systems often score text, audio, or video in isolation, or produce black-box outputs that are difficult to audit for coaching use. This paper presents SETU, an agentic ecosystem for corporate communication coaching aimed at recruiters, frontline sales professionals and training units who prepare for audience specific conversations. SETU is designed for two scoped scenarios: (i) recruiter-candidate eligibility-and-interest calls with persona context and (ii) sales pitches with target-audience adaptation; owing to limited evaluation resources, this paper reports results on scenario (ii) only. The ecosystem decomposes analysis into specialized video, audio-speech, text-relevance, scoring, notification and reporting agents coordinated through trust-aware orchestration. It generates modality-attributed coaching reports for formative training, with human reviewers retaining final judgment. The name SETU (bridge in several Indic languages) reflects the goal of bridging communication gaps across regional languages and audience expectations.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "abstract": "Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.",
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
    "abstract": "Continual multimodal instruction tuning requires multimodal large language models to acquire new task abilities sequentially while preserving previously learned knowledge. LoRA-MoE provides a promising solution by introducing expert-based capacity, but repeatedly learning and maintaining full LoRA experts leads to substantial parameter overhead. This raises a natural question: is full expert expansion necessary for every new task? To answer it, we analyze the SVD of task-specific LoRA updates and observe substantial overlap in their input- and output-side LoRA direction subspaces, with task-specific adaptation largely captured by lightweight coordinates over these subspaces. Motivated by this observation, we propose CoRe-MoE, a Compact Reusable MoE framework for parameter-efficient continual multimodal instruction tuning. CoRe-MoE extracts reusable input- and output-side direction bases from an initial expert bank, and for subsequent tasks trains only compact coordinate experts together with task-specific low-rank routers. Experiments on two representative MLLMs show that CoRe-MoE improves final average performance over the strongest competing baseline by up to 5.90 points, while using less than 1% of the trainable parameters required by sequential LoRA for later tasks. The code is publicly available at this https URL.",
    "topics": [
      "multi-modal"
    ],
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "abstract": "Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.\nIn this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.",
    "topics": [
      "llm-reasoning"
    ],
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "abstract": "Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a rag\" onclick=\"window.location.href='wiki.html'\">retrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "abstract": "We present RoboPhD, a system where AI agents autonomously conduct research to improve Text-to-SQL performance. RoboPhD implements a closed-loop evolution cycle with two coordinated components: a SQL Generation agent composed of a database analysis script and SQL generation instructions, and an Evolution agent that designs new versions based on performance feedback. Central to the framework is an ELO-based selection mechanism enabling survival-of-the-fittest dynamics while handling non-transitivity in performance. Starting from a naive 70-line baseline, RoboPhD evolves agents through iterative cross-pollination, discovering effective techniques without any external guidance on the Text-to-SQL domain. Our best agent, evolved to 1500 lines over 18 iterations, autonomously discovered strategies such as size-adaptive database analysis that adjusts depth based on schema complexity and SQL generation patterns for column selection, evidence interpretation, and aggregation. Evolution provides the largest gains on cheaper models: while we improve by 2.3 points over a strong Claude Opus 4.5 naive baseline, we show an improvement of 8.9 points over the weaker Claude Haiku model. This enables 'skip a tier' deployment: evolved Haiku exceeds naive Sonnet accuracy, and evolved Sonnet exceeds naive Opus, both at lower cost. The full system achieves 73.67% accuracy on the BIRD test set, demonstrating that AI can autonomously build a strong agentic system with only a trivial human-provided starting point.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "abstract": "While most efforts to improve LLM-based tool-using agents focus on the agent itself - through larger models, better prompting, or fine-tuning - agent performance increasingly plateaus due to the quality of the tool interfaces these agents consume. Tool descriptions are often written for human developers and tolerate ambiguity that agents cannot resolve, particularly as the number of candidate tools grows. Existing approaches to improving tool interfaces (1) require re-running a multi-stage per-tool pipeline - synthesizing queries, executing an agent to collect trajectories, annotating trajectories, and prompting a strong LLM multiple times - for every API that enters the catalog, and (2) typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to internalize reusable patterns of what makes a tool description effective. To support this approach, we construct a large-scale dataset of high-quality tool interfaces derived from real-world APIs through a principled data synthesis workflow. Experiments on widely adopted benchmarks show that Trace-Free+ improves robustness as tool catalogs scale to 150+ candidates - in scaling experiments, reducing accuracy degradation by 29.23% and improving average query-level success by 60.89% on StableToolBench - generalizes across domains without retraining, and provides complementary gains on top of agent fine-tuning.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "abstract": "We exhibit new subgroups of rational torsion points in geometrically simple Jacobians of genus-two curves over $\\mathbb Q$. The largest group, which has order 96 and invariants [2,2,2,12], is realized by curves of the form $y^2 = x(x-a^2)(x-b^2)(x-c^2)(x-u^2)(x-v^2)$ where $a,b,c,u,v$ are positive integers that satisfy $a^2 + b^2 + c^2 = u^2 + v^2$ and $a^4 + b^4 + c^4 = u^4 + v^4$. We also find realizations of the groups [2,2,20], [2,2,4,4], [2,2,2,8], [2,4,8], and [6,6]. Finally, we record, to the best of our knowledge, all known subgroups that arise in genus-two Jacobians over $\\mathbb Q$, in the geometrically simple case and in general.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "abstract": "Robotic sorting of recyclable waste is challenging due to the deformable and geometrically inconsistent nature of target objects. We present a training-free suction grasping system for sorting deformed aseptic beverage cartons, decoupling target identification from grasp-point selection. An open-vocabulary vision-language model detects cartons from a text prompt, SAM2 refines each detection into an instance mask, and a geometric scoring method selects the suction point by combining surface flatness with normal alignment. Three geometric methods are compared: k-nearest-neighbour PCA, Sobel cross-product, and RANSAC plane fitting. Evaluated on a real robot across three deformation levels and 35 cluttered scenes, single-object grasp success reaches 88.2% and end-to-end retrieval in clutter is 72.6%.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "abstract": "Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "abstract": "Exponentially decaying long-range hoppings are ubiquitous in realistic tight-binding models and are often truncated to obtain a finite-range description. We show that this approximation can fail dramatically in non-Hermitian systems under open boundary conditions: an infinitesimal long-range hopping can nonperturbatively reconstruct the spectrum and eigenstates of a short-range non-Hermitian system. The mechanism is controlled by a competition between the decay length of infinitesimal long-range hoppings and the localization length of non-Hermitian skin modes, leading to a sharp transition as the decay rate is tuned. In one dimension, we show that a squeezed generalized Brillouin zone (GBZ) replaces the original GBZ of the short-ranged Hamiltonian, yielding the reconstructed open-boundary spectrum. In two or higher dimensions, we formulate a squeezed amoeba formulation describing the reconstructed spectral density. We further show that long-range hoppings can qualitatively reshape Green's function, which can be readily detected in experiments.",
    "topics": [
      "ai-agents"
    ],
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "abstract": "We introduce a renormalization-group (RG) guided machine-learning algorithm for lattice field generation based on approximate inversion of an RG transformation. A ` PH0  PH1 <div class="tag-item size-${size}" data-concept="${concept}">${concept}</div> PH2 
<div class="tag-list-item" data-concept="${concept}">
<span class="tag-list-name">${concept}</span>
<span class="tag-list-count">${data.count}</span>
</div>
     PH3 
<h3>${concept}</h3>
<div class="tag-details-meta">
<span><strong>${data.count}</strong> mentions</span>
<span><strong>${uniquePapers.length}</strong> papers</span>
</div>
<ul class="tag-details-papers">
      ${uniquePapers.map(paper =>  PH4 ).join('')}
</ul>
  `;
  
  details.classList.add('active');
  details.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function updateView() {
  const topicFilter = document.getElementById('topicFilter').value;
  const conceptMap = extractConcepts(papers, topicFilter);
  
  renderTagCloud(conceptMap);
  renderTagList(conceptMap);
  
  // Hide details when filter changes
  document.getElementById('tagDetails').classList.remove('active');
}

// View toggle
document.getElementById('cloudView').addEventListener('click', () => {
  document.getElementById('tagCloud').style.display = 'flex';
  document.getElementById('tagList').style.display = 'none';
  document.getElementById('cloudView').classList.add('active');
  document.getElementById('listView').classList.remove('active');
});

document.getElementById('listView').addEventListener('click', () => {
  document.getElementById('tagCloud').style.display = 'none';
  document.getElementById('tagList').style.display = 'grid';
  document.getElementById('listView').classList.add('active');
  document.getElementById('cloudView').classList.remove('active');
});

// Topic filter
document.getElementById('topicFilter').addEventListener('change', updateView);

// Initial render
updateView();
</script>
