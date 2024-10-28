
def repetir_numero():
    salir = False

    while not salir:
        numero = int(input("Introduce una palabra: "))
        
        if numero == 0:
            salir = True
        else:
            print(numero)


def main():
    repetir_numero()


if __name__ == "__main__":
	main()