import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
import logging
import os

logging.basicConfig(filename='logs/lstm_model.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_lstm_model(input_shape):
    """Define an LSTM model architecture."""
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    logging.info("LSTM model created")
    return model

def train_lstm_model(model, X_train, y_train, epochs=20, batch_size=32):
    """Train the LSTM model and save checkpoints."""
    checkpoint_dir = "models/saved_model_files/lstm_model.h5"
    checkpoint = ModelCheckpoint(checkpoint_dir, save_best_only=True)
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, callbacks=[checkpoint])
    logging.info(f"LSTM model trained for {epochs} epochs")
    return model, history
