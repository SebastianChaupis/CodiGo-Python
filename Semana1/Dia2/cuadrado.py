l = int(input ("Ingrese el lado del cuadrado :"))

for fila in range(1,l+1):
    if (fila == 1 or fila==l):
        print("* " * l)
    else:
        print("* "+ "  "* (l - 2)+ "*")
    
    
