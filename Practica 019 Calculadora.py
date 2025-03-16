# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:09:29 2025

@author: elvin
"""

# Calculadora básica

# Solicitar al usuario que ingrese el primer valor y convertirlo a un número decimal
a = float(input("Ingresa el primer valor: "))        # Primer valor

# Solicitar al usuario que ingrese el segundo valor y convertirlo a un número decimal
b = float(input("Ingresa el segundo valor: "))      # Segundo valor

# Realizar y mostrar la suma de los dos valores
print("Suma:", a + b)                               # Imprime la suma de a y b

# Realizar y mostrar la resta de los dos valores
print("Resta:", a - b)                              # Imprime la resta de a y b

# Realizar y mostrar la multiplicación de los dos valores
print("Multiplicación:", a * b)                     # Imprime la multiplicación de a y b

# Realizar y mostrar la división de los dos valores
print("División:", a / b)                           # Imprime la división de a entre b

# Realizar y mostrar la división entera de los dos valores
print("División entera:", a // b)                   # Imprime la división entera de a entre b

# Realizar y mostrar el módulo (resto de la división) de los dos valores
print("Módulo:", a % b)                             # Imprime el módulo de a entre b

# Realizar y mostrar la potencia de a elevado a b
print("Potencia:", a ** b)                          # Imprime a elevado a b

# Realizar y mostrar la raíz cuadrada de a
print("Raíz cuadrada de a:", a ** 0.5)              # Imprime la raíz cuadrada de a

# Realizar y mostrar la raíz cuadrada de b
print("Raíz cuadrada de b:", b ** 0.5)              # Imprime la raíz cuadrada de b

# Realizar y mostrar el valor absoluto de la resta de a y b
print("Valor absoluto de la resta:", abs(a - b))    # Imprime el valor absoluto de a - b

# Realizar y mostrar el redondeo de la división de a entre b
print("Redondeo de la división:", round(a / b, 2))  # Imprime la división redondeada a 2 decimales

# Realizar y mostrar el logaritmo en base 10 de a
import math
print("Logaritmo en base 10 de a:", math.log10(a))  # Imprime el logaritmo en base 10 de a

# Realizar y mostrar el logaritmo en base 10 de b
print("Logaritmo en base 10 de b:", math.log10(b))  # Imprime el logaritmo en base 10 de b

# Realizar y mostrar el seno de a (en radianes)
print("Seno de a:", math.sin(a))                    # Imprime el seno de a

# Realizar y mostrar el coseno de b (en radianes)
print("Coseno de b:", math.cos(b))                  # Imprime el coseno de b

# Imprimir un mensaje de finalización
print("\n¡Pero sigo siendo el rey!")                # Mensaje de finalización