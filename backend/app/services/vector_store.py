import chromadb
from app.core.config import CHROMA_PERSIST_DIR
from app.services.embedding_service import embed_text

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=CHROMA_PERSIST_DIR
    )
)

def get_collection(stack_id: str):
    return client.get_or_create_collection(name=f"stack_{stack_id}")

def add_documents(stack_id: str, texts: list):
    collection = get_collection(stack_id)
    for i, text in enumerate(texts):
        collection.add(
            ids=[f"{stack_id}_{i}"],
            documents=[text],
            embeddings=[embed_text(text)]
        )

def query_documents(stack_id: str, query: str, k: int = 3):
    collection = get_collection(stack_id)
    result = collection.query(
        query_embeddings=[embed_text(query)],
        n_results=k
    )
    return result["documents"][0]
