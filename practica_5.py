"""
Conversor de unidades con validación
Contexto: 🙌
En una aplicación de cálculo de distancias, necesitamos convertir kilómetros a millas. Sin embargo, la
entrada del usuario no siempre es válida, y puede generar errores si no se maneja correctamente.
Consigna: ✍
Implementá un programa en Python que:
    ● Solicite al usuario una distancia en kilómetros (Listo)
    ● Verifique si la entrada es numérica válida (Listo)
    ● Convierta el valor a millas (1 km = 0.621371 mi) (Listo)
    ● Muestre un mensaje de error si el valor ingresado no es un número
Paso a paso: ⚙
1. Usá un bloque try/except para capturar ValueError (Listo)
2. Si es válida, hacé la conversión y mostrala con 2 decimales
3. Si falla, mostrale un mensaje amable al usuario
4. Puedes usar un bucle para reintentar hasta que ingrese bien
"""
# constante de conversión
MILLA = 0.621371

while True:
    try:
        kilometro = input("Ingrese la distancia en kilómetros: ")
        if kilometro.strip() == "":
            print("Error: Entrada inválida. Por favor, ingrese un número válido.")
            continue
        else:
            kilometro = float(kilometro)
            if kilometro < 0:
                print("Error: La distancia no puede ser negativa. Por favor, ingrese un número válido.")
                continue
            else:
                millas = kilometro * MILLA
                print(f"La distancia en millas es: {millas:.2f} mi")
                break

    except ValueError:
        print("Error: El dato ingresado no es valido debe ser un número.")
        continue

    
