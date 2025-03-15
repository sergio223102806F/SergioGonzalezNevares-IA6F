# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:50:23 2025

@author: elvin
"""

# Solicitar al usuario que ingrese las longitudes de los catetos
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

# Mostrar el resultado
print("La longitud de la hipotenusa es", hipotenusa)

