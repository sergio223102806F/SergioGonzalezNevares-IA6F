# -*- coding: utf-8 -*-
"""

@author: elvin
"""

import random  # Importa el módulo random para generar números aleatorios.

class Temperaturas:
    def __init__(self, dias=31, horas=24):
        # Inicializa los atributos de la clase: número de días y horas.
        self.dias = dias
        self.horas = horas
        # Genera la matriz de temperaturas llamando al método generar_temperaturas.
        self.temps = self.generar_temperaturas()

    # Método para generar la matriz de temperaturas
    def generar_temperaturas(self):
        # Crea una matriz bidimensional (lista de listas) con temperaturas aleatorias.
        # random.uniform(15.0, 35.0) genera un número aleatorio entre 15.0 y 35.0.
        # round(..., 1) redondea el número a 1 decimal.
        return [[round(random.uniform(15.0, 35.0), 1) for h in range(self.horas)] for d in range(self.dias)]

    # Método para imprimir la matriz de temperaturas
    def imprimir_temperaturas(self):
        print("Matriz de temperaturas (Día x Hora):")  # Imprime un título.
        # Recorre cada fila (día) de la matriz junto con su índice (empezando desde 1).
        for dia, temperaturas in enumerate(self.temps, start=1):
            # Imprime las temperaturas del día actual, separadas por comas.
            print(f"Día {dia}: {', '.join(f'{temp:.1f}°C' for temp in temperaturas)}")

    # Método para calcular el promedio al mediodía
    def calcular_promedio_mediodia(self):
        # Suma las temperaturas al mediodía (hora 11, índice 11 en la lista).
        total = sum(dia[11] for dia in self.temps)
        # Calcula el promedio dividiendo la suma total entre el número de días (31).
        return total / self.dias

# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase Temperaturas.
    temps = Temperaturas()
    
    # Imprimir la matriz de temperaturas llamando al método imprimir_temperaturas.
    temps.imprimir_temperaturas()
    
    # Calcular el promedio al mediodía llamando al método calcular_promedio_mediodia.
    promedio = temps.calcular_promedio_mediodia()
    # Imprimir el resultado del promedio, redondeado a 1 decimal.
    print("\nTemperatura promedio al mediodía:", round(promedio, 1), "°C")