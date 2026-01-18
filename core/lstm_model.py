import tensorflow as tf
import numpy as np
import pandas as pd

def build_lstm(input_shape):
    """
    ARQUITECTURA OPTIMIZADA (>65% Accuracy Target)
    - Stacked LSTM con BatchNormalization para estabilidad.
    - Regularización L2 para evitar overfitting.
    - Optimizer Adam con Learning Rate Decay.
    """
    model = tf.keras.Sequential([
        # Primera capa con mayor capacidad
        tf.keras.layers.LSTM(128, return_sequences=True, input_shape=input_shape, 
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        
        # Segunda capa para capturar patrones complejos
        tf.keras.layers.LSTM(64, return_sequences=False),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        
        # Capas densas para refinamiento
        tf.keras.layers.Dense(32, activation='swish'),
        tf.keras.layers.Dense(16, activation='swish'),
        
        # Salida: Probabilidad de Shock (0-1) o Score
        tf.keras.layers.Dense(1, activation='sigmoid') 
    ])
    
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy', 'AUC'])
    return model

def prepare_data(df, window_size=30):
    """
    Prepara los datos para el modelo LSTM.
    """
    data = df.values
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size, 0]) # Asumiendo que la primera columna es el target
    return np.array(X), np.array(y)
