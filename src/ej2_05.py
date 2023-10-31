"""
Ejercicio 2.1.5

Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales 
o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar o no.
"""

def tributar(edad, ingresos):
    if edad >= 16 and ingresos >= 1000:
        return "Usted puede tributar."
    else:
        return "Usted no puede tributar."


def main():
    edad=int(input("Introduzca su edad: "))
    ingresos=int(input("Cantidad de ingresos mensuales: "))
    print(tributar(edad , ingresos))
    
if __name__ == "__main__" :
    main()