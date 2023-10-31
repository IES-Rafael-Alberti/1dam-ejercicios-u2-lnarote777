"""
Ejercicio 2.1.3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""


def division(num1 , num2):
    if num2 == 0:
        return "***ERROR*** - El divisor no puede ser 0."
    div = num1/num2
    return div


def main():
    n1=int(input("Introduzca un número entero: "))
    n2=int(input("Introduzca otro número entero: "))
    print(division(n1 , n2))
    
if __name__ == "__main__" :
    main()