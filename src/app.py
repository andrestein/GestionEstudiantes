from src.model.login import login
from src.classess.Administrador import Administrador
from src.classess.Profesor import Profesor
from src.classess.Estudiante import Estudiante
from src.util.db import dbSeeder
from src.classess.Usuario import Usuario

def gestionEstudiantes():
    print("start application")
    dbSeeder()
    login()
    #admin = Administrador("andres","123","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #admin.crearUsuario()
    #estudiante = Estudiante("estudiante","1234","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #estudiante.crearUsuario()
    #profesor = Profesor("profesor","1235","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #profesor.crearUsuario()
    
    
    