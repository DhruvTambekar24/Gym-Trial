import numpy as np

class VectorStore:
    def __init__(self):
        self.embeddings = None
        self.docs = []

    def add(self, embeds, docs):
        if self.embeddings is None:
            self.embeddings = embeds.copy()
        else:
            self.embeddings = np.vstack([self.embeddings, embeds])
        self.docs.extend(docs)

    def similarity_search(self, query_vec, top_k=3):
        if self.embeddings is None or len(self.docs) == 0:
            return []
        sims = self.embeddings.dot(query_vec)
        idx = list(reversed(sims.argsort()))[:top_k]
        return [self.docs[i] for i in idx]
