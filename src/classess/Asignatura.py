class Asignatura():
    def __init__(self,nombre,profesor,notas):
        self.nombre = nombre
        self.profesor = profesor,
        self.agregarNotas(notas)

    def agregarNotas(self,value):
        self._notas = value