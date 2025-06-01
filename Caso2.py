'''
Autores: 
         Marian Alejandra Guillén Castillo
         Nora Maria Obregón Membreño
         Jesy Nicole González Jarquín

Fecha: 01/06/2025
Versión: (Versionado por GitHub)

Descripción: 

Caso 2: Cálculo de promedio académico en la UAM
Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.
'''

import os

def CalculoPromedioAcademico():
    os.system("cls")
    print("🎓 Cálculo de Promedio Académico en la UAM 🎓")
    print("..................................................")
    print("  (Este programa calcula promedios por asignatura\n   y promedio general por estudiante)")
    print("..................................................")

    estudiantes = [] # Lista vacia para almacenar los datos de los estudiantes
    asignaturas = ["Matemática", "Programación", "Redes"] # Lista de asignaturas que se van a manejar
    evaluaciones = ["Tarea 1", "Tarea 2", "Tarea 3", "Examen"] # Lista de evaluaciones que se van a manejar

    while True:
        nombreEstudiante = input("\nIngrese el nombre del estudiante (o escriba 'fin' para terminar): ").strip()
        if nombreEstudiante.strip().lower() == 'fin': #con strip() y lower por cualquier entrada rara
            break
        
        calificaciones = {}  # Diccionario para guardar las notas por asignatura

        
        print(f"\n📚 Ingresando calificaciones para {nombreEstudiante} 📚")
        for asignatura in asignaturas:
            print(f"\nAsignatura: {asignatura}")
            notas = [] # Lista para almacenar las notas

            # Bucle para ingresar las notas de cada evaluación
            for evaluacion in evaluaciones:
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota de {evaluacion} (0-100): "))
                        if nota < 0 or nota > 100: #para validar que la nota esté entre 0 y 100
                            raise ValueError
                        break
                    except ValueError:
                        print("❌ Por favor, ingrese un número válido entre 0 y 100.")
                notas.append(nota) # Agregamos la nota a la lista de notas

            promedioAsignatura = sum(notas) / len(notas) # Calculamos el promedio de la asignatura
            # Guardamos las notas y el promedio en el diccionario de calificaciones
            calificaciones[asignatura] = { 
                "notas": notas,
                "promedio": promedioAsignatura
            } #con esto se logra que lo que se guardo notas y el promedio se guarde dentro del diccionario de calificaciones

        estudiantes.append({
            "nombre": nombreEstudiante,
            "calificaciones": calificaciones
        }) #aca es donde se guarda el nombre del estudiante y sus calificaciones en la lista de estudiantes
    # Fin del ingreso de datos

    print("\n¿Desea ver el resumen de promedios? (s/n):")
    respuesta = input().strip().lower()

    while True:
        if respuesta == "s":
            print("\n🧾 RESUMEN DE PROMEDIOS 🧾")

            for estudiante in estudiantes:
                print(f"\n👤 Estudiante: {estudiante['nombre']}")
                sumaPromedios = 0

                for asignatura in asignaturas:
                    promedio = estudiante["calificaciones"][asignatura]["promedio"]
                    print(f"  - {asignatura}: {promedio:.2f}")
                    sumaPromedios += promedio

                promedioGeneral = sumaPromedios / len(asignaturas)
                print(f"Promedio general: {promedioGeneral:.2f}")

            print("\nGracias por usar el sistema de cálculo académico./n ")
            break
        elif respuesta == "n":
            print("\n❌ No se mostrará el resumen de promedios.")
            break
        else:
            print("\n❌ Respuesta no válida. Por favor, ingrese 's' o 'n'.")
            respuesta = input("¿Desea ver el resumen de promedios? (s/n): ").strip().lower()


if __name__ == "__main__":
    CalculoPromedioAcademico()
