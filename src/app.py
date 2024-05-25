from src.util.db import dbSeeder
from src.classess.Usuario import Usuario,consultarUsuario

def gestionEstudiantes():
    print("start application")
    dbSeeder()
    #user = Usuario("andres","123","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #user.crearUsuario()
    print(consultarUsuario("123"))