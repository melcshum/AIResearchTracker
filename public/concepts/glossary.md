---
title: "AI Concepts Glossary"
---

Quick reference for key terms across all research areas. See also [Papers by Concept](papers-by-concept.html) to find papers that use these concepts.

## Agent Concepts

**AI Agent**  
An autonomous system that perceives its environment, reasons about goals, and takes actions through tools or APIs to accomplish tasks.

**Tool Use**  
An agent's ability to call external APIs, execute code, browse the web, or interact with systems beyond text generation.

**Planning**  
Breaking complex goals into sequential steps, often with verification and backtracking when plans fail.

**ReAct**  
A reasoning paradigm that interleaves thinking (Reason) and acting (Act) in iterative cycles: think → act → observe → think again.

**World Models**  
Internal representations of environment dynamics that enable predictive planning without real-world interaction. The agent simulates outcomes before committing to actions.

**Multi-Agent Coordination**  
Multiple specialized agents collaborating through message-passing, shared memory, or hierarchical control to solve complex tasks.

**Embodied Agent**  
An agent operating in a simulated or physical environment (GUI automation, robotics) that must handle spatial reasoning and continuous state.

**Compositional Safety**  
The risk that benign subtasks, when reassembled across sessions or contexts, can create harmful objectives — a scaling law for agent safety.

## Reasoning Concepts

**Chain-of-Thought (CoT)**  
Step-by-step reasoning where models show their work, improving accuracy on complex tasks like math, logic, and planning.

**Self-Consistency**  
Sampling multiple reasoning paths and selecting the most consistent answer, reducing the chance of one-off errors.

**Tree-of-Thought**  
Exploring a tree of reasoning branches, pruning dead ends and backtracking when needed — closer to human problem-solving than linear chains.

**Verification**  
Checking intermediate steps or final outputs for correctness before committing, often using tool execution or self-reflection.

**Early Exit**  
Stopping reasoning when the answer stabilizes across steps, reducing token costs without sacrificing accuracy.

**Token Budget**  
The computational resources allocated for reasoning. Below certain thresholds, planning overhead hurts more than it helps.

**Adversarial Branch Probing**  
Constructing semantic perturbations around intermediate reasoning states to estimate stability — used for early exit decisions.

**Complexity-Aware Penalties**  
RL training with penalties for redundant reasoning steps, reducing verbosity while preserving accuracy.

## Retrieval Concepts

**rag" onclick="window.location.href='wiki.html'">rag" onclick="window.location.href='wiki.html'">Retrieval-Augmented Generation</span></span> (RAG)**  
Combining information retrieval with text generation: retrieving relevant documents at inference time and using them to ground responses, reducing hallucination.

**retrieval" onclick="window.location.href='wiki.html'">retrieval" onclick="window.location.href='wiki.html'">Dense Retrieval</span></span>**  
Using learned embedding" onclick="window.location.href='wiki.html'">embedding" onclick="window.location.href='wiki.html'">embeddings</span></span> (e.g., BGE, E5, GTE) to find semantically similar documents, mapping queries and documents into a shared vector space.

**Sparse Retrieval**  
Traditional methods like BM25 that match on lexical overlap — fast, interpretable, and surprisingly robust for keyword-based search.

**Hybrid Search**  
Combining retrieval" onclick="window.location.href='wiki.html'">retrieval" onclick="window.location.href='wiki.html'">dense retrieval</span></span> with sparse methods to get semantic understanding plus keyword precision.

**Re-ranking**  
A second-stage model that re-scores retrieved candidates for higher precision after initial retrieval.

**Knowledge Graph**  
Structured representations of entities and relationships that complement vector retrieval with explicit, auditable reasoning.

**Agentic RAG**  
An agent decides when to retrieve, what to retrieve, and how to use results — rather than a fixed retrieve-then-generate pipeline.

**Query Transformation**  
Rewriting, decomposing, or expanding queries before retrieval (e.g., HyDE, multi-query, step-back prompting) to improve recall.

**Citation & Attribution**  
Linking generated claims back to specific source documents for verifiability and trust.

## Multi-Modal Concepts

**Vision-Language Model (VLM)**  
A model that processes both images and text, enabling visual question answering, captioning, and cross-modal reasoning. Examples: LLaVA, GPT-4V, Gemini.

**Cross-Modal Reasoning**  
Drawing inferences across different modalities — using visual context to inform text generation, or audio to inform visual understanding.

**Contrastive Learning**  
Training method that aligns representations across modalities (e.g., CLIP matches images to text descriptions in a shared embedding space).

**Mixture-of-Experts (MoE)**  
Using specialized expert sub-networks for different modalities or tasks, enabling efficient scaling without activating all parameters for every input.

**Catastrophic Forgetting**  
The tendency of neural networks to lose previously learned knowledge when trained on new tasks — a major challenge in continual learning.

**Grounded Generation**  
Producing outputs tied to specific regions of an image, moments in a video, or spans in a document — enabling verifiable, locatable outputs.

**Multimodal Safety**  
Content moderation across images, documents, screenshots, and audio under domain-varying policies — moving beyond text-only guardrails.

**Document Understanding**  
Reading and reasoning about scanned documents, charts, tables, and screenshots — combining OCR, layout analysis, and semantic understanding.
