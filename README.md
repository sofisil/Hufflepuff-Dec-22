# Sencillo PY

## Crear un entorno virtual.

MAC/Linux: `python3 -m venv venv`

Windows: `python -m venv venv o py -m venv venv`

## Activar el entorno virtual

UNIX/Mac/Linux: `source venv/bin/activate`

Windows: `.\venv\Scripts\activate` o `./venv/Scripts/activate`

## En caso de contar con alguna restriccion, normalmente en Windows

Debe ingresar a al Windows PowerShell y ejecutar en administrador

`Set-ExecutionPolicy Unrestricted`

## Una vez creado el entorno virtual deben Importar las dependencias correspondientes 

`pip install -r requirements.txt`

##Ejecutar con el comando

`flask run`
