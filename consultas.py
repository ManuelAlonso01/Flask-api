import sqlite3 as sql

def get_usuarios():
    conexion = sql.connect('database.db')
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        if resultados:
            data = []
            for i in resultados:
                usuario = {
                    'id': i[0],
                    'nombre': i[1],
                    'email': i[2],
                    'edad': i[3]
                }
                data.append(usuario)  
            return data
        else:
            return None
    except sql.Error:
        return None
    finally:
        conexion.close()

def get_usuario_id(id_usuario):
    conexion = sql.connect('database.db')
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
        resultado = cursor.fetchone()
        if resultado:
            data = []
            usuario = {
                'id': resultado[0],
                'nombre': resultado[1],
                'email': resultado[2],
                'edad': resultado[3]
                }
            data.append(usuario)  
            return data
        else:
            return None
    except sql.Error:
        return None
    finally:
        conexion.close()

def crear_usuario(nombre, email, edad):
    conexion = sql.connect('database.db')
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios(nombre, email, edad) VALUES (?, ?, ?)",
                       (nombre, email, edad,))
        conexion.commit()
        return True
    except sql.Error:
        return None
    finally:
        conexion.close()

def editar_usuario(id_usuario, nombre, email, edad):
    conexion = sql.connect('database.db')
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE usuarios SET nombre = ?, email = ?, edad = ? WHERE id = ?",
                       (nombre, email, edad, id_usuario))
        conexion.commit()
        return True
    except sql.Error:
        return None
    finally:
        conexion.close()

def eliminar_usuario(id_usuario):
    conexion = sql.connect('database.db')
    cursor = conexion.cursor()
    try:
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
        conexion.commit()
        return True
    except sql.Error:
        return None
    finally:
        conexion.close()
