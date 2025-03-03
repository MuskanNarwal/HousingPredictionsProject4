from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import os
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load dataset
df = pd.read_csv("housing_index_final.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

model_dir = "saved_models"

# Cache models and scalers to avoid reloading
models = {}
scalers = {}

# Load models and scalers for each region
for region in df["Geography"].unique():
    model_path = os.path.join(model_dir, f"lstm_{region}.h5")
    if os.path.exists(model_path):
        models[region] = load_model(model_path, compile=False)
        models[region].compile(optimizer='adam', loss='mse')

        # Fit scaler for the region
        scaler = MinMaxScaler()
        df_region = df[df["Geography"] == region].sort_values("Date")
        df_region["Scaled_Index"] = scaler.fit_transform(df_region[["Index Value"]])
        scalers[region] = scaler
    else:
        print(f"Model for region {region} not found at {model_path}")

def generate_predictions(region):
    if region not in models:
        return None, None

    df_region = df[df["Geography"] == region].sort_values("Date")
    scaler = scalers[region]

    seq_length = 12
    if len(df_region) < seq_length:
        print(f"Not enough data to generate predictions for region: {region}")
        return None, None

    X = np.array([df_region["Scaled_Index"].values[-seq_length:]])
    model = models[region]

    future_preds = []
    input_seq = X.reshape(1, seq_length, 1)

    for _ in range(72):
        pred = model.predict(input_seq, verbose=0)[0][0]
        future_preds.append(pred)
        input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

    future_preds = scaler.inverse_transform(np.array(future_preds).reshape(-1, 1))
    date_range = pd.date_range(start=df_region["Date"].max(), periods=73, freq='M')[1:]

    return date_range.strftime('%Y-%m-%d').tolist(), future_preds.flatten().tolist()

@app.route("/")
def home():
    return "<h1>Welcome to the Housing Index Prediction API</h1>"

@app.route("/predict", methods=["GET"])
def predict():
    region = request.args.get("region")
    print(f"Received request for region: {region}")  # Debugging log

    if not region:
        return jsonify({"error": "Region parameter is required"}), 400

    if region not in models:
        return jsonify({"error": f"Model for region '{region}' not found"}), 400

    # Generate predictions for the region
    dates, preds = generate_predictions(region)

    if dates and preds:
        return jsonify({"region": region, "dates": dates, "predictions": preds})
    else:
        return jsonify({"error": "Prediction failed for region: " + region}), 500

if __name__ == "__main__":
    print("Available regions:", df["Geography"].unique())  # Debugging log
    app.run(debug=True)