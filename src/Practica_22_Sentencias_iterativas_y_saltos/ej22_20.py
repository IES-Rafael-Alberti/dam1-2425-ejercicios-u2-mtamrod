
def solicitar_usuario():
    frase = input("Introduce una frase: ").lower()
    letra = input("Introduce una letra: ").lower()

    return frase, letra


def encontrar_letra(frase: str, letra: str) -> str:
    n_letras = 0
    for i in frase:
        if i == letra:
            n_letras += 1
            pos_1letra = i 
        
    if n_letras == 1:
        return f"Hay {n_letras} coincidencias y la coincidencia es en la posición {pos_1letra}."
    elif n_letras > 1:
        return f"Hay {n_letras} coincidencias y la primera coincidencia es en la posición {pos_1letra}."
    else:
        return f"Hay {n_letras} coincidencias."


def main():
    frase, letra = solicitar_usuario()
    print(encontrar_letra(frase, letra))


if __name__ == "__main__":
    main()