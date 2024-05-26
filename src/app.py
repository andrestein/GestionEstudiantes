from src.model.menu import menuPrincipal
from src.model.login import login
from src.classes.Administrador import Administrador
from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.util.db import dbSeeder
from src.classes.Usuario import Usuario

def gestionEstudiantes():
    dbSeeder()
    menuPrincipal()
    #admin = Administrador("andres","123","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #admin.crearUsuario()
    #estudiante = Estudiante("estudiante","1234","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    
    #estudiante.crearUsuario()
    #profesor = Profesor("profesor","1235","pass","andres","24","Masculino","test","3015595423","andres.granda@gmail.com")
    #profesor.crearUsuario()
    
    
    