#tamaño_maximo = 100
#matriz_items = [[None]] * 100

def cargar_items(matriz: list, cantidad: int) -> None:
    """
    Carga productos en la matriz.

    Args:
        matriz (list): Lista de pacientes.
        cantidad (int): Cantidad de pacientes a cargar.
    """
    for i in range(len(matriz)):
        if matriz[i] == [None]:
            posicion_libre = i
            break

    for j in range(cantidad):
        numero_historia_clinica = validar_numero_historia_clinica()
        nombre_paciente = validacion_nombre()
        edad = validar_edad()
        diagnostico = validacion_diagnostico()
        cantidades = validar_dias_internacion()
        matriz[posicion_libre + j] = [numero_historia_clinica, nombre_paciente, edad, diagnostico, cantidades]
    print("Cargó correctamente el paciente")


def menu():
    """
    Muestra el menú principal de opciones al usuario.
    """
    print("""
    Sistema de Gestion de Clinica "La Fuerza"
    Elije una opción:
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
                if matriz[j][1] > matriz[j + 1][1]:
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
    Solicita un nombre de producto sin números.

    Returns:
        str: Nombre válido del producto.
    """
    producto = input("Ingrese nombre de productos (sin numeros): ")
    while producto.isdigit() == True or len(producto) == 0:
        #or len(producto) < 5: por si necesito en alguna otra condicion - por ejemplo largo de un codigo y lo incluyo en el print tambien
        print("Producto inválido..")
        producto = input("Ingrese ingrese nombre de producto sin numeros: ")
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
        item = input("Vuelve a ingresar: ")
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
        diagnostico = input("Vuelve a ingresar: ")
    return diagnostico



#LISTAS

def agregar(lista: list[any], elemento: any) -> list[any]:
    """Crea una nueva lista que contiene los elementos de la lista original y añade el nuevo elemento al final.

    Args:
        lista (List[Any]): Lista original a la que se desea agregar el elemento.
        elemento (Any): Elemento que se desea agregar al final de la lista.
    Returns:
        list[Any]: Una nueva lista con el elemento añadido al final.

    """
    controlador_de_lista(lista)
    lista_nueva = lista + [elemento]
    return lista_nueva


def controlador_de_lista (lista : any) -> bool:
    """
    Verifica si el parámetro ingresado es una lista.

    Args:
        lista (any): Objeto a evaluar.

    Returns:
        bool: Retorna True si el objeto es una lista, de lo contrario retorna False.
    """
    if type(lista) == list:
        return True
    else:
        return False


def eliminar_primer_instancia(lista: list[any], elemento: any) -> str:
    """
    Elimina la primera aparición de un elemento en la lista y devuelve
    un mensaje con la lista original, la modificada y el elemento eliminado.

    Args:
        lista (list[any]): Lista original.
        elemento (any): Elemento a eliminar.

    Returns:
        str: Descripción del resultado de la operación.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            eliminado = lista[i]
            nueva_lista = lista[:i] + lista[i+1:]
            return f"La lista original {lista} queda {nueva_lista}. Se elimino {eliminado}"
    return None


def eliminar_todos(lista: list[any], elemento: any) -> str | None:
    """
    Elimina todas las apariciones de un elemento en la lista original
    y devuelve un mensaje describiendo la operación. Si el elemento no está presente,
    retorna None.

    Args:
        lista (list[Any]): Lista original.
        elemento (Any): Elemento a eliminar.

    Returns:
        str | None: Mensaje describiendo el resultado, o None si no se encontró el elemento.
    """
    
    # Verificamos si el elemento está en la lista
    if elemento not in lista:
        return None
    
    nueva_lista = []

    for i in lista:
        if i != elemento:
            nueva_lista = nueva_lista + [i]
            lista[:] = nueva_lista

    return f"La lista queda {lista}. Se eliminaron todas las instancias de {elemento}"



def eliminar(lista: list[any]) -> str:
    """
    Elimina el último elemento de la lista y devuelve un mensaje con el estado original,
    el nuevo estado de la lista y el elemento eliminado.

    Args:
        lista (list[Any]): Lista original de la que se eliminará el último elemento.

    Returns:
        str: Mensaje que describe la lista original, la lista resultante y el elemento eliminado.
    """
    eliminado = lista[-1]
    nueva_lista = lista[:-1]
    lista[:] = nueva_lista

    return f"La lista queda {lista}. Se elimino {eliminado}"


def insertar(lista: list[any], elemento: any, indice: int) -> list[any]:
    """
    Crea una nueva lista que contiene los elementos de la lista original y añade el nuevo elemento en la posición indicada.
    Si la posición es mayor que la longitud de la lista, el elemento se añade al final.
    Si la posición ya está ocupada, se reemplaza el valor existente.

    Args:
        lista (list[any]): Lista original sobre la que se quiere insertar o reemplazar un elemento.
        elemento (any): Elemento que se desea insertar.
        indice (int): Posición (1-based) en la que se desea insertar o reemplazar el elemento.

    Returns:
        list[any]: Una nueva lista con el elemento añadido o reemplazado según corresponda.
    """
    indice = int(input("ingrese la posicion: "))
    indice = indice - 1
    if indice > len(lista):
        lista_nueva = lista + [elemento]
    
    else:
        lista[indice] = elemento
        lista_nueva = lista
    
    return lista_nueva


def obtener_indice(lista: list[any], elemento: any) -> int:
    """
    Busca un elemento en la lista y devuelve su posición si se encuentra o sino -1.

    Args:
        lista (list[any]): Lista en la que se busca el elemento.
        elemento (any): Elemento cuyo índice se desea encontrar.

    Returns:
        int: La posición del elemento en la lista (comenzando en 1).
             Devuelve -1 si el elemento no se encuentra.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return f"Su posicion es {i + 1}"
    return -1


def vaciar_lista(lista: list[any]) -> None:
    """
    Elimina todos los elementos de la lista, dejándola vacía.

    Args:
        lista (list[Any]): Lista original a vaciar.

    Returns:
        None
    """
    controlador_de_lista(lista)
    lista[:] = []