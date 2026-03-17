import tkinter as tk 

root = tk.Tk()

root.geometry("300x300")

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


root.mainloop()