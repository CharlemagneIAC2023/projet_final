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
# pip install fastapi uvicorn
# echo ""

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
echo "-> execution fetch_data_dag.py"
echo ""

python3 fetch_data_dag.py

echo ""
echo "-> execution train_model.py"
echo ""

python3 train_model.py

echo ""
echo "-> lancement ui mlflow, cliquer sur le lien pour ouvrir l'interface"
echo ""

gnome-terminal -- bash -c "mlflow ui --backend-store-uri file:///home/charlemagne/mlflow_experiments; exec bash" # insérer nouveau chemin si nouvel utilisateur 
sleep 10

# echo ""
# echo "-> lancement FastAPI"
# echo ""

# gnome-terminal -- bash -c "uvicorn app:app --reload --host 0.0.0.0 --port 8000 --log-level debug; exec bash"
# sleep 10

# echo ""
# echo "-> execution app.py"
# echo ""

# python3 app.py

echo ""
echo "-> rapatriement du modèle"
echo ""

cp -rfv /home/charlemagne/mlflow_experiments/686774497317680375/b47d9cbd35084959bbbc7696076996f4/artifacts/linear_regression_model ./models/


echo ""
echo "-> déploiement api docker"
echo ""

cd projet_final/dev && docker build -t fastapi_app .
docker run -p 8000:8000 fastapi_app

echo ""
echo "-> requête à l'API"
echo ""

curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"year": 2023, "month": 5, "day": 10, "humidity": 60}'
echo""