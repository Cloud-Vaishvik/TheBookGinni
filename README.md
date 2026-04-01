# 🧞 TheBookGinni — Universal Book AI Assistant

> An AI-powered assistant that answers questions **strictly from your uploaded books** — supports **any book in any language**. No hallucination, no external knowledge.

---

## ✨ Features

- 📚 **Universal book support** — Upload and search across any PDF books simultaneously — fiction, non-fiction, textbooks, novels, and more
- 🌐 **Multi-language support** — Books written in Hindi, French, Spanish, Arabic, Chinese, Japanese, Russian, German, and 15+ other languages are fully supported
- 🗣️ **Reply language selector** — Ask in one language, get answers in another; or auto-detect and match the user's language
- 🔍 **Smart RAG pipeline** — Unicode-aware keyword scoring picks the most relevant chunks from every book, including non-Latin scripts
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
- ✅ 1 million token context window — handles large books in any language

### 2. Open the App
Just open `index.html` in any modern browser. No installation or server required.

### 3. Paste Your API Key
Enter your Gemini API key in the sidebar. A green dot confirms it's valid.

### 4. Upload Any Book
Click the upload area or drag and drop your PDF files. Works with books in any language!

### 5. Select Reply Language (Optional)
Use the language dropdown in the top bar to choose your preferred reply language, or leave it on **Auto-Detect** to match your question's language.

### 6. Ask Questions
Type any question and get answers grounded strictly in your uploaded texts.

---

## 🌐 Supported Languages

| Script | Languages |
|--------|-----------|
| Devanagari | Hindi, Marathi, Sanskrit |
| Arabic | Arabic, Urdu, Persian |
| Latin | English, French, Spanish, German, Italian, Portuguese, Dutch, Polish, Turkish |
| CJK | Chinese (Simplified & Traditional), Japanese |
| Korean | Korean (Hangul) |
| Cyrillic | Russian, Ukrainian, Bulgarian |
| Bengali | Bengali |
| Dravidian | Tamil, Telugu |

---

## 🛠️ How It Works (RAG Pipeline)

```
Your Question (any language)
     ↓
Unicode-aware Keywords Extracted
     ↓
All Books Split into 1,500-char Overlapping Chunks
     ↓
Every Chunk Scored for Relevance (supports CJK, Arabic, Devanagari, Latin)
     ↓
Top 8 Chunks from EACH Book Selected
     ↓
Context Assembled (up to 700,000 chars)
     ↓
Language of Books Auto-Detected & Displayed
     ↓
Gemini Answers from Your Books Only
     ↓
Reply in Your Chosen Language
```

### Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Chunk size | 1,500 chars | ~375 tokens per chunk |
| Chunks per book | 8 | Top scored chunks taken per book |
| Max context | 700,000 chars | ~175k tokens sent to Gemini |
| History window | 20 messages | Last 20 messages kept for conversation |
| Language detection | Heuristic (script analysis) | Auto-detects Hindi, Arabic, CJK, Latin, Cyrillic |

---

## 💬 Chat History

TheBookGinni saves every conversation locally, just like ChatGPT:

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
TheBookGinni/
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
| [Google Gemini API](https://ai.google.dev/) | AI responses with multilingual support |
| [PDF.js](https://mozilla.github.io/pdf.js/) | PDF text extraction (Unicode-aware) |
| Browser localStorage | Persistent storage |

---

## 📖 Example Questions

**English books:**
- *What are the main themes of this novel?*
- *Summarize the key arguments in chapter 3*

**Hindi books (हिन्दी किताबें):**
- *इस पुस्तक का मुख्य विषय क्या है?*
- *लेखक ने क्या निष्कर्ष निकाले?*

**French books:**
- *Quels sont les principaux thèmes de ce livre?*
- *Résumez le premier chapitre*

**Spanish books:**
- *¿Cuáles son los temas principales de este libro?*
- *¿Qué conclusiones saca el autor?*

---

## 🙏 Acknowledgements

- [Google AI Studio](https://aistudio.google.com/) for the free Gemini API
- [Mozilla PDF.js](https://mozilla.github.io/pdf.js/) for in-browser PDF parsing with Unicode support
- [Google Fonts](https://fonts.google.com/) — Cormorant Garamond & Outfit

---

*TheBookGinni v1.0 — Built with Google Gemini 2.5 Flash · Universal Multi-Language Book AI*
