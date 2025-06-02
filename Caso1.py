'''
Caso 1: Registro semanal de gastos de estudiantes UAM
Autores: Jesy Nicole González Jarquín
         Marian Alejandra Guillén Castillo
         Nora Maria Obregón Membreño
Fecha: 20/05/2025
Versión: (Versionado por github)

Descripción:
Este programa simula el control de gastos semanales de un estudiante de primer año de la UAM.
Se registran los gastos diarios durante 4 semanas (7 días cada una). Al final se muestra el total
gastado por semana y el acumulado del mes.
'''

import os


def registroGastosEstudiante():
    os.system("cls" if os.name == "nt" else "clear")  # Limpia la consola dependiendo del sistema operativo
    print("📘 Registro semanal de gastos - Estudiantes UAM")
    print("-------------------------------------------------")

    nombreEstudiante = input("Ingrese el nombre del estudiante: ").strip()
    gastoMensual = 0.0

    for semana in range(1, 5):
        print(f"\n📅 Semana {semana}")
        gastoSemanal = 0.0

        for dia in range(1, 8):
            while True:
                try:
                    gastoDiario = float(input(f"Ingrese el gasto del día {dia}: "))
                    if gastoDiario < 0:
                        print("❌ El gasto no puede ser negativo. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("⚠️ Ingrese un número válido.")

            gastoSemanal += gastoDiario

        print(f"💸 Total gastado en la semana {semana}: {gastoSemanal}")
        gastoMensual += gastoSemanal

    print("\n📍 Resumen mensual")
    print(f"👤 Estudiante: {nombreEstudiante}")
    print(f"💰 Total mensual gastado: {gastoMensual}")

if __name__ == "__main__":
    registroGastosEstudiante()

