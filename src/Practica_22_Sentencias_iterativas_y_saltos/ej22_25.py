
def palabra_mas_larga(frase: str):
    n_letras = 0
    palabra = ""
    for i in frase:
        if i != " ":
            palabra += i
        if i == " ":
            if n_letras < len(palabra):
                n_letras = len(palabra)
                palabra_grande = palabra
                palabra = ""
            
    return palabra_grande


def main():
    frase = input("Introduce una frase: ") + " "
    print(f"Frase: {frase}\nPalabra más larga: {palabra_mas_larga(frase)}")


if __name__ == "__main__":
    main()