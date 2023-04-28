from fetch_news import fetch_news, save_articles_to_json
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from fetch_news import fetch_news, extract_title_and_id, save_articles_to_sqlite

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "fetch_news",
    default_args=default_args,
    description="Fetch news articles and store them in SQLite",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 4, 28),
    catchup=False,
)

def fetch_and_store_news(**kwargs):
    articles = fetch_news()
    title_and_id_articles, _ = extract_title_and_id(articles)
    db_url = "sqlite:///news_articles.db"  
    save_articles_to_sqlite(title_and_id_articles, db_url)

fetch_and_store_news_task = PythonOperator(
    task_id="fetch_and_store_news",
    python_callable=fetch_and_store_news,
    provide_context=True,
    dag=dag,
)
