# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 16:21:54 2025

@author: elvin
"""

import random

# Función para imprimir la matriz de temperaturas de manera legible
def imprimir_temperaturas(temps):
    print("Matriz de temperaturas (Día x Hora):")
    for dia, temperaturas in enumerate(temps, start=1):
        print(f"Día {dia}: {', '.join(f'{temp:.1f}°C' for temp in temperaturas)}")

# Crear una matriz bidimensional para almacenar las temperaturas
# La matriz tiene 31 filas (días) y 24 columnas (horas)
# Se llena con valores aleatorios entre 15.0 y 35.0 °C, redondeados a 1 decimal
temps = [[round(random.uniform(15.0, 35.0), 1) for h in range(24)] for d in range(31)]

# Imprimir la matriz de temperaturas (opcional, para ver los datos)
imprimir_temperaturas(temps)

# Inicializar una variable para almacenar la suma de temperaturas al mediodía
total = 0.0

# Recorrer cada fila (día) de la matriz
for dia in temps:
    # Sumar la temperatura registrada al mediodía (hora 11, ya que la lista comienza en 0)
    total += dia[11]

# Calcular el promedio de temperatura al mediodía
promedio = total / 31

# Imprimir el resultado
print("\nTemperatura promedio al mediodía:", round(promedio, 1), "°C")