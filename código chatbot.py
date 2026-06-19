import csv


def cargar_empleados():
    empleados = []

    try:
        with open("empleados.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                fila["dias_disponibles"] = int(fila["dias_disponibles"])
                empleados.append(fila)

    except FileNotFoundError:
        print("No se encontró el archivo empleados.csv")

    return empleados


def guardar_empleados(empleados):
    with open("empleados.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["dni", "nombre", "dias_disponibles"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(empleados)


def buscar_empleado(empleados, dni):
    for empleado in empleados:
        if empleado["dni"] == dni:
            return empleado

    return None


def solicitar_vacaciones():
    empleados = cargar_empleados()

    dni = input("Ingrese su DNI: ")

    empleado = buscar_empleado(empleados, dni)

    if empleado is None:
        print("Empleado no encontrado.")
        return

    print(f"Bienvenido/a {empleado['nombre']}")
    print(f"Días disponibles: {empleado['dias_disponibles']}")

    while True:
        try:
            dias = int(input("¿Cuántos días desea solicitar? "))

            if dias <= 0:
                print("Ingrese una cantidad válida.")
                continue

            break

        except ValueError:
            print("Debe ingresar un número.")

    if dias > empleado["dias_disponibles"]:
        print("Solicitud rechazada por falta de días disponibles.")
    else:
        empleado["dias_disponibles"] -= dias
        guardar_empleados(empleados)

        print("Solicitud aprobada.")
        print(f"Días restantes: {empleado['dias_disponibles']}")


solicitar_vacaciones()