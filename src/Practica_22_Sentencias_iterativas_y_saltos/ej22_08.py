
def piramide_numeros(numero: int) -> str:
    piramide = ""
    for i in range (1, numero + 1, 2):
        piramide += str(i) + " "
        for n in range(i - 2, -1, -2):
            piramide += str(n) + " "

        if i != numero:
            piramide += "\n"

    return piramide


def main():
    numero = int(input("Introduce un número: "))
    print(piramide_numeros(numero))


if __name__ == "__main__":
    main()