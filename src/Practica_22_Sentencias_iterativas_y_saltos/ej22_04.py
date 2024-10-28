
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


def mostrar_serie(numero: int) -> str:
    impares = ""

    for i in range (numero, -1, -1): 
        impares += str(i) + ", "

    return impares.rstrip(", ")


def main():
    numero = input("Introduce un numero entero positivo: ")

    numero = comprobar_numero(numero)
    print(f"Los números impares son: {mostrar_serie(numero)}")


if __name__ == "__main__":
    main()