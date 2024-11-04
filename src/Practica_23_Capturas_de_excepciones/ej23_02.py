
def comprobar_numero(numero: str) -> int:
    error = True
    while error:
        try:
            numero = int(numero)
            if numero <= 0:
                raise ValueError
            error = False
        except ValueError:
            print("*ERROR* Número inválido")
            numero = input("Introduce un numero entero positivo: ")
    
    return numero


def mostrar_impares(numero: int) -> str:
    impares = ""

    for i in range (0, numero + 1):
        if i%2 != 0: 
            impares += str(i) + ", "

    return impares.rstrip(", ")


def main():
    numero = input("Introduce un numero entero positivo: ")

    numero = comprobar_numero(numero)
    print(f"Los números impares son: {mostrar_impares(numero)}")


if __name__ == "__main__":
    main()