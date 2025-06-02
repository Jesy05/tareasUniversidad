# este codigo sirve para mostrar poner una contraseña y validar que es la correcta 

import os

def password():
    os.system('cls') #lll
    password = "contra123"
    intentos = 3 #tralala
    while intentos > 0:
        entrada = input("Introduce la contraseña: ")
        if entrada == password:
            print("Contraseña correcta.")
            print("Puede pasarle adelante\n...\n...\n...")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    print("Has agotado todos los intentos.")
    return False

if __name__ == "__main__":
    password()