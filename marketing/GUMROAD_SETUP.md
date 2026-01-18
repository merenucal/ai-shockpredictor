# Configuración de Gumroad para ai-shockpredictor

Para empezar a cobrar hoy mismo, sigue estos pasos:

1. **Crear Producto:**
   - Ve a [Gumroad](https://gumroad.com/products).
   - Nombre: `ShockPredictor PRO`.
   - Tipo: `Suscripción`.
   - Precio: `€29 / mes`.

2. **Configurar Webhook (Opcional para automatización):**
   - En la pestaña "Content", añade el enlace a tu bot de Telegram o a la URL de tu API para activar la cuenta automáticamente tras el pago.

3. **Obtener Enlace de Checkout:**
   - Copia el enlace (ej: `https://gumroad.com/l/shockpredictor-pro`).
   - Pégalo en `auth/paywall.py` dentro del repositorio.

4. **Primeros 10 Usuarios PRO (Estrategia):**
   - Ofrece un cupón de descuento del 50% para los primeros 10: `EARLYBIRD50`.
   - Publica el cupón en el Post 1 de X/Bluesky.
