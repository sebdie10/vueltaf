import flask
from flask import request, session, redirect
import json
from flask_mysqldb import MySQL
import registro

app= flask.Flask(__name__)
app.secret_key = 'cortina'

# Required configuracion de mysql
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "vueltaf"

mysql = MySQL(app)




@app.route('/crearusuario', methods =['GET','POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form['email']
        userName = request.form['username']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña = request.form['Contraseña']
        registro.registrar(mysql,userName,nombre,apellido,contraseña,email)
    return flask.render_template('registroUsuario.html')


@app.route("/login", methods=['GET','POST'])
def login_():
    if request.method == 'POST':
        userName = request.form['email']
        contraseña = request.form['contraseña']
        session['user_id'] = registro._login(mysql,userName,contraseña)
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
    cur = mysql.connection.cursor()
    cur.execute("select * from carreras24 where estado = 'proximo'")
    data = cur.fetchall()
    nombre = data[0][1]
    print(data)
    data= data[0]
    fecha=data[2]
    fecha_f= fecha.date()
    print(fecha)
    #nombre = data[0][1]#'GP Bahrein'
    #fecha = '2024-02-29'
    hora = fecha.time()#'00:00:00'
    return flask.render_template('temporizador.html', nombre=nombre, fecha=fecha_f, hora=hora)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)