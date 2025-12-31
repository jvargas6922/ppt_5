"""
Tipos comunes de excepciones en Python:
"""

# ZeroDivisionError(Ocurre cuando se intenta dividir un número por cero)
"""
try:
    num_1 = 10
    num_2 = 0
    division = num_1 / num_2
except ZeroDivisionError as e:
    print(f"Error: {e} : No se puede dividir por cero.")

"""

# ValueError(Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado)
"""
try:
    num_1 = 10
    num_2 = 'hola'
    num_2 = int(num_2)
except ValueError as e:
    print(f"Error: {e} : Tipo de dato incorrecto.")
"""

# IndexError(Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista o secuencia)
"""
autos = ['Toyota', 'Honda', 'Mazda']
            0.        1.        2 => Indices

print(autos[0])#Toyota
print(autos[1])#Honda
print(autos[2])#Mazda
print(autos[3])# no existe!!
try:
    print(autos[3])
except IndexError as e:
    print(f"Error: {e} : Indice fuera de rango.")

"""

# KeyError(Ocurre cuando se intenta acceder a una clave que no existe en un diccionario)
"""
regiones_chile = {
    "I": "Región de Tarapacá",
    "II": "Región de Antofagasta",
    "III": "Región de Atacama",
    "IV": "Región de Coquimbo",
    "V": "Región de Valparaíso",
    "RM": "Región Metropolitana de Santiago",
    "VI": "Región del Libertador General Bernardo O'Higgins",
    "VII": "Región del Maule",
    "XVI": "Región de Ñuble",
    "VIII": "Región del Biobío",
    "IX": "Región de La Araucanía",
    "XIV": "Región de Los Ríos",
    "X": "Región de Los Lagos",
    "XI": "Región de Aysén del General Carlos Ibáñez del Campo",
    "XII": "Región de Magallanes y de la Antártica Chilena", 
}
# Exepcion a capturar
# print(regiones_chile["XX"])

try:
    print(regiones_chile["XX"])
except KeyError as e:
    print(f"Error: {e} : La clave no existe en el diccionario.")

"""

# TypeError (Ocurre cuando una operación o función se aplica a un objeto de un tipo inapropiado)
num_1 = 10
num_2 = "5"
# suma = num_1 + num_2  # No se puede sumar un entero y una cadena

try:
    suma = num_1 + num_2
except TypeError as e:
    print(f"Error: {e} : No se puede sumar un entero y una cadena.")