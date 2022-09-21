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