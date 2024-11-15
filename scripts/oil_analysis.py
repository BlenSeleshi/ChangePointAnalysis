# oil_analysis.py

import wbdata
import pandas as pd
from statsmodels.tsa.api import VAR
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_worldbank_data():
    """Fetches world economic indicators related to oil analysis."""
    indicators = {
        'NY.GDP.MKTP.CD': 'GDP', 
        'FP.CPI.TOTL.ZG': 'Inflation',
        'SL.UEM.TOTL.ZS': 'Unemployment', 
        'PA.NUS.FCRF': 'Exchange Rate'
    }
    
    try:
        logging.info("Fetching World Bank data...")
        # Fetch data without a date range and filter by dates afterwards
        data = wbdata.get_dataframe(indicators, country='WLD',date = ("1987-05-20", "2022-11-14"), freq='Y', source=None, parse_dates=False, keep_levels=False, skip_cache=False)
        data.reset_index(inplace=True)
        
        logging.info("Data fetched successfully.")
        return data

    except IndexError as e:
        logging.error("Data retrieval failed: Check indicator codes, country code, or date format.")
        raise e
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise e


def preprocess_data(df, oil_df):
    """Merges oil prices with economic data and scales it."""
    merged_df = pd.merge(df, oil_df, on='year', how='inner')
    # scaler = MinMaxScaler()
    # scaled_data = scaler.fit_transform(merged_df.iloc[:, 1:])
    # merged_df.iloc[:, 1:] = scaled_data
    return merged_df

def plot_correlation_matrix(df, title='Correlation Matrix'):
    """Plots the correlation matrix of the DataFrame."""
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    plt.title(title)
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.show()

def vector_autoregression(df):
    """Runs a Vector Autoregression model on the DataFrame."""
    model = VAR(df)
    var_result = model.fit(maxlags=15, ic='aic')
    print(var_result.summary())
    return var_result

def markov_switching_model(oil_prices):
    """Applies a Markov-Switching model to oil prices."""
    model = sm.tsa.MarkovRegression(oil_prices, k_regimes=2, trend='c', switching_variance=True)
    ms_model_fit = model.fit()
    print(ms_model_fit.summary())
    return ms_model_fit

import matplotlib.pyplot as plt

def plot_time_series(df, columns, title='Time Series Plot'):
    """Plots multiple selected columns in the DataFrame over time on a single plot."""
    plt.figure(figsize=(14, 8))
    
    for col in columns:
        if col in df.columns:
            plt.plot(df['Date'], df[col], label=col)  # Ensure each column is in the DataFrame
    
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()


