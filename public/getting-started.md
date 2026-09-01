---
title: "Getting Started Guide"
---

# 🚀 Getting Started with AI Research Tracker

Welcome to your personalized AI-powered research learning platform! This guide will help you get started and make the most of all the AI features.

## 📋 Quick Setup

### 1. Start the Services

```bash
# Start the API server (for user data and AI features)
python3 api_server.py

# In another terminal, start the web server
python3 -m http.server 8001
```

### 2. Open Your Browser

Navigate to: `http://localhost:8001`

### 3. Create Your User Profile

Go to **Topics Management** in the navigation and create your user profile with your research interests.

---

## 🎯 Your Learning Journey

### Step 1: Configure Your Topics

**Navigate to:** Topics Management

1. Click "Create User" and enter your username
2. Add topics that interest you (e.g., "AI Agents", "LLM Reasoning", "RAG Systems")
3. Enable the topics you want to track
4. The system will automatically fetch relevant papers

**💡 Tip:** Start with 3-5 topics to avoid overwhelming yourself.

---

### Step 2: Explore Your Dashboard

**Navigate to:** Dashboard

Your dashboard shows:
- 📊 **Overview Stats**: Total papers, read count, notes count, active topics
- 📈 **Topic Progress**: Visual progress bars for each topic
- 🕐 **Recent Activity**: Latest bookmarks and notes
- 📅 **Reading Activity**: 7-day activity chart

**💡 Tip:** Check your dashboard daily to track your learning progress.

---

### Step 3: Discover Papers

**Navigate to:** Search Papers

1. Use the search bar to find papers by keyword
2. Filter by topic using the topic filter
3. Click the bookmark icon (⭐) to save papers
4. Click the note icon (📝) to add personal notes
5. Set reading status (To Read, Reading, Read)

**💡 Tip:** Bookmark papers first, then add notes as you read them.

---

## 🤖 AI-Powered Features

### Feature 1: AI Summaries

**Navigate to:** AI Summaries

**What it does:**
- Automatically generates one-liner summaries from paper abstracts
- Extracts key points and contributions
- Helps you quickly understand papers without reading the full abstract

**How to use:**
1. The system automatically generates summaries for your bookmarked papers
2. Click "Generate All" to create summaries for all papers
3. Use the search bar to find specific summaries
4. Click on a paper title to view the full paper

**💡 Tip:** Use summaries to quickly scan papers and decide which ones to read in depth.

---

### Feature 2: AI Study Guide

**Navigate to:** AI Study Guide

**What it does:**
- Creates personalized study materials from your saved papers
- Extracts key concepts and definitions
- Generates flashcards for active learning
- Identifies connections between concepts

**How to use:**
1. Click "Generate Study Guide"
2. Review the extracted concepts and definitions
3. Use the flashcards to test your knowledge
4. Explore concept connections to understand relationships

**💡 Tip:** Review the study guide weekly to reinforce your learning.

---

### Feature 3: AI Wiki Assistant

**Navigate to:** AI Wiki Assistant

**What it does:**
- Builds an intelligent knowledge base from your papers
- Provides AI-generated explanations of concepts
- Links related papers to each concept
- Creates a searchable wiki of your research area

**How to use:**
1. Click "Extract Concepts" to identify key concepts
2. Click "Generate Explanations" to create AI explanations
3. Click "Link Papers" to connect papers to concepts
4. Browse the wiki to explore your knowledge base

**💡 Tip:** The wiki grows smarter as you add more papers and notes.

---

### Feature 4: AI Recommendations

**Navigate to:** Recommendations

**What it does:**
- Analyzes your reading history and interests
- Suggests papers you might find valuable
- Ranks recommendations by relevance
- Explains why each paper was recommended

**How to use:**
1. View your personalized recommendations
2. Check the "Why recommended?" explanation
3. Click on papers to read more
4. Bookmark papers that interest you

**💡 Tip:** The more papers you read and bookmark, the better the recommendations become.

---

### Feature 5: Paper Comparison

**Navigate to:** Compare Papers

**What it does:**
- Compare multiple papers side-by-side
- Analyze topic coverage across papers
- Identify similarities and differences
- Extract key insights from each paper

**How to use:**
1. Select 2-5 papers to compare
2. Click "Compare Selected"
3. Review the comparison matrix
4. Analyze topic coverage and key insights

**💡 Tip:** Use comparison when researching a specific topic to understand different approaches.

---

### Feature 6: Weekly Digest

**Navigate to:** Weekly Digest

**What it does:**
- Automatically generates weekly summaries
- Highlights top papers and themes
- Tracks your reading progress
- Provides insights into your research trends

**How to use:**
1. View your latest weekly digest
2. Check the top papers of the week
3. Review theme analysis
4. Track your reading progress over time

**💡 Tip:** Review the digest every Sunday to plan your reading for the next week.

---

## 📚 Reading Workflow

### Recommended Workflow

1. **Discover**: Use Search Papers or Recommendations to find interesting papers
2. **Bookmark**: Save papers you want to read
3. **Summarize**: Read AI summaries to get an overview
4. **Read**: Read the full paper and take notes
5. **Study**: Use the Study Guide to reinforce learning
6. **Compare**: Compare related papers to deepen understanding
7. **Review**: Check your Weekly Digest to track progress

### Daily Routine

**Morning (10 min):**
- Check Dashboard for progress
- Review Weekly Digest
- Plan today's reading

**Reading Session (30-60 min):**
- Read 1-2 papers
- Add notes and bookmarks
- Update reading status

**Evening (5 min):**
- Review AI Summaries of new papers
- Check Recommendations
- Update study guide if needed

---

## 🎓 Learning Tips

### 1. Start Small
- Begin with 3-5 topics
- Read 1-2 papers per day
- Gradually expand your interests

### 2. Be Consistent
- Set aside time daily for reading
- Use the dashboard to track streaks
- Review your progress weekly

### 3. Take Notes
- Add notes to every paper you read
- Use the AI Study Guide to reinforce learning
- Connect concepts across papers

### 4. Use AI Features
- Let AI summaries help you scan papers quickly
- Use recommendations to discover new papers
- Compare papers to understand different approaches

### 5. Build Your Knowledge Base
- The AI Wiki grows with your reading
- Use it as a reference for your research
- Share it with collaborators

---

## 🔧 Troubleshooting

### API Server Not Running?

```bash
# Check if API server is running
lsof -i :5001

# Start API server
python3 api_server.py
```

### Papers Not Loading?

```bash
# Fetch new papers
python3 fetch_arxiv.py

# Generate topic pages
python3 generate_topic_pages.py
```

### AI Features Not Working?

1. Make sure API server is running
2. Check that you have bookmarked some papers
3. Try refreshing the page
4. Check browser console for errors

---

## 📞 Need Help?

- **Documentation**: Check the README.md file
- **Issues**: Report bugs on GitHub
- **Features**: Request new features via GitHub issues

---

## 🎉 You're Ready!

You now have everything you need to start your AI-powered research journey. Remember:

- ✅ Configure your topics
- ✅ Bookmark papers regularly
- ✅ Use AI features to save time
- ✅ Track your progress on the dashboard
- ✅ Build your knowledge base with the wiki

Happy researching! 🚀
