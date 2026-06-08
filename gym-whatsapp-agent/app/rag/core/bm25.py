def bm25_search(docs, query):
    q = query.lower()
    return [d for d in docs if q in d.lower()][:5]
