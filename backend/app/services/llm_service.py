import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def generate_answer(query: str, context: list):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}
    """
    response = model.generate_content(prompt)
    return response.text
