import random

eleccion = input("Elija piedra, papel o tijera ")
eleccion = eleccion.lower()
opciones = ['piedra', 'papel', 'tijera']
ordenador = opciones[random.randint(0,2)]

if (eleccion == ordenador):
    print(F"Empate, el cpu ha sacado: {ordenador}")
elif ((eleccion == 'tijera') and (ordenador == 'papel')) or ((eleccion == 'papel') and (ordenador == 'piedra')) or ((eleccion == 'piedra') and (ordenador == 'tijera')):
    print(f"Enhorabuena, has ganado, el cpu ha sacado: {ordenador}")
else:
    print(f"Has perdido, el cpu ha sacado: {ordenador}")