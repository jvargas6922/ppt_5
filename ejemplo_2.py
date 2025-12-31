"""
practica de excepciones
"""

try:
    print(10/0)
except ZeroDivisionError as e:
    # print("Error: No se puede dividir por cero")
    print(f"Error: {e}")

try:
    edad = int("veinticinco")  # Esto generará un ValueError
except ValueError as e:
    # print("Error: No se pudo convertir la cadena a un número entero.")
    print(f"Error: {e}")

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError as e :
    # print("Error: Índice fuera de rango al acceder a la lista.")
    print(f"Error: {e}")

try:
    datos = {"nombre": "Joffred"}
    print(datos["apellido"])
except KeyError as e:
    # print("Error: La clave no existe en el diccionario.")
    print(f"Error: {e}")

try:
    resultado = "10" + 5
    print(resultado)  # Esto generará un TypeError
except TypeError as e:  
    # print("Error: No se pueden concatenar diferentes tipos de datos.")
    print(f"Error: {e}")