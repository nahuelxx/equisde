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
