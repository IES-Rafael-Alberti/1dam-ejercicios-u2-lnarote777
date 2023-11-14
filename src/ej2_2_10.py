"""
Ejercicio 2.2.10

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return "No es primo"
        else:
            return "Es primo"
 


def main():
    n= int(input("introduzca un número entero: "))
    print(es_primo(n))
    
    
    
    
if __name__ == "__main__":
    main()
