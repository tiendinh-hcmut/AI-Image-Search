import streamlit as st
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
import os

st.set_page_config(page_title="AI Image Search", layout="wide")
st.title("🔍 Trình Tìm Kiếm Ảnh Bằng AI")

@st.cache_resource
def load_system():
    model = SentenceTransformer('clip-ViT-B-32')
    client = QdrantClient(
    url="https://6500f011-eb83-4726-a85d-3e1e59a6a17b.us-east-2-0.aws.cloud.qdrant.io", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6NjY1NzNmYWEtZmI2Mi00NTg0LTg4NmEtOTM4MzVmZWU5OWRmIn0.oxo_haBTtqEuOhT1JowaOmRHFFXH_OX4THRcg6nVjC8"
)
    return model, client

model, client = load_system()

query = st.text_input("Bạn muốn tìm ảnh gì? (Thử gõ: cat, city, forest...)", "")

if query:
    st.write(f"Đang tìm kiếm cho: **{query}**...")
    
    query_vector = model.encode(query).tolist()
    
    results = client.query_points(
        collection_name="image_collection",
        query=query_vector,
        limit=3 
    ).points
    
    st.write("### Kết quả:")
    
    cols = st.columns(3)
    
    for idx, res in enumerate(results):
        filename = res.payload["filename"]
        score = res.score  
        
        img_path = os.path.join("data", filename)
        
        with cols[idx]:
            if os.path.exists(img_path):
                st.image(img_path, caption=f"{filename} (Độ khớp: {score:.2f})")
            else:
                st.error(f"Không tìm thấy file ảnh: {filename}")