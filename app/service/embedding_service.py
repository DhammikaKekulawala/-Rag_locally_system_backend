from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = []
        self.chunks = []

    def generate_embeddings(self, text_chunks: list[str]):
        self.chunks = text_chunks
        self.embeddings = self.model.encode(text_chunks)
