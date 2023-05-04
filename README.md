# Projet en local IA Cloud final:


## Description des tâches réalisées: 
done Créer un nouveau DAG Airflow avec une tâche pour récupérer le jeu de données en utilisant des opérateurs Python
done Utiliser Scikit-learn pour entraîner le modèle
done suivre les métriques d'entraînement avec mlflow
done Envoyer le modèle entraîné dans MLFlow Model Registry

done Utiliser FastAPI pour créer une API qui utilise le modèle
done Écrire un fichier Dockerfile pour Dockeriser l'API

done Construire l'image Docker
done Envoyer l'image Docker construite dans un registry distant 

done Créer un script qui récupère l'image Docker du registry et le dernier modèle entraîné
done Déployer l'API en local


## Actions à réaliser pour déployer un modèle, dockeriser l'API, créer un environnement virtuel et installer les dépendances:
-> cloner le projet Git dans vos dags Airflow, le chemin devrait ressembler à ceci:   /home/nom/airflow/dags

-> modifier les droits des fichiers situés dans /airflow/dags/projet_final/scripts:   chmod +x init.sh start.sh stop.sh

-> lancer tout d'abord le script init.sh:   ./init.sh

-> puis lancer le script start.sh une fois que le fichier init à terminé de s'exécuter:   ./start.sh

-> pour supprimer les fichiers et dossiers générés par les deux scripts précédents et qui pourraient créer des conflits en cas de nouvelle initialisation:   ./stop.sh

