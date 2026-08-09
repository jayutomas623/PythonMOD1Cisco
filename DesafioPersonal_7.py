# Bucle While

# var = 9

# while var != 0:
#     var = int(input("Por favor ingrese el numero \"0\" para parar el programa: "))

# print("\nTermino el programa :)")


# print("\nIniamos una cuenta regresiva")

# cuenta = int(input("Ingrese el numero desde el cual se iniciara: "))

# while(cuenta >= 0):
#     print(cuenta)
#     cuenta -= 1

# print("Termino la secuencia")

# Desconteo de 2 en 2

cuenta_2 = int(input("\nIngrese un numero par y mayor a 2 para realizar el conteo: "))

if(cuenta_2 % 2 == 0 and cuenta_2 >= 2):
    while(cuenta_2 >= 0):
        print(f" El valor del contador es: {cuenta_2}")
        cuenta_2 -= 2
else:
    print("El numero ingresado no cumple con los requisitos.")