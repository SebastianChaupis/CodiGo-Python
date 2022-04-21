tabla = int(input("Ingrese la tabla con la que quiere multipiclar: "))

for contador in range(1,5):
    valor = tabla * contador
    print(str(tabla) + ' x ' + str(contador) + ' = ' + str(valor))
