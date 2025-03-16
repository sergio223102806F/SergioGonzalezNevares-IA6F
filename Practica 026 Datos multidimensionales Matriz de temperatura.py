# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 16:21:54 2025

@author: elvin
"""

import random  # Importar el módulo random para generar números aleatorios

# Función para imprimir la matriz de temperaturas de manera legible
def imprimir_temperaturas(temps):                                                                 # Definir la función para imprimir temperaturas
    print("Matriz de temperaturas (Día x Hora):")                                                 # Mostrar el encabezado de la matriz
    for dia, temperaturas in enumerate(temps, start=1):                                           # Iterar sobre cada día y sus temperaturas
        print(f"Día {dia}: {', '.join(f'{temp:.1f}°C' for temp in temperaturas)}")                # Mostrar las temperaturas del día

# Crear una matriz bidimensional para almacenar las temperaturas
# La matriz tiene 31 filas (días) y 24 columnas (horas)
# Se llena con valores aleatorios entre 15.0 y 35.0 °C, redondeados a 1 decimal
temps = [[round(random.uniform(15.0, 35.0), 1) for h in range(24)] for d in range(31)]            # Generar la matriz de temperaturas aleatorias

# Imprimir la matriz de temperaturas (opcional, para ver los datos)
imprimir_temperaturas(temps)                                                                      # Llamar a la función para imprimir la matriz

# Inicializar una variable para almacenar la suma de temperaturas al mediodía
total = 0.0                                                                                       # Inicializar la variable para la suma total

# Recorrer cada fila (día) de la matriz
for dia in temps:                                                                                 # Iterar sobre cada día en la matriz
    total += dia[11]                                                                              # Sumar la temperatura al mediodía (hora 11)

# Calcular el promedio de temperatura al mediodía
promedio = total / 31                                                                             # Calcular el promedio de temperaturas

# Imprimir el resultado
print("\nTemperatura promedio al mediodía:", round(promedio, 1), "°C")                            # Mostrar el promedio redondeado a 1 decimal