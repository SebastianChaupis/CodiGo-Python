# CRUD DE ALUMNOS
print("-"*50)
print("|"+" "*9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "*8 + "|")
print("-"*50)
# MENU
print("|"+" "*9 + "MENU DE OPCIONES     " + " "*18 + "|")
print("|"+" "*9 + "[1] REGISTRAR ALUMNO " + " "*18 + "|")
print("|"+" "*9 + "[2] MOSTRAR ALUMNO   " + " "*18 + "|")
print("|"+" "*9 + "[3] ACTUALIZAR ALUMNO" + " "*18 + "|")
print("|"+" "*9 + "[4] ELIMINAR ALUMNO  " + " "*18 + "|")
print("|"+" "*9 + "[5] SALIR            " + " "*18 + "|")
print("-"*50)

# OPCIONES
opciones = 0
alumnos = []
while (opciones != 5):
    opciones = int(input("Ingrese opcion: "))
    if (opciones == 1):
        print("Agregar Alumno CodiGo")
        nombre = input("Ingrese nombre completo: ")
        email = input("Ingrese email: ")
        celular = input("Ingrese celular: ")
        dicAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
        alumnos.append(dicAlumno)
        print("Alumno Registrado Correctamente")
    elif(opciones == 2):
        for columna in dicAlumno:
            print(columna, end="        |")
        print()
        print("-"*50)
        for alumno in alumnos:
            for clave, valor in alumno.items():
                print(valor, end=" | ")
            print()
        print()
    elif(opciones == 3):
        buscar = input("Ingresar el email del alumno: ")
        indexAlumno = -1
        for i in range(len(alumnos)):
            dicAlumnoBusqueda = alumnos[i]
            for clave, valor in dicAlumnoBusqueda.items():
                if(valor == buscar and clave== 'email' ):
                    indexAlumno = i
                    break
        if (indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
            nombre =input("Nombre: ")
            email =input("Email: ")
            celular =celular("Celular: ")
            dicAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            alumnos[indexAlumno]= dicAlumnoEditar
            print("Alumno Editado")
    elif(opciones == 4):
        buscar = input("Ingrese el nombre del alumno que desea eliminar: ")
        alumnos.pop(buscar)
        print("Eliminado del registro")
