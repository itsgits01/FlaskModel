# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:39:41 2024

@author: gites
"""

from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

# Load the model
model = load_model('stock_price_model.h5')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Convert the incoming data to a DataFrame
    df = pd.DataFrame(data)
    # Process your data to match the model input shape
    last_60_days_data = ...  # Preprocess your data here
    
    # Make predictions
    predictions = predict_future_stock_price(model, last_60_days_data)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
