"""
Ejercicio 2.1.6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""


def grupo(name, sexo):
    name = name.upper()
    sexo = sexo.upper()
    if (sexo == "F" and name <= "M") or (sexo == "M" and name >= "N"):
        return "A"
    else:
        return "B"
    
    
def main():
    nombre = input("Introduzca su nombre: ")
    genero= input("Introduzca su género (M/F): ")
    print("Perteneces al grupo " , grupo(nombre, genero))
    
    
if __name__ == "__main__" :
    main()