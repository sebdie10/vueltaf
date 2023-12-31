import flask
from flask import request, session, redirect
import json
import registro
import sqlite3
from datetime import datetime

app= flask.Flask(__name__)
app.secret_key = 'cortina'

# Required configuracion de mysql
formato_fecha = '%Y-%m-%d %H:%M:%S'

db = sqlite3.connect('db/vueltaf.db', check_same_thread=False)

@app.route('/')
def index():
    
    return redirect('/time')


@app.route('/crearusuario', methods =['GET','POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form['email']
        userName = request.form['username']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña = request.form['Contraseña']
        registro.registrar(db,userName,nombre,apellido,contraseña,email)
    return flask.render_template('registroUsuario.html')


@app.route("/login", methods=['GET','POST'])
def login_():
    if request.method == 'POST':
        userName = request.form['email']
        contraseña = request.form['contraseña']
        session['user_id'] = registro._login(db,userName,contraseña)
        print(session['user_id'])
        if session['user_id']:
            return redirect('/time')
    return flask.render_template('login.html')

@app.route('/logout')
def cerrarSesion():
   session.clear()
   return redirect('/login')


@app.route('/time')
def tiempo():
    cur = db.cursor()
    cur.execute("select * from carreras24 where estado = 'proximo'")
    data = cur.fetchall()
    print(data)
    nombre = data[0][1]
    data= data[0]
    fecha=data[2]
    fecha_objeto = datetime.strptime(fecha, formato_fecha)
    fecha_f= fecha_objeto.date()
    print(type(fecha_f))
    #nombre = data[0][1]#'GP Bahrein'
    #fecha = '2024-02-29'
    hora = fecha_objeto.time()#'00:00:00'
    return flask.render_template('temporizador.html', nombre=nombre, fecha=fecha_f, hora=hora)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)