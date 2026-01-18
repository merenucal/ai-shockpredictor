import shap
import matplotlib.pyplot as plt
import numpy as np

def get_shap_explanations(model, X_train, X_test, feature_names):
    """
    Genera explicaciones SHAP para el modelo LSTM.
    """
    # Para modelos de Deep Learning usamos DeepExplainer o GradientExplainer
    # Simplificamos usando una muestra para el background
    explainer = shap.GradientExplainer(model, X_train[:100])
    shap_values = explainer.shap_values(X_test[:10])
    
    # SHAP para series temporales puede ser complejo de visualizar directamente
    # Aquí generamos un resumen de importancia de características
    shap.summary_plot(shap_values[0][:, -1, :], X_test[:10, -1, :], feature_names=feature_names, show=False)
    plt.savefig('web/static/shap_summary.png')
    plt.close()
    
    return shap_values

def plot_local_explanation(shap_values, feature_names, index=0):
    """
    Genera un gráfico de fuerza para una predicción específica.
    """
    # Visualización simplificada para el dashboard
    pass
