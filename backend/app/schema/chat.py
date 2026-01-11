from pydantic import BaseModel

class ChatRequest(BaseModel):
    stack_id: str
    query: str
