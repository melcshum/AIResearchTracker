# Website Restructuring Plan: Public vs Private Sections

## Overview
Restructure the AI Research Tracker into two distinct sections serving different audiences with separate themes and purposes.

---

## 🎯 Objectives

1. **Clear Separation**: Public content for researchers, private content for technical staff
2. **Distinct Themes**: Visual differentiation between sections
3. **Purpose-Driven Design**: Each section optimized for its audience
4. **Maintain Functionality**: All features preserved, better organized

---

## 📁 Proposed Structure

```
research-notes/
├── public/                    # Researchers & Users
│   ├── index.qmd             # Public landing page
│   ├── papers/               # Research papers
│   ├── topics/               # Topic pages (AI Agents, LLM, RAG, Multi-Modal)
│   ├── concepts/             # Glossary, connections, papers-by-concept
│   ├── digests/              # Weekly/monthly summaries
│   ├── wiki.md               # Knowledge wiki
│   ├── wiki-graph.md         # Knowledge graph visualization
│   ├── global-search.md      # Search interface
│   ├── reading-list.md       # Personal reading management
│   ├── notes.md              # Paper notes
│   ├── search-papers.md      # Paper search
│   ├── compare-papers.md     # Paper comparison
│   ├── tag-cloud.md          # Concept visualization
│   ├── statistics.md         # Research analytics
│   ├── authors.md            # Author profiles
│   ├── recommendations.md    # Paper recommendations
│   ├── learning-paths.md     # Structured learning
│   ├── must-read-papers.md   # Curated papers
│   ├── concept-explorer.qmd  # Interactive concept map
│   ├── research-workflow.md  # Research methodology guide
│   ├── external-hub.md       # Researcher hub (moved from root)
│   └── _quarto.yml           # Public section config
│
├── private/                   # Technical Staff & Admin
│   ├── index.md              # Private landing page
│   ├── system-architecture.md # System design docs
│   ├── SYSTEM_ARCHITECTURE.md # Architecture documentation
│   ├── system-health.md      # System monitoring
│   ├── admin.md              # Admin overview
│   ├── settings.md           # System settings
│   ├── requirements.md       # User requirements
│   ├── AGENTS.md             # Agent guide
│   ├── AUTOMATION.md         # Automation setup
│   ├── COMPLETE_AUTOMATION_GUIDE.md
│   ├── SHORTCUTS_SETUP.md
│   ├── DESIGN_GUIDE.md       # Design system
│   ├── UI_ENHANCEMENTS.md    # UI improvements
│   ├── UI_REFINEMENT_SUMMARY.md
│   ├── SESSION_SUMMARY.md
│   ├── OBSIDIAN_ENHANCEMENTS.md
│   ├── BACKLINKS_IMPLEMENTATION.md
│   ├── internal-hub.md       # Technical hub (moved from root)
│   ├── test-activity-feed.html # Test tools
│   └── _quarto.yml           # Private section config
│
├── _site/                     # Combined output
│   ├── public/               # Public section output
│   ├── private/              # Private section output
│   └── index.html            # Root router
│
├── _includes/                 # Shared includes
│   ├── mermaid.html
│   ├── custom-head.html
│   ├── custom-style.html
│   ├── theme-toggle.html
│   └── navbar-custom.html
│
├── _extensions/               # Theme extensions
│   ├── public-theme/
│   └── private-theme/
│
└── index.qmd                  # Root router page
```

---

## 🎨 Theme Design

### Public Theme (Researchers)
**Purpose**: Academic, clean, focused on content consumption
**Color Palette**:
- Primary: Deep blue (#1e3a8a) - Trust, knowledge
- Secondary: Teal (#0d9488) - Growth, discovery
- Accent: Amber (#f59e0b) - Highlights, actions
- Background: Light gray (#f8fafc) - Clean, readable

**Typography**:
- Headings: Serif (Georgia, Times) - Academic feel
- Body: Sans-serif (Inter, system) - Readability
- Code: Monospace (Fira Code) - Technical clarity

**Visual Style**:
- Card-based layouts
- Subtle shadows
- Rounded corners (8px)
- Minimal animations
- Focus on content hierarchy

### Private Theme (Technical Staff)
**Purpose**: Dashboard-style, data-dense, operational
**Color Palette**:
- Primary: Slate (#334155) - Professional, serious
- Secondary: Indigo (#6366f1) - Technical, modern
- Accent: Emerald (#10b981) - Success, metrics
- Background: Dark mode default (#0f172a) - Reduce eye strain

**Typography**:
- Headings: Sans-serif (Inter, system) - Clean, modern
- Body: Sans-serif (Inter, system) - Readability
- Code: Monospace (JetBrains Mono) - Technical precision

**Visual Style**:
- Grid-based layouts
- Data tables and metrics
- Sharp corners (4px)
- Status indicators
- Technical diagrams prominent

---

## 🔧 Implementation Plan

### Phase 1: Directory Structure
1. Create `public/` and `private/` directories
2. Move files to appropriate locations
3. Update file paths in all documents

### Phase 2: Theme Development
1. Create `public-theme/` extension
   - Custom SCSS with academic styling
   - Typography overrides
   - Component styles
2. Create `private-theme/` extension
   - Dashboard-style SCSS
   - Data visualization styles
   - Technical component styles

### Phase 3: Quarto Configuration
1. Create `public/_quarto.yml`
   - Academic theme
   - Research-focused navigation
   - Public sidebar structure
2. Create `private/_quarto.yml`
   - Technical theme
   - Admin-focused navigation
   - Private sidebar structure
3. Create root `_quarto.yml` for multi-project build

### Phase 4: Navigation & Routing
1. Create root `index.qmd` as router
   - "Continue to Research" → public/
   - "Continue to Admin" → private/
2. Update all internal links
3. Add cross-section navigation where appropriate

### Phase 5: Testing & Verification
1. Verify all pages render correctly
2. Test all internal links
3. Verify theme application
4. Check responsive design
5. Validate navigation flow

---

## 📋 File Migration Map

### Public Section (26 files)
- ✅ papers/ (all papers)
- ✅ topics/ (4 topic files)
- ✅ concepts/ (3 files)
- ✅ digests/ (2 files)
- ✅ wiki.md
- ✅ wiki-graph.md
- ✅ global-search.md
- ✅ reading-list.md
- ✅ notes.md
- ✅ search-papers.md
- ✅ compare-papers.md
- ✅ tag-cloud.md
- ✅ statistics.md
- ✅ authors.md
- ✅ recommendations.md
- ✅ learning-paths.md
- ✅ must-read-papers.md
- ✅ concept-explorer.qmd
- ✅ research-workflow.md
- ✅ external-hub.md
- ✅ rss.xml (generated)

### Private Section (17 files)
- ✅ system-architecture.md
- ✅ SYSTEM_ARCHITECTURE.md
- ✅ system-health.md
- ✅ admin.md
- ✅ settings.md
- ✅ requirements.md
- ✅ AGENTS.md
- ✅ AUTOMATION.md
- ✅ COMPLETE_AUTOMATION_GUIDE.md
- ✅ SHORTCUTS_SETUP.md
- ✅ DESIGN_GUIDE.md
- ✅ UI_ENHANCEMENTS.md
- ✅ UI_REFINEMENT_SUMMARY.md
- ✅ SESSION_SUMMARY.md
- ✅ OBSIDIAN_ENHANCEMENTS.md
- ✅ BACKLINKS_IMPLEMENTATION.md
- ✅ internal-hub.md
- ✅ test-activity-feed.html

### Root Files (3 files)
- ✅ index.qmd (router)
- ✅ dashboard.md (redirect to public/external-hub)
- ✅ _quarto.yml (multi-project config)

---

## 🎯 Success Criteria

1. **Clear Separation**: Users can easily identify which section they're in
2. **Theme Distinction**: Visual differences immediately apparent
3. **Purpose Alignment**: Each section serves its audience effectively
4. **Navigation Flow**: Easy to move between sections when needed
5. **No Broken Links**: All internal links work correctly
6. **Responsive Design**: Both themes work on mobile and desktop
7. **Performance**: No degradation in load times

---

## ⚠️ Risks & Mitigations

### Risk 1: Broken Links
**Mitigation**: Automated link checker script before deployment

### Risk 2: Theme Conflicts
**Mitigation**: Use Quarto's theme inheritance, test each theme independently

### Risk 3: Navigation Confusion
**Mitigation**: Clear visual indicators (breadcrumbs, section badges)

### Risk 4: Build Complexity
**Mitigation**: Use Quarto's multi-project feature, test build process

---

## 🚀 Next Steps

1. ✅ Review and approve this plan
2. Create directory structure
3. Migrate files
4. Develop themes
5. Configure Quarto
6. Update navigation
7. Test and verify
8. Deploy

---

## 📊 Timeline Estimate

- **Phase 1** (Structure): 30 minutes
- **Phase 2** (Themes): 1 hour
- **Phase 3** (Config): 30 minutes
- **Phase 4** (Navigation): 30 minutes
- **Phase 5** (Testing): 30 minutes
- **Total**: ~3.5 hours

---

**Status**: Plan ready for review  
**Ready to Proceed**: Yes (awaiting approval)
