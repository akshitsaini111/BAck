import boto3
import json
from app.config import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BEDROCK_MODEL_ID

# Initialize Bedrock client
bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Generate text embeddings using Amazon Bedrock
async def generate_embedding(text: str):
    payload = json.dumps({"inputText": text})
    response = bedrock_client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=payload
    )
    result = json.loads(response["body"].read())
    return result.get("embedding", [])

async def get_llama_response(prompt: str):
    payload = json.dumps({"prompt": prompt})
    response = bedrock_client.invoke_model(
        modelId=LLAMA_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=payload
    )
    result = json.loads(response["body"].read())
    return result.get("output", "No response")
