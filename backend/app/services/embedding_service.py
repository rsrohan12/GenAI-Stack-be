import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def embed_text(text: str) -> list:
    result = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return result["embedding"]
