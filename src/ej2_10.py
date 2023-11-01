"""
Ejercicio 2.1.10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no 
y todos los ingredientes que lleva.

"""

def menu(pizza):
    ing = "Mozzarella , salsa tomate y "
    if pizza == "Sí":
        ingrediente=input("Ingredientes vegetarianos: Pimiento y tofu. Elija uno: ")
        return "Su pizza es vegetariana. Ingredientes: " + ing + ingrediente
    else:
        ingrediente=input("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. Elija uno:")
        return "Su pizza no es vegetariana. Ingredientes: " + ing + ingrediente




def main():
    pizza= input("¿Desea una pizza Vegetariana? (Sí/No) ").title()
    print(menu(pizza))
    
    
    
if __name__ == "__main__":
    main()