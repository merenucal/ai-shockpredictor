import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from core.lstm_model import build_lstm
from auth.paywall import check_subscription, show_paywall

st.set_page_config(page_title="AI ShockPredictor", layout="wide")

st.title("🚀 AI ShockPredictor Dashboard")
st.sidebar.title("Configuración")

plan = check_subscription()
st.sidebar.write(f"Plan Actual: **{plan}**")

# Simulación de datos
def get_mock_data():
    dates = pd.date_range(start='2025-01-01', periods=100, freq='H')
    data = pd.DataFrame({
        'Price': np.random.randn(100).cumsum() + 100,
        'Shock_Score': np.random.randint(0, 100, 100),
        'Sentiment': np.random.uniform(-1, 1, 100)
    }, index=dates)
    return data

df = get_mock_data()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Análisis de Shocks en Tiempo Real")
    st.line_chart(df[['Price', 'Shock_Score']])

with col2:
    st.subheader("Métricas Clave")
    current_score = df['Shock_Score'].iloc[-1]
    st.metric("Shock Score", f"{current_score}/100", delta=int(current_score - df['Shock_Score'].iloc[-2]))
    
    if current_score > 70:
        st.error("⚠️ ALTO RIESGO DE SHOCK DETECTADO")
    else:
        st.success("✅ Mercado Estable")

st.divider()

if plan == 'Free':
    st.subheader("🧠 Análisis Avanzado (LSTM + SHAP)")
    show_paywall()
else:
    st.subheader("🧠 Análisis Premium LSTM")
    st.write("Modelo LSTM procesando flujos on-chain y sentimiento de IA...")
    # Aquí iría la lógica de carga del modelo y visualización SHAP
    st.image("web/static/shap_summary.png", caption="Explicabilidad SHAP del Modelo")
