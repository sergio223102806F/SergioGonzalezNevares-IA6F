# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:46:53 2025

@author: elvin
"""

# Leer tres números ingresados por el usuario
numero1 = int(input("Ingresa el primer número: "))  # Solicita el primer número y lo convierte a entero
numero2 = int(input("Ingresa el segundo número: "))  # Solicita el segundo número y lo convierte a entero
numero3 = int(input("Ingresa el tercer número: "))   # Solicita el tercer número y lo convierte a entero

# Suponemos temporalmente que el primer número es el mayor.
# Esto lo verificaremos más adelante.
numero_mayor = numero1

# Verificamos si el segundo número es mayor que el número mayor actual
# y actualizamos el número mayor si es necesario.
if numero2 > numero_mayor:
    numero_mayor = numero2

# Verificamos si el tercer número es mayor que el número mayor actual
# y actualizamos el número mayor si es necesario.
if numero3 > numero_mayor:
    numero_mayor = numero3

# Imprimir el resultado
print("El número mayor es:", numero_mayor)  # Muestra en pantalla el número mayor