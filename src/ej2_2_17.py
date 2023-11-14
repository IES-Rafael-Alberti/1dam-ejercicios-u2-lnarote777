"""  
Ejercicio 2.2.17

Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

"""


def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma


def main():   
    n = int(input("Introduzca un número entero positivo: ")) 
    print(suma_digitos(n))

if __name__ == "__main__":
    main()