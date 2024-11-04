
def comprobar_entrada(edad: str) -> int:
    error = True
    while error:
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
            error = False
        except ValueError:
            print(f"*ERROR* Valor inválido")
            edad = input("Introduce tu edad: ")

    return edad


def precio_entrada(edad: int) -> int:
    if edad < 4:
        return 0
    elif edad >= 4 and edad < 18:
        return 5
    else:
        return 10


def main():
    edad = input("Introduce tu edad: ")

    edad = comprobar_entrada(edad)
    print(f"El precio de la entrada es de {precio_entrada(edad)}€")


if __name__ == "__main__":
    main()