from fastapi import FastAPI
from app.api import router

app = FastAPI(title="GenAI RAG Practice")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}
