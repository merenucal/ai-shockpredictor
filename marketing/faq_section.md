# Preguntas Frecuentes (FAQ) - AI ShockPredictor

## 1. ¿Qué es el "Shock Score"?

El **Shock Score** es una métrica de riesgo desarrollada por nuestra red neuronal LSTM que mide la probabilidad de que ocurra un evento de volatilidad extrema (un "shock") en el mercado de Bitcoin en las próximas 24-72 horas. Se basa en el análisis de datos on-chain (movimientos reales de capital) y no solo en el precio histórico.

---

## 2. ¿Cómo funciona AI ShockPredictor?

Nuestro modelo utiliza tres capas de análisis:

1.  **Datos On-Chain (CryptoQuant):** Analizamos el flujo de capital entre exchanges, los Funding Rates (apalancamiento), y el comportamiento de las ballenas (grandes tenedores).
2.  **Red Neuronal LSTM:** Entrena con estos datos históricos para aprender patrones que preceden a eventos de volatilidad extrema.
3.  **Explicabilidad SHAP:** Cada alerta incluye una explicación de qué factores on-chain dispararon la alerta, para que puedas auditar la decisión del modelo.

---

## 3. ¿Es una predicción de precios?

**No.** Somos muy claros en esto: **no predecimos precios**. Detectamos riesgo extremo. El Shock Score te dice cuándo el mercado está en una situación de alta volatilidad, no hacia dónde irá el precio.

---

## 4. ¿Qué precisión tiene el modelo?

Según nuestro backtesting histórico, el modelo detectó correctamente:
*   **Marzo 2020 (COVID Crash):** Shock Score en 92% el día anterior.
*   **Mayo 2021 (Elon Tweet Crash):** Shock Score en 78% horas antes.
*   **Noviembre 2022 (FTX Collapse):** Shock Score en 79% días antes.

Sin embargo, **no hay garantías en los mercados**. El modelo es una herramienta de gestión de riesgos, no una garantía de rentabilidad.

---

## 5. ¿Cuál es la diferencia entre el plan Free y el plan PRO?

| Característica | Free | PRO |
|---|---|---|
| Acceso al Dashboard | Sí | Sí |
| Histórico de Shock Scores | 7 días | Ilimitado |
| Alertas en Tiempo Real | No | Sí (Telegram) |
| Explicabilidad SHAP Detallada | No | Sí |
| Análisis On-Chain Avanzado | No | Sí |
| Precio | Gratis | 29€/mes (50% OFF ahora) |

---

## 6. ¿Cómo recibo las alertas en el plan PRO?

Las alertas llegan directamente a tu **canal privado de Telegram**. Recibirás:
*   Alerta instantánea cuando el Shock Score supere el 70%.
*   Resumen diario de riesgo bajo (Shock Score < 30%).
*   Explicación SHAP de cada alerta.

---

## 7. ¿Qué pasa si mi suscripción expira?

Si tu suscripción PRO expira (después de los 30 días de prueba gratuita), tu acceso al canal privado de Telegram se bloqueará automáticamente. Recibirás un mensaje con un enlace para renovar.

---

## 8. ¿El código está realmente abierto?

**Sí.** El código fuente está disponible en [GitHub](https://github.com/merenucal/ai-shockpredictor). Puedes auditar el modelo, contribuir mejoras, o crear tu propia versión.

---

## 9. ¿Quién está detrás de AI ShockPredictor?

El proyecto fue creado por **"Antonio"** (seudónimo). Hemos elegido el anonimato para que el foco se mantenga en la tecnología y los resultados, no en la persona. Cualquier consulta debe dirigirse a **merenucal@gmail.com**.

---

## 10. ¿Hay un período de prueba?

**Sí.** Todos los nuevos usuarios PRO reciben **30 días de prueba gratuita** (100% de descuento). Después de los 30 días, la suscripción se renueva automáticamente a 29€/mes, a menos que la canceles.

---

## 11. ¿Puedo cancelar en cualquier momento?

**Sí.** Puedes cancelar tu suscripción en cualquier momento desde tu panel de Gumroad. No hay penalizaciones ni cargos ocultos.

---

## 12. ¿Qué datos personales recopilan?

Solo recopilamos los datos necesarios para procesar tu suscripción (email y datos de pago a través de Gumroad). No vendemos ni compartimos tus datos con terceros.

---

## 13. ¿Funciona en móvil?

**Sí.** El dashboard es totalmente responsive y funciona en cualquier dispositivo. Las alertas de Telegram también llegan a tu móvil en tiempo real.

---

## 14. ¿Hay soporte técnico?

**Sí.** Si tienes dudas o problemas, puedes contactar a **merenucal@gmail.com**. Respondemos en un plazo de 24 horas.
