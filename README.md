# AI Image Semantic Search (Microservices Architecture)

An advanced image search system powered by Semantic Search. This project uses AI to understand the visual content of images and text, returning highly relevant results. It is built using a modern microservices architecture, separating the frontend UI from the backend AI logic.

**Live Demo:** [https://khfhgvtzsld2vjujtyqv7b.streamlit.app/](https://khfhgvtzsld2vjujtyqv7b.streamlit.app/)

## Core Features
* 🔤 **Text-to-Image Search:** Enter natural language queries (e.g., "forest", "cat") to find relevant images.
* 🖼️ **Image-to-Image Search:** Upload an image to find visually and semantically similar images in the database.

## Tech Stack & Architecture
This project is separated into two main components:

**1. Backend API (Render):**
* **Framework:** FastAPI.
* **AI Model:** OpenAI CLIP (`clip-ViT-B-32`) via `sentence-transformers` for feature extraction.
* **Vector Database:** Qdrant Cloud.

**2. Frontend UI (Streamlit Cloud):**
* **Framework:** Streamlit.
* Communicates with the Backend API via HTTP requests.

## Local Installation & Setup

1. Clone this repository:
   ```bash
   git clone [https://github.com/tiendinh-hcmut/AI-Image-Search.git](https://github.com/tiendinh-hcmut/AI-Image-Search.git)
   cd AI-Image-Search
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Backend API (Terminal 1):
   ```bash
   uvicorn api:app --reload
   ```

4. Run the Frontend UI (Terminal 2):
   ```bash
   python -m streamlit run app.py
   ```

*Note: Scripts for data ingestion and downloading images have been moved to the `tools/` directory.*

## Author
* **Đinh Tiến**