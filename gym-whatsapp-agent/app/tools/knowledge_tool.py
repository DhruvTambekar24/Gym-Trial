from app.rag.rag_service import RAGService

rag = RAGService(knowledge_path="app/rag/knowledge_base/knowledge.txt")

def knowledge_lookup(query: str):
    return rag.retrieve(query)
