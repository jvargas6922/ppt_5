"""
Juego del Impostor
V1
 - debemos definir la cantidad de jugadores (listo)
 - asignar aleatoriamente un impostor. (listo)
 - seleccionar un palabra secreta definida de forma aleatoria. (listo)
 - cada jugador debe intentar descubir al impostor. cantidad rondas = 3

V2
"""
import random

print("Bienvenido al juego del Impostor")
num_jugadores = input("Ingrese la cantidad de jugadores: ")
try:
    num_jugadores = int(num_jugadores)
    print(f"Cantidad de jugadores: {num_jugadores}")
    # Crear una lista de jugadores
    jugadores = [f"Jugador {i+1}" for i in range(num_jugadores)]

    # Seleccionar aleatoriamente un impostor
    impostor = random.choice(jugadores)
    print(f"El impostor es: {impostor}")
    print("\n")

    # palabras secretas
    palabras_secretas = ["manzana", "banana", "naranja", "uva", "pera"]
    palabra_secreta = random.choice(palabras_secretas)
    print(f"La palabra secreta es: {palabra_secreta}")
    print("\n")

    print("La palabra secreta seleccionada corresponde a frutas")
    # definir la cantidad de rondas
    rondas = 3
    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")
        for jugador in jugadores:
            print(f"{jugador} está participando en la ronda {ronda}.")
            # tenemos que preguntar la palabra a los usuarios.
            palabra = input(f"{jugador}, ingresa la palabra secreta: ")
            print("\n")

            if palabra.lower() == palabra_secreta:
                print(f"{jugador} ha acertado la palabra secreta!")
                break
            else:
                print(f"{jugador} no ha acertado la palabra secreta.")
                print("\n")
            

except ValueError:
    print("Por favor, ingrese un número válido para la cantidad de jugadores.")



