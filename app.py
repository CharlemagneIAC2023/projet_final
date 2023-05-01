from fastapi import FastAPI, HTTPException
import mlflow.pyfunc
import pandas as pd


app = FastAPI()

model_name = "WeatherPredictionModel"
model = mlflow.pyfunc.load_model(f"models:/{model_name}/production")

@app.post("/predict")
async def predict_weather(year: int, month: int, day: int, humidity: float):
    input_data = pd.DataFrame(
        [[year, month, day, humidity]],
        columns=["year", "month", "day", "humidity"]
    )

    try:
        prediction = model.predict(input_data)
        return {"predicted_max_temp": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
