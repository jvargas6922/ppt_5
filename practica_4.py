"""
Contexto: 🙌
Muchos programas realizan cálculos entre números. La división es una operación común, pero puede
romperse si los datos no están controlados correctamente.
Consigna: ✍
Creá una función que:
Paso a paso: ⚙
1. Capturá cada excepción en un bloque
    ● Pida al usuario dos números
    ● Intente dividir el primero por el segundo
    ● Maneje dos errores posibles:
    ● Entrada inválida (ValueError)
    ● División por cero (ZeroDivisionError)
Imprima mensajes personalizados para cada uno separado
1. Captura cada exepción en un bloque separado
2. Usá else para mostrar el resultado si todo salió bien
3. Usá finally para imprimir siempre un cierre como “Proceso finalizado”
4. Probalo con entradas correctas y con fallos para ver los resultados
"""

# definimos la funcion a ocupar
# def division():
#     try:
#         numerador = input("Ingrese el numerador: ") 
#         denominador = input("Ingrese el denominador: ")
#         numerador = float(numerador)  # Convertimos a float para permitir decimales
#         denominador = float(denominador)  # Convertimos a float para permitir decimales
#         resultado = numerador / denominador
#     except ValueError:
#         print("Error: Entrada inválida. Por favor, ingrese números válidos.")
#     except ZeroDivisionError:
#         print("Error: División por cero no permitida. El denominador debe ser distinto de cero.")
#     else:
#         print(f"El resultado de la división es: {resultado}")
#     finally:
#         print("Proceso finalizado.")

# division()

# version 2 de la funcion
def division_2(numerador , denominador):
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        return "Error: División por cero no permitida. El denominador debe ser distinto de cero."
    else:
        return f"El resultado de la división es: {resultado}"
    finally:
        print("Proceso finalizado.")

def peticion():
    while True:
        dato_1 = input("Ingrese el numerador: ")
        dato_2 = input("Ingrese el denominador: ")
        # validar que los datos no vengan vacios
        if dato_1.strip() == "" or dato_2.strip() == "":
            print("Error: Entrada inválida. Por favor, ingrese números válidos.")
            continue
        else:
            try:
                #  los 2 campos tienen datos
                num_1 = float(dato_1)
                num_2 = float(dato_2)
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese números válidos.")
                continue
            # llamar a la funcion division_2
            resultado = division_2(num_1 , num_2)
            print(resultado)
            break
            

    

peticion()



