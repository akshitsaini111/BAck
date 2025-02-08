from app.database import database
from app.config import COLLECTION_NAME
from app.models import LlamaResponse
from app.bedrock import get_llama_response
import uuid

from app.bedrock import get_llama_response

async def generate_response(prompt: str):
    response_text = await get_llama_response(prompt)
    return {"prompt": prompt, "response": response_text}


async def get_stored_response(response_id: str):
    return await database[COLLECTION_NAME].find_one({"id": response_id}, {"_id": 0})
