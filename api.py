from fastapi import FastAPI, UploadFile, File
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from PIL import Image
import io
import os

app = FastAPI()

model = SentenceTransformer('clip-ViT-B-32')
client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY")
)

@app.get("/search")
def search_text(keyword: str):
    query_vector = model.encode(keyword).tolist()
    results = client.query_points(
        collection_name="image_collection",
        query=query_vector,
        limit=3 
    ).points
    
    output = [{"filename": res.payload["filename"], "score": res.score} for res in results]
    return {"keyword": keyword, "results": output}

@app.post("/search_by_image")
async def search_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    query_vector = model.encode(image).tolist()
    
    results = client.query_points(
        collection_name="image_collection",
        query=query_vector,
        limit=3 
    ).points
    
    output = [{"filename": res.payload["filename"], "score": res.score} for res in results]
    return {"results": output}