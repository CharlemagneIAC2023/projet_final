#!/bin/bash


echo ""
echo ""
echo "  PROJET IA CLOUD: init.sh"
echo ""
echo ""

echo ""
echo "-> installation dépendances pour environnement virtuel"
echo ""
pip install virtualenv
pip install --upgrade pip

echo ""
echo "-> création environnement virtuel"
echo ""

cd ../ && virtualenv -p python3.10 carolus_ia_final

echo ""
echo "-> activez l'environnement virtuel grâce à la commande suivante:"
echo "source ../carolus_ia_final/bin/activate"
echo "-> une fois fait, lancez le script start.sh"
echo ""
