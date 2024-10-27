
def comprobar_edad(edad: str) -> int:
    error = True
    while error:
        try:
            edad = int(edad)
            if edad < 0 or edad > 125:
                raise ValueError
            error = False
        except ValueError:
            print("*ERROR* Edad inválida")
            edad = input("Introduce tu edad: ")

    return edad


def años_cumplidos(edad: int) -> str:
    años_cumplidos = ""

    for i in range (0, edad + 1):
        años_cumplidos += str(i) + ", "

    return años_cumplidos.rstrip(", ")


def main():
    edad = input("Introduce tu edad: ")
    edad = comprobar_edad(edad)
    print(f"Los años cumplidos son: {años_cumplidos(edad)}")


if __name__ == "__main__":
    main()