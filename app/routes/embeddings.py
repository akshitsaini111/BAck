from fastapi import APIRouter, HTTPException
from app.models import TextInput
from app.services.embeddings import store_text_embedding, get_embedding

router = APIRouter()

@router.post("/generate")
async def generate_vector(input_data: TextInput):
    embedding_id = await store_text_embedding(input_data.text)
    return {"message": "Embedding generated", "id": embedding_id}

@router.get("/get/{vector_id}")
async def get_vector(vector_id: str):
    embedding = await get_embedding(vector_id)
    if not embedding:
        raise HTTPException(status_code=404, detail="Vector not found")
    return embedding
