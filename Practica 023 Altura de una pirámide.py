# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:40:29 2025

@author: elvin
"""

# Función para validar que el usuario ingrese un número entero positivo
def obtener_bloques():
    while True:  # Bucle infinito hasta que se ingrese un valor válido
        try:  # Intenta ejecutar el código dentro del bloque
            bloques = int(input("Ingresa el número de bloques: "))  # Solicita y convierte la entrada a entero
            if bloques > 0:  # Verifica si el número es mayor que 0
                return bloques  # Retorna el número de bloques si es válido
            else:  # Si el número es menor o igual a 0
                print("Por favor, ingresa un número mayor que 0.")  # Mensaje de error
        except ValueError:  # Si la conversión a entero falla
            print("Entrada inválida. Ingresa un número entero.")  # Mensaje de error

# Función para calcular la altura de la pirámide y los bloques sobrantes
def calcular_piramide(bloques):
    altura = 0  # Inicializa la altura de la pirámide en 0
    bloques_capa = 1  # Inicializa los bloques necesarios para la primera capa
    while bloques >= bloques_capa:  # Mientras haya bloques suficientes para la capa actual
        bloques -= bloques_capa  # Resta los bloques usados en la capa actual
        altura += 1  # Incrementa la altura de la pirámide
        bloques_capa += 1  # Aumenta los bloques necesarios para la siguiente capa
    return altura, bloques  # Retorna la altura y los bloques sobrantes

# Función para dibujar la pirámide
def dibujar_piramide(altura):
    for i in range(1, altura + 1):  # Itera desde 1 hasta la altura de la pirámide
        print(" " * (altura - i), end="")  # Imprime espacios para centrar la pirámide
        print("[]" * i)  # Imprime los bloques de la capa actual

# Programa principal
bloques = obtener_bloques()  # Llama a la función para obtener el número de bloques válido
altura, sobrantes = calcular_piramide(bloques)  # Calcula la altura y los bloques sobrantes

# Mostrar resultados
print("\nResultados:")  # Encabezado de los resultados
print(f"La altura de la pirámide es: {altura}")  # Muestra la altura de la pirámide
print(f"Bloques sobrantes: {sobrantes}")  # Muestra los bloques sobrantes

# Dibujar la pirámide si se pudo construir
if altura > 0:  # Si la altura es mayor que 0
    print("\nAsí se vería tu pirámide:")  # Mensaje para mostrar la pirámide
    dibujar_piramide(altura)  # Llama a la función para dibujar la pirámide
else:  # Si no se pudo construir la pirámide
    print("No hay suficientes bloques para construir una pirámide.")  # Mensaje de error