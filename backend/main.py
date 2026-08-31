import os
import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer
from google import genai

from rag_engine import (
    process_book,
    retrieve_relevant_chunks
)

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

app = FastAPI(
    title="TheBookGinni RAG API",
    description="Backend API for TheBookGinni multilingual RAG system",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedding_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=GEMINI_API_KEY)

book_data = None
book_name = None


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5


@app.get("/")
def root():
    return {
        "name": "TheBookGinni RAG API",
        "status": "running",
        "version": "2.0.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/upload")
async def upload_book(file: UploadFile = File(...)):
    global book_data, book_name

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    temp_dir = tempfile.mkdtemp()
    pdf_path = os.path.join(temp_dir, file.filename)

    try:
        with open(pdf_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"Processing book: {file.filename}")

        book_data = process_book(pdf_path, embedding_model)
        book_name = file.filename

        return {
            "message": "Book processed successfully.",
            "book": book_name,
            "pages": book_data["total_pages"],
            "chunks": len(book_data["chunks"])
        }

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


@app.post("/ask")
def ask_question(request: QuestionRequest):
    global book_data

    if book_data is None:
        raise HTTPException(
            status_code=400,
            detail="Please upload a book first."
        )

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    results = retrieve_relevant_chunks(
        request.question,
        book_data,
        embedding_model,
        request.top_k
    )

    if not results:
        return {
            "answer": "The answer is not available in the uploaded book.",
            "sources": []
        }

    context_parts = []

    for i, result in enumerate(results, start=1):
        context_parts.append(
            f"[Source {i} | Page {result.get('page', 'Unknown')}]\n"
            f"{result['chunk']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are TheBookGinni, an AI assistant that answers
questions about uploaded books.

IMPORTANT RULES:

1. Answer ONLY using the provided book context.
2. Do not use outside knowledge.
3. Do not invent information.
4. If the answer cannot be found in the context, say:

"The answer is not available in the uploaded book."

5. Cite the relevant page numbers.
6. Use citations in this format:

[Source 1, Page 25]

BOOK CONTEXT:

{context}

USER QUESTION:

{request.question}

ANSWER:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        answer = response.text

    except Exception as e:
        print(f"Gemini error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to generate an answer."
        )

    sources = []

    for result in results:
        sources.append({
            "page": result.get("page"),
            "chunk_id": result.get("chunk_id"),
            "score": result.get("score")
        })

    return {
        "answer": answer,
        "sources": sources
    }
