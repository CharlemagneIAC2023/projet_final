#!/bin/bash


# python3 ../../fetch_data_dag.py

# python3 ../../train_model.py

username=$USER
gnome-terminal -- bash -c "mlflow ui --backend-store-uri file:///home/$username/mlflow_experiments; exec bash"  
sleep 10

cd ../../../../mlflow_experiments/686774497317680375/ && last_directory=$(ls -td */ | head -n 1) 
cd -
cp -rfv ../../../../mlflow_experiments/686774497317680375/$last_directory/artifacts/linear_regression_model ./models/

cd projet_final/dev && docker build -t fastapi_app .
docker login
docker tag fastapi_app carolus174/fastapi_app
docker push carolus174/fastapi_app
scp -r carolus174/linear_regression_model ./models/
docker pull carolus174/fastapi_app

gnome-terminal -- bash -c "docker run -p 8000:8000 carolus174/fastapi_app; exec bash" 
sleep 10

echo ""
echo ""
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"year": 2023, "month": 5, "day": 10, "humidity": 60}'
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"year": 2023, "month": 5, "day": 11, "humidity": 60}'
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"year": 2023, "month": 5, "day": 12, "humidity": 60}'
echo ""
echo ""
