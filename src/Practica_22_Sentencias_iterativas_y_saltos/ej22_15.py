
def repetir_numero():
    salir = False
    suma = 0
    while not salir:
        numero = int(input("Introduce un numero: "))
        if numero > 0:
            suma += numero
        elif numero == 0:
            salir = True

    return suma


def main():
    print(repetir_numero())


if __name__ == "__main__":
    main()