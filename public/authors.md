---
title: "Author Profiles"
---

Track research groups and individual contributors across the collection. Click on any author to see their papers and research areas.

<div class="authors-container">
<div class="authors-controls">
<input type="text" id="authorSearch" placeholder="Search authors..." class="author-search">
<select id="topicFilter" class="topic-filter">
<option value="">All Topics</option>
<option value="ai-agents">AI Agents</option>
<option value="llm-reasoning">LLM Reasoning</option>
<option value="rag-retrieval">RAG & Retrieval</option>
<option value="multi-modal">Multi-Modal</option>
</select>
</div>
  
<div id="authorCount" class="author-count"></div>
<div id="authorsList" class="authors-list"></div>
</div>

<style>
.authors-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.authors-controls {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.author-search {
  flex: 1;
  min-width: 200px;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.author-search:focus {
  outline: none;
  border-color: #4a90e2;
}

.topic-filter {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.author-count {
  color: #666;
  margin-bottom: 15px;
  font-size: 14px;
}

.authors-list {
  display: grid;
  gap: 15px;
}

.author-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}

.author-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-color: #4a90e2;
}

.author-card.expanded {
  border-color: #4a90e2;
  background: #f8fbff;
}

.author-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.author-name {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}

.author-stats {
  display: flex;
  gap: 15px;
  align-items: center;
}

.paper-badge {
  background: #4a90e2;
  color: white;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.author-topics {
  margin-top: 8px;
}

.topic-tag {
  display: inline-block;
  padding: 3px 8px;
  background: #e8f4f8;
  color: #2c5aa0;
  border-radius: 4px;
  font-size: 11px;
  margin-right: 4px;
  margin-top: 4px;
}

.author-papers {
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #e0e0e0;
  display: none;
}

.author-card.expanded .author-papers {
  display: block;
}

.paper-entry {
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}

.paper-entry:last-child {
  border-bottom: none;
}

.paper-entry a {
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
}

.paper-entry a:hover {
  color: #4a90e2;
}

.paper-date {
  color: #999;
  font-size: 12px;
  margin-left: 8px;
}

.expand-icon {
  color: #999;
  font-size: 14px;
  transition: transform 0.2s;
}

.author-card.expanded .expand-icon {
  transform: rotate(90deg);
}
</style>

<script>
const authorsData = [
  {
    "name": "M",
    "paper_count": 8,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      },
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Y",
    "paper_count": 8,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "S",
    "paper_count": 6,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      },
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "T",
    "paper_count": 5,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      },
      {
        "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
        "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      },
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "J",
    "paper_count": 4,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "W",
    "paper_count": 4,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Z",
    "paper_count": 4,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Liu",
    "paper_count": 4,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "H",
    "paper_count": 4,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wang",
    "paper_count": 4,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "A",
    "paper_count": 3,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      },
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "D",
    "paper_count": 3,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Li",
    "paper_count": 3,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "P",
    "paper_count": 3,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      },
      {
        "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
        "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "R",
    "paper_count": 3,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "C",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Lin",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "B",
    "paper_count": 2,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "L",
    "paper_count": 2,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      },
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Roy",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      },
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Goswami",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Anna Hasenfratz",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Renormalization-guided cascade upscaling for lattice field generation",
        "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
        "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ethan T. Neil",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Renormalization-guided cascade upscaling for lattice field generation",
        "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
        "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Letizia Parato",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Renormalization-guided cascade upscaling for lattice field generation",
        "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
        "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Noah Schwartz",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Renormalization-guided cascade upscaling for lattice field generation",
        "url": "papers/2026-08-28/2608.28581v1-Renormalization-guided-cascade-upscaling-for-lattice-field-generation.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "Renormalization-guided inverse blocking for lattice field generation: construction and validation",
        "url": "papers/2026-08-28/2608.28580v1-Renormalization-guided-inverse-blocking-for-lattice-field-generation-constructio.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Seganrasan Subramanian",
    "paper_count": 2,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
        "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      },
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yulong Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Li Wang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wei Du",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Peilin Li",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yuqin Dai Zhiyuan Zhao",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Lingyong Fang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ziniu Liu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ru Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Huijia Zhu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Gongshen Liu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
        "url": "papers/2025-10-03/2510.02816v1-NCV-A-Node-Wise-Consistency-Verification-Approach-for-Low-Cost-Structured-Error-.html",
        "date": "2025-10-03",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "V\u00edctor Gallego",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
        "url": "papers/2026-05-28/2605.30003v1-Discovering-Cooperative-Pipelines-Autoresearch-for-Sequential-Social-Dilemmas.html",
        "date": "2026-05-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yujuan Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Linyin Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Shijie Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xu Yuan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yunshan Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yi Bin",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Wenqi Fan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Qing Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Meenu Ravi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Shailik Sarkar",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Lulwah AlKulaib",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yordanos Tessema",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Chang-Tien Lu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yuhan Meng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Shaofei Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jionghao Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jiandong Jin",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Puyi Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hanlin Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Anis Yusof",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Peng Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhenkai Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yao Guo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ding Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Nolasque",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Grey",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Pham",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Vani",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Thinking Costs Tokens: When More Structure is Worth the Price",
        "url": "papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Dore",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Damo",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "G",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Cabrio",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "E",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Villata",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis",
        "url": "papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Millstone",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Akidau",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Br%C3%BCderl",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pekker",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "If Agents Were Angels, No Governance Would Be Necessary: Out-of-Band Policy Enforcement at a Trusted Tool Boundary",
        "url": "papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "He",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Cui",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery with Unknown Spatial Coefficient Fields",
        "url": "papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Song",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Xue",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "de Rijke",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Salim",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "F D",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark",
        "url": "papers/2026-08-31/2608.27840-An-Empirical-Evaluation-of-Cross-City-POI-Recommen.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Han",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Qian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Ghawate",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
        "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Patil",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence",
        "url": "papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Du",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhao",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Kong",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Qu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wei",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Q",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "The Illusion of $\\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs",
        "url": "papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Cheng",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Chen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing",
        "url": "papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Liao",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Shi",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "F",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yu",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense",
        "url": "papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Pekhale",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "S M",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sarkar",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chakraborty",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tejas",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "J M",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "U B",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dhar",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SETU: An Agentic Ecosystem for Multilingual, Persona-Aware Communication Coaching",
        "url": "papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Singh",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "V",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Doshi",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Narsimhan",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ghosh",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Luna",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "K",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator",
        "url": "papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Gu",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "N",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ai",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Fu",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning",
        "url": "papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Birla",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Savagaonkar",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Visnu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Rasipuram",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Sengupta",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning",
        "url": "papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Chuangtao Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
        "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html",
        "date": "2026-07-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Arijit Khan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
        "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html",
        "date": "2026-07-24",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Andrew Borthwick",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
        "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html",
        "date": "2026-01-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Stephen Ash",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
        "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html",
        "date": "2026-01-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ruocheng Guo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kaiwen Dong",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xiang Gao",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kamalika Das",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jennifer S. Balakrishnan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Rational torsion on simple genus two Jacobians",
        "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Filip Najman",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Rational torsion on simple genus two Jacobians",
        "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ari Shnidman",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Rational torsion on simple genus two Jacobians",
        "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Andrew V. Sutherland",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Rational torsion on simple genus two Jacobians",
        "url": "papers/2026-08-28/2608.28543v1-Rational-torsion-on-simple-genus-two-Jacobians.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Marin Maletic",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
        "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Goran Vasiljevic",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Training-free Suction Grasp Detection for Deformed Aseptic Cartons Using Vision-Language Models and Geometric Surface Scoring",
        "url": "papers/2026-08-28/2608.28246v1-Training-free-Suction-Grasp-Detection-for-Deformed-Aseptic-Cartons-Using-Vision-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Olivier Dietrich",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
        "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Krishna Sapkota",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
        "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Konrad Schindler",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
        "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Genady Beryozkin",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction",
        "url": "papers/2026-08-28/2608.28567v1-GeBDA-Building-Damage-Assessment-as-Text-Based-Sequence-Prediction.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ding Gu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
        "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhanpeng Fu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
        "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yu-Min Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
        "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhong Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "How Long-Range Tails Reshape Non-Hermitian Spectra",
        "url": "papers/2026-08-28/2608.28577v1-How-Long-Range-Tails-Reshape-Non-Hermitian-Spectra.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ali Arslan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Bounds for inertialess dynamo",
        "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hezekiah Grayer",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Bounds for inertialess dynamo",
        "url": "papers/2026-08-28/2608.28584v1-Bounds-for-inertialess-dynamo.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hai-Lan Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Weitang Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Luca Moreschini",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jonathan Denlinger",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhigang Shuai",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Claudia Ojeda-Aristizabal",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Alessandra Lanzara",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Layer-Controlled Intermolecular Coupling and Many-Body Effects in C$_{60}$ Films",
        "url": "papers/2026-08-28/2608.28583v1-Layer-Controlled-Intermolecular-Coupling-and-Many-Body-Effects-in-C_60-Films.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hanzhang Jia",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Logos: An Agent Harness on a Cross-Process Bus",
        "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Liheng Zeng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Logos: An Agent Harness on a Cross-Process Bus",
        "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hao Cheng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Logos: An Agent Harness on a Cross-Process Bus",
        "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yi Gao",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Logos: An Agent Harness on a Cross-Process Bus",
        "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Bo Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Logos: An Agent Harness on a Cross-Process Bus",
        "url": "papers/2026-08-28/2608.28553v1-Logos-An-Agent-Harness-on-a-Cross-Process-Bus.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Andreas Nygaard",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Fast and efficient nested sampling with BEST",
        "url": "papers/2026-08-28/2608.28514v1-Fast-and-efficient-nested-sampling-with-BEST.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Javier Aguilar Mart\u00edn",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models",
        "url": "papers/2026-08-28/2608.28541v1-An-Enclosed-Mode-Is-a-Gauge-Choice-Topology-Relative-to-Reach-in-Certified-Code-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xinyi Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
        "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yutong Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
        "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Peijie Sun",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework",
        "url": "papers/2026-08-28/2608.28503v1-SG-UMP-Sequence-Guided-Universal-Multimodal-Prioritization-Calculation-Framework.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Lukas M\u00fcller",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
        "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Lukas Woike",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Modular Functors with Singularities from Vertex Operator Algebras Beyond Rigidity and Finiteness",
        "url": "papers/2026-08-28/2608.28579v1-Modular-Functors-with-Singularities-from-Vertex-Operator-Algebras-Beyond-Rigidit.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Keito Sasagawa",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
        "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shuhei Kurita",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
        "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Daisuke Kawahara",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images",
        "url": "papers/2026-08-28/2608.28248v1-Synth-JDoc-Synthesizing-a-Japanese-Document-Image-Dataset-for-OCR-with-Diverse-L.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Benjamin Constable",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Anup Roy",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vishal Sharma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Rishabh Upadhyay",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Robin Mills",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Aidan Millar",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG",
        "url": "papers/2026-08-28/2608.28572v1-PULSAR-Pooled-Unified-Late-Interaction-Search-and-Retrieval-for-Enterprise-Visua.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Akshay Pal",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
        "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Andrew Lucas",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
        "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Umang Mehta",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interaction corrections to topological density three-point functions in two-dimensional Fermi liquids: a coadjoint orbit perspective",
        "url": "papers/2026-08-28/2608.28588v1-Interaction-corrections-to-topological-density-three-point-functions-in-two-dime.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yuansi Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
        "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yunbum Kook",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "On two proofs of $d^2$ mixing of weighted Dikin walks",
        "url": "papers/2026-08-28/2608.28566v1-On-two-proofs-of-d2-mixing-of-weighted-Dikin-walks.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Chengpiao Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
        "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kaizheng Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Learning a Size-Weight Frontier for Synthetic-Augmented Inference",
        "url": "papers/2026-08-28/2608.28576v1-Learning-a-Size-Weight-Frontier-for-Synthetic-Augmented-Inference.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dominik Storck",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
        "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Tobias Eisenreich",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
        "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Stefan Wagner",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Recovering Software Architecture Intent from Historical Work Items using Generative AI: A Mixed-Methods Industry Case Study",
        "url": "papers/2026-08-28/2608.28403v1-Recovering-Software-Architecture-Intent-from-Historical-Work-Items-using-Generat.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Adil Alshammari",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
        "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hayretdin Bahsi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach",
        "url": "papers/2026-08-28/2608.28542v1-Offline-Verifiable-Accountability-for-Cross-Organization-Agent-Messaging-A-Prese.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kishor Datta Gupta",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
        "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ahmed Rafi Hasan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
        "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Md. Mahfuzur Rahman",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
        "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Md. Sadman Haque",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
        "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mohd Ariful Haque",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes",
        "url": "papers/2026-08-28/2608.28216v1-WALDO-One-Shot-Exemplar-Conditioned-Object-Detection-in-Cluttered-Scenes.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Aaryan Ajay Sharma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
        "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Sai Nishanth Padala",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging",
        "url": "papers/2026-08-28/2608.28547v1-DARTS-Decoder-Aware-Representation-Tuning-via-Surgery-for-Model-Merging.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Nan Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mohit Yadav",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jonathan Wulff",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Aidan Rosenbaum",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kezhou Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yuvan Sharma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xu Dong",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yiwei Tao",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning",
        "url": "papers/2026-08-28/2608.28578v1-Aero-Hand-Open-A-Simulation-Ready-Tendon-Driven-Hand-for-Dexterous-Manipulation-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Faraz Faruqi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ahmed Katary",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Demircan Tas",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Theresa Hradilak",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ning Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jiaji Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Fabian Manhardt",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Martin Nisser",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vrushank Phadnis",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ruofei Du",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Federico Tombari",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Megan Hofmann",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Stefanie Mueller",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "InstructMesh: Selective Refinement of Generative 3D Models for Fabrication",
        "url": "papers/2026-08-28/2608.28534v1-InstructMesh-Selective-Refinement-of-Generative-3D-Models-for-Fabrication.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Farah Atif",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sougata Saha",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Monojit Choudhury",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Seungyeon Kim",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
        "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "No\u00e9mie Jaquier",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos",
        "url": "papers/2026-08-28/2608.28570v1-ChainSplat-A-Physics-Inspired-Screw-Theoretic-Model-for-Learning-Deformable-Line.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vaibhav Mehandiratta",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
        "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Saket Ramchandra",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs",
        "url": "papers/2026-08-28/2608.28589v1-QGPINNs-A-Physics-Informed-Neural-Network-Framework-for-Nonlocal-Differential-Eq.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jiazhao Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hao Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Shuaihang Yuan",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Congcong Wen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Geeta Chandra Raju Bethala",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Giles Hamilton-Fletcher",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yu Hao",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "John-Ross Rizzo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mengyu Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Anthony Tzes",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yi Fang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance",
        "url": "papers/2026-08-28/2608.28218v1-Focus-Where-It-Counts-A-Salience-Driven-Vision-Language-Model-for-Low-Vision-Ass.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ryan van Mastrigt",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Machine learned designs of functional colloidal foldamers",
        "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zorana Zeravcic",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Machine learned designs of functional colloidal foldamers",
        "url": "papers/2026-08-28/2608.28554v1-Machine-learned-designs-of-functional-colloidal-foldamers.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Viet-Hoang Tran",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
        "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Tan M. Nguyen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "The Erd\u0151s-Hajnal Property for the six-vertex Graph with Edge Set $\\{ab,bc,cd,de,af,bf,df\\}$",
        "url": "papers/2026-08-28/2608.28551v1-The-Erd\u0151s-Hajnal-Property-for-the-six-vertex-Graph-with-Edge-Set-abbccddeafbfdf.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yupeng Zhang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Liuyuan Jiang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hongyi Huang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Bingheng Li",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lisha Chen",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Haosen Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Video Generative Models as Geometry Learner",
        "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jifei Song",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Video Generative Models as Geometry Learner",
        "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhensong Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Video Generative Models as Geometry Learner",
        "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xiatian Zhu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Video Generative Models as Geometry Learner",
        "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jiankang Deng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Video Generative Models as Geometry Learner",
        "url": "papers/2026-08-28/2608.28549v1-Video-Generative-Models-as-Geometry-Learner.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pietro Tiberi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
        "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Gabriele Marcelli",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
        "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vitangelo Lasorella",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM",
        "url": "papers/2026-08-28/2608.28529v1-Relaxed-Sender-Anonymity-for-CBDC-Interbank-Settlement-A-Zero-Knowledge-Approach.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Akito Hattori",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval",
        "url": "papers/2026-08-28/2608.27809v1-LINE-Conversation-History-Retrieval-for-Personal-Memory-RAG-Evaluating-Search-Re.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Le Xia",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
        "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Rose Qingyang Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
        "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Paul S. Kudyba",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
        "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhenlin An",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
        "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Haijian Sun",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN",
        "url": "papers/2026-08-28/2608.28532v1-xTRUCE-A-Provably-Safe-Arbiter-for-Multi-xApp-Conflict-Mitigation-in-Agentic-O-R.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Piotr Sierant",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Exact quantification of nonlocal magic",
        "url": "papers/2026-08-28/2608.28563v1-Exact-quantification-of-nonlocal-magic.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Chenhong He",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lei Li",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shicheng Li",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hanglong Lv",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lingpeng Kong",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qi Liu",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tong Yang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shuhuai Ren",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ehsan Abedi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
        "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zhenhao Li",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
        "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Timo Schultz",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Continuity equation on metric spaces via measure-valued derivations and BV-Wasserstein curves",
        "url": "papers/2026-08-28/2608.28586v1-Continuity-equation-on-metric-spaces-via-measure-valued-derivations-and-BV-Wasse.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jaewon Jung",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Haizhong Zheng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Hongsun Jang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jaeyong Song",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Beidi Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jinho Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents",
        "url": "papers/2026-08-28/2608.28389v1-CamoDocs-A-Poisoning-Attack-Against-Retrieval-Augmented-Language-Models-Using-Ca.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Shivam Mishra",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
        "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dhannu Ram Meena",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
        "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Muneendra Ojha",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
        "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Krishna Pratap Singh",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
        "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kuldeep Singh",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span> and Vocabulary-Constrained Filtering for Ontology Learning",
        "url": "papers/2026-08-27/2608.27101v1-pro-team-at-LLMs4OL-2026-Tasks-Flagship-and-Reuse-Retrieval-Augmented-Generation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Maxime Bouthors",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Josep Crego",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Fran\u00e7ois Yvon",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Maciej Besta",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Leonard Schmidt",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Lara Nonino",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Robert Gerstenberger",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pierre Pang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Patrik Okanovic",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ales Kubicek",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Tiancheng Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Baraq Lipshitz",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Torsten Hoefler",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Syed Mahbubul Huq",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
        "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Christopher Child",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
        "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Tillman Weyde",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
        "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pranava Madhyastha",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Knowing Before Answering: Decoding Language Models for Reliable RAG",
        "url": "papers/2026-08-27/2608.27661v1-Knowing-Before-Answering-Decoding-Language-Models-for-Reliable-RAG.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Guechaoui",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Diaa Zellagui",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Souleyman Chaib",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Sahraoui Dhelim",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yassir Lairgi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ludovic Moncla",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Khalid Benabdeslem",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "R\u00e9my Cazabet",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pierre Cl\u00e9au",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Corey D. C. Heath",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space",
        "url": "papers/2026-08-27/2608.27121v1-How-AI-Experiences-Art-Emergent-Aesthetic-Structure-in-a-Self-Supervised-Multimo.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Haowen Gu",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Gensheng Pei",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Junzhu Mao",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qiong Wang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mingwu Ren",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yazhou Yao",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Abhigya Verma",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Amit Kumar Saha",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Sai Harshitha Aluru",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Eduardo Almeida Palmieri",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Chahine Ghanem",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dipo Dunsin",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Zubair Baig",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ed de Quincey",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kim-Kwang Raymond Choo",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Xu Mingze",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
        "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html",
        "date": "2026-04-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Huanxi Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Kun Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jiaqi Liao",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Qiang Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Pengfei Qian",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "YuanZhao Zhai",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dawei Feng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Bo Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Huaimin Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Masahiro Kato",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
        "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html",
        "date": "2026-06-18",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Siddhant Saxena",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
        "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html",
        "date": "2026-05-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Nilesh Trivedi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
        "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html",
        "date": "2026-05-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vinayaka Jyothi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies",
        "url": "papers/2026-05-06/2605.04637v1-SWE-WebDevBench-Evaluating-Coding-Agent-Application-Platforms-as-Virtual-Softwar.html",
        "date": "2026-05-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Marianne Menglin Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Daniel Garcia",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Fjona Parllaku",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vikas Upadhyay",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Syed Fahad Allam Shah",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Dan Roth",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  }
];

function renderAuthors() {
  const searchTerm = document.getElementById('authorSearch').value.toLowerCase();
  const topicFilter = document.getElementById('topicFilter').value;
  
  let filtered = authorsData.filter(author => {
    const matchesSearch = !searchTerm || author.name.toLowerCase().includes(searchTerm);
    const matchesTopic = !topicFilter || author.topics.includes(topicFilter);
    return matchesSearch && matchesTopic;
  });
  
  document.getElementById('authorCount').textContent = 
     PH0 ;
  
  const container = document.getElementById('authorsList');
  
  if (filtered.length === 0) {
    container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">No authors found.</p>';
    return;
  }
  
  container.innerHTML = filtered.map(author =>  PH1 <span class="topic-tag">${t}</span> PH2 
<div class="paper-entry">
<a href="${p.url}">${p.title}</a>
<span class="paper-date">${p.date}</span>
</div>
         PH3 ).join('');
}

document.getElementById('authorSearch').addEventListener('input', renderAuthors);
document.getElementById('topicFilter').addEventListener('change', renderAuthors);

renderAuthors();
</script>
