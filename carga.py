from validaciones import validar_dias_internacion,validacion_diagnostico,validacion_nombre,validar_edad,validar_numero_historia_clinica



def cargar_items(matriz: list, cantidad: int) -> None:
    """
    Carga la matriz.

    Args:
        matriz (list): Lista de pacientes con sus atributos.
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
        print("----- Cargó correctamente el paciente ------- ")