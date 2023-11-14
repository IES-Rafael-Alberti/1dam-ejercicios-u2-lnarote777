"""
Ejercicio 2.1.4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

def par(num):
    if num%2 == 0:
        return str(num) + " es par."
    else:
        return str(num) + " es impar."


def main():
    n=int(input("Introduzca un número entero: "))
    print(par(n))
    
if __name__ == "__main__" :
    main()