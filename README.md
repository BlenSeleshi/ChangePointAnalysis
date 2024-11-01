# Brent Oil Price Analysis

This repository contains scripts and Jupyter notebooks for analyzing the impact of major political and economic events on Brent oil prices. The analysis includes time series forecasting with SARIMAX, change point detection using the Pruned Exact Linear Time (PELT) algorithm, and rolling volatility analysis. These methods aim to provide insights for investors, policymakers, and energy companies on how Brent oil prices respond to global events.

## Project Structure

- **`brent_oil_analysis.py`**: A Python script that performs ARIMA modeling, rolling volatility calculations, and change point detection.
- **`brent_oil_analysis.ipynb`**: A Jupyter notebook that provides an interactive environment to explore and visualize Brent oil prices, change points, and volatility trends over time. It includes detailed commentary and visualizations for each step of the analysis.

## Requirements

The analysis requires the following libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `ruptures`
- `scipy`

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Data

The analysis uses historical Brent oil price data, typically in a CSV format with columns:

- `Date`: Date of each price observation.
- `Price`: Brent oil price in USD.

Load the data into the script or notebook, ensuring it is in a time series format indexed by `Date`.

## Analysis Steps

### 1. SARIMAX Modeling

The **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous factors) model is used for time series forecasting. Key steps include:

- Differencing the data to make it stationary.
- Training an ARIMA(1,1,1) model on the differenced series.
- Evaluating model performance with Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) scores, as well as diagnostic plots (e.g., Ljung-Box and Jarque-Bera tests).
- Interpreting coefficients to understand the contribution of autoregressive and moving average components.

### 2. Rolling Volatility Calculation

The rolling volatility calculation provides a measure of price variability over a moving window:

- Compute the 30-day rolling standard deviation of the price series.
- Visualize the rolling volatility alongside the Brent oil price to observe periods of high and low volatility.
- Use the visualization to identify periods of price instability, which may correlate with known political or economic events.

### 3. Change Point Detection with PELT

Change point detection identifies moments where the trend or structure of the price series changes significantly:

- Use the **Pruned Exact Linear Time (PELT)** algorithm from the `ruptures` library to detect change points in the price series.
- Visualize change points as red dashed lines on the time series plot.
- This analysis helps to pinpoint dates where significant shifts in oil prices occurred, which can often be aligned with historical events impacting the energy market.

## Visualizations

The notebook and script include the following visualizations:

- **Brent Oil Price with Rolling Volatility**: Shows the Brent oil price trend over time with 30-day rolling volatility.
- **Brent Oil Price with Change Points**: Highlights change points identified using the PELT algorithm on the Brent oil price timeline.

Each visualization provides insight into historical patterns, volatility, and potential influences on oil prices.

## Usage

### Running the Script

To run the SARIMAX model and generate volatility and change point analysis, execute the script as follows:

```bash
python brent_oil_analysis.py
```

### Running the Notebook

The Jupyter notebook offers an interactive exploration of the data. Launch the notebook:

```bash
jupyter brent_oil_analysis.ipynb
```

The notebook is organized with explanations and visualizations for each analysis step. Modify parameters (e.g., rolling window size, SARIMAX model order) to experiment with different configurations.

## Results Interpretation

- **ARIMA Results**: Provides insights into the dynamics of Brent oil prices, showing how past prices influence current prices through autoregressive and moving average components.
- **Rolling Volatility**: Highlights periods of market instability, which may signal responses to economic or geopolitical events.
- **Change Point Detection**: Detects key moments when the Brent oil price trend shifts, allowing for historical event correlation analysis.

## Conclusion

This analysis framework helps stakeholders understand how major events impact Brent oil prices. The results and visualizations provide a comprehensive view of price trends, volatility patterns, and structural changes over time.

For further inquiries or suggestions, please contact the repository owner.
