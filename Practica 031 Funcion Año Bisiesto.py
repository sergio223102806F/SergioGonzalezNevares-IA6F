# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 17:55:12 2025

@author: elvin
"""

# Función para determinar si un año es bisiesto
def is_year_leap(year):
    # Si el año no es divisible por 4, no es bisiesto.
    if year % 4 != 0:
        return False
    # Si el año es divisible por 4 pero no por 100, es bisiesto.
    elif year % 100 != 0:
        return True
    # Si el año es divisible por 100 pero no por 400, no es bisiesto.
    elif year % 400 != 0:
        return False
    # Si el año es divisible por 400, es bisiesto.
    else:
        return True

# Lista de años para probar la función
test_data = [1900, 2000, 2016, 1987]
# Lista de resultados esperados para los años en test_data
test_results = [False, True, True, False]

# Recorre cada año en la lista test_data
for i in range(len(test_data)):
    # Obtiene el año actual de la lista test_data
    yr = test_data[i]
    # Imprime el año actual sin salto de línea (end="")
    print(yr, "-> ", end="")
    # Llama a la función is_year_leap para verificar si el año es bisiesto
    result = is_year_leap(yr)
    # Compara el resultado con el resultado esperado
    if result == test_results[i]:
        print("OK")  # Si coincide, imprime "OK"
    else:
        print("Failed")  # Si no coincide, imprime "Failed"