# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:40:29 2025

@author: elvin
"""

# Función para validar que el usuario ingrese un número entero positivo
def obtener_bloques():
    while True:
        try:
            bloques = int(input("Ingresa el número de bloques: "))
            if bloques > 0:
                return bloques
            else:
                print("Por favor, ingresa un número mayor que 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

# Función para calcular la altura de la pirámide y los bloques sobrantes
def calcular_piramide(bloques):
    altura = 0
    bloques_capa = 1
    while bloques >= bloques_capa:
        bloques -= bloques_capa
        altura += 1
        bloques_capa += 1
    return altura, bloques

# Función para dibujar la pirámide
def dibujar_piramide(altura):
    for i in range(1, altura + 1):
        # Imprime espacios para centrar la pirámide
        print(" " * (altura - i), end="")
        # Imprime los bloques de la capa actual
        print("[]" * i)

# Programa principal
bloques = obtener_bloques()  # Obtener el número de bloques válido
altura, sobrantes = calcular_piramide(bloques)  # Calcular altura y bloques sobrantes

# Mostrar resultados
print("\nResultados:")
print(f"La altura de la pirámide es: {altura}")
print(f"Bloques sobrantes: {sobrantes}")

# Dibujar la pirámide si se pudo construir
if altura > 0:
    print("\nAsí se vería tu pirámide:")
    dibujar_piramide(altura)
else:
    print("No hay suficientes bloques para construir una pirámide.")