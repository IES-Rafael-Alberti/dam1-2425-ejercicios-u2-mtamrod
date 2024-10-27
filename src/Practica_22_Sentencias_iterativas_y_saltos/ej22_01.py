
def mostrar_pantalla(palabra: str):
    for i in range (0, 10):
        print(palabra)


def main():
    palabra = input("Introduce una palabra: ")

    mostrar_pantalla(palabra)


if __name__ == "__main__":
    main()