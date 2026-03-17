import tkinter as tkinter
from tkinter import simpledialog
from tkinter import messagebox

#name=simpledialog.askstring("Producto","Ingrese nombre del producto: ")
#price=simpledialog.askfloat("Precio","Ingrese el valor del producto: ")
#amount=simpledialog.askinteger("Cantidad","Ingrese la cantidad")
#total=(price*amount)
#print(name)
#messagebox.showinfo("Cantidad", f"El total es: {total}")

all_data = []

name=simpledialog.askstring("producto","Ingrese nombre del producto: ")
price=simpledialog.askfloat("precio","Ingrese el precio del producto: ")
while price <= 0:
    price=simpledialog.askfloat("precio","El valor debe ser superior a 0.\nIngrese cantidad nuevamente ")
amount=simpledialog.askinteger("cantidad","Ingrese cantidad: ")
while amount <= 0:
    amount=simpledialog.askinteger("cantidad,""Debe de ingresar un minimo de '1' producto.\nIngrese la cantidad nuevamente: ")
total=(price*amount)
messagebox.showinfo("subtotal",f"Subtotal:{total}")
s_log={
    "name": name,
    "price": price,
    "amount":amount,
    "total":total
}
all_data.append(s_log)
reporte=""
for i in all_data:
        reporte += (f"producto: {i['name']}\n\nvalor unitario: {i['price']}\ncantidad: {i['amount']}\n\ntotal: {i['total']}.\n\n")
print(reporte)