from flask import Flask, request, jsonify
import sqlite3
import os
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Conectar a la base de datos SQLite
def connect_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'db', 'pedidos.db')
    conn = sqlite3.connect(db_path)
    return conn

# Crear tabla de pedidos si no existe
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, productos TEXT, cantidad INTEGER)''')
    conn.commit()
    conn.close()

# Endpoint para crear un nuevo pedido
@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    nuevo_pedido = request.json
    print(f"Recibido: {nuevo_pedido}")  # Agregar esta línea para depuración
    productos = nuevo_pedido['productos']
    cantidad = nuevo_pedido['cantidad']
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (productos, cantidad) VALUES (?, ?)", (productos, cantidad))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Pedido creado exitosamente'}), 201

# Endpoint para obtener todos los pedidos
@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return jsonify(pedidos)

if __name__ == '__main__':
    create_table()
    app.run(port=5005, debug=True)
