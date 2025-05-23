'''
Autores: Jesy Nicole González Jarquín
         Marian Alejandra Guillén Castillo
         Nora Maria Obregón Membreño
Fecha: 20/05/2025
Versión: (Versionado por github)

Descripción: 

Caso 4: Control de ventas en kioscos estudiantiles de la UAM
Implemente un programa que simule el control de ventas de alimentos 
en tres kioscos dentro del campus UAM. Cada kiosco ofrece cinco productos 
diferentes y se registrarán las ventas durante cuatro días. El programa debe 
calcular y mostrar el total vendido por producto en cada
kiosco, así como el total general por día. 


'''
import os

def ControlVentasKioscos():
    os.system("cls")
    print("📊 Control de Ventas en Kioscos Estudiantiles UAM 📊")
    print("....................................................")
    print("  (En este programa puede ingresar la cantidad de \n  productos vendidos por kiosco, categoría y día)")
    print("....................................................")

    # Acá inicializamos las listas y diccionarios para manejar los kioscos y productos
    # y sus cantidades vendidas
    kioscos = ["Kiosco 1", "Kiosco 2", "Kiosco 3"] # esto entre los [] es una lista para manejar kioscos
    productos = ["Tacos", "Bebidas", "Snacks", "Galletas", "Frutas"] # esto entre los [] es una lista para manejar productos
    dias = [f"Día {i}" for i in range(1, 5)] # esto es una lista para manejar los días, del día 1 al día 4

    # En este bloque vamos a guardar todas las ventas por día, por kiosco y por producto

    #primero creamos los espacios para guardar esos datos
    ventas = { # ventas es un diccionario que va a manejar los días y dentro de cada día va a manejar los kioscos
        dia: {kiosco: {producto: 0 for producto in productos} for kiosco in kioscos} 
        # Al principio, todas las cantidades vendidas serán cero, por eso inicializamos con 0
        # y basicamente hay 4 niveles de diccionarios
        for dia in dias # Para cada elemento que haya en la lista dias, voy a hacer algo, 
        #y durante cada vuelta, ese día se va a guardar en la variable dia    
    }

    #así, en estructura anidada y no en diccionarios separados porque así están 
    # conectados los datos y no hay problemas al momento de sumar, también es para 
    # no tener que repetir claves y hacer búsquedas redundantes.


    # Acá vamos a pedirle al usuario que ingrese la cantidad de productos vendidos por kiosco
    for dia in dias:
        print(f"\n{dia}") # el scape para que se vea más ordenado y el f-string para meter variables dentro de un string
        # ahí va a ir imprimiendo el día en el que se encuentra mientras va iterando gracias al for de arriba,
        for kiosco in kioscos: # iteramos sobre cada kiosco que tenemos en la lista kioscos
            print(f"\n{kiosco}") # imprimimos el nombre de cada kiosco
            print("Productos disponibles:")
            for producto in productos: # igual que arriba, iteramos sobre los productos
                print(f"  - {producto}") # imprimimos el nombre de cada producto
                while True: # bucle para validar la entrada
                    try: # el try para poder usar ValueError y manejar errores si dijita algo que no es
                        cantidad = int(input(f"Digite la cantidad vendida de {producto}: "))
                        if cantidad < 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Por favor, ingrese un número entero válido (no negativo).")
                ventas[dia][kiosco][producto] += cantidad # sumamos la cantidad vendida al total del kiosco
                # y al total general # con los [] se accede a los elementos de los diccionarios

    print("\n¿Quiere ver el resumen de ventas? (s/n):")
    respuesta = input().strip().lower() # la entrada la pedimos con el strip para quitar espacios
    # y lower para que no importe si lo escriben en mayúscula o minúscula

    while True:
        if respuesta == "s":
            print("\n🧾 RESUMEN DE VENTAS 📊")

            # Total de productos vendidos por kiosco (sumando todos los días)
            print("\n🏪 Total de productos vendidos por kiosco (en 4 días):")
            for kiosco in kioscos:
                total_kiosco = 0
                for dia in dias:
                    for producto in productos:
                        total_kiosco += ventas[dia][kiosco][producto]
                print(f"  - {kiosco}: {total_kiosco} unidades") # primero {kiosco} que es donde se cuardo kiosco1 etc...
                # y despues el total de productos vendidos en ese kiosco

            # Total de productos vendidos por tipo (sumando todos los kioscos y días)
            print("\n🍔 Total de productos vendidos por tipo:")
            for producto in productos:
                total_producto = 0
                for dia in dias:
                    for kiosco in kioscos:
                        total_producto += ventas[dia][kiosco][producto]
                print(f"  - {producto}: {total_producto} unidades")

            # Total general de todas las ventas
            total_general = 0
            for dia in dias:
                for kiosco in kioscos:
                    for producto in productos:
                        total_general += ventas[dia][kiosco][producto]
            print(f"\n📦 Total general de ventas: {total_general} unidades")
            print("\nGracias por usar el programa de control de ventas. ¡Hasta luego! 👋")
            break  # Terminamos el bucle después de mostrar el resumen
        elif respuesta == "n":
            print("\n❌ No se mostrará el resumen de ventas.")
            break  # Salimos del bucle si no quiere ver el resumen

        else:
            print("\n❌ Respuesta no válida. Por favor, ingrese 's' o 'n'.")
            respuesta = input("¿Quiere ver el resumen de ventas? (s/n): ").strip().lower()


if __name__ == "__main__":
    ControlVentasKioscos()
