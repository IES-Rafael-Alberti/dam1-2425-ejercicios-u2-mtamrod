
def suma_entrada() -> int:
    pares = 0
    numero = 0

    while numero != -1:
        suma = 0
        numero = int(input("Introduce un número: "))
        if numero % 2 == 0:
            pares += 1

        if numero != -1:
            for i in range (0, numero + 1):
                suma += i
            print(f"La suma de los numeros que componen {numero} es: {suma}")

    return pares
        

def main():
    print(f"En los números introducidos hay {suma_entrada()} pares")


if __name__ == "__main__":
    main()