from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

DB_FILE = "usuarios.db"

def registrar_usuario(usuario, contraseña):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        hash_pw = generate_password_hash(contraseña)
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, hash_pw))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def verificar_usuario(usuario, contraseña):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    conn.close()
    if fila and check_password_hash(fila[0], contraseña):
        return True
    return False

def agregar_tarea(usuario, descripcion):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (usuario, descripcion) VALUES (?, ?)", (usuario, descripcion))
    conn.commit()
    conn.close()

def listar_tareas(usuario):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion FROM tareas WHERE usuario = ?", (usuario,))
    filas = cursor.fetchall()
    conn.close()
    return filas    


@app.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")
    if not usuario or not contraseña:
        return jsonify({"error": "Se requiere usuario y contraseña"}), 400

    if registrar_usuario(usuario, contraseña):
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    else:
        return jsonify({"error": "El usuario ya existe"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")
    if verificar_usuario(usuario, contraseña):
        return jsonify({"mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route("/agregar_tarea", methods=["POST"])
def nueva_tarea():
    data = request.get_json()
    usuario = data.get("usuario")
    descripcion = data.get("descripcion")
    if not usuario or not descripcion:
        return jsonify({"error": "Faltan datos"})
    agregar_tarea(usuario, descripcion)
    return jsonify({"mensaje": "Tarea agregada"})

@app.route("/listar_tareas", methods=["POST"])
def ver_tareas():
    data = request.get_json()
    usuario = data.get("usuario")
    tareas = listar_tareas(usuario)
    return jsonify({"tareas": [{"id": t[0], "descripcion": t[1]} for t in tareas]})

@app.route("/tareas", methods=["GET"])
def tareas():
    return """
    <html>
        <head><title>Tareas</title></head>
        <body>
            <h1>Bienvenido!</h1>
            <p>lista de tareas</p>
            <ul>
                <li>Tarea 1</li>
                <li>Tarea 2</li>
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)       
