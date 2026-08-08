#Programa: Saludo

# Tema: Uso de Print() y variables

# 1. Crear una varialbe llamada nombre y le asignamos un texto

nombre = "Juan"

numero = 10

numeroReal = 3.14

Texto = " Hola Soy xd xd xd"

print(numero)

print(numeroReal)

print(nombre)

print("Hola Soy Jayu")

print('Hola Soy Tomas') # Son lo mismo, pero se recomienda usar comillas dobles

print(Texto)


# 2. Mostrar un mensaje combinado texto fijo y la variable
# La 'f' antes del string permite insertar variables dentro del texto

print(f"Bienvenido al curso de Python, {nombre}") # Primera forma de concatenar texto y variable, usando f-string

print("Bienvenido al curso de Python, " + nombre) # Segunda forma de concatenar texto y variable

apellido = "Perez"

print(f"Bienvenidos {nombre} {apellido}")



