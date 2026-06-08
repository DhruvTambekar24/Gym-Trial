def hybrid_search(vector_results, bm25_results):
    seen = set()
    out = []
    for r in vector_results + bm25_results:
        if r not in seen:
            out.append(r)
            seen.add(r)
    return out
