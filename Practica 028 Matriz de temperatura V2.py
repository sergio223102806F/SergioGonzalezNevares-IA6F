# -*- coding: utf-8 -*-
"""

@author: elvin
"""

import random  # Importa el módulo random para generar números aleatorios.

# Función para generar la matriz de temperaturas
def generar_temperaturas(dias=31, horas=24):
    # Crea una matriz bidimensional (lista de listas) con temperaturas aleatorias.
    # Cada fila representa un día, y cada columna representa una hora.
    # random.uniform(15.0, 35.0) genera un número aleatorio entre 15.0 y 35.0.
    # round(..., 1) redondea el número a 1 decimal.
    return [[round(random.uniform(15.0, 35.0), 1) for h in range(horas)] for d in range(dias)]

# Función para imprimir la matriz de temperaturas
def imprimir_temperaturas(temps):
    print("Matriz de temperaturas (Día x Hora):")  # Imprime un título.
    # Recorre cada fila (día) de la matriz junto con su índice (empezando desde 1).
    for dia, temperaturas in enumerate(temps, start=1):
        # Imprime las temperaturas del día actual, separadas por comas.
        print(f"Día {dia}: {', '.join(f'{temp:.1f}°C' for temp in temperaturas)}")

# Función para calcular el promedio al mediodía
def calcular_promedio_mediodia(temps):
    # Suma las temperaturas al mediodía (hora 11, índice 11 en la lista).
    total = sum(dia[11] for dia in temps)
    # Calcula el promedio dividiendo la suma total entre el número de días (31).
    return total / len(temps)

# Programa principal
if __name__ == "__main__":
    # Generar la matriz de temperaturas llamando a la función generar_temperaturas.
    temps = generar_temperaturas()
    
    # Imprimir la matriz de temperaturas llamando a la función imprimir_temperaturas.
    imprimir_temperaturas(temps)
    
    # Calcular el promedio al mediodía llamando a la función calcular_promedio_mediodia.
    promedio = calcular_promedio_mediodia(temps)
    # Imprimir el resultado del promedio, redondeado a 1 decimal.
    print("\nTemperatura promedio al mediodía:", round(promedio, 1), "°C")