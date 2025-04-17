from PyPDF2 import PdfReader
from fastapi import UploadFile
from app.utils.create_chunk import CreateChunk

class DocumentService:
    def __init__(self):
        self.create_chunk = CreateChunk()
        
    def get_text(self, file: UploadFile) -> str:
        """Extract text from PDF file."""
        pdf_reader = PdfReader(file.file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
