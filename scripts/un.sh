#!/bin/bash


pip install virtualenv
pip install --upgrade pip

cd ../ && virtualenv -p python3.10 carolus_ia_final

echo ""
echo ""
echo "  activer l'environnement virtuel grâce à la commande suivante:"
echo "  source ../carolus_ia_final/bin/activate"
echo "  une fois fait, lancer le script deux.sh"
echo ""