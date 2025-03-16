# -*- coding: utf-8 -*-
"""
@author: elvin
"""
import numpy as np                                                              # Importa la biblioteca NumPy para manejar matrices y cálculos numéricos

# Crear una matriz de temperaturas con valores aleatorios entre 15.0 y 35.0 °C
# np.random.uniform(15.0, 35.0, (31, 24)) genera una matriz de 31 filas (días) y 24 columnas (horas)
# np.round(..., 1) redondea todos los valores de la matriz a 1 decimal
temps = np.round(np.random.uniform(15.0, 35.0, (31, 24)), 1)                    # Generar la matriz de temperaturas aleatorias

# Imprimir la matriz de temperaturas (opcional)
print("Matriz de temperaturas (Día x Hora):")                                   # Imprimir un título
# Recorre cada fila (día) de la matriz junto con su índice (empezando desde 1)
for dia, temperaturas in enumerate(temps, start=1):                             # Iterar sobre cada día y sus temperaturas
    print(f"Día {dia}: {', '.join(f'{temp:.1f}°C' for temp in temperaturas)}")  # Imprimir las temperaturas del día actual

# Calcular el promedio de temperatura al mediodía (hora 11)
# temps[:, 11] selecciona todas las filas (días) y la columna 11 (hora 12)
# np.mean(...) calcula el promedio de los valores seleccionados
promedio = np.mean(temps[:, 11])                                                # Calcular el promedio de temperaturas al mediodía

# Imprimir el resultado del promedio, redondeado a 1 decimal
print("\nTemperatura promedio al mediodía:", round(promedio, 1), "°C")          # Mostrar el promedio redondeado a 1 decimal

