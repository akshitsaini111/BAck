from fastapi import APIRouter, HTTPException
from app.models import PromptInput
from app.services.llama import generate_response, get_stored_response

router = APIRouter()

# @router.post("/generate")
# async def generate_llama_response(input_data: PromptInput):
#     return await generate_response(input_data.prompt)

@router.post("/generate")
async def generate_llama_response():
    return await generate_response()

@router.get("/get/{response_id}")
async def get_response(response_id: str):
    response_data = await get_stored_response(response_id)
    if not response_data:
        raise HTTPException(status_code=404, detail="Response not found")
    return response_data
