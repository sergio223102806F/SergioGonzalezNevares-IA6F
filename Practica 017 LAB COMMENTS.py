# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:36:31 2025

@author: elvin
"""

#LAB COMMENTS
# Este programa calcula el número de segundos en un número dado de horas
# Este programa fue escrito hace dos días

a = 2  # Número de horas
seconds = 3600  # Número de segundos en 1 hora

print("Horas:", a)  # Imprimir el número de horas
print("Segundos en Horas:", a * seconds)  # Imprimir el número de segundos en el número dado de horas

# Aquí también deberíamos imprimir "Goodbye" (Adiós)
print("Goodbye")  # Se agregó el mensaje faltante "Goodbye"

# Este es el final del programa que calcula el número de segundos en 2 horas

# Ejemplo adicional: Calcular el número de segundos en un número dado de minutos
minutes = 30  # Número de minutos
seconds_per_minute = 60  # Número de segundos en 1 minuto

print("Minutos:", minutes)  # Imprimir el número de minutos
print("Segundos en Minutos:", minutes * seconds_per_minute)  # Imprimir el número de segundos en los minutos dados

# Ejemplo adicional: Calcular el número de segundos en un número dado de días
days = 1  # Número de días
hours_per_day = 24  # Número de horas en 1 día
seconds_per_hour = 3600  # Número de segundos en 1 hora

print("Días:", days)  # Imprimir el número de días
print("Segundos en Días:", days * hours_per_day * seconds_per_hour)  # Imprimir el número de segundos en los días dados

# Ejemplo adicional: Calcular el número de segundos en un número dado de semanas
weeks = 1  # Número de semanas
days_per_week = 7  # Número de días en 1 semana

print("Semanas:", weeks)  # Imprimir el número de semanas
print("Segundos en Semanas:", weeks * days_per_week * hours_per_day * seconds_per_hour)  # Imprimir el número de segundos en las semanas dadas
