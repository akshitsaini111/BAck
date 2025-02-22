from fastapi import FastAPI
from app.routes.embeddings import router as embedding_router
from app.routes.llama import router as llama_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(embedding_router, prefix="/vectors", tags=["Embeddings"])
app.include_router(llama_router, prefix="/llama", tags=["Llama 3"])

@app.get("/")
def root():
    return {"message": "Amazon Bedrock Vector API"}
