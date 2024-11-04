
def mostrar_del_reves(palabra: str) -> str:
	longitud_palabra = len(palabra)
	palabra_reves = ""
	
	
	for i in range (longitud_palabra - 1, -1, -1):
		palabra_reves += palabra[i]

		if i != longitud_palabra:
			palabra_reves += "\n"
        
	return palabra_reves

def main():
	palabra = input("Introduce una palabra: ")
	print(mostrar_del_reves(palabra))


if __name__ == "__main__":
	main()