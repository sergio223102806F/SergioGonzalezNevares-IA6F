# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:16:08 2025

@author: elvin
"""
#Variables dentro de Radicales
a = 3.0                                             #Variable Uno
b = 4.0                                             #Variable DOS
c = (a ** 2 + b ** 2) ** 0.5                        #Operacion Raiz
print("c =", c)                                     #Imprime el resultado
 

#Ejercicio John, Mary, Adam
# Paso 1: Asignar valores a las variables
john = 3
mary = 5
adam = 6

# Paso 2: Imprimir las variables en una línea, separadas por comas
print(john, mary, adam, sep=", ")

# Paso 3: Calcular el total de manzanas
total_apples = john + mary + adam

# Paso 4: Imprimir el total de manzanas
print(total_apples)

# Paso 5: Experimentar con nuevas variables y operaciones
new_john = 10
new_mary = 7
new_adam = 4

total_new_apples = new_john + new_mary + new_adam
diferencia = new_john - john
producto = new_mary * adam
division = new_adam / mary
division_entera = new_john // john

# Imprimir los resultados de los experimentos
print("Total de nuevas manzanas:", total_new_apples)
print("Diferencia entre el nuevo John y el viejo John:", diferencia)
print("Producto de la nueva Mary y el viejo Adam:", producto)
print("División del nuevo Adam por la vieja Mary:", division)
print("División entera del nuevo John por el viejo John:", division_entera)

# Imprimir una cadena de texto y un número entero juntos
print("Número total de manzanas:", total_apples)