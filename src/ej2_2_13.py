"""
Ejercicio 2.2.13

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def eco(frase):
    while True:
        if frase == "salir":
            break
        print(frase) 
    return ''
    
    
    
    
def main(): 
    frase =input("Introduzca algo: ")    
    print(eco(frase))

if __name__ == "__main__":
    main()