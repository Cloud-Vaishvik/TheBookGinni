import re
from pathlib import Path

import faiss
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extract text page-by-page while preserving PDF page numbers."""
    reader = PdfReader(str(pdf_path))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = re.sub(r"\s+", " ", text).strip()

        if text:
            pages.append({"page": page_number, "text": text})

    return pages, len(reader.pages)


def chunk_text(pages, chunk_size=500, overlap=100):
    """Split each page into overlapping chunks and preserve its page number."""
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    step = chunk_size - overlap

    for page_data in pages:
        page_number = page_data["page"]
        text = page_data["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end].strip()

            if chunk:
                chunks.append({"text": chunk, "page": page_number})

            start += step

    return chunks


def create_embeddings(chunks, model):
    """Create multilingual embeddings for all chunks."""
    if not chunks:
        raise ValueError(
            "No text could be extracted from the PDF. "
            "The PDF may contain scanned/image-only pages."
        )

    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(
        chunk_texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings.astype("float32")


def build_faiss_index(embeddings):
    """Build a normalized cosine-similarity FAISS index."""
    faiss.normalize_L2(embeddings)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    return index


def process_book(pdf_path, embedding_model):
    """Complete PDF ingestion pipeline: PDF -> pages -> chunks -> embeddings -> FAISS."""
    print("1. Extracting text...")
    pages, total_pages = extract_text_from_pdf(pdf_path)
    print(f"   PDF pages: {total_pages}")
    print(f"   Text pages: {len(pages)}")

    print("2. Creating chunks...")
    chunks = chunk_text(pages)
    print(f"   Chunks created: {len(chunks)}")

    print("3. Creating embeddings...")
    embeddings = create_embeddings(chunks, embedding_model)

    print("4. Building FAISS index...")
    index = build_faiss_index(embeddings)

    print("\nBook processed successfully.")

    return {
        "pages": pages,
        "total_pages": total_pages,
        "chunks": chunks,
        "embeddings": embeddings,
        "index": index
    }


def ingest_uploaded_book(pdf_path, embedding_model):
    """Optional helper for processing a book directly."""
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    book_data = process_book(pdf_path, embedding_model)

    print(f"\nBook: {pdf_path.name}")
    print(f"PDF pages: {book_data['total_pages']:,}")
    print(f"Text pages: {len(book_data['pages']):,}")
    print(f"Chunks created: {len(book_data['chunks']):,}")
    print(f"Vectors indexed: {book_data['index'].ntotal:,}")

    return book_data


def retrieve_relevant_chunks(query, book_data, embedding_model, top_k=5):
    """Retrieve the most relevant chunks using semantic similarity with FAISS."""
    if not query or not query.strip():
        return []

    if not book_data or "index" not in book_data:
        return []

    top_k = max(1, min(int(top_k), book_data["index"].ntotal))

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    faiss.normalize_L2(query_embedding)
    scores, indices = book_data["index"].search(query_embedding, top_k)

    results = []

    for score, index in zip(scores[0], indices[0]):
        if index == -1:
            continue

        chunk = book_data["chunks"][int(index)]
        results.append({
            "chunk": chunk["text"],
            "page": int(chunk["page"]),
            "score": float(score),
            "chunk_id": int(index)
        })

    return results


print("RAG engine loaded successfully.")
