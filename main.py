from rag import config
from rag.pdf_loader import load_all_pdfs
from rag.text_cleaner import clean_text
from rag.chunker import split_by_headings, paragraph_chunking
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator

def build_rag_pipeline():
    print("📄 Loading PDFs...")
    raw_text = load_all_pdfs(config.DATA_DIR)

    print("🧹 Cleaning text...")
    cleaned = clean_text(raw_text)

    print("✂️ Chunking...")
    sections = split_by_headings(cleaned, config.HEADINGS)
    documents = paragraph_chunking(sections, config.MIN_CHUNK_LENGTH)

    print("🧠 Building embeddings...")
    embedder = EmbeddingModel(config.EMBEDDING_MODEL)
    embeddings = embedder.encode([d["text"] for d in documents])

    print("🗄️ Creating vector store...")
    store = VectorStore(embeddings.shape[1])
    store.add(embeddings)

    retriever = Retriever(embedder, store, documents)
    generator = Generator(config.GEN_MODEL)

    return retriever, generator


def cli_chat():
    retriever, generator = build_rag_pipeline()

    print("\n✅ RAG system ready!")
    print("Type your question or type 'exit' to quit.\n")

    while True:
        question = input("❓ You: ")
        if question.lower() == "exit":
            print("👋 Exiting...")
            break

        docs = retriever.retrieve(question, config.TOP_K)
        answer = generator.generate(question, docs)

        print("\n🤖 Assistant:")
        print(answer)
        print("-" * 60)


if __name__ == "__main__":
    cli_chat()
