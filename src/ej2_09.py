"""
Ejercicio 2.1.9

Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""


def cobro(edad):
    entrada1="Gratis"
    entrada2= 5, "€"
    entrada3= 10, "€"
    if edad < 4 :
        return entrada1
    elif edad > 4 and edad < 18 :
        return entrada2
    elif edad >= 18:
        return entrada3