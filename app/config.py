import os
from dotenv import load_dotenv

load_dotenv()
#MONGO
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "vector_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "embeddings")
#AWS
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "amazon.titan-embed-text-v1")
LLAMA_MODEL_ID = os.getenv("LLAMA_MODEL_ID", "meta.llama3-8b-instruct-v1")
