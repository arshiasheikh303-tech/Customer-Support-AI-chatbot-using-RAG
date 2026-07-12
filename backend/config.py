import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "AI Customer Support Chatbot"
    VERSION = "1.0.0"

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60


    DATABASE_URL = os.getenv("DATABASE_URL")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL = "llama3-8b-8192"

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    CHROMA_DB_PATH = "chroma_db"

    DOCUMENT_FOLDER = "documents"
    UPLOAD_FOLDER = "uploads"


    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150
    TOP_K_RESULTS = 4


    MAX_FILE_SIZE = 10 * 1024 * 1024   # 10 MB

    ALLOWED_EXTENSIONS = [
        ".pdf",
        ".docx",
        ".txt"
    ]


settings = Settings()