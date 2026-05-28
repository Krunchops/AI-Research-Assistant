# AI Research Assistant

A simple full-stack RAG (Retrieval-Augmented Generation) application where users can upload PDFs and ask questions based on the document.

Built using:
- FastAPI
- Streamlit
- ChromaDB
- LangChain
- Groq
- Sentence Transformers

---

# Features

- Upload PDF documents
- Semantic search using embeddings
- Ask questions from uploaded PDFs
- FastAPI backend
- Streamlit frontend

---

# What I Learned

This project helped me understand:
- RAG pipelines
- Embeddings
- Chunking
- Vector databases
- Semantic retrieval
- FastAPI backend development
- Streamlit frontend development
- Full-stack AI app architecture

---

# Problems Faced While Building

Some real engineering problems I faced during development:

- Vector database contamination from old embeddings
- Incorrect file paths during PDF uploads
- Backend/frontend integration issues
- Retrieval returning irrelevant chunks
- Chunking issues affecting answer quality
- Debugging FastAPI server errors
- Handling persistent ChromaDB storage properly

Fixing these issues taught me more than the actual implementation.

---

# Run Backend

```bash
cd backend
uvicorn main:app --reload
```

---

# Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

# Future Improvements

- Source citations
- Chat memory
- Multi-PDF support
- Better retrieval and reranking
- Authentication
- Deployment
