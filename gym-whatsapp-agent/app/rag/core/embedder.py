import numpy as np

def embed_texts(texts):
    # Return deterministic pseudo-embeddings using hash
    embeds = []
    for t in texts:
        h = abs(hash(t)) % (10**8)
        vec = np.full((128,), (h % 100) / 100.0, dtype=float)
        embeds.append(vec)
    return np.vstack(embeds)
