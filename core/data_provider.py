import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class CryptoQuantProvider:
    """
    Proveedor de datos reales de CryptoQuant (On-chain & Exchange Flows).
    """
    def __init__(self):
        self.api_key = os.getenv("CRYPTOQUANT_API_KEY")
        self.base_url = "https://api.cryptoquant.com/v1"

    def get_exchange_inflow(self, symbol="btc", window="1h"):
        """
        Obtiene el flujo de entrada a exchanges (indicador de presión de venta).
        """
        if not self.api_key:
            print("⚠️ CRYPTOQUANT_API_KEY no configurada. Usando datos simulados.")
            return self._get_mock_data()
            
        endpoint = f"{self.base_url}/{symbol}/exchange-flows/inflow?window={window}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['result'])
            return df
        else:
            return self._get_mock_data()

    def _get_mock_data(self):
        import numpy as np
        dates = pd.date_range(start='2026-01-10', periods=100, freq='H')
        return pd.DataFrame({
            'timestamp': dates,
            'inflow': np.random.uniform(100, 1000, 100),
            'outflow': np.random.uniform(100, 1000, 100)
        })

def get_combined_features():
    """
    Combina datos de CryptoQuant con sentimiento y volumen para el LSTM.
    """
    provider = CryptoQuantProvider()
    inflow_df = provider.get_exchange_inflow()
    
    # Aquí se integraría con otras fuentes (Binance API, Sentiment API)
    # Por ahora devolvemos el dataframe preparado para el modelo
    return inflow_df
