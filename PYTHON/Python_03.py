#entrada de datos

print("\n----MENU----")
print("1.Cuadrado")
print("2.Rectangulo")
print("3.Circulo")

opcion = int(input("Ingrese una opcion: "))

#proceso de datos
if opcion == 1 or opcion == 2 or opcion == 3:

    if opcion == 1:  # cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))

        if lado > 0:
            area = lado * lado
            print(f"El area del cuadrado es: {area:.2f}")
        else:
            print("Medida incorrecta, ingrese un valor mayor a 0")


    elif opcion == 2:  # rectangulo
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))

        if base > 0 and altura > 0:
            area = base * altura
            print(f"El area del rectangulo es: {area:.2f}")
        else:
            print("Medidas incorrectas, ingrese valores mayores a 0")


    elif opcion == 3:  # circulo
        radio = float(input("Ingrese el radio del circulo: "))

        if radio > 0:
            area = 3.14 * radio * radio
            print(f"El area del circulo es: {area:.2f}")
        else:
            print("Medida incorrecta, ingrese un valor mayor a 0")

else:
    print("Opcion incorrecta, ingrese una opcion del menu")
    

