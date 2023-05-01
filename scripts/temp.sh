#!/bin/bash


echo ""
echo ""
echo "  PROJET IA CLOUD: temp.sh"
echo ""
echo ""


echo ""
echo "-> airflow db init"
echo ""

cd ../../../ 
pwd
gnome-terminal -- bash -c "echo'hello world'; exec bash"
pwd

echo ""
echo "-> déplacement des fichiers fetch_data_dag.py et train_model.py vers dossier dags de airflow"
echo ""
ls -la
cd dags/projet_final/dev && cp -rfv fetch_data_dag.py train_model.py ../../

echo ""
echo "-> lancement fetch_data_dag.py"
echo ""

#python3 fetch_data_dag.py

echo ""
echo "-> lancement train_model.py"
echo ""

#python3 train_model.py