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
    "name": "Wei Liu",
    "paper_count": 3,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yao Guo",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
        "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      },
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wenkai Wang",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Pengzhi Gao",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jian Luan",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      },
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hamed Babaei Giglou",
    "paper_count": 2,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
        "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      },
      {
        "title": "When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning",
        "url": "papers/2026-08-31/2608.31118v1-When-Does-Bigger-Help-A-Controlled-Study-of-LLM-Scale-for-Ontology-Learning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "S\u00f6ren Auer",
    "paper_count": 2,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
        "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      },
      {
        "title": "When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning",
        "url": "papers/2026-08-31/2608.31118v1-When-Does-Bigger-Help-A-Controlled-Study-of-LLM-Scale-for-Ontology-Learning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jennifer D'Souza",
    "paper_count": 2,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
        "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      },
      {
        "title": "When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning",
        "url": "papers/2026-08-31/2608.31118v1-When-Does-Bigger-Help-A-Controlled-Study-of-LLM-Scale-for-Ontology-Learning.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Liang Wang",
    "paper_count": 2,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      },
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhi Qiu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
        "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html",
        "date": "2026-01-21",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jiazheng Sun",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
        "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html",
        "date": "2026-01-21",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Chenxiao Xia",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
        "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html",
        "date": "2026-01-21",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jun Zheng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
        "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html",
        "date": "2026-01-21",
        "topics": [
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Xin Peng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CI4A: Semantic Component Interfaces for Agents Empowering Web Automation",
        "url": "papers/2026-01-21/2601.14790v1-CI4A-Semantic-Component-Interfaces-for-Agents-Empowering-Web-Automation.html",
        "date": "2026-01-21",
        "topics": [
          "ai-agents",
          "rag-retrieval"
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
    "name": "Amine El Hattami",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows",
        "url": "papers/2026-06-06/2606.08049v1-SKILLnb-Selective-Formalization-and-Gated-Execution-for-Durable-Agent-Workflows.html",
        "date": "2026-06-06",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Nicolas Chapados",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows",
        "url": "papers/2026-06-06/2606.08049v1-SKILLnb-Selective-Formalization-and-Gated-Execution-for-Durable-Agent-Workflows.html",
        "date": "2026-06-06",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Christopher Pal",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows",
        "url": "papers/2026-06-06/2606.08049v1-SKILLnb-Selective-Formalization-and-Gated-Execution-for-Durable-Agent-Workflows.html",
        "date": "2026-06-06",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "V\u00edctor Gallego",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas",
        "url": "papers/2026-05-28/2605.30003v1-Discovering-Cooperative-Pipelines-Autoresearch-for-Sequential-Social-Dilemmas.html",
        "date": "2026-05-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Diego Sanmartin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "KG-RAG: Bridging the Gap Between Knowledge and Creativity",
        "url": "papers/2024-05-20/2405.12035v1-KG-RAG-Bridging-the-Gap-Between-Knowledge-and-Creativity.html",
        "date": "2024-05-20",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Wentao Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interactive Training: Feedback-Driven Neural Network Optimization",
        "url": "papers/2025-10-02/2510.02297v1-Interactive-Training-Feedback-Driven-Neural-Network-Optimization.html",
        "date": "2025-10-02",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yang Young Lu",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interactive Training: Feedback-Driven Neural Network Optimization",
        "url": "papers/2025-10-02/2510.02297v1-Interactive-Training-Feedback-Driven-Neural-Network-Optimization.html",
        "date": "2025-10-02",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Yuntian Deng",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Interactive Training: Feedback-Driven Neural Network Optimization",
        "url": "papers/2025-10-02/2510.02297v1-Interactive-Training-Feedback-Driven-Neural-Network-Optimization.html",
        "date": "2025-10-02",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Oliver Bensch",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Leonie Bensch",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tommy Nilsson",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Florian Saling",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Wafa M. Sadri",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Carsten Hartmann",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tobias Hecking",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "J. Nathan Kutz",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Reliable Offline Personal AI Assistant for Long Duration Spaceflight",
        "url": "papers/2024-10-21/2410.16397v1-Towards-a-Reliable-Offline-Personal-AI-Assistant-for-Long-Duration-Spaceflight.html",
        "date": "2024-10-21",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "JV Roig",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Scalable and Reliable Evaluation of AI Knowledge Retrieval Systems: RIKER and the Coherent Simulated Universe",
        "url": "papers/2025-12-22/2601.08847v2-Scalable-and-Reliable-Evaluation-of-AI-Knowledge-Retrieval-Systems-RIKER-and-the.html",
        "date": "2025-12-22",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Chengyang Gu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Le Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jingbo Zhou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yize Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yu Shi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Siqi Bao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Zheng-Fan Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Hua Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Hui Xiong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents",
        "url": "papers/2026-08-22/2608.21830v1-Beyond-Success-and-Failure-Length-Aware-Contrastive-Learning-for-GUI-Agents.html",
        "date": "2026-08-22",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Weihang Pan",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhengxu Yu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yuxiang Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wenzhi Li",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhongming Jin",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Binbin Lin",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiaofei He",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jieping Ye",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning",
        "url": "papers/2026-08-22/2608.21860v1-ChainPrune-Evaluating-and-Reducing-Redundancy-in-Long-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-22",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wentao Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
        "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Zhenye Xu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
        "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Ruoyi Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
        "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Musen Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment",
        "url": "papers/2026-08-25/2608.24555v1-StrokeGuard-A-Multi-Agent-Guided-System-for-Prehospital-Stroke-Assessment.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Hui Sun",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Evaluating Language Models on Cross-Language Code Functional Equivalence",
        "url": "papers/2026-08-25/2608.23961v1-Evaluating-Language-Models-on-Cross-Language-Code-Functional-Equivalence.html",
        "date": "2026-08-25",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Anderson Uch\u00f4a",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Evaluating Language Models on Cross-Language Code Functional Equivalence",
        "url": "papers/2026-08-25/2608.23961v1-Evaluating-Language-Models-on-Cross-Language-Code-Functional-Equivalence.html",
        "date": "2026-08-25",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Rohit Gheyi",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Evaluating Language Models on Cross-Language Code Functional Equivalence",
        "url": "papers/2026-08-25/2608.23961v1-Evaluating-Language-Models-on-Cross-Language-Code-Functional-Equivalence.html",
        "date": "2026-08-25",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wesley K. G. Assun\u00e7\u00e3o",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Evaluating Language Models on Cross-Language Code Functional Equivalence",
        "url": "papers/2026-08-25/2608.23961v1-Evaluating-Language-Models-on-Cross-Language-Code-Functional-Equivalence.html",
        "date": "2026-08-25",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Muhammad Tayyab Khan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings",
        "url": "papers/2026-08-25/2608.24039v1-Design-to-Plan-A-Large-Language-Model-Based-Multi-Agent-Framework-for-Manufactur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Lequn Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings",
        "url": "papers/2026-08-25/2608.24039v1-Design-to-Plan-A-Large-Language-Model-Based-Multi-Agent-Framework-for-Manufactur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Wenhe Feng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings",
        "url": "papers/2026-08-25/2608.24039v1-Design-to-Plan-A-Large-Language-Model-Based-Multi-Agent-Framework-for-Manufactur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Seung Ki Moon",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings",
        "url": "papers/2026-08-25/2608.24039v1-Design-to-Plan-A-Large-Language-Model-Based-Multi-Agent-Framework-for-Manufactur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "CheolWon Na",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hao Ni",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lukasz Szpruch",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zhangyang Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Dhagash Mehta",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Saurabh Nagrecha",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Alejandro Lopez-Lira",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chanyeol Choi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yongjae Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jee-Hyong Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems",
        "url": "papers/2026-08-25/2608.24069v1-Poisoning-Agentic-Alpha-Adversarial-Vulnerabilities-Across-Roles-and-Architectur.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yijie Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reflection with Action-Induced Visual Differences for Desktop GUI Agents",
        "url": "papers/2026-08-25/2608.24015v1-Reflection-with-Action-Induced-Visual-Differences-for-Desktop-GUI-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Chaoyue Niu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reflection with Action-Induced Visual Differences for Desktop GUI Agents",
        "url": "papers/2026-08-25/2608.24015v1-Reflection-with-Action-Induced-Visual-Differences-for-Desktop-GUI-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Fan Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reflection with Action-Induced Visual Differences for Desktop GUI Agents",
        "url": "papers/2026-08-25/2608.24015v1-Reflection-with-Action-Induced-Visual-Differences-for-Desktop-GUI-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Guihai Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reflection with Action-Induced Visual Differences for Desktop GUI Agents",
        "url": "papers/2026-08-25/2608.24015v1-Reflection-with-Action-Induced-Visual-Differences-for-Desktop-GUI-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Tao Xiong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xavier Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qinzhuo Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Changqiao Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shengyu Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Task-Adaptive Rubrics for GUI Reward Modeling",
        "url": "papers/2026-08-25/2608.24174v1-Task-Adaptive-Rubrics-for-GUI-Reward-Modeling.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Guo Gan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yilun Zhao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Cong Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jinbiao Wei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Tingyu Song",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zheyuan Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Lin Fu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hong Zhou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments",
        "url": "papers/2026-08-25/2608.24099v1-Are-Android-GUI-Agents-Robust-Against-Runtime-Anomalies-AnTrap-Evaluating-Agents.html",
        "date": "2026-08-25",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Abhilash Nandy",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Rahul Seetharaman",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Aman Bansal",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Rounak Saha",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Manav Nitin Kapadnis",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Millon Madhur Das",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Pawan Goyal",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Niloy Ganguly",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension",
        "url": "papers/2026-08-24/2608.23172v2-CaRGo-T-Causal-Reasoning-Graph-of-Thought-improves-Multimodal-Humor-Comprehensio.html",
        "date": "2026-08-24",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yi Zhu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Xiongwei Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Qiyi Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Tingyu Qu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Jiajun Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Sihan Cao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Long Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Weigao Sun",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Feida Zhu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Yiran Zhong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Steven Hoi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks",
        "url": "papers/2026-08-24/2608.23035v2-MobilePA-Bench-Benchmarking-Mobile-Planner-Agents-on-Complex-Real-World-Tasks.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Yujuan Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Linyin Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Shijie Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Xu Yuan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yunshan Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yi Bin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Wenqi Fan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Qing Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering",
        "url": "papers/2026-08-24/2608.22688v1-FashionKG-RAG-Knowledge-Graph-Enhanced-Retrieval-Augmented-Generation-for-Fashio.html",
        "date": "2026-08-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Long Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuhan Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chaoran Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Wanxia Cao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Kun Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chenliang Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lixin Zou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis",
        "url": "papers/2026-08-24/2608.22847v1-GSAR-Goal-State-Anchor-Rewards-for-Mobile-GUI-Agents-with-Self-Evolving-Data-Syn.html",
        "date": "2026-08-24",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiaxuan Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents",
        "url": "papers/2026-08-23/2608.22577v2-CausalCache-Conditional-High-Fidelity-Restoration-for-Long-Horizon-GUI-Agents.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zhanfeng Liao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents",
        "url": "papers/2026-08-23/2608.22577v2-CausalCache-Conditional-High-Fidelity-Restoration-for-Long-Horizon-GUI-Agents.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiayao Teng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents",
        "url": "papers/2026-08-23/2608.22577v2-CausalCache-Conditional-High-Fidelity-Restoration-for-Long-Horizon-GUI-Agents.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuan Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents",
        "url": "papers/2026-08-23/2608.22577v2-CausalCache-Conditional-High-Fidelity-Restoration-for-Long-Horizon-GUI-Agents.html",
        "date": "2026-08-23",
        "topics": [
          "ai-agents.gui",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Murat Dura",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching",
        "url": "papers/2026-08-23/2608.22332v1-Mechanistic-Interpretability-of-Chain-of-Thought-Reasoning-via-Sequential-Activa.html",
        "date": "2026-08-23",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Serkan \u00d6zt\u00fcrk",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching",
        "url": "papers/2026-08-23/2608.22332v1-Mechanistic-Interpretability-of-Chain-of-Thought-Reasoning-via-Sequential-Activa.html",
        "date": "2026-08-23",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Selma Tekir",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching",
        "url": "papers/2026-08-23/2608.22332v1-Mechanistic-Interpretability-of-Chain-of-Thought-Reasoning-via-Sequential-Activa.html",
        "date": "2026-08-23",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Meenu Ravi",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Shailik Sarkar",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Lulwah AlKulaib",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yordanos Tessema",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Chang-Tien Lu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering",
        "url": "papers/2026-08-23/2608.22634v1-GeoRisk-RAG-A-Hierarchy-Aware-Risk-Framework-for-Improving-RAG-Reliability-throu.html",
        "date": "2026-08-23",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yuhan Meng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Shaofei Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jionghao Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jiandong Jin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Puyi Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hanlin Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Anis Yusof",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Peng Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhenkai Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ding Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system",
        "url": "papers/2026-08-15/2608.15012v1-SysEvolve-An-AI-native-safe-autonomous-adversarial-attack-defense-co-evolutionar.html",
        "date": "2026-08-15",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Haokun Deng",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation",
        "url": "papers/2026-08-30/2608.29753v1-PAGE-RAG-Provenance-Aware-Graph-Evidence-Promotion-for-Fixed-Budget-Multi-hop-Re.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xunkai Li",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation",
        "url": "papers/2026-08-30/2608.29753v1-PAGE-RAG-Provenance-Aware-Graph-Evidence-Promotion-for-Fixed-Budget-Multi-hop-Re.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hongchao Qin",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation",
        "url": "papers/2026-08-30/2608.29753v1-PAGE-RAG-Provenance-Aware-Graph-Evidence-Promotion-for-Fixed-Budget-Multi-hop-Re.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Rong-Hua Li",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation",
        "url": "papers/2026-08-30/2608.29753v1-PAGE-RAG-Provenance-Aware-Graph-Evidence-Promotion-for-Fixed-Budget-Multi-hop-Re.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Guransh Singh",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Vishwajeet Kumar",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Arkadeep Acharya",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Adnan Qidwai",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jaydeep Sen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Sachindra Joshi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking",
        "url": "papers/2026-08-30/2608.29953v1-SearchWiki-Learning-to-Build-and-Navigate-Knowledge-Wikis-for-Active-Information.html",
        "date": "2026-08-30",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Qunhui Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "AiFlow: Token-Native Reactive Orchestration with Bounded Backpressure for Streaming LLM Applications",
        "url": "papers/2026-08-01/2608.00558v1-AiFlow-Token-Native-Reactive-Orchestration-with-Bounded-Backpressure-for-Streami.html",
        "date": "2026-08-01",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Kai Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Conggai Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sarah Ali Siddiqui",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Syed Sohail Ahmed",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xin Yuan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shenghong Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Wei Ni",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "When Agentic AI Meets Integrated Sensing and Communication",
        "url": "papers/2026-08-06/2608.05792v1-When-Agentic-AI-Meets-Integrated-Sensing-and-Communication.html",
        "date": "2026-08-06",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ivaxi Sheth",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Safety Must Precede the Deployment of Open-Ended AI",
        "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html",
        "date": "2025-02-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Jan Wehner",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Safety Must Precede the Deployment of Open-Ended AI",
        "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html",
        "date": "2025-02-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Sahar Abdelnabi",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Safety Must Precede the Deployment of Open-Ended AI",
        "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html",
        "date": "2025-02-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Ruta Binkyte",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Safety Must Precede the Deployment of Open-Ended AI",
        "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html",
        "date": "2025-02-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Mario Fritz",
    "paper_count": 1,
    "topics": [
      "ai-agents"
    ],
    "papers": [
      {
        "title": "Safety Must Precede the Deployment of Open-Ended AI",
        "url": "papers/2025-02-06/2502.04512v4-Safety-Must-Precede-the-Deployment-of-Open-Ended-AI.html",
        "date": "2025-02-06",
        "topics": [
          "ai-agents"
        ]
      }
    ]
  },
  {
    "name": "Chengxiao Dai",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zhanhui Lin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zhaokun Yan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Youyang Ni",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Chenjun Lei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Luyan Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing",
        "url": "papers/2026-07-22/2607.19985v1-Coordinating-from-Memory-Graph-Structured-Experience-Reuse-for-Multi-Agent-Adapt.html",
        "date": "2026-07-22",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Debarpan Bhattacharya",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs",
        "url": "papers/2026-08-31/2608.30646v1-BiG-SURE---Bipartite-Graph-for-Semantic-Uncertainty-and-Reliability-Estimation-o.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Malay Phadke",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs",
        "url": "papers/2026-08-31/2608.30646v1-BiG-SURE---Bipartite-Graph-for-Semantic-Uncertainty-and-Reliability-Estimation-o.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Sriram Ganapathy",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs",
        "url": "papers/2026-08-31/2608.30646v1-BiG-SURE---Bipartite-Graph-for-Semantic-Uncertainty-and-Reliability-Estimation-o.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Boyang Mu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving",
        "url": "papers/2026-08-31/2608.30672v1-HiRS-Agent-A-Hierarchical-Multi-Agent-System-for-Reliable-Long-Horizon-Remote-Se.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zhiwei Wei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving",
        "url": "papers/2026-08-31/2608.30672v1-HiRS-Agent-A-Hierarchical-Multi-Agent-System-for-Reliable-Long-Horizon-Remote-Se.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mugen Peng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving",
        "url": "papers/2026-08-31/2608.30672v1-HiRS-Agent-A-Hierarchical-Multi-Agent-System-for-Reliable-Long-Horizon-Remote-Se.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Wenjia Xu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving",
        "url": "papers/2026-08-31/2608.30672v1-HiRS-Agent-A-Hierarchical-Multi-Agent-System-for-Reliable-Long-Horizon-Remote-Se.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qi Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Zhaojie Kang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yingjie He",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Zheng Lin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Hao Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Guangxin Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yan Gong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Rong Fu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jianyuan Ni",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework",
        "url": "papers/2026-08-31/2608.30498v1-CM2-Multimodal-Cultural-Reasoning-via-an-Integrated-Multi-Agent-Framework.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.multi-agent",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Shaoan Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Aocheng Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Fei Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jingyi Xu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiaoyang Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yueyu Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qianli Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Fan Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ran Mei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jia Wei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiangpeng Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xuhao Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hongming Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuanbin Shao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yiyang Lin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ziliang Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Liang Pan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xinhang Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuntao Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tingxiang Fan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation",
        "url": "papers/2026-08-31/2608.30935v1-LightNav-0-Eliciting-VLM-Spatial-Intelligence-for-Generalist-Embodied-Navigation.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Atta Ul Asad",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ahsan Bilal",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Muhammad Ali",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Muhammad Haseeb",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Dean F. Hougen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30996v1-Faithfulness-Is-Not-Free-Auditing-Offline-KV-Cache-Quantization-in-Retrieval-Aug.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Afsaneh Hasanebrahimi",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs",
        "url": "papers/2026-08-31/2608.30480v1-VisER-Visual-Evidence-and-Reliance-for-Object-Hallucination-Detection-in-LVLMs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hanxun Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs",
        "url": "papers/2026-08-31/2608.30480v1-VisER-Visual-Evidence-and-Reliance-for-Object-Hallucination-Detection-in-LVLMs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Christopher Leckie",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs",
        "url": "papers/2026-08-31/2608.30480v1-VisER-Visual-Evidence-and-Reliance-for-Object-Hallucination-Detection-in-LVLMs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Sarah Erfani",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs",
        "url": "papers/2026-08-31/2608.30480v1-VisER-Visual-Evidence-and-Reliance-for-Object-Hallucination-Detection-in-LVLMs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Walid Bousselham",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "LOCI: A Locator-Critic with Refinement Loop",
        "url": "papers/2026-08-31/2608.30959v1-LOCI-A-Locator-Critic-with-Refinement-Loop.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mathilde Caron",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "LOCI: A Locator-Critic with Refinement Loop",
        "url": "papers/2026-08-31/2608.30959v1-LOCI-A-Locator-Critic-with-Refinement-Loop.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Arsha Nagrani",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "LOCI: A Locator-Critic with Refinement Loop",
        "url": "papers/2026-08-31/2608.30959v1-LOCI-A-Locator-Critic-with-Refinement-Loop.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Cordelia Schmid",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "LOCI: A Locator-Critic with Refinement Loop",
        "url": "papers/2026-08-31/2608.30959v1-LOCI-A-Locator-Critic-with-Refinement-Loop.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mohammad Abolnejadian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings",
        "url": "papers/2026-08-31/2608.31115v1-InsightToast-Proactive-Information-Retrieval-Glanceable-Visualization-in-the-Sid.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Matthew Brehmer",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings",
        "url": "papers/2026-08-31/2608.31115v1-InsightToast-Proactive-Information-Retrieval-Glanceable-Visualization-in-the-Sid.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Peio Popov",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
        "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Mahsa Sanaei",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques",
        "url": "papers/2026-08-31/2608.31137v1-OntoAligner-Ensemble-Voting-Based-Fusion-across-Heterogeneous-Ontology-Alignment.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jingyi He",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs",
        "url": "papers/2026-08-31/2608.30705v1-VisLens-Single-Pass-Interpretable-Visual-Search-for-Multimodal-LLMs.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sanghwan Kim",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs",
        "url": "papers/2026-08-31/2608.30705v1-VisLens-Single-Pass-Interpretable-Visual-Search-for-Multimodal-LLMs.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zeynep Akata",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs",
        "url": "papers/2026-08-31/2608.30705v1-VisLens-Single-Pass-Interpretable-Visual-Search-for-Multimodal-LLMs.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mathias Zinnen",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Alisha Mund",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sabine Lang",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lukas H\u00fcttner",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Thomas Gorges",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Vincent Christlein",
    "paper_count": 1,
    "topics": [
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Lot Machine: Multimodal Lot Extraction from Auction Catalogs",
        "url": "papers/2026-08-31/2608.30510v1-Lot-Machine-Multimodal-Lot-Extraction-from-Auction-Catalogs.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yinwen Lu",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns",
        "url": "papers/2026-08-31/2608.30550v1-GarmentWeaver-Schema-Aware-Structured-Synthesis-for-Multimodal-Sewing-Patterns.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Weihao Luo",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns",
        "url": "papers/2026-08-31/2608.30550v1-GarmentWeaver-Schema-Aware-Structured-Synthesis-for-Multimodal-Sewing-Patterns.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yueqi Zhong",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns",
        "url": "papers/2026-08-31/2608.30550v1-GarmentWeaver-Schema-Aware-Structured-Synthesis-for-Multimodal-Sewing-Patterns.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Tiffanie Godelaine",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
        "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Maxime Zanella",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
        "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Karim El Khoury",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
        "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Benoit Macq",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
        "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Christophe De Vleeschouwer",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols",
        "url": "papers/2026-08-31/2608.30420v1-Whole-Slide-Image-Analysis-under-Realistic-Few-Shot-Annotation-Protocols.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Zixing Lei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Gengze Zhou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiong-Hui Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiazhao Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yiyang Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hang Yin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Haoqi Yuan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qi Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weixin Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Siheng Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation",
        "url": "papers/2026-08-31/2608.30396v1-Scaffolding-Foundation-Models-into-Physical-World-Agents-Pushes-the-Frontier-of-.html",
        "date": "2026-08-31",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Van-Giang Nguyen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification",
        "url": "papers/2026-08-31/2608.30997v1-Multi-View-Reflective-Surface-Inspection-via-Semantic-Saliency-Cross-Verificatio.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Thanh-Tuan Tran",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification",
        "url": "papers/2026-08-31/2608.30997v1-Multi-View-Reflective-Surface-Inspection-via-Semantic-Saliency-Cross-Verificatio.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xuan-Hieu Phan",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification",
        "url": "papers/2026-08-31/2608.30997v1-Multi-View-Reflective-Surface-Inspection-via-Semantic-Saliency-Cross-Verificatio.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiem HoangVan",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification",
        "url": "papers/2026-08-31/2608.30997v1-Multi-View-Reflective-Surface-Inspection-via-Semantic-Saliency-Cross-Verificatio.html",
        "date": "2026-08-31",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ruofan Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Shengyang Xu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Minjie Hong",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Xiaoda Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Sashuai Zhou",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ke Lei",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Tao Jin",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zhou Zhao",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.30163v1-Doc-REFRAG-Rethinking-Multimodal-Document-Retrieval-Augmented-Generation.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Marry Kong",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Rina Buoy",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Sovisal Chenda",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Nguonly Taing",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Masakazu Iwamura",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Koichi Kise",
    "paper_count": 1,
    "topics": [
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards a Joint Khmer Text Recognition and Word Segmentation",
        "url": "papers/2026-08-31/2608.30213v1-Towards-a-Joint-Khmer-Text-Recognition-and-Word-Segmentation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Samir Abdaljalil",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hunzalah Hassan Bhatti",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ahlam Bashiti",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Farina Amir",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Md Arid Hasan",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Basel Mousi",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Nadir Durrani",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Fahim Dalvi",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zien Sheikh Ali",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Erchin Serpedin",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hasan Kurban",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Mustafa Jarrar",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Shammur Absar Chowdhury",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Firoj Alam",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation",
        "url": "papers/2026-08-31/2608.30475v1-ImageEval-2026-Culturally-Grounded-Arabic-Multimodal-Evaluation.html",
        "date": "2026-08-31",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Riya Ahuja",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.31139v1-Configurable-Semantic-Chunking-for-Biomedical-Information-Extraction-in-Retrieva.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Tim Kacprowski",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.31139v1-Configurable-Semantic-Chunking-for-Biomedical-Information-Extraction-in-Retrieva.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Roya Shiasi Sardoabi",
    "paper_count": 1,
    "topics": [
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation",
        "url": "papers/2026-08-31/2608.31139v1-Configurable-Semantic-Chunking-for-Biomedical-Information-Extraction-in-Retrieva.html",
        "date": "2026-08-31",
        "topics": [
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Chuangtao Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
        "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html",
        "date": "2026-07-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Arijit Khan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Towards Trustworthy and Cost-Efficient Data Integration: From Na\u00efve RAG to Agentic RAG",
        "url": "papers/2026-07-24/2607.22319v1-Towards-Trustworthy-and-Cost-Efficient-Data-Integration-From-Na\u00efve-RAG-to-Agenti.html",
        "date": "2026-07-24",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hankyul Baek",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jaewon Noh",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sang Seo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yongsu Kim",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Gabriel Waikin Loh Matienzo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Young Il Kim",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ee Wei Seah",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Akriti Vij",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios",
        "url": "papers/2026-06-15/2606.17114v1-An-Evaluation-of-Data-Leakage-Risks-in-Tool-Using-LLM-Agents-in-Realistic-Scenar.html",
        "date": "2026-06-15",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Andrew Borthwick",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui"
    ],
    "papers": [
      {
        "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
        "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html",
        "date": "2026-01-03",
        "topics": [
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Stephen Ash",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui"
    ],
    "papers": [
      {
        "title": "RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution",
        "url": "papers/2026-01-03/2601.01126v2-RoboPhD-Self-Improving-Text-to-SQL-Through-Autonomous-Agent-Evolution.html",
        "date": "2026-01-03",
        "topics": [
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ruocheng Guo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Kaiwen Dong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiang Gao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Kamalika Das",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use",
        "url": "papers/2026-02-23/2602.20426v2-Learning-to-Rewrite-Tool-Descriptions-for-Reliable-LLM-Agent-Tool-Use.html",
        "date": "2026-02-23",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiaxi Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ke Deng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yun Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jingyuan Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yucheng Shi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Qiaoyu Tan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jin Lu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ninghao Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval",
        "url": "papers/2026-06-03/2606.04391v1-Online-Skill-Learning-for-Web-Agents-via-State-Grounded-Dynamic-Retrieval.html",
        "date": "2026-06-03",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jihong Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiamu Zhou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weiming Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Teng Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weiwen Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zhuosheng Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xingyu Lou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weinan Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Huarong Deng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jun Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution",
        "url": "papers/2026-01-12/2601.07262v3-ColorBrowserAgent-Complex-Long-Horizon-Browser-Agent-with-Adaptive-Knowledge-Evo.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xinyi Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Geng Hong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yueyue Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "MingXuan Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Feier Jin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Xudong Pan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jiarun Dai",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Baojun Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent",
        "url": "papers/2026-01-12/2601.07263v1-When-Bots-Take-the-Bait-Exposing-and-Mitigating-the-Emerging-Social-Engineering-.html",
        "date": "2026-01-12",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yiming Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "Hybrid Offline-Online Multi-Agent Decision Transformers for Wireless Resource Management",
        "url": "papers/2026-08-28/2608.28878v1-Hybrid-Offline-Online-Multi-Agent-Decision-Transformers-for-Wireless-Resource-Ma.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Kun Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "Hybrid Offline-Online Multi-Agent Decision Transformers for Wireless Resource Management",
        "url": "papers/2026-08-28/2608.28878v1-Hybrid-Offline-Online-Multi-Agent-Decision-Transformers-for-Wireless-Resource-Ma.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Cong Shen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "Hybrid Offline-Online Multi-Agent Decision Transformers for Wireless Resource Management",
        "url": "papers/2026-08-28/2608.28878v1-Hybrid-Offline-Online-Multi-Agent-Decision-Transformers-for-Wireless-Resource-Ma.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Dongning Guo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "Hybrid Offline-Online Multi-Agent Decision Transformers for Wireless Resource Management",
        "url": "papers/2026-08-28/2608.28878v1-Hybrid-Offline-Online-Multi-Agent-Decision-Transformers-for-Wireless-Resource-Ma.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Tejas Srinivasan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Shikib Mehri",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Nandita Shankar Naik",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Anirban Das",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "William M. Campbell",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jesse Thomason",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics",
        "url": "papers/2026-08-28/2608.27818v1-AcCoRD-Evaluating-User-Agent-Collaboration-Under-Realistic-User-Preference-Dynam.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiaoqing Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Keman Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Bin Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hongyu Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiaoyong Du",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wuqiong Pan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration",
        "url": "papers/2026-08-28/2608.28264v1-Finding-Where-the-Buck-Stops-An-Automated-Failure-Attribution-Based-Reflection-F.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Farah Atif",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sougata Saha",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Monojit Choudhury",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues",
        "url": "papers/2026-08-28/2608.28144v1-The-Shape-of-Power-A-Multilingual-Framework-for-Social-Power-Reasoning-in-Dialog.html",
        "date": "2026-08-28",
        "topics": [
          "llm-reasoning",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yupeng Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Liuyuan Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hongyi Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Bingheng Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lisha Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents",
        "url": "papers/2026-08-28/2608.28399v1-RetailAgent-Structured-Adverse-Timing-in-Self-Conditioned-Multimodal-LLM-Trading.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xinyuan Gui",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Shaowen Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Sheng Sun",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zijian Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zishu Yu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zheming Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference",
        "url": "papers/2026-08-28/2608.28726v1-Pro-Router-Token-Aware-Progressive-Model-Routing-with-Adaptive-Edge-Cloud-Collab.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Sarang Manoj Pekhale",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-28/2608.27869v1-See-Hypothesize-Validate-Multimodal-Agentic-Framework-for-Discovering-Governing-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Amartya Roy",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-28/2608.27869v1-See-Hypothesize-Validate-Multimodal-Agentic-Framework-for-Discovering-Governing-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Rajat Sarkar",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-28/2608.27869v1-See-Hypothesize-Validate-Multimodal-Agentic-Framework-for-Discovering-Governing-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Souvik Chakraborty",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "See, Hypothesize, Validate: Multimodal Agentic Framework for Discovering Governing PDEs",
        "url": "papers/2026-08-28/2608.27869v1-See-Hypothesize-Validate-Multimodal-Agentic-Framework-for-Discovering-Governing-.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Chenhong He",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Lei Li",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Shicheng Li",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Hanglong Lv",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Lingpeng Kong",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Qi Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Tong Yang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Shuhuai Ren",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs",
        "url": "papers/2026-08-28/2608.28383v1-Semantic-Head-Specialization-Guides-Hybrid-ViT-Attention-for-Multimodal-LLMs.html",
        "date": "2026-08-28",
        "topics": [
          "multi-modal",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "openJiuwen Team",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Tao Yu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Xinyu Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Qianqian Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Xiaoneng Xiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Chia Kwangyang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Xingchen Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Ran Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Yangkai Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Zheng Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Yeo Boon Hong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Bingzheng Gan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Enrui Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Shuo Cheng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Deyang Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Ruifeng Shi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Hongbo Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Qi Ye",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Xuefeng Jin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Zhangchun Zhao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents",
        "url": "papers/2026-08-28/2608.27969v1-openJiuwen-Beyond-Static-Harnesses-for-Long-Horizon-Coding-Agents.html",
        "date": "2026-08-28",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Zijie Meng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Xiwei Dai",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yixuan Tang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jin Hao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yang Feng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Fudong Zhu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Xiaoqiang Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Shaosheng Cao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Zuozhu Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning",
        "url": "papers/2026-08-19/2608.18878v1-DentAgent-Evidence-Centric-Multi-Agent-Coordination-for-Multimodal-Dental-Reason.html",
        "date": "2026-08-19",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "multi-modal",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Weiming Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents",
        "url": "papers/2026-08-26/2608.25777v1-LocalLSTC-A-Long-Short-Term-Control-Architecture-for-Locally-Deployed-GUI-Agents.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Helen Paik",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents",
        "url": "papers/2026-08-26/2608.25777v1-LocalLSTC-A-Long-Short-Term-Control-Architecture-for-Locally-Deployed-GUI-Agents.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yulei Sui",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents",
        "url": "papers/2026-08-26/2608.25777v1-LocalLSTC-A-Long-Short-Term-Control-Architecture-for-Locally-Deployed-GUI-Agents.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Hongbo Liu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Peixian Chen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Sihan Liu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Peiyuan Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Kai Zou",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Dian Zheng",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiaoxing Hu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuhao Dong",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mengdan Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yunhang Shen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Haoyu Cao",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weibo Gu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xing Sun",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shengjie Zhao",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios",
        "url": "papers/2026-08-26/2608.25529v1-Video-IFBench-Evaluating-Instruction-Following-of-Multimodal-LLMs-in-Video-Under.html",
        "date": "2026-08-26",
        "topics": [
          "llm-reasoning",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Miseon Yu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration",
        "url": "papers/2026-08-26/2608.25457v2-MACGen-Toward-Functionally-Correct-and-Secure-Code-Generation-via-Multi-Agent-Co.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jaehoon Choi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration",
        "url": "papers/2026-08-26/2608.25457v2-MACGen-Toward-Functionally-Correct-and-Secure-Code-Generation-via-Multi-Agent-Co.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Younghan Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration",
        "url": "papers/2026-08-26/2608.25457v2-MACGen-Toward-Functionally-Correct-and-Secure-Code-Generation-via-Multi-Agent-Co.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Yunheung Paek",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration",
        "url": "papers/2026-08-26/2608.25457v2-MACGen-Toward-Functionally-Correct-and-Secure-Code-Generation-via-Multi-Agent-Co.html",
        "date": "2026-08-26",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Simeng Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yilong Chen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Wenyuan Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhenyu Zhang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yao Chen",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Junyuan Shang",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Tingwen Liu",
    "paper_count": 1,
    "topics": [
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21265v2-Memory-Augmentation-Unlocks-Efficient-Chain-of-Thought-Reasoning.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Luiz Giacomossi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Zafer Yigit",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Marwan Shakarna",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Shoaib Saleemi",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Ivan Tomasic",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Baran \u00c7ur\u00fckl\u00fc",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "H\u00e5kan Forsberg",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent"
    ],
    "papers": [
      {
        "title": "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions",
        "url": "papers/2026-08-21/2608.20906v1-A-Safety-Driven-Architectural-Framework-for-Fail-Operational-Drone-Swarms-in-Cri.html",
        "date": "2026-08-21",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Yujie Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21614v1-SAEM-Stage-Aware-Expert-Management-for-Memory-Efficient-MoE-Inference-in-Chain-o.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Bin Gao",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21614v1-SAEM-Stage-Aware-Expert-Management-for-Memory-Efficient-MoE-Inference-in-Chain-o.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Tulika Mitra",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning",
        "url": "papers/2026-08-21/2608.21614v1-SAEM-Stage-Aware-Expert-Management-for-Memory-Efficient-MoE-Inference-in-Chain-o.html",
        "date": "2026-08-21",
        "topics": [
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Sujin Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps",
        "url": "papers/2026-08-18/2608.17659v1-MobileWorldSafety-Benchmarking-GUI-Agent-Safety-Against-Environmental-Injection-.html",
        "date": "2026-08-18",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Lijun Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps",
        "url": "papers/2026-08-18/2608.17659v1-MobileWorldSafety-Benchmarking-GUI-Agent-Safety-Against-Environmental-Injection-.html",
        "date": "2026-08-18",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Tianyi Du",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps",
        "url": "papers/2026-08-18/2608.17659v1-MobileWorldSafety-Benchmarking-GUI-Agent-Safety-Against-Environmental-Injection-.html",
        "date": "2026-08-18",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jing Shao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps",
        "url": "papers/2026-08-18/2608.17659v1-MobileWorldSafety-Benchmarking-GUI-Agent-Safety-Against-Environmental-Injection-.html",
        "date": "2026-08-18",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Maxime Bouthors",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Josep Crego",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Fran\u00e7ois Yvon",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Reasoning about In-Context Samples for Machine-Translation",
        "url": "papers/2026-08-27/2608.27036v1-Reasoning-about-In-Context-Samples-for-Machine-Translation.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Maciej Besta",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Leonard Schmidt",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Lara Nonino",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Robert Gerstenberger",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Pierre Pang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Patrik Okanovic",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ales Kubicek",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Tiancheng Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Baraq Lipshitz",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Torsten Hoefler",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Performance Foundations of Parallel & Distributed Reasoning Language Models",
        "url": "papers/2026-08-27/2608.27046v1-Performance-Foundations-of-Parallel-Distributed-Reasoning-Language-Models.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Guechaoui",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Diaa Zellagui",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Souleyman Chaib",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Sahraoui Dhelim",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations",
        "url": "papers/2026-08-27/2608.26921v1-AraMS-28k-The-Largest-Publicly-Released-Line-Level-Dataset-of-Historical-Arabic-.html",
        "date": "2026-08-27",
        "topics": [
          "multi-modal",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yassir Lairgi",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Ludovic Moncla",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Khalid Benabdeslem",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "R\u00e9my Cazabet",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Pierre Cl\u00e9au",
    "paper_count": 1,
    "topics": [
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning",
        "url": "papers/2026-08-27/2608.26870v1-C-Unseen-Weak-Signal-Detection-in-Dynamic-Temporal-Knowledge-Graphs-via-LLM-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Ji Soo Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jinyoung Park",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Seohyun Lee",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jongha Kim",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Joonmyung Choi",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jinsung Yoon",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Hyunwoo J. Kim",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs",
        "url": "papers/2026-08-27/2608.26684v1-Reason-in-the-Words-You-Speak-Idiolectal-Paraphrasing-Off-Policy-Traces-for-Reas.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Haowen Gu",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Gensheng Pei",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Junzhu Mao",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Qiong Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Mingwu Ren",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yazhou Yao",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation",
        "url": "papers/2026-08-27/2608.26856v1-From-Reasoning-to-Pixels-Grounded-Medical-Multimodal-LLMs-for-VQA-and-Segmentati.html",
        "date": "2026-08-27",
        "topics": [
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yu Han",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-27/2608.27508v1-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-World-Models-with-Reinforcement.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Tianwen Qian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning",
        "url": "papers/2026-08-27/2608.27508v1-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-World-Models-with-Reinforcement.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Abhigya Verma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Amit Kumar Saha",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Seganrasan Subramanian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Sai Harshitha Aluru",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling",
        "url": "papers/2026-08-27/2608.26623v1-AgentJudgeBench-A-Multi-Difficulty-Benchmark-for-Evaluating-LLM-Judges-on-Agenti.html",
        "date": "2026-08-27",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Junxuan Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zijun Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ziyi Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Peng Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yuzhou Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Ming Yan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yang Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Learning Simple Test-Time Environments for LLM Web Agents",
        "url": "papers/2026-08-29/2608.29305v1-Learning-Simple-Test-Time-Environments-for-LLM-Web-Agents.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jonan Richards",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
        "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Kosei Horikawa",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
        "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Youmei Fan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
        "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yutaro Kashiwa",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
        "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Mairieli Wessel",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent",
        "url": "papers/2026-08-29/2608.29204v1-AgentLogs-A-Dataset-for-Opening-the-Black-Box-of-GitHubs-Cloud-Agent.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Millicent Ochieng",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Felermino D. M. A. Ali",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Elizabeth A. Ankrah",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Najeeb Gambo Abdulhamid",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Migisha Boyd",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Stephanie Nyairo",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Mercy Muchai",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Samuel Chege Maina",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Aditya Vashistha",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Anja Thieme",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jacki O'Neill",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities",
        "url": "papers/2026-08-29/2608.29209v1-Toward-Cultural-Alignment-Human-Centered-Evaluation-of-Multimodal-AI-Stories-Acr.html",
        "date": "2026-08-29",
        "topics": [
          "multi-modal",
          "ai-agents.gui",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yuwei Lou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Hao Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yuzhou Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Zongfei Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jincai Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jidong Ge",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Xianping Tao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs",
        "url": "papers/2026-08-29/2608.29263v1-RACER-Reinforced-Agent-Collaboration-for-Explainable-Reasoning-on-Knowledge-Grap.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "ai-agents.multi-agent",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yian Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs",
        "url": "papers/2026-08-29/2608.29028v1-Facts-Without-Rules-Boundary-Metadata-Collapse-in-Multi-Agent-LLM-Handoffs.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Agam Goyal",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs",
        "url": "papers/2026-08-29/2608.29028v1-Facts-Without-Rules-Boundary-Metadata-Collapse-in-Multi-Agent-LLM-Handoffs.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Eshwar Chandrasekharan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs",
        "url": "papers/2026-08-29/2608.29028v1-Facts-Without-Rules-Boundary-Metadata-Collapse-in-Multi-Agent-LLM-Handoffs.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hari Sundaram",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs",
        "url": "papers/2026-08-29/2608.29028v1-Facts-Without-Rules-Boundary-Metadata-Collapse-in-Multi-Agent-LLM-Handoffs.html",
        "date": "2026-08-29",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zihan Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Longxu Dou",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qi Gao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiangwu Guo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Shengchao Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zilong Huang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zihang Jiang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Lei Ke",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mengcheng Lan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weixian Lei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Hanxuan Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Honglin Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xiyun Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zaitang Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Leowei Liang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xin Luo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Haozhe Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Jiayi Mao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zhoujie Pan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Can Qin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Tianyuan Qu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Weiqi Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yonglin Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuxin Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chenxu Wu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yingchen Yu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Chenyu Zhang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Yuhao Zheng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations",
        "url": "papers/2026-08-16/2608.15930v1-UI-Mate-Advancing-Open-Weight-Foundation-GUI-Agents-with-In-Context-Demonstratio.html",
        "date": "2026-08-16",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ryan C. Barron",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
        "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html",
        "date": "2025-02-27",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Maksim E. Eren",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
        "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html",
        "date": "2025-02-27",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Olga M. Serafimova",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
        "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html",
        "date": "2025-02-27",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Cynthia Matuszek",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
        "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html",
        "date": "2025-02-27",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Boian S. Alexandrov",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Bridging Legal Knowledge and AI: Retrieval-Augmented Generation with Vector Stores, Knowledge Graphs, and Hierarchical Non-negative Matrix Factorization",
        "url": "papers/2025-02-27/2502.20364v2-Bridging-Legal-Knowledge-and-AI-Retrieval-Augmented-Generation-with-Vector-Store.html",
        "date": "2025-02-27",
        "topics": [
          "rag-retrieval",
          "multi-modal",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Eduardo Almeida Palmieri",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Mohamed Chahine Ghanem",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Dipo Dunsin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Zubair Baig",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Ed de Quincey",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Kim-Kwang Raymond Choo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "Agentic and Generative AI for Open-Source Intelligence and Cyber Investigations: Taxonomy, Evaluation, Challenges, and Future Directions",
        "url": "papers/2026-07-03/2607.03233v1-Agentic-and-Generative-AI-for-Open-Source-Intelligence-and-Cyber-Investigations-.html",
        "date": "2026-07-03",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "rag-retrieval",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Xu Mingze",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "ai-agents.multi-agent",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture",
        "url": "papers/2026-04-06/2604.04820v1-ANX-Protocol-First-Design-for-AI-Agent-Interaction-with-a-Supporting-3EX-Decoupl.html",
        "date": "2026-04-06",
        "topics": [
          "ai-agents",
          "ai-agents.gui",
          "ai-agents.multi-agent",
          "llm-reasoning",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Samira Abedini",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
        "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html",
        "date": "2026-03-16",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Sina Mavali",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
        "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html",
        "date": "2026-03-16",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Lea Sch\u00f6nherr",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
        "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html",
        "date": "2026-03-16",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Martin Pawelczyk",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
        "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html",
        "date": "2026-03-16",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Rebekka Burkholz",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks",
        "url": "papers/2026-03-16/2603.15809v1-Dont-Trust-Stubborn-Neighbors-A-Security-Framework-for-Agentic-Networks.html",
        "date": "2026-03-16",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.multi-agent"
        ]
      }
    ]
  },
  {
    "name": "Jagadeesh Chundru",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "Agentic Compilation: Mitigating the LLM Rerun Crisis for Minimized-Inference-Cost Web Automation",
        "url": "papers/2026-04-08/2604.09718v2-Agentic-Compilation-Mitigating-the-LLM-Rerun-Crisis-for-Minimized-Inference-Cost.html",
        "date": "2026-04-08",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yinfang Chen",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Manish Shetty",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Gagan Somashekar",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Minghua Ma",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Yogesh Simmhan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Jonathan Mace",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Chetan Bansal",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Rujia Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Saravan Rajmohan",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning",
      "multi-modal"
    ],
    "papers": [
      {
        "title": "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds",
        "url": "papers/2025-01-12/2501.06706v1-AIOpsLab-A-Holistic-Framework-to-Evaluate-AI-Agents-for-Enabling-Autonomous-Clou.html",
        "date": "2025-01-12",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "multi-modal",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Huanxi Liu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Kun Hu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Jiaqi Liao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Qiang Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Pengfei Qian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "YuanZhao Zhai",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Dawei Feng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Bo Ding",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Huaimin Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers",
        "url": "papers/2026-07-16/2607.14642v1-MCPEvol-Bench-Benchmarking-LLM-Agent-Performance-Across-Dynamic-Evolutions-of-MC.html",
        "date": "2026-07-16",
        "topics": [
          "llm-reasoning",
          "ai-agents",
          "rag-retrieval"
        ]
      }
    ]
  },
  {
    "name": "Shen You",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiaoming Zhu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Weining Weng",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Hefei Mei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Weixuan Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhongshen Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zeji LI",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ye-Wen Wang",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zijun Liao",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Juchao Zhuo",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Yang Wei",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Fuhao Qiu",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Siqin Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Zhenjie Lian",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Danei Gong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Junkai Ji",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Xiangtao Li",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Qiuzhen Lin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Ka-Chun Wong",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.multi-agent",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction",
        "url": "papers/2026-08-03/2608.01652v1-SyncPlan-Long-Horizon-LLM-Coordination-with-Explicit-Synchronization-and-Adaptiv.html",
        "date": "2026-08-03",
        "topics": [
          "ai-agents",
          "ai-agents.multi-agent",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Sidra Nasir",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "A Comprehensive Framework for Reliable Legal AI: Combining Specialized Expert Systems and Adaptive Refinement",
        "url": "papers/2024-12-29/2412.20468v2-A-Comprehensive-Framework-for-Reliable-Legal-AI-Combining-Specialized-Expert-Sys.html",
        "date": "2024-12-29",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Qamar Abbas",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "A Comprehensive Framework for Reliable Legal AI: Combining Specialized Expert Systems and Adaptive Refinement",
        "url": "papers/2024-12-29/2412.20468v2-A-Comprehensive-Framework-for-Reliable-Legal-AI-Combining-Specialized-Expert-Sys.html",
        "date": "2024-12-29",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Samita Bai",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "A Comprehensive Framework for Reliable Legal AI: Combining Specialized Expert Systems and Adaptive Refinement",
        "url": "papers/2024-12-29/2412.20468v2-A-Comprehensive-Framework-for-Reliable-Legal-AI-Combining-Specialized-Expert-Sys.html",
        "date": "2024-12-29",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Rizwan Ahmed Khan",
    "paper_count": 1,
    "topics": [
      "ai-agents.gui",
      "multi-modal",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "A Comprehensive Framework for Reliable Legal AI: Combining Specialized Expert Systems and Adaptive Refinement",
        "url": "papers/2024-12-29/2412.20468v2-A-Comprehensive-Framework-for-Reliable-Legal-AI-Combining-Specialized-Expert-Sys.html",
        "date": "2024-12-29",
        "topics": [
          "rag-retrieval",
          "ai-agents.gui",
          "multi-modal"
        ]
      }
    ]
  },
  {
    "name": "Masahiro Kato",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning",
      "rag-retrieval"
    ],
    "papers": [
      {
        "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
        "url": "papers/2026-06-18/2606.20041v1-AI-Economist-Agent-An-Agentic-Framework-for-Model-Grounded-Economic-Analysis-wit.html",
        "date": "2026-06-18",
        "topics": [
          "rag-retrieval",
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Honjar Xing",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs",
        "url": "papers/2026-06-18/2606.20978v1-How-Should-Agents-Read-Demonstrations-Hierarchical-Structure-Beats-Flat-Action-L.html",
        "date": "2026-06-18",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Jefferson Lin",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs",
        "url": "papers/2026-06-18/2606.20978v1-How-Should-Agents-Read-Demonstrations-Hierarchical-Structure-Beats-Flat-Action-L.html",
        "date": "2026-06-18",
        "topics": [
          "ai-agents",
          "llm-reasoning"
        ]
      }
    ]
  },
  {
    "name": "Henry Lieberman",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs",
        "url": "papers/2026-06-18/2606.20978v1-How-Should-Agents-Read-Demonstrations-Hierarchical-Structure-Beats-Flat-Action-L.html",
        "date": "2026-06-18",
        "topics": [
          "ai-agents",
          "llm-reasoning"
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
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Daniel Garcia",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Fjona Parllaku",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Vikas Upadhyay",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Syed Fahad Allam Shah",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
        ]
      }
    ]
  },
  {
    "name": "Dan Roth",
    "paper_count": 1,
    "topics": [
      "ai-agents",
      "ai-agents.gui",
      "llm-reasoning"
    ],
    "papers": [
      {
        "title": "ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering",
        "url": "papers/2025-10-22/2510.20036v2-ToolScope-Enhancing-LLM-Agent-Tool-Use-through-Tool-Merging-and-Context-Aware-Fi.html",
        "date": "2025-10-22",
        "topics": [
          "ai-agents",
          "llm-reasoning",
          "ai-agents.gui"
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
    `Showing ${filtered.length} of ${authorsData.length} authors`;
  
  const container = document.getElementById('authorsList');
  
  if (filtered.length === 0) {
    container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">No authors found.</p>';
    return;
  }
  
  container.innerHTML = filtered.map(author => `
    <div class="author-card" onclick="this.classList.toggle('expanded')">
      <div class="author-header">
        <span class="author-name">${author.name}</span>
        <div class="author-stats">
          <span class="paper-badge">${author.paper_count} paper${author.paper_count !== 1 ? 's' : ''}</span>
          <span class="expand-icon">▶</span>
        </div>
      </div>
      <div class="author-topics">
        ${author.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
      </div>
      <div class="author-papers">
        ${author.papers.map(p => `
          <div class="paper-entry">
            <a href="${p.url}">${p.title}</a>
            <span class="paper-date">${p.date}</span>
          </div>
        `).join('')}
      </div>
    </div>
  `).join('');
}

document.getElementById('authorSearch').addEventListener('input', renderAuthors);
document.getElementById('topicFilter').addEventListener('change', renderAuthors);

renderAuthors();
</script>
