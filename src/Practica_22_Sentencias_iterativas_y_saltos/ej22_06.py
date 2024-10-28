
def constructor_piramide(numero: int) -> str:
    piramide = ""

    for i in range (1, numero + 1):
        piramide += "*" * i

        if i != numero:
            piramide += "\n"

    return piramide


def main():
    numero = int(input("Introduce un numero entero: "))
    print(constructor_piramide(numero))


if __name__ == "__main__":
    main()