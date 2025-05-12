from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from load_kb import load_kb

def create_index():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    kb = load_kb()
    questions = [item["question"] for item in kb]
    embeddings = model.encode(questions)
    np.save("embeddings/kb_embeddings.npy", embeddings)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, "embeddings/index.faiss")

if __name__ == "__main__":
    create_index()