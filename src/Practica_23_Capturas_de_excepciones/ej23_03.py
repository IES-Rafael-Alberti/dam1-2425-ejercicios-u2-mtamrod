
def comprobar_numero() -> int:
    error = True
    while error:
        try:
            numero = introducir_numero()
            numero = int(numero)
            if numero <= 0:
                raise ValueError
            error = False
        except ValueError:
              print("Número inválido.")
    return numero


def mostrar_del_reves() -> str:
	numero = comprobar_numero()
	numeros_reversa = ""
	for i in range (numero, -1, -1):
		numeros_reversa += str(i) + ", "
        
	return numeros_reversa.rstrip(", ")


def introducir_numero() -> str:
    numero = input("Introduce un numero: ")
	
    return numero


def main():
	print(mostrar_del_reves())


if __name__ == "__main__":
	main()