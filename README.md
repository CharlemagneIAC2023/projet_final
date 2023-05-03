# projet_final

-> cloner le projet Git dans vos dags Airflow, le chemin devrait ressembler à ceci: /home/nom/airflow/dags

-> modifier les droits des fichiers situés dans /airflow/dags/projet_final/scripts: chmod +x init.sh start.sh stop.sh

-> lancer tout d'abord le script init.sh: ./init.sh

-> puis lancer le script start.sh une fois que le fichier init à terminé de s'exécuter: ./start.sh

-> pour supprimer les fichiers et dossiers générés par les deux scripts précédents et qui pourraient créer des conflits en cas de nouvelle initialisation, ainsi que stoper tous les processus lancés: ./stop.sh