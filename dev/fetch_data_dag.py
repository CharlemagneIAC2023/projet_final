from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
import sqlite3
import pandas as pd


def fetch_data():

    print("Fetching data...")
    api_key = "60ea556105752c18a776cf70bb6754b0"
    lat = "43.384132"
    lon = "5.372437"
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        records = []
        for entry in data["list"]:
            date = entry["dt_txt"]
            max_temp = entry["main"]["temp_max"]
            humidity = entry["main"]["humidity"]
            records.append((date, max_temp, humidity))

        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                date TEXT PRIMARY KEY,
                max_temp REAL,
                humidity REAL
            )
        """)

        cursor.executemany("""
        INSERT OR IGNORE INTO weather_data (date, max_temp, humidity) VALUES (?, ?, ?)
        """, records)

        conn.commit()

        print("Data in weather_data table:")
        cursor.execute("SELECT * FROM weather_data")
        print(cursor.fetchall())
        conn.close()

    else:
        raise Exception(f"Erreur lors de la récupération des données : {response.status_code}")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "fetch_data_dag",
    default_args=default_args,
    description="Récupérer les données météorologiques à chaque exécution",
    schedule=timedelta(days=1),  
    start_date=datetime(2023, 5, 1),
    catchup=False,
)

fetch_data_task = PythonOperator(
    task_id="fetch_data",
    python_callable=fetch_data,
    dag=dag,
)

fetch_data()