# centrar_ventana.py
# función centrar.
def centrar(ancho, alto, app):
    x = app.winfo_screenwidth() // 2 - ancho // 2
    y = app.winfo_screenheight() // 2 - alto // 2
 
    posi = str(ancho) + 'x' + str(alto) + '+' + str(x) + '+' + str(y)
 
    return posi
 
if __name__ == '__main__':
    pass

#main.py
import tkinter as tk
 
import controllers
 
from centrar_ventana import centrar
 
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(centrar(alto=475, ancho=780, app=root))
    root.resizable(False, False)
 
    controller = controllers.librosController(root)
    root.mainloop()

#dbConn.py
import sqlite3
 
class dbConn():
    def __init__(self, dbname):
        self.dbname = dbname
 
    def __connect(self):
        self.connection = sqlite3.connect(self.dbname)
 
    def __openCursor(self):
        self.cursor = self.connection.cursor()
 
    def __closeCursor(self):
        self.cursor.close()
 
    def createTable(self, tableName, fields):
        command = 'CREATE TABLE IF NOT EXISTS ' + tableName + fields
        self.__connect()
        self.connection.execute(command)
        self.connection.commit()
        self.connection.close()
 
    def execute(self, command, fields=()):
        self.__connect()
        self.__openCursor()
 
        if fields:
            self.cursor.execute(command, fields)
        else:
            self.cursor.execute(command)
 
        result = self.cursor.fetchall()
        self.connection.commit()
        self.__closeCursor()
        self.connection.close()
 
        return result

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

#views.py
import tkinter as tk
from tkinter import Button, ttk
 
class librosView():
    def __init__(self, root):
        self.root = root
        self.root.title('Administración de Biblioteca')
 
        self.frame1 = ttk.Frame(self.root, border=2, relief='groove')
        self.frame1.grid(padx=5, pady=5, row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
 
        self.labelId = ttk.Label(self.frame1, text='Id: ')
        self.labelId.grid(row=0, column=0, padx=5, pady=5)
 
        self.textvarId = tk.StringVar()
        self.entryId = ttk.Entry(self.frame1, textvariable=self.textvarId, state='disabled')
        self.entryId.grid(row=0, column=1, padx=5, pady=5)
 
        self.labelTitulo = ttk.Label(self.frame1, text='Título: ')
        self.labelTitulo.grid(row=1, column=0, padx=5, pady=5, sticky='e')
 
        self.textvarTitulo = tk.StringVar()
        self.entryTitulo = ttk.Entry(self.frame1, textvariable=self.textvarTitulo)
        self.entryTitulo.grid(row=1, column=1, padx=5, pady=5)
 
#----------------------------------------------------------------------
#A partir de este punto desarrollar el código incluyendo los widgets restantes, nombrar con el mismo criterio que se utilizó para Id y Autor
 
#Añadir un frame2 sin border ni relief y el sticky en todas las direcciones.
        self.frame2 = ttk.Frame(self.root)
        self.frame2.grid(padx=5, pady=5, row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
 
#Aplicamos estilos y los modificamos para la cabecera del treeview.
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", background='grey', foreground='white')
 
        #Define el nombre y el ancho en píxeles de las columnas.
        columns = {'Id': 50, 'Título': 200, 'Autor': 200, 'Editorial': 110, 'Año': 50, 'Páginas': 50, 'ISBN': 80}
        self.treeview = ttk.Treeview(self.frame2, columns=tuple(columns.keys()), show='headings', height=14, selectmode='browse')
        #Define las cabeceras
        for clave, valor in columns.items():
            self.treeview.heading(clave, text=clave)
            self.treeview.column(clave, width=valor)
 
        self.treeview.grid(row=0, column=0, sticky='nsew')
 
        #Añade un barra lateral de scroll (enrollado).
        scrollbar = ttk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
 
#Añadir un frame3 sin border ni relief.
        self.frame3 = ttk.Frame(self.root)
        self.frame3.grid(padx=5, pady=5, row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.buttonAdd = ttk.Button(self.frame3, text='Añadir')
        self.buttonAdd.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.buttonUpdate = ttk.Button(self.frame3,text='Actualizar')
        self.buttonUpdate.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.buttonRemove = ttk.Button(self.frame3, text='Remover')
        self.buttonRemove.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.buttonLimpiar = ttk.Button(self.frame3, text='Limpiar')
        self.buttonLimpiar.pack['command'] = self.limpiar

 
#Dentro del frame3 se incluyen los botones restantes como buttonUpdate, buttonRemove y buttonLimpiar.
 
#En el buttom limpiar agregar el command limpiar
        #self.buttonLimpiar['command'] = self.limpiar
#----------------------------------------------------------------------
 
        self.frame4 = ttk.Frame(self.root, border=1, relief='groove')
        self.frame4.grid(padx=5, pady=5, row=3, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
 
        statusbar = tk.Label(self.frame4, text='Tabla Libros', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
 
    def getId(self):
        return self.textvarId.get()
 
    def setId(self, id):
        self.textvarId.set(id)
 
    def getTitulo(self):
        return self.textvarTitulo.get()
 
    def setTitulo(self, titulo):
        self.textvarTitulo.set(titulo)
 
    def getAutor(self):
        return self.textvarAutor.get()
 
    def setAutor(self, author):
        self.textvarAutor.set(author)
 
    def getEditorial(self):
        return self.textvarEditorial.get()
 
    def setEditorial(self, editorial):
        self.textvarEditorial.set(editorial)
 
    def getAnio(self):
        return self.textvarAnio.get()
 
    def setAnio(self, year):
        self.textvarAnio.set(year)
 
    def getPaginas(self):
        return self.textvarPaginas.get()
 
    def setPaginas(self, pages):
        self.textvarPaginas.set(pages)
 
    def getIsbn(self):
        return self.textvarIsbn.get()
 
    def setIsbn(self, isbn):
        self.textvarIsbn.set(isbn)
 
    def getCursorId(self):
        selectedLbData = self.treeview.selection()
        id = self.treeview.item(selectedLbData)['values'][0]
        return id
 
    def getCursorTitulo(self):
        selectedLbData = self.treeview.selection()
        titulo = self.treeview.item(selectedLbData)['values'][1]
        return titulo
 
    def getCursorAutor(self):
        selectedLbData = self.treeview.selection()
        author = self.treeview.item(selectedLbData)['values'][2]
        return author
 
    def getCursorEditorial(self):
        selectedLbData = self.treeview.selection()
        editorial = self.treeview.item(selectedLbData)['values'][3]
        return editorial
 
    def getCursorAnio(self):
        selectedLbData = self.treeview.selection()
        year = self.treeview.item(selectedLbData)['values'][4]
        return year
 
    def getCursorPaginas(self):
        selectedLbData = self.treeview.selection()
        paginas = self.treeview.item(selectedLbData)['values'][5]
        return paginas
 
    def getCursorIsbn(self):
        selectedLbData = self.treeview.selection()
        isbn = self.treeview.item(selectedLbData)['values'][6]
        return isbn
 
    def setTreeview(self, data):
        if not data: return
        self.treeview.delete(*self.treeview.get_children())
        for row in data:
            self.treeview.insert('', tk.END, text=row[0], values=row)
 
    def limpiar(self):
        self.textvarId.set('')
        self.textvarTitulo.set('')
        self.textvarAutor.set('')
        self.textvarEditorial.set('')
        self.textvarAnio.set('')
        self.textvarPaginas.set('')
        self.textvarIsbn.set('')
 
        #Deselecciona fila de treeview.
        self.treeview.selection_remove(self.treeview.selection())
 
        return
#controllers.py
import views
import models
 
class librosController():
    def __init__(self, root):
        self.root = root
        self.model = models.librosModel()
        self.view = views.librosView(root)
        self.view.buttonAdd["command"] = self.addToTreeview
        self.view.buttonUpdate["command"] = self.updateFromTreeview
        self.view.buttonRemove["command"] = self.removeFromTreeview
 
        self.view.treeview.bind('<<TreeviewSelect>>', self.loadTreeviewToEntry)
 
        self.loadToTreeview()
 
    def loadToTreeview(self):
        data = self.model.getAllData()
        self.view.setTreeview(data)
 
    def addToTreeview(self):
        self.addToDB()
        self.loadToTreeview()
 
    def removeFromTreeview(self):
        self.removeFromDB()
        self.loadToTreeview()
 
    def updateFromTreeview(self):
        self.updateDB()
        self.loadToTreeview()
 
    def loadTreeviewToEntry(self, event=None):
        if self.view.treeview.selection():
            id = self.view.getCursorId()
            titulo = self.view.getCursorTitulo()
            autor = self.view.getCursorAutor()
            editorial = self.view.getCursorEditorial()
            anios = self.view.getCursorAnio()
            paginas = self.view.getCursorPaginas()
            isbn = self.view.getCursorIsbn()
 
            self.view.setId(id)
            self.view.setTitulo(titulo)
            self.view.setAutor(autor)
            self.view.setEditorial(editorial)
            self.view.setAnio(anios)
            self.view.setPaginas(paginas)
            self.view.setIsbn(isbn)
 
    def addToDB(self):
        titulo = self.view.getTitulo()
        autor = self.view.getAutor()
        editorial = self.view.getEditorial()
        anios = self.view.getAnio()
        paginas = self.view.getPaginas()
        isbn = self.view.getIsbn()
        self.model.create(titulo, autor, editorial, anios, paginas, isbn)
 
    def updateDB(self):
        id = self.view.getCursorId()
        titulo = self.view.getTitulo()
        autor = self.view.getAutor()
        editorial = self.view.getEditorial()
        anios = self.view.getAnio()
        paginas = self.view.getPaginas()
        isbn = self.view.getIsbn()
        self.model.update(id, titulo, autor, editorial, anios, paginas, isbn)
 
    def removeFromDB(self):
        id = self.view.getCursorId()
        self.model.delete(id)
 

