# brent_oil_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import ruptures as rpt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load and preprocess data
def load_and_preprocess(file_path):
    logging.info("Loading and preprocessing data.")
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by='Date').set_index('Date')
    data['Price'] = data['Price'].interpolate()
    logging.info("Data loaded and missing values interpolated.")
    return data

# Function for exploratory data analysis (EDA) - price trends
def plot_price_trends(data):
    logging.info("Plotting price trends.")
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Brent Oil Prices Over Time')
    plt.legend()
    plt.show()
    logging.info("Price trend plot completed.")

# Function to calculate basic statistics and volatility
def calculate_basic_statistics(data):
    logging.info("Calculating basic statistics.")
    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    std_dev_price = data['Price'].std()
    rolling_std_dev = data['Price'].rolling(window=30).std()
    
    logging.info(f"Mean price: {mean_price}")
    logging.info(f"Median price: {median_price}")
    logging.info(f"Standard deviation of price: {std_dev_price}")
    
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    plt.plot(data.index, rolling_std_dev, label='30-Day Rolling Volatility', linestyle='--', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price and Volatility (USD)')
    plt.title('Brent Oil Prices and Rolling Volatility')
    plt.legend()
    plt.show()
    
    return mean_price, median_price, std_dev_price

# Bayesian Change Point Detection using PyMC3
def bayesian_change_point_detection(data, mean_price):
    logging.info("Starting simplified Bayesian change point detection.")
    
    # Calculate cumulative sums to look for a point of deviation from the overall mean
    price_array = data['Price'].values
    cumulative_sum = np.cumsum(price_array - mean_price)
    
    # Detect the point of maximum deviation as a candidate for change point
    change_point_index = np.argmax(np.abs(cumulative_sum))
    
    # Plot results
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, price_array, label='Brent Oil Price')
    plt.axvline(x=data.index[change_point_index], color='red', linestyle='--', label='Change Point')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Brent Oil Prices with Simplified Change Point Detection')
    plt.legend()
    plt.show()
    
    logging.info(f"Simplified Bayesian change point detection completed. Change point detected at index {change_point_index}")
    return change_point_index

# Function for change point detection using PELT algorithm
def pelt_change_point_detection(data, penalty=10, model_type="rbf"):
    logging.info("Starting PELT change point detection.")
    price_array = data['Price'].values
    algo = rpt.Pelt(model=model_type).fit(price_array)
    change_points = algo.predict(pen=penalty)
    
    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    for cp in change_points[:-1]:
        plt.axvline(x=data.index[cp], color='red', linestyle='--', label='Change Point' if cp == change_points[0] else "")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Brent Oil Prices with Detected Change Points (PELT)')
    plt.legend()
    plt.show()
    
    logging.info("PELT change point detection completed.")
    logging.info(f"Detected change points: {change_points}")
    return change_points

# Function to perform ARIMA modeling
def apply_arima(data, order=(1, 1, 1)):
    model = ARIMA(data['Price'], order=order)
    model_fit = model.fit()
    
    # Plot model fit and forecast
    plt.figure(figsize=(14, 7))
    plt.plot(data['Price'], label='Original')
    plt.plot(model_fit.fittedvalues, color='red', label='ARIMA Fit')
    plt.legend(loc='best')
    plt.title('ARIMA Model Fit')
    plt.show()
    
    return model_fit.summary()