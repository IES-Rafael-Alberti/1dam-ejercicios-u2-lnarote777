"""
Ejercicio 2.1.6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""


def grupo(name, sexo):
    if (sexo == "Mujer" and name <= "M") or (sexo == "Hombre" and name >= "N"):
        return "A"
    else:
        return "B"
    
    
def main():
    name = input("Introduzca su nombre: ")
    sexo = input("Introduzca su género: ")
    name= name.upper()
    sexo= sexo.upper()
    print("Perteneces al grupo: " , grupo(name, sexo))
    
    
if __name__ == "__main__" :
    main()