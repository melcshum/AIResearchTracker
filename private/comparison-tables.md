---
title: "Comparison Tables"
---

Quick reference tables comparing different approaches, architectures, and methods.

## Agent Architectures

| Architecture | Best For | Key Strength | Key Limitation | Example Papers |
|--------------|----------|--------------|----------------|----------------|
| **ReAct** | Simple tool-use tasks | Easy to implement, interpretable | Can get stuck in loops, limited planning | [WM-R1](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) |
| **Tool-Use Agents** | API integration, code execution | Flexible, can access any tool | Requires careful tool design, error handling | [SETU](papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) |
| **Multi-Agent Systems** | Complex, multi-domain tasks | Specialization, parallelism | Coordination overhead, debugging complexity | [SETU](papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) |
| **Embodied Agents** | GUI automation, robotics | Handles spatial reasoning, continuous state | Expensive training, sim-to-real gap | [WM-R1](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) |
| **World Model Agents** | Predictive planning, sample efficiency | Plans without real-world interaction | Model accuracy limits performance | [WM-R1](papers/2026-08-31/2608.27508-WM-R1-Training-GUI-Agents-to-Reason-and-leverage-W.html) |

## Reasoning Methods

| Method | How It Works | Token Cost | Accuracy | Best For |
|--------|--------------|------------|----------|----------|
| **Chain-of-Thought (CoT)** | Step-by-step reasoning | Medium | High (for complex tasks) | Math, logic, planning |
| **Self-Consistency** | Sample multiple paths, vote | High (N×CoT) | Very High | Tasks with multiple solution paths |
| **Tree-of-Thought** | Explore reasoning tree, prune | Very High | Highest (for hard problems) | Complex problems with dead ends |
| **Early Exit (SABER)** | Stop when answer stabilizes | Low (30-50% savings) | Same as CoT | Cost-sensitive deployment |
| **Verification** | Check intermediate steps | Medium-High | High (reduces errors) | High-stakes decisions |

**Key insight**: More reasoning ≠ better. [Thinking Costs Tokens](papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) shows there are token-budget thresholds below which overhead hurts.

## Retrieval Methods

| Method | How It Works | Speed | Accuracy | Best For |
|--------|--------------|-------|----------|----------|
| **Sparse (BM25)** | Keyword matching | Very Fast | Good (exact matches) | Known terms, fast retrieval |
| **Dense (Embeddings)** | Semantic similarity | Fast | Better (conceptual) | Natural language queries |
| **Hybrid** | Combine sparse + dense | Medium | Best | General-purpose retrieval |
| **Re-ranking** | Second-stage scoring | Slower | Highest | High-precision needs |
| **Knowledge Graphs** | Structured entity-relation | Varies | Best (for structured data) | Domain-specific reasoning |

**When to use what**:
- **Know the exact terms?** → Sparse retrieval
- **Conceptual query?** → Dense retrieval
- **Need both?** → Hybrid search
- **High stakes?** → Add re-ranking
- **Structured domain?** → Knowledge graphs

**Example**: [CareGraph](papers/2026-08-31/2608.27484-CareGraph-An-Auditable-Hybrid-AI-Framework-for-Evi.html) uses hybrid neuro-symbolic retrieval for medical AI.

## Multi-Modal Architectures

| Architecture | Modalities | Key Strength | Key Limitation | Example Papers |
|--------------|------------|--------------|----------------|----------------|
| **Vision-Language (VLM)** | Image + Text | Visual understanding, VQA | Can hallucinate visual details | [See, Hypothesize, Validate](papers/2026-08-31/2608.27869-See-Hypothesize-Validate-Multimodal-Agentic-Framew.html) |
| **Audio-Language** | Audio + Text | Speech understanding, dialogue | Limited to audio context | [SETU](papers/2026-08-31/2608.27524-SETU-An-Agentic-Ecosystem-for-Multilingual-Persona.html) |
| **Omni-Modal** | Text + Image + Audio + Video | Unified processing | Complex training, expensive | Emerging research |
| **Document Understanding** | Scanned docs + Text | Tables, charts, layouts | OCR errors, layout complexity | [From Documents to Reasoning](papers/2026-08-31/2608.27919-From-Documents-to-Reasoning-A-Validated-Synthetic.html) |

## Safety Approaches

| Approach | What It Addresses | Strength | Limitation | Example Papers |
|----------|-------------------|----------|------------|----------------|
| **Trusted Tool Boundaries** | Agent overreach | Clear enforcement points | Requires careful boundary design | [If Agents Were Angels](papers/2026-08-31/2608.27646-If-Agents-Were-Angels-No-Governance-Would-Be-Neces.html) |
| **Intent-Aligned Retrieval** | Malicious queries | Small models (22M) outperform large ones | Requires intent classification | [Cross-Session Decomposition Attacks](papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) |
| **Multimodal Safety Moderation** | Harmful content across modalities | Comprehensive (image, text, audio) | Policy definition is hard | [Nemotron 3.5](papers/2026-08-31/2608.27548-Nemotron-35-Content-Safety-Moderator-A-Compact-Mul.html) |
| **Compositional Safety** | Benign queries combined into harmful objectives | Addresses cross-session risks | Hard to detect, fundamental scaling issue | [Cross-Session Decomposition Attacks](papers/2026-08-31/2608.27945-Cross-Session-Decomposition-Attacks-Scaling-Risk-a.html) |

## Efficiency Methods

| Method | Token Savings | Accuracy Impact | Deployment Complexity | Example Papers |
|--------|---------------|-----------------|----------------------|----------------|
| **Early Exit (SABER)** | 30-40% | None (same accuracy) | Low (training-free) | [SABER](papers/2026-08-31/2608.27963-SABER-Stability-Aware-Early-Exit-for-LLM-Reasoning.html) |
| **Complexity-Aware Penalties** | 25-50% | Same or better | Medium (requires retraining) | [Thinking Costs Tokens](papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) |
| **Token Budget Thresholds** | Varies | Avoids overhead harm | Low (inference-time) | [Thinking Costs Tokens](papers/2026-08-31/2608.27506-Thinking-Costs-Tokens-When-More-Structure-is-Worth.html) |
| **Mixture-of-Experts (MoE)** | Significant (sparse activation) | Same or better | High (complex architecture) | [CoRe-MoE](papers/2026-08-31/2608.27867-CoRe-MoE-Compact-Reusable-MoE-for-Continual-Multim.html) |

## Decision Matrices

### Which reasoning method should I use?

```
Is your task simple (factual recall, simple classification)?
├─ Yes → Direct generation (no reasoning needed)
└─ No → Is accuracy critical?
    ├─ Yes → Is cost a concern?
    │   ├─ Yes → Early Exit (SABER) — save 30-40% tokens
    │   └─ No → Tree-of-Thought or Self-Consistency
    └─ No → Chain-of-Thought (good balance)
```

### Which retrieval method should I use?

```
Do you know the exact search terms?
├─ Yes → Sparse retrieval (BM25)
└─ No → Is your data structured (entities, relations)?
    ├─ Yes → Knowledge Graphs
    └─ No → Do you need high precision?
        ├─ Yes → Hybrid search + Re-ranking
        └─ No → Dense retrieval (embeddings)
```

### Which agent architecture should I use?

```
Is your task single-step or multi-step?
├─ Single-step → Simple tool-use agent
└─ Multi-step → Does it involve visual/spatial reasoning?
    ├─ Yes → Embodied agent with world models
    └─ No → Does it span multiple domains?
        ├─ Yes → Multi-agent system
        └─ No → ReAct agent with planning
```

## Performance Tradeoffs

| Factor | Improve By... | Cost |
|--------|---------------|------|
| **Accuracy** | More reasoning steps, verification, RAG | Higher token costs, slower inference |
| **Speed** | Early exit, sparse retrieval, simpler models | May sacrifice accuracy |
| **Cost** | Early exit, token budgets, small specialized models | May limit capabilities |
| **Safety** | Governance boundaries, intent filtering, moderation | Added complexity, potential false positives |
| **Flexibility** | Multi-agent systems, tool use, hybrid retrieval | Harder to debug, coordinate |

**Key insight**: There's no free lunch. Every improvement comes with tradeoffs. The art is in choosing the right balance for your use case.
