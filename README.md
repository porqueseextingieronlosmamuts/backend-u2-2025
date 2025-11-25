**Descripción**: 
- Proyecto Django para llevar un registro de visitas (modelo `Visita`). Permite registrar nombre, RUT, motivo y la hora de entrada; además se añadió `fecha_de_salida` para marcar la salida desde el admin.

**Instalación y ejecución local**

Requisitos:
- Python 3.11+ (usar la versión que tengas configurada en el proyecto)
- Virtualenv (recomendado)

Pasos (Windows, `cmd.exe`):

1. Clonar el repositorio (si aún no lo tienes):
```
git clone <repo-url>
cd backend-u2-2025
```
2. Crear y activar un entorno virtual:
```
python -m venv venv
venv\Scripts\activate
```
3. Instalar dependencias:
```
pip install -r requirements.txt
```
4. Configurar variables de entorno (ejemplo en `.env`):
```
db_name=tu_db
db_user=tu_usuario
db_password=tu_pass
db_host=localhost
db_port=5432
```
5. Crear y aplicar migraciones:
```
python manage.py makemigrations
python manage.py migrate
```
6. Crear superusuario para acceder al admin (opcional pero recomendado):
```
python manage.py createsuperuser
```
7. Ejecutar servidor de desarrollo:
```
python manage.py runserver
```

Nota sobre archivos estáticos: la configuración tiene `STATIC_ROOT = BASE_DIR / 'staticfiles'`. Para (re)generar los archivos estáticos en `staticfiles`:
```
python manage.py collectstatic --noinput
```

**Rutas principales de la API / Vistas**

La aplicación `Visitas` expone vistas y plantillas. Las rutas principales en el proyecto son (rutas relativas al dominio):
- `/` : página principal con lista de visitas (según `Visitas/views.py`).
- `/visitas/nueva/` : formulario para crear una nueva visita.
- `/visitas/<id>/` : detalle de una visita.
- `/visitas/<id>/editar/` : editar visita.
- `/visitas/<id>/eliminar/` : eliminar visita.

Además, el admin de Django está disponible en:
- `/admin/` : interfaz administrativa (usar superusuario creado).

Si tu proyecto tiene rutas API REST adicionales (no presentes por defecto en este repo), añádelas aquí.

**Autenticación (endpoints y ejemplos)**

Este proyecto usa el admin de Django para la gestión; no se encontró en el código un sistema de API token/REST explícito. Para autenticarse en el admin usa las credenciales del superusuario creadas con `createsuperuser`.

Ejemplo de login al admin (navegador):
- URL: `http://127.0.0.1:8000/admin/`
- Usuario: el superusuario creado
- Password: la contraseña que definiste

Si prefieres exponer una API con autenticación token (ej. `rest_framework.authtoken` o JWT), puedo añadir endpoints y ejemplos de payload/curl. Indicaciones rápidas para añadir autenticación token con Django REST Framework:
1. Instala DRF y drf-simplejwt (opcional):
```
pip install djangorestframework djangorestframework-simplejwt
```
2. Añade `'rest_framework'` a `INSTALLED_APPS` y configura URLs para `token` o `jwt`.
3. Endpoints de ejemplo (si se implementan):
- `POST /api/token/` con payload `{"username": "user", "password": "pass"}` devuelve access/refresh tokens (JWT).

Ejemplo curl para JWT (si se añadiera):
```
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=tu_usuario&password=tu_pass"
```

**URL de despliegue en la nube (si aplica)**
- URL observada en `Registro/settings.py` en `ALLOWED_HOSTS`: `https://backend-u2-2025-production.up.railway.app`

Si necesitas que actualice o amplíe este README con rutas REST precisas, ejemplos de payloads reales, o documentación de cada vista y formulario, dime qué formato prefieres (OpenAPI, Markdown extendido, o un archivo `docs/`).

---
Última actualización: 2025-11-24
# backend-u2-2025

