import numpy as np
from rag import config
from rag.pdf_loader import load_all_pdfs
from rag.text_cleaner import clean_text
from rag.chunker import split_by_headings, paragraph_chunking
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator
from evaluation.rag_eval import evaluate_rag

# ✏️ ADD YOUR QUESTIONS BASED ON PDFs
QUESTIONS = [
    "What is the document about?",
    "What child care topic is primarily discussed?",
    "Who is the target age group for the child care practices mentioned?",
    "What are the key child care principles explained?",
    "What methods or routines are described for child care?",
    "What safety measures are recommended for children?",
    "What role do caregivers or parents play according to the document?",
    "What health or hygiene practices are mentioned?",
    "How does the document address emotional or mental development of children?",
    "What challenges in child care are discussed?",
    "What solutions or best practices are suggested?",
    "What examples or case studies are included?",
    "What benefits of proper child care are highlighted?",
    "What policies, guidelines, or standards are referenced?",
    "What conclusions or recommendations are provided?"
]


raw = load_all_pdfs(config.DATA_DIR)
cleaned = clean_text(raw)
sections = split_by_headings(cleaned, config.HEADINGS)
documents = paragraph_chunking(sections, config.MIN_CHUNK_LENGTH)

embedder = EmbeddingModel(config.EMBEDDING_MODEL)
embeddings = embedder.encode([d["text"] for d in documents])

store = VectorStore(embeddings.shape[1])
store.add(embeddings)

retriever = Retriever(embedder, store, documents)
generator = Generator(config.GEN_MODEL)

results = [evaluate_rag(q, retriever, generator, embedder) for q in QUESTIONS]

for r in results:
    print(r)

print("\nAVERAGES")
print("Retrieval:", np.mean([r["retrieval"] for r in results]))
print("Answer Quality:", np.mean([r["answer_quality"] for r in results]))
print("Grounding:", np.mean([r["grounding"] for r in results]))
