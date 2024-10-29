
def es_primo(numero: int) -> str:
    if numero == 2:
        return "es primo"
    elif numero % 2 != 0:
        return "es primo"
    else:
        return "no es primo"


def main():
    numero = int(input("Introduce un número: "))
    print(f"El número {numero} {es_primo(numero)}")


if __name__ == "__main__":
    main()