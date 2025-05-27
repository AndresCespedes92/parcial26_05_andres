from validaciones import validar_numero_historia_clinica


def buscar_por_historia_clinica(matriz: list) -> None | str:
    """
    Busca un producto por historia clinica en la matriz.

    Args:
        matriz (list): Lista de pacientes.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return

    numero_historia_clinica = validar_numero_historia_clinica()

    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][0] == numero_historia_clinica:
            print(f"Paciente encontrado: {matriz[i]}")
            return  # Salimos inmediatamente al encontrarlo

    # Si termina el bucle y no hizo return, es porque no lo encontró
    print("Paciente no encontrado.")



def ordenar_por_numero_historia_clinica(matriz: list) -> None | list:
    """
    Ordena la matriz por numero de historia clinica de menor a mayor.

    Args:
        matriz (list): Lista de pacientes.

    Returns:
        list: Vacio o Matriz ordenada.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return
    
    cantidad = 0
    for i in range(len(matriz)):
        if matriz[i] != [None]:
            cantidad = cantidad + 1
    
    for i in range(cantidad):
        if matriz[i] != [None]:
            for j in range(cantidad - i - 1):
                if matriz[j][0] > matriz[j + 1][0]:
                    aux = matriz[j]
                    matriz[j] = matriz[j + 1]
                    matriz[j + 1] = aux

    print("Pacientes ordenados por numero de historia clinica")
    return matriz



def mostrar_paciente_mas_dias(matriz: list) -> None:
    """
    Muestra el paciente con mas dias de la matriz.
    
    Args:
        matriz (list): Lista de pacientes.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return

    max_dias = 0
    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] > max_dias:
            max_dias = matriz[i][4]

    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] == max_dias:
            print(f"Paciente con mas dias de internacion: {matriz[i]}")




def mostrar_paciente_menos_dias(matriz: list) -> None :
    """
    Muestra el paciente con menos dias de internacion de la matriz.
    
    Args:
        matriz (list): Lista de pacientes.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return

    menos_dias_de_internacion = 999999999
    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] < menos_dias_de_internacion:
            menos_dias_de_internacion = matriz[i][4]

    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] == menos_dias_de_internacion:
            print(f"Paciente con menos dias de internacion: {matriz[i]}")




def mostrar_mayores_a_5(matriz: list) -> None:
    """
    Muestra pacientes cuya internacion es mayor a 5 dias.
    
    Args:
        matriz (list): Lista de pacientes y cantidad.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return

    hay_items = False
    contador = 0

    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] > 5:
            contador = contador + 1
            print(f"Pacientes con internacion mayor a 5 dias: {matriz[i]}")
            
            hay_items = True
    if hay_items == True:
        print(f"La cantidad de pacientes con dias de internacion mayor a 5 dias es {contador}")

    if hay_items == False:
        print("No hay pacientes con internacion mayor a 5 dias.")



def mostrar_pacientes(matriz: list) -> None:
    """
    Muestra todos los ppacientes cargados en la matriz.
    
    Args:
        matriz (list): Lista de pacientes.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return
    else:
        print(
"""
Pacientes:
N* Historia Clinica - Nombre - Edad - Diagnostico - Cant Dias de Internacion""")
        for i in range(len(matriz)):
            if matriz[i] != [None]: #solo las filas cargadas quiero ver
                for j in range(len(matriz[i])):
                    print(matriz[i][j], end=" ")
                print() #salta cada vez que se completa la fila



def promedio_internacion(matriz: list) -> int:
    """
    Muestra promedio de internacion de los pacientes.
    
    Args:
        matriz (list): Lista de pacientes.
    """
    if matriz[0] == [None]:
        print("""
        ------No hay pacientes cargados aún--------
              """)
        return
    
    hay_items = False
    contador = 0
    acumulador_dias_internacion = 0

    for i in range(len(matriz)):
        if matriz[i] != [None] and matriz[i][4] > 0:
            for j in range(len(matriz[i])):
                acumulador_dias_internacion = matriz[i][4] + acumulador_dias_internacion
                contador = contador + 1
                hay_items = True
    
    if hay_items == True:
        print(f"El promedio de internacion de dias de internacion de los pacientes registrados es {acumulador_dias_internacion/contador}")