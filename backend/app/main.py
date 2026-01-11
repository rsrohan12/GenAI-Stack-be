from fastapi import FastAPI
from app.api.routes import documents, chat
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workflow RAG Backend")

app.include_router(documents.router, prefix="/documents")
app.include_router(chat.router, prefix="/chat")
