"""
Ejercicio 2.2.15

Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
"""



def sumatoria_positivos():
    suma = 0
    while True:
        num = int(input("Ingrese un número entero (0 para finalizar): "))
        if num == 0:
            break
        if num > 0:
            suma += num
    return suma



    
def main():    
    print("El sumatorio de los números positivos que ha ingresado es" , sumatoria_positivos())

if __name__ == "__main__":
    main()