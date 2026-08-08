# Tercer ejercicio: Par o impar

# Tema: Operador modulo (%) y condicional if

# 1. Pedir un numero al usuario
numero = int(input("Ingrese un numero: "))

# 2. Usamos % (modulo) para saber el resto de la division del numero entre 2
# si el resto es 0, el numero es par, si el resto es 1, el numero es impar
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")