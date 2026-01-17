import faiss

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)

    def add(self, embeddings):
        self.index.add(embeddings)

    def search(self, query_embedding, k):
        _, idx = self.index.search(query_embedding, k)
        return idx
