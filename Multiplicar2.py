'''
Autor: Jesy Nicole González Jarquín 
Fecha: 16/05/2025
Versión: 1.0 
Descripción: Este programa calcula las tablas de multiplicar hasta el numero n 
            ingresado por el usuario (pero sin for, solo while). 

'''
import os

def funcion():
    os.system("cls")
    print("📋 Tabla de Multiplicación")
    while True:
        try:
            n = int(input("Digite el número de tablas de multiplicar que quiere: "))
            m = int(input("Digite el número hasta el cual quiere multiplicar las tablas: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")   
    print(" ")
    i = 1
    while i <= n:
        print("La tabla de multiplicar del número", i, "hasta el", m, "es:")
        j = 1
        while j <= m:
            print(i, "x", j, "=", i * j)
            j += 1
        print(" ")
        i += 1
        
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

