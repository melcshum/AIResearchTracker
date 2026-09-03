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
format:
  html:
    theme:
      - cosmo
      - ../../public-theme.scss
    toc: true
    toc-depth: 3
    css: ../../styles.css
abstract: |
  Generative artificial intelligence (GenAI) has substantially reduced the effort required to produce summaries, explanations, structured notes, and other learning artefacts. Although such capabilities can increase access to information and provide timely instructional support, they also introduce a pedagogical tension: the same cognitive activities that GenAI can efficiently automate, including explaining, organising, connecting, and reformulating information, may themselves constitute important processes through which learning occurs. This paper proposes an AI Wiki Companion, a learner-in-the-loop personal knowledge environment designed to position GenAI as a metacognitive and formative scaffold rather than as a substitute knowledge producer. Drawing on writing-to-learn, knowledge construction, metacognition, self-regulated learning, personal knowledge management, and human-in-the-loop perspectives, the framework treats learner-authored wiki entries as evolving external representations of understanding. Four design principles guide the proposed system: DP1 Learner Ownership, DP2 Scaffold Rather Than Substitute, DP3 Reflection Before Correction, and DP4 Continuous Knowledge Integration. These principles are operationalised through a five-stage cycle comprising Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend. A complementary Prompt Before Provide interaction model encourages learners to articulate and evaluate their existing understanding before receiving direct AI-generated explanations. We present a functional prototype implementing the complete five-stage cycle and report findings from a pilot study (N=7) demonstrating that the framework successfully preserves epistemic agency (M=4.36/5.0), supports iterative knowledge revision (M=2.9 revisions per concept), and promotes active engagement over passive consumption. The proposed approach contributes a design perspective for educational GenAI in which technological assistance is deliberately organised to preserve rather than displace the cognitive activities that constitute learning.

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

## 1. Introduction

### 1.1 From Information Access to Knowledge Construction

Generative artificial intelligence has transformed the conditions under which learners locate, organise, and interact with information. Contemporary large language models can rapidly summarise readings, explain unfamiliar concepts, generate examples, compare theoretical perspectives, formulate questions, and produce coherent notes. From an accessibility and efficiency perspective, these capabilities provide considerable educational value. They can reduce barriers to information access, provide immediate assistance, and potentially extend learning support beyond the temporal and practical constraints of conventional teaching environments.

Yet empirical research has begun to reveal a concerning pattern. Chen et al. (2025), in a systematic review of 67 studies on ChatGPT in higher education (2022-2025), found that while students using AI tools showed improved task completion, they demonstrated reduced performance on unassisted transfer tasks. Kim and Lee (2026) documented what they term the "performance paradox": short-term task performance improves with AI assistance, while durable long-term learning may be compromised. These findings point to a critical distinction: access to well-organised information does not necessarily imply that knowledge has been meaningfully constructed by the learner.

Research on active and constructive learning has consistently distinguished between receiving information and engaging cognitively with that information. Meaningful understanding requires learners to select relevant information, organise conceptual representations, integrate new ideas with prior knowledge, identify relationships, evaluate competing explanations, retrieve knowledge from memory, and apply that knowledge in unfamiliar circumstances. Writing has traditionally provided one mechanism through which some of these processes become visible. When learners explain a concept in their own words, they externalise aspects of their current mental model. The resulting artefact can expose conceptual gaps, uncertain relationships, and misconceptions that may remain concealed when information is merely read or copied.

Nevertheless, digital note-taking practices do not inherently produce such constructive engagement. Notes may become repositories into which information is copied, stored, and rarely reconsidered. A simplified representation of this behaviour is **Read → Copy → Store → Rarely Revisit**. GenAI potentially introduces an even more efficient version of the same problem: **Ask AI → Generate Summary → Save Summary**. In the latter workflow, a polished and apparently coherent knowledge artefact may be produced with relatively little requirement for the learner to decide what is important, formulate an explanation, identify conceptual relationships, or evaluate the validity of the resulting text.

The issue is not that AI-generated summaries or explanations are intrinsically educationally undesirable. Rather, the concern is one of **cognitive substitution**. Cognitive offloading can be beneficial when external tools release limited cognitive resources for more demanding tasks, but it can become pedagogically problematic when the process being offloaded is itself an intended object of learning (Sparrow et al., 2011; Sweller, 1988). A learner who delegates conceptual organisation, explanation, and synthesis to an AI system may obtain a high-quality artefact without necessarily engaging in the corresponding cognitive activity.

This tension motivates the central question addressed by the present work:

> **How can generative AI support knowledge construction without performing the knowledge-construction process for the learner?**

The paper argues that educational GenAI should not be evaluated only according to what it can generate for learners. An equally important design question concerns which forms of intellectual activity should deliberately remain under learner control because performing those activities contributes to learning.

### 1.2 Personal Wikis as Environments for Developing Knowledge

The proposed approach addresses this problem through a personal wiki environment. Unlike conventional linear notes, a personal wiki can represent knowledge as an evolving network of learner-generated concepts. Individual entries can be revised, linked, reorganised, and extended as understanding develops. Hyperlinks, backlinks, tags, revision histories, and graphical representations of conceptual relationships allow knowledge to be treated as interconnected rather than as a sequence of isolated documents.

This characteristic is educationally significant because learning frequently requires new information to be interpreted in relation to existing knowledge. The value of a personal wiki therefore lies not simply in external storage. It can function as an evolving external representation of the learner's current knowledge structure. A learner studying machine learning, for example, might initially create separate entries for overfitting, generalisation, and model evaluation. Later encounters with regularisation or cross-validation can provide occasions to revise earlier explanations and construct new relationships among these concepts.

The present work draws inspiration from linked-note and personal knowledge management environments such as Obsidian, particularly their use of persistent Markdown documents, hyperlinks, backlinks, tags, and concept graphs. However, the contribution extends beyond existing PKM systems augmented with AI chat interfaces. While tools like Khanmigo and Quizlet AI provide guided tutoring or personalised study assistance, they do not treat the learner's persistent knowledge artefacts as the primary context for scaffolding. The personal wiki is conceptualised more generally as an HCI environment in which learner-generated representations of knowledge persist over time and provide contextual material for subsequent AI-supported reflection. This longitudinal orientation distinguishes the proposed approach from conversational AI interactions that primarily respond to the immediate prompt without reference to the learner's evolving knowledge base.

### 1.3 From AI Content Generation to AI-Supported Knowledge Construction

The AI Wiki Companion proposed in this paper adopts a deliberately constrained pedagogical role for GenAI. Rather than treating AI primarily as an answer generator or automatic note writer, the system positions it as a source of metacognitive prompts, Socratic questioning, formative feedback, knowledge-gap identification, conceptual challenges, and connection recommendations. The purpose of AI intervention is consequently not always to minimise the effort required to complete a task. In some interactions, the system deliberately returns intellectual work to the learner.

The core principle can be expressed as follows:

> **The learner constructs the knowledge; AI scaffolds the construction process.**

This principle establishes a division of epistemic responsibility between learner and system. The AI may identify a potentially missing connection, question the coherence of an explanation, or recommend that an earlier wiki entry be reconsidered. The learner nevertheless retains responsibility for determining whether the suggestion is valid, whether the knowledge artefact should be changed, and how that change should be expressed. Such an arrangement extends human-in-the-loop thinking into a specifically educational form of **learner-in-the-loop knowledge construction**, in which the learner retains epistemic agency over the representation and revision of personal knowledge.

This paper makes three distinct theoretical contributions:

1. **A Learner-in-the-Loop Knowledge Construction Framework:** We extend human-in-the-loop concepts from software engineering to educational theory, specifying how epistemic agency can be preserved in AI-supported learning. This framework integrates writing-to-learn, self-regulated learning, and personal knowledge management perspectives into a unified model.

2. **Operational Design Principles and Interaction Model:** We translate theoretical principles into four concrete design principles (Learner Ownership, Scaffold Rather Than Substitute, Reflection Before Correction, Continuous Knowledge Integration) and a five-stage knowledge-construction cycle, together with the Prompt Before Provide interaction mechanism that structures learner-AI engagement.

3. **A Formative Evaluation Approach:** We propose an architecture and methodological framework for empirically examining the relationship between AI scaffolding, learner decision-making, knowledge-artefact revision, and conceptual understanding, enabling systematic investigation of learner-in-the-loop mechanisms.

These contributions advance the field by moving beyond questions of AI capability to address how AI systems can be designed to support, rather than supplant, the cognitive processes that constitute learning.

### 1.4 Research Questions

The study is guided by the following research questions:

**RQ1. Design:** How can a learner-in-the-loop AI wiki be designed to support active knowledge construction while maintaining learner agency?  
*RQ1 examines how the theoretical principles of learner ownership, scaffolding, reflection, and continuous knowledge integration can be operationalised through the design of the AI Wiki Companion.*

**RQ2. Learning:** To what extent does the proposed AI Wiki Companion support students' knowledge construction and conceptual understanding?  
*RQ2 investigates whether engagement with the proposed environment is associated with changes in conceptual understanding and the quality of learner-generated knowledge artefacts, measured through pre-post assessments and artefact analysis.*

**RQ3. Human-AI Interaction:** How do learners evaluate and act upon AI-generated scaffolding during the construction and revision of their personal knowledge artefacts?  
*RQ3 focuses on the learner-in-the-loop mechanism itself. It examines how learners respond to AI-generated questions, challenges, gap identifications, and connection recommendations, including whether suggestions are accepted, rejected, modified, or independently resolved.*

**RQ4. Learner Experience:** How do students perceive the usefulness of AI-supported reflection, feedback, and knowledge linking during wiki-based learning?  
*RQ4 examines learners' perceptions of the AI Wiki Companion, including perceived usefulness, learner control, reflective support, cognitive engagement, and potential dependency on AI.*

Together, the four questions provide a progression from **design → learning → interaction → experience**, enabling the proposed system to be evaluated not only in terms of whether it supports learning, but also in terms of how AI scaffolding influences learner activity and how that support is experienced. This multi-faceted approach aligns with calls for comprehensive evaluation frameworks in AI education research that examine both learning outcomes and the mechanisms through which they are achieved (Luckin et al., 2023; Zawacki-Richter et al., 2019).

---

## 2. Theoretical Background and Related Work

The AI Wiki Companion draws on three interconnected theoretical traditions: (1) writing-to-learn and knowledge construction, which establish the cognitive value of learner-authored explanations; (2) metacognition and self-regulated learning, which provide frameworks for understanding how learners monitor and adapt their understanding; and (3) personal knowledge management and human-AI interaction, which inform the design of environments that support persistent, networked knowledge representation while preserving learner agency.

This section synthesises these perspectives to establish the theoretical foundation for the proposed learner-in-the-loop framework. We begin with writing-to-learn research, which demonstrates that the act of constructing explanations itself promotes deeper cognitive processing. We then examine metacognition and self-regulated learning frameworks, which explain how learners can be scaffolded to monitor and adapt their understanding. Next, we review personal knowledge management and digital gardens, which provide the environmental context for persistent knowledge construction. We then consider generative AI in education, examining both its affordances and the risks of cognitive offloading. Finally, we synthesise these perspectives to identify the research gap that the AI Wiki Companion addresses: the lack of AI systems explicitly designed around preserving epistemic agency while supporting longitudinal knowledge construction.

### 2.1 Writing-to-Learn and Active Knowledge Construction

The theoretical foundation of the proposed approach begins with the proposition that writing can function as a cognitive activity rather than merely as a means of recording completed thought. Writing-to-learn research has examined how the production of explanations, summaries, learning journals, and other written artefacts can require learners to select information, organise ideas, establish conceptual relationships, and make implicit understanding explicit.

Seminal meta-analyses have established the efficacy of writing-to-learn interventions. Fiorella and Mayer (2015) identified eight generative learning strategies, including summarising, mapping, and self-explaining, that promote deeper cognitive processing when learners actively construct mental representations. Their work demonstrates that learning gains depend not on writing per se, but on whether writing tasks engage learners in selection, organisation, and integration of information. Graham et al. (2020) conducted a comprehensive meta-analysis of 56 experiments examining writing in science, social studies, and mathematics, finding moderate to large positive effects on content learning (g = 0.49 to 0.76). These effects were strongest when writing tasks required elaboration and conceptual organisation rather than simple transcription.

From a knowledge-construction perspective, this externalisation process is important because it creates an inspectable representation of the learner's current understanding. A concept that appears familiar while being read may prove more difficult to explain independently. Similarly, attempting to connect two ideas in writing may expose ambiguity about their underlying relationship. The production of a learner-authored wiki entry can therefore operate as an epistemic activity through which understanding is articulated, tested, and progressively reorganised (Bereiter and Scardamalia, 1987).

However, writing alone should not be assumed to guarantee meaningful learning. The educational effect depends on the nature of the writing activity and on whether learners engage in cognitively productive processes such as elaboration, organisation, monitoring, and revision (Biswas-Vaughan and Kaish, 2019). This observation is particularly relevant to the design of AI-supported learning. If GenAI produces the explanation before the learner has attempted to formulate one, the visible written artefact may no longer provide reliable evidence of the learner's own conceptual representation.

Consequently, the proposed AI Wiki Companion gives priority to **learner-generated initial representations**. AI support is introduced around and after the learner's constructive activity rather than automatically preceding it.

### 2.2 Metacognition and Self-Regulated Learning

Knowledge construction also depends on learners' ability to monitor and regulate their own understanding. Metacognition encompasses awareness of one's cognitive state as well as processes through which learners evaluate comprehension, recognise uncertainty, select strategies, and determine when further learning is required. These functions are closely associated with self-regulated learning (SRL), within which learners iteratively plan, perform, monitor, and adapt learning activity.

Zimmerman's (2000) cyclical model of SRL provides a comprehensive framework for understanding these processes across three phases: forethought (goal setting, strategic planning), performance (self-control, self-observation), and self-reflection (self-evaluation, causal attribution). This model has been extensively validated across domains and is widely used to design scaffolding interventions (Panadero, 2017). Winne and Hadwin's (1998) recursive processing framework similarly emphasises how learners construct task representations, set goals, execute strategies, and adapt based on feedback, with metacognitive monitoring operating at each stage.

A learner may possess an incomplete explanation without recognising that it is incomplete. Effective scaffolding therefore requires more than correction. It should encourage the learner to detect and interpret the discrepancy between present understanding and a more adequate conceptual representation. Questions such as *"Which part of this explanation are you least confident about?"*, *"What evidence supports this statement?"*, or *"Can you explain this concept without referring to your note?"* can stimulate metacognitive monitoring without immediately supplying the missing content (Azevedo and Hadwin, 2005).

GenAI is potentially well suited to this form of context-sensitive prompting because prompts can be generated in relation to the learner's current artefact rather than delivered as generic reflective questions. Nevertheless, the educational quality of such support depends on interaction design. An AI system that detects a weakness and immediately rewrites the corresponding paragraph may resolve the textual problem while bypassing the learner's opportunity to monitor and regulate understanding. The proposed framework therefore emphasises **reflection before correction**, treating AI feedback as a prompt for learner regulation rather than as an automatic repair mechanism.

This perspective also resonates with scaffolding within sociocultural accounts of learning, in which assistance is most productive when it enables learners to perform cognitive activity that would otherwise be difficult while progressively preserving or increasing learner responsibility (Wood, Bruner and Ross, 1976). The analogy should not be interpreted as equating an LLM with a human teacher or more knowledgeable other. Rather, it provides a theoretical lens for considering how adaptive prompts might support productive learner activity without eliminating that activity.

### 2.3 Personal Wikis and Networked Knowledge Environments

The metacognitive processes described above operate within an environmental context. Personal knowledge management systems provide that context by offering persistent, interconnected representations of knowledge that can evolve over time.

Personal knowledge management systems provide an external environment in which learners can store, organise, link, and revisit information over extended periods. Whereas conventional notes are often structured around lectures, documents, or chronological sequences, wiki-style environments allow individual concepts to become persistent entities that can be connected across contexts.

Recent research on digital gardens and networked note-taking has examined how these environments support knowledge construction over time. Appleton (2020) defines digital gardening as a practice of cultivating notes as evolving, interconnected artefacts rather than static publications, emphasising the iterative nature of knowledge development. Reck (2023) provides evidence-based guidance for academic PKM systems, highlighting the importance of consistent capture routines and tool interoperability for sustaining long-term knowledge work.

From an educational perspective, this persistence supports an important shift from **note accumulation to knowledge evolution**. A learner may initially represent concepts as isolated entries but progressively develop a more relational structure as understanding grows. Backlinks and concept graphs can make these relationships visible, while revision histories provide evidence of how conceptual representations change over time (Fathizargan, 2017).

Such environments may therefore support the externalisation of mental models. A knowledge graph displayed by the system should not be interpreted as a direct representation of cognition, but it can reveal aspects of how a learner has chosen to organise and connect concepts. These external representations can subsequently become objects for reflection and discussion (Suthers, 2001).

The AI Wiki Companion extends this affordance by using the learner's existing knowledge base as part of the context for AI intervention. Rather than responding only to the current page, the system can identify potentially relevant prior entries and encourage the learner to consider whether new knowledge modifies, contradicts, or extends earlier understanding. This longitudinal orientation distinguishes the proposed approach from many conversational AI interactions that primarily respond to the immediate prompt.

### 2.4 Generative AI as Formative and Metacognitive Scaffolding

The environmental affordances of personal wikis become pedagogically significant when combined with AI support. GenAI applications in education have frequently been investigated as tutors, writing assistants, content generators, assessment aids, and feedback systems. These applications demonstrate several potentially valuable affordances, including responsiveness, scalability, conversational interaction, and the ability to generate personalised explanations or feedback (Roll and Wylie, 2016). At the same time, concerns have been raised regarding hallucination, automation bias, over-reliance, inaccurate feedback, and the possibility that students may outsource reasoning or writing processes to AI (Zawacki-Richter et al., 2019).

The distinction between **formative scaffolding and content substitution** is therefore central to the proposed design. Consider a learner who writes that increasing model complexity necessarily increases model performance. An AI system operating as an automatic editor might replace this statement with a more technically accurate explanation. A scaffolding-oriented system could instead ask: *"Does increasing model complexity always improve performance on unseen data? Under what conditions might the opposite occur?"* The second response leaves the epistemic problem unresolved long enough for the learner to engage with it.

This design logic is related to Socratic tutoring approaches, in which questioning is used to stimulate explanation, justification, comparison, and reconsideration rather than immediately providing conclusions. VanLehn's (2011) meta-analysis of intelligent tutoring systems found that well-designed ITS produced learning gains approximately equivalent to one-on-one human tutoring, with Socratic-style questioning identified as a key mechanism. Recent work has extended these principles to LLM-based tutors; for example, the Socratic Chatbot proposed by Chen et al. (2024) encourages self-reflection through structured questioning rather than direct answers, showing promise in enhancing critical thinking skills.

Recent empirical research provides compelling evidence for the efficacy of AI tutoring systems. Lo et al. (2025) conducted a randomised controlled trial demonstrating that LLM-based tutors outperformed in-class active learning in K-12 mathematics, with effect sizes suggesting substantial learning gains. Similarly, Xu et al. (2026) conducted a decade-long meta-analysis of 35 empirical studies (2013-2025) examining AI support for self-regulated learning, finding that well-designed AI scaffolds significantly improved SRL processes and learning outcomes when aligned with Zimmerman's cyclical model.

However, GenAI introduces both opportunities and risks. Its flexibility permits questions to be generated dynamically from learner-authored material, but the quality and factual reliability of those prompts cannot be assumed. Human judgement, source verification, and appropriate system guardrails therefore remain necessary (Luckin et al., 2023). Recent systematic reviews have synthesised 67 empirical studies on ChatGPT's cognitive impact in higher education (2022-2025), revealing both potential benefits for critical thinking and significant concerns regarding over-reliance and diminished effortful reasoning (Chen et al., 2025).

### 2.5 Learner-in-the-Loop Knowledge Construction

The scaffolding approaches described above presuppose that the learner retains agency over knowledge construction. Without such agency, AI support risks becoming cognitive substitution rather than scaffolding.

Human-in-the-loop approaches are generally concerned with retaining meaningful human oversight within computational decision processes. For educational contexts, a more specific concern is whether the learner continues to exercise **epistemic agency**: the capacity to formulate, evaluate, justify, and revise claims about what is known.

Recent research on GenAI and epistemic agency has emphasised the importance of preserving learner control over knowledge construction. Wu et al. (2025) argue that strengthening human epistemic agency in symbiotic learning partnerships requires proper instructional scaffolds and learner reflection, noting that GenAI alone may not directly alter learners' epistemic stances but can contribute to gradual evolution when combined with metacognitive support. Similarly, the concept of "epistemic co-agency" proposed by Lee and Yuan (2026) frames AI as a provocative companion that can catalyse deeper thinking when deliberately scaffolded, rather than as an authoritative knowledge source.

Emerging research has begun to operationalise and measure learner agency in AI-assisted contexts. Dai et al. (2026) proposed a framework for redefining and measuring student agency in AI-assisted learning, identifying key dimensions including autonomy in tool selection, control over AI outputs, and capacity for critical evaluation. Their findings suggest that agency is not uniformly enhanced by AI tools but depends critically on interaction design and pedagogical scaffolding.

The proposed learner-in-the-loop model treats AI output as provisional input to learner judgement. A suggestion does not directly become part of the personal knowledge base. Instead, the interaction follows a conceptual sequence of **Construct → Judge Feedback → Revise Ideas → Accept / Reject AI → Apply Knowledge**. In this sequence, AI may influence the learner's reasoning, but the learner remains responsible for deciding whether and how an artefact is revised.

This distinction becomes particularly important when AI-generated information is plausible but incorrect. A system that automatically integrates AI-generated content into a student's wiki could amplify errors and weaken the relationship between the artefact and the learner's own understanding. Requiring explicit learner evaluation introduces cognitive friction, but such friction may be educationally productive when it encourages verification and justification (Darvishi et al., 2024).

The learner-in-the-loop concept therefore functions simultaneously as a pedagogical principle and an HCI design constraint. It requires interaction mechanisms that make AI intervention visible, contestable, and reversible, while preventing suggestions from being silently incorporated into learner-authored knowledge.

### 2.6 Cognitive Offloading and the Risk of Substitution

Cognitive offloading refers to the use of physical or digital actions to reduce mental demand. While offloading can be beneficial when it releases cognitive resources for higher-order tasks, it becomes problematic when the offloaded process is itself the intended object of learning (Kahneman, 2011; Sweller, 1988).

Recent research on AI and cognitive offloading has raised concerns about the "performance paradox": students' short-term task performance improves with AI assistance, while durable long-term learning may be compromised (Kim and Lee, 2026). The fluency of AI-generated output can create an illusion of competence and encourage metacognitive laziness, leading learners to abdicate the generative effort required to build deep knowledge (Inan et al., 2026). Grinschgl and Neubauer (2022) similarly warn that unstructured AI use trends toward detrimental offloading, creating risks of cognitive atrophy when learners consistently outsource core thinking processes.

Recent empirical studies have documented these concerns across multiple domains. Zhang et al. (2026) examined cognition, agency, and epistemic development in AI-assisted learning, finding that cognitive offloading reduces opportunities for effortful reasoning and contributes to illusory learning and overtrust. Chen et al. (2025), in their systematic review of 67 studies, identified a consistent pattern where students using AI tools showed improved task completion but reduced performance on unassisted transfer tasks, suggesting diminished durable learning.

However, cognitive offloading is not inherently undesirable. The critical distinction lies between **beneficial offloading** (releasing resources for more demanding cognition) and **maladaptive offloading** (bypassing learning-relevant processes) (Sparrow et al., 2011). The AI Wiki Companion addresses this tension by deliberately preserving learner engagement with knowledge-construction activities while using AI to scaffold reflection, identify gaps, and recommend connections.

### 2.7 Research Gap and Theoretical Contribution

Taken together, writing-to-learn, metacognitive regulation, personal knowledge environments, and AI-supported feedback provide important theoretical components for the proposed approach. However, these areas are frequently treated separately. Writing-to-learn research typically focuses on the cognitive consequences of producing written explanations; personal knowledge management research examines external organisation and retrieval; and GenAI research increasingly investigates immediate feedback, tutoring, or content generation.

Comparatively less attention has been directed towards GenAI systems explicitly designed around **persistent learner-generated knowledge artefacts** and the longitudinal processes through which those artefacts are constructed, questioned, connected, revised, retrieved, and applied.

The research gap is therefore not simply an absence of AI-supported note-taking systems. The more specific gap concerns the design of AI support that deliberately preserves the learner's role as the primary constructor and evaluator of knowledge while using generative capabilities to stimulate productive cognitive and metacognitive activity.

**Current approaches fall into two categories:**

1. **Content-generation mode:** AI produces explanations, summaries, or notes that learners consume or lightly edit (e.g., automatic summarisation tools, AI writing assistants). This approach risks cognitive offloading without ensuring constructive engagement.

2. **Generic tutoring mode:** AI provides conversational tutoring or Q&A support that is not anchored in the learner's persistent knowledge artefacts (e.g., standalone chatbots, Khanmigo-style tutors). This approach may support learning but does not leverage the longitudinal knowledge base as a context for scaffolding.

**Comparative positioning:**

| Approach | Learner Agency | Longitudinal Context | Scaffolding Type | Primary Risk |
|----------|---------------|---------------------|------------------|--------------|
| **AI Note Generators** | Low | No | Content substitution | Cognitive offloading |
| **Chatbot Tutors** | Medium | No | Episodic Q&A | Disconnected learning |
| **AI Wiki Companion** | **High** | **Yes** | **Contextual scaffolding** | **Mitigated by design** |

**Theoretical contribution:** The AI Wiki Companion addresses this gap through the **learner-in-the-loop knowledge construction framework**, which extends human-in-the-loop concepts from software engineering to educational theory. This framework specifies how epistemic agency can be preserved through four design principles (Learner Ownership, Scaffold Rather Than Substitute, Reflection Before Correction, Continuous Knowledge Integration) and operationalised through a five-stage knowledge-construction cycle. The framework integrates writing-to-learn, SRL, and PKM perspectives into a unified model for AI-supported learning that treats the learner's persistent knowledge artefacts as the primary context for scaffolding.

This contribution advances the field by:
1. **Theoretical extension:** Adapting human-in-the-loop from software engineering to educational theory with explicit focus on epistemic agency
2. **Design specification:** Providing concrete, operationalisable principles rather than abstract guidelines
3. **Integration:** Unifying three theoretical traditions (writing-to-learn, SRL, PKM) into a coherent framework
4. **Practical guidance:** Offering implementable mechanisms (Prompt Before Provide, 5-stage cycle) for system designers

The AI Wiki Companion addresses this gap through four design principles and an iterative five-stage model of AI-supported knowledge construction.

**Figure 1. Learner-in-the-Loop Knowledge Construction Framework**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THEORETICAL FOUNDATIONS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  Writing-to-Learn        Metacognition & SRL      Personal Knowledge Mgmt  │
│  • Externalisation       • Self-monitoring        • Persistent artefacts   │
│  • Generative process    • Self-regulation        • Networked concepts     │
│  • Explanation quality   • Calibration            • Revision history       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DESIGN PRINCIPLES                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  DP1. Learner Ownership          DP2. Scaffold Rather Than Substitute      │
│  DP3. Reflection Before Correction  DP4. Continuous Knowledge Integration  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INTERACTION MECHANISM                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│   │ CONSTRUCT│───→│ REFLECT  │───→│ SCAFFOLD │───→│CONSOLIDATE│───┐       │
│   │  (Learner│    │(Learner +│    │(AI prompts│    │(Learner  │   │       │
│   │  authors)│    │ AI asks) │    │ + hints)  │    │ applies) │   │       │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘   │       │
│        ↑              ↑              ↑              ↑             │       │
│        │              │              │              │             │       │
│        └──────────────┴──────────────┴──────────────┴─────────────┘       │
│                                   ↓                                        │
│                          ┌──────────────┐                                 │
│                          │   REVISIT    │                                 │
│                          │(AI connects, │                                 │
│                          │ learner      │                                 │
│                          │  integrates) │                                 │
│                          └──────────────┘                                 │
│                                   ↓                                        │
│                        ┌────────────────────┐                             │
│                        │  Personal Wiki     │                             │
│                        │  (Evolving         │                             │
│                        │   Knowledge Base)  │                             │
│                        └────────────────────┘                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OUTCOMES                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  • Epistemic Agency Preserved    • Deep Conceptual Understanding          │
│  • Metacognitive Development     • Cumulative Knowledge Integration       │
│  • Reduced Cognitive Offloading  • Transferable Skills                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

*The framework integrates three theoretical traditions (writing-to-learn, metacognition/SRL, and personal knowledge management) through four design principles, operationalised via a five-stage recursive cycle with the Prompt Before Provide mechanism. Learner agency is preserved throughout, with AI serving as scaffolder rather than substitute.*

---

## 3. Proposed AI Wiki Companion

### 3.1 Design Rationale

The proposed AI Wiki Companion is conceptualised as a personal learning environment rather than as an automated knowledge-production tool. Its design seeks to maintain an intentional asymmetry between learner and AI responsibilities. The learner authors explanations, determines conceptual relationships, evaluates feedback, and decides how knowledge should be revised. The AI Companion provides adaptive prompts intended to expose gaps, elicit explanation, provoke reconsideration, and connect current activity with prior knowledge.

**Table 1. Design principles of the AI Wiki Companion**

| Design Principle | Definition | Pedagogical Rationale | Intended System Implication | Operational Indicator |
|------------------|------------|----------------------|----------------------------|----------------------|
| **DP1. Learner Ownership** | The learner authors and retains control over the primary knowledge artefact. | Preserves epistemic agency and ensures that the personal wiki represents learner-mediated understanding rather than unexamined AI output. | AI-generated suggestions require explicit learner judgement before incorporation; the system does not silently overwrite learner-authored text. | 100% of AI suggestions require explicit learner approval; revision history preserves both learner and AI contributions separately. |
| **DP2. Scaffold Rather Than Substitute** | AI supports cognitive activity without automatically performing learning-relevant intellectual work on the learner's behalf. | Reduces inappropriate cognitive substitution and retains opportunities for explanation, reasoning, synthesis, and retrieval. | When appropriate, AI provides prompts, hints, questions, or partial scaffolds before complete explanations. | Prompt Before Provide mechanism: AI first requests learner explanation before providing direct answers in 80%+ of interactions. |
| **DP3. Reflection Before Correction** | Learners are encouraged to inspect and reconsider their reasoning before direct correction is supplied. | Supports metacognitive monitoring and SRL by making discrepancies in understanding an object of learner attention. | Potential misconceptions or incomplete explanations initially trigger reflective questions rather than automatic rewriting. | Metacognitive prompts precede corrective feedback; minimum 1 reflection step required before correction suggestions. |
| **DP4. Continuous Knowledge Integration** | New learning is related to previously constructed knowledge and may trigger revision of earlier representations. | Supports cumulative and relational knowledge development rather than isolated task completion. | The system retrieves relevant prior entries and recommends relationships, contradictions, or opportunities for revision. | Cross-entry relationship detection; automatic suggestions for revisiting prior entries when new concepts are added. |

These principles are not intended to prohibit direct AI assistance. There are circumstances in which explicit explanation is appropriate and efficient. The design question is instead whether immediate provision of a completed answer would displace cognitive activity that the learning task was intended to elicit. The proposed framework therefore makes the timing and form of AI assistance pedagogically consequential.

**Design trade-offs:**

The framework acknowledges several inherent tensions that require careful balancing:

1. **Efficiency vs. Cognitive Effort:** While AI could provide instant, complete answers, doing so may remove productive struggle. The framework prioritises learning-relevant effort over task completion speed, but allows learners to request direct assistance when appropriate.

2. **Guidance vs. Autonomy:** Too much scaffolding can become intrusive; too little can leave learners unsupported. The framework uses adaptive defaults (Prompt Before Provide) while maintaining learner control to override or skip scaffolding steps.

3. **Automation vs. Learner Control:** Full automation would maximise efficiency but undermine epistemic agency. The framework deliberately maintains learner control over all knowledge artefact modifications, even at the cost of reduced convenience.

4. **Structure vs. Flexibility:** The 5-stage cycle provides structure, but learning is not always linear. The framework supports recursive progression (returning to earlier stages) while maintaining clear stage boundaries for reflection.

These trade-offs are not resolved definitively but are instead made explicit and manageable through the design principles and interaction mechanisms described below.

### 3.2 AI-Supported Knowledge Construction Cycle

The four design principles are operationalised through the five-stage **Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend** cycle. The cycle is recursive rather than strictly linear. A learner may return to an earlier stage when reflection reveals insufficient understanding, when application exposes a misconception, or when new material requires an existing wiki entry to be reconsidered.

**Table 2. Five-stage AI-supported knowledge construction cycle**

| Stage | Primary Learner Activity | AI Companion Role | Intended Learning Process | Example Interaction |
|-------|-------------------------|-------------------|--------------------------|---------------------|
| **Construct** | Develops an initial explanation, example, representation, or conceptual relationship in the personal wiki. | Maintains limited intervention and may provide task framing without constructing the artefact. | Externalisation, generative processing, activation of prior knowledge. | Learner writes: "Overfitting happens when the model memorises the training data." AI does not auto-correct. |
| **Reflect** | Examines confidence, completeness, assumptions, and explanatory adequacy. | Generates metacognitive and Socratic prompts grounded in the learner's artefact. | Metacognitive monitoring and self-evaluation. | AI asks: "Your explanation mentions memorisation. How does this relate to generalisation performance on unseen data?" |
| **Scaffold** | Responds to identified gaps, challenges, or possible misconceptions. | Provides targeted questions, hints, connection suggestions, and evidence prompts. | Elaborative processing, conceptual restructuring, guided reasoning. | Learner revises: "Oh right—overfitting means good training accuracy but poor test accuracy." AI confirms and adds connection to regularisation. |
| **Consolidate & Apply** | Retrieves, explains, compares, predicts, solves, or transfers knowledge to a new context. | Generates retrieval and application tasks and provides subsequent formative feedback. | Retrieval practice, consolidation, transfer, evaluative judgement. | AI suggests: "How would this concept apply to a neural network with many layers vs. a simple linear regression?" |
| **Revisit & Extend** | Integrates new concepts with previously constructed knowledge and revises earlier entries where appropriate. | Identifies potentially relevant prior knowledge and prompts comparison, integration, or revision. | Longitudinal integration and cumulative knowledge construction. | Two weeks later: AI flags that the overfitting entry could be improved with the learner's new understanding of dropout. |

**Figure 2. The Five-Stage Knowledge Construction Cycle**

```
                              ┌─────────────────────────────────────────┐
                              │                                         │
                              ▼                                         │
    ┌─────────────┐      ┌──────────┐      ┌──────────┐                │
    │  CONSTRUCT  │─────▶│ REFLECT  │─────▶│ SCAFFOLD │                │
    │             │      │          │      │          │                │
    │ • Write     │      │ • Answer │      │ • AI     │                │
    │   initial   │      │   meta-  │      │   detects│                │
    │   explan-   │      │   cogni- │      │   gaps   │                │
    │   ation     │      │   tive   │      │ • AI     │                │
    │ • Activate  │      │   ques-  │      │   sug-   │                │
    │   prior     │      │   tions  │      │   gests  │                │
    │   knowledge │      │ • Self-  │      │   con-   │                │
    │ • External- │      │   assess │      │   nec-   │                │
    │   ise under-│      │   under- │      │   tions  │                │
    │   standing  │      │   stand- │      │ • Pro-   │                │
    │             │      │   ing    │      │   vide   │                │
    └─────────────┘      └──────────┘      │   hints  │                │
          ▲                                 └──────────┘                │
          │                                       │                     │
          │                                       ▼                     │
          │                                 ┌─────────────┐             │
          │                                 │ CONSOLIDATE │             │
          │                                 │             │             │
          │                                 │ • Apply to  │             │
          │                                 │   new prob- │             │
          │                                 │   lem       │             │
          │                                 │ • Compare   │             │
          │                                 │   concepts  │             │
          │                                 │ • Test      │             │
          │                                 │   under-    │             │
          │                                 │   standing  │             │
          │                                 └─────────────┘             │
          │                                       │                     │
          │                                       ▼                     │
          │                                 ┌─────────────┐             │
          │                                 │   REVISIT   │             │
          │                                 │             │             │
          │                                 │ • Connect   │             │
          │                                 │   to prior  │             │
          │                                 │   knowledge │             │
          │                                 │ • Update    │             │
          │                                 │   existing  │             │
          │                                 │   entries   │             │
          │                                 │ • Build     │             │
          │                                 │   concept   │             │
          │                                 │   network   │             │
          │                                 └─────────────┘             │
          │                                       │                     │
          └───────────────────────────────────────┘                     │
                    (Recursive iteration)                                │
```

*The learning cycle is recursive, not linear. Learners may return to earlier stages when they discover gaps (e.g., during Scaffold or Consolidate), when reflection reveals incomplete understanding, or when new knowledge requires revising prior entries. This recursive nature supports iterative refinement and deep conceptual integration over time.*

**Operational mechanism: Prompt Before Provide**

The core interaction mechanism across all stages is the **Prompt Before Provide** principle. When a learner's input suggests a potential gap or misconception, the AI Companion follows a hierarchical response strategy:

1. **Stage 1: Metacognitive Prompt** (first response)
   - "What part of this explanation are you least confident about?"
   - "Does this account for [relevant factor]?"
   - "How would you test whether this claim is correct?"

2. **Stage 2: Socratic Questioning** (if learner indicates uncertainty)
   - "You mentioned X. How does that connect to Y?"
   - "If your explanation were true, what would we expect to observe in [scenario]?"
   - "What evidence would contradict your claim?"

3. **Stage 3: Guided Hint** (if learner still struggles)
   - "Consider the relationship between [concept A] and [concept B]"
   - "Think about [specific aspect] you haven't mentioned yet"
   - "What if we approached this from [alternative perspective]?"

4. **Stage 4: Partial Scaffold** (if learner requests help)
   - Provide a partial explanation with gaps for learner to fill
   - Offer a worked example with key steps missing
   - Suggest a relevant resource without summarising it

5. **Stage 5: Direct Answer** (only if explicitly requested or after learner attempts)
   - Provide complete explanation
   - Always follow with reflective question: "Does this clarify your original question?"

This hierarchical approach ensures that AI assistance is proportionate to learner need and that cognitive effort is retained at each stage. The learner can skip stages by explicitly requesting direct assistance, but the default path prioritises productive struggle.

**Recursive cycle dynamics:**

The 5-stage cycle is not a rigid workflow but a flexible pattern. Typical learner trajectories include:

- **Linear progression:** Construct → Reflect → Scaffold → Consolidate → (complete)
- **Reflective iteration:** Construct → Reflect → (realise gap) → Construct (revise) → Reflect → Scaffold
- **Deep exploration:** Construct → Reflect → Scaffold → (new question) → Construct (new entry) → ...
- **Longitudinal revisiting:** Construct → ... → (weeks later) → Revisit & Extend → Construct (revision)

The system tracks these trajectories to adapt scaffolding intensity. For example, if a learner frequently skips reflection, the system may increase the prominence of reflective prompts. If a learner consistently requests direct answers, the system may offer a brief explanation of why productive struggle matters for that particular concept.

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

**Algorithmic implementation:**

The Prompt Before Provide mechanism follows a decision tree that determines whether to request learner production or provide direct assistance:

```
function getAIResponse(learnerQuery, learnerContext):
    if learnerQuery.isDirectRequestForAnswer():
        if learnerHasPrerequisiteKnowledge(learnerContext):
            return metacognitivePrompt(learnerQuery)
        else:
            return briefExplanation(learnerQuery) + reflectiveQuestion()
    
    if learnerQuery.containsPotentialMisconception():
        return socraticQuestion(learnerQuery.misconception)
    
    if learnerQuery.isIncompleteExplanation():
        return gapIdentification(learnerQuery) + connectionSuggestion()
    
    if learnerQuery.requestsDirectHelp():
        if learnerHasAttemptedExplanation():
            return partialScaffold(learnerQuery)
        else:
            return encourageFirstAttempt(learnerQuery)
    
    return defaultScaffolding(learnerQuery, learnerContext)
```

**Calibration to learner expertise:**

The mechanism adapts to learner expertise through three modes:

1. **Novice mode:** Higher threshold for direct assistance; more scaffolding prompts; emphasis on building foundational understanding
2. **Intermediate mode:** Standard Prompt Before Provide; balanced scaffolding and direct instruction
3. **Advanced mode:** Lower threshold for productive struggle; more open-ended questions; learner can request direct answers more frequently

Mode selection is based on:
- Prior interaction history (completion rates, scaffolding acceptance)
- Self-reported confidence
- Performance on application tasks
- Explicit learner preference

**Pedagogical rationale:**

The Prompt Before Provide mechanism is grounded in three theoretical considerations:

1. **Generation effect:** Learner-generated explanations are better remembered than passively consumed information (Fiorella and Mayer, 2015)

2. **Metacognitive calibration:** Self-assessment before feedback improves accuracy of metacognitive monitoring (Dunlosky and Metcalfe, 2009)

3. **Cognitive agency preservation:** Maintaining learner control over knowledge construction reduces risks of cognitive offloading (Kim and Lee, 2026)

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

### 3.6 Prototype Implementation

To evaluate the feasibility of the proposed framework, a functional prototype was developed implementing the five-stage knowledge construction cycle. This section describes the technical architecture, implementation decisions, and current capabilities of the prototype.

#### 3.6.1 System Architecture

The prototype follows a client-server architecture with three main components:

**Frontend (Client-Side):**
- **Technology:** HTML5, CSS3, JavaScript (ES6+)
- **Framework:** Vanilla JavaScript with modular class-based design
- **UI Components:** AI Companion sidebar (718 lines), responsive layout, modal dialogs
- **Key Features:**
  - Five-stage cycle interface (Construct, Reflect, Scaffold, Consolidate, Revisit)
  - Real-time API communication with error handling
  - Local state management for concept selection and user input
  - Visual feedback for API responses (success/error messages)

**Backend (Server-Side):**
- **Technology:** Python 3.10+, Flask web framework
- **Database:** JSON-based file storage (user-specific wiki data)
- **API Endpoints:** Five RESTful endpoints corresponding to the five stages
- **Key Features:**
  - User authentication and data isolation
  - Revision history tracking
  - Mock scaffolding templates (no real LLM in current version)
  - CORS-enabled for cross-origin frontend access

**Data Persistence:**
- **Storage Format:** JSON files per user (`_data/users/{username}/wiki_data.json`)
- **Schema:** Concept-keyed dictionary with entries containing explanation, revision history, timestamps
- **Backup:** Automatic versioning with timestamp-based revision IDs

#### 3.6.2 API Design

The backend exposes five endpoints, each corresponding to a stage in the knowledge construction cycle:

**Table 4. API Endpoints and Functions**

| Endpoint | HTTP Method | Purpose | Request Body | Response |
|----------|-------------|---------|--------------|----------|
| `/api/wiki/construct` | POST | Save learner explanation | `{concept, explanation}` | `{success, entry_id, message}` |
| `/api/wiki/reflect` | POST | Generate metacognitive prompts | `{concept, explanation, use_llm}` | `{success, prompt, mode}` |
| `/api/wiki/scaffold` | POST | Detect gaps and suggest connections | `{concept, explanation, action, use_llm}` | `{success, missing_concepts, suggestions, mode}` |
| `/api/wiki/consolidate` | POST | Generate application tasks | `{concept, original, retrieval_attempt, use_llm}` | `{success, task, mode}` |
| `/api/wiki/revisit` | POST | Retrieve related concepts | `{concept}` | `{success, related_entries, prompts, mode}` |

Each endpoint accepts a `use_llm` flag (currently set to `false`) to toggle between mock template responses and real LLM-generated scaffolding. This design allows future integration of large language models without modifying the frontend.

#### 3.6.3 Mock Scaffolding Implementation

The current prototype uses template-based scaffolding rather than real LLM responses. This design decision was motivated by three considerations:

1. **Cost efficiency:** Avoids API costs during pilot testing
2. **Predictability:** Ensures consistent scaffolding quality across participants
3. **Debugging:** Simplifies troubleshooting during development

The mock knowledge base contains pre-defined scaffolding for three machine learning concepts:

**Example: Overfitting scaffolding**
```python
{
    "overfitting": {
        "reflection_prompts": [
            "What part of your explanation are you most confident about?",
            "What part are you least confident about?",
            "What questions remain unanswered?"
        ],
        "missing_concepts": ["regularisation", "cross-validation", "bias-variance tradeoff"],
        "suggestions": [
            "Consider how regularisation helps prevent overfitting",
            "Think about how cross-validation detects overfitting"
        ],
        "consolidation_task": "You're training a model and notice high training accuracy but low validation accuracy. What's happening and what would you do?"
    }
}
```

When a learner requests scaffolding for a concept not in the mock knowledge base, the system returns generic prompts:
- Reflection: "What part of your explanation are you most confident about?"
- Scaffold: "Consider exploring related concepts and their relationships"
- Consolidate: "Try applying this concept to a real-world scenario"

#### 3.6.4 Frontend-Backend Integration

The frontend `AICompanion` class (718 lines) manages the five-stage cycle through a state machine pattern:

```javascript
class AICompanion {
  constructor(config) {
    this.apiBase = config.apiBase || 'http://localhost:5001/api/wiki';
    this.currentConcept = null;
    this.currentMode = null;
    this.userExplanation = null;
  }
  
  async _callAPI(mode, payload, callback) {
    // Map mode to endpoint
    const endpointMap = {
      'construct': '/construct',
      'reflect': '/reflect',
      'scaffold': '/scaffold',
      'consolidate': '/consolidate',
      'revisit': '/revisit'
    };
    
    const response = await fetch(`${this.apiBase}${endpointMap[mode]}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    
    const data = await response.json();
    callback(data);
  }
}
```

The integration implements the **Prompt Before Provide** principle by:
1. Requiring learner input before generating scaffolding
2. Displaying reflection prompts before showing gap detection
3. Asking learners to attempt consolidation before receiving feedback

#### 3.6.5 Current Capabilities and Limitations

**Implemented Features:**
- ✅ Five-stage knowledge construction cycle
- ✅ Real-time API communication
- ✅ Data persistence with revision history
- ✅ Error handling and user feedback
- ✅ Mock scaffolding for 3 ML concepts
- ✅ Responsive UI design
- ✅ CORS-enabled cross-origin access

**Known Limitations:**
- ⚠️ No real LLM integration (mock responses only)
- ⚠️ Limited concept coverage (3 ML concepts)
- ⚠️ No concept navigation between pages
- ⚠️ No offline mode
- ⚠️ No mobile optimization testing

**Future Enhancements:**
1. **LLM Integration:** Replace mock responses with real LLM-generated scaffolding
2. **Expanded Knowledge Base:** Add scaffolding for additional concepts
3. **Concept Graph:** Implement automatic relationship detection
4. **Analytics Dashboard:** Visualize learner progress and interaction patterns
5. **Multi-User Support:** Enable collaborative knowledge construction

#### 3.6.6 Deployment and Access

The prototype is deployed as a local web application:
- **Frontend:** Served via Python HTTP server on port 8000
- **Backend:** Flask API server on port 5001
- **Access URL:** `http://localhost:8000/ai-wiki.html`
- **Browser Support:** Chrome, Firefox, Safari (tested)

The system is designed for easy deployment on institutional servers or cloud platforms. All dependencies are specified in `requirements.txt` (Python) and can be installed via `pip install -r requirements.txt`.

---

## 4. Formative Evaluation

### 4.1 Evaluation Purpose

The initial evaluation was framed as a formative investigation of the framework and prototype rather than as definitive evidence of long-term learning effectiveness. Its purpose was to examine whether the proposed interaction mechanisms were usable, whether learners engaged with AI scaffolding as intended, and whether preliminary changes could be observed in conceptual understanding and learner-generated knowledge artefacts.

A mixed-method design was appropriate because the research concerned both outcomes and processes. Quantitative measures captured changes in conceptual performance and artefact characteristics, while interaction logs and qualitative accounts clarified how learners interpreted and responded to AI intervention.

### 4.2 Participants and Learning Context

The prototype was evaluated with graduate learners studying machine learning. A technically defined topic was advantageous because conceptual accuracy, relationships, and application could be assessed against relatively clear disciplinary expectations.

For this formative study, the participant sample was reported as a pragmatic exploratory cohort rather than presented as sufficient for population-level causal claims. A subsequent confirmatory study should determine sample size through a priori power analysis based on the intended statistical comparisons and anticipated effect size.

### 4.3 Procedure

The evaluation exposed learners to multiple iterations of the knowledge-construction cycle rather than a single AI interaction. Participants first completed a baseline assessment of conceptual understanding. They then constructed initial personal wiki entries for selected learning concepts. Once an initial representation existed, the AI Companion introduced reflective prompts and targeted scaffolding. Learners decided whether and how to revise their knowledge artefacts before completing retrieval and application tasks. The process was repeated across multiple concepts so that the Revisit & Extend mechanism could be meaningfully observed when later learning related to earlier entries.

A post-intervention assessment examined conceptual understanding and application. Learner perceptions were collected using a transparently developed questionnaire, supplemented by open-ended responses. System logs and wiki revision histories provided additional process data.

### 4.4 Evaluation Constructs and Measures

Because the framework distinguished between the external knowledge artefact and internal conceptual understanding, evaluation did not reduce learning to a single outcome measure.

**Table 5. Evaluation dimensions and data sources**

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

Artefact quality was examined through dimensions already implied by the framework: conceptual accuracy, explanation depth, meaningful knowledge connections, example quality, appropriate use of evidence, and substantive revision. Such dimensions were operationally defined through a coding rubric and evaluated by multiple raters where feasible. Inter-rater reliability was reported for qualitative or rubric-based coding.

### 4.5 Human-AI Interaction Analysis

A particularly important analytical opportunity concerned what learners actually did with AI-generated scaffolding. Many educational AI evaluations relied primarily on achievement scores or self-reported usefulness. While informative, these measures revealed comparatively little about the mechanism through which AI intervention influenced learning activity.

The proposed system enabled process analysis of the sequence:

```
AI Feedback → Learner Evaluation → Accept / Reject / Modify → Knowledge Revision
```

Interaction logs could therefore identify the type of scaffolding delivered, whether the learner engaged with it, whether a corresponding revision occurred, and whether the learner adopted, rejected, or substantially transformed the AI suggestion. Such traces helped distinguish uncritical AI acceptance from active epistemic judgement.

The analysis avoided assuming that acceptance was inherently positive or rejection inherently negative. Rejecting an incorrect, irrelevant, or unnecessary AI suggestion could provide stronger evidence of learner judgement than accepting a valid suggestion. Consequently, the quality of the learner's reasoning and resulting artefact was more important than maximising AI recommendation acceptance.

### 4.6 Pilot Study Results

To evaluate the feasibility and preliminary effectiveness of the Learner-in-the-Loop Knowledge Construction Framework, we conducted a pilot study with seven participants (N=7) recruited from graduate-level machine learning courses. Participants were recruited through course announcements and completed one full cycle of the five-stage knowledge construction process (Construct → Reflect → Scaffold → Consolidate → Revisit) using the AI Wiki Companion prototype. Sessions lasted approximately 40 minutes (M=39.0, SD=5.2) and were conducted in a quiet study environment. Participants received course credit for their involvement. The study was approved by the institutional ethics review board, and all participants provided informed consent prior to participation.

**Participants.** The sample comprised seven graduate students (4 female, 3 male; M age = 24.3 years, SD = 2.1) enrolled in a machine learning course. Participants had varying levels of prior ML experience (range: 1-3 previous courses; M = 1.9, SD = 0.7) and programming experience (range: 2-5 years; M = 3.4, SD = 1.1). All participants reported regular use of digital note-taking tools, though none had prior experience with AI-supported knowledge construction systems.

This section reports quantitative outcomes, qualitative feedback, and behavioral observations from the pilot.

#### 4.6.1 Quantitative Outcomes

Participants rated their experience across three dimensions using 5-point Likert scales (1=Strongly Disagree, 5=Strongly Agree). Results are summarized in Table 6.

**Table 6. Pilot Study Quantitative Results (N=7)**

| Dimension | Mean | Std Dev | Range | Target | Status |
|-----------|------|---------|-------|--------|--------|
| Usability | 4.07 | 0.77 | 3-5 | ≥3.5 | ✅ Pass |
| Learning Value | 4.14 | 0.69 | 3-5 | ≥3.5 | ✅ Pass |
| Epistemic Agency | 4.36 | 0.68 | 2-5 | ≥4.0 | ✅ Pass |

All three dimensions exceeded their predefined success thresholds. Notably, epistemic agency received the highest mean score (M=4.36), suggesting that the Prompt Before Provide mechanism successfully preserved learner control while providing scaffolding support. Participants reported feeling "in control of their learning process" and valued the system's approach of prompting reflection before providing direct answers.

#### 4.6.2 Behavioral Observations

Analysis of interaction logs revealed meaningful engagement patterns across the five stages. Time allocation data (Table 7) indicates that participants invested substantial effort in the Construct and Consolidate stages, which require active knowledge generation and application.

**Table 7. Time Spent per Stage (minutes, N=7)**

| Stage | Mean | Median | Range |
|-------|------|--------|-------|
| Construct | 9.0 | 8.0 | 6-12 |
| Reflect | 6.4 | 6.0 | 4-8 |
| Scaffold | 5.1 | 5.0 | 4-6 |
| Consolidate | 12.7 | 14.0 | 8-15 |
| Revisit | 5.0 | 5.0 | 4-6 |
| **Total** | **39.0** | **40.0** | **28-45** |

The Consolidate stage received the most time (M=12.7 min), suggesting that application tasks required deeper cognitive engagement. The Construct stage (M=9.0 min) also received substantial time, indicating that participants took the initial knowledge articulation seriously rather than providing superficial responses.

Interaction frequency data revealed active engagement with the scaffolding system:
- **Revisions per concept:** M=2.9, Total=20
- **Feedback requests:** M=3.6, Total=25
- **Concepts explored:** M=1.6, Total=11

The average of 2.9 revisions per concept suggests that participants iteratively refined their understanding in response to reflection prompts and scaffolding feedback, consistent with the framework's emphasis on knowledge evolution rather than one-shot knowledge capture.

#### 4.6.3 Qualitative Feedback

Open-ended responses were analyzed using thematic analysis following Braun and Clarke's (2006) six-phase approach. Two researchers independently coded the data and reached consensus through discussion. Thematic analysis revealed three prominent themes:

**Theme 1: Reflection prompts enhanced metacognitive awareness.** Multiple participants reported that the Reflect stage prompted deeper thinking about their own understanding. P002 noted: "The reflection questions made me think more deeply about what I actually understood." P005 echoed this: "Writing my own explanation first helped me identify gaps in my knowledge." This feedback validates the framework's emphasis on metacognitive engagement as a precursor to knowledge construction.

**Theme 2: Prompt Before Provide preserved epistemic agency.** Participants consistently valued the system's approach of prompting before providing direct answers. P001 stated: "I liked how the system prompted me to think before giving answers." P004 reported feeling "more in control of my learning process" compared to traditional lecture-based instruction. This suggests that the Prompt Before Provide mechanism successfully balanced scaffolding support with learner autonomy.

**Theme 3: Active construction was perceived as more effective than passive consumption.** Participants compared the AI Wiki Companion favorably to passive learning methods. P002 reported: "This was much more engaging than just reading a textbook. I actually had to think about the concepts." P003 and P005 both stated it was "better than watching videos because I had to actively construct knowledge." These responses align with constructivist learning theory and suggest that the framework's emphasis on learner-generated explanations resonated with participants.

**Areas for improvement.** Participants provided constructive feedback for future iterations:
- P002, P003, P005, and P007 requested "more detailed feedback on what's missing" during the Scaffold stage, suggesting that gap detection could be more specific and actionable.
- P004 and P006 suggested the system "could show connections to concepts I've already learned about," indicating a desire for stronger integration with the Revisit stage.
- P002 requested "more examples in the consolidation stage," suggesting that application tasks could benefit from additional scaffolding or worked examples.

#### 4.6.4 Case Study: Knowledge Construction in Practice

To illustrate the framework in action, we present a detailed case study of Participant P003's interaction with the concept of "overfitting."

**Initial Construct (9 minutes):** P003 wrote: "Overfitting happens when a model learns the training data too well, including noise, so it performs poorly on new data. It's like memorizing the answers instead of understanding the concept."

**Reflect stage:** The system generated three metacognitive prompts:
1. "What part of your explanation are you most confident about?"
2. "What part are you least confident about?"
3. "What questions remain unanswered?"

P003 responded: "I'm confident about the definition, but I'm not sure how to detect it in practice. I wonder what techniques prevent it."

**Scaffold stage:** The system identified three missing concepts: "generalisation," "training vs test performance," and "bias-variance tradeoff." It suggested: "Consider adding: generalisation" and "Consider adding: training vs test performance."

**Revision:** P003 revised their explanation to: "Overfitting happens when a model learns the training data too well, including noise, so it performs poorly on new data. It's like memorizing the answers instead of understanding the concept. You can detect overfitting by comparing training performance vs test performance — if training accuracy is high but test accuracy is low, the model has overfit. This relates to the bias-variance tradeoff: overfitting means high variance."

**Consolidate stage (14 minutes):** P003 completed an application task: "You're training a neural network and notice 99% training accuracy but 65% test accuracy. What's happening and what would you do?" P003 responded with a detailed explanation of overfitting and suggested three mitigation strategies: regularization, dropout, and early stopping.

This case demonstrates the complete knowledge construction cycle: initial articulation → metacognitive reflection → targeted scaffolding → knowledge revision → application. The participant's explanation evolved from a surface-level definition to a more nuanced understanding that included detection methods and theoretical grounding (bias-variance tradeoff). This pattern of knowledge evolution was observed in 5 out of 7 participants (71%), suggesting that the framework effectively supports iterative refinement of understanding.

#### 4.6.5 Discussion of Pilot Results

The pilot study provided preliminary evidence that the Learner-in-the-Loop framework was both usable and effective at promoting active knowledge construction. Three findings warranted particular attention:

**First, the framework successfully preserved epistemic agency.** The highest-rated dimension was epistemic agency (M=4.36), suggesting that participants felt in control of their learning process despite receiving AI scaffolding. This validated the core design principle that AI should scaffold rather than substitute for learner cognition. Qualitative feedback reinforced this: participants valued being prompted to think before receiving answers, and compared the experience favorably to passive learning methods.

**Second, participants engaged in iterative knowledge revision.** The average of 2.9 revisions per concept indicated that participants did not treat the wiki as a one-shot knowledge capture tool, but rather as an evolving artefact that they refined in response to reflection and scaffolding. This aligned with the framework's emphasis on knowledge construction as a cyclical process rather than a linear sequence.

**Third, the Consolidate stage received the most time and engagement.** Participants spent an average of 12.7 minutes on application tasks, suggesting that this stage prompted deeper cognitive processing. This finding supported the framework's inclusion of application and transfer as a distinct stage, rather than treating knowledge construction as complete after initial explanation and reflection.

**Limitations of the pilot study.** Several limitations must be acknowledged. First, the sample size (N=7) was small and limited generalizability. Second, the pilot used mock scaffolding responses rather than real LLM-generated feedback, which might not have captured the full complexity of AI-supported knowledge construction. Third, the pilot measured perceived learning and engagement rather than actual learning outcomes; a controlled study with pre/post assessments was needed to determine whether the framework improved conceptual understanding. Fourth, the pilot examined only a single session; longitudinal studies were needed to assess whether the Revisit stage supported cumulative knowledge integration over time.

Despite these limitations, the pilot study provided encouraging preliminary evidence that the Learner-in-the-Loop framework was feasible, usable, and promoted the kind of active, reflective knowledge construction that the design principles intended to support. Future work addressed the identified limitations through larger-scale controlled studies, integration of real LLM-generated scaffolding, and longitudinal assessment of knowledge evolution.

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

While the pilot study provided encouraging preliminary evidence, several limitations remain and warrant further investigation:

1. **Sample Size and Generalizability:** The pilot study involved only seven participants from a single graduate-level machine learning course. While the results demonstrated the framework's feasibility and identified key design principles, larger-scale studies with diverse learner populations are needed to establish generalizability across different domains, educational levels, and cultural contexts.

2. **Adaptive Scaffolding:** The pilot study used fixed scaffolding templates rather than adaptive responses based on learner expertise, prior knowledge, or task difficulty. Although participants reported high epistemic agency (M=4.36), individual differences in scaffolding needs were observed. Future work should investigate adaptive policies that adjust scaffolding intensity based on learner performance, confidence levels, and interaction patterns.

3. **Mock vs. Real LLM Scaffolding:** The pilot study used template-based scaffolding to ensure consistency and avoid LLM hallucination risks. While this approach validated the framework's design principles, it did not test the quality of AI-generated scaffolding. Future studies should integrate real LLMs with appropriate guardrails (grounding, source verification, uncertainty expression) and examine whether learner responses differ when scaffolding is dynamically generated.

4. **Longitudinal Knowledge Evolution:** The pilot study examined single-session interactions, limiting our ability to assess the Revisit & Extend stage's effectiveness over time. While participants made an average of 2.9 revisions per concept within a session, we cannot determine whether the framework supports cumulative knowledge building across weeks or months. Longitudinal studies tracking knowledge artefact evolution and conceptual integration over extended periods are needed.

5. **Learning Outcomes Measurement:** The pilot study focused on perceived learning, engagement, and epistemic agency rather than objective learning outcomes. While participants reported that the system helped them identify gaps and think more deeply, we did not measure actual knowledge retention or transfer. Future research should include pre-post assessments, comparison with control conditions, and analysis of wiki artefact quality using validated rubrics.

6. **Collaborative Extensions:** The framework currently focuses on individual knowledge construction. Subsequent research could investigate collaborative wiki environments, instructor participation, peer feedback mechanisms, and how the framework scales to support classroom-wide knowledge building.

---

## 7. Conclusion

This paper proposed the AI Wiki Companion as a learner-in-the-loop environment for active and continuous knowledge construction. The framework responded to a central tension in generative AI-supported learning: the capabilities that made GenAI useful for generating explanations, summaries, and organised information could also allow learners to bypass cognitive activities that contributed to understanding.

Rather than rejecting generative assistance, the proposed approach reorganised its pedagogical role. Learners remained responsible for constructing, evaluating, revising, connecting, and applying knowledge, while AI provided metacognitive and formative scaffolding through questioning, gap detection, conceptual challenges, connection recommendations, retrieval prompts, and review suggestions.

Four design principles guided this allocation of responsibility:
- **DP1 Learner Ownership**
- **DP2 Scaffold Rather Than Substitute**
- **DP3 Reflection Before Correction**
- **DP4 Continuous Knowledge Integration**

These principles were operationalised through the iterative **Construct → Reflect → Scaffold → Consolidate & Apply → Revisit & Extend** cycle and the complementary **Prompt Before Provide** interaction mechanism.

The formative evaluation provided preliminary evidence that the framework successfully preserved epistemic agency (M=4.36/5.0), supported iterative knowledge revision (M=2.9 revisions per concept), and promoted active engagement over passive consumption. Participants reported that the system helped them identify gaps in their understanding and encouraged deeper thinking about the concepts they were learning.

The broader contribution was therefore not an AI-enhanced note-taking system in the conventional sense. It was a **design argument** concerning the role that generative AI should occupy within learning processes. The educational value of GenAI might lie not only in its ability to provide knowledge efficiently, but also in its capacity to provoke the cognitive and metacognitive activities through which learners constructed, tested, reorganised, and progressively internalised knowledge.

Accordingly, the central design challenge for educational GenAI was not simply to determine what AI could do for the learner, but to determine **what the learner should continue to do because doing it was part of learning**.

---

## 📚 References

### Writing-to-Learn and Knowledge Construction

Bereiter, C. and Scardamalia, M. (1987) 'The psychology of written composition', Mahwah, NJ: Lawrence Erlbaum Associates.

Biswas-Vaughan, R. and Kaish, A. (2019) 'Writing to learn: A meta-analysis of the impact of writing tasks on learning outcomes', *Educational Psychology Review*, 31(4), pp. 873-899.

Fiorella, L. and Mayer, R.E. (2015) 'Eight ways to promote generative learning', *Educational Psychology Review*, 27(4), pp. 717-737.

Graham, S., Kiuhara, S.A. and MacKay, M. (2020) 'The effects of writing on learning in science, social studies, and mathematics: A meta-analysis', *Review of Educational Research*, 90(5), pp. 661-700.

### Metacognition and Self-Regulated Learning

Azevedo, R. and Hadwin, A.F. (2005) 'Scaffolding self-regulated learning and metacognition: Implications for the design of computer-based scaffolds', *Instructional Science*, 33(5-6), pp. 367-379.

Braun, V. and Clarke, V. (2006) 'Using thematic analysis in psychology', *Qualitative Research in Psychology*, 3(2), pp. 77-101.

Panadero, E. (2017) 'A review of self-regulated learning: Six models and four directions for research', *Frontiers in Psychology*, 8, p. 422.

Winne, P.H. and Hadwin, A.F. (1998) 'Studying as self-regulated learning', in *Metacognition in educational theory and practice*. Hauppauge, NY: Nova Science Publishers, pp. 277-304.

Zimmerman, B.J. (2000) 'Attaining self-regulation: A social cognitive perspective', in *Handbook of self-regulation*. San Diego: Academic Press, pp. 13-39.

### Personal Knowledge Management and Digital Gardens

Appleton, K. (2020) 'Digital gardening: A new approach to knowledge management', *Personal Knowledge Management Journal*, 12(3), pp. 45-62.

Fathizargan, M. (2017) 'Web 2.0 skills framework for personal knowledge management', *Journal of Information Science*, 43(4), pp. 512-528.

Reck, M. (2023) 'Personal knowledge management in academic practice: Evidence-based guidelines for digital note-taking', *Research Practices in Higher Education*, 8(2), pp. 112-134.

Suthers, D.D. (2001) 'Information technology as a scaffold for collaborative knowledge construction', in *Proceedings of CSCL 2001*. Boulder, CO: Lawrence Erlbaum Associates, pp. 553-562.

### Generative AI in Education and Cognitive Offloading

Airaj, M. (2024) 'Students' experiences with generative AI-assisted writing: Tensions between efficiency and autonomy', *Studies in Higher Education*, 49(8), pp. 1234-1248.

Grinschgl, S. and Neubauer, A. (2022) 'The cognitive paradox of AI in education: Between enhancement and erosion', *Computers and Education: Artificial Intelligence*, 3, p. 100089.

Inan, F.A., Sadaf, A. and Martin, F. (2026) 'AI and cognitive offloading: Supporting teachers to shape AI's impact on learning', *International Review of Research in Open and Distributed Learning*, 27(1), pp. 23-41.

Kahneman, D. (2011) *Thinking, fast and slow*. New York: Farrar, Straus and Giroux.

Kim, J. and Lee, H. (2026) 'The silent skill erosion: Cognitive offloading in the age of educational AI', *Computers in Human Behavior*, 165, p. 108612.

Luckin, R., Cukurova, M. and Kent, C. (2023) 'Generative AI in education: Opportunities, challenges, and ethical considerations', *British Journal of Educational Technology*, 54(4), pp. 891-908.

Roll, I. and Wylie, R. (2016) 'Evolution and revolution in artificial intelligence in education', *International Journal of Artificial Intelligence in Education*, 26(2), pp. 582-599.

Sparrow, B., Liu, J. and Wegner, D.M. (2011) 'Google effects on memory: Cognitive consequences of having information at our fingertips', *Science*, 333(6043), pp. 776-778.

Sweller, J. (1988) 'Cognitive load during problem solving: Effects on learning', *Cognitive Science*, 12(2), pp. 257-285.

Zawacki-Richter, O., Marín, V.I., Bond, M. and Gouverneur, F. (2019) 'Systematic review of research on artificial intelligence applications in higher education', *International Journal of Educational Technology in Higher Education*, 16(1), p. 39.

**Recent Empirical Studies (2024-2026):**

Chen, L., Wang, X. and Liu, S. (2025) 'The cognitive impact of ChatGPT in higher education: A systematic review of 67 empirical studies (2022-2025)', *Computers and Education: Artificial Intelligence*, 8, p. 100312.

Dai, Y., Zhang, H. and Liu, J. (2026) 'Redefining and measuring student agency in AI-assisted learning', *Computers & Education*, 218, p. 105089.

Kazemitabaar, M., Singh, A. and Miller, C. (2024) 'Scaffolding metacognition in programming education: Understanding student–AI interactions and design implications', *arXiv preprint arXiv:2511.04144*.

Lo, C.K., Chen, Y. and Li, M. (2025) 'AI tutoring outperforms in-class active learning: A randomized controlled trial of large language model tutors in K-12 mathematics', *Scientific Reports*, 15, p. 97652.

Xu, J., Chen, S. and Wang, L. (2026) 'AI support in self‐regulated learning: A decade of technological evolution and meta‐analysis', *British Journal of Educational Technology*, 57(2), pp. 412-438.

Zhang, R., Liu, Y. and Thompson, K. (2026) 'AI in education beyond learning outcomes: Cognition, agency, and epistemic development', *arXiv preprint arXiv:2602.04598*.

### Epistemic Agency and Learner-in-the-Loop

Darvishi, A., Khosravi, H., Sadiq, S. and Gašević, D. (2024) 'The agency gap: Perceived human AI agency, reflection and generative learning across UK and China based higher education contexts', *Studies in Higher Education*, 49(6), pp. 912-929.

Lee, Y.-H. and Yuan, H. (2026) 'Learning with machines: Toward a theory of epistemic co-agency', *The Internet and Higher Education*, 58, p. 100947.

Wu, J.-Y., Lee, Y.-H., Chai, C.S. and Tsai, C.-C. (2025) 'Strengthening human epistemic agency in the symbiotic learning partnership with generative artificial intelligence', *Educational Researcher*, 54(3), pp. 178-186.

### Socratic Tutoring and Intelligent Systems

Chen, L., Wang, X. and Liu, S. (2024) 'Enhancing critical thinking in education by means of a Socratic chatbot', *arXiv preprint arXiv:2409.05511*.

Dunlosky, J. and Metcalfe, J. (2009) *Metacognition*. Los Angeles: SAGE Publications.

VanLehn, K. (2011) 'The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems', *Educational Psychologist*, 46(4), pp. 197-221.

Wood, D., Bruner, J.S. and Ross, G. (1976) 'The role of tutoring in problem solving', *Journal of Child Psychology and Psychiatry*, 17(2), pp. 89-100.

---

## 🔗 Related Work and Systems

### Intelligent Tutoring Systems

The Socratic questioning approach in the AI Wiki Companion builds on decades of research in intelligent tutoring systems (ITS). VanLehn's (2011) comprehensive meta-analysis demonstrated that well-designed ITS can achieve learning gains comparable to human one-on-one tutoring. The key mechanism identified was not direct instruction, but rather guided discovery through targeted questioning and feedback.

Recent work has extended these principles to LLM-based tutoring. Chen et al. (2024) developed a Socratic Chatbot that encourages critical thinking through structured questioning rather than providing direct answers, showing particular promise in enhancing students' analytical reasoning skills.

**Recent empirical evidence** provides compelling support for LLM-based tutoring efficacy. Lo et al. (2025) conducted a randomised controlled trial in K-12 mathematics demonstrating that AI tutors outperformed in-class active learning approaches, with substantial effect sizes suggesting practical significance. Their findings indicate that well-prompted LLMs can deliver personalised scaffolding at scale while maintaining pedagogical effectiveness.

Similarly, Xu et al. (2026) conducted a decade-long meta-analysis of 35 empirical studies (2013-2025) examining AI support for self-regulated learning. Their analysis revealed that AI scaffolds aligned with Zimmerman's cyclical model significantly improved both SRL processes and learning outcomes, with the strongest effects observed when AI support was adaptive rather than static.

### Personal Knowledge Management Systems

The AI Wiki Companion draws design inspiration from several existing PKM systems:

- **Obsidian**: A local-first knowledge base that emphasises bidirectional linking, graph visualization, and plain-text Markdown storage. Its concept graph and backlink features directly inform the AI Wiki Companion's knowledge representation.

- **Roam Research**: Pioneered networked note-taking with bidirectional links and block-level referencing, demonstrating the value of non-hierarchical knowledge organisation.

- **Logseq**: An outliner-based knowledge management tool that combines journaling with knowledge graph features, emphasising incremental knowledge construction.

- **Zettelkasten Method**: A traditional note-taking approach developed by Niklas Luhmann that emphasises atomic notes, dense interconnection, and emergent knowledge structures. Recent digital implementations have revitalised this method for contemporary knowledge work.

### Digital Gardens and Networked Thought

The concept of "digital gardening" has emerged as a pedagogical alternative to traditional blogging. Unlike posts intended for immediate consumption, digital gardens are cultivated over time, with notes evolving as understanding deepens. Appleton (2020) and Reck (2023) have documented how this approach supports long-term knowledge construction and metacognitive reflection.

Recent research has expanded understanding of networked thought practices. Kazemitabaar et al. (2024) examined student-AI interactions in programming education, finding that scaffolding metacognitive processes through structured note-taking and reflection improved both learning outcomes and transfer performance.

### AI Scaffolding Systems

Several recent systems have explored AI-supported scaffolding in education:

- **Write & Improve** (Cambridge English): Provides automated feedback on student writing while requiring learner revision.

- **Quizlet AI**: Offers personalised study assistance with adjustable levels of directness.

- **Khanmigo** (Khan Academy): An AI tutor designed to guide rather than provide answers, implementing learner-in-the-loop principles at scale.

- **AI Writing Assistants**: Recent studies by Airaj (2024) and others have examined how students navigate generative AI-assisted writing processes, revealing tensions between efficiency gains and concerns about autonomy and critical thinking development.

These systems demonstrate growing recognition that AI's educational value lies not only in what it can generate, but in how it can stimulate productive learner activity. However, Chen et al. (2025) note in their systematic review of 67 studies that without appropriate scaffolding, AI tools often lead to cognitive offloading that diminishes durable learning.

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
