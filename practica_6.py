"""
Realice un codigo que le permita hacer conversiones de tiempo 
de hora a minutos 
de minutos a segundos y 
de segundos a horas.
"""
# constantes
HORA_A_MINUTOS = 60
MINUTOS_A_SEGUNDOS = 60
HORA_A_SEGUNDOS = 3600


try:
    opciones = ['hora', 'minuto', 'segundo']
    print("Opciones de conversion:")
    print("1. Hora a Minutos")
    print("2. Minutos a Segundos")
    print("3. Segundos a Horas")
    print("4. Salir")
    while True:
        eleccion = input("Seleccione una opcion (1-4): ")
        # validacion de la eleccion
        # not eleccion.isdigit() validar que el input sea un numero
        # int(eleccion) < 1  validar que el no sea valor sea menor a 1
        # int(eleccion) > 4  validar que el no sea valor sea mayor a 4
        if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > 4:
            print("Opcion invalida. Por favor seleccione una opcion del 1 al 4.")
            continue
        eleccion = int(eleccion)
        if eleccion == 1:
            horas = float(input("Ingrese el numero de horas: "))
            minutos = horas * HORA_A_MINUTOS
            print(f"{horas} horas son {minutos} minutos.")
        elif eleccion == 2:
            minutos = float(input("Ingrese el numero de minutos: "))
            segundos = minutos * MINUTOS_A_SEGUNDOS
            print(f"{minutos} minutos son {segundos} segundos.")
        elif eleccion == 3:
            segundos = float(input("Ingrese el numero de segundos: "))
            horas = segundos / HORA_A_SEGUNDOS
            print(f"{segundos} segundos son {horas} horas.")
        if eleccion == 4:
            print("Saliendo del programa.")
            break
except ValueError:
    print("Entrada invalida. Por favor ingrese un numero valido.")