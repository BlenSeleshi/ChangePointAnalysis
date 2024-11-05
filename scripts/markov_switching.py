from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression
import joblib
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def train_markov_switching(data, k_regimes=2):
    """Train a Markov-Switching model with the specified number of regimes."""
    model = MarkovRegression(data['Price'], k_regimes=k_regimes, trend='c', switching_variance=True)
    markov_model = model.fit()
    logging.info(f"Markov-Switching model trained with {k_regimes} regimes")
    return markov_model

def save_markov_model(markov_model, model_path="markov_model.pkl"):
    """Save the trained Markov-Switching model."""
    joblib.dump(markov_model, model_path)
    logging.info(f"Markov model saved to {model_path}")
