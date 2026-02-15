import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

article_ids = []

def add_vector(vector, article_id):
    index.add(np.array([vector]).astype("float32"))
    article_ids.append(article_id)

def search(query_vector, k=5):
    D, I = index.search(np.array([query_vector]).astype("float32"), k)
    return [article_ids[i] for i in I[0]]
