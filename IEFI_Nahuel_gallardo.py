import tkinter as tk
from tkinter import StringVar, ttk
import tkinter
from turtle import title
from ttkbootstrap import Style
from centrar_ventana import centrar

#Funciones

def clean():
    entry1.delete(0, tk.END)

    entry2.delete(0, tk.END)

    entry3.config(state='normal')
    entry3.delete(0, tk.END)
    entry3.config(state='disabled')

    entry1.focus()

    return

def sumar():
    numero=int(entry1.get()) + int(entry2.get())
    resultado.set(numero)

def restar():
    numero=int(entry1.get()) - int(entry2.get())
    resultado.set(numero)

def multiplicar():
    numero=int(entry1.get()) * int(entry2.get())
    resultado.set(numero)

def dividir():
    numero=int(entry1.get()) / int(entry2.get())
    resultado.set(numero)

def porcentaje():
    numero=int(entry1.get()) / int(entry2.get()) *100
    resultado.set(numero)

#Frame

nahuelg= tkinter.Tk()
nahuelg.geometry(centrar(ancho=360, alto=250, app=nahuelg))
nahuelg.title('IEFI_2_NG')

frame = ttk.Frame(nahuelg, padding='10 10 10 10', height=70, width=30, borderwidth=2, relief='sunken')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.pack()

Style = Style('darkly')

#etiquetas y cajas

resultado= StringVar()

label1 = tk.Label(frame, text='Valor 1:', width=15)
label1.grid(row=0, column=0,  padx=5, pady=5)

label1 = tk.Label(frame, text='Valor 2:', width=15)
label1.grid(row=1, column=0,  padx=5, pady=5)

label1 = tk.Label(frame, text='Resultado', width=15)
label1.grid(row=2, column=0,  padx=5, pady=5)

entry1 = tk.Entry(frame, validate = "key", width = 15,)
entry1.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

entry2 = tk.Entry(frame, validate = "key", width = 15,)
entry2.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

entry3 = tk.Entry(frame, width=15, state='disabled', textvariable=resultado,)
entry3.grid(row=2, column=1, padx=5, pady=5 )

#Botones

boton1 = tk.Button(frame, text='+', width=15, command=sumar)
boton1.grid(row= 3, column=0, sticky='nsew', padx=5, pady=5)

boton2 = tk.Button(frame, text='-', width=15, command=restar)
boton2.grid(row= 3, column=1, sticky='nsew', padx=5, pady=5)

boton3 = tk.Button(frame, text='*', width=15, command=multiplicar)
boton3.grid(row= 4, column=0, sticky='nsew', padx=5, pady=5)

boton4 = tk.Button(frame, text='/', width=15, command=dividir)
boton4.grid(row= 4, column=1, sticky='nsew', padx=5, pady=5)

boton5 = tk.Button(frame, text='%', width=15, command=porcentaje)
boton5.grid(row= 5, column=0, sticky='nsew', padx=5, pady=5)

boton6 = tk.Button(frame, text='LIMPIAR', width=15, command= clean)
boton6.grid(row= 5, column=1, sticky='nsew', padx=5, pady=5)


nahuelg.mainloop()










