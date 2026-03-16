print("Bienvenido al registro de ventas!\n")

all_data = []
end = "no"

def sales_log():
    name=input("Ingrese nombre del producto: ")
    price=float(input("Ingrese el precio del producto: "))
    while price <= 0:
        price=float(input("El valor debe ser superior a 0.\nIngrese cantidad nuevamente "))
    amount=int(input("Ingrese cantidad: "))
    while amount <= 0:
        amount=int(input("Debe de ingresar un minimo de '1' producto.\nIngrese la cantidad nuevamente: "))
    total=(price*amount)
    print(f"Subtotal:{total}")
    s_log={
        "producto": name,
        "Precio": price,
        "cantidad":amount,
        "total":total
    }
    all_data.append(s_log)

def total_s():
    f_total= sum(i["total"] for i in all_data) 
    print(f"El total de las ventas es: {f_total}")
    


while end != "si":
    sales_log()
    end=input("Desea finalizar de digitar?: ")
total_s()

#try:
#except:
#print("Error: se ingreso un valor invalido intenten nuevamente.")

