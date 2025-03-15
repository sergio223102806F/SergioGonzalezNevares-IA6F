# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:40:29 2025

@author: elvin
"""

# Leer el número de bloques del usuario
bloques = int(input("Ingresa el número de bloques: "))

altura = 0  # Inicializar la altura de la pirámide
bloques_capa = 1  # Inicializar el número de bloques necesarios para la capa actual

# Calcular la altura de la pirámide
while bloques >= bloques_capa:
    bloques -= bloques_capa  # Restar los bloques usados en la capa actual
    altura += 1  # Incrementar la altura
    bloques_capa += 1  # Aumentar los bloques necesarios para la siguiente capa

# Imprimir el resultado
print("La altura de la pirámide:", altura)