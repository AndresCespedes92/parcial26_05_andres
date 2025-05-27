def cantidad_items() -> int:
    """
    Solicita al usuario cuántos pacientes desea cargar (1 a 10).

    Returns:
        int: Cantidad de pacientes.
    """
    cantidad = input("¿Cuántos pacientes desea cargar? (máximo 10): ")
    while not cantidad.isdigit() or int(cantidad) < 1 or int(cantidad) > 10:
        print("Cantidad inválida. Debe ser entre 1 y 10.")
        cantidad = input("¿Cuántos pacientes desea cargar? (máximo 10): ")
    return int(cantidad)

def validacion_item() -> str:
    """
    Solicita un atributo.

    Returns:
        str: Nombre válido del atributo.
    """
    producto = input("Ingrese nombre del atributo: ")
    while producto.isdigit() == True or len(producto) == 0:
        #or len(producto) < 5: por si necesito en alguna otra condicion - por ejemplo largo de un codigo y lo incluyo en el print tambien
        print("Atributo inválido..")
        producto = input("Ingrese atributo sin numeros: ")
    return producto


def validar_numero_historia_clinica()-> int:
    """
    Solicita numero de historia clinica.

    Returns:
        int: Numero de historia clinica.
    """
    numero_historia_clinica = input("Ingrese numero de historia clinica: ")
    while not numero_historia_clinica.isdigit() == True or numero_historia_clinica == 0 or len(numero_historia_clinica) == 0:
        print("Haga una entrada válida")
        numero_historia_clinica = input("Ingresa nuevamente numero de historia clinica: ")
    numero_historia_clinica = int(numero_historia_clinica)
    return numero_historia_clinica

def validar_edad()-> int:
    """
    Solicita la edad del paciente.

    Returns:
        int: Edad del paciente.
    """
    edad = input("Ingrese edad del paciente: ")
    while not edad.isdigit() == True or edad == 0 or len(edad) == 0:
        print("Haga una entrada válida")
        edad = input("Ingresa nuevamente la edad del paciente: ")
    edad = int(edad)
    return edad


def validar_dias_internacion() -> int:
    """
    Solicita dias de internacion.

    Returns:
        int: Dias de internacion.
    """
    dias = input("Ingrese dias de internacion del paciente: ")
    while not dias.isdigit() == True or dias == 0 or len(dias) == 0:
        print("Haga una entrada válida")
        dias = input("Ingresa nuevamente dias de internacion del paciente: ")
    dias = int(dias)
    return dias



def validacion_nombre() -> str:
    """
    Solicita un nombre de paciente sin números.

    Returns:
        str: Nombre de paciente.
    """
    nombre = input("Ingrese nombre de paciente (sin numeros): ")
    while nombre.isdigit() == True:
        #or len(producto) < 5: por si necesito en alguna otra condicion - por ejemplo largo de un codigo y lo incluyo en el print tambien
        print("Nombre inválido..")
        nombre = input("Vuelve a ingresar sin numeros: ")
    return nombre


def validacion_diagnostico() -> str:
    """
    Solicita un diagnostico sin números.

    Returns:
        str: Diagnostico.
    """
    diagnostico = input("Ingrese diagnostico del paciente (sin numeros): ")
    while diagnostico.isdigit() == True:
        #or len(producto) < 5: por si necesito en alguna otra condicion - por ejemplo largo de un codigo y lo incluyo en el print tambien
        print("Diagnostico inválido..")
        diagnostico = input("Vuelve a ingresar sin numeros: ")
    return diagnostico

