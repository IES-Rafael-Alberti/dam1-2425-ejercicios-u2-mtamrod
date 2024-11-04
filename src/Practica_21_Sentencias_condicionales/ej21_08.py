
def comprobar_puntuacion(puntuacion: str) -> float:
    error = True
    while error:
        try:
            puntuacion = float(puntuacion)
            if puntuacion < 0:
                raise ValueError
            error = False
        except ValueError:
            print("*ERROR* Puntuación inválida")
            puntuacion = input("Introduce la puntuación: ")

    return puntuacion


def nivel(puntuacion: float) -> str:
    if puntuacion == 0 and puntuacion < 0.4:
        return "Inaceptable"
    elif puntuacion >= 0.4 and puntuacion <= 0.6:
        return "Aceptable"
    else:
        return "Meritorio"
    

def main():
    puntuacion = input("Introduce la puntuación: ")
    puntuacion = comprobar_puntuacion(puntuacion)

    print(f"Su nivel es {nivel(puntuacion).lower()}")


if __name__ == "__main__":
    main()