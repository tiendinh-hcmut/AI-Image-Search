import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Image Search", layout="wide")
st.title("Trình Tìm Kiếm Ảnh AI")

def display_results(results):
    st.write("### Kết quả tìm kiếm:")
    cols = st.columns(3)
    for idx, res in enumerate(results):
        filename = res["filename"]
        score = res["score"]
        img_path = os.path.join("data", filename)
        
        with cols[idx]:
            if os.path.exists(img_path):
                st.image(img_path, caption=f"{filename} (Độ khớp: {score:.2f})", use_container_width=True)
            else:
                st.error(f"Không tìm thấy ảnh: {filename}")

tab1, tab2 = st.tabs(["🔤 Tìm bằng Chữ (Text-to-Image)", "🖼️ Tìm bằng Ảnh (Image-to-Image)"])

with tab1:
    query = st.text_input("Nhập từ khóa (Ví dụ: cat, forest, city...)", "")
    if query:
        st.write(f"Đang tìm kiếm cho từ khóa: **{query}**...")
        try:
            response = requests.get(f"https://ai-image-api-yh5q.onrender.com/search?keyword={query}")
            if response.status_code == 200:
                display_results(response.json()["results"])
            else:
                st.error("Lỗi khi xử lý từ khóa ở Backend!")
        except requests.exceptions.ConnectionError:
            st.error("🔴 Không thể kết nối đến Backend API. Hãy kiểm tra xem Uvicorn đã bật chưa!")

with tab2:
    uploaded_file = st.file_uploader("Tải một bức ảnh lên đây...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Ảnh bạn dùng để tìm kiếm", width=300)
        st.write("Đang trích xuất đặc trưng và tìm ảnh tương đồng...")
        
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        try:
            response = requests.post("https://ai-image-api-yh5q.onrender.com/search_by_image", files=files)
            if response.status_code == 200:
                display_results(response.json()["results"])
            else:
                st.error("Lỗi khi xử lý ảnh ở Backend!")
        except requests.exceptions.ConnectionError:
            st.error("🔴 Không thể kết nối đến Backend API. Hãy kiểm tra xem Uvicorn đã bật chưa!")
