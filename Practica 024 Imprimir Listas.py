# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:43:38 2025

@author: elvin
"""

# Definir una lista de números
numeros = [10, 5, 7, 2, 1]

# Imprimir el contenido original de la lista
print("Contenido original de la lista:", numeros)    # Mostrar el contenido original de la lista.

# Cambiar el valor del primer elemento de la lista (índice 0) a 111
numeros[0] = 111
# Imprimir el contenido actualizado de la lista
print("\nContenido anterior de la lista:", numeros)  # Mostrar el contenido anterior de la lista.

# Copiar el valor del quinto elemento (índice 4) al segundo elemento (índice 1)
numeros[1] = numeros[4]
# Imprimir el contenido actualizado de la lista
print("Contenido anterior de la lista:", numeros)    # Mostrar el contenido anterior de la lista.

# Imprimir la longitud de la lista
print("\nLongitud de la lista:", len(numeros))       # Mostrar la cantidad de elementos en la lista.

#Version 2
# Definir una lista de números
numeros = [10, 5, 7, 2, 1]                           # Crear una lista con valores iniciales

# Imprimir el contenido original de la lista
print("Contenido original de la lista:", numeros)    # Mostrar el contenido original de la lista

# Cambiar el valor del primer elemento de la lista (índice 0) a 111
numeros[0] = 111                                     # Modificar el primer elemento de la lista
print("\nContenido anterior de la lista:", numeros)  # Mostrar el contenido actualizado de la lista

# Copiar el valor del quinto elemento (índice 4) al segundo elemento (índice 1)
numeros[1] = numeros[4]                              # Copiar el valor del quinto elemento al segundo
print("Contenido anterior de la lista:", numeros)    # Mostrar el contenido actualizado de la lista

# Imprimir la longitud de la lista
print("\nLongitud de la lista:", len(numeros))       # Mostrar la cantidad de elementos en la lista