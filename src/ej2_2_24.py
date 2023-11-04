""" 
Ejercicio 2.2.24

Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""


def primos():
    cantidad = 0
    n = int(input("Número: "))

    while n != 0:
        primo = True

        for i in range(2, n):
            if n % i == 0:
                primo = False
                break

        if primo:
            cantidad += 1

        n = int(input("Número: "))

    return cantidad


def main():    
    total_primos = primos()
    print("Cantidad de números primos: ", total_primos)
    
    
if __name__ == "__main__":
    main()


