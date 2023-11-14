"""
Ejercicio 2.1.2
 
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""



def comprobarPassword(password):
    miPassWord = "contraseña" 
    
    if password.lower() == miPassWord.lower():
        return "Tu contraseña coincide con la mía."
    else:
        return "No coincide."


def main():
    
    password = input("Introduzca contraseña: ")
    
    print(comprobarPassword(password))

if __name__ == "__main__":
    main()
