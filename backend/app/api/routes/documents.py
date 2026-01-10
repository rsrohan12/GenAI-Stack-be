from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.services.vector_store import add_documents

router = APIRouter()

@router.post("/upload")
async def upload_document(stack_id: str, file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    add_documents(stack_id, chunks)
    return {"message": "Document processed successfully"}
