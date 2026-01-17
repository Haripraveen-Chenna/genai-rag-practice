import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        emb = self.model.encode(texts, show_progress_bar=True)
        return np.array(emb).astype("float32")
