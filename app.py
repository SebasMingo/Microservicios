from flask import Flask, request, jsonify
import sqlite3
import os
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Conectar a la base de datos SQLite
def connect_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'db', 'productos.db')
    conn = sqlite3.connect(db_path)
    return conn

# Crear tabla de productos si no existe
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL)''')
    conn.commit()
    conn.close()

# Endpoint para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return jsonify(productos)

# Endpoint para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    nuevo_producto = request.json
    nombre = nuevo_producto['nombre']
    precio = nuevo_producto['precio']
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Producto creado exitosamente'}), 201

# Otras rutas ...

if __name__ == '__main__':
    create_table()
    app.run(port=5000, debug=True)
