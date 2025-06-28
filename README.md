# PFO2_REDES
# Gestor de Tareas (PFO 2)

## Requisitos para instalar el proyecto

- Python 3
- Flask
- Bcrypt
- Requests

## Para instalar y ejecutar el proyecto 
1- Instalar python 3

2- Instalar dependencias:
pip install flask bcrypt requests

3- Correr el servidor
python servidor.py

 4- Enviar desde el cliente las peticiones
 
 ## Para ejecutar el proyecto 
 
 1- Registrar el usuario con metodo post a "/registro" enviando
 usuario y contraseña
 
 2- Autenticarse con el metodo post a "/login" enviando 
 usuario y contraseña con el que se registro
 
 3- si el usuario es valido nos redirige a la pagina
 (html) por metodo get "/tareas".

 ## ¿Por qué hashear contraseñas?
 
 Por que las contraseñas al encontrarse hasheadas si la base de datos es atacada no se obtienen las contraseñas originales.
 Por otro lado se evitan los ataques de diccionario y rainbow tables.
 Ademas el haseho resulta complejo para desencriptar, porque utiliza formulas matematicas complejas.
 
 ## Ventajas de usar SQLite
 
-No requiere servidor adicional.
-Es ideal para prototipos y aplicaciones pequeñas.
-Archivo único fácil de transportar y versionar.
