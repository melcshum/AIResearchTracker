---
title: "Papers by Concept"
---

Browse papers by the foundational concepts they address. Each paper is tagged with relevant concepts from the [glossary](glossary.html).

## Agent Concepts

### Tool Use
Papers demonstrating agents that call APIs, execute code, or interact with external systems.

- [WM-R1: Training GUI Agents to Reason and leverage World Models](../papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — GUI agents using world models for predictive planning
- [Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery](../papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html) — Agent that uses tools for scientific discovery
- [SETU: An Agentic Ecosystem for Multilingual Communication Coaching](../papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) — Multi-agent system for communication training

### Planning
Papers on multi-step planning, decomposition, and goal-directed behavior.

- [WM-R1: Training GUI Agents to Reason and leverage World Models](../papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — World models enable predictive planning without real-environment interaction
- [Thinking Costs Tokens: When More Structure is Worth the Price](../papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) — Token budget thresholds for planning overhead

### World Models
Papers on internal simulations of environment dynamics for predictive reasoning.

- [WM-R1: Training GUI Agents to Reason and leverage World Models](../papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — First RL framework training GUI agents with world models instead of real environments

### Multi-Agent Systems
Papers on multiple specialized agents collaborating.

- [SETU: An Agentic Ecosystem for Multilingual Communication Coaching](../papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) — Agentic ecosystem with specialized agents for different modalities

### Safety & Governance
Papers on ensuring agents act within policy boundaries.

- [If Agents Were Angels, No Governance Would Be Necessary](../papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html) — Out-of-band policy enforcement at trusted tool boundaries
- [Cross-Session Decomposition Attacks](../papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) — Compositional safety risks from reassembling benign subqueries

## Reasoning Concepts

### Chain-of-Thought
Papers on step-by-step reasoning and intermediate verification.

- [Thinking Costs Tokens: When More Structure is Worth the Price](../papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) — Investigates token-budget thresholds for planning and verification

### Early Exit
Papers on stopping reasoning when answers stabilize to reduce costs.

- [SABER: Stability-Aware Early Exit for LLM Reasoning](../papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html) — Training-free early exit via adversarial branch probing

### Verification & Reflection
Papers on checking intermediate steps or outputs for correctness.

- [Hypothesize, Evaluate, Refine: A Scientific Agent for PDE Discovery](../papers/2026-08-31/2608.27475-Hypothesize-Evaluate-Refine-A-Scientific-Agent-for.html) — Agent that hypothesizes, evaluates, and refines scientific models
- [See, Hypothesize, Validate: Multimodal Agentic Framework](../papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html) — Multimodal agent with explicit validation steps

### Efficiency in Reasoning
Papers on reducing token costs while preserving reasoning quality.

- [SABER: Stability-Aware Early Exit for LLM Reasoning](../papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html) — 30-40% token reduction via stability-aware early exit
- [Thinking Costs Tokens: When More Structure is Worth the Price](../papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) — Token budget thresholds and complexity-aware reasoning

### Causal Reasoning
Papers evaluating or improving causal and counterfactual reasoning.

- [The Illusion of What If: Evaluating Counterfactual Reasoning in LLMs](../papers/2026-08-31/2608.27953-The-Illusion-of-textitWhat-If-Evaluating-the-Break.html) — Reveals LLMs rely on surface heuristics rather than genuine counterfactual understanding

## Retrieval Concepts

### RAG (Retrieval-Augmented Generation)
Papers on combining retrieval with generation to reduce hallucination.

- [Retrieving Relations, Detecting Fallacies: A RAG Approach](../papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html) — RAG for political debate fallacy detection
- [From Documents to Reasoning: Synthetic Data Pipeline for Financial QA](../papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html) — Retrieval-grounded numerical reasoning

### Knowledge Graphs
Papers on structured knowledge representations for reasoning and retrieval.

- [CareGraph: An Auditable Hybrid AI Framework](../papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html) — Knowledge graphs for personalized health intelligence
- [Retrieving Relations, Detecting Fallacies: A RAG Approach](../papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html) — Relation retrieval for fallacy detection

### Hybrid Search
Papers combining dense and sparse retrieval methods.

- [CareGraph: An Auditable Hybrid AI Framework](../papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html) — Hybrid neuro-symbolic approach combining LLMs with structured knowledge

### Intent-Aligned Retrieval
Papers on retrieval focused on user intent rather than semantic similarity.

- [Cross-Session Decomposition Attacks](../papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) — 22M-parameter intent-aligned retrievers outperform larger embedding models for safety

## Multi-Modal Concepts

### Vision-Language Models
Papers on models that process both images and text.

- [See, Hypothesize, Validate: Multimodal Agentic Framework](../papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html) — Multimodal agent for discovering governing PDEs from observational data
- [WeAgent-MMSearch: Native Text-Vision Interaction](../papers/2026-08-31/2608.28062-WeAgent-MMSearch-Native-Text-Vision-Interaction-fo.html) — Multimodal search agent with native text-vision interaction

### Multimodal Safety
Papers on content moderation across multiple modalities.

- [Nemotron 3.5 Content Safety Moderator](../papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html) — Compact multimodal, multilingual safety moderation

### Continual Learning
Papers on acquiring new capabilities without forgetting old ones.

- [CoRe-MoE: Compact Reusable MoE for Continual Multimodal Instruction Tuning](../papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html) — Sequential task acquisition without catastrophic forgetting

### Document Understanding
Papers on reading and reasoning about documents, charts, and tables.

- [From Documents to Reasoning: Synthetic Data Pipeline for Financial QA](../papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html) — Numerical reasoning over financial documents with tables and charts

### Accessibility-Aware Planning
Papers on multimodal systems assisting users with accessibility requirements.

- [MAP: A Benchmark on Multimodal Accessibility Planning](../papers/2026-08-31/2608.28384-MAP-A-Benchmark-on-Multimodal-Accessibility-Planni.html) — First benchmark for multimodal AI as accessibility assistants

## Cross-Concept Papers

Papers that span multiple concept areas, showing how these research directions intersect.

### Agents + Reasoning + World Models
- [WM-R1: Training GUI Agents to Reason and leverage World Models](../papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — Combines agent architecture, reasoning, and world models for GUI automation

### Agents + Retrieval + Safety
- [Cross-Session Decomposition Attacks](../papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) — Safety risks at the intersection of agents, retrieval, and compositional reasoning

### Reasoning + Retrieval + Domain Applications
- [Retrieving Relations, Detecting Fallacies](../papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html) — RAG for reasoning about political debates
- [From Documents to Reasoning](../papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html) — Retrieval-grounded reasoning for financial QA

### Multi-Modal + Agents + Verification
- [See, Hypothesize, Validate](../papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html) — Multimodal agent with explicit verification steps for scientific discovery

### Multi-Modal + Continual Learning + Efficiency
- [CoRe-MoE](../papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html) — Efficient continual learning for multimodal models using Mixture-of-Experts
