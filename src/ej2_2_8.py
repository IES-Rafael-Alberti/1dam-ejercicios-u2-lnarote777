"""
Ejercicio 2.2.8

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""



def triangulo(num):
    for i in range(1, num+1 , 2):
        for x in range(i , 0, -2):
            print(x, end=" " )
        print("")
    return ""
    

def main():
    n = int(input("Introduce la altura del triángulo (entero positivo): "))
    print(triangulo(n))
    

if __name__ == "__main__":
    main()