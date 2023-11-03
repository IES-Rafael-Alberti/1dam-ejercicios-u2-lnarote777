""" 
Ejercicio 2.2.20

Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""



def buscar_letra_en_frase(frase, letra):
    i = 0
    while i != len(frase):
        if letra != frase[i]:
            print(f"No se encontró '{letra}' en la posición {i}")
            i += 1
            continue
        print(f"Se encontró '{letra}' en la posición {i}")
        break





def main():
    frase = input("Frase: ")
    letra = input("Letra para buscar su posición: ")    
    print(buscar_letra_en_frase(frase, letra))

if __name__ == "__main__":
    main()