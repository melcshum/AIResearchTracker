---
title: "From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction"
authors: 
  - name: "Research Team"
    affiliation: "AI Education Research"
date: "2026-09-02"
categories:
  - AI in Education
  - Knowledge Construction
  - Human-AI Interaction
  - Personal Knowledge Management
  - Metacognition
tags:
  - learner-in-the-loop
  - AI wiki
  - knowledge construction
  - writing-to-learn
  - metacognition
  - self-regulated learning
  - cognitive offloading
  - epistemic agency
paper-type: "conference-paper"
venue: "To Be Submitted"
status: "Draft"
abstract: |
  Generative artificial intelligence (GenAI) has substantially reduced the effort required to produce summaries, explanations, structured notes, and other learning artefacts. Although such capabilities can increase access to information and provide timely instructional support, they also introduce a pedagogical tension: the same cognitive activities that GenAI can efficiently automate, including explaining, organising, connecting, and reformulating information, may themselves constitute important processes through which learning occurs. This paper proposes an AI Wiki Companion, a learner-in-the-loop personal knowledge environment designed to position GenAI as a metacognitive and formative scaffold rather than as a substitute knowledge producer.

keywords:
  - generative artificial intelligence
  - knowledge construction
  - learner-in-the-loop
  - writing-to-learn
  - metacognition
  - self-regulated learning
  - personal wiki
  - cognitive offloading
  - AI in education
---

::: {.conference-paper-header}
## 📄 Conference Paper

**Title:** From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction

**Status:** Draft (To Be Submitted)

**Date:** September 2, 2026

**Categories:** AI in Education, Knowledge Construction, Human-AI Interaction, Personal Knowledge Management, Metacognition
:::

---

## 📋 Abstract

Generative artificial intelligence (GenAI) has substantially reduced the effort required to produce summaries, explanations, structured notes, and other learning artefacts. Although such capabilities can increase access to information and provide timely instructional support, they also introduce a pedagogical tension: the same cognitive activities that GenAI can efficiently automate, including explaining, organising, connecting, and reformulating information, may themselves constitute important processes through which learning occurs. This paper proposes an AI Wiki Companion, a learner-in-the-loop personal knowledge environment designed to position GenAI as a metacognitive and formative scaffold rather than as a substitute knowledge producer. Drawing on writing-to-learn, knowledge construction, metacognition, self-regulated learning, personal knowledge management, and human-in-the-loop perspectives, the framework treats learner-authored wiki entries as evolving external representations of understanding. Four design principles guide the proposed system: DP1 Learner Ownership, DP2 Scaffold Rather Than Substitute, DP3 Reflection Before Correction, and DP4 Continuous Knowledge Integration. These principles are operationalised through a five-stage cycle comprising Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend. A complementary Prompt Before Provide interaction model encourages learners to articulate and evaluate their existing understanding before receiving direct AI-generated explanations. The paper further specifies a system architecture integrating a Wiki Editor, Personal Knowledge Base, Concept Graph, Knowledge Context, and AI Companion, together with a formative evaluation framework examining conceptual understanding, knowledge-artefact development, learner responses to AI scaffolding, and perceived usefulness. The proposed approach contributes a design perspective for educational GenAI in which technological assistance is deliberately organised around preserving epistemic agency and productive cognitive engagement.

---

## 🔑 Keywords

generative artificial intelligence; knowledge construction; learner-in-the-loop; writing-to-learn; metacognition; self-regulated learning; personal wiki; cognitive offloading; AI in education

---

## 1. Introduction

### 1.1 From Information Access to Knowledge Construction

Generative artificial intelligence has transformed the conditions under which learners locate, organise, and interact with information. Contemporary large language models can rapidly summarise readings, explain unfamiliar concepts, generate examples, compare theoretical perspectives, formulate questions, and produce coherent notes. From an accessibility and efficiency perspective, these capabilities provide considerable educational value. They can reduce barriers to information access, provide immediate assistance, and potentially extend learning support beyond the temporal and practical constraints of conventional teaching environments.

The educational significance of these capabilities, however, cannot be assessed solely in terms of efficiency. Access to well-organised information does not necessarily imply that knowledge has been meaningfully constructed by the learner. Research on active and constructive learning has consistently distinguished between receiving information and engaging cognitively with that information. Meaningful understanding requires learners to select relevant information, organise conceptual representations, integrate new ideas with prior knowledge, identify relationships, evaluate competing explanations, retrieve knowledge from memory, and apply that knowledge in unfamiliar circumstances.

Writing has traditionally provided one mechanism through which some of these processes become visible. When learners explain a concept in their own words, they externalise aspects of their current mental model. The resulting artefact can expose conceptual gaps, uncertain relationships, and misconceptions that may remain concealed when information is merely read or copied. Writing can therefore function not simply as documentation of learning but as an activity through which understanding is progressively articulated and reorganised.

Nevertheless, digital note-taking practices do not inherently produce such constructive engagement. Notes may become repositories into which information is copied, stored, and rarely reconsidered. A simplified representation of this behaviour is **Read → Copy → Store → Rarely Revisit**. GenAI potentially introduces an even more efficient version of the same problem: **Ask AI → Generate Summary → Save Summary**. In the latter workflow, a polished and apparently coherent knowledge artefact may be produced with relatively little requirement for the learner to decide what is important, formulate an explanation, identify conceptual relationships, or evaluate the validity of the resulting text.

The issue is not that AI-generated summaries or explanations are intrinsically educationally undesirable. Rather, the concern is one of **cognitive substitution**. Cognitive offloading can be beneficial when external tools release limited cognitive resources for more demanding tasks, but it can become pedagogically problematic when the process being offloaded is itself an intended object of learning. A learner who delegates conceptual organisation, explanation, and synthesis to an AI system may obtain a high-quality artefact without necessarily engaging in the corresponding cognitive activity.

This tension motivates the central question addressed by the present work:

> **How can generative AI support knowledge construction without performing the knowledge-construction process for the learner?**

The paper argues that educational GenAI should not be evaluated only according to what it can generate for learners. An equally important design question concerns which forms of intellectual activity should deliberately remain under learner control because performing those activities contributes to learning.

### 1.2 Personal Wikis as Environments for Developing Knowledge

The proposed approach addresses this problem through a personal wiki environment. Unlike conventional linear notes, a personal wiki can represent knowledge as an evolving network of learner-generated concepts. Individual entries can be revised, linked, reorganised, and extended as understanding develops. Hyperlinks, backlinks, tags, revision histories, and graphical representations of conceptual relationships allow knowledge to be treated as interconnected rather than as a sequence of isolated documents.

This characteristic is educationally significant because learning frequently requires new information to be interpreted in relation to existing knowledge. The value of a personal wiki therefore lies not simply in external storage. It can function as an evolving external representation of the learner's current knowledge structure. A learner studying machine learning, for example, might initially create separate entries for overfitting, generalisation, and model evaluation. Later encounters with regularisation or cross-validation can provide occasions to revise earlier explanations and construct new relationships among these concepts.

The present work draws inspiration from linked-note and personal knowledge management environments such as Obsidian, particularly their use of persistent Markdown documents, hyperlinks, backlinks, tags, and concept graphs. The contribution is not, however, tied to a specific commercial platform. The personal wiki is conceptualised more generally as an HCI environment in which learner-generated representations of knowledge persist over time and provide contextual material for subsequent AI-supported reflection.

### 1.3 From AI Content Generation to AI-Supported Knowledge Construction

The AI Wiki Companion proposed in this paper adopts a deliberately constrained pedagogical role for GenAI. Rather than treating AI primarily as an answer generator or automatic note writer, the system positions it as a source of metacognitive prompts, Socratic questioning, formative feedback, knowledge-gap identification, conceptual challenges, and connection recommendations. The purpose of AI intervention is consequently not always to minimise the effort required to complete a task. In some interactions, the system deliberately returns intellectual work to the learner.

The core principle can be expressed as follows:

> **The learner constructs the knowledge; AI scaffolds the construction process.**

This principle establishes a division of epistemic responsibility between learner and system. The AI may identify a potentially missing connection, question the coherence of an explanation, or recommend that an earlier wiki entry be reconsidered. The learner nevertheless retains responsibility for determining whether the suggestion is valid, whether the knowledge artefact should be changed, and how that change should be expressed. Such an arrangement extends human-in-the-loop thinking into a specifically educational form of **learner-in-the-loop knowledge construction**, in which the learner retains epistemic agency over the representation and revision of personal knowledge.

The paper makes three related contributions:
1. **First**, it develops a pedagogically grounded learner-in-the-loop model that conceptualises GenAI as a scaffold for active knowledge construction.
2. **Second**, it operationalises this model through four design principles, a five-stage knowledge-construction cycle, and the Prompt Before Provide interaction mechanism.
3. **Third**, it proposes an architecture and evaluation approach through which the relationship among AI scaffolding, learner decision-making, knowledge-artefact revision, and conceptual understanding can be empirically examined.

### 1.4 Research Questions

The study is guided by the following research questions:

**RQ1. Design:** How can a learner-in-the-loop AI wiki be designed to support active knowledge construction while maintaining learner agency?  
*RQ1 examines how the theoretical principles of learner ownership, scaffolding, reflection, and continuous knowledge integration can be operationalised through the design of the AI Wiki Companion.*

**RQ2. Learning:** To what extent does the proposed AI Wiki Companion support students' knowledge construction and conceptual understanding?  
*RQ2 investigates whether engagement with the proposed environment is associated with changes in conceptual understanding and the quality of learner-generated knowledge artefacts.*

**RQ3. Human-AI Interaction:** How do learners evaluate and act upon AI-generated scaffolding during the construction and revision of their personal knowledge artefacts?  
*RQ3 focuses on the learner-in-the-loop mechanism itself. It examines how learners respond to AI-generated questions, challenges, gap identifications, and connection recommendations, including whether suggestions are accepted, rejected, modified, or independently resolved.*

**RQ4. Learner Experience:** How do students perceive the usefulness of AI-supported reflection, feedback, and knowledge linking during wiki-based learning?  
*RQ4 examines learners' perceptions of the AI Wiki Companion, including perceived usefulness, learner control, reflective support, cognitive engagement, and potential dependency on AI.*

Together, the four questions provide a progression from **design → learning → interaction → experience**, enabling the proposed system to be evaluated not only in terms of whether it supports learning, but also in terms of how AI scaffolding influences learner activity and how that support is experienced.

---

## 2. Theoretical Background and Related Work

### 2.1 Writing-to-Learn and Active Knowledge Construction

The theoretical foundation of the proposed approach begins with the proposition that writing can function as a cognitive activity rather than merely as a means of recording completed thought. Writing-to-learn research has examined how the production of explanations, summaries, learning journals, and other written artefacts can require learners to select information, organise ideas, establish conceptual relationships, and make implicit understanding explicit.

From a knowledge-construction perspective, this externalisation process is important because it creates an inspectable representation of the learner's current understanding. A concept that appears familiar while being read may prove more difficult to explain independently. Similarly, attempting to connect two ideas in writing may expose ambiguity about their underlying relationship. The production of a learner-authored wiki entry can therefore operate as an epistemic activity through which understanding is articulated, tested, and progressively reorganised.

However, writing alone should not be assumed to guarantee meaningful learning. The educational effect depends on the nature of the writing activity and on whether learners engage in cognitively productive processes such as elaboration, organisation, monitoring, and revision. This observation is particularly relevant to the design of AI-supported learning. If GenAI produces the explanation before the learner has attempted to formulate one, the visible written artefact may no longer provide reliable evidence of the learner's own conceptual representation.

Consequently, the proposed AI Wiki Companion gives priority to **learner-generated initial representations**. AI support is introduced around and after the learner's constructive activity rather than automatically preceding it.

### 2.2 Metacognition and Self-Regulated Learning

Knowledge construction also depends on learners' ability to monitor and regulate their own understanding. Metacognition encompasses awareness of one's cognitive state as well as processes through which learners evaluate comprehension, recognise uncertainty, select strategies, and determine when further learning is required. These functions are closely associated with self-regulated learning (SRL), within which learners iteratively plan, perform, monitor, and adapt learning activity.

A learner may possess an incomplete explanation without recognising that it is incomplete. Effective scaffolding therefore requires more than correction. It should encourage the learner to detect and interpret the discrepancy between present understanding and a more adequate conceptual representation. Questions such as *"Which part of this explanation are you least confident about?"*, *"What evidence supports this statement?"*, or *"Can you explain this concept without referring to your note?"* can stimulate metacognitive monitoring without immediately supplying the missing content.

GenAI is potentially well suited to this form of context-sensitive prompting because prompts can be generated in relation to the learner's current artefact rather than delivered as generic reflective questions. Nevertheless, the educational quality of such support depends on interaction design. An AI system that detects a weakness and immediately rewrites the corresponding paragraph may resolve the textual problem while bypassing the learner's opportunity to monitor and regulate understanding. The proposed framework therefore emphasises **reflection before correction**, treating AI feedback as a prompt for learner regulation rather than as an automatic repair mechanism.

This perspective also resonates with scaffolding within sociocultural accounts of learning, in which assistance is most productive when it enables learners to perform cognitive activity that would otherwise be difficult while progressively preserving or increasing learner responsibility. The analogy should not be interpreted as equating an LLM with a human teacher or more knowledgeable other. Rather, it provides a theoretical lens for considering how adaptive prompts might support productive learner activity without eliminating that activity.

### 2.3 Personal Wikis and Networked Knowledge Environments

Personal knowledge management systems provide an external environment in which learners can store, organise, link, and revisit information over extended periods. Whereas conventional notes are often structured around lectures, documents, or chronological sequences, wiki-style environments allow individual concepts to become persistent entities that can be connected across contexts.

From an educational perspective, this persistence supports an important shift from **note accumulation to knowledge evolution**. A learner may initially represent concepts as isolated entries but progressively develop a more relational structure as understanding grows. Backlinks and concept graphs can make these relationships visible, while revision histories provide evidence of how conceptual representations change over time.

Such environments may therefore support the externalisation of mental models. A knowledge graph displayed by the system should not be interpreted as a direct representation of cognition, but it can reveal aspects of how a learner has chosen to organise and connect concepts. These external representations can subsequently become objects for reflection and discussion.

The AI Wiki Companion extends this affordance by using the learner's existing knowledge base as part of the context for AI intervention. Rather than responding only to the current page, the system can identify potentially relevant prior entries and encourage the learner to consider whether new knowledge modifies, contradicts, or extends earlier understanding. This longitudinal orientation distinguishes the proposed approach from many conversational AI interactions that primarily respond to the immediate prompt.

### 2.4 Generative AI as Formative and Metacognitive Scaffolding

GenAI applications in education have frequently been investigated as tutors, writing assistants, content generators, assessment aids, and feedback systems. These applications demonstrate several potentially valuable affordances, including responsiveness, scalability, conversational interaction, and the ability to generate personalised explanations or feedback. At the same time, concerns have been raised regarding hallucination, automation bias, over-reliance, inaccurate feedback, and the possibility that students may outsource reasoning or writing processes to AI.

The distinction between **formative scaffolding and content substitution** is therefore central to the proposed design. Consider a learner who writes that increasing model complexity necessarily increases model performance. An AI system operating as an automatic editor might replace this statement with a more technically accurate explanation. A scaffolding-oriented system could instead ask: *"Does increasing model complexity always improve performance on unseen data? Under what conditions might the opposite occur?"* The second response leaves the epistemic problem unresolved long enough for the learner to engage with it.

This design logic is related to Socratic tutoring approaches, in which questioning is used to stimulate explanation, justification, comparison, and reconsideration rather than immediately providing conclusions. However, GenAI introduces both opportunities and risks. Its flexibility permits questions to be generated dynamically from learner-authored material, but the quality and factual reliability of those prompts cannot be assumed. Human judgement, source verification, and appropriate system guardrails therefore remain necessary.

### 2.5 Learner-in-the-Loop Knowledge Construction

Human-in-the-loop approaches are generally concerned with retaining meaningful human oversight within computational decision processes. For educational contexts, a more specific concern is whether the learner continues to exercise **epistemic agency**: the capacity to formulate, evaluate, justify, and revise claims about what is known.

The proposed learner-in-the-loop model treats AI output as provisional input to learner judgement. A suggestion does not directly become part of the personal knowledge base. Instead, the interaction follows a conceptual sequence of **Construct → Judge Feedback → Revise Ideas → Accept / Reject AI → Apply Knowledge**. In this sequence, AI may influence the learner's reasoning, but the learner remains responsible for deciding whether and how an artefact is revised.

This distinction becomes particularly important when AI-generated information is plausible but incorrect. A system that automatically integrates AI-generated content into a student's wiki could amplify errors and weaken the relationship between the artefact and the learner's own understanding. Requiring explicit learner evaluation introduces cognitive friction, but such friction may be educationally productive when it encourages verification and justification.

The learner-in-the-loop concept therefore functions simultaneously as a pedagogical principle and an HCI design constraint. It requires interaction mechanisms that make AI intervention visible, contestable, and reversible, while preventing suggestions from being silently incorporated into learner-authored knowledge.

### 2.6 Research Gap

Taken together, writing-to-learn, metacognitive regulation, personal knowledge environments, and AI-supported feedback provide important theoretical components for the proposed approach. However, these areas are frequently treated separately. Writing-to-learn research typically focuses on the cognitive consequences of producing written explanations; personal knowledge management research examines external organisation and retrieval; and GenAI research increasingly investigates immediate feedback, tutoring, or content generation.

Comparatively less attention has been directed towards GenAI systems explicitly designed around **persistent learner-generated knowledge artefacts** and the longitudinal processes through which those artefacts are constructed, questioned, connected, revised, retrieved, and applied.

The research gap is therefore not simply an absence of AI-supported note-taking systems. The more specific gap concerns the design of AI support that deliberately preserves the learner's role as the primary constructor and evaluator of knowledge while using generative capabilities to stimulate productive cognitive and metacognitive activity.

The AI Wiki Companion addresses this gap through four design principles and an iterative five-stage model of AI-supported knowledge construction.

---

## 3. Proposed AI Wiki Companion

### 3.1 Design Rationale

The proposed AI Wiki Companion is conceptualised as a personal learning environment rather than as an automated knowledge-production tool. Its design seeks to maintain an intentional asymmetry between learner and AI responsibilities. The learner authors explanations, determines conceptual relationships, evaluates feedback, and decides how knowledge should be revised. The AI Companion provides adaptive prompts intended to expose gaps, elicit explanation, provoke reconsideration, and connect current activity with prior knowledge.

**Table 1. Design principles of the AI Wiki Companion**

| Design Principle | Definition | Pedagogical Rationale | Intended System Implication |
|------------------|------------|----------------------|----------------------------|
| **DP1. Learner Ownership** | The learner authors and retains control over the primary knowledge artefact. | Preserves epistemic agency and ensures that the personal wiki represents learner-mediated understanding rather than unexamined AI output. | AI-generated suggestions require explicit learner judgement before incorporation; the system does not silently overwrite learner-authored text. |
| **DP2. Scaffold Rather Than Substitute** | AI supports cognitive activity without automatically performing learning-relevant intellectual work on the learner's behalf. | Reduces inappropriate cognitive substitution and retains opportunities for explanation, reasoning, synthesis, and retrieval. | When appropriate, AI provides prompts, hints, questions, or partial scaffolds before complete explanations. |
| **DP3. Reflection Before Correction** | Learners are encouraged to inspect and reconsider their reasoning before direct correction is supplied. | Supports metacognitive monitoring and SRL by making discrepancies in understanding an object of learner attention. | Potential misconceptions or incomplete explanations initially trigger reflective questions rather than automatic rewriting. |
| **DP4. Continuous Knowledge Integration** | New learning is related to previously constructed knowledge and may trigger revision of earlier representations. | Supports cumulative and relational knowledge development rather than isolated task completion. | The system retrieves relevant prior entries and recommends relationships, contradictions, or opportunities for revision. |

These principles are not intended to prohibit direct AI assistance. There are circumstances in which explicit explanation is appropriate and efficient. The design question is instead whether immediate provision of a completed answer would displace cognitive activity that the learning task was intended to elicit. The proposed framework therefore makes the timing and form of AI assistance pedagogically consequential.

### 3.2 AI-Supported Knowledge Construction Cycle

The four design principles are operationalised through the five-stage **Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend** cycle. The cycle is recursive rather than strictly linear. A learner may return to an earlier stage when reflection reveals insufficient understanding, when application exposes a misconception, or when new material requires an existing wiki entry to be reconsidered.

**Table 2. Five-stage AI-supported knowledge construction cycle**

| Stage | Primary Learner Activity | AI Companion Role | Intended Learning Process |
|-------|-------------------------|-------------------|--------------------------|
| **Construct** | Develops an initial explanation, example, representation, or conceptual relationship in the personal wiki. | Maintains limited intervention and may provide task framing without constructing the artefact. | Externalisation, generative processing, activation of prior knowledge. |
| **Reflect** | Examines confidence, completeness, assumptions, and explanatory adequacy. | Generates metacognitive and Socratic prompts grounded in the learner's artefact. | Metacognitive monitoring and self-evaluation. |
| **Scaffold** | Responds to identified gaps, challenges, or possible misconceptions. | Provides targeted questions, hints, connection suggestions, and evidence prompts. | Elaborative processing, conceptual restructuring, guided reasoning. |
| **Consolidate & Apply** | Retrieves, explains, compares, predicts, solves, or transfers knowledge to a new context. | Generates retrieval and application tasks and provides subsequent formative feedback. | Retrieval practice, consolidation, transfer, evaluative judgement. |
| **Revisit & Extend** | Integrates new concepts with previously constructed knowledge and revises earlier entries where appropriate. | Identifies potentially relevant prior knowledge and prompts comparison, integration, or revision. | Longitudinal integration and cumulative knowledge construction. |

#### 3.2.1 Construct

The Construct stage establishes learner authorship as the starting condition of the interaction. Rather than asking AI to generate a complete knowledge entry, the learner first articulates a concept using existing knowledge and available learning resources. This may involve writing an explanation, providing an example, identifying relevant evidence, or linking the concept to an existing wiki page.

For example, a learner encountering overfitting may initially write that a model overfits when it learns the training data too closely. Although incomplete, this representation provides evidence of the learner's present understanding. Premature AI rewriting would remove the opportunity to examine that representation. AI involvement is consequently restricted during initial construction unless assistance is required to overcome a barrier that would otherwise prevent meaningful participation.

#### 3.2.2 Reflect

During Reflect, the learner is encouraged to inspect the adequacy of the constructed artefact before receiving substantive correction. Contextual prompts may ask which part of an explanation is least certain, whether the learner can restate the concept without consulting the wiki, what assumptions underpin the explanation, or whether a counterexample can be generated.

The purpose is to encourage metacognitive monitoring and to establish a discrepancy, where appropriate, between what the learner currently believes and what additional understanding may be required. This stage gives operational form to **DP3, Reflection Before Correction**, and is intended to reduce the tendency for AI feedback to become passively consumed evaluative information.

#### 3.2.3 Scaffold

The Scaffold stage introduces more explicit AI support after the learner's current representation and reflection are available. The AI Companion may identify an omitted concept, challenge a weak relationship, highlight a potentially questionable assumption, ask for evidence, or suggest that another wiki entry is conceptually relevant.

If the learner explains overfitting without referring to generalisation, for instance, the system may ask how the two concepts are related. If regularisation has been linked to overfitting, the AI may request an explanation of why the relationship exists rather than treating the hyperlink itself as evidence of understanding. When a possible misconception is detected, the system frames it as an epistemic problem to be investigated.

This mode of interaction conceptualises AI feedback as a trigger for further cognition rather than as a replacement artefact.

#### 3.2.4 Consolidate & Apply

The Consolidate & Apply stage recognises that possession of an accurate written note does not necessarily demonstrate retrievable or transferable understanding. Learners are therefore required to use knowledge independently of the stored artefact. Tasks may involve free recall, explanation, comparison, prediction, problem solving, or application to a novel situation.

For example, after developing an entry on overfitting, a learner might first be asked to explain the concept without consulting the wiki. The system could subsequently present a scenario in which training accuracy is substantially higher than test accuracy and ask the learner to diagnose the problem and compare possible interventions. Such progression creates a distinction between the quality of the external artefact and the learner's capacity to use the represented knowledge.

#### 3.2.5 Revisit & Extend

The Revisit & Extend stage differentiates the proposed model from one-off AI-assisted writing. The personal knowledge base persists across learning episodes. When a learner later adds cross-validation, for example, the AI Companion may retrieve earlier entries on overfitting, generalisation, train-test split, and model evaluation. Rather than automatically creating new links, it can ask whether and how the new concept modifies the learner's earlier understanding.

Knowledge construction is therefore treated as cumulative and revisable. Earlier explanations are not regarded as completed products but as representations that may require refinement when the learner encounters new evidence, theoretical perspectives, or applications.

### 3.3 Prompt Before Provide

The **Prompt Before Provide** interaction model provides a concrete HCI mechanism for implementing the broader scaffold-rather-than-substitute principle. The mechanism applies particularly when the learner requests information about a concept that is itself an appropriate object of retrieval or explanation.

For example, when a learner asks, *"What is polymorphism?"*, a conventional conversational assistant may immediately provide a definition. Under Prompt Before Provide, the AI Companion may first ask the learner to describe their present understanding in two or three sentences. The subsequent system response can then be calibrated to the learner-generated representation.

Prompt Before Provide is not intended as an absolute prohibition against direct instruction. Requiring prior production in every interaction could increase unnecessary cognitive load, frustrate learners, or become pedagogically inappropriate when prerequisite knowledge is absent. Instead, the mechanism represents an adaptive default when learner retrieval, explanation, or self-assessment is itself educationally valuable.

The approach therefore seeks to balance two forms of support: **productive effort**, in which learners are given sufficient opportunity to reason, retrieve, and construct; and **instructional assistance**, in which AI supplies information when additional learner effort is unlikely to be educationally productive.

### 3.4 Core AI Companion Functions

The pedagogical framework is translated into a set of AI functions detailed in Table 3. These functions are organised according to the cognitive or metacognitive activity they are intended to stimulate rather than according to the generative capability of the underlying model.

**Table 3. AI Wiki Companion functions and intended learning roles**

| AI Wiki Function | Intended Learning Role | Illustrative Intervention |
|------------------|----------------------|--------------------------|
| **Socratic Questioning** | Elicit explanation, justification, comparison, and reasoning. | "Why does this relationship hold?" |
| **Knowledge Gap Detection** | Draw attention to concepts or relationships that may be incomplete. | "Your explanation discusses training performance but not generalisation. Is anything missing?" |
| **Connection Recommendation** | Encourage integration of new and existing knowledge. | "Could this concept be related to your earlier entry on the bias–variance trade-off?" |
| **Misconception Challenge** | Prompt reconsideration of potentially inaccurate reasoning. | "Would this claim remain true for unseen data?" |
| **Evidence Prompting** | Encourage verification and justification of knowledge claims. | "What source or evidence supports this statement?" |
| **Retrieval & Application Questions** | Promote recall, consolidation, and transfer. | "Explain the concept without consulting the wiki, then apply it to this scenario." |
| **Review/Revisit Recommendation** | Encourage longitudinal refinement of earlier knowledge. | "Does what you have just learned require your earlier model-evaluation entry to be revised?" |
| **Source Recommendation** | Direct the learner towards potentially relevant evidence while preserving verification responsibility. | "This source may be relevant. Verify its claims before integrating it into your wiki." |

Source recommendation warrants particular caution because LLM-generated citations and resource descriptions may be inaccurate. The learner must therefore verify recommended material before incorporating it into the personal knowledge base. Where technically feasible, retrieval should be grounded in verified scholarly databases or instructor-approved corpora rather than unconstrained model generation.

### 3.5 Conceptual System Architecture

The proposed architecture consists of the **Wiki Editor**, **Personal Knowledge Base**, **Concept Graph**, **Knowledge Context**, and **AI Companion**.

The **Wiki Editor** constitutes the primary learner-facing authoring environment. It supports the creation and revision of knowledge entries while making AI-generated interventions distinguishable from learner-authored text. Revision histories should preserve changes over time, enabling both learner reflection and research analysis.

The **Personal Knowledge Base** stores learner-generated explanations, examples, tags, evidence, links, and previous revisions. It functions as the persistent substrate through which the system supports longitudinal knowledge development.

The **Concept Graph** represents explicit relationships among wiki entries. These relationships may arise from learner-created links or system-detected candidate associations. Importantly, automatically detected associations remain recommendations until learners determine whether they constitute meaningful conceptual relationships.

The **Knowledge Context** component selects relevant information from the Personal Knowledge Base and Concept Graph for a particular AI interaction. Context selection is necessary because an unconstrained personal knowledge base may exceed model context limits and may contain material irrelevant to the immediate learning task. Retrieval should therefore prioritise conceptually related entries, recent revisions, prerequisite concepts, and previously identified misconceptions.

Finally, the **AI Companion** uses the selected Knowledge Context together with the learner's current artefact and interaction history to determine an appropriate scaffolding response. Depending on the stage of the knowledge-construction cycle, this response may take the form of a reflective prompt, Socratic question, misconception challenge, connection recommendation, retrieval task, or application problem.

The architecture can be represented conceptually as:

```
Learner → Wiki Editor → Personal Knowledge Base → Concept Graph → Knowledge Context → AI Companion → Scaffold → Learner Evaluation → Wiki Revision
```

Crucially, the final transition returns to the learner rather than directly to the Personal Knowledge Base. This design choice operationalises learner-in-the-loop control: AI recommendations must be interpreted and acted upon by the learner before they become part of the persistent knowledge artefact.

---

## 4. Proposed Formative Evaluation

### 4.1 Evaluation Purpose

The initial evaluation should be framed as a formative investigation of the framework and prototype rather than as definitive evidence of long-term learning effectiveness. Its purpose is to examine whether the proposed interaction mechanisms are usable, whether learners engage with AI scaffolding as intended, and whether preliminary changes can be observed in conceptual understanding and learner-generated knowledge artefacts.

A mixed-method design is appropriate because the research concerns both outcomes and processes. Quantitative measures can capture changes in conceptual performance and artefact characteristics, while interaction logs and qualitative accounts can clarify how learners interpret and respond to AI intervention.

### 4.2 Participants and Learning Context

The prototype may initially be evaluated with undergraduate learners studying a bounded conceptual domain such as introductory artificial intelligence, programming, databases, or machine learning. A technically defined topic is advantageous because conceptual accuracy, relationships, and application can be assessed against relatively clear disciplinary expectations.

For a formative study, the participant sample should be reported as a pragmatic exploratory cohort rather than presented as sufficient for population-level causal claims. A subsequent confirmatory study should determine sample size through a priori power analysis based on the intended statistical comparisons and anticipated effect size.

### 4.3 Procedure

The evaluation should expose learners to multiple iterations of the knowledge-construction cycle rather than a single AI interaction. Participants first complete a baseline assessment of conceptual understanding. They then construct initial personal wiki entries for selected learning concepts. Once an initial representation exists, the AI Companion introduces reflective prompts and targeted scaffolding. Learners decide whether and how to revise their knowledge artefacts before completing retrieval and application tasks. The process is repeated across multiple concepts so that the Revisit & Extend mechanism can be meaningfully observed when later learning relates to earlier entries.

A post-intervention assessment can then examine conceptual understanding and application. Learner perceptions may be collected using an appropriately validated or transparently developed questionnaire, supplemented by semi-structured interviews or open-ended responses. System logs and wiki revision histories provide additional process data.

### 4.4 Evaluation Constructs and Measures

Because the framework distinguishes between the external knowledge artefact and internal conceptual understanding, evaluation should not reduce learning to a single outcome measure.

**Table 4. Proposed evaluation dimensions and data sources**

| Evaluation Dimension | Indicative Construct | Possible Evidence Source |
|---------------------|---------------------|-------------------------|
| **Conceptual Understanding** | Accuracy and completeness of disciplinary understanding | Pre-/post-assessment |
| **Explanation Quality** | Depth, coherence, and justification | Wiki artefact rubric |
| **Knowledge Integration** | Meaningful connections among concepts | Wiki links, Concept Graph, artefact analysis |
| **Application and Transfer** | Ability to use knowledge in unfamiliar situations | Scenario-based or problem-solving tasks |
| **Revision Quality** | Substantive improvement following reflection or scaffolding | Version history |
| **Learner Response to AI** | Acceptance, rejection, modification, or independent resolution of AI prompts | Interaction logs and revision traces |
| **Metacognitive Engagement** | Monitoring, confidence judgements, reflection, and explanation of revision decisions | Reflection prompts, questionnaire, interviews |
| **Perceived Usefulness and Agency** | Learner experience of AI feedback, control, and learning support | Questionnaire and qualitative feedback |

Artefact quality can be examined through dimensions already implied by the framework: conceptual accuracy, explanation depth, meaningful knowledge connections, example quality, appropriate use of evidence, and substantive revision. Such dimensions should be operationally defined through a coding rubric and evaluated by multiple raters where feasible. Inter-rater reliability should be reported for qualitative or rubric-based coding.

### 4.5 Human-AI Interaction Analysis

A particularly important analytical opportunity concerns what learners actually do with AI-generated scaffolding. Many educational AI evaluations rely primarily on achievement scores or self-reported usefulness. While informative, these measures reveal comparatively little about the mechanism through which AI intervention influences learning activity.

The proposed system enables process analysis of the sequence:

```
AI Feedback → Learner Evaluation → Accept / Reject / Modify → Knowledge Revision
```

Interaction logs can therefore identify the type of scaffolding delivered, whether the learner engaged with it, whether a corresponding revision occurred, and whether the learner adopted, rejected, or substantially transformed the AI suggestion. Such traces may help distinguish uncritical AI acceptance from active epistemic judgement.

The analysis should avoid assuming that acceptance is inherently positive or rejection inherently negative. Rejecting an incorrect, irrelevant, or unnecessary AI suggestion may provide stronger evidence of learner judgement than accepting a valid suggestion. Consequently, the quality of the learner's reasoning and resulting artefact is more important than maximising AI recommendation acceptance.

---

## 5. Discussion

### 5.1 Reframing the Role of Generative AI in Learning

The proposed framework addresses a fundamental tension in educational GenAI. As models become increasingly capable of explaining, summarising, structuring, comparing, and rewriting information, they can remove effort from many academic tasks. Whether that reduction in effort is educationally beneficial depends on the function that the effort previously served.

If a task involves clerical transformation, automation may create opportunities for learners to concentrate on more demanding cognition. If, however, the task requires learners to explain relationships, retrieve knowledge, compare alternatives, or evaluate evidence, delegating the activity to AI may remove precisely the cognitive process the educational activity was designed to cultivate.

The relevant distinction is therefore not simply between AI use and non-use. It is between **AI assistance that enables productive cognitive activity** and **AI substitution that displaces it**.

The AI Wiki Companion operationalises this distinction by assigning different responsibilities to the learner and the system. AI questions, identifies, challenges, recommends, and prompts. The learner explains, judges, verifies, decides, revises, connects, and applies. The boundary is intentionally permeable because direct AI instruction remains appropriate under some conditions. Nevertheless, learner epistemic agency constitutes the default organising principle.

### 5.2 Personal Knowledge as an Evolving Artefact

A second contribution concerns the temporal structure of AI-supported learning. Many conversational AI interactions are episodic: a learner asks a question, receives an answer, and the interaction terminates. In contrast, a personal wiki persists across learning episodes. Earlier representations can become objects of later reflection.

The Revisit & Extend stage therefore makes knowledge evolution central to the system. When new material becomes relevant to an earlier concept, the AI Companion can prompt the learner to reconsider the existing representation. This creates a potential mechanism for supporting cumulative learning, conceptual integration, and revision over time.

Such longitudinal support may also produce richer evidence for learning analytics. Rather than analysing only prompts and responses, researchers can examine how conceptual representations change, which relationships emerge, when earlier knowledge is revisited, and what forms of AI intervention precede substantive revision.

### 5.3 Implications for HCI and AIED Design

From an HCI perspective, learner-in-the-loop knowledge construction requires interfaces that maintain clear boundaries between learner-authored and AI-generated content. Suggestions should be inspectable, attributable, contestable, and reversible. Automatically integrating AI text into the persistent knowledge base would undermine both epistemic transparency and the ability to interpret revision histories.

The framework further suggests that educational interfaces should not always optimise for minimum interaction cost. **Prompt Before Provide** intentionally introduces a small amount of friction when that friction creates an opportunity for retrieval, articulation, or self-assessment. This does not imply that difficulty is inherently desirable. Rather, interface efficiency should be evaluated in relation to pedagogical objectives.

For AIED, the framework shifts the emphasis from the quality of AI-generated answers towards the quality of learner activity elicited by AI intervention. A technically accurate response may be pedagogically weak if it removes the need for learner reasoning, while a carefully calibrated question may be educationally valuable precisely because it leaves part of the problem unresolved.

---

## 6. Limitations and Future Research

The proposed framework has several limitations that require empirical investigation:

1. **Adaptive Scaffolding:** The effectiveness of Prompt Before Provide is likely to depend on learner expertise, prior knowledge, task difficulty, and motivational state. Requiring construction before assistance may support retrieval and reflection for some learners but impose unnecessary cognitive load for others. Adaptive policies are therefore likely to be necessary.

2. **AI Scaffolding Quality:** The quality of GenAI scaffolding cannot be assumed. Large language models may generate inaccurate critiques, identify nonexistent gaps, propose superficial conceptual links, or express unwarranted confidence. The system should consequently incorporate grounding, source verification, transparent uncertainty where possible, and mechanisms through which learners can challenge AI output.

3. **External vs. Internal Knowledge:** An external wiki cannot be treated as a direct representation of internal knowledge. A learner may understand relationships that have not been explicitly linked, or may create links without understanding them. Wiki artefacts should therefore be analysed alongside independent conceptual and application measures.

4. **Over-Reliance Risk:** Learner-in-the-loop design does not in itself prevent over-reliance. Students may routinely accept suggestions despite being given formal control. Future studies should therefore examine not only whether control mechanisms exist but whether learners exercise meaningful evaluative judgement.

5. **Collaborative Extensions:** The framework currently focuses on individual knowledge construction. Subsequent research could investigate collaborative wiki environments, instructor participation, peer feedback, adaptive scaffolding policies, and longitudinal knowledge development across an entire course.

---

## 7. Conclusion

This paper proposes the AI Wiki Companion as a learner-in-the-loop environment for active and continuous knowledge construction. The framework responds to a central tension in generative AI-supported learning: the capabilities that make GenAI useful for generating explanations, summaries, and organised information may also allow learners to bypass cognitive activities that contribute to understanding.

Rather than rejecting generative assistance, the proposed approach reorganises its pedagogical role. Learners remain responsible for constructing, evaluating, revising, connecting, and applying knowledge, while AI provides metacognitive and formative scaffolding through questioning, gap detection, conceptual challenges, connection recommendations, retrieval prompts, and review suggestions.

Four design principles guide this allocation of responsibility:
- **DP1 Learner Ownership**
- **DP2 Scaffold Rather Than Substitute**
- **DP3 Reflection Before Correction**
- **DP4 Continuous Knowledge Integration**

These principles are operationalised through the iterative **Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend** cycle and the complementary **Prompt Before Provide** interaction mechanism.

The broader contribution is therefore not an AI-enhanced note-taking system in the conventional sense. It is a **design argument** concerning the role that generative AI should occupy within learning processes. The educational value of GenAI may lie not only in its ability to provide knowledge efficiently, but also in its capacity to provoke the cognitive and metacognitive activities through which learners construct, test, reorganise, and progressively internalise knowledge.

Accordingly, the central design challenge for educational GenAI is not simply to determine what AI can do for the learner, but to determine **what the learner should continue to do because doing it is part of learning**.

---

## 📚 Related Work

### Key References

- **Writing-to-Learn:** Research examining how writing activities support cognitive processing and knowledge construction
- **Metacognition & SRL:** Frameworks for understanding self-regulated learning and metacognitive monitoring
- **Personal Knowledge Management:** Systems for persistent, networked knowledge representation
- **Human-in-the-Loop AI:** Approaches to retaining human agency in AI-assisted systems
- **Socratic Tutoring:** Intelligent tutoring systems using questioning rather than direct instruction
- **Cognitive Offloading:** Research on when and how external tools support or hinder learning

### Related Systems

- **Obsidian:** Personal knowledge base with linking and graph visualization
- **Notion:** Collaborative workspace with structured notes
- **Roam Research:** Networked note-taking with bidirectional links
- **Logseq:** Outliner with knowledge graph features
- **Zettelkasten:** Traditional note-taking method for knowledge management

---

## 🔗 Connections to AI Research Tracker

This paper directly informs the design of the **AI Research Tracker** system:

1. **Wiki Page:** Implements the AI Learning Companion with Write, Review, Coach, and Update modes
2. **Learning Journey:** Follows the 5-stage knowledge construction cycle
3. **Workspace:** Supports active paper reading and insight capture
4. **AI Study Guide:** Provides scaffolding rather than direct answers
5. **Spaced Repetition:** Supports the Consolidate & Apply stage

The framework validates the learner-in-the-loop approach already embedded in the AI Research Tracker architecture.

---

## 📝 Notes for Implementation

### Current Implementation Status

✅ **Implemented:**
- Learner-authored wiki entries (public/wiki.md, public/ai-wiki.md)
- AI Companion with 4 modes (Write, Review, Coach, Update)
- Learning Journey with 5 stages
- Version history tracking
- Concept linking and backlinks

🔄 **In Progress:**
- Prompt Before Provide interaction model
- Metacognitive reflection prompts
- Knowledge gap detection
- Connection recommendations

📋 **Planned:**
- Scaffolding vs. substitution analytics
- Learner response tracking (accept/reject/modify)
- Longitudinal knowledge evolution visualization
- Formative evaluation framework

---

## 📊 Citation

```bibtex
@article{AIWikiCompanion2026,
  title = {From Notes to Knowledge: Designing an AI Wiki Companion for Learner-in-the-Loop Knowledge Construction},
  author = {Research Team},
  journal = {To Be Submitted},
  year = {2026},
  month = {September},
  keywords = {generative AI, knowledge construction, learner-in-the-loop, writing-to-learn, metacognition, self-regulated learning, personal wiki, cognitive offloading, AI in education}
}
```

---

<div class="paper-actions">
  <button class="btn-primary" onclick="bookmarkPaper()">🔖 Bookmark</button>
  <button class="btn-secondary" onclick="exportPaper()">📤 Export PDF</button>
  <button class="btn-secondary" onclick="sharePaper()">🔗 Share</button>
  <button class="btn-secondary" onclick="addNotes()">✏️ Add Notes</button>
</div>

<style>
.conference-paper-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
}

.conference-paper-header h2 {
  color: white !important;
  margin: 0 0 0.5rem 0;
}

.paper-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e5e7eb;
}

.btn-primary {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s;
}

.btn-primary:hover {
  background: #5a6fd6;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-secondary {
  background: #f3f4f6;
  color: #374151;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-secondary:hover {
  background: #e5e7eb;
  border-color: #9ca3af;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.95rem;
}

th, td {
  border: 1px solid #e5e7eb;
  padding: 1rem;
  text-align: left;
  vertical-align: top;
}

th {
  background: #f9fafb;
  font-weight: 600;
  color: #374151;
}

tr:nth-child(even) {
  background: #f9fafb;
}

blockquote {
  border-left: 4px solid #667eea;
  padding-left: 1.5rem;
  margin: 1.5rem 0;
  font-style: italic;
  color: #4b5563;
  background: #f9fafb;
  padding: 1rem 1.5rem;
  border-radius: 0 8px 8px 0;
}

pre {
  background: #1f2937;
  color: #f3f4f6;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.9rem;
  line-height: 1.6;
}
</style>

<script>
function bookmarkPaper() {
  console.log('Bookmarking paper...');
  // Implementation pending
}

function exportPaper() {
  console.log('Exporting to PDF...');
  // Implementation pending
}

function sharePaper() {
  console.log('Sharing paper...');
  // Implementation pending
}

function addNotes() {
  console.log('Adding notes...');
  // Implementation pending
}
</script>
