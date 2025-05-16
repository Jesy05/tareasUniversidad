'''
Autor: fulano 
Fecha: 16/05/2025
Versión: 1.0 
Descripción: Este programa 

'''
import os

def funcion():
    os.system("cls")

    print("¿Desea continuar? (s/n)")
    continuar = input("Digite su respuesta: ")
    if continuar.lower() == "s":
        funcion()
    elif continuar.lower() == "n":
        print("Gracias por usar el programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Saliendo del programa.")

if __name__ == "__main__":
    funcion()



