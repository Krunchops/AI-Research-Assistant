import streamlit as st
import requests
st.set_page_config(
    page_title=(
        "AI Research Paper Assisstant"
    ),
    layout="centered"
)
st.title("AI Research Assisstant")
question=st.text_input(
    "Ask a question about the pdf"
)
if st.button("Ask"):
    response=requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "question":question
        }
    )
    answer=response.json()['answer']
    st.write(answer)
uploaded_file=st.file_uploader(
    "Upload_PDF",
    type=["pdf"]
)
if uploaded_file:
    if st.button(
        "Process PDF"
    ):
        files={
            'file':(
                uploaded_file.name,
                uploaded_file,
                'application/pdf'
            )
        }
        response=requests.post(
            "http://127.0.0.1:8000/upload_pdf",
            files=files
        )
        st.success(response.json()['message'])