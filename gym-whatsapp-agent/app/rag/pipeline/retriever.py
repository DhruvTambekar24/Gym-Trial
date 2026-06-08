from app.rag.core.embedder import embed_texts

def retrieve(texts_store, query, top_k=3):
    q_emb = embed_texts([query])[0]
    return texts_store.similarity_search(q_emb, top_k=top_k)
