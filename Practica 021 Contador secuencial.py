# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:58:08 2025

@author: elvin
"""

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

numeros_impares = 0  # Contador para números impares
numeros_pares = 0    # Contador para números pares

# Leer el primer número.
numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el primer número

# 0 termina la ejecución.
while numero != 0:                                                  # Bucle mientras el número no sea 0
    # Verificar si el número es impar.
    if numero % 2 == 1:                                             # Si el número es impar
        # Incrementar el contador de números impares.
        numeros_impares += 1                                        # Aumenta el contador de impares
    else:                                                           # Si el número es par
        # Incrementar el contador de números pares.
        numeros_pares += 1                                          # Aumenta el contador de pares
    # Leer el siguiente número.
    numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el siguiente número

# Imprimir los resultados.
print("Cantidad de números impares:", numeros_impares)              # Muestra en pantalla la cantidad de impares
print("Cantidad de números pares:", numeros_pares)                  # Muestra en pantalla la cantidad de pares

# Calcular la suma total de números ingresados
suma_total = numeros_impares + numeros_pares                        # Suma total de números ingresados
print("Total de números ingresados:", suma_total)                   # Muestra en pantalla el total de números

# Calcular el porcentaje de números impares
if suma_total > 0:                                                  # Verifica si se ingresaron números
    porcentaje_impares = (numeros_impares / suma_total) * 100       # Calcula el porcentaje de impares
    print("Porcentaje de números impares:", round(porcentaje_impares, 2), "%")  # Muestra el porcentaje de impares
else:
    print("No se ingresaron números para calcular el porcentaje.")  # Mensaje si no se ingresaron números

# Calcular el porcentaje de números pares
if suma_total > 0:                                                  # Verifica si se ingresaron números
    porcentaje_pares = (numeros_pares / suma_total) * 100           # Calcula el porcentaje de pares
    print("Porcentaje de números pares:", round(porcentaje_pares, 2), "%")  # Muestra el porcentaje de pares
else:
    print("No se ingresaron números para calcular el porcentaje.")  # Mensaje si no se ingresaron números

# Encontrar el número más grande ingresado
if suma_total > 0:                                                  # Verifica si se ingresaron números
    numero_mayor = float('-inf')                                    # Inicializa el número mayor con un valor muy pequeño
    numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el primer número
    while numero != 0:                                              # Bucle mientras el número no sea 0
        if numero > numero_mayor:                                   # Compara el número con el mayor actual
            numero_mayor = numero                                   # Actualiza el número mayor
        numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el siguiente número
    print("El número más grande ingresado es:", numero_mayor)       # Muestra en pantalla el número mayor
else:
    print("No se ingresaron números para encontrar el mayor.")      # Mensaje si no se ingresaron números

# Encontrar el número más pequeño ingresado
if suma_total > 0:                                                  # Verifica si se ingresaron números
    numero_menor = float('inf')                                     # Inicializa el número menor con un valor muy grande
    numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el primer número
    while numero != 0:                                              # Bucle mientras el número no sea 0
        if numero < numero_menor:                                   # Compara el número con el menor actual
            numero_menor = numero                                   # Actualiza el número menor
        numero = int(input("Ingresa un número o escribe 0 para detener: "))  # Solicita el siguiente número
    print("El número más pequeño ingresado es:", numero_menor)      # Muestra en pantalla el número menor
else:
    print("No se ingresaron números para encontrar el menor.")      # Mensaje si no se ingresaron números