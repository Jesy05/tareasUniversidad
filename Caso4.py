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
    dias = [f"Día {i}" for i in range(1, 5)] # esto es una lista para manejar los días

    # aquí vamos a guardar todas las ventas por día, por kiosco y por producto
    ventas = {
        dia: {kiosco: {producto: 0 for producto in productos} for kiosco in kioscos}
        for dia in dias # esto es un diccionario para manejar los días por eso los simbolos de {} y a como 
        # acostumbramos iniciamos en 0 para que no haya problemas al momento de sumar
    }

    for dia in dias:
        print(f"\n{dia}") # el scape para que se vea más ordenado
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
                # y al total general

    print("\n¿Quiere ver el resumen de ventas? (s/n):")
    respuesta = input().strip().lower() # la entrada la pedimos con el strip para quitar espacios
    # y lower para que no importe si lo escriben en mayúscula o minúscula

    while True:
        if respuesta == "s":
            print("\n🧾 Resumen de ventas por kiosco y producto:")
            for dia in dias:
                print(f"\n📅 {dia}")
                total_dia = 0
                for kiosco in kioscos:
                    print(f"\n{kiosco}")
                    for producto in productos:
                        cantidad = ventas[dia][kiosco][producto]
                        print(f"  - {producto}: {cantidad} unidades vendidas")
                        total_dia += cantidad
                print(f"\n📦 Total general vendido en {dia}: {total_dia} unidades")
            break
        elif respuesta == "n":
            print("\n❌ Respuesta no válida. Por favor, ingrese 's' o 'n'.")
            respuesta = input("¿Quiere ver el resumen de ventas? (s/n): ").strip().lower()
            break

if __name__ == "__main__":
    ControlVentasKioscos()
