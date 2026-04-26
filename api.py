from fastapi import FastAPI, UploadFile, File
from qdrant_client import QdrantClient
from PIL import Image
import io
import os

app = FastAPI()

model = None
client = None

def get_model():
    global model
    if model is None:
        print("Đang import PyTorch và tải model CLIP...")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('clip-ViT-B-32')
    return model

def get_client():
    global client
    if client is None:
        print("Đang kết nối Qdrant...")
        client = QdrantClient(
            url=os.getenv("QDRANT_URL"), 
            api_key=os.getenv("QDRANT_API_KEY")
        )
    return client

# --- API ---

@app.get("/search")
def search_text(keyword: str):
    ai_model = get_model()
    db_client = get_client()
    
    query_vector = ai_model.encode(keyword).tolist()
    results = db_client.query_points(
        collection_name="image_collection",
        query=query_vector,
        limit=3 
    ).points
    
    output = [{"filename": res.payload["filename"], "score": res.score} for res in results]
    return {"keyword": keyword, "results": output}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is fine"}

@app.post("/search_by_image")
async def search_image(file: UploadFile = File(...)):
    ai_model = get_model()
    db_client = get_client()

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    query_vector = ai_model.encode(image).tolist()
    results = db_client.query_points(
        collection_name="image_collection",
        query=query_vector,
        limit=3 
    ).points
    
    output = [{"filename": res.payload["filename"], "score": res.score} for res in results]
    return {"results": output}