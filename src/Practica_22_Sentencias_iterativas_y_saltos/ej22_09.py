
CONTRASENA = "DragonBall"

def contrasenia_valida(entrada_contrasenia: str):
    i = 3
    while i != 0:
        i -= 1
        if entrada_contrasenia == CONTRASENA:
             print("La contraseña es correcta")
        elif i == 0:
            print(f"Contraseña incorrecta ({i} intentos)")
            print("Oh no! Te has quedado sin intentos.")
        else:
            print(f"Contraseña incorrecta ({i} intentos)")
            entrada_contrasenia = input("Introduce una contraseña: ")


def main():
    entrada_contrasenia = input("Introduce una contraseña (Tienes 3 intentos): ")
    contrasenia_valida(entrada_contrasenia)


if __name__ == "__main__":
    main()