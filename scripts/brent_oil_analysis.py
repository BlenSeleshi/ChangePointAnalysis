# brent_oil_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import ruptures as rpt
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
    logging.info("Starting Bayesian change point detection.")
    with pm.Model() as model:
        # Priors
        mean_prior = pm.Normal('mean_prior', mu=mean_price, sigma=10)
        change_point = pm.DiscreteUniform('change_point', lower=0, upper=len(data)-1)
        
        # Likelihood
        likelihood = pm.Normal('likelihood', mu=mean_prior, sigma=10, observed=data['Price'])
        
        # Inference
        trace = pm.sample(1000, tune=1000, cores=2, progressbar=False)
    
    pm.plot_posterior(trace)
    plt.show()
    logging.info("Bayesian change point detection completed.")

# Function for change point detection using PELT algorithm
def pelt_change_point_detection(data, penalty=20, model_type="rbf"):
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
