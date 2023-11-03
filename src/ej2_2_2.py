"""
Ejercicio 2.2.2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def cumplidos(edad):
    cont = 1
    anos = str()
    for i in range(1, edad + 1):
        cont += i
        if i != edad:
            anos += str(f"{i}, ")
        else:
            anos += str(f"{edad} años. ")
    return anos
        
        
        
def main():
    years= int(input("introduzca su edad: "))
    print("Ha cumplido" , cumplidos(years))
    
    
if __name__ == "__main__":
    main()
