import requests
from storage.db import SessionLocal, Article

API_KEY = "da48be64b21e48aa89eaaf86fa70e2f9"

def fetch_articles():
    print("Fetching articles...")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    data = response.json()
    print("Response JSON:", data)
    return data.get("articles", [])

def save_articles():
    session = SessionLocal()
    articles = fetch_articles()

    print("Number of articles received:", len(articles))

    for a in articles:
        article = Article(
            title=a.get("title", ""),
            content=a.get("description", "")
        )
        session.add(article)

    session.commit()
    session.close()
    print("Articles saved!")

if __name__ == "__main__":
    save_articles()
