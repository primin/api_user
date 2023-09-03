# api-usuario
Proyecto para módulo 3 diplomado Full-Stack
API de usuario realizada en Python con Flask
Los pasos para ejecutar el proyecto son los siguientes:

1.- Crear la Base de Datos diplomado en Postgres ejecutando el siguiente script:
CREAR BASE DE DATOS diplomado
    CON
    PROPIETARIO = postgres
    CODIFICACIÓN = 'UTF8'
    LC_COLLATE = 'Español_Bolivia.1252'
    LC_CTYPE = 'Español_Bolivia.1252'
    ESPACIO DE TABLA = pg_default
    LÍMITE DE CONEXIÓN = -1
    IS_TEMPLATE = Falso;

2.- Crear las siguientes tablas dentro de la Base de datos diplomado:
CREAR TABLA public.usuario
(
    id_usuario carácter(36) COLLATE pg_catalog."default" NO NULL,
    nombre carácter variable(50) COLLATE pg_catalog."default",
    primer_apellido carácter variable(50) COLLATE pg_catalog."default",
    segundo_apellido carácter variable(50) COLLATE pg_catalog."default",
    cedula_identidad carácter variable(15) COLLATE pg_catalog."default",
    fecha_nacimiento fecha,
    RESTRICCIÓN usuario_pkey CLAVE PRIMARIA (id_usuario)
)

TABLESPACE pg_default;

ALTERAR TABLA SI EXISTE public.usuario
    PROPIETARIO de postgres;

CREAR TABLA public.datos_api
(
    id bigint NO NULO,
    nombre_api carácter variable(30) COLLATE pg_catalog."default",
    versión de carácter variable(10) COLLATE pg_catalog."default",
    Carácter "desarrolladoPor" variable(70) COLLATE pg_catalog."default",
    carácter de correo electrónico variable(30) COLLATE pg_catalog."default",
    estado carácter variable(8) COLLATE pg_catalog."default",
    RESTRICCIÓN datos_api_pkey CLAVE PRIMARIA (id)
)

TABLESPACE pg_default;

ALTERAR TABLA SI EXISTE public.datos_api
    PROPIETARIO de postgres;

3 . Si no se encuentra instalado virtualenv, procedemos a instalarlo:
instalación de pip virtualenv
4 . Creamos el entorno virtual:
python -m virtualenv venv
5 . activar el entorno virtual:
.\venv\Scripts\activar
6 . Si aparece el error enable.ps1 porque la ejecución de scripts está deshabilitada en este sistema:
Vaya al menú de Windows y busque PowerShell.
Una vez en el powerShell escribe el siguiente comando:
Lista Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Force
7.- Abrir el ejecutar y escribir gpedit.msc, luego ir a Plantillas administrativas->Componentes de windows y buscar windows powerShell, una vez seleccionamos dicha opción nos vamos a la parte derecha y buscamos la opción "Activar la ejecución de scripts" y la abrimos, una vez dentro buscamos la opción Habilitada y en opciones buscamos la opción "Permitir solo scripts firmados", aplicamos los cambios y lo cerramos.
8 . Volvemos al código de Visual Studio y ejecutamos el entorno virtual.
.\venv\Scripts\activar
9 . Listamos todos los paquetes que tenemos instalados:
lista de pipas
10 . Istalamos flask, flask-cors, psycopg2, python-depair, python-dotenv:
pip install flask flask-cors psycopg2 desacoplamiento de python python-dotenv
11 . Hacer correr el programa:
pitón .\src\app.py

Para ejecutar las apis se sugiere utilizar postman, las direcciones son las siguientes:
1.- Para crear un usuario POST '/usuarios'
URL: localhost:5000/api/usuarios/usuarios
En cartero vamos a la sección Cuerpo, dentro de ella seleccionamos la opción raw y el tipo JSON, luego agregamos lo siguiente:
{
  "nombre": "Carlos",
  "primerApellido" : "Pinto",
  "segundoApellido" : "Machicado",
  "cédulaIdentidad": "7045932",
  "fechaNacimiento" : "1994-08-21"
}

2.- Para listar a todos lo usuarios: GET '/usuarios'
URL: localhost:5000/api/usuarios/

3.- Para listar un usuario en específico GET '/usuarios/ : id_usuario '
URL: localhost:5000/api/usuarios/idUsuario

4.- Para actualizar los datos de un usuario: PUT '/usuarios/ : id_usuario '
URL: localhost:5000/api/usuarios/usuarios/idUsuario
En cartero vamos a la sección Cuerpo, dentro de ella seleccionamos la opción raw y el tipo JSON, luego agregamos lo siguiente:
{
  "nombre" : "Alain",
  "primerApellido" : "Ramos",
  "segundoApellido" : "Paredes",
  "cédulaIdentidad": "7394201",
  "fechaNacimiento" : "2000-01-25"
}

5.- Para eliminar a un usuario: DELETE 'usuarios/ : id_usuario '
URL: localhost:5000/api/usuarios/usuarios/idUsuario

6.- Para mostrar el promedio de edades de los usuarios: GET '/usuarios/promedio-edad'
URL: localhost:5000/api/usuarios/promedio-edad/

7.- Para mostrar la versión del api rest: GET '/estado'
URL: localhost:5000/api/usuarios/estado/
