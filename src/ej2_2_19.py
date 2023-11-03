""" 
Ejercicio 2.2.19

Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""



def menu():
    while True:
        print("1 - comenzar programa")
        print("2 - imprimir listado")
        print("3 - finalizar programa")
        opcion=int(input("elija una opción (1, 2 ó 3): "))
        if opcion==1:
            print("¡Comenzamos!")
        elif opcion==2:
            print("Toómbola el 13 abril, feria del 2 al 7 de abril, café importado - 18 enero.")
        elif opcion==3:
            print("Fin")
            break
        else:
            print("Opción incorrecta. Debe ingresar 1, 2 ó 3")
    return ""  
            
            
        
    
def main():    
    print(menu())

if __name__ == "__main__":
    main()