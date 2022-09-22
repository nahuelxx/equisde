#models.py
from dbConn import dbConn
 
class librosModel():
    def __init__(self):
        self.titulo = ''
        self.autor = ''
        self.editorial = ''
        self.anio = 0
        self.paginas = 0
        self.isbn = 0
 
        #Abre la conexión con la base de datos Biblioteca y si no existe la crea.
        self.conn = dbConn('biblioteca.db')
        #Crea la tabla libros si no existe.
        command = 'CREATE TABLE IF NOT EXISTS libros ('\
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
            'titulo TEXT NOT NULL UNIQUE, '\
            'autor TEXT NOT NULL, '\
            'editorial TEXT NOT NULL, '\
            'anio INTEGER NOT NULL, '\
            'paginas INTEGER NOT NULL, '\
            'isbn TEXT NOT NULL UNIQUE)'
        #Ejecuta el comando en la base de datos.
        self.conn.execute(command)
 
    def create(self, titulo, autor, editorial, anio, paginas, isbn):
        command = 'INSERT INTO libros (titulo, autor, editorial, anio, paginas, isbn) VALUES (?, ?, ?, ?, ?, ?)'
        values = (titulo, autor, editorial, anio, paginas, isbn)
        return self.conn.execute(command, values)
 
    def read(self, id):
        command = 'SELECT * FROM libros WHERE id = ?'
        values = (id)
        return self.conn.execute(command, values)
 
    def update(self, id, titulo, autor, editorial, anio, paginas, isbn):
        command = ('UPDATE libros SET titulo = ?, autor = ?, editorial = ?, anio = ?, paginas = ?, isbn = ? WHERE id = ?')
        values = (titulo, autor, editorial, anio, paginas, isbn, id)
        return self.conn.execute(command, values)
 
    def delete(self, id):
        command = ('DELETE FROM libros WHERE id = ?')
        values = (id, )
        return self.conn.execute(command, values)
 
    def getAllData(self):
        command = ('SELECT * FROM libros')
        return self.conn.execute(command)
 
    def __del__(self):
        del self.conn
