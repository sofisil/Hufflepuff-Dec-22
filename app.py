# Importamos librerias
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

#Instanciamos la app en la variable app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instanciamos la base de datos en la variable db
db = SQLAlchemy(app)


#creamos los modelos para nuestra base de datos
class Usuarios (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    ciudad = db.Column(db.String(80), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    genero = db.Column(db.String(80), nullable = False)
    profesion = db.Column(db.String(80), nullable = False)

    def __init__(self, usuario, password, email, ciudad, edad, genero, profesion):
        self.usuario = usuario
        self.password = password
        self.email = email
        self.ciudad = ciudad
        self.edad = edad
        self.genero = genero
        self.profesion = profesion

#Definimos nuestras rutas
@app.route("/")
def pag_inicio():
    return render_template("pag_inicio.html")


@app.route('/formulario', methods=['GET', 'POST'])
def formulario_registro():
    usuario = ''
    password = ''   
    email = '' 
    ciudad = '' 
    edad = '' 
    genero = '' 
    profesion = ''

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        email = request.form['email']
        ciudad = request.form['ciudad']
        edad = request.form['edad']
        genero = request.form['genero']
        profesion = request.form['profesion']
        registro_usuario = Usuarios(usuario, password, email, ciudad, edad, genero, profesion)
        db.session.add(registro_usuario)
        db.session.commit()
        if profesion == 'EM':
            return redirect(url_for('info_emprendedor')) #cambiar a la funcion de la ruta de vista emprendedor dp
        elif profesion == 'PI':
            return redirect(url_for('info_profesional')) #cambiar a la funcion de la ruta de vista profesional
    return render_template('formulario.html')


@app.route('/ingreso')
def inicio_sesion():
    email = ''
    password = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and Usuarios.password == password:
            return render_template('/')
        return "<h1>Id de usuario invalido o contrasenha</h1>"
    return render_template('ingreso.html')

@app.route("/emprendedor")
def emprendedor():
    return render_template("emprendedor.html")

@app.route("/info_emprendedor")
def info_emprendedor():
    usuario = Usuarios.query.all()
    largor = len(usuario)-1
    diccionario_usuario = usuario[largor].__dict__
    nombre_usuario =  diccionario_usuario['usuario']
    return render_template("vista_emprendedor.html",nombre_usuario = nombre_usuario)

@app.route("/profesional")
def profesional():
    return render_template("profesional.html")


@app.route("/info_profesional")
def info_profesional():
    usuario = Usuarios.query.all()
    largor = len(usuario)-1
    diccionario_usuario = usuario[largor].__dict__
    nombre_usuario =  diccionario_usuario['usuario']
    return render_template("vista_profesional.html",nombre_usuario = nombre_usuario)

if __name__ == '__main__':
    app.run(debug = True)
    with app.app_context():
        db.create_all(bind_key='__all__')

