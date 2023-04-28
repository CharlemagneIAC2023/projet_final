import json
import os
import requests


NEWS_API_KEY = "d614b5d3009a45ac98c1fbbaa02fea36"

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
    save_articles_to_json(articles)
