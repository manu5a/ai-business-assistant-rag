# AI Assistant Agent (RAG + FastAPI)

This project started as an attempt to understand how real-world AI systems answer questions from documents instead of relying only on pre-trained knowledge.

Most LLM demos are simple, but in real applications, you need a pipeline that can:

* ingest data,
* search it efficiently,
* and generate reliable answers.

So I built this system end-to-end using FastAPI, FAISS, and OpenAI APIs.

---

## 🚀 What it does

* Upload a PDF document
* Convert it into embeddings
* Store it in a vector database (FAISS)
* Retrieve relevant chunks based on a question
* Generate a context-aware answer using an LLM

---

## 🧠 Why I built this

While learning AI, I realized that:

* Models alone are not enough
* Real systems need retrieval + APIs + deployment
* Most job roles expect “AI + backend”, not just ML

This project helped me understand how RAG systems are actually built and deployed.

---

## ⚙️ Key Design Decisions

* Used **FAISS** for fast local vector search instead of cloud DB
* Used **FastAPI** to expose the AI system as a service
* Implemented **chunking + overlap** to improve retrieval quality
* Kept the system modular (loader → embeddings → retriever → LLM)

---

## 🏗️ Architecture

User → FastAPI → PDF Processing → Chunking → Embeddings → FAISS → Retriever → LLM → Response

## 🏗️ Architecture

```text
                ┌────────────────────┐
                │      User          │
                │ (API / Swagger UI) │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     FastAPI        │
                │   (Backend API)    │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                                   ▼
┌──────────────────┐              ┌────────────────────┐
│   PDF Upload     │              │   Question Input   │
│ (/upload route)  │              │   (/ask route)     │
└─────────┬────────┘              └─────────┬──────────┘
          ▼                                 ▼
┌──────────────────┐              ┌────────────────────┐
│ PDF Processing   │              │   Retriever        │
│ (Text Extract)   │              │ (FAISS Search)     │
└─────────┬────────┘              └─────────┬──────────┘
          ▼                                 ▼
┌──────────────────┐              ┌────────────────────┐
│ Text Chunking    │────────────▶│  Relevant Chunks    │
└─────────┬────────┘              └─────────┬──────────┘
          ▼                                 ▼
┌──────────────────┐              ┌────────────────────┐
│ OpenAI Embedding │              │      LLM           │
│ (Vector Creation)│              │ (Answer Generator) │
└─────────┬────────┘              └─────────┬──────────┘
          ▼                                 ▼
┌──────────────────┐              ┌────────────────────┐
│  FAISS Vector DB │────────────▶│   Final Answer     │
└──────────────────┘              │  + Sources        │
                                 └────────────────────┘
```
### Key Flow

1. User uploads PDF  
2. Text is extracted and split into chunks  
3. Chunks are converted into embeddings  
4. Stored in FAISS vector database  
5. User asks a question  
6. Relevant chunks are retrieved  
7. LLM generates final answer using context  
---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* FAISS
* OpenAI API
* Docker
