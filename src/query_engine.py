from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from load_kb import load_kb
from config import CLAUDE_API_KEY
import anthropic

def get_response(user_question, k=3):
    kb = load_kb()
    embeddings = np.load("embeddings/kb_embeddings.npy")
    index = faiss.read_index("embeddings/index.faiss")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode([user_question])
    D, I = index.search(np.array(query_vector), k)
    retrieved_docs = [kb[i] for i in I[0]]
    context = "\n".join([f"Pregunta: {doc['question']}\nRespuesta: {doc['answer']}" for doc in retrieved_docs])
    prompt = f"""\nResponde a la siguiente pregunta del usuario usando los documentos de soporte que te doy como contexto.\n\nContexto:\n{context}\n\nPregunta del usuario: {user_question}\n"""
    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=500,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text