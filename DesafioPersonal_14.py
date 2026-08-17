#Generar un numero random que el usuario deba buscar con pistas, sin embargo si el usuario se equivoca mas de 3 veces, perdera

import random

numero_random = random.randint(1, 1000)

entrada_usuario = int(input("Ingrese el numero que cree que es: "))

cantidad_de_errores = 0

print(numero_random)

while(entrada_usuario != numero_random):
    cantidad_de_errores += 1
    entrada_usuario = int(input("Intentalo de nuevo: "))
    if(entrada_usuario > numero_random):
        print("Muy alto")
    elif(entrada_usuario < numero_random):
        print("Muy bajo")
    if(cantidad_de_errores > 3 and entrada_usuario != numero_random):
        break
    print(cantidad_de_errores)

if(cantidad_de_errores > 3 and entrada_usuario != numero_random):
    print("Perdiste")
else:    
    print("Felicidades lo lograste!!")