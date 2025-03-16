# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:46:53 2025

@author: elvin
"""

# Leer tres números ingresados por el usuario
numero1 = int(input("Ingresa el primer número: "))  # Solicita el primer número y lo convierte a entero
numero2 = int(input("Ingresa el segundo número: "))  # Solicita el segundo número y lo convierte a entero
numero3 = int(input("Ingresa el tercer número: "))   # Solicita el tercer número y lo convierte a entero

# Suponemos temporalmente que el primer número es el mayor.
# Esto lo verificaremos más adelante.
numero_mayor = numero1                              # Asigna el primer número como el mayor temporalmente

# Verificamos si el segundo número es mayor que el número mayor actual
# y actualizamos el número mayor si es necesario.
if numero2 > numero_mayor:                          # Compara el segundo número con el mayor actual
    numero_mayor = numero2                          # Actualiza el número mayor si el segundo es mayor

# Verificamos si el tercer número es mayor que el número mayor actual
# y actualizamos el número mayor si es necesario.
if numero3 > numero_mayor:                          # Compara el tercer número con el mayor actual
    numero_mayor = numero3                          # Actualiza el número mayor si el tercero es mayor

# Imprimir el resultado
print("El número mayor es:", numero_mayor)          # Muestra en pantalla el número mayor

# Calcular la suma de los tres números
suma = numero1 + numero2 + numero3                  # Suma los tres números
print("La suma de los números es:", suma)           # Muestra en pantalla la suma

# Calcular el promedio de los tres números
promedio = suma / 3                                 # Calcula el promedio de los tres números
print("El promedio de los números es:", promedio)   # Muestra en pantalla el promedio

# Calcular el producto de los tres números
producto = numero1 * numero2 * numero3              # Multiplica los tres números
print("El producto de los números es:", producto)   # Muestra en pantalla el producto

# Encontrar el número menor entre los tres números
numero_menor = numero1                              # Asigna el primer número como el menor temporalmente

if numero2 < numero_menor:                          # Compara el segundo número con el menor actual
    numero_menor = numero2                          # Actualiza el número menor si el segundo es menor

if numero3 < numero_menor:                          # Compara el tercer número con el menor actual
    numero_menor = numero3                          # Actualiza el número menor si el tercero es menor

print("El número menor es:", numero_menor)          # Muestra en pantalla el número menor

# Verificar si los tres números son iguales
if numero1 == numero2 == numero3:                   # Compara si los tres números son iguales
    print("Todos los números son iguales.")         # Muestra en pantalla si son iguales
else:
    print("Los números no son iguales.")            # Muestra en pantalla si no son iguales

# Verificar si los números están en orden ascendente
if numero1 < numero2 < numero3:                     # Compara si los números están en orden ascendente
    print("Los números están en orden ascendente.") # Muestra en pantalla si están en orden ascendente
else:
    print("Los números no están en orden ascendente.")  # Muestra en pantalla si no están en orden ascendente

# Verificar si los números están en orden descendente
if numero1 > numero2 > numero3:                     # Compara si los números están en orden descendente
    print("Los números están en orden descendente.") # Muestra en pantalla si están en orden descendente
else:
    print("Los números no están en orden descendente.")  # Muestra en pantalla si no están en orden descendente

# Calcular la diferencia entre el número mayor y el número menor
diferencia = numero_mayor - numero_menor            # Calcula la diferencia entre el mayor y el menor
print("La diferencia entre el mayor y el menor es:", diferencia)  # Muestra en pantalla la diferencia

# Calcular la suma de los cuadrados de los tres números
suma_cuadrados = numero1**2 + numero2**2 + numero3**2  # Calcula la suma de los cuadrados
print("La suma de los cuadrados de los números es:", suma_cuadrados)  # Muestra en pantalla la suma de cuadrados

# Calcular la raíz cuadrada de la suma de los cuadrados
raiz_suma_cuadrados = suma_cuadrados ** 0.5         # Calcula la raíz cuadrada de la suma de cuadrados
print("La raíz cuadrada de la suma de los cuadrados es:", raiz_suma_cuadrados)  # Muestra en pantalla la raíz cuadrada