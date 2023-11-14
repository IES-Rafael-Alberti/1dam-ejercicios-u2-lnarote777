""" 
Ejercicio 2.2.16

Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""

def mayor():
    max = None
    while True:
        num = int(input("Ingrese un número entero (0 para finalizar): "))
        if num == 0:
            break
        if num > 0:
            if max is None or num > max :
                max = num
    return max



    
def main():    
    print("El mayor de los números positivos que ha ingresado es" , mayor())

if __name__ == "__main__":
    main()