from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from rag import RAGSystem

router = APIRouter()

rag_system = RAGSystem()

try:
    rag_system.load_vector_database()
except Exception as e:
    print(f"Warning: Could not load vector database on startup: {e}")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]


@router.get("/")
def home():
    return {"message": "AI Customer Support API is Running 🚀"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if rag_system.vector_db is None:
        raise HTTPException(
            status_code=503,
            detail="Vector database is not loaded. Please run ingest.py first."
        )

    try:
        result = rag_system.ask(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))