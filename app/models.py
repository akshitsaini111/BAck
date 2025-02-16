from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class VectorEmbedding(BaseModel):
    id: str
    vector: List[float]
    metadata: dict = {}
    
class PromptInput(BaseModel):
    prompt: str

class LlamaResponse(BaseModel):
    id: str
    prompt: str
    response: str

class RequestModel(BaseModel):
    prompt: str

class TopicRequestModel(BaseModel):
    topic: str
    subtopic: str
    level: str
