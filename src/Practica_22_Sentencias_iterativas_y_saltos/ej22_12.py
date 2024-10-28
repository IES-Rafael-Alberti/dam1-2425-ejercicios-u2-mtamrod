
def contar_palabra(frase: str, letra: str) -> int:
    n_letras = 0

    for i in frase:
        if i == letra:
            n_letras += 1

    return n_letras


def main():
    frase = input("Introduce una frase: ").lower()
    letra = input("Introduce una palabra: ").lower()

    print(f"Hay {contar_palabra(frase, letra)} '{letra}' en la frase '{frase}'")


if __name__ == "__main__":
	main()