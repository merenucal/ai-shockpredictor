import streamlit as st

def check_subscription():
    """
    Verifica el estado de suscripción del usuario.
    """
    if 'user_plan' not in st.session_state:
        st.session_state.user_plan = 'Free'
    
    return st.session_state.user_plan

def show_paywall():
    """
    Muestra la interfaz de pago si el usuario intenta acceder a funciones PRO.
    """
    st.warning("🔒 Esta función es exclusiva para usuarios PRO.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Free")
        st.write("€0 / mes")
        st.write("- Dashboard básico\n- Retraso de 1h")
        st.button("Plan Actual", disabled=True)

    with col2:
        st.subheader("Pro")
        st.write("€29 / mes")
        st.write("- Alertas en tiempo real\n- Modelo LSTM\n- Gráficos SHAP")
        st.link_button("Suscribirse (Gumroad)", "https://gumroad.com/l/shockpredictor-pro")

    with col3:
        st.subheader("Pro+")
        st.write("€99 / mes")
        st.write("- Todo lo de Pro\n- API Access\n- Soporte prioritario")
        st.link_button("Suscribirse (Gumroad)", "https://gumroad.com/l/shockpredictor-pro-plus")

def require_pro(func):
    """
    Decorador para proteger funciones PRO.
    """
    def wrapper(*args, **kwargs):
        if check_subscription() == 'Free':
            show_paywall()
        else:
            return func(*args, **kwargs)
    return wrapper
