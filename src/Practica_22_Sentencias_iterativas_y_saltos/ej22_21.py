
def ingreso_monto():
    monto = -1
    suma = 0
    while monto != 0 or monto < 0:
        monto = float(input("Introduce el monto de compra: "))
        suma += monto

    return suma


def descuento_monto(suma: float) -> float:
    if suma > 1000:
        suma -= suma * 0.1

    return suma 


def main():
    suma = ingreso_monto()
    suma = descuento_monto(suma)

    print(f"El total a pagar es de {suma:.2f}€")


if __name__ == "__main__":
    main()