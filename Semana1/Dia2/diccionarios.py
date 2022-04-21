# Similar a JSON
capitales = {
    "Perú": "Lima",
    "Ecuador": "Quito",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
print(capitales)
nuevaCapitales = {"Brasil": "Brasilia"}
# Agregar nuevo valor en el diccionario
capitales.update(nuevaCapitales)
print(capitales)

# Eliminar
capitales.pop("Chile")
print(capitales)

# Recorrer diccionarios
for capital in capitales:
    print(capital + ":" + capitales[capital])
print("-"*20)
##############
print(capitales.keys())
print("-"*20)
###############
print(capitales.values())
print("-"*20)
##############
for clave in capitales.keys():
    print(clave+"=>"+capitales[clave])
print("-"*20)
##############
for clave, valor in capitales.items():
    print(clave+" -- " + valor)
print("-"*20)
###############
# Base de datos de alumnos
alumno1 = {
    "Nombre": "Sebastian",
    "Edad": 22,
    "Nota": 19.5,
    "Aprobado": True,
    "Cursos": ["JavaScript", "Python", "C#"]
}
alumno2 = {
    "Nombre": "Lisa",
    "Edad": 24,
    "Nota": 17.5,
    "Aprobado": True,
    "Cursos": ["Kotlin", "Swift", "Java"]
}
alumnos = [alumno1, alumno2]
print(alumnos)
##################
print("*"*100)
for columna in alumno1:
    print(columna, end="        |")
print()
print("*"*100)
for alumno in alumnos:
    for clave, valor in alumno.items():
        print(valor, end=" | ")
    print()

print ("+"*100)
print (capitales.values())
busqueda = input("CAPITAL")
for capital in capitales:
    print(capital)