"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
    Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
    tiene que tributar o no."""
def comprobar_edad_sueldo() -> tuple:
    error = True
    while error:
        edad = input("Introduce tu edad: ")
        ingreso_mensual = input("Introduce tu sueldo mensual: ")
        try:
            int(edad)
            error = False
            float(ingreso_mensual)
            error = False
        except ValueError:
            if error:
                print("*ERROR* La edad debe de ser un número entero")
            else:
                print("*ERROR* El sueldo debe de ser un número")
                error = True
        
    
    edad = int(edad)
    ingreso_mensual = float(ingreso_mensual)

    return edad, ingreso_mensual


def tributar(edad, ingreso_mensual):
    if edad > 16 and ingreso_mensual > 1000:
        return "Si"
    else:
        return "No"


def main():
    edad, ingreso_mensual = comprobar_edad_sueldo()
    print(f"{tributar(edad, ingreso_mensual)} eres apto para tributar.")


if __name__ == "__main__":
    main()