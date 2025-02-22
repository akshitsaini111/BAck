from app.database import database
from app.config import COLLECTION_NAME
from app.models import LlamaResponse
from app.bedrock import get_llama_response
import uuid

from app.promptStore import get_system_prompt, get_user_prompt,get_system_level

from app.bedrock import get_llama_response

async def generate_response(prompt: str):
    response_text = await get_llama_response(prompt)
    return {"prompt": prompt, "response": response_text}

async def generate_response():
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt()
    combined_prompt = f"System: {system_prompt}\nUser: {user_prompt}"
    
    response_text = await get_llama_response(combined_prompt)
 
    return {"response": response_text}

async def getLevel(prompt: str):
    system_prompt = get_system_level()
    user_prompt="Give Me The Level Of The Question" + prompt
    combined_prompt = f"System: {system_prompt}\nUser: {user_prompt}"

    response_text = await get_llama_response(combined_prompt)
    
    return {"response": response_text}


async def get_stored_response(response_id: str):
    return await database[COLLECTION_NAME].find_one({"id": response_id}, {"_id": 0})
import json
import re

async def generate_question(topic: str, subtopic: str, level: str):
    system_prompt = get_system_level()
    user_prompt = f"""
    Generate exactly 5 unique and well-structured math questions on the subtopic '{subtopic}', which falls under the main topic '{topic}'.  
    The difficulty level of these questions should be '{level}'.  
    **Return the response as a valid JSON object with two fields:**
    - "questions" (a list of 5 question strings)
    - "answers" (a list of 5 corresponding answer strings)
    
    **Strictly follow this JSON format:**  
    {{
        "questions": [
            "Question 1?",
            "Question 2?",
            "Question 3?",
            "Question 4?",
            "Question 5?"
        ],
        "answers": [
            "Answer 1",
            "Answer 2",
            "Answer 3",
            "Answer 4",
            "Answer 5"
        ]
    }}
    
    **Only return the JSON object. Do not include any explanations, descriptions, or additional text.**
    """

    combined_prompt = f"System: {system_prompt}\nUser: {user_prompt}"
    response_text = await get_llama_response(combined_prompt)
    response_text = response_text.strip().strip("```json").strip("```")
    match = re.search(r"\{.*\}", response_text, re.DOTALL)
    if match:
        response_text = match.group(0)
    else:
        return {"error": "Failed to extract JSON from AI response.", "raw_response": response_text}

    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return {"error": "Invalid JSON response from AI.", "raw_response": response_text}

    return response_json

