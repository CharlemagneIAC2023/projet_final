from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from fetch_news_api import fetch_news, save_articles_to_json

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
    description="Fetch news articles using News API",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 5, 1),
    catchup=False,
)

def fetch_and_save_news():
    articles = fetch_news()
    save_articles_to_json(articles)

fetch_news_task = PythonOperator(
    task_id="fetch_and_save_news",
    python_callable=fetch_and_save_news,
    dag=dag,
)
