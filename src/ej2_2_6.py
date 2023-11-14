"""
Ejercicio 2.2.6

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""


def triangulo(num):
    for i in range(num):
        for x in range(i+1):
            print("*", end="")
        print("")
    return ""
    

def main():
    n = int(input("Introduce la altura del triángulo (entero positivo): "))
    print(triangulo(n))
    

if __name__ == "__main__":
    main()