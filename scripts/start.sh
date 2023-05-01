#!/bin/bash


echo ""
echo ""
echo "  PROJET IA CLOUD: start.sh"
echo ""
echo ""

echo ""
echo "-> installation de toutes les dépendances dépendances"
echo ""

pip install apache-airflow
echo ""
pip install sqlite3
echo ""
pip install sqlalchemy
pip install tensorflow numpy sklearn mlflow
echo ""
pip install scikit-learn
echo ""
pip install requests
echo ""
pip install mlflow
echo ""
pip install fastapi uvicorn
echo ""

echo ""
echo "-> airflow db init"
echo ""

cd ../../../ && rm -fv airflow.db && airflow db init

echo ""
echo "-> création utilisateur airflow"
echo ""
airflow users create --username carolus --email clement.charlemagne@ynov.com --firstname Clement --lastname Charlemagne --password carolus --role Admin


echo ""
echo "-> lancement serveur airflow en tache de fond"
echo ""

gnome-terminal -- bash -c "airflow webserver; exec bash"
sleep 10

echo ""
echo "-> lancement scheduler airflow en tache de fond"
echo ""

gnome-terminal -- bash -c "airflow scheduler; exec bash"
sleep 10

echo ""
echo "-> déplacement des fichiers fetch_data_dag.py et train_model.py vers dossier dags de airflow"
echo ""

cd dags/projet_final/dev && cp -rfv fetch_data_dag.py train_model.py ../../

echo ""
echo "-> lancement fetch_data_dag.py"
echo ""

python3 fetch_data_dag.py

echo ""
echo "-> lancement train_model.py"
echo ""

python3 train_model.py