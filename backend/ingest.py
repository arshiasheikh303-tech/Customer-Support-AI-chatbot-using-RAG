from backend.rag import RAGSystem

rag = RAGSystem()
docs = rag.load_documents("backend/documents")  # folder with your PDFs
chunks = rag.split_documents(docs)
rag.create_vector_database(chunks)
print(f"Ingested {len(chunks)} chunks into chroma_db")