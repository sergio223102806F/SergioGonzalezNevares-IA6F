# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 17:32:53 2025

@author: elvin
"""
#Version 1
def boring_function(message="'Boredom Mode' ON."):
    print(message)  # Imprime el mensaje proporcionado.
    return 123  # Devuelve el valor 123.

print("This lesson is interesting!")  # Imprime un mensaje inicial.
boring_function()  # Llama a la función sin argumentos (usa el valor por defecto).
print("This lesson is boring...")  # Imprime un mensaje final.

#Version 2
# Define una función lambda que imprime un mensaje y devuelve 123.
boring_function = lambda: print("'Boredom Mode' ON.") or 123

print("This lesson is interesting!")  # Imprime un mensaje inicial.
boring_function()  # Llama a la función lambda.
print("This lesson is boring...")  # Imprime un mensaje final.

#Version 3
class BoringLesson:
    def boring_function(self):
        print("'Boredom Mode' ON.")  # Imprime un mensaje.
        return 123  # Devuelve el valor 123.

# Crear una instancia de la clase BoringLesson.
lesson = BoringLesson()

print("This lesson is interesting!")  # Imprime un mensaje inicial.
lesson.boring_function()  # Llama al método boring_function.
print("This lesson is boring...")  # Imprime un mensaje final.

