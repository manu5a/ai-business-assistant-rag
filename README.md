# AI Assistant Agent (RAG + LLM + FastAPI)

An AI-powered assistant that can understand documents, answer questions, and assist with business tasks using Retrieval-Augmented Generation (RAG) and Large Language Models.

---

## 🚀 Overview

This project demonstrates how modern AI assistant systems are built using LLMs combined with retrieval mechanisms. Instead of relying only on pre-trained knowledge, the system retrieves relevant information from user-provided data and generates accurate, context-aware responses.

The assistant can:

* Process and understand PDF documents
* Answer natural language questions
* Retrieve relevant context using vector search
* Generate intelligent responses using LLMs

---

## 🧠 Key Concepts

* Retrieval-Augmented Generation (RAG)
* Vector Databases (FAISS)
* Embeddings & Semantic Search
* LLM Integration (OpenAI API)
* AI Backend Engineering
* REST API Design

---

## ⚙️ Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using FAISS
* 💬 Ask questions in natural language
* 🤖 Context-aware AI responses
* ⚡ FastAPI backend with Swagger UI
* 🐳 Dockerized application
* 🌍 Deployment-ready (Render)

---

## 🏗️ Architecture

User → FastAPI API → Document Processing → Text Chunking → Embeddings → FAISS Vector Store → Retriever → LLM → Response

---

## 🧪 API Endpoints

| Method | Endpoint  | Description                |
| ------ | --------- | -------------------------- |
| GET    | `/`       | API status                 |
| GET    | `/health` | Health check               |
| POST   | `/upload` | Upload and index documents |
| POST   | `/ask`    | Ask questions              |

---

## 📌 Example Request

```json
{
  "question": "Summarise the document"
}
```

---

## 📌 Example Response

```json
{
  "answer": "The document discusses advancements in AI image generation...",
  "sources": ["Draft.pdf"]
}
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* FAISS
* OpenAI API
* Docker

---

## 🖥️ Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/ai-assistant-agent.git
cd ai-assistant-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```env
OPENAI_API_KEY=your_key_here
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker

```bash
docker build -t ai-assistant-agent .
docker run -p 8000:8000 --env-file .env ai-assistant-agent
```

---

## 🌍 Live Demo

👉 https://your-app-name.onrender.com/docs

---

## 💡 What This Project Shows

* Building production-style AI backend systems
* Designing RAG pipelines
* Integrating LLMs with APIs
* Handling document-based AI workflows
* Deploying AI services using Docker

---

## 🔮 Future Improvements

* User authentication (JWT)
* Chat history
* Multi-file support
* Frontend (React / Streamlit)
* Database integration (PostgreSQL)
* CI/CD pipeline

---

## 👨‍💻 Author

Manoj Kumar Arigachetta

🔗 LinkedIn: https://www.linkedin.com/in/manoj-kumar-arigachetta-ai/
🔗 GitHub: https://github.com/manu5a
