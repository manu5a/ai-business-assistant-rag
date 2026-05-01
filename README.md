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

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* FAISS
* OpenAI API
* Docker
