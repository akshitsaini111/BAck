from app.database import database
from app.config import COLLECTION_NAME
from app.models import VectorEmbedding

async def store_embedding(embedding: VectorEmbedding):
    result = await database[COLLECTION_NAME].insert_one(embedding.dict())
    return str(result.inserted_id)

async def get_embedding(vector_id: str):
    return await database[COLLECTION_NAME].find_one({"id": vector_id})
