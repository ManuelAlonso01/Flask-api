from flask import Flask, request
from consultas import *


app = Flask(__name__)


@app.route('/usuarios', methods=["GET"])
def obtener_usuarios():
    resultados = get_usuarios()
    if resultados:
        return resultados, 200
    else:
        return {"Error": "No se pudo obtener a los usuarios"}, 404
 
    
@app.route('/usuarios/<int:id>', methods=["GET"])
def obtener_usuario_id(id):
    resultado = get_usuario_id(id)
    if resultado:
        return resultado, 200
    else:
        return {"Error": "No se pudo obtener al usuario"}, 404
 
    
@app.route('/usuarios', methods=["POST"])
def insertar_usuario():
    data = request.get_json(silent=True)
    if not data:
        return {"Error": "JSON vacio o invalido"}, 400
    nombre = data.get('nombre')
    email = data.get('email')
    edad = data.get('edad')
    if not nombre or not email or not edad:
        return {"Error": "Faltan campos"}, 400
    if crear_usuario(nombre, email, edad):
        return "", 200
    else:
        return {"Error": "No se pudo insertar el usuario"}, 400
 
    
@app.route('/usuarios/<int:id>', methods=["PUT"])
def actualizar_usuario(id):
    data = request.get_json(silent=True)
    if not data:
        return {"Error": "JSON vacio o invalido"}, 400
    nombre = data.get('nombre')
    email = data.get('email')
    edad = data.get('edad')
    if not nombre or not email or not edad:
        return {"Error": "Faltan campos"}, 400
    if editar_usuario(id, nombre, email, edad):
        return "", 200
    else:
        return {"Error": "No se pudo actualizar el usuario"}, 400

@app.route('/usuarios/<int:id>', methods=["DELETE"])
def borrar_usuario(id):
    if eliminar_usuario(id):
        return "", 204
    else:
        return {"Error": "No se pudo eliminar al usuario"}, 404   

if __name__ == "__main__":
    app.run(port=5000, debug=True)