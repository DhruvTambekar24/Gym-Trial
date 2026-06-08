from app.rag.rag_service import RAGService

def test_rag_load_and_query():
    r = RAGService(knowledge_path="app/rag/knowledge_base/knowledge.txt")
    res = r.retrieve("gym")
    assert isinstance(res, list)
