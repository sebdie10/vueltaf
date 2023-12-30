
'''
def _login(db,username,contraseña):
    cur = db.cursor()
    cur.execute("select id from users where email = %s and contraseña = %s", (username,contraseña))
    data = cur.fetchall()
    return data[0][0]

def registrar(db,userName,nombre,apellido,contraseña,email):
    cur =db.cursor()
    cur.execute(
        'insert into users(nombre, apellido, user_name,contraseña,email) values(%s,%s,%s,%s,%s)',
        (
            nombre,
            apellido,
            userName,
            contraseña,
            email)
        )
    db.commit()
    pass
'''


def _login(db, username, contraseña):
    cur = db.cursor()
    cur.execute("SELECT id FROM users WHERE email = ? AND contraseña = ?", (username, contraseña))
    data = cur.fetchall()
    print(data)
    return data[0][0]


def registrar(db, userName, nombre, apellido, contraseña, email):
    cur = db.cursor()
    cur.execute(
        'INSERT INTO users(nombre, apellido, user_name, contraseña, email) VALUES (?, ?, ?, ?, ?)',
        (nombre, apellido, userName, contraseña, email)
    )
    db.commit()