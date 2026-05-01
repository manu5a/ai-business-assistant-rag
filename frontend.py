import streamlit as st
import requests

API_URL = "https://ai-business-assistant-rag.onrender.com"

st.set_page_config(page_title="AI Business Assistant", page_icon="🤖")

st.title("🤖 AI Business Assistant")
st.write("Upload a PDF and ask questions about it using RAG.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    if st.button("Upload and Process PDF"):
        files = {
            "file": (uploaded_file.name, uploaded_file, "application/pdf")
        }

        with st.spinner("Uploading and indexing PDF..."):
            response = requests.post(f"{API_URL}/upload", files=files)

        if response.status_code == 200:
            st.success("PDF uploaded and indexed successfully.")
            st.json(response.json())
        else:
            st.error(response.text)

question = st.text_input("Ask a question about the PDF")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{API_URL}/ask",
                json={"question": question}
            )

        if response.status_code == 200:
            data = response.json()
            st.subheader("Answer")
            st.write(data["answer"])

            st.subheader("Sources")
            st.write(data["sources"])
        else:
            st.error(response.text)
    else:
        st.warning("Please enter a question.")