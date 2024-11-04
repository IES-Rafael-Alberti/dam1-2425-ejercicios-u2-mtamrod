CONTRASENA = "contrasena"

def comprobar_contraseña(contrasena: str):
    try:
        if contrasena != CONTRASENA:
            raise NameError("Incorrect Password!!")
    except NameError as e:
        print(e)
    
    return "Your password is correct!!"


def main():
    contrasena = input("Introduce la contraseña: ")
    print(comprobar_contraseña(contrasena))


if __name__ == "__main__":
    main()