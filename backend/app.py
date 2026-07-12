from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.database import engine, Base
from backend.rag import RAGSystem

app = FastAPI(
    title="AI Customer Support API",
    description="Backend API for AI Customer Support Chatbot",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change later to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# RAG System (loaded once at startup)
# -----------------------------
rag_system = RAGSystem()

@app.on_event("startup")
def load_rag():
    try:
        rag_system.load_vector_database()
    except Exception as e:
        # Vector DB hasn't been built yet — /chat will report this clearly
        print(f"Warning: could not load vector database: {e}")


# -----------------------------
# Request Model
# -----------------------------
class ChatRequest(BaseModel):
    question: str


# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "AI Customer Support API is Running 🚀"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Chat Route
# -----------------------------
@app.post("/chat")
def chat(request: ChatRequest):
    if rag_system.vector_db is None:
        return {
            "question": request.question,
            "answer": "The knowledge base hasn't been built yet. Run the document ingestion step first.",
            "sources": []
        }

    result = rag_system.ask(request.question)

    return {
        "question": result["question"],
        "answer": result["answer"],
        "sources": result["sources"]
    }