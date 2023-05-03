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


model_uri = "models/linear_regression_model"
model = mlflow.pyfunc.load_model(model_uri)
app = FastAPI()

@app.post("/predict")
async def predict(input_data: PredictionInput):
    df = pd.DataFrame([input_data.dict()], columns=["year", "month", "day", "humidity"])
    prediction = model.predict(df)
    return {"max_temp": prediction[0]}
