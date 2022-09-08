import os

quedan = True
participantes = {}
while(quedan):
    print("Bienvenido a la casa de apuestas")
    nombre = input("Nombre de registro: ")
    apuesta = int(input("Valor de la apuesta: "))
    participantes[nombre] = apuesta
    confirmacion = input("¿Quedan más participantes? ")
    os.system('clear')
    if (confirmacion != 'si'):
        quedan = False

print("Apuestas realizadas:")
for i in participantes:
    print(i, participantes[i])

print(f"La apuesta ganadora es la de {max(participantes)} con {participantes[max(participantes)]}")