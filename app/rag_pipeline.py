from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from app.vector_store import load_faiss_vector_store


def answer_question(question: str) -> dict:
    vector_store = load_faiss_vector_store()

    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
    )

    prompt = ChatPromptTemplate.from_template(
        """Answer the question based only on the context below.
        
Context:
{context}

Question:
{input}

Answer clearly and concisely."""
    )

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    result = retrieval_chain.invoke({"input": question})

    sources = []
    for doc in result.get("context", []):
        source = doc.metadata.get("source", "Unknown")
        if source not in sources:
            sources.append(source)

    return {
        "answer": result["answer"],
        "sources": sources,
    }