import tkinter as tkinter
from tkinter import simpledialog

name=simpledialog.askstring("Producto","Ingrese nombre del producto: ")
price=simpledialog.askfloat("Precio","Ingrese el valor del producto: ")
amount=simpledialog.askinteger("Cantidad","Ingrese la cantidad")
total=(price*amount)
print(name)
print(total)