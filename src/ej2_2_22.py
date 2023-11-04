""" 
Ejercicio 2.2.22

Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""


def pares_impares(num):
    total_pares = 0
    total_impares = 0  
    while num != 0:
        par = 0
        impar = 0
        while num != 0:
            ultimonum = num % 10

            if ultimonum % 2 == 0:
                par += 1
                total_pares += 1
            else:
                impar += 1
                total_impares += 1

            num = num // 10      
             
        print("El número tiene" , par , " pares y " , impar , " impares")
        num = int(input("Ingrese un número entero positivo (0 para finalizar): "))
        
    return f"Total de dígitos pares: {total_pares}. \nTotal de dígitos impares: {total_impares}." 

        
        
def main():    
    num = int(input("Ingrese un número entero positivo (0 para finalizar): "))
    print(pares_impares(num))
    
    
if __name__ == "__main__":
    main()