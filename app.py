# Importamos librerias
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

#Instanciamos la app en la variable app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instanciamos la base de datos en la variable db
db = SQLAlchemy(app)

@app.route("/")
def pag_inicio():
    return render_template("pag_inicio.html")

@app.route("/formulario")
def formular():
    return render_template("formulario.html")

#creamos los modelos para nuestra base de datos
class Usuarios (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(80), nullable = False)

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        

#Definimos nuestras rutas
@app.route('/formulario', methods=['GET', 'POST'])
def pagina_inicio():
    usuario = ''
    password = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        registro_usuario = Usuarios(usuario, password)
        db.session.add(registro_usuario)
        db.session.commit()
    return render_template('formulario.html')

@app.route('/admin')
def admin():
    usuarios = Usuarios.query.all()
    print(usuarios)
    return render_template('admin.html', usuarios = usuarios)

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar():
    usuarios = Usuarios.query.all()
    if request.method == 'POST':
        id = request.form['id_user']
        password_viejo = request.form['password_viejo']
        nuevo_password = request.form['nuevo_password']
        usuario = Usuarios.query.get(id)
        if password_viejo == usuario.password:
            usuario.password = nuevo_password
            db.session.add(usuario)
            db.session.commit()
            print("Password Cambiado")
    return render_template('/actualizar.html', usuarios = usuarios)

@app.route('/borrar', methods = ['GET', 'POST'])
def borrar():
    usuarios = Usuarios.query.all()
    if request.method == 'POST':
        id = request.form['id_user']
        usuario = Usuarios.query.get(id)
        print("Holis")
        db.session.delete(usuario)
        db.session.commit()
        return redirect(url_for('borrar'))
    return render_template('borrar.html', usuarios = usuarios)

if __name__ == '__main__':
    app.run(debug = True)
    with app.app_context():
        db.create_all(bind_key='__all__')

