
def repetir_palabra():
    salir = False

    while not salir:
        palabra = input("Introduce una palabra: ")
        
        if palabra.lower() == "salir":
            salir = True
        else:
            print(palabra)


def main():
    repetir_palabra()


if __name__ == "__main__":
	main()