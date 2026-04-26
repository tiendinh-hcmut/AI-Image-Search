import json
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(
    url="https://6500f011-eb83-4726-a85d-3e1e59a6a17b.us-east-2-0.aws.cloud.qdrant.io", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6NjY1NzNmYWEtZmI2Mi00NTg0LTg4NmEtOTM4MzVmZWU5OWRmIn0.oxo_haBTtqEuOhT1JowaOmRHFFXH_OX4THRcg6nVjC8"
)

with open("output/image_vectors.json", "r") as f:
    data = json.load(f)

collection_name = "image_collection"

client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=512, distance=Distance.COSINE),
)

points = []
for idx, item in enumerate(data):
    points.append(
        PointStruct(
            id=idx,
            vector=item["vector"],
            payload={"filename": item["filename"]} 
        )
    )

client.upsert(
    collection_name=collection_name,
    points=points
)

print(f"Đã nạp thành công {len(data)} vector vào Qdrant!")