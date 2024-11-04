
def suma_entrada(numero: int) -> int:
    suma = 0
    for i in range (0, numero + 1):
        suma += i

    return suma


def main():
    numero = int(input("Introduce un número: "))
    print(f"La suma de los numeros que componen {numero} es: {suma_entrada(numero)}")

if __name__ == "__main__":
    main()