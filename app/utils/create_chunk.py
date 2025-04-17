class CreateChunk:
    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + chunk_size
            
            # Adjust chunk end to not cut words
            if end < text_length:
                # Find the last space before the chunk_size
                while end > start and text[end] != ' ':
                    end -= 1
            
            # Add chunk to list
            chunks.append(text[start:end].strip())
            
            # Move start position considering overlap
            start = end - overlap

        return chunks 