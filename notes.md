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
    "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
    "authors": "Zhi Qiu, Jiazheng Sun, Chenxiao Xia, Jun Zheng, Xin Peng",
    "date": "2026-01-21",
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2601.14790v1",
    "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html"
  },
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
    "title": "SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows",
    "authors": "Amine El Hattami, Nicolas Chapados, Christopher Pal",
    "date": "2026-06-06",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2606.08049v1",
    "url": "papers/2026-06-06/2606.08049v1-SKILLnb-Selective-Formalization-and-Gated-Execution-for-Durable-Agent-Workflows.html"
  },
  {
    "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
    "authors": "V\u00edctor Gallego",
    "date": "2026-05-28",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2605.30003v1",
    "url": "papers/2026-05-28/2605.30003v1-Discovering-Cooperative-Pipelines-Autoresearch-for-Sequential-Social-Dilemmas.html"
  },
  {
    "title": "KG-RAG: Bridging the Gap Between Knowledge and Creativity",
    "authors": "Diego Sanmartin",
    "date": "2024-05-20",
    "topics": [
      "rag-retrieval",
      "llm-reasoning",
      "ai-agents"
    ],
    "arxiv_id": "2405.12035v1",
    "url": "papers/2024-05-20/2405.12035v1-KG-RAG-Bridging-the-Gap-Between-Knowledge-and-Creativity.html"
  },
  {
    "title": "Interactive Training: Feedback-Driven Neural Network Optimization",
    "authors": "Wentao Zhang, Yang Young Lu, Yuntian Deng",
    "date": "2025-10-02",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2510.02297v1",
    "url": "papers/2025-10-02/2510.02297v1-Interactive-Training-Feedback-Driven-Neural-Network-Optimization.html"
  },
  {
    "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
    "authors": "Oliver Bensch, Leonie Bensch, Tommy Nilsson, Florian Saling, Wafa M. Sadri, Carsten Hartmann, Tobias Hecking, J. Nathan Kutz",
    "date": "2024-10-21",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2410.16397v1",
    "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html"
  },
  {
    "title": "Scalable and Reliable Evaluation of AI Knowledge Retrieval Systems: RIKER and the Coherent Simulated Universe",
    "authors": "JV Roig",
    "date": "2025-12-22",
    "topics": [
      "rag-retrieval",
      "multi-modal",
      "llm-reasoning"
    ],
    "arxiv_id": "2601.08847v2",
    "url": "papers/2025-12-22/2601.08847v2-Scalable-and-Reliable-Evaluation-of-AI-Knowledge-Retrieval-Systems-RIKER-and-the.html"
  },
  {
    "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
    "authors": "Chengyang Gu, Le Zhang, Jingbo Zhou, Yize Chen, Yu Shi, Siqi Bao, Zheng-Fan Wu, Hua Wu, Hui Xiong",
    "date": "2026-08-22",
    "topics": [
      "ai-agents.gui",
      "ai-agents",
      "multi-modal",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.21830v1",
    "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html"
  },
  {
    "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
    "authors": "Weihang Pan, Zhengxu Yu, Yuxiang Zhang, Wenzhi Li, Zhongming Jin, Binbin Lin, Xiaofei He, Jieping Ye",
    "date": "2026-08-22",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.21860v1",
    "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html"
  },
  {
    "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
    "authors": "Wentao Yang, Zhenye Xu, Ruoyi Li, Musen Zhang, Yao Guo",
    "date": "2026-08-25",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2608.24555v1",
    "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html"
  },
  {
    "title": "Evaluating Language Models on Cross-Language Code Functional Equivalence",
    "authors": "Hui Sun, Anderson Uch\u00f4a, Rohit Gheyi, Wesley K. G. Assun\u00e7\u00e3o",
    "date": "2026-08-25",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.23961v1",
    "url": "papers/2026-08-25/2608.23961v1-Evaluating-Language-Models-on-Cross-Language-Code-Functional-Equivalence.html"
  },
  {
    "title": "Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings",
    "authors": "Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng, Seung Ki Moon",
    "date": "2026-08-25",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.24039v1",
    "url": "papers/2026-08-25/2608.24039v1-Design-to-Plan-A-Large-Language-Model-Based-Multi-Agent-Framework-for-Manufactur.html"
  },
  {
    "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
    "authors": "CheolWon Na, Hao Ni, Lukasz Szpruch, Zhangyang Wang, Dhagash Mehta, Saurabh Nagrecha, Alejandro Lopez-Lira, Chanyeol Choi, Yongjae Lee, Jee-Hyong Lee",
    "date": "2026-08-25",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.24069v1",
    "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html"
  },
  {
    "title": "Reflection with Action-Induced Visual Differences for Desktop GUI Agents",
    "authors": "Yijie Ma, Chaoyue Niu, Fan Wu, Guihai Chen",
    "date": "2026-08-25",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.24015v1",
    "url": "papers/2026-08-25/2608.24015v1-Reflection-with-Action-Induced-Visual-Differences-for-Desktop-GUI-Agents.html"
  },
  {
    "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
    "authors": "Tao Xiong, Xavier Hu, Wenkai Wang, Qinzhuo Wu, Changqiao Wu, Pengzhi Gao, Wei Liu, Jian Luan, Shengyu Zhang",
    "date": "2026-08-25",
    "topics": [
      "ai-agents.gui",
      "ai-agents",
      "rag-retrieval",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.24174v1",
    "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html"
  },
  {
    "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
    "authors": "Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, Lin Fu, Hong Zhou",
    "date": "2026-08-25",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.24099v1",
    "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html"
  },
  {
    "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
    "authors": "Abhilash Nandy, Rahul Seetharaman, Aman Bansal, Rounak Saha, Manav Nitin Kapadnis, Millon Madhur Das, Pawan Goyal, Niloy Ganguly",
    "date": "2026-08-24",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.23172v2",
    "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html"
  },
  {
    "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
    "authors": "Yi Zhu, Xiongwei Wu, Qiyi Wang, Tingyu Qu, Jiajun Liu, Sihan Cao, Long Chen, Weigao Sun, Feida Zhu, Yiran Zhong, Steven Hoi",
    "date": "2026-08-24",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2608.23035v2",
    "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html"
  },
  {
    "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
    "authors": "Yujuan Ding, Linyin Luo, Shijie Wang, Xu Yuan, Yunshan Ma, Yi Bin, Wenqi Fan, Qing Li",
    "date": "2026-08-24",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "llm-reasoning",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.22688v1",
    "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html"
  },
  {
    "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
    "authors": "Long Zhang, Yuhan Chen, Chaoran Zhang, Wanxia Cao, Kun Huang, Pengzhi Gao, Wei Liu, Jian Luan, Chenliang Li, Lixin Zou",
    "date": "2026-08-24",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.22847v1",
    "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html"
  },
  {
    "title": "CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents",
    "authors": "Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng, Yuan Wang",
    "date": "2026-08-23",
    "topics": [
      "ai-agents.gui",
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.22577v2",
    "url": "papers/2026-08-23/2608.22577v2-CausalCache-Conditional-High-Fidelity-Restoration-for-Long-Horizon-GUI-Agents.html"
  },
  {
    "title": "Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching",
    "authors": "Murat Dura, Serkan \u00d6zt\u00fcrk, Selma Tekir",
    "date": "2026-08-23",
    "topics": [
      "llm-reasoning",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.22332v1",
    "url": "papers/2026-08-23/2608.22332v1-Mechanistic-Interpretability-of-Chain-of-Thought-Reasoning-via-Sequential-Activa.html"
  },
  {
    "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
    "authors": "Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib, Yordanos Tessema, Chang-Tien Lu",
    "date": "2026-08-23",
    "topics": [
      "rag-retrieval",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.22634v1",
    "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html"
  },
  {
    "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
    "authors": "Yuhan Meng, Shaofei Li, Jionghao Huang, Jiandong Jin, Puyi Wang, Hanlin Jiang, Anis Yusof, Peng Jiang, Zhenkai Liang, Yao Guo, Ding Li",
    "date": "2026-08-15",
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.15012v1",
    "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html"
  },
  {
    "title": "PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation",
    "authors": "Haokun Deng, Xunkai Li, Hongchao Qin, Rong-Hua Li",
    "date": "2026-08-30",
    "topics": [
      "rag-retrieval",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.29753v1",
    "url": "papers/2026-08-30/2608.29753v1-PAGE-RAG-Provenance-Aware-Graph-Evidence-Promotion-for-Fixed-Budget-Multi-hop-Re.html"
  },
  {
    "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
    "authors": "Guransh Singh, Vishwajeet Kumar, Arkadeep Acharya, Adnan Qidwai, Jaydeep Sen, Sachindra Joshi",
    "date": "2026-08-30",
    "topics": [
      "rag-retrieval",
      "multi-modal",
      "ai-agents"
    ],
    "arxiv_id": "2608.29953v1",
    "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html"
  },
  {
    "title": "AiFlow: Token-Native Reactive Orchestration with Bounded Backpressure for Streaming LLM Applications",
    "authors": "Qunhui Zhang",
    "date": "2026-08-01",
    "topics": [
      "llm-reasoning",
      "ai-agents",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.00558v1",
    "url": "papers/2026-08-01/2608.00558v1-AiFlow-Token-Native-Reactive-Orchestration-with-Bounded-Backpressure-for-Streami.html"
  },
  {
    "title": "When Agentic AI Meets Integrated Sensing and Communication",
    "authors": "Kai Li, Conggai Li, Sarah Ali Siddiqui, Syed Sohail Ahmed, Xin Yuan, Shenghong Li, Wei Ni",
    "date": "2026-08-06",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.05792v1",
    "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html"
  },
  {
    "title": "Safety Must Precede the Deployment of Open-Ended AI",
    "authors": "Ivaxi Sheth, Jan Wehner, Sahar Abdelnabi, Ruta Binkyte, Mario Fritz",
    "date": "2025-02-06",
    "topics": [
      "ai-agents"
    ],
    "arxiv_id": "2502.04512v4",
    "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html"
  },
  {
    "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
    "authors": "Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang",
    "date": "2026-07-22",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "rag-retrieval",
      "ai-agents.gui"
    ],
    "arxiv_id": "2607.19985v1",
    "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html"
  },
  {
    "title": "BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs",
    "authors": "Debarpan Bhattacharya, Malay Phadke, Sriram Ganapathy",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.30646v1",
    "url": "papers/2026-08-31/2608.30646v1-BiG-SURE---Bipartite-Graph-for-Semantic-Uncertainty-and-Reliability-Estimation-o.html"
  },
  {
    "title": "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving",
    "authors": "Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2608.30672v1",
    "url": "papers/2026-08-31/2608.30672v1-HiRS-Agent-A-Hierarchical-Multi-Agent-System-for-Reliable-Long-Horizon-Remote-Se.html"
  },
  {
    "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
    "authors": "Qi Li, Zhaojie Kang, Yingjie He, Zheng Lin, Hao Zhang, Guangxin Wu, Yan Gong, Rong Fu, Jianyuan Ni",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.30498v1",
    "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html"
  },
  {
    "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
    "authors": "Shaoan Wang, Aocheng Luo, Fei Huang, Jingyi Xu, Xiaoyang Wang, Yueyu Wang, Qianli Ma, Fan Yang, Ran Mei, Jia Wei, Jiangpeng Hu, Xuhao Liu, Hongming Chen, Yuanbin Shao, Yiyang Lin, Ziliang Li, Liang Pan, Xinhang Liu, Yuntao Ma, Tingxiang Fan",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents",
      "multi-modal"
    ],
    "arxiv_id": "2608.30935v1",
    "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html"
  },
  {
    "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
    "authors": "Atta Ul Asad, Ahsan Bilal, Muhammad Ali, Muhammad Haseeb, Dean F. Hougen",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.30996v1",
    "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html"
  },
  {
    "title": "VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs",
    "authors": "Afsaneh Hasanebrahimi, Hanxun Huang, Christopher Leckie, Sarah Erfani",
    "date": "2026-08-31",
    "topics": [
      "multi-modal",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.30480v1",
    "url": "papers/2026-08-31/2608.30480v1-VisER-Visual-Evidence-and-Reliance-for-Object-Hallucination-Detection-in-LVLMs.html"
  },
  {
    "title": "LOCI: A Locator-Critic with Refinement Loop",
    "authors": "Walid Bousselham, Mathilde Caron, Arsha Nagrani, Cordelia Schmid",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.30959v1",
    "url": "papers/2026-08-31/2608.30959v1-LOCI-A-Locator-Critic-with-Refinement-Loop.html"
  },
  {
    "title": "InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings",
    "authors": "Mohammad Abolnejadian, Matthew Brehmer",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.31115v1",
    "url": "papers/2026-08-31/2608.31115v1-InsightToast-Proactive-Information-Retrieval-Glanceable-Visualization-in-the-Sid.html"
  },
  {
    "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
    "authors": "Hamed Babaei Giglou, S\u00f6ren Auer, Peio Popov, Mahsa Sanaei, Jennifer D'Souza",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.31137v1",
    "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html"
  },
  {
    "title": "When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning",
    "authors": "Hamed Babaei Giglou, S\u00f6ren Auer, Jennifer D'Souza",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.31118v1",
    "url": "papers/2026-08-31/2608.31118v1-When-Does-Bigger-Help-A-Controlled-Study-of-LLM-Scale-for-Ontology-Learning.html"
  },
  {
    "title": "VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs",
    "authors": "Jingyi He, Sanghwan Kim, Zeynep Akata",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.30705v1",
    "url": "papers/2026-08-31/2608.30705v1-VisLens-Single-Pass-Interpretable-Visual-Search-for-Multimodal-LLMs.html"
  },
  {
    "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
    "authors": "Mathias Zinnen, Alisha Mund, Sabine Lang, Lukas H\u00fcttner, Thomas Gorges, Vincent Christlein",
    "date": "2026-08-31",
    "topics": [
      "multi-modal"
    ],
    "arxiv_id": "2608.30510v1",
    "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html"
  },
  {
    "title": "GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns",
    "authors": "Yinwen Lu, Weihao Luo, Yueqi Zhong",
    "date": "2026-08-31",
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.30550v1",
    "url": "papers/2026-08-31/2608.30550v1-GarmentWeaver-Schema-Aware-Structured-Synthesis-for-Multimodal-Sewing-Patterns.html"
  },
  {
    "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
    "authors": "Tiffanie Godelaine, Maxime Zanella, Karim El Khoury, Benoit Macq, Christophe De Vleeschouwer",
    "date": "2026-08-31",
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.30420v1",
    "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html"
  },
  {
    "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
    "authors": "Zixing Lei, Gengze Zhou, Xiong-Hui Chen, Jiazhao Zhang, Yiyang Huang, Hang Yin, Haoqi Yuan, Qi Wu, Weixin Li, Siheng Chen",
    "date": "2026-08-31",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.multi-agent",
      "multi-modal"
    ],
    "arxiv_id": "2608.30396v1",
    "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html"
  },
  {
    "title": "Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification",
    "authors": "Van-Giang Nguyen, Thanh-Tuan Tran, Xuan-Hieu Phan, Xiem HoangVan",
    "date": "2026-08-31",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.30997v1",
    "url": "papers/2026-08-31/2608.30997v1-Multi-View-Reflective-Surface-Inspection-via-Semantic-Saliency-Cross-Verificatio.html"
  },
  {
    "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
    "authors": "Ruofan Hu, Shengyang Xu, Minjie Hong, Xiaoda Yang, Sashuai Zhou, Ke Lei, Tao Jin, Zhou Zhao",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval",
      "multi-modal",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.30163v1",
    "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html"
  },
  {
    "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
    "authors": "Marry Kong, Rina Buoy, Sovisal Chenda, Nguonly Taing, Masakazu Iwamura, Koichi Kise",
    "date": "2026-08-31",
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.30213v1",
    "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html"
  },
  {
    "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
    "authors": "Samir Abdaljalil, Hunzalah Hassan Bhatti, Ahlam Bashiti, Farina Amir, Md Arid Hasan, Basel Mousi, Nadir Durrani, Fahim Dalvi, Zien Sheikh Ali, Erchin Serpedin, Hasan Kurban, Mustafa Jarrar, Shammur Absar Chowdhury, Firoj Alam",
    "date": "2026-08-31",
    "topics": [
      "multi-modal",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.30475v1",
    "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html"
  },
  {
    "title": "Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation",
    "authors": "Riya Ahuja, Tim Kacprowski, Roya Shiasi Sardoabi",
    "date": "2026-08-31",
    "topics": [
      "rag-retrieval"
    ],
    "arxiv_id": "2608.31139v1",
    "url": "papers/2026-08-31/2608.31139v1-Configurable-Semantic-Chunking-for-Biomedical-Information-Extraction-in-Retrieva.html"
  },
  {
    "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
    "authors": "Chuangtao Ma, Arijit Khan",
    "date": "2026-07-24",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "llm-reasoning",
      "ai-agents.multi-agent",
      "multi-modal"
    ],
    "arxiv_id": "2607.22319v1",
    "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html"
  },
  {
    "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
    "authors": "Hankyul Baek, Jaewon Noh, Sang Seo, Yongsu Kim, Gabriel Waikin Loh Matienzo, Young Il Kim, Ee Wei Seah, Akriti Vij",
    "date": "2026-06-15",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2606.17114v1",
    "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html"
  },
  {
    "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
    "authors": "Andrew Borthwick, Stephen Ash",
    "date": "2026-01-03",
    "topics": [
      "ai-agents",
      "ai-agents.gui"
    ],
    "arxiv_id": "2601.01126v2",
    "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html"
  },
  {
    "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
    "authors": "Ruocheng Guo, Kaiwen Dong, Xiang Gao, Kamalika Das",
    "date": "2026-02-23",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2602.20426v2",
    "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html"
  },
  {
    "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
    "authors": "Jiaxi Li, Ke Deng, Yun Wang, Jingyuan Huang, Yucheng Shi, Qiaoyu Tan, Jin Lu, Ninghao Liu",
    "date": "2026-06-03",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "ai-agents.gui"
    ],
    "arxiv_id": "2606.04391v1",
    "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html"
  },
  {
    "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
    "authors": "Jihong Wang, Jiamu Zhou, Weiming Zhang, Teng Wang, Weiwen Liu, Zhuosheng Zhang, Xingyu Lou, Weinan Zhang, Huarong Deng, Jun Wang",
    "date": "2026-01-12",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval",
      "multi-modal"
    ],
    "arxiv_id": "2601.07262v3",
    "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html"
  },
  {
    "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
    "authors": "Xinyi Wu, Geng Hong, Yueyue Chen, MingXuan Liu, Feier Jin, Xudong Pan, Jiarun Dai, Baojun Liu",
    "date": "2026-01-12",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2601.07263v1",
    "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html"
  },
  {
    "title": "Hybrid Offline-Online Multi-Agent Decision Transformers for Wireless Resource Management",
    "authors": "Yiming Zhang, Kun Yang, Cong Shen, Dongning Guo",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.28878v1",
    "url": "papers/2026-08-28/2608.28878v1-Hybrid-Offline-Online-Multi-Agent-Decision-Transformers-for-Wireless-Resource-Ma.html"
  },
  {
    "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
    "authors": "Tejas Srinivasan, Shikib Mehri, Nandita Shankar Naik, Anirban Das, William M. Campbell, Jesse Thomason",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27818v1",
    "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html"
  },
  {
    "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
    "authors": "Xiaoqing Wang, Keman Huang, Bin Liang, Hongyu Li, Xiaoyong Du, Wuqiong Pan",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.28264v1",
    "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html"
  },
  {
    "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
    "authors": "Farah Atif, Sougata Saha, Monojit Choudhury",
    "date": "2026-08-28",
    "topics": [
      "llm-reasoning",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2608.28144v1",
    "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html"
  },
  {
    "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
    "authors": "Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.28399v1",
    "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html"
  },
  {
    "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
    "authors": "Xinyuan Gui, Shaowen Wang, Sheng Sun, Zijian Wang, Zishu Yu, Zheming Yang",
    "date": "2026-08-28",
    "topics": [
      "multi-modal",
      "llm-reasoning",
      "ai-agents.multi-agent",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.28726v1",
    "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html"
  },
  {
    "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
    "authors": "Sarang Manoj Pekhale, Amartya Roy, Rajat Sarkar, Souvik Chakraborty",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "multi-modal",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.27869v1",
    "url": "papers/2026-08-28/2608.27869v1-See-Hypothesize-Validate-Multimodal-Agentic-Framework-for-Discovering-Governing-.html"
  },
  {
    "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
    "authors": "Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren",
    "date": "2026-08-28",
    "topics": [
      "multi-modal",
      "llm-reasoning",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.28383v1",
    "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html"
  },
  {
    "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
    "authors": "openJiuwen Team, Tao Yu, Xinyu Zhang, Qianqian Chen, Xiaoneng Xiang, Chia Kwangyang, Xingchen Huang, Ran Chen, Yangkai Ding, Zheng Wang, Yeo Boon Hong, Bingzheng Gan, Enrui Hu, Shuo Cheng, Deyang Li, Ruifeng Shi, Hongbo Wang, Qi Ye, Xuefeng Jin, Zhangchun Zhao",
    "date": "2026-08-28",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2608.27969v1",
    "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html"
  },
  {
    "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
    "authors": "Zijie Meng, Xiwei Dai, Yixuan Tang, Jin Hao, Yang Feng, Fudong Zhu, Xiaoqiang Liu, Shaosheng Cao, Zuozhu Liu",
    "date": "2026-08-19",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "multi-modal",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.18878v1",
    "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html"
  },
  {
    "title": "LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents",
    "authors": "Weiming Li, Helen Paik, Yulei Sui",
    "date": "2026-08-26",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.25777v1",
    "url": "papers/2026-08-26/2608.25777v1-LocalLSTC-A-Long-Short-Term-Control-Architecture-for-Locally-Deployed-GUI-Agents.html"
  },
  {
    "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
    "authors": "Hongbo Liu, Peixian Chen, Sihan Liu, Peiyuan Zhang, Kai Zou, Dian Zheng, Xiaoxing Hu, Yuhao Dong, Mengdan Zhang, Yunhang Shen, Haoyu Cao, Wei Liu, Weibo Gu, Xing Sun, Shengjie Zhao",
    "date": "2026-08-26",
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "arxiv_id": "2608.25529v1",
    "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html"
  },
  {
    "title": "MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration",
    "authors": "Miseon Yu, Jaehoon Choi, Younghan Lee, Yunheung Paek",
    "date": "2026-08-26",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.25457v2",
    "url": "papers/2026-08-26/2608.25457v2-MACGen-Toward-Functionally-Correct-and-Secure-Code-Generation-via-Multi-Agent-Co.html"
  },
  {
    "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
    "authors": "Simeng Zhang, Yilong Chen, Wenyuan Zhang, Zhenyu Zhang, Yao Chen, Junyuan Shang, Tingwen Liu",
    "date": "2026-08-21",
    "topics": [
      "llm-reasoning"
    ],
    "arxiv_id": "2608.21265v2",
    "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html"
  },
  {
    "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
    "authors": "Luiz Giacomossi, Zafer Yigit, Marwan Shakarna, Shoaib Saleemi, Ivan Tomasic, Baran \u00c7ur\u00fckl\u00fc, H\u00e5kan Forsberg",
    "date": "2026-08-21",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2608.20906v1",
    "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html"
  },
  {
    "title": "SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning",
    "authors": "Yujie Zhang, Bin Gao, Tulika Mitra",
    "date": "2026-08-21",
    "topics": [
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.21614v1",
    "url": "papers/2026-08-21/2608.21614v1-SAEM-Stage-Aware-Expert-Management-for-Memory-Efficient-MoE-Inference-in-Chain-o.html"
  },
  {
    "title": "MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps",
    "authors": "Sujin Chen, Lijun Li, Tianyi Du, Jing Shao",
    "date": "2026-08-18",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.17659v1",
    "url": "papers/2026-08-18/2608.17659v1-MobileWorldSafety-Benchmarking-GUI-Agent-Safety-Against-Environmental-Injection-.html"
  },
  {
    "title": "Reasoning about In-Context Samples for Machine-Translation",
    "authors": "Maxime Bouthors, Josep Crego, Fran\u00e7ois Yvon",
    "date": "2026-08-27",
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27036v1",
    "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html"
  },
  {
    "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
    "authors": "Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler",
    "date": "2026-08-27",
    "topics": [
      "llm-reasoning",
      "ai-agents",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.27046v1",
    "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html"
  },
  {
    "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
    "authors": "Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim",
    "date": "2026-08-27",
    "topics": [
      "multi-modal",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.26921v1",
    "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html"
  },
  {
    "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
    "authors": "Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\u00e9my Cazabet, Pierre Cl\u00e9au",
    "date": "2026-08-27",
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.26870v1",
    "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html"
  },
  {
    "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
    "authors": "Ji Soo Lee, Jinyoung Park, Seohyun Lee, Jongha Kim, Joonmyung Choi, Jinsung Yoon, Hyunwoo J. Kim",
    "date": "2026-08-27",
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.26684v1",
    "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html"
  },
  {
    "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
    "authors": "Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao",
    "date": "2026-08-27",
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.26856v1",
    "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html"
  },
  {
    "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
    "authors": "Yu Han, Tianwen Qian",
    "date": "2026-08-27",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "arxiv_id": "2608.27508v1",
    "url": "papers/2026-08-27/2608.27508v1-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-World-Models-with-Reinforcement.html"
  },
  {
    "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
    "authors": "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru",
    "date": "2026-08-27",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.26623v1",
    "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html"
  },
  {
    "title": "Learning Simple Test-Time Environments for LLM Web Agents",
    "authors": "Junxuan Li, Zijun Liu, Ziyi Huang, Peng Li, Yuzhou Liu, Ming Yan, Yang Liu",
    "date": "2026-08-29",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.29305v1",
    "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html"
  },
  {
    "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
    "authors": "Jonan Richards, Kosei Horikawa, Youmei Fan, Yutaro Kashiwa, Mairieli Wessel",
    "date": "2026-08-29",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.29204v1",
    "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html"
  },
  {
    "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
    "authors": "Millicent Ochieng, Felermino D. M. A. Ali, Elizabeth A. Ankrah, Najeeb Gambo Abdulhamid, Migisha Boyd, Stephanie Nyairo, Mercy Muchai, Samuel Chege Maina, Aditya Vashistha, Anja Thieme, Jacki O'Neill",
    "date": "2026-08-29",
    "topics": [
      "multi-modal",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.29209v1",
    "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html"
  },
  {
    "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
    "authors": "Yuwei Lou, Hao Hu, Yuzhou Jiang, Zongfei Zhang, Liang Wang, Jincai Liu, Jidong Ge, Xianping Tao",
    "date": "2026-08-29",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval",
      "ai-agents.multi-agent",
      "ai-agents.gui"
    ],
    "arxiv_id": "2608.29263v1",
    "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html"
  },
  {
    "title": "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs",
    "authors": "Yian Wang, Agam Goyal, Eshwar Chandrasekharan, Hari Sundaram",
    "date": "2026-08-29",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.29028v1",
    "url": "papers/2026-08-29/2608.29028v1-Facts-Without-Rules-Boundary-Metadata-Collapse-in-Multi-Agent-LLM-Handoffs.html"
  },
  {
    "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
    "authors": "Zihan Ding, Longxu Dou, Qi Gao, Xiangwu Guo, Shengchao Hu, Zilong Huang, Zihang Jiang, Lei Ke, Mengcheng Lan, Weixian Lei, Hanxuan Li, Honglin Li, Xiyun Li, Zaitang Li, Leowei Liang, Xin Luo, Haozhe Ma, Jiayi Mao, Zhoujie Pan, Can Qin, Tianyuan Qu, Weiqi Wang, Wenkai Wang, Yonglin Wang, Yuxin Wang, Chenxu Wu, Yingchen Yu, Chenyu Zhang, Yuhao Zheng",
    "date": "2026-08-16",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2608.15930v1",
    "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html"
  },
  {
    "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
    "authors": "Ryan C. Barron, Maksim E. Eren, Olga M. Serafimova, Cynthia Matuszek, Boian S. Alexandrov",
    "date": "2025-02-27",
    "topics": [
      "rag-retrieval",
      "multi-modal",
      "ai-agents",
      "llm-reasoning"
    ],
    "arxiv_id": "2502.20364v2",
    "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html"
  },
  {
    "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
    "authors": "Eduardo Almeida Palmieri, Mohamed Chahine Ghanem, Dipo Dunsin, Zubair Baig, Ed de Quincey, Kim-Kwang Raymond Choo",
    "date": "2026-07-03",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval",
      "multi-modal"
    ],
    "arxiv_id": "2607.03233v1",
    "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html"
  },
  {
    "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
    "authors": "Xu Mingze",
    "date": "2026-04-06",
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "arxiv_id": "2604.04820v1",
    "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html"
  },
  {
    "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
    "authors": "Samira Abedini, Sina Mavali, Lea Sch\u00f6nherr, Martin Pawelczyk, Rebekka Burkholz",
    "date": "2026-03-16",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "ai-agents.multi-agent"
    ],
    "arxiv_id": "2603.15809v1",
    "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html"
  },
  {
    "title": "Agentic Compilation: Mitigating the LLM Rerun Crisis for Minimized-Inference-Cost Web Automation",
    "authors": "Jagadeesh Chundru",
    "date": "2026-04-08",
    "topics": [
      "llm-reasoning",
      "ai-agents",
      "ai-agents.gui"
    ],
    "arxiv_id": "2604.09718v2",
    "url": "papers/2026-04-08/2604.09718v2-Agentic-Compilation-Mitigating-the-LLM-Rerun-Crisis-for-Minimized-Inference-Cost.html"
  },
  {
    "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
    "authors": "Yinfang Chen, Manish Shetty, Gagan Somashekar, Minghua Ma, Yogesh Simmhan, Jonathan Mace, Chetan Bansal, Rujia Wang, Saravan Rajmohan",
    "date": "2025-01-12",
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "ai-agents.gui"
    ],
    "arxiv_id": "2501.06706v1",
    "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html"
  },
  {
    "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
    "authors": "Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang",
    "date": "2026-07-16",
    "topics": [
      "llm-reasoning",
      "ai-agents",
      "rag-retrieval"
    ],
    "arxiv_id": "2607.14642v1",
    "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html"
  },
  {
    "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
    "authors": "Shen You, Xiaoming Zhu, Weining Weng, Hefei Mei, Weixuan Wang, Zhongshen Li, Zeji LI, Ye-Wen Wang, Zijun Liao, Juchao Zhuo, Yang Wei, Fuhao Qiu, Siqin Li, Zhenjie Lian, Danei Gong, Junkai Ji, Xiangtao Li, Qiuzhen Lin, Liang Wang, Ka-Chun Wong",
    "date": "2026-08-03",
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "arxiv_id": "2608.01652v1",
    "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html"
  },
  {
    "title": "A Comprehensive Framework for Reliable Legal AI: Combining Specialized Expert Systems and Adaptive Refinement",
    "authors": "Sidra Nasir, Qamar Abbas, Samita Bai, Rizwan Ahmed Khan",
    "date": "2024-12-29",
    "topics": [
      "rag-retrieval",
      "ai-agents.gui",
      "multi-modal"
    ],
    "arxiv_id": "2412.20468v2",
    "url": "papers/2024-12-29/2412.20468v2-A-Comprehensive-Framework-for-Reliable-Legal-AI-Combining-Specialized-Expert-Sys.html"
  },
  {
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "authors": "Masahiro Kato",
    "date": "2026-06-18",
    "topics": [
      "rag-retrieval",
      "ai-agents",
      "llm-reasoning"
    ],
    "arxiv_id": "2606.20041v1",
    "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html"
  },
  {
    "title": "How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs",
    "authors": "Honjar Xing, Jefferson Lin, Henry Lieberman",
    "date": "2026-06-18",
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "arxiv_id": "2606.20978v1",
    "url": "papers/2026-06-18/2606.20978v1-How-Should-Agents-Read-Demonstrations-Hierarchical-Structure-Beats-Flat-Action-L.html"
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
      "ai-agents",
      "llm-reasoning",
      "ai-agents.gui"
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
    
    return `
      <div class="paper-card" data-arxiv-id="${paper.arxiv_id}">
        <div class="paper-header">
          <div class="paper-title">
            <a href="${paper.url}" target="_blank">${paper.title}</a>
            <div class="paper-meta">${paper.authors} • ${paper.date}</div>
            <div>
              ${paper.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
            </div>
          </div>
          <div class="status-selector">
            <button class="status-btn to-read ${status === 'to-read' ? 'active' : ''}" data-status="to-read">To Read</button>
            <button class="status-btn reading ${status === 'reading' ? 'active' : ''}" data-status="reading">Reading</button>
            <button class="status-btn read ${status === 'read' ? 'active' : ''}" data-status="read">Read</button>
          </div>
        </div>
        <div class="notes-section">
          <textarea class="notes-textarea" placeholder="Add your notes, thoughts, or key takeaways...">${noteText}</textarea>
          <div class="notes-saved">✓ Saved</div>
        </div>
      </div>
    `;
  }).join('');
  
  // Attach event listeners
  document.querySelectorAll('.status-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const card = this.closest('.paper-card');
      const arxivId = card.dataset.arxivId;
      const status = this.dataset.status;
      
      // Update UI
      card.querySelectorAll('.status-btn').forEach(b => b.classList.remove('active'));
      if (card.querySelector(`[data-status="${status}"]`).classList.contains('active')) {
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
  a.download = `paper-notes-${new Date().toISOString().split('T')[0]}.json`;
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
