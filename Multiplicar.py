'''
Autor: Jesy Nicole González Jarquín
Fecha: 02/05/2025
Versión: 1.0 
Descripción: Este programa calcula las tablas de multiplicar hasta el numero n 
ingresado por el usuario. 
'''
import os

def multiplicar():
    os.system("cls")
    print("📋 Tabla de Multiplicación")
    n= int(input("Digite el número de tablas de multiplicar que quiere: "))
    m= int(input("Digite el número hasta el cual quiere multiplicar las tablas: "))
    print(" ")
    for i in range(1, n+1):
        print("La tabla de multiplicar del número", i, "hasta el", m,"es:")
        for j in range(1, m+1): # el 1 es el primer número a multiplicar y el m es el último número a multiplicar
            # + 1 porque el rango no incluye el último número
            print(i, "x", j, "=", i*j)
        print(" ")
    print("¿Desea continuar? (s/n)")
    continuar = input("Digite su respuesta: ")
    if continuar.lower() == "s":
        multiplicar()
    elif continuar.lower() == "n":
        print("Gracias por usar el programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Saliendo del programa.")

if __name__ == "__main__":
    multiplicar()


