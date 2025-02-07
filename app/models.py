from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class VectorEmbedding(BaseModel):
    id: str
    vector: List[float]
    metadata: dict = {}
