
def comprobar_opcion_introducida() -> int:
    opcion_seleccionada = input("Introduce la opción a seleccionar: ")
    try:
        opcion_seleccionada = int(opcion_seleccionada)
        if opcion_seleccionada < 1 or opcion_seleccionada > 3:
            raise ValueError
        
        return opcion_seleccionada
    except ValueError:
        print("**ERROR** El valor introducido es incorrecto")
        return None

def constructor_menu():
    menu = "***OPCIONES***\n1.- Comenzar Programa\n2.- Imprimir Listado\n3.- Finalizar Programa"
    print(menu)

    return menu


def funcion_menu(opcion_seleccionada, menu: str):
    if opcion_seleccionada is not None:
        while opcion_seleccionada != 3:
            if opcion_seleccionada == 1:
                print("-------------------------------------\nSeleccionaste: 1.- Comenzar Programa\n-------------------------------------")
            elif opcion_seleccionada == 2:
                print("-------------------------------------\nSeleccionaste: 2.- Imprimir Listado\n-------------------------------------")
            print(menu)
            opcion_seleccionada = comprobar_opcion_introducida()
        print("-------------------------------------\nSeleccionaste: 3.- Finalizar Programa\n-------------------------------------")
    else:
        raise ValueError

def main():
    menu = constructor_menu()
    opcion_seleccionada = comprobar_opcion_introducida()
    if opcion_seleccionada is not None:
        funcion_menu(opcion_seleccionada, menu)


if __name__ == "__main__":
    main()