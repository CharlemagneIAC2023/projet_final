import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib
import mlflow.sklearn
import sklearn
import mlflow.pyfunc


class LinearRegressionModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = LinearRegression()
    
    def predict(self, context, model_input):
        return self.model.predict(model_input)


mlflow.set_tracking_uri("/home/charlemagne/mlflow_experiments/test_new_experiment")
mlflow.set_experiment("WeatherPrediction")
print("MLflow tracking URI:", mlflow.get_tracking_uri())

conn = sqlite3.connect("weather_data.db")
data = pd.read_sql_query("SELECT * FROM weather_data", conn)
conn.close()

data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month
data["day"] = data["date"].dt.day

X = data[["year", "month", "day", "humidity"]]
y = data["max_temp"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean squared error: {mse}")

    mlflow.log_metric("mse", mse)
    linear_regression_pyfunc = LinearRegressionModel()
    linear_regression_pyfunc.load_context(None)
    mlflow.pyfunc.log_model("linear_regression_model", python_model=linear_regression_pyfunc)

    run_id = mlflow.active_run().info.run_id
    artifact_uri = f"runs:/{run_id}/linear_regression_model"

registered_model = mlflow.register_model(artifact_uri, "WeatherPredictionModel")

from mlflow.tracking.client import MlflowClient

client = MlflowClient()
model_version = client.create_model_version(name=registered_model.name, source=artifact_uri, run_id=run_id)

stage = "Staging"
client.transition_model_version_stage(
    name=registered_model.name,
    version=model_version.version,
    stage=stage,
)
print(f"Model version {model_version.version} is now in '{stage}' stage.")

stage = "Production"
client.transition_model_version_stage(
    name=registered_model.name,
    version=model_version.version,
    stage=stage,
)
print(f"Model version {model_version.version} is now in '{stage}' stage.")
print(f"MLflow tracking URI: {mlflow.get_tracking_uri()}")


