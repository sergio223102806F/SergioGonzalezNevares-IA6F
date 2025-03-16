# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:01:14 2025

@author: elvin
"""
#Version 2
# Cuenta Básica de Usuario
# Declara una variable numérica llamada 'var' con el valor 12.
var = 12

# Declara una variable llamada 'account_balance' que almacena el saldo de la cuenta (3000.0).
account_balance = 3000.0

# Declara una variable llamada 'client_name' que almacena el nombre del cliente.
# El nombre incluye un salto de línea (\n) al principio.
client_name = '\n Federico, El Caballo Homosexual'

# Imprime el estado de la cuenta, mostrando el valor de 'var', 'account_balance' y 'client_name'.
print("Estado de la cuenta:")
print("Variable numérica:", var)
print("Saldo de la cuenta:", account_balance)
print("Nombre del cliente:", client_name)

# Imprime solo el valor de la variable 'var'.
print("\nValor de la variable 'var':", var)

# Cambia el valor de la variable 'var' a un texto: "Teoría de Control".
var = "Teoría de Control"

# Imprime un mensaje concatenando "Python version: " con el valor actual de 'var'.
print("\nPython version: " + var)

# Reinicia la variable 'var' a un valor numérico (10).
var = 10

# Imprime el valor inicial de 'var'.
print("\nValor inicial de 'var':", var)

# Suma 1000 al valor actual de 'var' y lo almacena en la misma variable.
var = var + 1000

# Imprime el valor de 'var' después de sumar 1000.
print("Valor de 'var' después de sumar 1000:", var)

# Multiplica el valor actual de 'var' por 2 y lo almacena en la misma variable.
var = var * 2

# Imprime el valor de 'var' después de multiplicar por 2.
print("Valor de 'var' después de multiplicar por 2:", var)

# Resta 500 al valor actual de 'var' y lo almacena en la misma variable.
var = var - 500

# Imprime el valor de 'var' después de restar 500.
print("Valor de 'var' después de restar 500:", var)

# Divide el valor actual de 'var' entre 5 y lo almacena en la misma variable.
var = var / 5

# Imprime el valor de 'var' después de dividir entre 5.
print("Valor de 'var' después de dividir entre 5:", var)

# Interacción con el usuario:

# Solicita al usuario que ingrese un monto para depositar en la cuenta.
# El valor ingresado se convierte a tipo float (número decimal).
new_deposit = float(input("Ingrese el monto a depositar en la cuenta: "))

# Suma el monto depositado al saldo actual de la cuenta.
account_balance += new_deposit

# Imprime el nuevo saldo de la cuenta después del depósito.
print("Nuevo saldo de la cuenta:", account_balance)

# Validación de saldo:

# Si el saldo de la cuenta es menor que 0, imprime una alerta.
if account_balance < 0:
    print("\n¡Alerta! La cuenta está en números rojos.")

# Si el saldo de la cuenta es igual a 0, imprime un mensaje indicando que no hay saldo.
elif account_balance == 0:
    print("\nLa cuenta tiene un saldo de $0.")

# Si el saldo de la cuenta es positivo, imprime un mensaje indicando que el saldo es positivo.
else:
    print("\nLa cuenta tiene un saldo positivo.")

# Uso de una lista para almacenar transacciones:

# Crea una lista vacía llamada 'transactions' para almacenar las transacciones realizadas.
transactions = []

# Añade una nueva transacción a la lista. La transacción es una tupla con el tipo ("Depósito") y el monto.
transactions.append(("Depósito", new_deposit))

# Imprime el historial de transacciones:

# Recorre cada transacción en la lista 'transactions'.
print("\nHistorial de transacciones:")
for transaction in transactions:
    # Imprime el tipo y el monto de cada transacción.
    print(f"Tipo: {transaction[0]}, Monto: {transaction[1]}")

# Función para calcular intereses:

# Define una función llamada 'calculate_interest' que calcula el interés compuesto.
def calculate_interest(balance, rate, years):
    """
    Calcula el interés compuesto sobre un saldo dado.
    :param balance: Saldo inicial.
    :param rate: Tasa de interés anual (en decimal).
    :param years: Número de años.
    :return: Saldo final después de aplicar el interés.
    """
    # Fórmula del interés compuesto: balance * (1 + rate) ** years
    return balance * (1 + rate) ** years

# Aplicar interés al saldo de la cuenta:

# Define la tasa de interés anual (5% en decimal).
interest_rate = 0.05

# Define el período de inversión en años (3 años).
investment_years = 3

# Calcula el saldo final después de aplicar el interés compuesto.
final_balance = calculate_interest(account_balance, interest_rate, investment_years)

# Imprime el saldo final después de aplicar el interés, redondeado a 2 decimales.
print(f"\nSaldo después de {investment_years} años con un interés del {interest_rate * 100}%: {final_balance:.2f}")

# Mensaje final:

# Imprime un mensaje de agradecimiento al usuario por usar el sistema.
print("\nGracias por usar nuestro sistema de cuenta básica. ¡Hasta luego!")