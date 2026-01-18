# Workflow RAG Backend

This project provides the backend for a **no-code workflow builder** that allows users to upload documents and ask questions using an AI-powered chat interface. It utilizes a **Retrieval-Augmented Generation (RAG)** architecture to ensure answers are grounded in the specific content of uploaded PDFs.

---

## 🚀 Key Features

* **PDF Processing:** Extracts and chunks text from uploaded documents for efficient retrieval.
* **Vector Embeddings:** Generates high-quality embeddings using **Gemini Embeddings** for semantic search.
* **Vector Storage:** Stores and manages document segments in **ChromaDB** for fast similarity searches.
* **Isolated Context:** Documents are isolated per **Workflow Stack**, ensuring queries only reference data relevant to that specific project.
* **Smart Retrieval:** Uses **Gemini LLM** to synthesize final answers based on retrieved context, combining accuracy with natural language generation.

---

## 🛠 Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL (Metadata) & ChromaDB (Vector Store)
* **AI Models:** Gemini Embeddings & Gemini LLM
* **PDF Parsing:** PyMuPDF

---

## 🔄 How It Works

1. **User Query:** The user submits a question via the API.
2. **Embedding:** The system converts the query into a vector representation using Gemini Embeddings.
3. **Search:** ChromaDB identifies the most relevant document chunks for that specific `stack_id`.
4. **Generation:** The retrieved context and original query are sent to Gemini LLM.
5. **Response:** The system returns a concise, data-backed answer grounded in the uploaded documents.

---

## ⚙️ Setup & Installation

### Prerequisites

* Python 3.8 or higher
* PostgreSQL database
* Gemini API key

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd workflow-rag-backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the project root or export the following variables:

```bash
export GEMINI_API_KEY=your_api_key
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/workflows
```

### 4. Initialize the Database

Make sure PostgreSQL is running and the database specified in `DATABASE_URL` exists.

```bash
# Create database if it doesn't exist
createdb workflows
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

* **API Base URL:** `http://localhost:8000`
* **Interactive Docs (Swagger UI):** `http://localhost:8000/docs`
* **Alternative Docs (ReDoc):** `http://localhost:8000/redoc`

---

## 🛣 API Endpoints

### Upload Document

**`POST /documents/upload?stack_id=<stack_id>`**

Uploads a PDF and indexes it for the specified stack.

**Parameters:**
* `stack_id` (query parameter): Unique identifier for the workflow stack

**Request:**
* Content-Type: `multipart/form-data`
* Body: PDF file

**Response:**
```json
{
  "message": "Document uploaded and indexed successfully",
  "stack_id": "demo",
  "chunks_indexed": 42
}
```

### Chat with a Stack

**`POST /chat`**

Ask questions based on the documents uploaded to a specific stack.

**Request Body:**
```json
{
  "stack_id": "demo",
  "query": "What are the main features of the product?"
}
```

**Response:**
```json
{
  "stack_id": "demo",
  "query": "What are the main features of the product?",
  "answer": "Based on the uploaded documents, the main features include...",
  "sources": [
    {
      "chunk_id": "chunk_1",
      "relevance_score": 0.92
    }
  ]
}
```

### Health Check

**`GET /health`**

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## 📁 Project Structure

```
workflow-rag-backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── routes/              # API route handlers
│   ├── services/            # Business logic (RAG, embeddings, etc.)
│   ├── models/              # Database models
│   ├── utils/               # Helper functions
│   └── config.py            # Configuration management
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not committed)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 🔒 Security Considerations

* Never commit your `.env` file or expose API keys in version control
* Consider implementing rate limiting for production deployments
* Use HTTPS in production environments
* Implement proper authentication and authorization for sensitive endpoints

---

## 🧪 Testing

```bash
# Run tests (if test suite is available)
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

---

## 📝 Notes

This backend is designed to be simple, modular, and easy to extend. Future enhancements could include:

* **Saved workflow logic:** Persist and reuse custom workflow configurations
* **Web search integration:** Augment responses with real-time web data
* **User authentication & JWT:** Secure endpoints with token-based authentication
* **Multi-format support:** Extend beyond PDFs to Word documents, text files, etc.
* **Advanced chunking strategies:** Implement semantic chunking or sliding windows
* **Caching layer:** Add Redis for frequently accessed queries
* **Monitoring & logging:** Integrate tools like Prometheus or ELK stack

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

---

**Built with ❤️ using FastAPI and Gemini AI**