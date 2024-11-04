
def configurador_titulos(frase: str) -> int:
    cont_digitos = 0
    for i in frase:
        if i.isdigit():
            cont_digitos += 1

    return cont_digitos


def salto_linea():
    conjunto_frase = ""
    cont_linea = 0
    salir = False
    while not salir:
        frase = pedir_frase()
        if frase != "/" and frase != "*":
            conjunto_frase += frase.replace(" ", "")
        elif frase == "/":
            cont_linea += 1
            mostrar_por_pantalla(f"Línea completa. Aparecen {configurador_titulos(conjunto_frase)} dígitos numéricos.")
            conjunto_frase = ""
        elif frase == "*":
            salir = True
            mostrar_por_pantalla(f"Fin. Se leyeron {cont_linea} líneas completas.")
        

def pedir_frase() -> str:
    frase = input("Libro: ")  

    return frase


def mostrar_por_pantalla(mensaje: str):
    print(mensaje)


def main():
    salto_linea()


if __name__ == "__main__":
    main()