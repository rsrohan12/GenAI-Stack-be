# Workflow RAG Backend

This project provides the backend for a **no-code workflow builder** that allows users to upload documents and ask questions using an AI-powered chat interface. It utilizes a **Retrieval-Augmented Generation (RAG)** architecture to ensure answers are grounded in the specific content of uploaded PDFs.

---

## 🚀 Key Features

* **PDF Processing:** Extracts and chunks text from uploaded documents.
* **Vector Embeddings:** Generates high-quality embeddings using **Gemini Embeddings**.
* **Vector Storage:** Stores and manages document segments in **ChromaDB**.
* **Isolated Context:** Documents are isolated per **Workflow Stack**, ensuring queries only reference data relevant to that specific project.
* **Smart Retrieval:** Uses **Gemini LLM** to synthesize final answers based on retrieved context.

---

## 🛠 Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL (Metadata) & ChromaDB (Vector Store)
* **AI Models:** Gemini Embeddings & Gemini LLM
* **PDF Parsing:** PyMuPDF

---

## 🔄 How It Works

1. **User Query:** The user submits a question via the API.
2. **Embedding:** The system converts the query into a vector representation.
3. **Search:** ChromaDB identifies the most relevant document chunks for that specific `stack_id`.
4. **Generation:** The retrieved context and original query are sent to Gemini.
5. **Response:** The system returns a concise, data-backed answer.

---

## ⚙️ Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

```bash
export GEMINI_API_KEY=your_api_key
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/workflows
```

### 3. Run the Server

```bash
uvicorn app.main:app --reload
```

* **API Base URL:** `http://localhost:8000`
* **Interactive Docs (Swagger UI):** `http://localhost:8000/docs`

---

## 🛣 Main APIs

### Upload Document

**`POST /documents/upload?stack_id=<stack_id>`**

Uploads a PDF and indexes it for the specified stack.

### Chat with a Stack

**`POST /chat`**

Ask questions based on the documents uploaded to a specific stack.

**Request Body:**

```json
{
  "stack_id": "demo",
  "query": "Your question here"
}
```

---

## 📝 Notes

This backend is designed to be simple, modular, and easy to extend. Future enhancements could include:

* Saved workflow logic
* Web search integration
* User authentication & JWT
