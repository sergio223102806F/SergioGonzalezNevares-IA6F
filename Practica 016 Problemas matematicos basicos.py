# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:16:08 2025

@author: elvin
"""
# Variables dentro de Radicales
a = 3.0                                             # Variable Uno
b = 4.0                                             # Variable DOS
c = (a ** 2 + b ** 2) ** 0.5                        # Operación Raíz (Teorema de Pitágoras)
print("c =", c)                                     # Imprime el resultado de la raíz

# Ejercicio John, Mary, Adam
# Paso 1: Asignar valores a las variables
john = 3                                            # Manzanas de John
mary = 5                                            # Manzanas de Mary
adam = 6                                            # Manzanas de Adam

# Paso 2: Imprimir las variables en una línea, separadas por comas
print(john, mary, adam, sep=", ")                  # Imprime las manzanas separadas por comas

# Paso 3: Calcular el total de manzanas
total_apples = john + mary + adam                   # Suma de las manzanas

# Paso 4: Imprimir el total de manzanas
print(total_apples)                                 # Imprime el total de manzanas

# Paso 5: Experimentar con nuevas variables y operaciones
new_john = 10                                       # Nuevas manzanas de John
new_mary = 7                                        # Nuevas manzanas de Mary
new_adam = 4                                        # Nuevas manzanas de Adam

total_new_apples = new_john + new_mary + new_adam   # Suma de las nuevas manzanas
diferencia = new_john - john                        # Diferencia entre el nuevo John y el viejo John
producto = new_mary * adam                          # Producto de la nueva Mary y el viejo Adam
division = new_adam / mary                          # División del nuevo Adam por la vieja Mary
division_entera = new_john // john                  # División entera del nuevo John por el viejo John

# Imprimir los resultados de los experimentos
print("Total de nuevas manzanas:", total_new_apples)                  # Imprime el total de nuevas manzanas
print("Diferencia entre el nuevo John y el viejo John:", diferencia)  # Imprime la diferencia
print("Producto de la nueva Mary y el viejo Adam:", producto)         # Imprime el producto
print("División del nuevo Adam por la vieja Mary:", division)         # Imprime la división
print("División entera del nuevo John por el viejo John:", division_entera)  # Imprime la división entera

# Imprimir una cadena de texto y un número entero juntos
print("Número total de manzanas:", total_apples)    # Imprime el total de manzanas

# Operaciones adicionales con variables
promedio = (john + mary + adam) / 3                 # Calcula el promedio de manzanas
print("Promedio de manzanas:", promedio)            # Imprime el promedio

potencia = john ** mary                             # Calcula la potencia de john elevado a mary
print("Potencia de John elevado a Mary:", potencia) # Imprime la potencia

modulo = adam % john                                # Calcula el módulo de adam entre john
print("Módulo de Adam entre John:", modulo)         # Imprime el módulo

# Concatenación de cadenas y números
print("John tiene", john, "manzanas, Mary tiene", mary, "y Adam tiene", adam, "manzanas.")