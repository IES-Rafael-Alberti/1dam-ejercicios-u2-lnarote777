"""
Ejercicio 2.2.11

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""


def letras(palabra):
    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i])
    return ""


def main():
    word = input("Introduzca una palabra: ")
    print(letras(word))
     
    
if __name__ == "__main__":
    main()
