# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:21:09 2025

@author: elvin
"""

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

numeros_impares = 0  # Contador para números impares
numeros_pares = 0    # Contador para números pares

# Leer el primer número.
numero = int(input("Ingresa un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares.
        numeros_impares += 1
    else:
        # Incrementar el contador de números pares.
        numeros_pares += 1
    # Leer el siguiente número.
    numero = int(input("Ingresa un número o escribe 0 para detener: "))

# Imprimir los resultados.
print("Cantidad de números impares:", numeros_impares)
print("Cantidad de números pares:", numeros_pares)
