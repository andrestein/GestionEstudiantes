from src.util.db import *

class Usuario:
    def __init__(self, userName, id, password, nombre, edad, genero, direccion, cellphone, email):
        self.id = id
        self.userName = userName
        self.password = password
        self.nombre = nombre
        self.edad = edad 
        self.genero = genero 
        self.direccion = direccion
        self.cellphone = cellphone
        self.email = email

    def crearUsuario(self):
        con,cur = connectDatabase()
        tipo = "administrador"
        cur.execute(f''' 
            INSERT INTO Users
            (id, password, userName, nombre, edad, genero, direccion, cellphone, email, tipo)
            VALUES('{self.id}', '{self.password}', '{self.userName}', 
            '{self.nombre}', '{self.edad}', '{self.genero}', 
            '{self.direccion}', '{self.cellphone}', '{self.email}', '{tipo}');
        ''')
        con.commit()
    def leerInformacionUsuario(self):
        con,cur = connectDatabase()
        rowData = cur.execute(f''' select * from users where id='{self.id}';''').fetchone()
        con.commit()
        return rowData
    
def consultarUsuario(id):
    con,cur = connectDatabase()
    rowData = cur.execute(f''' select * from users where id='{id}';''').fetchone()
    print(rowData.userName)
    con.commit()
    return rowData