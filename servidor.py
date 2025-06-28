from flask import Flask, request, jsonify, redirect, url_for
import sqlite3
import bcrypt
from flask import render_template_string

app = Flask(__name__)
DB = 'usuarios.db'

# Inicializamos la base de datos
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            contrasena TEXT
        )  
    ''')
    conn.commit()
    conn.close()

init_db()

#  ruta de Registro
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({"error": "Datos incompletos"}), 400

    hash_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_contrasena))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409

# ruta de Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contraseña')

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = c.fetchone()
    conn.close()

    if resultado and bcrypt.checkpw(contrasena.encode('utf-8'), resultado[0]):
        return redirect(url_for('tareas'))
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Tareas (HTML de bienvenida)
@app.route('/tareas')
def tareas():
    html = """
    <!DOCTYPE html>    
    <head>
        <title>Bienvenido</title>
    </head>
    <body>
        <h1>¡Bienvenido a la app de tareas!</h1>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
