# Crear un programa en el que el usuario debe de adivinar un numero dentro de un rango dado, cada que el usuario falle en adivinar el margen de numeros sera reducido para darle pistas al usuario

numero_aleatorio = 777
rango_superior = 1000
rango_menor = 1
contador_intentos = 0

valor_usuario = int(input("Adivine el numero: "))


if(valor_usuario == numero_aleatorio):
    print("Felicidades adivinaste el numero")
else:
    contador_intentos += 1
    while(valor_usuario != numero_aleatorio):
        print(f"Equivocado, pero te doy una pista el rango superior es {rango_superior}, y el rango inferior es {rango_menor}\n")
        valor_usuario = int(input("Adivine el numero: "))
        if(contador_intentos >= 1 and rango_superior > 777 and rango_superior > 802 and rango_menor < 777 and rango_menor < 677):
            rango_superior -= 25
            rango_menor += 100
        else:
            print("Ya te di demasiadas pistas!!")
        contador_intentos += 1

print(f"Felicidades adivinaste !!!! el numero es: {numero_aleatorio}, \nlo adivinaste en {contador_intentos} intentos!!")