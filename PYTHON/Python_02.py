#entrada de datos 
from calendar import c


categoria = input("categoria(A,B,C o D) = ")
promedio = int(input("ingrese el promedio = "))

#proceso 
#determine la pension
if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400
else:
    print("categoria incorrecta, ingrese (A, B, C o D)")

#determine el descuento
if 0<=promedio<=20:
    if 0<promedio<14:
        print("no tiene descuento")
    elif 14<=promedio<6:
        pension -= pension*0.1
        print("tiene un descuento del 10%")
    elif 16<=promedio<18:
        print("tiene un descuento del 12%")
        pension -= pension*1.2
    elif 18<=promedio<=20:
        print("tiene un descuento del 15%")
        pension -= pension*1.5
else:
    print("promedio incorrecto")

#costo de la pension
print("el costo de la pension es: ", pension)