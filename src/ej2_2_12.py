"""
Ejercicio 2.2.12

Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""


def letra_en_frase():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    return f"La letra {letra} aparece {contador} veces en la frase."





def main():    
    print(letra_en_frase())

if __name__ == "__main__":
    main()
