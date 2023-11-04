""" 
Ejercicio 2.2.23

Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron.
"""


def contar_lineas():
    lineas = 0
    num = "0123456789"
    cantidadnum = 0

    while True:
        libro = input("Libro: ")
        if libro == "*":
            break
        for caracter in libro:
            if caracter in num:
                cantidadnum += 1
        if libro == "/":
            lineas += 1
            print("Aparecen", cantidadnum, "dígitos en la línea")
            cantidadnum = 0
    return lineas


        
def main():    
    total_lineas = contar_lineas()
    print("Se leyeron", total_lineas, "líneas completas")
    
    
if __name__ == "__main__":
    main()

