from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader, APIKey
from pydantic import BaseModel
import uvicorn
import numpy as np
from typing import List

app = FastAPI(title="AI ShockPredictor Commercial API", version="2.0.0")

API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Simulación de base de datos de API Keys (En producción usar DB real)
VALID_API_KEYS = {"sk_live_shock_12345": "Pro_User", "sk_test_shock_67890": "Trial_User"}

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header in VALID_API_KEYS:
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate credentials")

class ShockRequest(BaseModel):
    volume: List[float]
    sentiment: List[float]
    onchain_flow: List[float]

@app.get("/")
async def root():
    return {"status": "online", "message": "AI ShockPredictor API v2.0"}

@app.post("/v2/predict", tags=["Predictions"])
async def predict_shock(data: ShockRequest, api_key: APIKey = Depends(get_api_key)):
    """
    Endpoint principal para obtener el Shock Score basado en el modelo LSTM optimizado.
    """
    # Lógica de inferencia (Simulada para el ejemplo)
    # En producción: model.predict(np.array([data.volume, data.sentiment, data.onchain_flow]))
    mock_score = np.random.uniform(10, 95)
    
    return {
        "user_type": VALID_API_KEYS[api_key],
        "shock_score": round(mock_score, 2),
        "risk_level": "High" if mock_score > 70 else "Low",
        "timestamp": "2026-01-18T12:00:00Z"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
