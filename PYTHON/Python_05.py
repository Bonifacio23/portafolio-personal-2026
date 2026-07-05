
#entrada de datos
cantidad_total = int(input("Ingrese la cantidad total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
porcentaje = (preguntas_correctas / cantidad_total) * 100

#proceso de datos<
if porcentaje<50:
    nivel = "Fuera de nivel"
    print(f"Estas fuera de nivel y su porcentaje de preguntas correctas es de {porcentaje:2f}%")
elif 50<=porcentaje<76:
    nivel = "Nivel regular"
    print(f"Su porcentaje de preguntas correctas es de {porcentaje:2f}%")
elif 76<=porcentaje<90:
    nivel = "Nivel medio"
    print(f"Su porcentaje de preguntas correctas es de {porcentaje:.2f}%")
elif porcentaje>=90:
    nivel = "Nivel maximo"
    print(f"Su porcentaje de preguntas correctas es de {porcentaje:.2f}%")
else:
    print("Datos invalidos, ingrese los datos nuevamente")

#salida de datos

print("Usted esta: ",nivel)


