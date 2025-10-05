from repositories.user_repositories import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from config.conexion import get_db_session   # ✅ usamos tu conexión real
import logging

logger = logging.getLogger(__name__)

class UserService:

    @staticmethod
    def register_user(username, password):
        db = get_db_session()  # ✅ abrimos sesión
        logger.info(f'Registrando usuario en servicio: {username}')
        try:
            existing_user = UserRepository.get_by_username(username, db)
            if existing_user:
                logger.warning(f'Intento de registro con usuario existente: {username}')
                return {'error': 'Usuario ya existe', 'username': username}

            hashed_password = generate_password_hash(password)
            user = UserRepository.create_user(username, hashed_password, db)
            logger.info(f'Usuario creado en servicio: {user.username} (ID: {user.id})')
            return user
        finally:
            db.close()  # ✅ cerramos la sesión

    @staticmethod
    def authenticate(username, password):
        db = get_db_session()
        logger.info(f'Autenticando usuario en servicio: {username}')
        try:
            user = UserRepository.get_by_username(username, db)
            if user and check_password_hash(user.password, password):
                logger.info(f'Autenticación exitosa en servicio: {username}')
                return user
            logger.warning(f'Autenticación fallida en servicio: {username}')
            return None
        finally:
            db.close()

    @staticmethod
    def get_all_users():
        db = get_db_session()
        logger.info('Obteniendo todos los usuarios en servicio')
        try:
            users = UserRepository.get_all(db)
            logger.info(f'{len(users)} usuarios obtenidos en servicio')
            return users
        finally:
            db.close()
