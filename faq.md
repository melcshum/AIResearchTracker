---
title: "Frequently Asked Questions"
---

Common questions about AI agents, reasoning, retrieval, and multi-modal systems.

## General Questions

### What's the difference between an AI agent and a chatbot?

A chatbot responds to individual prompts in isolation. An AI agent is autonomous — it maintains state across interactions, uses tools (APIs, code execution, web browsing), plans multi-step actions, and learns from feedback. Think of a chatbot as a Q&A system, while an agent is more like a digital assistant that can accomplish complex tasks.

**Learn more**: [AI Agents: Foundations](topics/ai-agents.html#foundations)

### Do I need to understand all these concepts to use AI?

No. Most users interact with AI systems without understanding the underlying architecture. However, if you're:
- **Building AI applications**: Understanding RAG, reasoning, and agent architecture is essential
- **Evaluating AI systems**: Knowing about limitations (hallucination, safety risks) helps you assess reliability
- **Researching AI**: You'll need deep knowledge of all these concepts

**Start here**: [Learning Paths](learning-paths.html) — choose the path that matches your goals

### What's the most important concept to understand?

It depends on your goals:
- **Building applications**: RAG (Retrieval-Augmented Generation) — it's the foundation for most practical AI systems
- **Understanding limitations**: Reasoning efficiency and safety — these determine what AI can and can't do reliably
- **Future trends**: AI agents — this is where the field is heading

**Quick overview**: [How Concepts Connect](concepts/connections.html)

## Technical Questions

### What is RAG and why does it matter?

RAG (Retrieval-Augmented Generation) combines information retrieval with text generation. Instead of relying only on knowledge stored in model weights, the model retrieves relevant documents at inference time and uses them to ground its response. This reduces hallucination, improves factual accuracy, and enables access to up-to-date or proprietary information.

**Why it matters**: Most production AI systems use RAG. It's the difference between a model that "knows" things (and sometimes makes them up) and one that can look things up and cite sources.

**Learn more**: [RAG & Retrieval: Foundations](topics/rag-retrieval.html#foundations)

### What's the difference between dense and sparse retrieval?

- **Sparse retrieval** (e.g., BM25): Matches on exact keywords. Fast, interpretable, works well when you know the exact terms.
- **Dense retrieval** (e.g., BGE, E5): Uses learned embeddings to find semantically similar documents. Better for conceptual queries where keywords don't match exactly.
- **Hybrid search**: Combines both for robustness.

**Analogy**: Sparse is like searching for "apple" and getting documents with the word "apple". Dense is like searching for "fruit" and getting documents about apples, oranges, and bananas.

**Learn more**: [Glossary: Retrieval Methods](concepts/glossary.html#retrieval-methods)

### Why is reasoning efficiency important?

LLM reasoning (chain-of-thought, verification, planning) improves accuracy but costs tokens. Recent research shows:
- **Over-thinking is real**: More reasoning steps don't always mean better answers
- **Early exit works**: You can stop reasoning when the answer stabilizes, saving 30-50% of tokens
- **Token budgets matter**: Below certain thresholds, planning overhead hurts more than it helps

**Practical impact**: Efficiency determines whether AI systems are economically viable at scale.

**Learn more**: [LLM Reasoning: Efficiency](topics/llm-reasoning.html#efficiency-in-reasoning)

### What are world models and why do agents need them?

World models are internal simulations of environment dynamics. Instead of trying actions in the real world (expensive, slow, sometimes dangerous), agents simulate outcomes in their "mind" before committing. This enables:
- **Predictive planning**: Reason about consequences before acting
- **Sample efficiency**: Learn from simulated experiences
- **Safety**: Test dangerous actions in simulation first

**Example**: A GUI agent simulates clicking a button to predict what will happen, rather than actually clicking and potentially breaking something.

**Learn more**: [Glossary: World Models](concepts/glossary.html#world-models), [WM-R1 paper](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html)

### What is compositional safety and why is it a problem?

Compositional safety refers to the risk that benign subtasks, when reassembled across sessions or contexts, can create harmful objectives. For example:
- Session 1: "What's the address of X?" (benign)
- Session 2: "What's the schedule of X?" (benign)
- Session 3: "When is X out of town?" (benign)
- Combined: Stalking plan (harmful)

**Why it's hard**: Each individual query passes safety checks. The harm only emerges when queries are combined. Larger models paradoxically increase vulnerability because they're better at following complex instructions.

**Learn more**: [Cross-Session Decomposition Attacks](papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html)

## Practical Questions

### How do I choose between different agent architectures?

It depends on your use case:
- **Simple Q&A with tools**: ReAct (reason → act → observe → repeat)
- **Complex multi-step tasks**: Multi-agent systems with specialized agents
- **Visual environments**: Embodied agents with world models
- **High-stakes domains**: Agents with explicit verification steps

**Decision framework**: [Learning Path 2: Software Engineer](learning-paths.html#path-2-software-engineer--build-agents)

### What are the biggest limitations of current AI systems?

1. **Hallucination**: Models generate plausible but incorrect information (mitigated by RAG)
2. **Reasoning failures**: Models rely on surface heuristics rather than genuine understanding
3. **Safety risks**: Compositional attacks, prompt injection, goal misalignment
4. **Efficiency**: Reasoning is expensive; over-thinking wastes resources
5. **Catastrophic forgetting**: Learning new tasks can degrade old ones

**Learn more**: [Must-Read Papers: Evaluation & Benchmark](must-read-papers.html#evaluation--benchmark-papers)

### How do I stay current with AI research?

1. **Weekly digests**: Check our [Digests](digests/index.html) for weekly summaries
2. **Must-read papers**: Review [Must-Read Papers](must-read-papers.html) quarterly
3. **Topic pages**: Browse [Active Research Directions](topics/ai-agents.html#active-research-directions) in each topic
4. **Papers by date**: Check [Papers](papers/index.html) for the latest work

### Where can I learn more about specific concepts?

- **Definitions**: [Glossary](concepts/glossary.html) — 40+ key terms
- **Relationships**: [How Concepts Connect](concepts/connections.html) — see how ideas relate
- **Examples**: [Papers by Concept](concepts/papers-by-concept.html) — papers tagged with concepts
- **Deep dives**: Topic pages for each area (AI Agents, LLM Reasoning, RAG, Multi-Modal)

## Unanswered Questions?

This FAQ covers common questions, but AI research moves fast. If you have questions not addressed here:

1. Check the [Glossary](concepts/glossary.html) for definitions
2. Browse [Papers by Concept](concepts/papers-by-concept.html) for examples
3. Read the latest [Weekly Digest](digests/index.html) for current developments
4. Explore [Learning Paths](learning-paths.html) for structured learning
