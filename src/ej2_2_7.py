"""
Ejercicio 2.2.7

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""


def multiplicacion():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end="\t")
        print("")
    return ""    
        
        
        
def main():
    print(multiplicacion())
    

if __name__ == "__main__":
    main()