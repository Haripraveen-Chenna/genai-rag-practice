from app.core.chunking import chunk_text
from app.core.embeddings import store_embeddings

def ingest_document(file):
    text = file.file.read().decode("utf-8", errors="ignore")
    chunks = chunk_text(text)
    store_embeddings(chunks)
