"""
Ejercicio 2.2.5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""


def inversion(amount, interest, years):
    for i in range(years):
        amount *= 1 + interest / 100
        print("Capital tras " + str(i+1) + " años: " + str(amount) ) 
    return ""
    
    

def main():
    amount = float(input("¿Qué cantidad desea invertir? "))
    interest = float(input("¿Interes porcentual anual? "))
    years = int(input("¿Durante cuantos años? "))
    print(inversion(amount, interest, years))
        
        
        
if __name__ == "__main__":
    main()
  