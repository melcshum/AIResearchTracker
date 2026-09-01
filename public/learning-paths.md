---
title: "Learning Paths"
---

Structured reading guides for different backgrounds and goals. Each path builds knowledge progressively, linking to foundational concepts and key papers.

## Path 1: New to AI → Build Foundations

**Goal**: Understand core AI concepts from scratch, progressing to modern agent systems.

**Prerequisites**: Basic programming knowledge, familiarity with machine learning concepts helpful but not required.

### Step 1: Understand LLM Reasoning (1-2 days)
Start here — reasoning is the foundation everything else builds on.

**Read:**
- [LLM Reasoning: Foundations](topics/llm-reasoning.html#foundations) — What is reasoning? Chain-of-thought, self-consistency, tree-of-thought
- [Glossary: Reasoning Concepts](concepts/glossary.html#reasoning-concepts) — Look up any unfamiliar terms

**Key papers:**
- [Thinking Costs Tokens](papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) — Understand efficiency tradeoffs in reasoning
- [SABER: Early Exit for LLM Reasoning](papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html) — See how to reduce reasoning costs

**Checkpoint**: Can you explain chain-of-thought reasoning? Do you understand why "more thinking" isn't always better?

### Step 2: Learn Retrieval & RAG (1-2 days)
Now understand how models access external knowledge.

**Read:**
- [RAG & Retrieval: Foundations](topics/rag-retrieval.html#foundations) — What is RAG? Dense vs sparse retrieval, hybrid search
- [Glossary: Retrieval Concepts](concepts/glossary.html#retrieval-concepts)

**Key papers:**
- [Retrieving Relations, Detecting Fallacies](papers/2026-08-31/2608.27471-Retrieving-Relations-Detecting-Fallacies-A-RAG-App.html) — RAG for reasoning about political debates
- [CareGraph](papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html) — Hybrid approach combining knowledge graphs with LLMs

**Checkpoint**: Can you explain the difference between dense and sparse retrieval? Do you understand how RAG reduces hallucination?

### Step 3: Explore Multi-Modal Models (1-2 days)
Understand how models process images, audio, and video.

**Read:**
- [Multi-Modal: Foundations](topics/multi-modal.html#foundations) — Vision-language models, cross-modal reasoning
- [Glossary: Multi-Modal Concepts](concepts/glossary.html#multi-modal-concepts)

**Key papers:**
- [Nemotron 3.5 Content Safety Moderator](papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html) — Multimodal safety moderation
- [See, Hypothesize, Validate](papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html) — Multimodal agent for scientific discovery

**Checkpoint**: Can you explain what a vision-language model is? Do you understand cross-modal reasoning?

### Step 4: Bring It Together — AI Agents (2-3 days)
Now you're ready for agents, which combine reasoning, retrieval, and multi-modal capabilities.

**Read:**
- [AI Agents: Foundations](topics/ai-agents.html#foundations) — What is an agent? Core components, architectures
- [How Concepts Connect](concepts/connections.html) — See how everything relates
- [Glossary: Agent Concepts](concepts/glossary.html#agent-concepts)

**Key papers:**
- [WM-R1: GUI Agents with World Models](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — Agents that reason and plan using world models
- [If Agents Were Angels, No Governance Would Be Necessary](papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html) — Agent safety and governance

**Checkpoint**: Can you explain the ReAct paradigm? Do you understand why agent safety is a fundamental challenge?

**Total time**: 1-2 weeks

---

## Path 2: Software Engineer → Build Agents

**Goal**: Understand agent architecture and implementation patterns to build your own systems.

**Prerequisites**: Strong programming skills, basic understanding of LLMs and APIs.

### Step 1: Agent Architecture (2-3 days)
Start with the big picture — what agents are and how they're structured.

**Read:**
- [AI Agents: Foundations](topics/ai-agents.html#foundations) — Core components, architectures, challenges
- [How Concepts Connect: Agents + Reasoning](concepts/connections.html#agents--reasoning) — How agents use reasoning
- [How Concepts Connect: Agents + Retrieval](concepts/connections.html#agents--retrieval) — How agents access knowledge

**Key papers:**
- [WM-R1](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) — Study the agent architecture: perception → planning → action → observation
- [SETU](papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) — Multi-agent system design

**Checkpoint**: Can you diagram an agent architecture? Do you understand the tool-use loop?

### Step 2: Tool Use & Retrieval (2-3 days)
Learn how agents access external knowledge and capabilities.

**Read:**
- [RAG & Retrieval: Foundations](topics/rag-retrieval.html#foundations) — RAG pipeline, retrieval methods
- [How Concepts Connect: Retrieval + Reasoning](concepts/connections.html#reasoning--retrieval)

**Key papers:**
- [CareGraph](papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html) — Hybrid retrieval with knowledge graphs
- [WeAgent-MMSearch](papers/2026-08-31/2608.28062-WeAgent-MMSearch-Native-Text-Vision-Interaction-fo.html) — Agentic search with tool use

**Checkpoint**: Can you explain how to give an agent access to external APIs? Do you understand when to use RAG vs parametric knowledge?

### Step 3: Safety & Governance (1-2 days)
Critical for production systems — understand agent safety challenges.

**Read:**
- [AI Agents: Key Challenges](topics/ai-agents.html#key-challenges) — Safety, compositional risk, reliability
- [Glossary: Compositional Safety](concepts/glossary.html#compositional-safety)

**Key papers:**
- [If Agents Were Angels](papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html) — Governance at trusted tool boundaries
- [Cross-Session Decomposition Attacks](papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) — Compositional safety risks

**Checkpoint**: Can you explain why agent safety is harder than LLM safety? Do you understand trusted tool boundaries?

### Step 4: Browse Implementation Patterns (ongoing)
Study real agent implementations and patterns.

**Read:**
- [Papers by Concept: Tool Use](concepts/papers-by-concept.html#tool-use) — Papers demonstrating tool use
- [Papers by Concept: Planning](concepts/papers-by-concept.html#planning) — Papers on multi-step planning
- [Weekly Digests](digests/index.html) — Stay current with latest developments

**Total time**: 1-2 weeks for foundations, ongoing for staying current

---

## Path 3: ML Researcher → Cutting Edge

**Goal**: Quickly get up to speed on state-of-the-art research and identify open problems.

**Prerequisites**: Strong ML background, familiar with LLMs and recent literature.

### Step 1: This Week's Developments (30 min)
Start with the latest digest to see what's happening now.

**Read:**
- [Week 35 Digest](digests/week-2026-35.html) — Key papers and trends from this week

### Step 2: Browse by Concept (1-2 hours)
Use the concept-based organization to find papers relevant to your interests.

**Read:**
- [Papers by Concept](concepts/papers-by-concept.html) — Browse papers tagged with concepts you care about
- [Cross-Concept Papers](concepts/papers-by-concept.html#cross-concept-papers) — Papers at the intersections (often most interesting)

### Step 3: Dive into Specific Topics (ongoing)
Follow research threads that interest you.

**Read:**
- Topic pages for active research directions:
  - [AI Agents: Active Research](topics/ai-agents.html#active-research-directions)
  - [LLM Reasoning: Active Research](topics/llm-reasoning.html#active-research-directions)
  - [RAG & Retrieval: Active Research](topics/rag-retrieval.html#active-research-directions)
  - [Multi-Modal: Active Research](topics/multi-modal.html#active-research-directions)
- [Papers by date](papers/index.html) — Newest papers first

### Step 4: Identify Open Problems (ongoing)
Look for gaps and opportunities.

**Focus on:**
- Papers mentioning "limitations" or "future work"
- Cross-concept papers that reveal connections between fields
- Safety and governance papers — often underexplored areas with high impact

**Total time**: 2-3 hours to get oriented, ongoing for staying current

---

## Quick Reference

### Concept Cheat Sheet

| Concept | One-sentence explanation | Learn more |
|---------|-------------------------|------------|
| **AI Agent** | Autonomous system that perceives, reasons, and acts | [Foundations](topics/ai-agents.html#foundations) |
| **Chain-of-Thought** | Step-by-step reasoning before answering | [Foundations](topics/llm-reasoning.html#foundations) |
| **RAG** | Retrieving documents to ground generation | [Foundations](topics/rag-retrieval.html#foundations) |
| **Vision-Language Model** | Model that processes both images and text | [Foundations](topics/multi-modal.html#foundations) |
| **World Models** | Internal simulations for predictive planning | [Glossary](concepts/glossary.html#world-models) |
| **Early Exit** | Stopping reasoning when answer stabilizes | [Glossary](concepts/glossary.html#early-exit) |
| **Hybrid Search** | Combining dense and sparse retrieval | [Glossary](concepts/glossary.html#hybrid-search) |

### Time Estimates

| Path | Audience | Time to foundations | Time to cutting edge |
|------|----------|-------------------|---------------------|
| Path 1 | New to AI | 1-2 weeks | 3-4 weeks |
| Path 2 | Software Engineer | 1-2 weeks | Ongoing |
| Path 3 | ML Researcher | 2-3 hours | Ongoing |
