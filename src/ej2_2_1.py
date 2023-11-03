"""
Ejercicio 2.2.1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""


def rep(palabra):
    for i in range(9):
        print(palabra) 
    return palabra



def main():
    word=input("Introduzca una palabra: ")
    print(rep(word))
    
    
    
if __name__ == "__main__":
    main()