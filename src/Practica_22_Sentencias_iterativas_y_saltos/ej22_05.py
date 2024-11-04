
def comprobar_numero(cantidad_invertida: str, interes_anual: str, numero_anos: str) -> tuple:
    error = True
    while error:
        try:
            cantidad_invertida = float(cantidad_invertida)
            interes_anual = float(interes_anual)
            numero_anos = int(numero_anos)
            if cantidad_invertida <= 0 or interes_anual < 0 or numero_anos <= 0:
                raise ValueError
            error = False
        except ValueError: 
            print("*ERROR* Valor inválido")
            cantidad_invertida = input("Introduce la cantidad a invertir: ")
            interes_anual = input("Introduce el interés anual: ")
            numero_anos = input("Introduce el número de años: ")

    return cantidad_invertida, interes_anual, numero_anos


def interes_calculado(cantidad_invertida: float, interes_anual: float, numero_anos: int ) -> float:
    for i in range (0, numero_anos + 1):
        cantidad_invertida *= 1 + interes_anual / 100
        print(f"En el año {i} tenemos: {round(cantidad_invertida, 2)}")

    print("--------")
    return round(cantidad_invertida, 2)


def main():
    cantidad_invertida = input("Introduce la cantidad a invertir: ")
    interes_anual = input("Introduce el interés anual: ")
    numero_anos = input("Introduce el número de años: ")

    cantidad_invertida, interes_anual, numero_anos = comprobar_numero(cantidad_invertida, interes_anual, numero_anos)
    print(f"El dinero total obtenido es: {interes_calculado(cantidad_invertida, interes_anual, numero_anos)}")


if __name__ == "__main__":
    main()