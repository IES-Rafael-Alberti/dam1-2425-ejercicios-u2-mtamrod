
def comprobar_edad() -> int:
    edad_invalida = True

    while edad_invalida:
        valor_edad = input("Introduce tu edad: ")

        try:
            float(valor_edad)
            edad = int(valor_edad)

            if edad <= 0 or edad > 125 :
                raise ValueError
            
            edad_invalida = False
        except ValueError:
            print("*ERROR* Debes introducir una edad válida")

    return edad

def mayor_edad(edad: int) -> str:
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

def main():
    edad = comprobar_edad()
    print(mayor_edad(edad))


if __name__ == "__main__":
    main()