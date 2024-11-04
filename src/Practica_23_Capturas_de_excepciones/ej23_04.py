
def comprobar_numero() -> int:
    error = True
    while error:
        try:
            numero = introducir_numero()
            numero = int(numero)
            error = False
        except ValueError as e:
            print(f"La entrada no es correcta, {e}")
              
    return numero


def introducir_numero() -> str:
    numero = input("Introduce un numero: ")
	
    return numero


def main():
	comprobar_numero()


if __name__ == "__main__":
	main()