import os
from atproto import Client

def run_sales_post():
    handle = "aishockpredictor.bsky.social"
    password = "writer9300"
    gumroad_link = "https://merenu.gumroad.com/l/gvdxqd"
    
    client = Client()
    client.login(handle, password)
    
    # Post de venta directa optimizado para Cashtags
    sales_text = (
        "🚨 **AI ShockPredictor** - La IA que ve el futuro del $BTC. 🧠⚡️\n\n"
        "Nuestro 'Shock Score' te alerta de la volatilidad extrema antes de que el caos golpee.\n\n"
        "No operes a ciegas. Usa la IA que detecta los movimientos de las ballenas en tiempo real.\n\n"
        "Últimos 10 cupos con 50% de descuento: `EARLYBIRD50`\n\n"
        f"👉 Consigue tu acceso PRO:\n{gumroad_link}\n\n"
        "#Crypto #AI #Trading #Bitcoin"
    )
    
    try:
        client.send_post(text=sales_text)
        print("Post de venta con Cashtag enviado con éxito.")
    except Exception as e:
        print(f"Error enviando post de venta: {e}")

if __name__ == "__main__":
    run_sales_post()
