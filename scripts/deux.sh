#!/bin/bash


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

cd ../../../ && rm -fv airflow.db && airflow db init

airflow users create --username carolus --email clement.charlemagne@ynov.com --firstname Clement --lastname Charlemagne --password carolus --role Admin

gnome-terminal -- bash -c "airflow webserver; exec bash"
sleep 10

gnome-terminal -- bash -c "airflow scheduler; exec bash"
sleep 10

cd dags/projet_final/dev && cp -rfv fetch_data_dag.py train_model.py ../../

echo ""
echo "-> activer et executer dag Airflow"
echo ""
echo "-> une fois fait, lancer le script trois.sh"
echo ""
echo ""