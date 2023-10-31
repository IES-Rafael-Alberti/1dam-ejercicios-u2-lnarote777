"""
Ejercicio 2.1.7

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""


def impositivo(renta):
    if renta < 10000 :
        return "5%"
    elif renta > 10000 and renta < 20000 :
        return "15%"
    elif renta > 20000 and renta < 35000 :
        return "20%"
    elif renta >35000 and renta < 60000 :
        return "30%"
    elif renta > 60000 :
        return "45%"
    

def main():
    rentaAnual= int(input("Introduzca su renta anual: "))
    print("El tipo de impositivo que le corresponde es del " , impositivo(rentaAnual))
    

if __name__ == "__main__" :
    main()