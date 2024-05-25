import sqlite3

def connectDatabase():
    con = sqlite3.connect("gestion-estudiantes.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con,cur

def dbSeeder():
    con, cur = connectDatabase()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS Users (
            id TEXT NOT NULL,
            password TEXT NOT NULL,
            userName TEXT NOT NULL,
            nombre TEXT NOT NULL,
            edad TEXT NOT NULL,
            genero TEXT NOT NULL,
            direccion TEXT NOT NULL,
            cellphone TEXT NOT NULL,
            email TEXT NOT NULL,
            tipo TEXT NOT NULL,
            CONSTRAINT Users_PK PRIMARY KEY (id)
        );
        ''')
    con.commit()
    cur.execute(
        ''' CREATE TABLE IF NOT EXISTS Asignaturas (
                nombre TEXT NOT NULL,
                profesorId TEXT NOT NULL,
                CONSTRAINT NewTable_PK PRIMARY KEY (nombre),
                FOREIGN KEY (profesorId) REFERENCES Users(id)
            );
        ''')
    con.commit()
    cur.execute(
        ''' CREATE TABLE IF NOT EXISTS Notas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                asignaturaNombre TEXT NOT NULL,
                estudianteId TEXT NOT NULL,
                porcentaje REAL NOT NULL,
                FOREIGN KEY (asignaturaNombre) REFERENCES Asignaturas(nombre)
                FOREIGN KEY (estudianteId) REFERENCES Users(id)
            );
        ''')
    con.commit()