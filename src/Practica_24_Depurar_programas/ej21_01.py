
def algoritmo_burbuja(lista_numeros: list):
    """Ordena una lista de números usando el algoritmo de burbuja.

    Este algoritmo de burbuja realiza iteraciones a través de la lista y
    compara cada elemento con los anteriores. Si encuentra un número
    menor en una posición posterior, intercambia los elementos. Repite
    este proceso hasta que la lista esté ordenada.

    Args:
        lista_numeros (list): Una lista de números a ordenar.

    Returns:
        None: La función modifica la lista original y no devuelve nada.
    """
    for i in range(0, len(lista_numeros)):
            for j in range(0, i):
                if lista_numeros[i] < lista_numeros[j]:
                    lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]
    
    print("Lista ordenada: ", lista_numeros)


def main():
    """Función principal para ejecutar el algoritmo de burbuja.

    Define una lista de números y la pasa a la función `algoritmo_burbuja`
    para ordenar la lista e imprimir el resultado.
    """
    lista_numeros = [8, 3, 1, 19, 14, 50, 2]
    algoritmo_burbuja(lista_numeros)


if __name__ == "__main__":
    main()