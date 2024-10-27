"""Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

def comprobar_renta():
    renta = input("Introduce tu renta anual: ")
    error = True
    try:
        renta = float(renta)
        error = False

        if renta <= 0:
            raise ValueError("Los valores negativos no están permitidos")
        
    except ValueError as e:
        if error:
            print("*ERROR* El valor introducido no es un número")
        else:
            print(f"*ERROR* {e}")
    
    return renta


def tipo_impositivo(renta):
    if  renta < 10000 and renta > 0:
        return 5
    elif renta >= 10000 and renta < 20000:
        return 15
    elif renta >= 20000 and renta < 35000:
        return 20
    elif renta >= 35000 and renta < 60000:
        return 30
    elif renta >= 60000:
        return 45


def main():
    renta = comprobar_renta()
    tipo = tipo_impositivo(renta)
    
    if tipo is None:
        print(f"Su tipo impositivo es INVÁLIDO")
    else:
        print(f"Su tipo impositivo es {tipo}%")


if __name__ == "__main__":
    main()