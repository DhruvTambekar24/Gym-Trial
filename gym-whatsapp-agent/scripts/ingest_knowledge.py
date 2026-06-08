from app.rag.ingestion.loader import load_corpus

if __name__ == "__main__":
    text = load_corpus("app/rag/knowledge_base/knowledge.txt")
    print("Loaded", len(text), "chars")
