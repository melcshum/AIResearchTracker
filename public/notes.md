---
title: "Paper Notes & Progress"
---

Track your reading progress and add personal annotations to papers. All data is stored locally in your browser.

<div class="notes-container">
<div class="notes-header">
<h2>My Paper Notes</h2>
<div class="notes-actions">
<button id="exportNotesBtn" class="btn-primary">Export Notes</button>
<button id="importNotesBtn" class="btn-secondary">Import Notes</button>
<input type="file" id="importFile" accept=".json" style="display:none">
</div>
</div>

<div class="progress-summary">
<div class="progress-stat">
<div class="progress-value" id="toReadCount">0</div>
<div class="progress-label">To Read</div>
</div>
<div class="progress-stat">
<div class="progress-value" id="readingCount">0</div>
<div class="progress-label">Reading</div>
</div>
<div class="progress-stat">
<div class="progress-value" id="readCount">0</div>
<div class="progress-label">Read</div>
</div>
<div class="progress-stat">
<div class="progress-value" id="notesCount">0</div>
<div class="progress-label">With Notes</div>
</div>
</div>

<div class="notes-controls">
<input type="text" id="paperSearch" placeholder="Search papers..." class="search-input">
<select id="statusFilter" class="filter-select">
<option value="">All Status</option>
<option value="to-read">To Read</option>
<option value="reading">Reading</option>
<option value="read">Read</option>
</select>
<select id="hasNotesFilter" class="filter-select">
<option value="">All Papers</option>
<option value="yes">Has Notes</option>
<option value="no">No Notes</option>
</select>
</div>

<div id="papersList" class="papers-list"></div>
</div>

<style>
.notes-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.notes-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 15px;
}

.notes-header h2 {
  margin: 0;
  color: #2c3e50;
}

.notes-actions {
  display: flex;
  gap: 10px;
}

.btn-primary, .btn-secondary {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.btn-primary {
  background: #4a90e2;
  color: white;
}

.btn-primary:hover {
  background: #357abd;
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

.progress-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
}

.progress-stat {
  text-align: center;
}

.progress-value {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 5px;
}

.progress-label {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.9;
}

.notes-controls {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.search-input {
  flex: 1;
  min-width: 200px;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.search-input:focus {
  outline: none;
  border-color: #4a90e2;
}

.filter-select {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.papers-list {
  display: grid;
  gap: 15px;
}

.paper-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  transition: all 0.2s;
}

.paper-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.paper-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 15px;
  gap: 15px;
}

.paper-title {
  flex: 1;
}

.paper-title a {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  text-decoration: none;
}

.paper-title a:hover {
  color: #4a90e2;
}

.paper-meta {
  color: #666;
  font-size: 14px;
  margin-top: 5px;
}

.status-selector {
  display: flex;
  gap: 5px;
}

.status-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: all 0.2s;
}

.status-btn:hover {
  background: #f0f0f0;
}

.status-btn.active {
  background: #4a90e2;
  color: white;
  border-color: #4a90e2;
}

.status-btn.to-read.active {
  background: #ffc107;
  border-color: #ffc107;
  color: #000;
}

.status-btn.reading.active {
  background: #17a2b8;
  border-color: #17a2b8;
}

.status-btn.read.active {
  background: #28a745;
  border-color: #28a745;
}

.notes-section {
  margin-top: 15px;
}

.notes-textarea {
  width: 100%;
  min-height: 100px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-family: inherit;
  font-size: 14px;
  resize: vertical;
}

.notes-textarea:focus {
  outline: none;
  border-color: #4a90e2;
}

.notes-saved {
  color: #28a745;
  font-size: 12px;
  margin-top: 5px;
  opacity: 0;
  transition: opacity 0.3s;
}

.notes-saved.show {
  opacity: 1;
}

.topic-tag {
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-top: 8px;
}
</style>

<script>
const papers = [
  {
    "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
    "authors": "Yulong Zhang, Li Wang, Wei Du, Peilin Li, Yuqin Dai Zhiyuan Zhao, Lingyong Fang, Ziniu Liu, Ru Zhang, Huijia Zhu, Gongshen Liu",
    "date": "2025-10-03",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2510.02816v1",
    "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html"
  },
  {
    "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
    "authors": "V\u00edctor Gallego",
    "date": "2026-05-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2605.30003v1",
    "url": "papers/2026-05-28/2605.30003v1-Discovering-Cooperative-Pipelines-Autoresearch-for-Sequential-Social-Dilemmas.html"
  },
  {
    "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
    "authors": "Yujuan Ding, Linyin Luo, Shijie Wang, Xu Yuan, Yunshan Ma, Yi Bin, Wenqi Fan, Qing Li",
    "date": "2026-08-24",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.22688v1",
    "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html"
  },
  {
    "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
    "authors": "Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib, Yordanos Tessema, Chang-Tien Lu",
    "date": "2026-08-23",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.22634v1",
    "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html"
  },
  {
    "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
    "authors": "Yuhan Meng, Shaofei Li, Jionghao Huang, Jiandong Jin, Puyi Wang, Hanlin Jiang, Anis Yusof, Peng Jiang, Zhenkai Liang, Yao Guo, Ding Li",
    "date": "2026-08-15",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.15012v1",
    "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html"
  },
  {
    "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
    "authors": "Nolasque, T, Grey, J, Pham, C, Vani, A",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27506",
    "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html"
  },
  {
    "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
    "authors": "Dore, D, Damo, G, Cabrio, E, Villata, S",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27471",
    "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html"
  },
  {
    "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
    "authors": "Millstone, M, Akidau, T, Br%C3%BCderl, J, Pekker, M",
    "date": "2026-08-31",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27646",
    "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html"
  },
  {
    "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
    "authors": "Huang, Y, He, W, Lin, Z, Liu, C, Liang, D, Cui, Z",
    "date": "2026-08-31",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27475",
    "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html"
  },
  {
    "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
    "authors": "Li, P, Song, Y, Xue, H, de Rijke, M, Salim, F D",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27840",
    "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Han, Y, Qian, T",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27508",
    "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html"
  },
  {
    "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
    "authors": "Ghawate, P, Patil, T",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27484",
    "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html"
  },
  {
    "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
    "authors": "Wang, Y, Du, Y, Liu, Z, Zhang, R, Zhao, B, Yang, B, Kong, M, Qu, L, Wei, H, Liu, J, Zhu, Q",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27953",
    "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html"
  },
  {
    "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
    "authors": "Cheng, W, Xiang, H, Li, J, Wang, H, Chen, W",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27963",
    "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html"
  },
  {
    "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
    "authors": "Liao, D, Wang, Y, Shi, F, Yu, Y",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27945",
    "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Pekhale, S M, Roy, A, Sarkar, R, Chakraborty, S",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.27869",
    "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html"
  },
  {
    "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
    "authors": "Tejas, J M, Roy, U B, Goswami, T, Goswami, S, Dhar, M",
    "date": "2026-08-31",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27524",
    "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html"
  },
  {
    "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
    "authors": "Singh, V, Doshi, A, Narsimhan, M, Ghosh, S, Luna, K",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.27548",
    "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html"
  },
  {
    "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
    "authors": "Liu, R, Gu, N, Ai, M, Li, Y, Fu, P, Lin, Z, Wang, W",
    "date": "2026-08-31",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.27867",
    "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html"
  },
  {
    "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
    "authors": "Birla, L, Savagaonkar, M, Visnu, Rasipuram, S, Sengupta, S",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27919",
    "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2607.22319v1",
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2601.01126v2",
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2602.20426v2",
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Rational torsion on simple genus two Jacobians",
    "authors": "Jennifer S. Balakrishnan, Filip Najman, Ari Shnidman, Andrew V. Sutherland",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28543v1",
    "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html"
  },
  {
    "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
    "authors": "Marin Maletic, Goran Vasiljevic",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28246v1",
    "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html"
  },
  {
    "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
    "authors": "Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28567v1",
    "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html"
  },
  {
    "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
    "authors": "Ding Gu, Zhanpeng Fu, Yu-Min Hu, Zhong Wang",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28577v1",
    "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html"
  },
  {
    "title": "Renormalization-guided cascade upscaling for lattice field generation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28581v1",
    "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html"
  },
  {
    "title": "Bounds for inertialess dynamo",
    "authors": "Ali Arslan, Hezekiah Grayer",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28584v1",
    "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html"
  },
  {
    "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
    "authors": "Hai-Lan Luo, Weitang Li, Luca Moreschini, Jonathan Denlinger, Zhigang Shuai, Claudia Ojeda-Aristizabal, Alessandra Lanzara",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28583v1",
    "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html"
  },
  {
    "title": "Logos: An Agent Harness on a Cross-Process Bus",
    "authors": "Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28553v1",
    "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html"
  },
  {
    "title": "Fast and efficient nested sampling with BEST",
    "authors": "Andreas Nygaard",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28514v1",
    "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html"
  },
  {
    "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
    "authors": "Javier Aguilar Mart\u00edn",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28541v1",
    "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html"
  },
  {
    "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
    "authors": "Xinyi Zhang, Yutong Li, Peijie Sun",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28503v1",
    "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html"
  },
  {
    "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
    "authors": "Lukas M\u00fcller, Lukas Woike",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28579v1",
    "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html"
  },
  {
    "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
    "authors": "Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara",
    "date": "2026-08-28",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.28248v1",
    "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html"
  },
  {
    "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
    "authors": "Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28572v1",
    "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html"
  },
  {
    "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
    "authors": "Akshay Pal, Andrew Lucas, Umang Mehta",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28588v1",
    "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html"
  },
  {
    "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
    "authors": "Yuansi Chen, Yunbum Kook",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28566v1",
    "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html"
  },
  {
    "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
    "authors": "Chengpiao Huang, Kaizheng Wang",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28576v1",
    "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html"
  },
  {
    "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
    "authors": "Dominik Storck, Tobias Eisenreich, Stefan Wagner",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28403v1",
    "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html"
  },
  {
    "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
    "authors": "Adil Alshammari, Hayretdin Bahsi",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28542v1",
    "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html"
  },
  {
    "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
    "authors": "Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Md. Sadman Haque, Mohd Ariful Haque",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28216v1",
    "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html"
  },
  {
    "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
    "authors": "Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28547v1",
    "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html"
  },
  {
    "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
    "authors": "Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28578v1",
    "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html"
  },
  {
    "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
    "authors": "Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28534v1",
    "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.28144v1",
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
    "authors": "Anna Hasenfratz, Ethan T. Neil, Letizia Parato, Noah Schwartz",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28580v1",
    "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html"
  },
  {
    "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
    "authors": "Seungyeon Kim, No\u00e9mie Jaquier",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28570v1",
    "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html"
  },
  {
    "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
    "authors": "Vaibhav Mehandiratta, Saket Ramchandra",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28589v1",
    "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html"
  },
  {
    "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
    "authors": "Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28218v1",
    "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html"
  },
  {
    "title": "Machine learned designs of functional colloidal foldamers",
    "authors": "Ryan van Mastrigt, Zorana Zeravcic",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28554v1",
    "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html"
  },
  {
    "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
    "authors": "Viet-Hoang Tran, Tan M. Nguyen",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28551v1",
    "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.28399v1",
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Video Generative Models as Geometry Learner",
    "authors": "Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28549v1",
    "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html"
  },
  {
    "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
    "authors": "Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28529v1",
    "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html"
  },
  {
    "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
    "authors": "Akito Hattori",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27809v1",
    "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html"
  },
  {
    "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
    "authors": "Le Xia, Rose Qingyang Hu, Paul S. Kudyba, Zhenlin An, Haijian Sun",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28532v1",
    "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html"
  },
  {
    "title": "Exact quantification of nonlocal magic",
    "authors": "Piotr Sierant",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28563v1",
    "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.28383v1",
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
    "authors": "Ehsan Abedi, Zhenhao Li, Timo Schultz",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28586v1",
    "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html"
  },
  {
    "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
    "authors": "Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee",
    "date": "2026-08-28",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.28389v1",
    "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html"
  },
  {
    "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
    "authors": "Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27101v1",
    "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27036v1",
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27046v1",
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
    "authors": "Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27661v1",
    "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.26921v1",
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.26870v1",
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
    "authors": "Corey D. C. Heath",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.27121v1",
    "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.26856v1",
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2608.26623v1",
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2607.03233v1",
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2604.04820v1",
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2607.14642v1",
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2606.20041v1",
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
    "authors": "Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi",
    "date": "2026-05-06",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2605.04637v1",
    "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html"
  },
  {
    "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
    "authors": "Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth",
    "date": "2025-10-22",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2510.20036v2",
    "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html"
  }
];

function loadNotes() {
  return JSON.parse(localStorage.getItem('paperNotes') || '{}');
}

function saveNotes(notes) {
  localStorage.setItem('paperNotes', JSON.stringify(notes));
}

function updateProgressSummary() {
  const notes = loadNotes();
  const statuses = Object.values(notes).map(n => n.status).filter(s => s);
  
  document.getElementById('toReadCount').textContent = statuses.filter(s => s === 'to-read').length;
  document.getElementById('readingCount').textContent = statuses.filter(s => s === 'reading').length;
  document.getElementById('readCount').textContent = statuses.filter(s => s === 'read').length;
  document.getElementById('notesCount').textContent = Object.values(notes).filter(n => n.notes && n.notes.trim()).length;
}

function renderPapers() {
  const searchTerm = document.getElementById('paperSearch').value.toLowerCase();
  const statusFilter = document.getElementById('statusFilter').value;
  const hasNotesFilter = document.getElementById('hasNotesFilter').value;
  const notes = loadNotes();
  
  let filtered = papers.filter(paper => {
    const matchesSearch = !searchTerm || 
      paper.title.toLowerCase().includes(searchTerm) ||
      paper.authors.toLowerCase().includes(searchTerm);
    
    const paperNotes = notes[paper.arxiv_id] || {};
    const matchesStatus = !statusFilter || paperNotes.status === statusFilter;
    const hasNotes = paperNotes.notes && paperNotes.notes.trim();
    const matchesNotes = !hasNotesFilter || 
      (hasNotesFilter === 'yes' && hasNotes) ||
      (hasNotesFilter === 'no' && !hasNotes);
    
    return matchesSearch && matchesStatus && matchesNotes;
  });
  
  const container = document.getElementById('papersList');
  
  if (filtered.length === 0) {
    container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">No papers found.</p>';
    return;
  }
  
  container.innerHTML = filtered.map(paper => {
    const paperNotes = notes[paper.arxiv_id] || {};
    const status = paperNotes.status || '';
    const noteText = paperNotes.notes || '';
    
    return  PH0 <span class="topic-tag">${t}</span> PH1 ;
  }).join('');
  
  // Attach event listeners
  document.querySelectorAll('.status-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const card = this.closest('.paper-card');
      const arxivId = card.dataset.arxivId;
      const status = this.dataset.status;
      
      // Update UI
      card.querySelectorAll('.status-btn').forEach(b => b.classList.remove('active'));
      if (card.querySelector( PH2 ).classList.contains('active')) {
        // Deselect if clicking same button
        this.classList.remove('active');
        updatePaperStatus(arxivId, '');
      } else {
        this.classList.add('active');
        updatePaperStatus(arxivId, status);
      }
    });
  });
  
  document.querySelectorAll('.notes-textarea').forEach(textarea => {
    let timeout;
    textarea.addEventListener('input', function() {
      const card = this.closest('.paper-card');
      const arxivId = card.dataset.arxivId;
      const savedMsg = card.querySelector('.notes-saved');
      
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        updatePaperNotes(arxivId, this.value);
        savedMsg.classList.add('show');
        setTimeout(() => savedMsg.classList.remove('show'), 2000);
        updateProgressSummary();
      }, 500);
    });
  });
}

function updatePaperStatus(arxivId, status) {
  const notes = loadNotes();
  if (!notes[arxivId]) notes[arxivId] = {};
  notes[arxivId].status = status;
  saveNotes(notes);
  updateProgressSummary();
}

function updatePaperNotes(arxivId, noteText) {
  const notes = loadNotes();
  if (!notes[arxivId]) notes[arxivId] = {};
  notes[arxivId].notes = noteText;
  saveNotes(notes);
}

function exportNotes() {
  const notes = loadNotes();
  const data = {
    exportDate: new Date().toISOString(),
    notes: notes
  };
  
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download =  PH3 ;
  a.click();
  URL.revokeObjectURL(url);
}

function importNotes(file) {
  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const data = JSON.parse(e.target.result);
      if (data.notes) {
        const existing = loadNotes();
        const merged = {...existing, ...data.notes};
        saveNotes(merged);
        renderPapers();
        updateProgressSummary();
        alert('Notes imported successfully!');
      } else {
        alert('Invalid file format');
      }
    } catch (err) {
      alert('Error importing file: ' + err.message);
    }
  };
  reader.readAsText(file);
}

document.getElementById('exportNotesBtn').addEventListener('click', exportNotes);
document.getElementById('importNotesBtn').addEventListener('click', () => {
  document.getElementById('importFile').click();
});
document.getElementById('importFile').addEventListener('change', (e) => {
  if (e.target.files.length > 0) {
    importNotes(e.target.files[0]);
  }
});

document.getElementById('paperSearch').addEventListener('input', renderPapers);
document.getElementById('statusFilter').addEventListener('change', renderPapers);
document.getElementById('hasNotesFilter').addEventListener('change', renderPapers);

renderPapers();
updateProgressSummary();
</script>
