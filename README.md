# TheBookGinni 📚🧞

TheBookGinni is a multilingual AI book assistant built with **FastAPI, FAISS, Sentence Transformers, and Google Gemini**. Users can upload a PDF book and ask questions in natural language. The system retrieves relevant passages from the uploaded book and generates answers grounded in that retrieved context, with source page references.

## Features

- PDF book upload
- Page-aware text extraction and chunking
- Multilingual semantic embeddings
- FAISS vector similarity search
- Gemini 2.5 Flash answer generation
- Grounded answers using uploaded-book context only
- Source page references
- Multilingual question/answer support
- Chat history in the frontend
- FastAPI health, upload, and question endpoints

## Architecture

```text
Frontend (HTML/CSS/JavaScript)
              |
              v
        FastAPI Backend
              |
        +-----+------+
        |            |
        v            v
   RAG Engine     Gemini API
        |
   PDF -> chunks
        |
 Sentence Transformers
        |
      FAISS
        |
 Relevant passages
        |
        +----------> Gemini
                     |
                     v
             Answer + sources
```

## Project Structure

```text
TheBookGinni/
├── backend/
│   ├── main.py
│   ├── rag_engine.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── index.html
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Cloud-Vaishvik/TheBookGinni.git
cd TheBookGinni
```

### 2. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure Gemini

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit the `.env` file or your API key.

### 4. Start FastAPI

From the `backend/` directory:

```bash
python -m uvicorn main:app --reload
```

The API will run at `http://127.0.0.1:8000`.

Interactive API documentation: `http://127.0.0.1:8000/docs`

### 5. Open the frontend

Open `frontend/index.html` in a browser while the FastAPI backend is running.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API status |
| GET | `/health` | Backend health check |
| POST | `/upload` | Upload and index a PDF |
| POST | `/ask` | Ask a question about the uploaded book |

Example `/ask` request:

```json
{
  "question": "What is psychology?",
  "top_k": 5
}
```

## Tech Stack

- **Python**
- **FastAPI**
- **FAISS**
- **Sentence Transformers**
- **pypdf**
- **Google Gemini 2.5 Flash**
- **HTML / CSS / JavaScript**

## Notes

The current backend keeps one active uploaded book in memory at a time. Uploaded PDFs are processed temporarily and are not stored by the backend after ingestion.

This project is a portfolio/learning implementation of a retrieval-augmented generation (RAG) workflow.
