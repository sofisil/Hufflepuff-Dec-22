# Sencillo PY

## Create a virtual enviroment. Crear un entorno virtual. 

MAC/Linux: `python3 -m venv venv`

Windows: `python -m venv venv o py -m venv venv`

##  Activate virtual enviroment. Activar el entorno virtual.

UNIX/Mac/Linux: `source venv/bin/activate`

Windows: `.\venv\Scripts\activate` o `./venv/Scripts/activate`

## If you have any restrictions, usually in Windows. En caso de contar con alguna restriccion, normalmente en Windows. 

You must enter Windows PowerShell and run in administrator. Debe ingresar a al Windows PowerShell y ejecutar en administrador.

`Set-ExecutionPolicy Unrestricted`

## Once the virtual environment is created, you must Import the corresponding dependencies. Una vez creado el entorno virtual deben Importar las dependencias correspondientes 

`pip install -r requirements.txt`

## Run with command. Ejecutar con el comando

`flask run`


