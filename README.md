# 🛍️ API DANA – Tienda con Autenticación JWT

**API RESTful** desarrollada en **Flask** que permite la **gestión de usuarios y productos** con autenticación mediante **JSON Web Tokens (JWT)**.  
Ideal para aprender o implementar un backend seguro con operaciones CRUD y conexión a base de datos **SQLite**.

---

## 🚀 Características principales

- Registro e inicio de sesión de usuarios 🔐  
- Generación y validación de tokens JWT  
- CRUD completo de productos (crear, listar, actualizar y eliminar)  
- Acceso protegido: solo usuarios autenticados pueden manipular productos  
- Persistencia en base de datos SQLite (`mi_tienda.db`)  
- Arquitectura por capas: `controllers`, `services`, `repositories`, `models`, `config`

---

## 🧱 Estructura del proyecto

API_DANA/
│
├── config/
│ └── conexion.py
│
├── controllers/
│ ├── producto_controller.py
│ └── user_controller.py
│
├── models/
│ ├── producto_model.py
│ └── user_model.py
│
├── repositories/
│ ├── producto_repositories.py
│ └── user_repositories.py
│
├── services/
│ ├── producto_services.py
│ └── user_services.py
│
├── main.py
└── README.md


---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Dmichel26/API_DANA.git
cd API_DANA

2️⃣ Crear entorno virtual
python -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate         # En Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt


Si no tienes requirements.txt, puedes generarlo:

pip freeze > requirements.txt

4️⃣ Ejecutar la aplicación
python main.py


La API se ejecutará en:

http://127.0.0.1:5000

🔑 Endpoints principales
👤 Usuarios
➕ Registrar usuario
curl -X POST http://127.0.0.1:5000/users/register \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "12345"}'

🔐 Iniciar sesión (obtener token)
curl -X POST http://127.0.0.1:5000/users/login \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "12345"}'


Respuesta:

{
  "token": "<JWT_TOKEN>"
}

📦 Productos (requieren token)

⚠️ Reemplaza <TOKEN> con el JWT recibido tras iniciar sesión.

➕ Crear producto
curl -X POST http://127.0.0.1:5000/productos \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <TOKEN>" \
     -d '{"codigo": "P001", "producto": "Mouse inalámbrico", "precio": 95000}'

📋 Listar productos
curl -X GET http://127.0.0.1:5000/productos \
     -H "Authorization: Bearer <TOKEN>"

✏️ Actualizar producto
curl -X PUT http://127.0.0.1:5000/productos/1 \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <TOKEN>" \
     -d '{"precio": 99999}'

❌ Eliminar producto
curl -X DELETE http://127.0.0.1:5000/productos/1 \
     -H "Authorization: Bearer <TOKEN>"

🧩 Base de datos

Se crea automáticamente en la raíz del proyecto con el nombre:

mi_tienda.db

✨ Autor

Dana Michel Valderrama Merchán


🛠️ Tecnologías utilizadas

Python 3.10+

Flask

Flask-JWT-Extended

SQLAlchemy

SQLite

Flask-CORS
