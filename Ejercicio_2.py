# Segundo ejercicio: Suma simple con input()

# Tema: input(), int(), float(), variables

# 1. Pedir el primer numero al usuario y guardarlo en una variable
# input() siempre devuelve un string, por lo que debemos convertirlo a int() o float() si queremos hacer operaciones matematicas

numero1_texto = input("Ingresa el primer numero: ")

print(f"El primer numero ingresado es: {numero1_texto}")

#2. Convertit el texto a numero entero con int() y guardarlo en una variable

numero1 = int(numero1_texto)

print(f"El numero convertido es: {numero1}")

#3. Pedir el segundo numero al usuario y guardarlo en una variable
numero2_texto = input("Ingresa el segundo numero: ")

numero2 = int (numero2_texto)

# 4. Sumar ambos numeros y guardar el resultado en una variable

suma = numero1 + numero2

# 5. Mostrar el resultado de la suma al usuario

print(f"La suma de {numero1} y {numero2} es: {suma}")

# Otro ejemplo esta ves con resta
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")

resta = int(num1) - int(num2)

print(f"La resta de {num1} y {num2} es: {resta}")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

resta = numero1 - numero2

print(f"La resta de {numero1} y {numero2} es: {resta}")