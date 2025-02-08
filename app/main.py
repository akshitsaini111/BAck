from fastapi import FastAPI
from app.routes.embeddings import router as embedding_router
from app.routes.llama import router as llama_router

app = FastAPI()

app.include_router(embedding_router, prefix="/vectors", tags=["Embeddings"])
app.include_router(llama_router, prefix="/llama", tags=["Llama 3"])

@app.get("/")
def root():
    return {"message": "Amazon Bedrock Vector API"}
