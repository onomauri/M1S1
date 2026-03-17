import tkinter as tkinter
from tkinter import simpledialog
from tkinter import messagebox


print("Bienvenido al registro de ventas!\n")


all_data = []
end = "no"


def sales_log():
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

def summary():
    global reporte
    for i in all_data:
        reporte += (f"--------------------\n\nproducto: {i['name']}\n\nvalor unitario: {i['price']}\ncantidad: {i['amount']}\n\ntotal: {i['total']}.\n\n--------------------\n")


def total_s():
    f_total= sum(i["total"] for i in all_data)
    #print(f"El total recaudado en las ventas es: {f_total}")
    return f_total
try:
    while end != "si":
        sales_log()
        end=input("Desea finalizar de digitar?: ")
    summary()
    total_s()
    f_total=total_s()
    messagebox.showinfo("Resumen de ventas", reporte + f"El total recaudado en las ventas es: {f_total}")
    print("Gracias por usar el sistema de registro!")
except:
    print("Error: se ingreso un valor invalido intenten nuevamente.")
