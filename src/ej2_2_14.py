"""
Ejercicio 2.2.14

Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""


def sumatoria():
    num = int(input("Ingrese numeros enteros (0 para terminar): \n" ))
    suma = 0
    while num != 0 :
        suma += num
        num = int(input())
    return suma



    
def main():    
    print("El sumatorio de todos los números que ha ingresado es" , sumatoria())

if __name__ == "__main__":
    main()