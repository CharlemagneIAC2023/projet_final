#!/bin/bash


echo ""
echo ""
echo "  PROJET IA CLOUD: stop.sh"
echo ""
echo ""

echo ""
echo "-> supprime les fichiers générés ou déplacés durant le processus"
echo ""

rm -rfv ../carolus_ia_final/
rm -rfv ../../fetch_data_dag.py
rm -rfv ../../__pycache__/
rm -rfv ../../train_model.py
rm -rfv ../dev/models/
rm -rfv ../dev/__pycache__/
rm -rfv ../dev/weather_data.db
