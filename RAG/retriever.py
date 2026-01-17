class Retriever:
    def __init__(self, embedder, store, documents):
        self.embedder = embedder
        self.store = store
        self.documents = documents

    def retrieve(self, query, k=2):
        q_emb = self.embedder.encode([query])
        idx = self.store.search(q_emb, k)[0]
        return [self.documents[i] for i in idx]
