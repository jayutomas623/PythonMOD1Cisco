# Condicionales

# Estudiante aprobo la materia?

nota_obtenida = int(input("Ingrese la nota obetenida por el estudiante: "))

nota_minima = 51

if(nota_obtenida >= nota_minima):
    print(f"El estuidante aprobo la materia con una nota de: {nota_obtenida}")
else:
    print(f"El estudiante no aprobo la materia con una nota de: {nota_obtenida}")