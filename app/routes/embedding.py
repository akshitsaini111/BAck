from fastapi import APIRouter, HTTPException
from app.models import VectorEmbedding
from app.services.embeddings import store_embedding, get_embedding

router = APIRouter()

@router.post("/store")
async def store_vector(embedding: VectorEmbedding):
    result = await store_embedding(embedding)
    return {"message": "Stored successfully", "id": result}

@router.get("/get/{vector_id}")
async def get_vector(vector_id: str):
    embedding = await get_embedding(vector_id)
    if not embedding:
        raise HTTPException(status_code=404, detail="Vector not found")
    return embedding
