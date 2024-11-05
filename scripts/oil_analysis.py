# oil_analysis.py

import wbdata
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.api import VAR

def fetch_data(countries, indicators):
    """
    Fetch data from the World Bank for given countries and indicators.
    
    Parameters:
    countries (list): List of country codes.
    indicators (dict): Dictionary of indicators with descriptive keys.

    Returns:
    DataFrame: A DataFrame containing the fetched data.
    """
    data = wbdata.get_dataframe(indicators, country=countries, data_date=True)
    data.reset_index(inplace=True)
    return data

def plot_time_series(data, title):
    """
    Plot time series data.
    
    Parameters:
    data (DataFrame): DataFrame with time series data.
    title (str): Title for the plot.
    """
    plt.figure(figsize=(12, 6))
    for column in data.columns[1:]:
        plt.plot(data['date'], data[column], label=column)
    plt.legend()
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_correlations(data):
    """
    Calculate correlation between oil prices and economic indicators.
    
    Parameters:
    data (DataFrame): DataFrame containing oil prices and indicators.

    Returns:
    DataFrame: Correlation matrix.
    """
    return data.corr()

def fit_var_model(data):
    """
    Fit a VAR model to the data.
    
    Parameters:
    data (DataFrame): DataFrame for VAR modeling.

    Returns:
    results: Fitted VAR model results.
    """
    model = VAR(data)
    results = model.fit(maxlags=15, ic='aic')
    return results

def plot_correlation_heatmap(corr_matrix):
    """
    Plot a heatmap for the correlation matrix.
    
    Parameters:
    corr_matrix (DataFrame): Correlation matrix.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Correlation Heatmap')
    plt.show()
