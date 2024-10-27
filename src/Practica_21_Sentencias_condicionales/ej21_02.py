CONTRASENA = "contraseña"

def comprobar_contraseña() -> str:
    contraseña_introducida = input("Introduce la contraseña: ").lower()
    try:
        if len(contraseña_introducida) > 10:
            raise ValueError("La contraseña debe ser de 10 o menos caracteres")
        elif len(contraseña_introducida) <= 0:
            raise ValueError("La contraseña debe ser de más de 0 caracteres")
        
    except ValueError as e:
        print(f"*ERROR* {e}")

    return contraseña_introducida


def contraseña_correcta(contraseña_introducida: str) -> bool:
    if contraseña_introducida == CONTRASENA:
        print("Contraseña correcta!")
        return True
    elif contraseña_introducida != CONTRASENA:
        print("Contraseña incorrecta!")
        return False


def main():
    intentos = 3
    acierto = False
    while intentos > 0 and not acierto:
        print(f"Tienes {intentos} intentos")
        contraseña_introducida = comprobar_contraseña()
        acierto = contraseña_correcta(contraseña_introducida)
        intentos -= 1


if __name__ == "__main__":
    main()