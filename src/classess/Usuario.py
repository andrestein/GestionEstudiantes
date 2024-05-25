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
        try:
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
            print("Se creo el usuario con exito")
        except:
            print("Ups, ah ocurrido un error")
        
    def leerInformacionUsuario(self):
        try:
            con,cur = connectDatabase()
            rowData = cur.execute(f''' select * from users where id='{self.id}';''')
            user = None
            for user in rowData:
                user = Usuario(user["userName"],user["id"],
                    user["password"],user["nombre"],
                    user["edad"],user["genero"],user["direccion"],
                    user["cellphone"],user["email"])
            con.commit()
            return rowData
        except:
            print("Ups, ah ocurrido un error")
            return None
    
def consultarUsuario(id):
    try:
        con,cur = connectDatabase()
        rowData = cur.execute(f''' select * from users where id='{id}';''')
        user = None
        for user in rowData:
            user = Usuario(user["userName"],user["id"],
                user["password"],user["nombre"],
                user["edad"],user["genero"],user["direccion"],
                user["cellphone"],user["email"])
        con.commit()
        return user
    except:
        print("Ups, ah ocurrido un error")
        return None
        

def eliminarUsuario(id):
    try:
        con,cur = connectDatabase()
        cur.execute(f'''delete from users where id='{id}';''')
        con.commit()
        return "Se elimino con exito"
    except:
        print("Ups, ah ocurrido un error")
        return "Ups, ah ocurrido un error"

def actualizarUsuario(id,atributo,valor):
    try:
        con,cur = connectDatabase()
        cur.execute(f'''UPDATE Users
                    SET {atributo}='{valor}'
                    WHERE id='{id}';
                    ''')
        con.commit()
        return "Se actualizo con exito"
    except:
        return "Ups, ah ocurrido un error"