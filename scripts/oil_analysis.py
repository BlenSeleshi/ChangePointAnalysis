# oil_analysis.py
# oil_analysis.py

import wbdata
import datetime
import pandas as pd

def fetch_data(countries, indicators, start_date, end_date):
    """
    Fetch data from the World Bank for given countries and indicators over a specified date range.
    
    Parameters:
    countries (list): List of country codes.
    indicators (dict): Dictionary of indicators with descriptive keys.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    DataFrame: A DataFrame containing the fetched data.
    """
    # Convert date strings to datetime objects
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    # Fetch the data from World Bank API
    data = wbdata.get_dataframe(indicators, country=countries, data_date=(start_date, end_date))
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
