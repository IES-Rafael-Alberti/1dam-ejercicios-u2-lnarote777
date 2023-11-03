"""
Ejercicio 2.1.8

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""


def puntuacion():
    puntos = float(input("Introduzca su puntuación: "))
    inaceptable = 0.0
    aceptable = 0.4
    meritorio = 0.6
    if puntos == inaceptable:
        level = "Inaceptable"
    elif puntos == aceptable:
        level = "Aceptable"
    elif puntos >= meritorio:
        level = "Meritorio"
    else:
        level = ""
    print(nivel(level, puntos))
    
def nivel(level , puntos ):
    if level == "":
        return "Puntuación inválida"
    else:
        return "El nivel de rendimiento es " + level + ", le corresponden " + str(puntos * 2400) + "€"
        
        
        
        
def main():
    print(puntuacion())
    

if __name__ == "__main__":
    main()