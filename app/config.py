import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Business Assistant RAG")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

UPLOAD_DIR = "data/uploads"
FAISS_INDEX_DIR = "data/faiss_index"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Please add it to your .env file.")