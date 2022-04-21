#INPUTS 
print ("Menu de Opciones")
print ("[1]Registrar Alumno")
print ("[2]Mostrar Alumno")
print ("[3]Actualizar Alumno")
print ("[4]Eliminar Alumno")
print ("[5]SALIR")

opcion =0
alumnos = [{'nombre':"Sebastian","email":"sebaschaupis1@gmail.com","celular":"924808209"}]
while(opcion !=5):
    opcion = int(input("Ingrese numero de opcion: "))
    if(opcion ==1):
        print ("Nuevo Alumno")
        nombre = input("Nombre :")
        apellido = input("Apellido: ")
        email = input("Email: ")
        celular = input("Celular: ")
        lista = {
            'nombre':nombre,
            'apellido':apellido,
            'email':email,
            'celular':celular,
        }
        alumnos.append(lista)
        print("Alumno agregado existosamente")
        
#PROCESO
#OUTPUTS