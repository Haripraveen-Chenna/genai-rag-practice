from fastapi import APIRouter, UploadFile, File
from app.core.ingestion import ingest_document
from app.core.retriever import answer_query

router = APIRouter()

@router.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    ingest_document(file)
    return {"message": "Document ingested successfully"}

@router.post("/query")
async def query(payload: dict):
    query_text = payload.get("query")
    return answer_query(query_text)
