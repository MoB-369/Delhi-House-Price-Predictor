from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from request
        data = request.json  

        # Convert JSON to Pandas DataFrame
        custom_data = CustomData(
            area=float(data["area"]),
            latitude=float(data["latitude"]),
            longitude=float(data["longitude"]),
            Bedrooms=float(data["Bedrooms"]),
            Bathrooms=float(data["Bathrooms"]),
            neworold=data["neworold"],
            type_of_building=data["type_of_building"],
            Furnished_status_Semi_Furnished=data["Furnished_status_Semi_Furnished"],
            Furnished_status_Unfurnished=data["Furnished_status_Unfurnished"]
        )

        pred_df = custom_data.get_data_as_data_frame()

        
        # Predict
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        results = float(results[0])
        return jsonify({"prediction": round(results, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  
