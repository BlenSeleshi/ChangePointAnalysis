# Oil Price Analysis Project

## Overview

This repository contains scripts and Jupyter notebooks for analyzing the impact of major political and economic events on Brent oil prices. The analysis utilizes various modeling techniques, including time series forecasting with SARIMAX, change point detection using the Pruned Exact Linear Time (PELT) algorithm, and rolling volatility analysis. Additionally, it explores the dynamics of Brent oil prices through Vector Autoregression (VAR), Long Short-Term Memory (LSTM) networks, and Markov-Switching models. These methods aim to provide insights for investors, policymakers, and energy companies on how Brent oil prices respond to global events.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Analysis Steps](#analysis-steps)
- [Models](#models)
- [Data](#data)
- [Results Interpretation](#results-interpretation)
- [License](#license)

## Installation

To run this project, ensure you have Python 3.x installed, along with the necessary libraries. You can set up a virtual environment and install the required packages using pip. Here's how:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/oil-price-analysis.git
   cd oil-price-analysis
   ```

````

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
oil-price-analysis/
│
├── data/
│   └── your_data.csv               # Your input data file
├── models/
│       ├── var_model.pkl            # Saved VAR model
│       ├── markov_model.pkl         # Saved Markov-Switching model
│       ├── lstm_model.h5            # Saved LSTM model
│
├── scripts/
│   ├── data_preparation.py          # Data loading and preprocessing
│   ├── var_model.py                 # VAR model implementation
│   ├── markov_switching.py          # Markov-Switching model implementation
│   ├── lstm_model.py                # LSTM model implementation
│   ├── evaluation.py                # Model evaluation functions
│   └── brent_oil_analysis.py        # SARIMAX modeling and change point detection
│
└── brent_oil_analysis.ipynb          # Jupyter Notebook for analysis
```

## Requirements

The analysis requires the following libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `ruptures`
- `scipy`
- `tensorflow` (for LSTM)

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

### 4. VAR Model

Train a VAR model, generate forecasts, and compute Impulse Response Functions (IRFs) using the `var_model` module.

### 5. LSTM Model

Define, train, and evaluate an LSTM model for predicting future prices based on historical data.

### 6. Markov-Switching Model

Train and evaluate a Markov-Switching model for regime interpretation of the price series.

## Models

- **VAR Model**: Captures linear relationships between multiple time series and forecasts future values based on historical data.
- **LSTM Model**: A type of recurrent neural network (RNN) that is capable of learning long-term dependencies in time series data for more accurate predictions.
- **Markov-Switching Model**: Used for regime-switching analysis to understand different market conditions affecting oil prices.
- **SARIMAX Model**: A time series model used to capture the effects of seasonal variations and other exogenous factors on oil price forecasting.

## Visualizations

The notebook and script include the following visualizations:

- **Brent Oil Price with Rolling Volatility**: Shows the Brent oil price trend over time with 30-day rolling volatility.
- **Brent Oil Price with Change Points**: Highlights change points identified using the PELT algorithm on the Brent oil price timeline.
- **Forecast vs Actual Values**: Visualizes the performance of VAR and LSTM models against actual price data.

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
- **Model Performance**: Evaluation metrics (e.g., RMSE, MAE) are used to assess the forecasting accuracy of VAR and LSTM models.

## Conclusion

This analysis framework helps stakeholders understand how major events impact Brent oil prices. The results and visualizations provide a comprehensive view of price trends, volatility patterns, and structural changes over time.

For further inquiries or suggestions, please contact the repository owner.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
````
