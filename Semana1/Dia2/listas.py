dias= ["Lunes","Martes","Miercoles"]
print (dias)

#Eliminar ultimo valor de la lista
dias.pop()
print(dias)
#Agregar un valor a la lista
dias.append("Miercoles")
print(dias)

dias[0]= "Domingo"
print(dias)

dias = tuple(dias)
print(dias)

print(dias[1:4])

for dia in dias:
    print ( dia)
    
