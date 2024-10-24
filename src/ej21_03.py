
def comprobar_numero() -> float:
    numero_correcto = False
    while not numero_correcto:
        numero_1 = input("Introduce un número: ")
        numero_2 = input("Introduce un segundo número: ")
        try:
            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            if numero_2 == 0:
                print("*ERROR* El divisor no puede ser 0")
            else:
                numero_correcto = True
        except ValueError:
            print("*ERROR* No es un número")

    return numero_1, numero_2


def divisor_numeros(numero_1: float, numero_2:float) -> float:
    solucion = numero_1/numero_2
    return solucion


def main():
    numero_1, numero_2 = comprobar_numero()
    solucion = divisor_numeros(numero_1, numero_2)

    print(f"{solucion}")


if __name__ == "__main__":
    main()