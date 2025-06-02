'''
Autores: Jesy Nicole González Jarquín
Marian Alejandra Guillén Castillo
Nora Maria Obregón Membreño
Fecha: 20/05/2025
Versión: (Versionado por github)

Descripción:

Caso 3: Registro de participación estudiantil por carrera en la UAM
Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
extracurriculares por carrera. Considere tres carreras (por ejemplo: Sistemas, Marketing y
Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
por carrera y el total general de participantes. Utilice bucles anidados.
'''

import os

def RegistroParticipacionEstudiantil():
 os.system("cls")
print("🎯 Registro de Participación Estudiantil - UAM 🎯")
print("..................................................")
print(" (Ingrese el número de estudiantes que participaron \n en cada actividad por carrera, año y sección)")
print("..................................................")


carreras = ["Sistemas", "Marketing", "Derecho"]
años = ["1er Año", "2do Año", "3er Año"]
secciones = ["A", "B"]

# Creamos un diccionario anidado para registrar participación
participacion = {
    carrera: {
        año: {seccion: 0 for seccion in secciones}
        for año in años
    }
    for carrera in carreras
}

# Recorremos las carreras, los años y las secciones para pedir datos
for carrera in carreras:
    print(f"\n📚 Carrera: {carrera}")
    for año in años:
        print(f"  📘 {año}")
        for seccion in secciones:
            while True:
                try:
                    cantidad = int(input(f"    - Sección {seccion}, Participantes: "))
                    if cantidad < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("    ❌ Por favor, ingrese un número entero válido (no negativo).")
            participacion[carrera][año][seccion] += cantidad

print("\n¿Desea ver el resumen de participación? (s/n):")
respuesta = input().strip().lower()

while True:
    if respuesta == "s":
        print("\n📊 RESUMEN DE PARTICIPACIÓN 📋")

        totalGeneral = 0
        for carrera in carreras:
            totalCarrera = 0
            print(f"\n🔸 Carrera: {carrera}")
            for año in años:
                for seccion in secciones:
                    cantidad = participacion[carrera][año][seccion]
                    print(f"  - {año} Sección {seccion}: {cantidad} participantes")
                    totalCarrera += cantidad
            print(f"✅ Total en {carrera}: {totalCarrera} estudiantes")
            totalGeneral += totalCarrera

        print(f"\n📦 Total general de participantes: {totalGeneral} estudiantes")
        print("\nGracias por registrar la participación estudiantil. 👏")
        break

    elif respuesta == "n":
        print("\n❌ No se mostrará el resumen de participación.")
        break

    else:
        print("\n❌ Respuesta no válida. Por favor, ingrese 's' o 'n'.")
        respuesta = input("¿Desea ver el resumen de participación? (s/n): ").strip().lower()

