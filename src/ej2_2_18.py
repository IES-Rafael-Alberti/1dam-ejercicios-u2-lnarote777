""" 
Ejercicio 2.2.18

Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen.
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""


def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma



numeros_pares = 0

while True:
    num = int(input("Ingrese un número entero positivo (-1 para finalizar): "))
    
    if num == -1:
        break
    
    if num > 0:
        suma = suma_digitos(num)
        print(f"La suma de los dígitos de {num} es {suma}.")
        
        if suma % 2 == 0:
            numeros_pares += 1

print(f"De los números ingresados, {numeros_pares} son números pares.")

