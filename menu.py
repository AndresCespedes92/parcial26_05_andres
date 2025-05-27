

def menu():
    """
    Mostrar el menú principal de opciones al usuario.
    """
    print("""
    Sistema de Gestion de Clinica -"La Fuerza"- 
    
    -Elije una opción por favor:
          
    1. Cargar pacientes
    2. Mostrar todos los pacientes
    3. Buscar pacientes por numero de Historia Clinica
    4. Ordenar pacientes por numero de Historia Clinica
    5. Mostrar pacientes con mas dias de internacion
    6. Mostrar pacientes con menos dias de internacion
    7. Cantidad de pacientes con mas de 5 dias de internacion
    8. Promedio de dias de internacion de todos los pacientes
    9. Salir
    """)

def opcion_valida()-> int:
    """
    Valida que la opción ingresada sea un número entre 1 y 9.

    Returns:
        int: Opcion válida seleccionada por el usuario.
    """
    opcion = input("Ingrese opción (1-9): ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 9:
        print("Opción inválida. Ingrese un número del 1 al 9.")
        opcion = input("Ingrese opción (1-9): ")
    return int(opcion)