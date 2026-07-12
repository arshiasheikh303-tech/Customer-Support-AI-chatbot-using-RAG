# Customer Support AI Chatbot (RAG)

An AI-powered customer support chatbot built with Retrieval-Augmented Generation (RAG). It answers customer questions by retrieving relevant information from your support documents (FAQs, refund policy, shipping info) and generating accurate, context-aware responses.

## Features

- 🔍 **Retrieval-Augmented Generation** — grounds answers in your actual support documents instead of hallucinating
- 📄 **Document ingestion** — automatically processes and chunks PDF/text support docs
- 🧠 **Vector search** — uses embeddings + ChromaDB to find the most relevant context for each question
- ⚡ **Fast LLM inference** — powered by Groq's LLaMA 3 model
- 🔐 **Authentication** — secure API access
- 💬 **Streamlit frontend** — simple, interactive chat interface

## Tech Stack

- **Backend:** Python, FastAPI (or similar)
- **LLM:** Groq (LLaMA 3 - 8B)
- **Embeddings:** sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store:** ChromaDB
- **Frontend:** Streamlit
- **Auth:** JWT-based authentication

## Project Structure

```
.
├── backend/
│   ├── app.py              # Main application entry point
│   ├── auth.py              # Authentication logic
│   ├── config.py             # App settings (loaded from environment variables)
│   ├── database.py           # Database connection/models
│   ├── ingest.py             # Document ingestion & chunking pipeline
│   ├── models.py             # Data models
│   ├── rag.py                 # Core RAG retrieval + generation logic
│   ├── routes.py             # API routes
│   └── documents/            # Source support documents (FAQ, policies, etc.)
├── frontend/
│   └── streamlit_app.py       # Streamlit chat UI
├── .env.example               # Example environment variables (copy to .env)
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

This will chunk and embed the documents into the local ChromaDB vector store.

### 6. Run the backend

```bash
python backend/app.py
```

### 7. Run the frontend

```bash
streamlit run frontend/streamlit_app.py
```

## How It Works

1. **Ingestion** — Support documents are split into chunks and converted into vector embeddings, stored in ChromaDB.
2. **Retrieval** — When a user asks a question, the system embeds the query and retrieves the most relevant document chunks.
3. **Generation** — The retrieved context + user question are passed to the LLM (LLaMA 3 via Groq), which generates a grounded, accurate response.

## Roadmap

- [ ] Add conversation history / multi-turn context
- [ ] Support more document formats
- [ ] Add feedback/rating system for responses
- [ ] Deploy to cloud hosting

## License

This project is open source. Add your preferred license here (e.g. MIT).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.
