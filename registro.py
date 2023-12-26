def _login(mysql,username,contraseña):
    cur = mysql.connection.cursor()
    cur.execute("select id from users where email = %s and contraseña = %s", (username,contraseña))
    data = cur.fetchall()
    return data[0][0]


def registrar(mysql,userName,nombre,apellido,contraseña,email):
    cur =mysql.connection.cursor()
    cur.execute(
        'insert into users(nombre, apellido, user_name,contraseña,email) values(%s,%s,%s,%s,%s)',
        (
            nombre,
            apellido,
            userName,
            contraseña,
            email)
        )
    mysql.connection.commit()
    pass