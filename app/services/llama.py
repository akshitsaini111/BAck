from app.database import database
from app.config import COLLECTION_NAME
from app.models import LlamaResponse
from app.bedrock import get_llama_response
import uuid

from app.promptStore import get_system_prompt, get_user_prompt

from app.bedrock import get_llama_response

# async def generate_response(prompt: str):
#     response_text = await get_llama_response(prompt)
#     return {"prompt": prompt, "response": response_text}

async def generate_response():
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt()
    combined_prompt = f"System: {system_prompt}\nUser: {user_prompt}"
    
    response_text = await get_llama_response(combined_prompt)
 
    return {"response": response_text}



async def get_stored_response(response_id: str):
    return await database[COLLECTION_NAME].find_one({"id": response_id}, {"_id": 0})
