from app.database import database
from app.config import COLLECTION_NAME
from app.models import VectorEmbedding
from app.bedrock import generate_embedding
import uuid

async def store_text_embedding(text: str):
    vector = await generate_embedding(text)
    embedding_id = str(uuid.uuid4())
    
    embedding = {
        "id": embedding_id,
        "vector": vector,
        "metadata": {"text": text}
    }
    
    await database[COLLECTION_NAME].insert_one(embedding)
    return embedding_id

async def get_embedding(vector_id: str):
    return await database[COLLECTION_NAME].find_one({"id": vector_id}, {"_id": 0})
