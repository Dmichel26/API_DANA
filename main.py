"""
Archivo principal de la aplicación Flask.
Configura JWT, conexión a base de datos y registra los controladores.
"""

import logging
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Importar los blueprints
from controllers.user_controller import user_bp
from controllers.producto_controller import producto_bp

# Importar la base y el engine de la configuración
from config.conexion import Base, engine

# =========================
# Configuración inicial
# =========================
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Clave secreta para firmar los tokens JWT (cámbiala en producción)
app.config["JWT_SECRET_KEY"] = "clave_super_segura_tienda"

# Inicializar JWT
jwt = JWTManager(app)

# Permitir solicitudes desde frontend o Swagger
CORS(app)

# =========================
# Base de datos
# =========================
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Tablas creadas/verificadas correctamente en la base de datos.")
except Exception as e:
    logger.error(f"Error al crear las tablas: {e}")

# =========================
# Registro de controladores
# =========================
app.register_blueprint(user_bp)
app.register_blueprint(producto_bp)
logger.info("Controladores registrados correctamente.")

# =========================
# Rutas base
# =========================
@app.route("/")
def index():
    return jsonify({
        "api": "Tienda API",
        "status": "OK",
        "descripcion": "API REST de tienda con usuarios, JWT y productos.",
        "autor": "Dana Michel Valderrama Merchán",
        "endpoints": {
            "/users/register": "Registrar usuario",
            "/users/login": "Iniciar sesión y obtener token JWT",
            "/productos": "CRUD de productos (requiere token)"
        }
    }), 200


@app.route("/health")
def health():
    return {"status": "ok"}, 200


# =========================
# Manejo básico de errores
# =========================
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found", "msg": "Recurso no encontrado"}), 404


@app.errorhandler(500)
def server_error(e):
    logger.exception("Error interno del servidor")
    return jsonify({"error": "Internal Server Error", "msg": "Error inesperado"}), 500


# =========================
# Punto de entrada
# =========================
if __name__ == "__main__":
    logger.info("Iniciando aplicación Flask...")
    app.run(debug=True)
