from src.classess.Usuario import Usuario
from src.util.db import connectDatabase

class Estudiante(Usuario):
    def __init__(self, userName, id, password, nombre, edad, genero, direccion, cellphone, email, asignatura=None):
        super().__init__(userName, id, password, nombre, edad, genero, direccion, cellphone, email)
        self.agregarAsignatura(asignatura)
    def agregarAsignatura(self,value):
        self._asignatura = value
    def __dir__(self):
        return["userName", "id", "password", "nombre", "edad", "genero", "direccion", "cellphone", "email", "asignatura"]
    def crearUsuario(self):
        try:
            con,cur = connectDatabase()
            tipo = "estudiante"
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