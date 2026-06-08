from app.rag.ingestion.loader import load_corpus
from app.rag.ingestion.cleaner import clean_text
from app.rag.ingestion.chunker import chunk_text
from app.rag.core.embedder import embed_texts
from app.rag.core.vector_store import VectorStore

class RAGService:
    def __init__(self, knowledge_path=None):
        self.vs = VectorStore()
        if knowledge_path:
            text = load_corpus(knowledge_path)
            text = clean_text(text)
            chunks = chunk_text(text)
            embeds = embed_texts(chunks)
            self.vs.add(embeds, chunks)

    def retrieve(self, query, top_k=3):
        return self.vs.similarity_search(embed_texts([query])[0], top_k=top_k)
