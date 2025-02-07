from pydantic import BaseModel
from typing import List

class VectorEmbedding(BaseModel):
    id: str
    vector: List[float]
    metadata: dict = {}
