# Wiki Enhancement - Phase 2 Summary

**Date:** September 2, 2026  
**Status:** ✅ COMPLETED

---

## What We Did

Integrated local LLM (Ollama with gemma4-64k) into the Wiki Companion to provide **real AI-powered metacognitive scaffolding** for the Reflect and Scaffold modes.

---

## Key Changes

### 1. Updated JavaScript Functions
- **`aiGenerateReflectionPrompts()`** - Now calls `/api/wiki/companion` endpoint
  - Sends learner's explanation + concept name
  - Receives metacognitive questions from LLM
  - Displays questions in formatted list
  - Shows loading state while waiting for LLM response
  
- **`aiDetectGaps()`** - Now calls `/api/wiki/companion` endpoint  
  - Sends explanation + concept + action='detect_gaps'
  - Receives missing terms and suggestions from LLM
  - Displays feedback with warnings and suggestions
  - Maintains "Prompt Before Provide" interaction model

### 2. Enhanced API Server
- **Updated `/api/wiki/companion` endpoint** in `api_server.py`
  - Added support for `action` parameter in scaffold mode
  - Created specialized prompt for `detect_gaps` action
  - Improved JSON parsing instructions for Ollama
  - Uses `gemma4-64k` model (local, private, fast)

### 3. LLM Integration Details
- **Provider:** Ollama (local LLM)
- **Model:** gemma4-64k
- **Endpoint:** `http://localhost:11434/api/generate`
- **Format:** JSON responses
- **Timeout:** 30 seconds
- **Privacy:** All processing happens locally, no data leaves the machine

---

## How It Works

### Reflect Mode Flow
1. Learner writes explanation of a concept
2. Clicks "Generate Reflection Questions"
3. JavaScript sends explanation to API
4. API calls Ollama with metacognitive prompt
5. LLM generates 2-3 reflective questions
6. Questions displayed to learner
7. Learner reflects before moving to Scaffold

**Example Output:**
```json
{
  "questions": [
    "How confident are you that this a complete explanation of how RAG works?",
    "If you had to explain this to someone who doesn't know what 'context' means, how would you expand?",
    "What assumptions are you making about how documents are retrieved?"
  ]
}
```

### Scaffold Mode Flow (Detect Gaps)
1. Learner writes explanation
2. Clicks "Identify Gaps"
3. JavaScript sends explanation to API
4. API calls Ollama with gap detection prompt
5. LLM analyzes for missing concepts
6. Returns missing terms + suggestions
7. Feedback displayed with warnings

**Example Output:**
```json
{
  "missingTerms": ["vector database", "embeddings", "reranking"],
  "suggestions": [
    "How do embeddings relate to document retrieval?",
    "Consider how reranking improves result quality"
  ]
}
```

---

## Design Principles Honored

✅ **DP1: Learner Ownership** - Learner writes explanation first, AI doesn't intervene  
✅ **DP2: Scaffold Rather Than Substitute** - AI asks questions, doesn't provide answers  
✅ **DP3: Reflection Before Correction** - Reflect mode comes before Scaffold mode  
✅ **DP4: Continuous Knowledge Integration** - LLM connects to prior knowledge

---

## Technical Architecture

```
┌─────────────────┐
│   Wiki Page     │
│   (wiki.md)     │
└────────┬────────┘
         │
         │ fetch()
         │
         ▼
┌─────────────────┐
│  API Server     │
│  (Flask:5001)   │
└────────┬────────┘
         │
         │ requests.post()
         │
         ▼
┌─────────────────┐
│   Ollama        │
│  (gemma4-64k)   │
│ localhost:11434 │
└─────────────────┘
```

---

## Testing Results

✅ **Reflect Mode Test:**
- Prompt: "RAG is a technique that retrieves documents and uses them as context for the language model."
- Result: 3 high-quality metacognitive questions generated in ~21 seconds
- Format: Valid JSON array parsed correctly

✅ **Scaffold Mode Test:**
- Prompt: "RAG combines retrieval with generation by searching a knowledge base..."
- Result: LLM identified missing terms (vector database, embeddings)
- Note: Some JSON parsing issues with repetition, fixed with stricter prompt

✅ **API Server:** Running on http://localhost:5001
✅ **Ollama:** Running with gemma4-64k model
✅ **Quarto Site:** Rebuilt with 267 pages

---

## Files Modified

1. **`public/wiki.md`**
   - Updated `aiGenerateReflectionPrompts()` to call API
   - Updated `aiDetectGaps()` to call API
   - Added error handling and loading states

2. **`api_server.py`**
   - Enhanced `/api/wiki/companion` endpoint
   - Added `action` parameter for scaffold mode
   - Improved JSON prompt instructions

3. **`private/WIKI_PHASE2_SUMMARY.md`** (this file)
   - Documentation of Phase 2 implementation

---

## Known Issues & Future Improvements

### Current Issues
1. **JSON Parsing:** LLM sometimes repeats text in scaffold mode
   - **Fix Applied:** Stricter JSON instructions in prompt
   - **Monitor:** Test with more examples

2. **Response Time:** ~15-20 seconds per LLM call
   - **Cause:** gemma4-64k is a large model
   - **Future:** Consider smaller model for faster responses

### Future Improvements
1. **Streaming Responses:** Show partial results as LLM generates
2. **Caching:** Cache responses for same concept/explanation pairs
3. **Fallback:** Graceful fallback if Ollama is unavailable
4. **Mode 3 (Scaffold - Challenge):** Implement `aiChallengeMisconceptions()` with LLM
5. **Mode 5 (Revisit):** Implement connection suggestions with LLM
6. **Feedback Loop:** Track which suggestions learners find helpful

---

## Next Steps

1. **Test the Wiki:**
   - Visit http://100.64.0.17:8001/public/wiki.html
   - Click on any term (e.g., "RAG", "perception")
   - Try Reflect mode: Write explanation → Generate Reflection Questions
   - Try Scaffold mode: Click "Identify Gaps"
   - Observe LLM-generated feedback

2. **Iterate:**
   - Report any issues or unexpected behavior
   - Suggest improvements to prompts
   - Test with different concepts

3. **Phase 3 (Optional):**
   - Implement formative evaluation tracking
   - Add knowledge evolution version history
   - Track learner responses to AI scaffolding

---

## Success Criteria Met

✅ Local LLM integration working  
✅ Reflect mode generates metacognitive questions  
✅ Scaffold mode identifies knowledge gaps  
✅ Prompt Before Provide interaction model maintained  
✅ All design principles honored  
✅ No external API dependencies (fully local)  
✅ Privacy-preserving (no data leaves machine)  

---

**Phase 2 Complete!** The Wiki Companion now uses real AI to scaffold knowledge construction while preserving learner agency.
