
def numero_mayor(numero: int, mayor: int) -> int:
    salir = False
    while not salir:
        if numero > mayor:
            mayor = numero
        elif numero == 0:
            salir = True
        numero = int(input("Introduce un número: "))

    return mayor


def main():
    numero = int(input("Introduce un número: "))
    mayor = 0
    print(numero_mayor(numero, mayor))

if __name__ == "__main__":
    main()