from models.producto_model import Producto
from sqlalchemy.orm import Session

class ProductoRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self):
        return self.db.query(Producto).all()
        
    def get_by_id(self, producto_id: int):
        return self.db.query(Producto).filter(Producto.id == producto_id).first()

    def create(self, codigo: str, producto: str, precio: float):
        new_producto = Producto(codigo=codigo, producto=producto, precio=precio)
        self.db.add(new_producto)
        self.db.commit()
        self.db.refresh(new_producto)
        return new_producto
    
    def update(self, producto_id: int, codigo: str = None, producto: str = None, precio: float = None):
        prod = self.get_by_id(producto_id)
        if prod:
            if codigo:
                prod.codigo = codigo
            if producto:
                prod.producto = producto
            if precio is not None:
                prod.precio = precio
            self.db.commit()
            self.db.refresh(prod)
        return prod

    def delete(self, producto_id: int):
        prod = self.get_by_id(producto_id)
        if prod:
            self.db.delete(prod)
            self.db.commit()
        return prod
