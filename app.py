"""
⚠ Una excepción es un evento que interrumpe el flujo normal de un programa cuando ocurre un
error durante su ejecución.
🔍 ¿Cuándo ocurre una excepción?
● Cuando intentás dividir por cero
● Cuando accedés a una posición inexistente de una lista
● Cuando usás mal un tipo de dato
● Cuando fallan entradas del usuario o procesos externos
💥 ¿Qué pasa si no se maneja una excepción?
● Python detiene la ejecución
● Se muestra un mensaje de error (traceback) con información del fallo
● El usuario puede perder el progreso o no entender el problema
"""

"""
Division por cero
formas de poder controlar este tipo errores.
    1. Usando condicionales
    2. Validando que los datos ingresados sean correctos
    3. Usando bloques try/except



    ejemplo de manejo de excepciones usando try/except  
    try:
        # Código que puede generar una excepción
        resultado = num_1 / num_2
    except ZeroDivisionError:
        # Código para manejar la excepción
        print("Error: No se puede dividir por cero.")
    else:
        # Código que se ejecuta si no hubo excepción
        print(f"El resultado de la división es: {resultado}")
"""


# Division por cero
# num_1 = input("Ingrese el dividendo: ")
# num_2 = input("Ingrese el divisor: ")

# # validar que los datos ingresados sean numeros, que no sean flotantes ni cadenas

# num_1 = int(num_1)
# num_2 = int(num_2)

# # validacion de los 2 datos deben ser = 0
# division = num_1 / num_2
# print(f"El resultado de la división es: {division}")


# Usando try/except (Uso basico) version 1
# try:
#     num_1 = input("Ingrese el dividendo: ")
#     num_2 = input("Ingrese el divisor: ")
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#     division = num_1 / num_2
#     print(f"El resultado de la división es: {division}")
# except:
#     print("Error: No se puede dividir por cero o ingreso un dato incorrecto.")


# usando try/except (Uso avanzado) version 2
try:
    num_1 = input("Ingrese el dividendo: ")
    num_2 = input("Ingrese el divisor: ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    division = num_1 / num_2
    print(f"El resultado de la división es: {division}")
except (ZeroDivisionError, ValueError) as e:
    if isinstance(e, ZeroDivisionError):
        print("Error: No se puede dividir por cero.")
    elif isinstance(e, ValueError):
        print("Error: Ingreso un dato incorrecto. Por favor ingrese números enteros.")