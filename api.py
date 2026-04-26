from fastapi import FastAPI, UploadFile, File
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from PIL import Image
import io

app = FastAPI()

model = SentenceTransformer('clip-ViT-B-32')
client = QdrantClient(
    url="https://6500f011-eb83-4726-a85d-3e1e59a6a17b.us-east-2-0.aws.cloud.qdrant.io", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6NjY1NzNmYWEtZmI2Mi00NTg0LTg4NmEtOTM4MzVmZWU5OWRmIn0.oxo_haBTtqEuOhT1JowaOmRHFFXH_OX4THRcg6nVjC8"
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