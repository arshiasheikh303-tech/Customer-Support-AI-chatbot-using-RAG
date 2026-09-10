<div align="center">

# Customer Support AI Chatbot (RAG)

**Retrieval-Augmented Generation** · Grounded Answers, Not Guesses

![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/GROQ%20%2F%20LLAMA%203-F55036?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LANGCHAIN-1C3C3C?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/CHROMADB-6E56CF?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

**Problem:** Generic chatbots guess when they don't know an answer, which is exactly the wrong behavior for customer support. **Approach:** retrieve the actual relevant passage from your FAQ, refund policy, or shipping docs first, then generate a response grounded in that retrieved context — so the bot answers from your real documents instead of hallucinating.

## Features

- 🔍 **Retrieval-Augmented Generation** — grounds answers in your actual support documents instead of hallucinating
- 📄 **Document ingestion** — automatically processes and chunks PDF/text support docs
- 🧠 **Vector search** — uses embeddings + ChromaDB to find the most relevant context for each question
- ⚡ **Fast LLM inference** — powered by Groq's LLaMA 3 model
- 🔐 **Authentication** — secure API access
- 💬 **Streamlit frontend** — simple, interactive chat interface

## Tech Stack

| Category | Tools |
|---|---|
| Backend | Python, FastAPI (or similar) |
| LLM | Groq (LLaMA 3 - 8B) |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector Store | ChromaDB |
| Frontend | Streamlit |
| Auth | JWT-based authentication |

## How It Works

1. **Ingestion** — support documents are split into chunks and converted into vector embeddings, stored in ChromaDB
2. **Retrieval** — when a user asks a question, the system embeds the query and retrieves the most relevant document chunks
3. **Generation** — the retrieved context + user question are passed to the LLM (LLaMA 3 via Groq), which generates a grounded, accurate response

## Project Structure

```
.
├── backend/
│   ├── app.py              # Main application entry point
│   ├── auth.py             # Authentication logic
│   ├── config.py           # App settings (loaded from environment variables)
│   ├── database.py         # Database connection/models
│   ├── ingest.py           # Document ingestion & chunking pipeline
│   ├── models.py           # Data models
│   ├── rag.py              # Core RAG retrieval + generation logic
│   ├── routes.py           # API routes
│   └── documents/          # Source support documents (FAQ, policies, etc.)
├── frontend/
│   └── streamlit_app.py    # Streamlit chat UI
├── .env.example             # Example environment variables (copy to .env)
├── .gitignore
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/arshiasheikh303-tech/Customer-Support-AI-chatbot-using-RAG.git
cd Customer-Support-AI-chatbot-using-RAG
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and fill in your own values:

```bash
copy .env.example .env      # Windows
cp .env.example .env        # macOS/Linux
```

Required variables:

```
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ Never commit your `.env` file. It's already excluded via `.gitignore`.

### 5. Ingest your documents

Place your support documents (PDF/text) in `backend/documents/`, then run:

```bash
python backend/ingest.py
```

This chunks and embeds the documents into the local ChromaDB vector store.

### 6. Run the backend

```bash
python backend/app.py
```

### 7. Run the frontend

```bash
streamlit run frontend/streamlit_app.py
```

## Roadmap

- [ ] Add conversation history / multi-turn context
- [ ] Support more document formats
- [ ] Add feedback/rating system for responses
- [ ] Deploy to cloud hosting

## License

This project is open source. Add your preferred license here (e.g. MIT).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

---

<div align="center">

Part of my [portfolio](https://arshia-portfolio-dx5dn9lw8-arshia-firdous303.vercel.app) · [More projects →](https://github.com/arshiasheikh303-tech)

</div>
