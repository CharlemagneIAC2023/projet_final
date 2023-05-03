from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
from mlflow.tracking import MlflowClient


class PredictionInput(BaseModel):
    year: int
    month: int
    day: int
    humidity: float


model_uri = "/home/charlemagne/mlflow_experiments/686774497317680375/b47d9cbd35084959bbbc7696076996f4//artifacts/linear_regression_model" # insérer nouveau chemin si nouvel utilisateur 
model = mlflow.pyfunc.load_model(model_uri)
app = FastAPI()

@app.post("/predict")
async def predict(input_data: PredictionInput):
    df = pd.DataFrame([input_data.dict()], columns=["year", "month", "day", "humidity"])
    prediction = model.predict(df)
    return {"max_temp": prediction[0]}
