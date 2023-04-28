import json
import os
import requests
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NEWS_API_KEY = "d614b5d3009a45ac98c1fbbaa02fea36"

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String)

def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

def save_articles_to_sqlite(articles, db_url):
    engine = init_db(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for article in articles:
        new_article = Article(id=article["id"], title=article["title"])
        session.add(new_article)

    session.commit()
    session.close()

def fetch_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "world",
        "language": "en",
        "pageSize": 100,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
    else:
        print(f"Error fetching news: {data['message']}")
        articles = []

    return articles

def extract_title_and_id(articles, start_id=1):
    result = []
    for article in articles:
        title = article.get("title")
        if title:
            result.append({
                "id": start_id,
                "title": title
            })
            start_id += 1

    return result, start_id

def load_existing_articles(output_file="articles.json"):
    if os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                articles = json.load(f)
            next_id = max(article["id"] for article in articles) + 1
            return articles, next_id
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {output_file}. Creating a new file.")
            return [], 1
    return [], 1

def save_articles_to_json(articles, output_file="articles.json"):
    existing_articles, start_id = load_existing_articles(output_file)
    title_and_id_articles, _ = extract_title_and_id(articles, start_id)
    all_articles = existing_articles + title_and_id_articles

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_articles, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    articles = fetch_news()
    title_and_id_articles, _ = extract_title_and_id(articles)
    db_url = "sqlite:///news_articles.db" 
    save_articles_to_sqlite(title_and_id_articles, db_url)
