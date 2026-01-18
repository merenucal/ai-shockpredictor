# 🚀 Guía de Despliegue - AI ShockPredictor

## Información de Despliegue

**Dominio:** aishockpredictor.com
**Hosting:** Hostalia
**Tipo:** Landing Page + Redirecciones

---

## Paso 1: Configuración en Hostalia

1. Accede al panel de control de Hostalia
2. Ve a **Gestor de Archivos** (File Manager)
3. Navega a la carpeta **public_html**
4. Sube el archivo `landing_page.html`

---

## Paso 2: Configuración de la Página Principal

1. Renombra `landing_page.html` a `index.html`
2. Asegúrate de que los archivos de imagen estén en la carpeta correcta:
   - `/public_html/marketing/logo_hero.jpg`
   - `/public_html/marketing/logo_icon.png`

---

## Paso 3: Configuración de Redirecciones

Crea un archivo `.htaccess` en la raíz (`public_html/`) con el siguiente contenido:

```apache
# Redirección de tráfico HTTP a HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Redirecciones de rutas importantes
Redirect 301 /github https://github.com/merenucal/ai-shockpredictor
Redirect 301 /pro https://merenu.gumroad.com/l/gvdxqd
Redirect 301 /telegram https://t.me/aishockpredictor
Redirect 301 /bluesky https://bsky.app/profile/aishockpredictor.bsky.social
```

---

## Paso 4: Verificación SSL

- Asegúrate de que SSL/TLS está habilitado en Hostalia
- Verifica que el certificado es válido para `aishockpredictor.com`

---

## Paso 5: Optimización SEO

1. Verifica que el archivo `index.html` tiene los meta tags correctos
2. Envía el sitio a Google Search Console
3. Configura un sitemap (opcional pero recomendado)

---

## Estructura de Carpetas Recomendada

```
public_html/
├── index.html (landing_page.html renombrado)
├── marketing/
│   ├── logo_hero.jpg
│   └── logo_icon.png
└── .htaccess
```

---

## Verificación Final

Después del despliegue:
1. Accede a https://aishockpredictor.com
2. Verifica que todas las imágenes se cargan correctamente
3. Prueba todos los botones y enlaces
4. Comprueba la responsividad en móvil

---

## Soporte

Para problemas de despliegue, contacta con el soporte de Hostalia o envía un email a merenucal@gmail.com
