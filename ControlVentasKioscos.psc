//Autores: Jesy Nicole González Jarquín, Marian Alejandra Guillén Castillo y Nora Maria Obregón Membreño
//Fecha: 20/05/2025
//Versión 1.0
//Descripción: Caso 4: Control de ventas en kioscos estudiantiles de la UAM. Implemente un programa que simule el control de ventas de alimentos 
//diferentes y se registrarán las ventas durante cuatro días. El programa debe calcular y mostrar el total vendido por producto en cada
//kiosco, así como el total general por día.
	Algoritmo ControlVentasKioscos
		//Definimos variables y dimesionamos
		Definir ventas Como Entero
		Definir nombresKiosco Como Cadena
		Definir nombresProducto Como Cadena
		Definir i, j, k, cantidad, total_dia Como Entero
		Definir respuesta Como Cadena
		
		Dimension ventas[4,3,5]
		Dimension nombresKiosco[3]
		Dimension nombresProducto[5]
		
		//Indicamos que i es = 3 ( Dias) j es = 2 (kiosco) k = (Productos)
		Para i = 0 Hasta 3 Hacer
			
			Para j = 0 Hasta 2 Hacer
				
				Para k = 0 Hasta 4 Hacer
					
					ventas[i,j,k] = 0
				FinPara
			FinPara
		FinPara
		//Agregamos nombres para los llamados
		nombresKiosco[0] = "Kiosco 1"
		nombresKiosco[1] = "Kiosco 2"
		nombresKiosco[2] = "Kiosco 3"
		
		nombresProducto[0] = "Tacos" 
		nombresProducto[1] = "Bebidas"
		nombresProducto[2] = "Snacks"
		nombresProducto[3] = "Galletas"
		nombresProducto[4] = "Frutas"
		
		Escribir "$$ Control de Ventas en Kioscos Estudiantiles UAM $$"
		Escribir "...................................................."
		Escribir "  (En este programa puede ingresar la cantidad de"
		Escribir "   productos vendidos por kiosco, categoría y día)"
		Escribir "...................................................."
		
		//Bucle para repetir los 4 dias y sumar los productos
		Para i = 0 Hasta 3 Hacer
			
			
			Escribir "Día ", i+1
			Para j = 0 Hasta 2 Hacer
				
				
				Escribir nombresKiosco[j]
				Escribir "Productos disponibles:"
				Para k = 0 Hasta 4 Hacer
					
					Escribir "  - ", nombresProducto[k]
					Repetir
						Escribir "Digite la cantidad vendida de ", nombresProducto[k], ": "
						Leer cantidad
						Si cantidad < 0 Entonces
							Escribir "Por favor, ingrese un número entero válido (no negativo)."
						FinSi
					Hasta Que cantidad >= 0
					ventas[i,j,k] <- ventas[i,j,k] + cantidad
				FinPara
			FinPara
		FinPara
		
	
		Escribir "¿Quiere ver el resumen de ventas? (s/n):"
		Leer respuesta
		
		Si Minusculas(respuesta) = "s" Entonces
			
			Escribir "## Resumen de ventas por kiosco y producto:"
			// Bucle para ver los 4 dias y su resumen de venta 
			Para i <- 0 Hasta 3 Hacer
				
				
				Escribir "## Día ", i+1
				total_dia = 0
				Para j = 0 Hasta 2 Hacer
					
					
					Escribir nombresKiosco[j]
					Para k <- 0 Hasta 4 Hacer
						
						Escribir "  - ", nombresProducto[k], ": ", ventas[i,j,k], " unidades vendidas"
						total_dia = total_dia + ventas[i,j,k]
					FinPara
				FinPara
				
				Escribir "## Total general vendido en Día ", i+1, ": ", total_dia, " unidades"
			FinPara
		FinSi
FinAlgoritmo
