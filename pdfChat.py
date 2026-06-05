import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# Extract text from PDFs
def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:

            text += page.extract_text()

    return text


# Split text into chunks
def get_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)

    return chunks


# Create vector store
def get_vector_store(text_chunks):

    vector_store = FAISS.from_texts(
        text_chunks,
        embedding=embedding_model
    )

    vector_store.save_local("faiss_index")


# Create conversational chain
def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context.

    If the answer is not available in the context,
    say: "Answer is not available in the context."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    model = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    chain = load_qa_chain(
        model,
        chain_type="stuff",
        prompt=prompt
    )

    return chain


# User question processing
def user_input(user_question):

    new_db = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {
            "input_documents": docs,
            "question": user_question
        },
        return_only_outputs=True
    )

    st.write("Reply:", response["output_text"])


# Main app
def main():

    st.set_page_config(page_title="Chat with Multiple PDFs")

    st.header("Chat with Multiple PDF using Groq 🤖")

    user_question = st.text_input(
        "Ask a question from PDF files"
    )

    if user_question:

        user_input(user_question)

    with st.sidebar:

        st.title("Menu")

        pdf_docs = st.file_uploader(
            "Upload PDF Files",
            accept_multiple_files=True
        )

        if st.button("Submit & Process"):

            with st.spinner("Processing..."):

                raw_text = get_pdf_text(pdf_docs)

                text_chunks = get_text_chunks(raw_text)

                get_vector_store(text_chunks)

                st.success("Done")


if __name__ == "__main__":
    main()