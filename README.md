# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

## Instalación

1. Clonar o descargar este proyecto.

2. Instalar dependencias necesarias:

pip install flask requests

3. Crear la base de datos:

python init_db.py

4. Ejecutar el servidor:

python servidor.py

5. Ejecutar el cliente:

python Cliente.py

## Endpoints

- POST/registro
  Registra un nuevo usuario.

{"usuario": "lucia", "contraseña": "1234"}

- POST/login
  Verifica usuario y contraseña.

{"usuario": "lucia", "contraseña": "1234"}

- POST/agregar_tarea
  Agrega una tarea asociada a un usuario.

{"usuario": "lucia", "descripcion": "Comprar pan"}

- POST /listar_tarea
  Lista las tareas del usuario.

{"usuario": "lucia"}

- GET/tareas
  Devuelve un HTML simple de bienvenida.

## Cliente en consola

Al ejecutar python Cliente.py se muestra el siguiente menú:

1. Registrar usuario

2. Login

3. Agregar tarea

4. Listar tareas

5. Ver HTML de /tareas

6. Salir

## Pruebas

Se incluye carpeta con capturas de pantalla mostrando:

- Menú

- Registro de un usuario nuevo.

- Login exitoso.

- Agregar una tarea.

- Listar las tareas de ese usuario.

- Visualización del HTML de /tareas.

## Respuestas Conceptuales:

- ¿Por qué hashear contraseñas?

Porque si alguien accede a la base de datos no podra ver las contraseñas.

- Ventajas de usar SQLite en este proyecto.

Es muy facil de usar y no necesita la instalación de un servidor de base de datos ademas de ser portable
