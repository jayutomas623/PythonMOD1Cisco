nota_del_estudiante = 50
min_aprobado = 51

if(nota_del_estudiante >= min_aprobado):
    print("Estudiante aprobado")
else:
    print("Estudiante reprobado")
    print("Este mensaje esta dentro de la condicional if-else\n")


# Un estudiante quiere postular a ser Preco
# Debe cumplir con ciertas condiciones para pasar =>16 años, 60 Kg min, de 5to sec.
nombre_estudiante = "Jayu Tomas Mendoza Amaru"
edad = 15
peso = 80
grado = 5

edad_condicion = 16
peso_condicion = 60
grado_condicion = 5

if(edad >= edad_condicion):
    if(peso >= peso_condicion):
        if(grado == grado_condicion):
            print(f"El estudiante {nombre_estudiante} puede ingresar al pre-militar")
else:
    print(f"El estudiante {nombre_estudiante} no puede ingresar a la premilitar\n\n")



# Se debe dar una categoria al estudiante dependiendo de la nota obtenida de 51-70 Basico, de 71 - 80 Medio, de 81 - 95 Experto, 96 - 100 Maestro
nota_obtenida = 50

if(nota_obtenida >= 51):
    if(nota_obtenida <= 70):
        print("Basico")
    elif(nota_obtenida <= 80):
        print("Medio")
    elif(nota_obtenida <= 95):
        print("Experto")
    else:
        print("Maestro")
else:
    print("Reprobado")

#Redondeo y formateo de numeros

var = 7.5
var_1 = 6.5


var = round(var)
print(var)
print()

var_1 = round(var_1)
print(var_1)
print()

# Formato flexible
numero = 3.14159264
print(f"{'1 decimal:':<15} {format(numero, '.1f')}")

# Formato f-string
print(f"Redondeo en f-string: {numero: .2f}")
