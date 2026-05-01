import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from app.config import FAISS_INDEX_DIR


def create_documents(text: str, source_name: str) -> list[Document]:
    """Split extracted PDF text into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(page_content=chunk, metadata={"source": source_name})
        for chunk in chunks
    ]

    return documents


def save_documents_to_faiss(documents: list[Document]) -> None:
    """Create or update FAISS index with document embeddings."""
    embeddings = OpenAIEmbeddings()

    if os.path.exists(FAISS_INDEX_DIR) and os.listdir(FAISS_INDEX_DIR):
        vector_store = FAISS.load_local(
            FAISS_INDEX_DIR,
            embeddings,
            allow_dangerous_deserialization=True,
        )
        vector_store.add_documents(documents)
    else:
        vector_store = FAISS.from_documents(documents, embeddings)

    vector_store.save_local(FAISS_INDEX_DIR)


def load_faiss_vector_store() -> FAISS:
    """Load FAISS index from local storage."""
    embeddings = OpenAIEmbeddings()

    if not os.path.exists(FAISS_INDEX_DIR) or not os.listdir(FAISS_INDEX_DIR):
        raise FileNotFoundError("No FAISS index found. Upload a PDF first.")

    return FAISS.load_local(
        FAISS_INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )