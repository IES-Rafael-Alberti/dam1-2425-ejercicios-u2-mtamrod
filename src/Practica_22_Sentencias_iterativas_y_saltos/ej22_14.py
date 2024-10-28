
def repetir_numero():
    salir = False
    suma = 0
    while not salir:
        numero = int(input("Introduce un numero: "))
        if numero == 0:
            salir = True
        else:
            suma += numero

    return suma


def main():
    print(repetir_numero())


if __name__ == "__main__":
    main()