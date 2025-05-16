'''
Autor: Jesy Nicole González Jarquín
Fecha: 02/05/2025
Versión: 1.0 
Descripción: Este programa calcula la tabla de multiplicar del numero n 
             desde 1 - m. 
'''
import os

def multiplicar():
    os.system("cls")
    print("📋 Tabla de Multiplicación")
    n= int(input("Digite el número base de la tabla: "))
    m= int(input("Digite el número hasta donde quiere multiplicar: "))
    print(" ")
    print("La tabla de multiplicar del número", n, "es:")
    for i in range(1, m+1):
        print(n, "x", i, "=", n*i)
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
