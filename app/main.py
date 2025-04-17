from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.services.document_services import DocumentService



app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
document_service = DocumentService()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Endpoint to upload a PDF document
@app.post("/upload", 
         summary="Upload PDF Document",
         description="Upload a PDF document for processing and embedding")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    else:
        try:
            # Process the document
            text = await document_service.get_text(file)
            return JSONResponse(content={"message": "Document processed successfully", "text": text})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

