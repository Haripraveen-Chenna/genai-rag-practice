import streamlit as st

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


from rag import config
from rag.pdf_loader import load_all_pdfs
from rag.text_cleaner import clean_text
from rag.chunker import split_by_headings, paragraph_chunking
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator

st.set_page_config("RAG Chat", layout="wide")
st.title("📄 PDF RAG Chat")

@st.cache_resource
def load_rag():
    raw = load_all_pdfs(config.DATA_DIR)
    cleaned = clean_text(raw)
    sections = split_by_headings(cleaned, config.HEADINGS)
    docs = paragraph_chunking(sections, config.MIN_CHUNK_LENGTH)

    embedder = EmbeddingModel(config.EMBEDDING_MODEL)
    embeddings = embedder.encode([d["text"] for d in docs])

    store = VectorStore(embeddings.shape[1])
    store.add(embeddings)

    return Retriever(embedder, store, docs), Generator(config.GEN_MODEL)

retriever, generator = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

q = st.chat_input("Ask about your PDFs...")

if q:
    st.session_state.messages.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)

    docs = retriever.retrieve(q, config.TOP_K)
    answer = generator.generate(q, docs)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
