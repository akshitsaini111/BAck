from fastapi import APIRouter, HTTPException
from app.models import PromptInput, RequestModel, TopicRequestModel
from app.services.llama import generate_question, generate_response, get_stored_response, getLevel

router = APIRouter()

# @router.post("/generate")
# async def generate_llama_response(input_data: PromptInput):
#     return await generate_response(input_data.prompt)

@router.post("/generate")
async def generate_llama_response():
    return await generate_response()

@router.post("/getLevel")
async def generate_llama_response(request: RequestModel):
    return await getLevel(request.prompt)

@router.get("/get/{response_id}")
async def get_response(response_id: str):
    response_data = await get_stored_response(response_id)
    if not response_data:
        raise HTTPException(status_code=404, detail="Response not found")
    return response_data

@router.get("/generateQuestions")
async def generateQuestion(request:TopicRequestModel):
     return await generate_question(request.topic, request.subtopic, request.level)
