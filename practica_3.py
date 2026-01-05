"""
¿En qué consistirá la Demo?
Vas a solicitar al usuario que ingrese un número, y vas a manejar posibles errores para evitar que el programa
se rompa.
🔹 Objetivo funcional:
    ● Solicitar un número entero
    ● Detectar si el usuario escribe texto o caracteres inválidos
    ● Mostrar un mensaje amigable en lugar de un traceback

🔹 Variantes para probar:
    ● Ingresar "25"   → ❌ ValueError (por ser float)
    ● Ingresar "abc"  → ❌ ValueError
    ● Ingresar "10.5" → ✅ válido

"""

numero = input("Por favor ingrese un nuemero: ")
try:
    numero = int(numero)
    print(f"El número ingresado es: {numero}")
    resultado = 100 / numero
except ValueError as e:
    print("Error: Debe ingresar un número entero válido.")
    print(f"Detalle del error: {e}")
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero.")
    print(f"Detalle del error: {e}")
except Exception as e:
    print("Ha ocurrido un error inesperado.")
    print(f"Detalle del error: {e}")

