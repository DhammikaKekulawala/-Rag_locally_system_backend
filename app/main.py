from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.service.document_service import DocumentService  
from app.service.embedding_service import EmbeddingService

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize service
document_service = DocumentService()
embedding_service = EmbeddingService()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Endpoint to upload a PDF document
@app.post("/upload", summary="Upload PDF Document", description="Upload a PDF document for processing and embedding")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    try:
        # Use the service to get text
        chunks = await document_service.process_document(file)
        # Use the embedding service to get embeddings
        embedding_service.generate_embeddings(chunks)
        return {"message": "Document processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
