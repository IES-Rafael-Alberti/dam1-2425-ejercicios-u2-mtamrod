#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def comprobar_numero() -> int:
    error = True
    while error:
        numero_intro = input("Introduce un número entero: ")
        try:
            float(numero_intro)
            error = False
            numero_intro = int(numero_intro)
        except ValueError as e:
            if error:
                print(f"*ERROR* No puede ser una cadena de caractéres.")
            else:
                print(f"*ERROR* No puede ser un decimal.")
                error = True 

    return numero_intro


def par_impar(numero_intro: int):
    if int(numero_intro)%2 == 0:
        tipo = "par"
    else:
        tipo = "impar"

    return tipo


def main():
    numero_intro = comprobar_numero()
    print(par_impar(numero_intro))


if __name__ == "__main__":
    main()