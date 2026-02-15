from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from storage.db import SessionLocal, Article
import faiss
import numpy as np

app = FastAPI()

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384
index = faiss.IndexFlatL2(dimension)
article_ids = []

def build_index():
    print("Building vector index...")
    session = SessionLocal()
    articles = session.query(Article).all()

    for article in articles:
        if article.content:
            embedding = model.encode(article.content)
            index.add(np.array([embedding]).astype("float32"))
            article_ids.append(article.id)

    session.close()
    print("Index built with", len(article_ids), "articles")

@app.on_event("startup")
def startup_event():
    build_index()

@app.get("/search")
def search_articles(query: str):
    query_vector = model.encode(query)
    D, I = index.search(np.array([query_vector]).astype("float32"), 5)

    ids = [article_ids[i] for i in I[0] if i < len(article_ids)]

    session = SessionLocal()
    articles = session.query(Article).filter(Article.id.in_(ids)).all()
    session.close()

    return [{"title": a.title, "content": a.content} for a in articles]
