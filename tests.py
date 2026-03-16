import tkinter as tkinter
from tkinter import simpledialog
from tkinter import messagebox

name=simpledialog.askstring("Producto","Ingrese nombre del producto: ")
price=simpledialog.askfloat("Precio","Ingrese el valor del producto: ")
amount=simpledialog.askinteger("Cantidad","Ingrese la cantidad")
total=(price*amount)
print(name)
messagebox.showinfo("Cantidad", f"El total es: {total}")