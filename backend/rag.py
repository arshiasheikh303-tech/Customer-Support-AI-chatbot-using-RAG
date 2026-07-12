import os

from langchain_community.document_loaders import PyPDFLoader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()


class RAGSystem:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant",
            temperature=0
        )

        self.vector_db = None

    def load_documents(self, pdf_folder):

        documents = []

        for file in os.listdir(pdf_folder):

            if file.endswith(".pdf"):

                loader = PyPDFLoader(
                    os.path.join(pdf_folder, file)
                )

                documents.extend(loader.load())

        return documents

    def split_documents(self, documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        return splitter.split_documents(documents)

    def create_vector_database(self, chunks):

        self.vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory="chroma_db"
        )

    def load_vector_database(self):

        self.vector_db = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embedding_model
        )

    def ask(self, question):

        qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 4}),
            return_source_documents=True
        )

        result = qa.invoke({"query": question})

        sources = []

        for doc in result["source_documents"]:
            sources.append(
                doc.metadata.get("source", "Unknown")
            )

        return {
            "question": question,
            "answer": result["result"],
            "sources": list(set(sources))
        }