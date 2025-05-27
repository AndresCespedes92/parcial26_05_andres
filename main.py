from datos import matriz_items
from menu import menu, opcion_valida
from validaciones import cantidad_items
from carga import cargar_items
from operaciones import (
    buscar_por_historia_clinica,
    ordenar_por_numero_historia_clinica,
    mostrar_paciente_mas_dias,
    mostrar_paciente_menos_dias,
    mostrar_mayores_a_5,
    mostrar_pacientes,
    promedio_internacion
)

def main():
    """
    Función principal que ejecuta el menú interactivo del sistema.
    """
    opcion = 0
    while opcion != 9:
        menu()
        opcion = opcion_valida()

        if opcion == 1:
            cantidad = cantidad_items()
            cargar_items(matriz_items, cantidad)
        elif opcion == 2:
            mostrar_pacientes(matriz_items)        
        elif opcion == 3:
            buscar_por_historia_clinica(matriz_items)
        elif opcion == 4:
            ordenar_por_numero_historia_clinica(matriz_items)
            mostrar_pacientes(matriz_items)
        elif opcion == 5:
            mostrar_paciente_mas_dias(matriz_items)
        elif opcion == 6:
            mostrar_paciente_menos_dias(matriz_items)
        elif opcion == 7:
            mostrar_mayores_a_5(matriz_items)
        elif opcion == 8:
            promedio_internacion(matriz_items)
        elif opcion == 9:
            print("Saliste del programa.")
            break
main()
