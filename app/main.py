from fastapi import FastAPI
from app.routes.embeddings import router as embedding_router

app = FastAPI()

app.include_router(embedding_router, prefix="/vectors", tags=["Embeddings"])

@app.get("/")
def root():
    return {"message": "Amazon Bedrock Vector API"}
