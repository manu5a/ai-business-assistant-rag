import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import APP_NAME, UPLOAD_DIR
from app.pdf_loader import extract_text_from_pdf
from app.vector_store import create_documents, save_documents_to_faiss
from app.rag_pipeline import answer_question
from app.schemas import QuestionRequest, QuestionResponse

app = FastAPI(
    title=APP_NAME,
    description="A Retrieval-Augmented Generation API for asking questions about business PDF documents.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "AI Business Assistant RAG API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_text_from_pdf(file_path)
        documents = create_documents(text, source_name=file.filename)
        save_documents_to_faiss(documents)

        return {
            "message": "PDF uploaded and indexed successfully.",
            "filename": file.filename,
            "chunks_created": len(documents),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    try:
        result = answer_question(request.question)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))