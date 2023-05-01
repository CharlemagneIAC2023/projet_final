from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd


class PredictionInput(BaseModel):
    year: int
    month: int
    day: int
    humidity: float


model_uri = "/home/charlemagne/mlflow_experiments/686774497317680375/fd24d9dd3ea14106ba9a23d6aa1de02a/artifacts/linear_regression_model"
model = mlflow.pyfunc.load_model(model_uri)
app = FastAPI()

@app.post("/predict")
async def predict(input_data: PredictionInput):
    df = pd.DataFrame([input_data.dict()], columns=["year", "month", "day", "humidity"])
    prediction = model.predict(None, df)
    return {"max_temp": prediction[0]}
