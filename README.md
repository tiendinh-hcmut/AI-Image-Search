# AI Image Semantic Search

An intelligent image search system powered by Semantic Search. Unlike traditional systems that match filenames, this system uses Artificial Intelligence to "understand" the visual content of images and the context of text queries, delivering highly relevant results based on similarity.

**Live Demo:** [https://khfhgvtzsld2vjujtyqv7b.streamlit.app/](https://khfhgvtzsld2vjujtyqv7b.streamlit.app/)

## Tech Stack
* **AI Model (Feature Extraction):** OpenAI CLIP (`clip-ViT-B-32`) via `sentence-transformers`.
* **Vector Database:** Qdrant Cloud (Storing and querying high-dimensional vectors with Cosine Similarity).
* **Web Framework:** Streamlit.
* **Language:** Python.

## How it Works (Architecture)
1. **Data Ingestion:** The CLIP model scans the original image dataset, encoding each image into a 512-dimensional vector which is then stored in Qdrant Cloud.
2. **Inference:** When a user enters a query (e.g., "forest", "cat"), the same CLIP model encodes the text into a corresponding 512-dimensional vector.
3. **Vector Search:** Qdrant calculates the Cosine Similarity between the text vector and the image vectors in the database, returning the top 3 most relevant images.

## Installation & Local Setup

1. Clone this repository:
   ```bash
   git clone [https://github.com/tiendinh-hcmut/AI-Image-Search.git](https://github.com/tiendinh-hcmut/AI-Image-Search.git)
   cd AI-Image-Search
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Run the ingestion script if using a local database:
   ```bash
   python upload_vectors.py
   ```

4. Launch the Web UI:
   ```bash
   python -m streamlit run app.py
   ```

## Author
* **Đinh Tiến**