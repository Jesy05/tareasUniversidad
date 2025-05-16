'''
Autor: Jesy Nicole González Jarquín
Fecha: 16/05/2025
Versión: 1.0 

Descripción: Caso 1: Registro semanal de gastos de estudiantes UAM

Cree un programa que simule el control de gastos semanales de un grupo 
de estudiantes de primer año de la UAM. El sistema debe procesar datos 
de 4 semanas, y por cada semana, ingresar el gasto realizado cada día 
(7 días por semana). El programa debe calcular el total gastado por semana 
y el total acumulado del mes. Utilice bucles anidados para recorrer
semanas y días.

'''
import os


def RegistroSemanal():
    os.system("cls")
    print("📋 Registro Mensual de Gastos Por Semana")
    total_acumulado = 0
    for semanas in range(1, 5): # 4 semanas
        print(f"\nSemana {semanas}")
        total_semana = 0
        for dia in range(1, 8): # 7 días
            gasto = float(input(f"Digite el gasto del día {dia}: ")) # {dia} es un número del 1 al 7 las {} son para concatenar
           
            # Validación para que el gasto no sea negativo
            while gasto < 0:
                print("El gasto no puede ser negativo. Intente de nuevo.")
                gasto = float(input(f"Digite el gasto del día {dia}: "))
            total_semana += gasto
        print(f"Total gastado en la semana {semanas}: {total_semana}")
        total_acumulado += total_semana
    print(f"\nTotal acumulado del mes: {total_acumulado}")

    print("¿Desea continuar? (s/n)")
    continuar = input("Digite su respuesta: ")
    if continuar.lower() == "s":
        RegistroSemanal()
    elif continuar.lower() == "n":
        print("Gracias por usar el programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Saliendo del programa.")

if __name__ == "__main__":
    RegistroSemanal()


