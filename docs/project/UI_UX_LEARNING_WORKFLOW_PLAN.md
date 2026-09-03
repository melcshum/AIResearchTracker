# UI/UX Learning Workflow Plan

## Vision
Transform the AI Research Tracker from a collection of tools into a **guided learning journey** that follows the constructivist learning cycle:

```
Write Wiki → Review → AI Enhance → Attain Knowledge → Keep Updated
     ↑                                                        ↓
     └────────────────────────────────────────────────────────┘
```

## Current Problems

### 1. Navigation Doesn't Reflect Learning Flow
- **Workspace** is the landing page, but it's a dashboard, not a learning starting point
- **AI Wiki** (the core learning tool) is buried in "Explore" menu
- Users don't know where to start their learning journey
- Pages are organized by function, not by learning stage

### 2. Missing Learning Path Guidance
- No clear "start here" for new users
- No progression indicators
- No connection between stages
- Users jump between tools without understanding the workflow

### 3. Wiki Not Positioned as Starting Point
- Wiki should be where learning **begins** (active construction)
- Currently treated as a reference tool (passive consumption)
- AI Companion features not prominently showcased

## Proposed Solution

### New Navigation Structure (Learning-Centric)

```
📚 Learn (START HERE)
  ├─ 📖 AI Wiki (Write & Build Understanding)
  ├─ 🎯 Learning Path (Your Journey)
  └─ 📊 Progress Dashboard

📖 Read & Review
  ├─ 🔬 Research Workspace
  ├─ 📄 Paper Reader
  ├─ 📚 Paper Library
  └─ 📖 Reading List

💡 Capture & Reflect
  ├─ ✨ Highlights
  ├─ 💡 Takeaways
  ├─ ❓ Questions
  └─ 📝 Notes

🤖 AI Enhancement
  ├─ 🎓 AI Study Guide
  ├─ 📝 AI Summaries
  ├─ 📊 Feedback Dashboard
  └─ 💬 AI Wiki Assistant

🧠 Retain & Master
  ├─ 🔄 Spaced Repetition
  ├─ 📅 Timeline
  ├─ 🎯 Recommendations
  └─ 📊 Compare Papers

🔄 Stay Updated
  ├─ 📰 Weekly Digest
  ├─ 🔔 New Papers Alert
  └─ 📈 Trending Topics

⚙️ Tools
  ├─ 🎯 Research Goals
  ├─ 💾 Export/Import
  ├─ 🕸️ Citation Graph
  ├─ 📁 Collections
  └─ 🔧 Admin
```

## Implementation Plan

### Phase 1: Restructure Navigation (Priority: HIGH)
**Goal:** Align navigation with learning workflow

**Changes:**
1. Update `_quarto.yml` with new menu structure
2. Rename "Workspace" to "Research Workspace" and move to "Read & Review"
3. Move "AI Wiki" to top-level "Learn" menu
4. Add "Learning Path" as guided journey
5. Reorganize all pages into learning stages

**Files:**
- `_quarto.yml` - Main navigation config
- `public/index.qmd` - Landing page (redirect to Learn)

### Phase 2: Create Learning Journey Page (Priority: HIGH)
**Goal:** Provide clear starting point and guidance

**New Page:** `public/learning-journey.md`
- Visual learning path with 5 stages
- Progress indicators for each stage
- "Start Here" call-to-action
- Quick links to relevant tools for each stage
- Onboarding tutorial for new users

### Phase 3: Enhance Wiki as Starting Point (Priority: MEDIUM)
**Goal:** Position Wiki as the primary learning tool

**Changes:**
1. Add "Start Learning" button to Wiki hero section
2. Show learning progress (terms explored, explanations written)
3. Highlight AI Companion features prominently
4. Add "Continue Learning" section showing last activity
5. Suggest next steps based on current term

**Files:**
- `public/wiki.md` - Enhanced hero and sidebar
- `public/ai-wiki.md` - Enhanced Learn by Building section

### Phase 4: Add Progress Tracking (Priority: MEDIUM)
**Goal:** Visualize learning journey and mastery

**New Features:**
1. Learning progress dashboard showing:
   - Terms explored (X/Y)
   - Explanations written
   - Mastery levels (🌱→🌿→🌳)
   - Time spent learning
2. Stage completion indicators
3. Streak tracking (daily learning)
4. Achievement badges

**Files:**
- `public/dashboard.md` - Enhanced with learning metrics
- `public/my-learning-path.md` - Visual journey map

### Phase 5: Improve Transitions Between Stages (Priority: LOW)
**Goal:** Guide users through the workflow naturally

**Changes:**
1. Add "Next Step" buttons at bottom of each page
2. Show related tools in context (e.g., "Now review with AI" after writing)
3. Add breadcrumbs showing current stage
4. Suggest next actions based on activity

**Example Flow:**
```
Wiki (Write) 
  → [Next: Review] → Paper Reader
  → [Next: Enhance] → AI Study Guide
  → [Next: Retain] → Spaced Repetition
  → [Next: Update] → Weekly Digest
```

## Detailed Page Mapping

### Stage 1: WRITE (Active Construction)
**Primary Tool:** AI Wiki
- Click terms to explore
- Write explanations in own words
- Use AI Companion (Write mode)
- Build personal understanding

**Supporting Tools:**
- Paper Reader (source material)
- Research Workspace (organized reading)

**Success Metrics:**
- Number of terms explored
- Explanations written
- Time spent writing

### Stage 2: REVIEW (Metacognition)
**Primary Tool:** Paper Reader + Highlights
- Re-read explanations
- Compare with expert definitions
- Identify gaps
- Refine understanding

**Supporting Tools:**
- Takeaways (key insights)
- Questions (unclear points)
- Notes (personal reflections)

**Success Metrics:**
- Explanations revised
- Gaps identified and filled
- Questions answered

### Stage 3: AI ENHANCE (Feedback Loop)
**Primary Tool:** AI Wiki Assistant + Study Guide
- Get AI feedback on explanations
- Receive suggestions for improvement
- Access related papers and examples
- Refine based on AI insights

**Supporting Tools:**
- Feedback Dashboard (track AI interactions)
- AI Summaries (condensed knowledge)

**Success Metrics:**
- AI feedback received
- Improvements made
- Accuracy score

### Stage 4: ATTAIN (Internalization)
**Primary Tool:** Spaced Repetition + Learning Path
- Practice recall through quizzes
- Review at optimal intervals
- Track mastery progression
- Build long-term retention

**Supporting Tools:**
- Timeline (visualize progress)
- Recommendations (what to learn next)
- Compare Papers (deepen understanding)

**Success Metrics:**
- Quiz scores
- Mastery levels achieved
- Retention rate

### Stage 5: UPDATE (Continuous Improvement)
**Primary Tool:** Weekly Digest + New Papers
- Monitor new research
- Update explanations with new insights
- Stay current with field
- Contribute to community knowledge

**Supporting Tools:**
- Trending Topics
- Citation Graph (see connections)
- Collections (organize by theme)

**Success Metrics:**
- Updates made
- New papers reviewed
- Contributions submitted

## UI/UX Design Principles

### 1. Progressive Disclosure
- Start simple (just Wiki)
- Reveal complexity as user progresses
- Don't overwhelm with all tools at once

### 2. Clear Affordances
- Big "Start Learning" buttons
- Visual indicators for next steps
- Obvious progress tracking

### 3. Contextual Guidance
- Show relevant tools for current stage
- Suggest next actions
- Provide tooltips and hints

### 4. Visual Hierarchy
- Primary action = largest/most prominent
- Secondary actions = smaller/subtle
- Tertiary actions = hidden until needed

### 5. Consistent Patterns
- Same layout across all pages
- Consistent color coding for stages
- Predictable navigation

## Color Coding by Stage

```
WRITE:     #3498db (Blue)   - Creation, construction
REVIEW:    #f39c12 (Orange) - Reflection, analysis
ENHANCE:   #9b59b6 (Purple) - AI, intelligence
ATTAIN:    #27ae60 (Green)  - Growth, mastery
UPDATE:    #e74c3c (Red)    - Alert, new information
```

## Success Metrics

### User Engagement
- Daily active users
- Time spent in each stage
- Completion rate of learning cycles

### Learning Outcomes
- Terms mastered (🌳 level)
- Explanations written
- Quiz scores improvement

### Retention
- Users returning after 7 days
- Streak length
- Contribution frequency

## Implementation Timeline

### Week 1: Navigation Restructure
- [x] Update `_quarto.yml`
- [x] Test all links work
- [x] Update landing page

### Week 2: Learning Journey Page
- [x] Create `learning-journey.md`
- [x] Add visual path diagram
- [x] Implement progress tracking

### Week 3: Wiki Enhancements
- [x] Add "Start Learning" hero
- [x] Enhance AI Companion visibility
- [x] Add progress indicators

### Week 4: Progress Dashboard
- [x] Enhance dashboard with learning metrics
- [x] Add mastery tracking
- [x] Implement streak counter

### Week 5: Stage Transitions
- [x] Add "Next Step" buttons
- [x] Implement breadcrumbs
- [x] Add contextual suggestions

## Technical Considerations

### Data Storage
- Use localStorage for progress tracking
- Sync to API for multi-device support
- Track: terms explored, explanations written, mastery levels, timestamps

### Performance
- Lazy load progress data
- Cache frequently accessed metrics
- Optimize for mobile devices

### Accessibility
- Keyboard navigation for all stages
- Screen reader friendly progress indicators
- High contrast color coding
- Clear focus states

## Next Steps

1. **Immediate:** Update `_quarto.yml` with new navigation
2. **This Week:** Create learning journey landing page
3. **Next Week:** Enhance Wiki as starting point
4. **Ongoing:** Add progress tracking and visualizations

---

**Status:** ✅ All phases completed (2026-09-02)
**Last Updated:** 2026-09-02
**Owner:** UI/UX Design Team
