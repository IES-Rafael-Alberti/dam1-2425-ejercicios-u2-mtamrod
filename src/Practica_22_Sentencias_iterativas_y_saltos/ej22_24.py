
def es_primo():
    cont_primos = 0
    numero = entrada_numero()
    while numero != 0:
        if numero == 2:
            cont_primos += 1
        elif numero % 2 != 0:
            cont_primos += 1
        numero = entrada_numero()

    return cont_primos


def entrada_numero():
    salir = False
    while not salir:
        numero = int(input("Introduce un número: "))
        if numero > 1 or numero == 0:
            salir = True
        else:
            print("Número incorrecto")

    return numero


def main():
    print(f"En el total de número introducidos hay {es_primo()} primos")


if __name__ == "__main__":
    main()