# Contador de numeros impares y pares, pararlo utilizando unicamente 0, e iniciar el programa solo si el primer numero ingresado es 1. Si el usuario ingresa numeros negativos no se contaran y se contaran en una variable aparte de errores. Si el usuario no ingresa el numero 1 al inicio, se le mostrara un mensaje de error.

contador_pares = 0
contador_impares = 0
contador_errores = 0

entrada_usuario = int(input("Ingrese el numero 1  para iniciar el conteto de pares e impares: "))

if(entrada_usuario == 1):
    while(entrada_usuario != 0):
        entrada_usuario = int(input("Ingrese un numero: "))
        if(entrada_usuario > 0 and entrada_usuario % 2 == 0):
            contador_pares += 1
        elif(entrada_usuario > 0 and entrada_usuario % 2 == 1):
            contador_impares +=1
        elif(entrada_usuario > 0):
            contador_errores += 1

        print(f"El contador de pares es: {contador_pares}")
        print(f"El contador de impares es: {contador_impares}")
        print(f"El contador de errores es: {contador_errores}")

else:
    print(f"Programa no iniciado se ingreso: {entrada_usuario}")
    