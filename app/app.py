from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

# Load processed analysis data (e.g., historical trends and event correlations)
price_trends_data = pd.read_csv( r'C:\Users\Blen\OneDrive\Documents\10Academy\Week10\data\Copy of BrentOilPrices.csv')  # Replace with the actual data file
event_data = pd.read_csv(r'C:\Users\Blen\OneDrive\Desktop\10Academy\ChangePointAnalysis\data\additional_economic_indicators.csv')  # Replace with the actual data file
model_metrics = {
    "rmse": 2.34,
    "mae": 1.16
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Brent Oil Price Dashboard API!"})

# Endpoint: Historical Price Trends
@app.route('/api/trends', methods=['GET'])
def get_price_trends():
    try:
        trends = price_trends_data.to_dict(orient='records')
        return jsonify({"status": "success", "data": trends})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Endpoint: Event Correlations
@app.route('/api/events', methods=['GET'])
def get_event_correlations():
    try:
        events = event_data.to_dict(orient='records')
        return jsonify({"status": "success", "data": events})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Endpoint: Model Metrics
@app.route('/api/metrics', methods=['GET'])
def get_model_metrics():
    try:
        return jsonify({"status": "success", "data": model_metrics})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
