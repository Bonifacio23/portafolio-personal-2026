
#entrada de datos
from math import e


opcion = 0

while opcion != 5:
    print("\n----MENU----")
    print("1.Contrato A")
    print("2.Contrato B")
    print("3.Contrato C")
    print("4.Contrato D")
    print("5.Salir")
    salario_actual = float(input("Ingrese el salario actual: "))
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
        if opcion == 1:
            salario_nuevo = salario_actual + (salario_actual * 0.07)
            print("tiene un aumento del 7% sobre su salario actual")
            print(f"El nuevo salario es: {salario_nuevo:.2f}")
        elif opcion == 2:
            salario_nuevo = salario_actual + (salario_actual * 0.09)
            print("tiene un aumento del 9% sobre su salario actual")
            print(f"El nuevo salario es: {salario_nuevo:.2f}")
        elif opcion == 3:
            salario_nuevo = salario_actual + (salario_actual * 0.11)
            print("tiene un aumento del 11% sobre su salario actual")
            print(f"El nuevo salario es: {salario_nuevo:.2f}")
        elif opcion == 4:

            print(f"No tiene aumento, su salario es: ", salario_actual)
        elif opcion == 5:
            print("Saliendo del programa...")
    else:
        print("Opcion incorrecta, ingrese una opcion del menu")
        
