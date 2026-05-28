from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from pydantic import BaseModel
from pathlib import Path
from backend_textsplitter import (
    split_documents
)
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.parent / "data"
DATA_DIR.mkdir(
    exist_ok = True
)
from backend_pdf_loader import load_path



from backend_vector_Store import (

    create_vector_store,

    retrieve_relevant_chunks
)

from backend_rag_pipeline import (
    generate_answer
)

app = FastAPI()

# ---------------------------- #

# ---------------------------- #

class QueryRequest(
    BaseModel
):

    question: str

# ---------------------------- #

@app.post("/ask")

def ask_question(
    request: QueryRequest
):

    retrieved_docs = (
        retrieve_relevant_chunks(

            vector_store,

            request.question
        )
    )

    answer = generate_answer(

        request.question,

        retrieved_docs
    )

    return {

        "answer": answer
    }
@app.post("/upload_pdf")
async def upload_pdf(
    file:UploadFile=File(...)
):
    file_path=DATA_DIR / file.filename
    with open(
        file_path,"wb"
    ) as f:
        content=await file.read()
        f.write(content)
    docs=load_path(file_path)
    chunks=split_documents(docs)
    global vector_store
    vector_store=(create_vector_store(chunks))
    return {
        'message':'PDF uploaded successfully'
    }