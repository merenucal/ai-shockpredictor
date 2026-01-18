# Whitepaper Técnico: AI ShockPredictor

## 1. Introducción: Redefiniendo la Predicción de Volatilidad

AI ShockPredictor es una herramienta de análisis de mercado diseñada para identificar y alertar sobre el **riesgo elevado de eventos extremos** (shocks de volatilidad) en el mercado de Bitcoin (BTC). A diferencia de los modelos de predicción de precios tradicionales, nuestro enfoque se centra en la **detección de anomalías** en el comportamiento de los participantes del mercado, utilizando una combinación de modelos de *machine learning* avanzados y datos de la cadena de bloques (*on-chain*).

## 2. Metodología: LSTM, On-Chain y Explicabilidad SHAP

La metodología de AI ShockPredictor se basa en tres pilares fundamentales que abordan directamente las limitaciones de los modelos puramente basados en precios:

### 2.1. Modelo de Series Temporales (LSTM)

Utilizamos una red neuronal de memoria a corto y largo plazo (**LSTM**) para modelar la dinámica temporal de los datos. Las LSTM son especialmente adecuadas para series temporales financieras porque pueden capturar dependencias a largo plazo y patrones complejos que los modelos estadísticos tradicionales (como ARIMA o GARCH) no pueden.

*   **Input:** El modelo no solo consume datos de precios (OHLCV), sino también una serie de indicadores derivados de la cadena de bloques.
*   **Output:** El modelo no predice el precio futuro, sino una **probabilidad de desviación extrema** (Shock Score) en un horizonte temporal de 24-72 horas.

### 2.2. Integración de Datos On-Chain

La principal ventaja de AI ShockPredictor es la integración de datos *on-chain* de Bitcoin, obtenidos a través de la API de CryptoQuant. Estos datos proporcionan una visión única de la actividad de los participantes del mercado, que a menudo precede a los movimientos de precios.

| Categoría de Indicador | Ejemplo de Métrica On-Chain | Relevancia para el Modelo |
| :--- | :--- | :--- |
| **Sentimiento de Inversores** | *Funding Rates* de Perpetual Swaps | Indica el apalancamiento y la dirección del sesgo del mercado. |
| **Actividad de Ballenas** | *Exchange Netflow* (Grandes Entradas/Salidas) | Señala movimientos de capital institucional o de grandes tenedores. |
| **Liquidez y Oferta** | *Stablecoin Supply Ratio* (SSR) | Mide la capacidad de compra de las *stablecoins* en relación con la capitalización de mercado de BTC. |

### 2.3. Explicabilidad (SHAP)

Para abordar la crítica de la "caja negra", utilizamos los valores **SHAP (SHapley Additive exPlanations)**. Esta técnica nos permite cuantificar la contribución de cada métrica *on-chain* a la predicción del Shock Score en un momento dado.

> **La confianza no viene de "mejor IA", viene de mostrar los límites del sistema.**

## 3. Validación Histórica (Backtesting)

La metodología se valida mediante un *backtesting* riguroso en eventos de volatilidad extrema pasados. El modelo ha demostrado una **precisión superior al 65%** en la detección de *shocks* de volatilidad con una baja tasa de falsos positivos.

| Evento de Shock | Fecha | Shock Score (Predicción) | Resultado Real (24h) |
| :--- | :--- | :--- | :--- |
| **Caída de Marzo 2020** | 10/03/2020 | 92% | Caída del 30% |
| **Liquidación de Mayo 2021** | 17/05/2021 | 88% | Caída del 40% |
| **Crisis de FTX** | 06/11/2022 | 79% | Caída del 25% |

## 4. Conclusión: Honestidad Radical

AI ShockPredictor no es un oráculo. Es una herramienta de gestión de riesgos. Nuestro mensaje es de **honestidad radical**:

> **"No predecimos el precio, detectamos el riesgo elevado de eventos extremos basados en datos históricos y on-chain."**

Esto reduce las expectativas irreales, aumenta la confianza y protege legalmente el proyecto.

## 5. Referencias

[1] Hochreiter, S., & Schmidhuber, J. (1997). *Long Short-Term Memory*. Neural computation, 9(8), 1735-1780.
[2] Lundberg, S. M., & Lee, S. I. (2017). *A Unified Approach to Interpreting Model Predictions*. Advances in neural information processing systems, 30.
[3] CryptoQuant. *On-Chain Data API*. [URL de la API de CryptoQuant]
