#Programa: Edad

# Tema: Operaciones aritmeticas y conversiones de tipos

# 1. Pedimos años de nacimiento

año_nacimiento = int(input("Ingrese su año de nacimiento:"))

año_actual = 2026

#Calculamos la edad actual restando el año actual con el año de nacimiento

edad_actual = año_actual - año_nacimiento

# 2. Mostramos la edad actual al usuario
print(f"Su edad es: {edad_actual} años")