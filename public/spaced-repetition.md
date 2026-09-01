---
title: "Spaced Repetition"
---

# 🔄 Spaced Repetition Review

Review your saved papers at optimal intervals to maximize retention and understanding.

<div class="spaced-repetition-container">
  <div class="review-header">
    <div class="review-stats">
      <div class="stat-card">
        <div class="stat-number" id="dueToday">0</div>
        <div class="stat-label">Due Today</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="upcomingWeek">0</div>
        <div class="stat-label">Due This Week</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="totalReviews">0</div>
        <div class="stat-label">Total Reviews</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="streak">0</div>
        <div class="stat-label">Day Streak 🔥</div>
      </div>
    </div>
    <button id="startReviewBtn" class="btn-primary">Start Review Session</button>
  </div>

  <div id="reviewSession" class="review-session" style="display: none;">
    <div class="session-header">
      <h2>Review Session</h2>
      <div class="session-progress">
        <span id="currentCard">1</span> / <span id="totalCards">0</span>
      </div>
      <button id="endSessionBtn" class="btn-secondary">End Session</button>
    </div>
    
    <div class="review-card" id="reviewCard">
      <div class="card-header">
        <div class="card-title" id="paperTitle">Paper Title</div>
        <div class="card-meta">
          <span id="paperAuthors">Authors</span> • 
          <span id="paperDate">Date</span>
        </div>
      </div>
      
      <div class="card-content">
        <div class="abstract-section">
          <h3>Abstract</h3>
          <p id="paperAbstract">Abstract text</p>
        </div>
        
        <div class="notes-section">
          <h3>Your Notes</h3>
          <div id="paperNotes">No notes yet</div>
        </div>
        
        <div class="summary-section">
          <h3>AI Summary</h3>
          <div id="paperSummary">No summary available</div>
        </div>
      </div>
      
      <div class="card-actions">
        <button class="review-btn difficult" onclick="ratePaper('difficult')">
          <span class="btn-label">Difficult</span>
          <span class="btn-interval">Review in 1 day</span>
        </button>
        <button class="review-btn moderate" onclick="ratePaper('moderate')">
          <span class="btn-label">Moderate</span>
          <span class="btn-interval">Review in 3 days</span>
        </button>
        <button class="review-btn easy" onclick="ratePaper('easy')">
          <span class="btn-label">Easy</span>
          <span class="btn-interval">Review in 7 days</span>
        </button>
        <button class="review-btn mastered" onclick="ratePaper('mastered')">
          <span class="btn-label">Mastered</span>
          <span class="btn-interval">Review in 14 days</span>
        </button>
      </div>
    </div>
  </div>

  <div id="upcomingReviews" class="upcoming-reviews">
    <h2>📅 Upcoming Reviews</h2>
    <div class="reviews-timeline" id="reviewsTimeline"></div>
  </div>

  <div id="reviewHistory" class="review-history">
    <h2>📊 Review History</h2>
    <div class="history-chart" id="historyChart"></div>
  </div>
</div>

<style>
.spaced-repetition-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.review-stats {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.stat-card {
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  text-align: center;
  min-width: 120px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2c5aa0;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.btn-primary, .btn-secondary {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: #2c5aa0;
  color: white;
}

.btn-primary:hover {
  background: #1e4a8f;
}

.btn-secondary {
  background: #e0e0e0;
  color: #333;
}

.btn-secondary:hover {
  background: #d0d0d0;
}

.review-session {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.session-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e0e0e0;
}

.session-header h2 {
  margin: 0;
  color: #2c3e50;
}

.session-progress {
  font-size: 1.2rem;
  color: #666;
}

.review-card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 2rem;
}

.card-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e0e0e0;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.card-meta {
  color: #666;
  font-size: 0.9rem;
}

.card-content {
  margin-bottom: 2rem;
}

.card-content h3 {
  color: #2c3e50;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.abstract-section, .notes-section, .summary-section {
  margin-bottom: 1.5rem;
}

.abstract-section p, .notes-section div, .summary-section div {
  color: #555;
  line-height: 1.6;
  background: white;
  padding: 1rem;
  border-radius: 6px;
}

.card-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.review-btn {
  padding: 1rem;
  border: 2px solid;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  background: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.review-btn.difficult {
  border-color: #e74c3c;
  color: #e74c3c;
}

.review-btn.difficult:hover {
  background: #e74c3c;
  color: white;
}

.review-btn.moderate {
  border-color: #f39c12;
  color: #f39c12;
}

.review-btn.moderate:hover {
  background: #f39c12;
  color: white;
}

.review-btn.easy {
  border-color: #27ae60;
  color: #27ae60;
}

.review-btn.easy:hover {
  background: #27ae60;
  color: white;
}

.review-btn.mastered {
  border-color: #2c5aa0;
  color: #2c5aa0;
}

.review-btn.mastered:hover {
  background: #2c5aa0;
  color: white;
}

.btn-label {
  font-weight: 600;
  font-size: 1rem;
}

.btn-interval {
  font-size: 0.85rem;
  opacity: 0.8;
}

.upcoming-reviews, .review-history {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.upcoming-reviews h2, .review-history h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.reviews-timeline {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.timeline-day {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  border-left: 4px solid #2c5aa0;
}

.timeline-day-header {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.timeline-papers {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.timeline-paper {
  background: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.9rem;
  color: #555;
}

.history-chart {
  height: 300px;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #999;
}

.empty-state-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}
</style>

<script>
// Dynamic API base URL
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:5001' 
  : window.location.origin.replace(/:\\d+$/, ':5001');
let allPapers = [];
let userData = null;
let reviewQueue = [];
let currentReviewIndex = 0;
let reviewHistory = [];

async function loadData() {
  try {
    const papersResponse = await fetch('papers.json');
    allPapers = await papersResponse.json();
    
    const userResponse = await fetch(API_BASE + '/api/user/data');
    userData = await userResponse.json();
    
    // Initialize spaced repetition data if not exists
    if (!userData.spacedRepetition) {
      userData.spacedRepetition = {
        reviews: {},
        history: [],
        streak: 0,
        lastReviewDate: null
      };
      await saveUserData();
    }
    
    updateStats();
    renderUpcomingReviews();
    renderReviewHistory();
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

function updateStats() {
  const today = new Date().toISOString().split('T')[0];
  const weekFromNow = new Date();
  weekFromNow.setDate(weekFromNow.getDate() + 7);
  
  const reviews = userData.spacedRepetition.reviews;
  const bookmarks = userData.bookmarks || [];
  
  let dueToday = 0;
  let dueThisWeek = 0;
  
  bookmarks.forEach(arxivId => {
    const review = reviews[arxivId];
    if (review && review.nextReview) {
      const nextReviewDate = new Date(review.nextReview);
      const todayDate = new Date(today);
      
      if (nextReviewDate <= todayDate) {
        dueToday++;
      }
      
      if (nextReviewDate <= weekFromNow) {
        dueThisWeek++;
      }
    } else if (!review) {
      // Papers without review schedule are due today
      dueToday++;
      dueThisWeek++;
    }
  });
  
  const totalReviews = userData.spacedRepetition.history.length;
  const streak = userData.spacedRepetition.streak || 0;
  
  document.getElementById('dueToday').textContent = dueToday;
  document.getElementById('upcomingWeek').textContent = dueThisWeek;
  document.getElementById('totalReviews').textContent = totalReviews;
  document.getElementById('streak').textContent = streak;
}

function getDuePapers() {
  const today = new Date().toISOString().split('T')[0];
  const reviews = userData.spacedRepetition.reviews;
  const bookmarks = userData.bookmarks || [];
  
  const duePapers = [];
  
  bookmarks.forEach(arxivId => {
    const paper = allPapers.find(p => p.arxiv_id === arxivId);
    if (!paper) return;
    
    const review = reviews[arxivId];
    if (!review || !review.nextReview) {
      duePapers.push(paper);
    } else {
      const nextReviewDate = new Date(review.nextReview);
      const todayDate = new Date(today);
      
      if (nextReviewDate <= todayDate) {
        duePapers.push(paper);
      }
    }
  });
  
  return duePapers;
}

function startReviewSession() {
  reviewQueue = getDuePapers();
  
  if (reviewQueue.length === 0) {
    alert('No papers due for review today! Great job staying on top of your reading.');
    return;
  }
  
  currentReviewIndex = 0;
  document.getElementById('reviewSession').style.display = 'block';
  document.getElementById('totalCards').textContent = reviewQueue.length;
  
  showCurrentCard();
}

function showCurrentCard() {
  if (currentReviewIndex >= reviewQueue.length) {
    endSession();
    return;
  }
  
  const paper = reviewQueue[currentReviewIndex];
  const notes = userData.notes?.[paper.arxiv_id] || 'No notes yet';
  const summary = userData.summaries?.[paper.arxiv_id] || 'No summary available';
  
  document.getElementById('currentCard').textContent = currentReviewIndex + 1;
  document.getElementById('paperTitle').textContent = paper.title;
  document.getElementById('paperAuthors').textContent = paper.authors;
  document.getElementById('paperDate').textContent = paper.date;
  document.getElementById('paperAbstract').textContent = paper.abstract || 'No abstract available';
  document.getElementById('paperNotes').textContent = notes;
  document.getElementById('paperSummary').textContent = summary;
}

async function ratePaper(difficulty) {
  const paper = reviewQueue[currentReviewIndex];
  const intervals = {
    'difficult': 1,
    'moderate': 3,
    'easy': 7,
    'mastered': 14
  };
  
  const daysToAdd = intervals[difficulty];
  const nextReview = new Date();
  nextReview.setDate(nextReview.getDate() + daysToAdd);
  
  // Update review data
  if (!userData.spacedRepetition.reviews[paper.arxiv_id]) {
    userData.spacedRepetition.reviews[paper.arxiv_id] = {
      firstReview: new Date().toISOString(),
      reviewCount: 0
    };
  }
  
  const review = userData.spacedRepetition.reviews[paper.arxiv_id];
  review.lastReview = new Date().toISOString();
  review.nextReview = nextReview.toISOString().split('T')[0];
  review.reviewCount++;
  review.lastDifficulty = difficulty;
  
  // Update history
  userData.spacedRepetition.history.push({
    arxiv_id: paper.arxiv_id,
    date: new Date().toISOString(),
    difficulty: difficulty
  });
  
  // Update streak
  const today = new Date().toISOString().split('T')[0];
  if (userData.spacedRepetition.lastReviewDate !== today) {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toISOString().split('T')[0];
    
    if (userData.spacedRepetition.lastReviewDate === yesterdayStr) {
      userData.spacedRepetition.streak++;
    } else if (userData.spacedRepetition.lastReviewDate !== today) {
      userData.spacedRepetition.streak = 1;
    }
    
    userData.spacedRepetition.lastReviewDate = today;
  }
  
  await saveUserData();
  
  // Move to next card
  currentReviewIndex++;
  showCurrentCard();
  updateStats();
}

async function saveUserData() {
  try {
    await fetch(API_BASE + '/api/user/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  } catch (error) {
    console.error('Error saving data:', error);
  }
}

function endSession() {
  document.getElementById('reviewSession').style.display = 'none';
  renderUpcomingReviews();
  renderReviewHistory();
  updateStats();
}

function renderUpcomingReviews() {
  const container = document.getElementById('reviewsTimeline');
  const reviews = userData.spacedRepetition.reviews;
  const bookmarks = userData.bookmarks || [];
  
  const upcomingByDay = {};
  
  bookmarks.forEach(arxivId => {
    const paper = allPapers.find(p => p.arxiv_id === arxivId);
    if (!paper) return;
    
    const review = reviews[arxivId];
    if (review && review.nextReview) {
      const date = review.nextReview;
      if (!upcomingByDay[date]) {
        upcomingByDay[date] = [];
      }
      upcomingByDay[date].push(paper);
    }
  });
  
  const sortedDates = Object.keys(upcomingByDay).sort().slice(0, 7);
  
  if (sortedDates.length === 0) {
    container.innerHTML = '<div class="empty-state">No upcoming reviews scheduled</div>';
    return;
  }
  
  container.innerHTML = sortedDates.map(date => {
    const dateObj = new Date(date);
    const dateStr = dateObj.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
    const papers = upcomingByDay[date];
    
    return `
      <div class="timeline-day">
        <div class="timeline-day-header">${dateStr} (${papers.length} paper${papers.length !== 1 ? 's' : ''})</div>
        <div class="timeline-papers">
          ${papers.map(p => `<div class="timeline-paper">${p.title.substring(0, 50)}...</div>`).join('')}
        </div>
      </div>
    `;
  }).join('');
}

function renderReviewHistory() {
  const container = document.getElementById('historyChart');
  const history = userData.spacedRepetition.history;
  
  if (history.length === 0) {
    container.innerHTML = '<div class="empty-state">No review history yet. Start reviewing to see your progress!</div>';
    return;
  }
  
  // Group by date
  const byDate = {};
  history.forEach(review => {
    const date = review.date.split('T')[0];
    if (!byDate[date]) {
      byDate[date] = 0;
    }
    byDate[date]++;
  });
  
  const dates = Object.keys(byDate).sort().slice(-14);
  const maxCount = Math.max(...dates.map(d => byDate[d]));
  
  container.innerHTML = `
    <div style="display: flex; align-items: end; justify-content: space-around; height: 100%; gap: 0.5rem;">
      ${dates.map(date => {
        const count = byDate[date];
        const height = (count / maxCount) * 100;
        const dateObj = new Date(date);
        const label = dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        
        return `
          <div style="display: flex; flex-direction: column; align-items: center; flex: 1;">
            <div style="background: #2c5aa0; width: 100%; height: ${height}%; border-radius: 4px 4px 0 0; min-height: 10px;"></div>
            <div style="margin-top: 0.5rem; font-size: 0.75rem; color: #666;">${label}</div>
            <div style="font-size: 0.85rem; font-weight: 600; color: #2c5aa0;">${count}</div>
          </div>
        `;
      }).join('')}
    </div>
  `;
}

document.getElementById('startReviewBtn').addEventListener('click', startReviewSession);
document.getElementById('endSessionBtn').addEventListener('click', endSession);

// Initialize
loadData();
</script>
