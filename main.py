from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        # Save the file to a temporary location or process it directly
        with open(file.filename, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"filename": file.filename, "content_type": file.content_type}

