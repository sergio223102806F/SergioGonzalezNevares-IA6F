# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:50:23 2025

@author: elvin
"""

# Solicitar al usuario que ingrese las longitudes de los catetos
cateto_a = float(input("Ingresa la longitud del primer cateto: "))  # Primer cateto
cateto_b = float(input("Ingresa la longitud del segundo cateto: ")) # Segundo cateto

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5                  # Fórmula de Pitágoras

# Mostrar el resultado
print("La longitud de la hipotenusa es", hipotenusa)              # Imprime la hipotenusa

# Solicitar al usuario que ingrese el radio de un círculo
radio = float(input("Ingresa el radio del círculo: "))            # Radio del círculo

# Calcular el área del círculo
area = 3.1416 * radio**2                                         # Fórmula del área del círculo

# Mostrar el resultado
print("El área del círculo es", area)                             # Imprime el área del círculo

# Solicitar al usuario que ingrese la base y la altura de un triángulo
base = float(input("Ingresa la base del triángulo: "))            # Base del triángulo
altura = float(input("Ingresa la altura del triángulo: "))        # Altura del triángulo

# Calcular el área del triángulo
area_triangulo = (base * altura) / 2                             # Fórmula del área del triángulo

# Mostrar el resultado
print("El área del triángulo es", area_triangulo)                # Imprime el área del triángulo

# Solicitar al usuario que ingrese el lado de un cuadrado
lado = float(input("Ingresa el lado del cuadrado: "))             # Lado del cuadrado

# Calcular el área del cuadrado
area_cuadrado = lado**2                                          # Fórmula del área del cuadrado

# Mostrar el resultado
print("El área del cuadrado es", area_cuadrado)                  # Imprime el área del cuadrado

# Solicitar al usuario que ingrese el largo y el ancho de un rectángulo
largo = float(input("Ingresa el largo del rectángulo: "))         # Largo del rectángulo
ancho = float(input("Ingresa el ancho del rectángulo: "))        # Ancho del rectángulo

# Calcular el área del rectángulo
area_rectangulo = largo * ancho                                  # Fórmula del área del rectángulo

# Mostrar el resultado
print("El área del rectángulo es", area_rectangulo)              # Imprime el área del rectángulo

# Solicitar al usuario que ingrese el radio de una esfera
radio_esfera = float(input("Ingresa el radio de la esfera: "))   # Radio de la esfera

# Calcular el volumen de la esfera
volumen_esfera = (4/3) * 3.1416 * radio_esfera**3               # Fórmula del volumen de la esfera

# Mostrar el resultado
print("El volumen de la esfera es", volumen_esfera)              # Imprime el volumen de la esfera

# Solicitar al usuario que ingrese la longitud de un lado de un cubo
lado_cubo = float(input("Ingresa la longitud de un lado del cubo: "))  # Lado del cubo

# Calcular el volumen del cubo
volumen_cubo = lado_cubo**3                                      # Fórmula del volumen del cubo

# Mostrar el resultado
print("El volumen del cubo es", volumen_cubo)                    # Imprime el volumen del cubo

# Solicitar al usuario que ingrese la base y la altura de un paralelogramo
base_paralelogramo = float(input("Ingresa la base del paralelogramo: "))  # Base del paralelogramo
altura_paralelogramo = float(input("Ingresa la altura del paralelogramo: "))  # Altura del paralelogramo

# Calcular el área del paralelogramo
area_paralelogramo = base_paralelogramo * altura_paralelogramo   # Fórmula del área del paralelogramo

# Mostrar el resultado
print("El área del paralelogramo es", area_paralelogramo)        # Imprime el área del paralelogramo

# Solicitar al usuario que ingrese la base mayor, la base menor y la altura de un trapecio
base_mayor = float(input("Ingresa la base mayor del trapecio: "))  # Base mayor del trapecio
base_menor = float(input("Ingresa la base menor del trapecio: "))  # Base menor del trapecio
altura_trapecio = float(input("Ingresa la altura del trapecio: ")) # Altura del trapecio

# Calcular el área del trapecio
area_trapecio = ((base_mayor + base_menor) / 2) * altura_trapecio  # Fórmula del área del trapecio

# Mostrar el resultado
print("El área del trapecio es", area_trapecio)                  # Imprime el área del trapecio
