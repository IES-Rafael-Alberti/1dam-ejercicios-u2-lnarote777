"""
Ejercicio 2.2.9

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""


def comprobarPassword(password):
    miPassWord = "contraseña" 
    
    while password.lower() != miPassWord.lower():
        password = input("Contraseña inválida. Introduzca contraseña: ")
    return "Contraseña correcta."


def main():
    
    password = input("Introduzca contraseña: ")
    
    print(comprobarPassword(password))

if __name__ == "__main__":
    main()
