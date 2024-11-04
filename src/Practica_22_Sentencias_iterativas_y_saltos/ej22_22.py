
def entrada_numero():
    cant_impares = 0
    cant_pares = 0
    numero = -1
    while numero != '0':
        numero = input("Introduce un número positivo: ")
        if int(numero) < 0:
            numero *= -1
        cant_pares, cant_impares = par_impar(numero, cant_pares, cant_impares)

    return cant_pares, cant_impares


def par_impar(numero: str, cant_pares: int, cant_impares: int):
    for i in numero:
        if int(i) != 0:
            if int(i) % 2 == 0:
                cant_pares += 1
            else:
                cant_impares += 1

    return cant_pares, cant_impares


def main():
    cant_pares, cant_impares = entrada_numero()
    print(f"La cantidad de números pares es de {cant_pares} y la de impares de {cant_impares}")

if __name__ == "__main__":
    main()