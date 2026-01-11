from fastapi import APIRouter
from app.services.vector_store import query_documents
from app.services.llm_service import generate_answer
from app.schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    context = query_documents(req.stack_id, req.query)
    answer = generate_answer(req.query, context)
    return {"answer": answer}
