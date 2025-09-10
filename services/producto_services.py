from repositories.producto_repositories import ProductoRepository
from sqlalchemy.orm import Session

class ProductoService:
    def __init__(self, db_session: Session):
        self.repository = ProductoRepository(db_session)

    def listar_productos(self):
        return self.repository.get_all()
    
    def obtener_producto(self, producto_id: int):
        return self.repository.get_by_id(producto_id)

    def crear_producto(self, codigo: str, producto: str, precio: float):
        return self.repository.create(codigo, producto, precio)

    def actualizar_producto(self, producto_id: int, codigo: str = None, producto: str = None, precio: float = None):
        return self.repository.update(producto_id, codigo, producto, precio)

    def eliminar_producto(self, producto_id: int):
        return self.repository.delete(producto_id)
