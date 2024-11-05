import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import logging

logging.basicConfig(filename='logs/evaluation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def evaluate_forecast(y_true, y_pred):
    """Evaluate forecast accuracy using RMSE and MAE."""
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    logging.info(f"Forecast evaluation - RMSE: {rmse}, MAE: {mae}")
    return rmse, mae

def plot_forecast(y_true, y_pred, title="Forecast vs Actual"):
    """Plot forecast vs actual values."""
    plt.figure(figsize=(12, 6))
    plt.plot(y_true, label="Actual")
    plt.plot(y_pred, label="Forecast", linestyle="--")
    plt.title(title)
    plt.legend()
    plt.show()
    logging.info("Forecast plot generated")
