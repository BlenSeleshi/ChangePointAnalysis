from statsmodels.tsa.api import VAR
import logging
import joblib
import os

logging.basicConfig(filename='logs/var_model.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def train_var_model(data, lags=1):
    """Train a VAR model with specified lags."""
    model = VAR(data)
    var_model = model.fit(lags)
    logging.info(f"VAR model trained with lags={lags}")
    return var_model

def save_var_model(var_model, model_path="models/saved_model_files/var_model.pkl"):
    """Save the trained VAR model."""
    joblib.dump(var_model, model_path)
    logging.info(f"VAR model saved to {model_path}")

def forecast_var(var_model, steps=10):
    """Forecast future values using the VAR model."""
    forecast = var_model.forecast(var_model.y, steps=steps)
    logging.info(f"Forecasted {steps} steps using VAR model")
    return forecast

def impulse_response(var_model, impulse, response, steps=10):
    """Compute impulse response functions."""
    irf = var_model.irf(steps)
    logging.info(f"Impulse response function computed for {steps} steps")
    return irf.plot(impulse=impulse, response=response)
