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