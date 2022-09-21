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