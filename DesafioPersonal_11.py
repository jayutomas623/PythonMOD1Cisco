#Generar un numero random que el usuario deba buscar con pistas
import random

numero_random = random.randint(1, 1000)

entrada_usuario = int(input("Ingrese el numero que cree que es: "))

print(numero_random)

while(entrada_usuario != numero_random):
    entrada_usuario = int(input("Intentalo de nuevo: "))
    if(entrada_usuario > numero_random):
        print("Muy alto")
    else:
        print("Muy bajo")

print("Felicidades lo lograste!!")