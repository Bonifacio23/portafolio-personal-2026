#Python PROGRAMA DE ASISTENCIA ALUMNO/PROFESOR
from datetime import datetime

estudiantes = []
profesores = []
opcion = 0


def registrar_estudiante():
    nombre = input("Ingrese nombre del estudiante: ")

    codigo = input("Ingrese codigo del estudiante: ")

    while not (codigo.isdigit() and len(codigo) == 8):
        print("El código debe tener exactamente 8 números.")
        codigo = input("Ingrese codigo del estudiante: ")

    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            print("Ese código ya está registrado.")
            return

    for profesor in profesores:
        if profesor["codigo"] == codigo:
            print("Ese código ya está registrado.")
            return

    estudiante = {
        "nombre": nombre,
        "codigo": codigo,
        "asistencia": "Sin registrar",
        "hora": "--:--:--"
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado")


def registrar_profesor():
    nombre = input("Ingrese nombre del profesor: ")

    codigo = input("Ingrese codigo del profesor: ")

    while not (codigo.isdigit() and len(codigo) == 8):
        print("El código debe tener exactamente 8 números.")
        codigo = input("Ingrese codigo del profesor: ")

    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            print("Ese código ya está registrado.")
            return

    for profesor in profesores:
        if profesor["codigo"] == codigo:
            print("Ese código ya está registrado.")
            return

    profesor = {
        "nombre": nombre,
        "codigo": codigo,
        "asistencia": "Sin registrar",
        "hora": "--:--:--"
    }

    profesores.append(profesor)
    print("Profesor registrado")


def asistencia_estudiante():
    buscar = input("Ingrese codigo del estudiante: ")

    for estudiante in estudiantes:

        if estudiante["codigo"] == buscar:

            print("\n1. Presente")
            print("2. Tardanza")
            print("3. Falta")

            estado = input("Seleccione estado: ")

            if estado == "1":
                estudiante["asistencia"] = "Presente"
            elif estado == "2":
                estudiante["asistencia"] = "Tardanza"
            elif estado == "3":
                estudiante["asistencia"] = "Falta"
            else:
                print("Opción inválida")
                return

            estudiante["hora"] = datetime.now().strftime("%H:%M:%S")

            print("Asistencia registrada")
            return

    print("Estudiante no encontrado")


def asistencia_profesor():
    buscar = input("Ingrese codigo del profesor: ")

    for profesor in profesores:

        if profesor["codigo"] == buscar:

            print("\n1. Presente")
            print("2. Tardanza")
            print("3. Falta")

            estado = input("Seleccione estado: ")

            if estado == "1":
                profesor["asistencia"] = "Presente"
            elif estado == "2":
                profesor["asistencia"] = "Tardanza"
            elif estado == "3":
                profesor["asistencia"] = "Falta"
            else:
                print("Opción inválida")
                return

            profesor["hora"] = datetime.now().strftime("%H:%M:%S")

            print("Asistencia registrada")
            return

    print("Profesor no encontrado")


def ver_asistencias():

    print("\n--- ASISTENCIA ESTUDIANTES ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:
        for estudiante in estudiantes:
            print(
                estudiante["nombre"],
                "-",
                estudiante["codigo"],
                "-",
                estudiante["asistencia"],
                "-",
                estudiante["hora"]
            )

    print("\n--- ASISTENCIA PROFESORES ---")

    if len(profesores) == 0:
        print("No hay profesores")
    else:
        for profesor in profesores:
            print(
                profesor["nombre"],
                "-",
                profesor["codigo"],
                "-",
                profesor["asistencia"],
                "-",
                profesor["hora"]
            )


while opcion != 6:

    print("\n===== SISTEMA DE ASISTENCIA =====")
    print("1. Registrar estudiante")
    print("2. Registrar profesor")
    print("3. Marcar asistencia estudiante")
    print("4. Marcar asistencia profesor")
    print("5. Ver asistencias")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_estudiante()

        elif opcion == 2:
            registrar_profesor()

        elif opcion == 3:
            asistencia_estudiante()

        elif opcion == 4:
            asistencia_profesor()

        elif opcion == 5:
            ver_asistencias()

        elif opcion == 6:
            print("Saliendo del sistema...")

        else:
            print("Opción inválida")

    except ValueError:
        print("Debe ingresar un número.")