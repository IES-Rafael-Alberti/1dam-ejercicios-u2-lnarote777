"""
Ejercicio 2.2.4

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

def cuenta_atras(num):
    cuenta = str()
    for i in range(num, -1, -1):
        if i != 0:
            cuenta += f"{i}, "
        else:
            cuenta += f"{i}. "
    return cuenta
        
        
                   
def main():
    n= int(input("introduzca su num: "))
    print(cuenta_atras(n))
    
    
if __name__ == "__main__":
    main()
  
