"""
Ejercicio 2.2.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

"""



def impar(num):
    cont = 1
    suma = str()
    for i in range(1, num + 1, 2) :
        cont += i
        if i != num:
            suma += str(f"{i}, ")
        else:
            suma += str(f"{num}. ")
    return suma
        


def main():
    n= int(input("introduzca un número entero positivo: "))
    print(impar(n))
    
    
    
    
if __name__ == "__main__":
    main()
