# Flask-api

<img width="291" height="353" alt="image" src="https://github.com/user-attachments/assets/c4ee7683-eac1-4830-b435-f46d54ffbbe0" />

Esta api permite realizar operaciones CRUD (crear, leer, actualizar y borrar) sobre una base de datos de usuarios usando Flask y SQLite3.

## 1. Estructura del Proyecto.
  - ```main.py```: Punto de entrada de la aplicacion. Contiene las rutas y la logica de respúestas HTTP.
  - ```consultas.py```: Capa de acceso a datos. Gestiona la conexion a SQLite y las sentencias SQL.
  - ```erros.py```: Definicion de exepciones personalizadas para el manejo de errores.

## 2. Especificación de Endpoints.
  - ### **Obtener todos los usuarios**: Retorna una lista con todos los usuarios registrados.
    - URL: ```/usuarios```.
    - Metodo: ```GET```.
    - Respuestas:
        - ```200 OK```: Lista de objetos de usuario.
        - ```404 Not Found```: Si no hay usuarios en la base de datos.
        - ```500 Internal Server Error```: Si fallo la conexion a la base de datos.
      
  - ### **Obtener usuario por id**: Retorna los detalles de un usuario específico.
      - URL: ```/usuarios/id```
      - Metodo: ```GET```
      - Respuestas:
          - ```200 OK```: Objeto usuario {id, nombre, email, edad}.
          - ```404 Not Found```: El ID no existe.

  - ### **Crear nuevo usuario**:  Registra un usuario en el sistema.
      - URL: ```/usuarios```
      - Metodo: ```POST```
      - Cuerpo (JSON):
        ```bash
         {
            "nombre": "string",
            "email": "string",
            "edad": "integer"
          }
         ```
      - Respuestas:
        - ```200 OK```: Usuario creado exitosamente.
        - ```400 Bad Request```: Campos faltantes o JSON invalido.
  - ### **Actualizar usuario**: Modifica los datos de un usuario existente.
      - URL: ```/usuarios/id```
      - Método: ```PUT```
      - Cuerpo (JSON): Igual al POST.
      - Respuestas:
         - ```200 OK```: Actualización exitosa.
         - ```400 Bad Request```: Datos incompletos.
   - ### **Eliminar usuario**: Borra un usuario de la base de datos.
       - URL: ```/usuarios/id```
       - Método: ```DELETE```
       - Respuestas:
          - ```204 No Content```: Eliminación exitosa (sin cuerpo de respuesta).
          - ```404 Not Found```: El usuario no existe.
 ## 3. Manejo de Errores
  - ### **La API utiliza códigos de estado HTTP estándar y devuelve mensajes de error consistentes**:
    | Codigo | Descripcion    | Causa Comun                                                          |
    |--------|----------------|----------------------------------------------------------------------|
    | 400    | Bad Request    | El JSON enviado está mal formado o faltan llaves obligatorias.       |
    | 404    | Not Found      | El JSON enviado está mal formado o faltan llaves obligatorias.       |
    | 500    | Internal Error | Error inesperado en la base de datos SQLite.                         |
