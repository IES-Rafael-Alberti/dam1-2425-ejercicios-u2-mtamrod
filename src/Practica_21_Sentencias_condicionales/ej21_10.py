
def comprobar_ingrediente(ingrediente: str, tipo_pizza: str) -> str:
    error = True
    while error:
        if ingrediente == "jamón":
            ingrediente = "jamon"
        elif ingrediente == "salmón":
            ingrediente = "salmon"
            
        try:
            match tipo_pizza:
                case "VEGETARIANA":
                    if ingrediente != "tofu" and ingrediente != "pimiento":
                        raise ValueError
                case "NOVEGETARIANA":
                    if ingrediente != "peperoni" and ingrediente != "jamon" and ingrediente != "salmon":
                        raise ValueError
            
            error = False
        except ValueError:
            print(f"{ingrediente} no es un tipo de ingrediente válido")
            ingrediente = input("Indica un ingrediente correcto: ").lower().replace(" ","").replace(".", "")
        
    return ingrediente


def comprobar_tipo_pizza(tipo_pizza: str):
    error = True
    while error:
        try:
            if tipo_pizza != "VEGETARIANA" and tipo_pizza != "NOVEGETARIANA":
                raise ValueError
            error = False
        except ValueError:
            print(f"{tipo_pizza} no es un tipo de pizza válido")
            tipo_pizza = input("¿Qué tipo de pizza quieres (VEGETARIANA/NO VEGETARIANA)?: ").upper().replace(" ","").replace(".", "")
        
    return tipo_pizza


def menu_ingredientes_pizza(tipo_pizza: str):
    match tipo_pizza:
        case "VEGETARIANA":
            print("Los ingredientes a elegir son:\n - Tofu\n - Pimiento")
        case "NOVEGETARIANA":
            print("Los ingredientes a elegir son:\n - Peperoni\n - Jamón\n - Salmón")

    print("Solo puedes elegir 1 ingrediente (MOZZARELLA Y TOMATE INCLUÍDOS)")


def main():
    tipo_pizza = input("¿Qué tipo de pizza quieres (VEGETARIANA/NO VEGETARIANA)?: ").upper().replace(" ","").replace(".", "")

    tipo_pizza = comprobar_tipo_pizza(tipo_pizza)
    menu_ingredientes_pizza(tipo_pizza)

    ingrediente = input("Indica el ingrediente: ").lower().replace(" ","").replace(".", "")
    ingrediente = comprobar_ingrediente(ingrediente, tipo_pizza)

    if tipo_pizza == "NOVEGETARIANA":
        print(f"Has seleccionado una pizza no vegetariana con el ingrediente {ingrediente}.")
    else:
        print(f"Has seleccionado una pizza vegetariana con el ingrediente {ingrediente}.")


if __name__ == "__main__":
    main()