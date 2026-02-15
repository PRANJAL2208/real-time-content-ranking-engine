from sentence_transformers import SentenceTransformer
from storage.db import SessionLocal, Article
from processing.vector_index import add_vector

model = SentenceTransformer("all-MiniLM-L6-v2")

def process_articles():
    session = SessionLocal()
    articles = session.query(Article).all()

    for article in articles:
        if article.content:
            embedding = model.encode(article.content)
            add_vector(embedding, article.id)
            print("Processed:", article.title)

    session.close()

if __name__ == "__main__":
    process_articles()
