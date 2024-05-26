from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador
from src.model.login import login
from src.model.gestionAdmnistrador import registrarNuevoUsuario


tipo, user = login()

def mostrarMenu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'# {nombre}.')
    print(f"{user.nombre} ha ingresado como {tipo}. Seleccione una opción:")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leerOpcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutarOpcion(opcion, opciones):
    opciones[opcion][1]()

def generarMenu(nombre, opciones, opcion_salida):  
    opcion = None
    while opcion != opcion_salida:
        mostrarMenu(nombre, opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        

def menuPrincipal():
    opciones = None
    finalizar = "6"
    if(tipo == "administrador"):
        finalizar = "6"
        opciones = {
            "1": ("Registrar nuevo usuario.", registrarNuevoUsuario),
            "2": ("Consultar estudiante.", user.consultarEstudiante),
            "3": ("Actualizar información de usuario.", None),
            "4": ("Asignar asignatura.", None),
            "5": ("Cerrar sesión.", None),
            "6": ("Finalizar el programa.", None)
        }
    elif(tipo == "profesor"):
        finalizar = "6"
        opciones = {
            "1": ("Visualizar asignaturas.", None),
            "2": ("Visualizar información personal.", None),
            "3": ("Actualizar información personal.", None),
            "4": ("4. Asignar asignatura.", None),
            "5": ("Cerrar sesión.", None),
            "6": ("Finalizar el programa.", None)
        }
    elif(tipo == "estudiante"):
        finalizar = "5"
        opciones = {
            "1": (" Visualizar información personal.", None),
            "2": ("Actualizar información personal.", None),
            "3": ("Visualizar asignaturas.", None),
            "4": ("Cerrar sesión.", None),
            "5": ("Finalizar el programa.", None)
        }
    generarMenu("Menú principal", opciones, finalizar)

    def subMenuConsultarEstudiante():
        opciones = {
            "1": ("Consulta por id: ", ),            
            "2": ("Consulta por nombre", )   
        }


    while True:
        if(tipo == "administrador"):
            print("Bienvenido al menú de gestión de estudiantes.")
            print(f"{user.nombre} ha ingresado como {tipo}.")
            print("A continuación se mostraran las opciones a ejecutar: ")
            print("1. Registrar nuevo usuario")
            print("2. Actualizar información de usuario.")
            print("3. Consultar usuario.")
            print("4. Asignar asignatura")
            input("Ingrese su opción: ")
        elif(tipo == "Profesor"):
            print("Bienvenido al menú de gestión de estudiantes.")
            print(f"{user.nombre} ha ingresado como {tipo}.")
            print("1. Visualizar asignaturas")
            print("2. Visualizar información personal.")
            print("3. Actualizar información personal")
            print("4. Consultar estudiante.")
        elif(tipo == "Estudiante"):
            print("Bienvenido al menú de gestión de estudiantes.")
            print(f"{user.nombre} ha ingresado como {tipo}.")
            print("1. Visualizar información personal.")
            print("2. Actualizar información personal.")
            print("3. Visualizar asignaturas ")
            