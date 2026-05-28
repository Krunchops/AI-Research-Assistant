from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
def create_vector_store(chunks):
    embedding_model=HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vector_store=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )
    return vector_store
def retrieve_relevant_chunks(vector_store , query:str):
    results=(vector_store.similarity_search(
        query,k=5
    ))
    print("Retreived results:\n")
    for result in results:
        print(result.page_content)
    return results
    