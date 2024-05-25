from src.classess.Profesor import Profesor
from src.classess.Estudiante import Estudiante
from src.classess.Administrador import Administrador
from src.classess.Usuario import checkUsuario

def login():
    username="profesor"
    password = "pass"
    tipo, user = checkUsuario(username,password)
    currentUser = None
    if(tipo == "administrador"):
        currentUser = Administrador(user.userName,user.id,
            user.password,user.nombre,user.edad,user.genero,
            user.direccion,user.cellphone,user.email)
    elif(tipo == "estudiante"):
        currentUser = Estudiante(user.userName,user.id,
            user.password,user.nombre,user.edad,user.genero,
            user.direccion,user.cellphone,user.email)
    elif(tipo == "profesor"):
        currentUser = Profesor(user.userName,user.id,
            user.password,user.nombre,user.edad,user.genero,
            user.direccion,user.cellphone,user.email)
    else:
        print("El usuario no existe")
    print(currentUser)