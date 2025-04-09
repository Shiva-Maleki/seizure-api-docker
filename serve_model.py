from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)
model = joblib.load("seizure_model.pkl")

logging.basicConfig(level=logging.INFO)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    logging.info(f"Received input: {data}")
    
    required_fields = ["mean_bandpower", "spike_count", "frequency_variation"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
    
    df = pd.DataFrame([data])
    prediction = int(model.predict(df)[0])
    logging.info(f"Prediction: {prediction}")
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
   

