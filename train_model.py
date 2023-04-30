import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib


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

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse}")

joblib.dump(model, "temperature_prediction_model.joblib")
