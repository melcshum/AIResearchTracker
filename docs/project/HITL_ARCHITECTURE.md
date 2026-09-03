# Human-in-the-Loop (HITL) Architecture Design

## Executive Summary

This document outlines the architecture for integrating Human-in-the-Loop (HITL) mechanisms into the AI Research Tracker system. The goal is to create a collaborative learning environment where AI assists users while users continuously improve AI outputs through feedback, corrections, and contributions.

---

## 1. Core HITL Principles

### 1.1 Design Philosophy

**AI-Assisted, Human-Driven Learning**
- AI provides initial content, recommendations, and analysis
- Users validate, correct, and enhance AI outputs
- System learns from user interactions to improve over time
- Users maintain full control and ownership of their learning journey

### 1.2 Key Objectives

1. **Improve AI Accuracy** - User corrections refine extraction, summarization, and recommendations
2. **Deepen Learning** - Active engagement through annotation and feedback enhances retention
3. **Personalize Experience** - System adapts to individual learning styles and research interests
4. **Build Trust** - Transparency in AI decisions + user control = confidence in the system
5. **Create Knowledge Graph** - User contributions enrich the collective knowledge base

---

## 2. HITL Feature Categories

### Category A: Validation & Correction
Users validate and correct AI-generated content.

| Feature | Description | Impact |
|---------|-------------|--------|
| **Summary Correction** | Edit AI-generated paper summaries | Improves summarization quality |
| **Concept Validation** | Confirm/reject extracted concepts | Improves concept extraction accuracy |
| **Relationship Verification** | Validate concept-paper links | Improves knowledge graph quality |
| **Citation Checking** | Verify AI-extracted citations | Improves citation extraction |

### Category B: Active Annotation
Users add personal annotations and insights.

| Feature | Description | Impact |
|---------|-------------|--------|
| **Text Highlighting** | Mark important passages | Creates personal knowledge base |
| **Margin Notes** | Add comments to paper sections | Captures insights and questions |
| **Tagging System** | Add custom tags to papers | Improves personal organization |
| **Question Tracking** | Log research questions | Drives targeted discovery |

### Category C: Feedback & Rating
Users provide explicit feedback on AI outputs.

| Feature | Description | Impact |
|---------|-------------|--------|
| **Recommendation Rating** | Rate paper recommendations | Improves recommendation algorithm |
| **Summary Quality Score** | Rate summary helpfulness | Improves summarization |
| **Learning Path Feedback** | Rate learning path relevance | Improves path generation |
| **Search Relevance** | Rate search result quality | Improves search ranking |

### Category D: User Contributions
Users contribute original content.

| Feature | Description | Impact |
|---------|-------------|--------|
| **Concept Explanations** | Write personal explanations | Enriches wiki with diverse perspectives |
| **Examples & Use Cases** | Add practical examples | Makes concepts more concrete |
| **Related Work Notes** | Document connections between papers | Builds knowledge graph |
| **Study Guides** | Create custom study materials | Personalizes learning resources |

### Category E: Adaptive Learning
System adapts based on user behavior.

| Feature | Description | Impact |
|---------|-------------|--------|
| **Spaced Repetition Control** | Adjust review intervals | Optimizes memory retention |
| **Difficulty Adjustment** | Modify content complexity | Matches skill level |
| **Learning Path Customization** | Adjust path parameters | Personalizes learning journey |
| **Content Prioritization** | Mark topics as high/low priority | Focuses AI attention |

---

## 3. Data Model Design

### 3.1 Core Data Structures

#### User Feedback Schema
```json
{
  "feedback_id": "uuid",
  "user_id": "string",
  "timestamp": "ISO8601",
  "target_type": "summary|concept|recommendation|search_result",
  "target_id": "string",
  "feedback_type": "correction|validation|rating|annotation",
  "feedback_data": {
    // Varies by feedback_type
  },
  "metadata": {
    "context": "string",
    "confidence": "number (0-1)",
    "tags": ["string"]
  }
}
```

#### Annotation Schema
```json
{
  "annotation_id": "uuid",
  "user_id": "string",
  "paper_id": "string",
  "timestamp": "ISO8601",
  "type": "highlight|note|question|bookmark",
  "content": {
    "text": "string (for highlights)",
    "position": {
      "start_offset": "number",
      "end_offset": "number",
      "section": "string"
    },
    "note": "string (for notes/questions)",
    "color": "string (for highlights)"
  },
  "metadata": {
    "tags": ["string"],
    "is_private": "boolean",
    "related_annotations": ["uuid"]
  }
}
```

#### User Contribution Schema
```json
{
  "contribution_id": "uuid",
  "user_id": "string",
  "timestamp": "ISO8601",
  "type": "explanation|example|study_guide|related_work",
  "target_concept": "string (for explanations)",
  "target_paper": "string (for related_work)",
  "content": {
    "title": "string",
    "body": "string (markdown)",
    "examples": ["string"],
    "references": ["string"]
  },
  "metadata": {
    "version": "number",
    "upvotes": "number",
    "is_approved": "boolean",
    "tags": ["string"]
  }
}
```

#### Learning Preference Schema
```json
{
  "user_id": "string",
  "preferences": {
    "learning_style": "visual|textual|interactive",
    "difficulty_level": "number (1-5)",
    "daily_goal": {
      "papers": "number",
      "minutes": "number"
    },
    "focus_areas": {
      "concept_id": "priority (high|medium|low)"
    },
    "spaced_repetition": {
      "interval_multiplier": "number",
      "max_cards_per_day": "number"
    }
  },
  "history": {
    "last_active": "ISO8601",
    "total_papers_read": "number",
    "total_annotations": "number",
    "streak_days": "number"
  }
}
```

### 3.2 Database Schema

#### Tables

**feedback_log**
- Stores all user feedback for AI improvement
- Indexed by: user_id, target_type, timestamp

**annotations**
- User annotations on papers
- Indexed by: user_id, paper_id, type

**user_contributions**
- User-generated content (explanations, examples, etc.)
- Indexed by: user_id, type, target_concept

**learning_preferences**
- User learning settings and history
- Indexed by: user_id

**concept_validations**
- Tracks which users validated which concepts
- Indexed by: concept_id, user_id

**recommendation_ratings**
- User ratings on paper recommendations
- Indexed by: user_id, paper_id

---

## 4. API Design

### 4.1 Feedback APIs

```python
# Submit feedback on AI output
POST /api/feedback
{
  "target_type": "summary",
  "target_id": "paper_123",
  "feedback_type": "correction",
  "feedback_data": {
    "original": "AI-generated summary",
    "corrected": "User-corrected summary"
  }
}

# Get feedback history
GET /api/feedback/history?user_id=xxx&target_type=summary

# Get aggregated feedback for AI training
GET /api/feedback/aggregated?target_type=summary&min_confidence=0.8
```

### 4.2 Annotation APIs

```python
# Create annotation
POST /api/annotations
{
  "paper_id": "paper_123",
  "type": "highlight",
  "content": {
    "text": "Important finding",
    "position": {"start_offset": 100, "end_offset": 150},
    "color": "#FFD700"
  }
}

# Get annotations for paper
GET /api/annotations?paper_id=paper_123&user_id=xxx

# Update annotation
PUT /api/annotations/{annotation_id}

# Delete annotation
DELETE /api/annotations/{annotation_id}
```

### 4.3 Contribution APIs

```python
# Submit contribution
POST /api/contributions
{
  "type": "explanation",
  "target_concept": "Chain-of-Thought",
  "content": {
    "title": "Practical Guide to CoT",
    "body": "Markdown content...",
    "examples": ["Example 1", "Example 2"]
  }
}

# Get contributions for concept
GET /api/contributions?target_concept=Chain-of-Thought&type=explanation

# Upvote contribution
POST /api/contributions/{contribution_id}/upvote

# Get user contributions
GET /api/contributions/user/{user_id}
```

### 4.4 Learning Preference APIs

```python
# Get user preferences
GET /api/preferences/{user_id}

# Update preferences
PUT /api/preferences/{user_id}
{
  "difficulty_level": 4,
  "daily_goal": {"papers": 5, "minutes": 60},
  "focus_areas": {"ai-agents": "high", "reasoning": "medium"}
}

# Get learning statistics
GET /api/preferences/{user_id}/stats
```

### 4.5 Recommendation APIs (with HITL)

```python
# Get personalized recommendations
GET /api/recommendations?user_id=xxx&count=10

# Rate recommendation
POST /api/recommendations/{paper_id}/rate
{
  "rating": "helpful|somewhat|not_relevant",
  "reason": "string (optional)"
}

# Get recommendation feedback history
GET /api/recommendations/history?user_id=xxx
```

---

## 5. UI/UX Design

### 5.1 Feedback Components

#### Summary Correction Interface
```
┌─────────────────────────────────────────────┐
│ 📄 Paper Summary                            │
├─────────────────────────────────────────────┤
│ [AI-Generated Summary]                      │
│ "This paper presents a novel approach..."   │
│                                             │
│ [✏️ Edit Summary] [👍 Helpful] [👎 Not Good] │
└─────────────────────────────────────────────┘

When user clicks "Edit Summary":
┌─────────────────────────────────────────────┐
│ ✏️ Edit Summary                             │
├─────────────────────────────────────────────┤
│ [Text Editor with AI summary pre-filled]    │
│                                             │
│ [💾 Save Correction] [❌ Cancel]            │
│                                             │
│ ☐ Don't show this feedback prompt again    │
└─────────────────────────────────────────────┘
```

#### Concept Validation Interface
```
┌─────────────────────────────────────────────┐
│ 🧠 AI Extracted Concepts                    │
├─────────────────────────────────────────────┤
│ ☑ AI Agent                    [❌ Remove]   │
│ ☑ Multi-Agent Systems         [❌ Remove]   │
│ ☐ Planning                    [✅ Confirm]  │
│                                             │
│ ➕ Add Missing Concept                      │
│                                             │
│ [💾 Save Validations]                       │
└─────────────────────────────────────────────┘
```

### 5.2 Annotation Components

#### Paper Reader with Annotation Tools
```
┌─────────────────────────────────────────────┐
│ 📖 Paper Title                              │
├─────────────────────────────────────────────┤
│ [Highlight Tool] [Note Tool] [Question]     │
├─────────────────────────────────────────────┤
│                                             │
│ Abstract                                    │
│ ─────────                                   │
│ This paper presents [highlighted text]      │
│ with a novel approach to... [💬 Note]       │
│                                             │
│ [Sidebar: Annotations Panel]                │
│ • 3 highlights                              │
│ • 2 notes                                   │
│ • 1 question                                │
│                                             │
└─────────────────────────────────────────────┘
```

#### Annotation Sidebar
```
┌───────────────────────────────┐
│ 📝 Annotations (6)            │
├───────────────────────────────┤
│ 🖍 Highlights (3)             │
│ • "novel approach to..."      │
│ • "key finding that..."       │
│ • "future work should..."     │
│                               │
│ 💬 Notes (2)                  │
│ • "Compare with Smith 2024"   │
│ • "Need to verify claim..."   │
│                               │
│ ❓ Questions (1)              │
│ • "How does this scale?"      │
└───────────────────────────────┘
```

### 5.3 Contribution Components

#### Concept Explanation Editor
```
┌─────────────────────────────────────────────┐
│ 📚 Contribute: Chain-of-Thought Explanation │
├─────────────────────────────────────────────┤
│ Title: [________________________________]   │
│                                             │
│ Body (Markdown):                            │
│ ┌─────────────────────────────────────────┐ │
│ │ Chain-of-Thought (CoT) is a prompting...│ │
│ │                                         │ │
│ │ ## Key Points                           │ │
│ │ • Step-by-step reasoning                │ │
│ │ • Improves complex task performance     │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Examples:                                   │
│ [+ Add Example]                             │
│                                             │
│ Tags: [reasoning] [prompting] [+ Add]       │
│                                             │
│ [👁 Preview] [💾 Submit] [❌ Cancel]        │
└─────────────────────────────────────────────┘
```

### 5.4 Adaptive Learning Components

#### Learning Path Customizer
```
┌─────────────────────────────────────────────┐
│ 🎯 Customize Your Learning Path             │
├─────────────────────────────────────────────┤
│                                             │
│ Difficulty Level:                           │
│ [Beginner] [●●●●○] [Advanced]              │
│                                             │
│ Daily Goal:                                 │
│ Papers: [5 ▼]  Minutes: [60 ▼]             │
│                                             │
│ Focus Areas:                                │
│ ☑ AI Agents          [High ▼]              │
│ ☑ Reasoning          [Medium ▼]            │
│ ☐ Multi-Modal        [Low ▼]               │
│ ☐ RAG & Retrieval    [Low ▼]               │
│                                             │
│ Learning Style:                             │
│ (●) Textual  ( ) Visual  ( ) Interactive   │
│                                             │
│ [🔄 Regenerate Path] [💾 Save Preferences]  │
└─────────────────────────────────────────────┘
```

#### Spaced Repetition Control
```
┌─────────────────────────────────────────────┐
│ 🔄 Review: Chain-of-Thought                 │
├─────────────────────────────────────────────┤
│                                             │
│ Definition:                                 │
│ A prompting technique that encourages...    │
│                                             │
│ How well do you know this concept?          │
│                                             │
│ [😟 Again]  [🤔 Hard]  [😊 Good]  [😎 Easy] │
│  (1 day)    (3 days)   (7 days)  (14 days) │
│                                             │
│ [📝 Add Note] [👁 Show Answer]              │
└─────────────────────────────────────────────┘
```

---

## 6. User Workflows

### Workflow 1: Reading a Paper with HITL

```
1. User opens paper in reader
   ↓
2. AI displays: summary, extracted concepts, key findings
   ↓
3. User reads and interacts:
   • Highlights important passages
   • Adds notes to sections
   • Logs questions that arise
   ↓
4. User validates AI outputs:
   • Confirms/corrects extracted concepts
   • Rates summary quality
   • Suggests missing concepts
   ↓
5. System saves all interactions:
   • Annotations stored in user profile
   • Feedback logged for AI improvement
   • Questions added to research tracker
   ↓
6. System updates recommendations:
   • Adjusts future paper suggestions
   • Updates concept difficulty estimates
   • Refines user's learning path
```

### Workflow 2: Contributing to Knowledge Base

```
1. User explores wiki and finds concept
   ↓
2. User clicks "Contribute Explanation"
   ↓
3. User writes explanation with examples
   ↓
4. System validates contribution:
   • Checks for minimum length
   • Scans for inappropriate content
   • Suggests related concepts
   ↓
5. Contribution enters review queue:
   • Other users can upvote/downvote
   • Moderators can approve/reject
   ↓
6. Approved contribution appears in wiki:
   • Attributed to user
   • Included in concept page
   • Used to improve AI explanations
```

### Workflow 3: Adaptive Learning Loop

```
1. User sets learning preferences:
   • Difficulty level
   • Daily goals
   • Focus areas
   ↓
2. System generates personalized learning path
   ↓
3. User follows path and provides feedback:
   • Rates paper relevance
   • Adjusts difficulty as needed
   • Marks topics as complete
   ↓
4. System analyzes feedback:
   • Identifies knowledge gaps
   • Detects learning patterns
   • Adjusts difficulty dynamically
   ↓
5. System updates learning path:
   • Recommends next papers
   • Schedules spaced repetition
   • Suggests related concepts
   ↓
6. Loop continues with improved personalization
```

---

## 7. AI Improvement Pipeline

### 7.1 Feedback Collection

```python
# Collect user feedback
feedback_data = {
  "summary_corrections": get_corrections(target_type="summary"),
  "concept_validations": get_validations(target_type="concept"),
  "recommendation_ratings": get_ratings(target_type="recommendation"),
  "annotation_patterns": get_annotation_patterns()
}
```

### 7.2 Feedback Aggregation

```python
# Aggregate feedback for training
aggregated = {
  "summary_quality": calculate_avg_rating("summary"),
  "concept_accuracy": calculate_validation_rate("concept"),
  "recommendation_relevance": calculate_rating_distribution("recommendation"),
  "common_corrections": extract_correction_patterns()
}
```

### 7.3 Model Fine-Tuning

```python
# Use feedback to fine-tune models
if aggregated["summary_quality"] < 0.7:
  fine_tune_summarization_model(feedback_data["summary_corrections"])

if aggregated["concept_accuracy"] < 0.8:
  fine_tune_extraction_model(feedback_data["concept_validations"])

if aggregated["recommendation_relevance"] < 0.6:
  update_recommendation_algorithm(feedback_data["recommendation_ratings"])
```

### 7.4 Continuous Improvement Loop

```
User Feedback → Aggregation → Analysis → Model Update → Better AI → More User Trust → More Feedback
```

---

## 8. Implementation Phases

### Phase 1: Foundation (Weeks 1-2)
**Goal:** Basic feedback and annotation infrastructure

- [ ] Design and implement feedback data model
- [ ] Create feedback API endpoints
- [ ] Build annotation data model and APIs
- [ ] Implement basic UI for summary correction
- [ ] Add annotation toolbar to paper reader
- [ ] Create feedback storage and retrieval

**Deliverables:**
- Users can correct AI summaries
- Users can highlight text and add notes
- Feedback is stored in database

### Phase 2: Validation & Rating (Weeks 3-4)
**Goal:** Concept validation and recommendation feedback

- [ ] Build concept validation interface
- [ ] Implement recommendation rating system
- [ ] Create feedback aggregation pipeline
- [ ] Add feedback visualization dashboard
- [ ] Implement feedback-driven recommendation updates

**Deliverables:**
- Users can validate extracted concepts
- Users can rate paper recommendations
- System uses feedback to improve recommendations

### Phase 3: User Contributions (Weeks 5-6)
**Goal:** User-generated content system

- [ ] Design contribution data model
- [ ] Build contribution editor UI
- [ ] Implement contribution review workflow
- [ ] Create upvoting system
- [ ] Integrate contributions into wiki

**Deliverables:**
- Users can write concept explanations
- Contributions appear in wiki
- Community can vote on contributions

### Phase 4: Adaptive Learning (Weeks 7-8)
**Goal:** Personalized learning with user control

- [ ] Build learning preference system
- [ ] Create learning path customizer
- [ ] Implement spaced repetition with user control
- [ ] Add difficulty adjustment interface
- [ ] Create learning analytics dashboard

**Deliverables:**
- Users can customize learning paths
- Spaced repetition adapts to user feedback
- Learning analytics show progress

### Phase 5: AI Improvement Pipeline (Weeks 9-10)
**Goal:** Closed-loop AI improvement

- [ ] Build feedback aggregation system
- [ ] Create model fine-tuning pipeline
- [ ] Implement A/B testing for AI improvements
- [ ] Add feedback impact visualization
- [ ] Create automated retraining triggers

**Deliverables:**
- AI models improve based on user feedback
- System measures impact of feedback
- Continuous improvement loop established

---

## 9. Success Metrics

### User Engagement Metrics
- **Feedback Rate:** % of AI outputs that receive user feedback
- **Annotation Density:** Average annotations per paper
- **Contribution Rate:** % of users who contribute content
- **Retention Rate:** % of users who return weekly

### AI Quality Metrics
- **Correction Rate:** % of AI outputs that are corrected (lower = better)
- **Validation Rate:** % of AI outputs that are validated (higher = better)
- **Recommendation Relevance:** Average rating of recommendations
- **Summary Quality:** Average rating of summaries

### Learning Outcome Metrics
- **Knowledge Retention:** Spaced repetition success rate
- **Learning Velocity:** Papers read per week over time
- **Concept Mastery:** % of concepts marked as "learned"
- **Research Progress:** Questions answered over time

---

## 10. Technical Considerations

### 10.1 Performance
- Feedback operations should complete in < 200ms
- Annotation rendering should not slow paper loading
- Contribution queries should be cached

### 10.2 Scalability
- Feedback log should support millions of entries
- Annotation storage should be efficient (use compression)
- Contribution system should handle concurrent edits

### 10.3 Security
- User contributions should be sanitized
- Feedback should be authenticated
- Annotations should be private by default

### 10.4 Privacy
- Users control what feedback is shared
- Annotations are private unless explicitly shared
- Contributions can be anonymous

---

## 11. Future Enhancements

### Phase 6+: Advanced Features
- **Collaborative Annotations:** Share annotations with research groups
- **AI Tutor:** Personalized AI tutor based on learning patterns
- **Knowledge Graph Visualization:** Interactive graph of user's knowledge
- **Research Assistant:** AI assistant that learns from user's research style
- **Cross-User Learning:** Learn from other users' feedback (opt-in)

---

## 12. Conclusion

This HITL architecture creates a collaborative learning ecosystem where:
- **Users** actively shape their learning experience
- **AI** continuously improves from user feedback
- **Knowledge** grows through community contributions
- **Learning** becomes personalized and adaptive

The phased implementation ensures we deliver value quickly while building toward a comprehensive HITL system. Each phase builds on the previous, creating a robust foundation for AI-assisted, human-driven research learning.

---

## Appendix A: Example User Stories

### Story 1: Researcher Corrects AI Summary
**As a** researcher reading a paper on multi-agent systems  
**I want to** correct the AI-generated summary  
**So that** it accurately reflects the paper's contributions  
**And** the system learns from my correction

**Acceptance Criteria:**
- User can click "Edit Summary" button
- Editor opens with AI summary pre-filled
- User can modify text and save
- Correction is stored and linked to paper
- Future summaries for similar papers incorporate correction

### Story 2: User Annotates Paper
**As a** researcher reading a complex paper  
**I want to** highlight key passages and add notes  
**So that** I can review important points later  
**And** build a personal knowledge base

**Acceptance Criteria:**
- User can select text and click "Highlight"
- User can add notes to sections
- Annotations are saved to user profile
- Annotations appear in sidebar
- User can search and filter annotations

### Story 3: User Contributes Explanation
**As a** researcher who understands a concept well  
**I want to** write my own explanation  
**So that** I can help other researchers  
**And** enrich the knowledge base

**Acceptance Criteria:**
- User can click "Contribute Explanation" on concept page
- Editor supports markdown and examples
- Contribution enters review queue
- After approval, appears on concept page
- Other users can upvote contribution

---

## Appendix B: Database Schema Diagram

```
┌─────────────────┐
│     users       │
├─────────────────┤
│ user_id (PK)    │
│ username        │
│ email           │
│ created_at      │
└────────┬────────┘
         │
         ├─────────────────────────────────┐
         │                                 │
         ▼                                 ▼
┌─────────────────┐              ┌─────────────────┐
│   annotations   │              │   feedback_log  │
├─────────────────┤              ├─────────────────┤
│ annotation_id   │              │ feedback_id     │
│ user_id (FK)    │              │ user_id (FK)    │
│ paper_id        │              │ target_type     │
│ type            │              │ target_id       │
│ content         │              │ feedback_type   │
│ created_at      │              │ feedback_data   │
└─────────────────┘              └─────────────────┘

         │                                 │
         ▼                                 ▼
┌─────────────────┐              ┌─────────────────┐
│    papers       │              │  user_contribs  │
├─────────────────┤              ├─────────────────┤
│ paper_id (PK)   │              │ contrib_id (PK) │
│ title           │              │ user_id (FK)    │
│ authors         │              │ type            │
│ abstract        │              │ target_concept  │
│ ...             │              │ content         │
└─────────────────┘              └─────────────────┘
```

---

## Appendix C: API Endpoint Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/feedback` | POST | Submit feedback |
| `/api/feedback/history` | GET | Get feedback history |
| `/api/feedback/aggregated` | GET | Get aggregated feedback |
| `/api/annotations` | POST | Create annotation |
| `/api/annotations` | GET | Get annotations |
| `/api/annotations/{id}` | PUT | Update annotation |
| `/api/annotations/{id}` | DELETE | Delete annotation |
| `/api/contributions` | POST | Submit contribution |
| `/api/contributions` | GET | Get contributions |
| `/api/contributions/{id}/upvote` | POST | Upvote contribution |
| `/api/preferences/{user_id}` | GET | Get preferences |
| `/api/preferences/{user_id}` | PUT | Update preferences |
| `/api/recommendations` | GET | Get recommendations |
| `/api/recommendations/{id}/rate` | POST | Rate recommendation |

---

**Document Version:** 1.0  
**Last Updated:** 2026-09-01  
**Author:** AI Research Tracker Team  
**Status:** Design Phase
