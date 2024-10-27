
def comprobar_nombre(nombre: str):
    try:
        if nombre.count('.') > 0 or "ª" in nombre or nombre[0].isdigit() or float(nombre) :
            raise Exception("El nombre debe de ser una cadena de caracteres válida")
    except ValueError:
        pass


def comprobar_sexo(sexo: str):
    if sexo != "FEMENINO" and sexo != "MASCULINO":
        raise ValueError("Debes introducir un sexo válido")
    

def comprobar_sexo_nombre(sexo: str, nombre: str):
    try:
        comprobar_sexo(sexo)
        comprobar_nombre(nombre)
    except (ValueError, Exception) as e:
        print(f"*ERROR* {e}")
        return True
        
    return False


def rango(sexo: str, nombre: str) -> str:
    grupo = ""
    primera_letra = nombre[0]

    if sexo == "FEMENINO":
        if primera_letra < "M":
            grupo = "A"
        else:
            grupo = "B"
    else:
        if primera_letra >= "M":
            grupo = "A"
        else:
            grupo = "B"

    return grupo


def main():
    error = True

    while error:
        sexo = input("Introduce tu sexo (masculino/femenino): ").upper()
        nombre = input("Introduce tu nombre: ").upper()

        error = comprobar_sexo_nombre(sexo, nombre)
        
    grupo = rango(sexo, nombre)

    print(f"Eres del sexo {sexo.lower()}, te llamas {nombre.capitalize()} y perteneces al grupo {grupo}")


if __name__ == "__main__":
    main()