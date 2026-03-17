# 🧠 PsycheAI — Psychology Book Assistant

> An AI-powered psychology study tool that answers questions **strictly from your uploaded books** — no hallucination, no external knowledge.

---

## ✨ Features

- 📚 **Multi-book support** — Upload and search across all your psychology PDFs simultaneously
- 🔍 **Smart relevance search** — Keyword-based scoring picks the most relevant chunks from every book
- 💬 **Chat history** — All conversations are saved and accessible like ChatGPT, even after refresh
- 🔒 **Anti-hallucination** — Answers only from your uploaded texts; responds "No data found" if the topic isn't in your books
- 💾 **Persistent storage** — API key, books, chat history, and model preference are all saved locally
- ⚡ **Multi-model support** — Switch between Gemini 2.5 Flash, Pro, and Flash-Lite
- 🌐 **No backend needed** — Runs entirely in your browser as a single HTML file

---

## 🚀 Getting Started

### 1. Get a Free Gemini API Key
Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and create a free API key.

- ✅ No credit card required
- ✅ 500 requests/day free
- ✅ 1 million token context window — handles large books

### 2. Open the App
Just open `index.html` in any modern browser. No installation or server required.

### 3. Paste Your API Key
Enter your Gemini API key in the sidebar. A green dot confirms it's valid.

### 4. Upload Psychology Books
Click the upload area or drag and drop your PDF files. Multiple books can be uploaded at once.

### 5. Ask Questions
Type any psychology question and get answers grounded strictly in your uploaded texts.

---

## 🛠️ How It Works

```
Your Question
     ↓
Keywords Extracted
     ↓
All Books Split into 1,500-char Overlapping Chunks
     ↓
Every Chunk Scored for Relevance
     ↓
Top 8 Chunks from EACH Book Selected
     ↓
Context Assembled (up to 700,000 chars)
     ↓
Gemini Answers from Your Books Only
```

### Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Chunk size | 1,500 chars | ~375 tokens per chunk |
| Chunks per book | 8 | Top scored chunks taken per book |
| Max context | 700,000 chars | ~175k tokens sent to Gemini |
| History window | 20 messages | Last 20 messages kept for conversation |

---

## 💬 Chat History

PsycheAI saves every conversation locally, just like ChatGPT:

- Click any past chat in the **left panel** to reopen it
- Each session shows its title (first question asked), date, and message count
- Use **+ New Chat** to start a fresh conversation
- Hover over a session and click **×** to delete it

---

## 🤖 Supported Models

| Model | Best For |
|-------|----------|
| **Gemini 2.5 Flash** ⭐ | Everyday use — fast and smart (default) |
| **Gemini 2.5 Pro** | Complex, detailed questions |
| **Gemini 2.5 Flash-Lite** | Fastest responses |

---

## 📁 Project Structure

```
PsycheAI/
├── index.html        # The entire app — UI, logic, and styles in one file
├── README.md         # This file
└── _config.yml       # GitHub Pages configuration
```

---

## 🔐 Privacy

- Your API key and book contents are stored **only in your browser's localStorage**
- Nothing is sent to any server except the Gemini API (Google) when you ask a question
- No account, login, or data collection of any kind

---

## 🧩 Tech Stack

| Technology | Purpose |
|------------|---------|
| HTML / CSS / JavaScript | Frontend (single file) |
| [Google Gemini API](https://ai.google.dev/) | AI responses |
| [PDF.js](https://mozilla.github.io/pdf.js/) | PDF text extraction |
| Browser localStorage | Persistent storage |

---

## 📖 Example Questions

- *What is cognitive behavioral therapy?*
- *Explain the concept of classical conditioning*
- *What is the unconscious mind according to Freud?*
- *Describe Maslow's hierarchy of needs*
- *What are defense mechanisms in psychology?*

---

## 🙏 Acknowledgements

- [Google AI Studio](https://aistudio.google.com/) for the free Gemini API
- [Mozilla PDF.js](https://mozilla.github.io/pdf.js/) for in-browser PDF parsing
- [Google Fonts](https://fonts.google.com/) — Cormorant Garamond & Outfit

---

*PsycheAI v6.0 — Built with Google Gemini 2.5 Flash*
