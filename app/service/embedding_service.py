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

    def get_relevant_context(self, question: str, top_k: int = 3) -> str:
        if len(self.embeddings) == 0:
            raise Exception("No document has been processed yet")

        # Generate embedding for the question
        question_embedding = self.model.encode([question])[0]

        # Calculate similarities using numpy operations
        similarities = np.dot(self.embeddings, question_embedding)
        
        # Get indices of top k similar chunks
        top_k = min(top_k, len(similarities))  # Make sure we don't exceed array length
        top_indices = np.argsort(similarities)[-top_k:][::-1]  # Sort in descending order

        # Get relevant chunks and join them
        relevant_chunks = [self.chunks[i] for i in top_indices]
        return " ".join(relevant_chunks) 
