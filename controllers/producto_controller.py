from flask import Blueprint, request, jsonify
from services.producto_services import ProductoService
from config.conexion import get_db_session

producto_bp = Blueprint('productos', __name__)

service = ProductoService(get_db_session())

@producto_bp.route('/productos', methods=['GET'])
def get_productos():
    productos = service.listar_productos()
    return jsonify([{'id': p.id, 'codigo': p.codigo, 'producto': p.producto, 'precio': p.precio} for p in productos]), 200

@producto_bp.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    prod = service.obtener_producto(producto_id)
    if prod:
        return jsonify({'id': prod.id, 'codigo': prod.codigo, 'producto': prod.producto, 'precio': prod.precio}), 200
    return jsonify({'error': 'Producto no encontrado'}), 404

@producto_bp.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    codigo = data.get('codigo')
    producto = data.get('producto')
    precio = data.get('precio')
    if not codigo or not producto or precio is None:
        return jsonify({'error': 'Código, producto y precio son obligatorios'}), 400
    prod = service.crear_producto(codigo, producto, precio)
    return jsonify({'id': prod.id, 'codigo': prod.codigo, 'producto': prod.producto, 'precio': prod.precio}), 201

@producto_bp.route('/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    data = request.get_json()
    codigo = data.get('codigo')
    producto = data.get('producto')
    precio = data.get('precio')
    prod = service.actualizar_producto(producto_id, codigo, producto, precio)
    if prod:
        return jsonify({'id': prod.id, 'codigo': prod.codigo, 'producto': prod.producto, 'precio': prod.precio}), 200
    return jsonify({'error': 'Producto no encontrado'}), 404

@producto_bp.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    prod = service.eliminar_producto(producto_id)
    if prod:
        return jsonify({'message': 'Producto eliminado'}), 200
    return jsonify({'error': 'Producto no encontrado'}), 404
