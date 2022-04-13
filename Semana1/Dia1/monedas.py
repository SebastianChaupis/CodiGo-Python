#PROGRAMA PARA CONVERTIR MONEDAS
#Version 1.0 Soles a Dolares
#INPUTS - ENTRADAS
monto =input("Ingrese un monto para conversion: ")
#PROCESO DE DATOS
opcion=""
while(opcion ==""):
    print ("Opcion 1 - Soles a Dolares")
    print ("Opcion 2 - Dolares a Soles")
    print ("Opcion 3 - Soles a Euros")
    print ("Opcion 3 - Euros a Soles")
    opcion=input("Eliga una opcion: ")
    if(opcion =="1"):
        montoDolares = float(monto) / 3.80
        montoDolaresFormato = "${:,.2f}".format(montoDolares)
        print ("El monto en dolares es: " + str(montoDolaresFormato))
    elif(opcion=="2"):
        montoSoles = float(monto)* 3.80
        montoSolesFormato = "S/.{:,.2f}".format(montoSoles)
        print ("El monto en dolares es: " + str(montoSolesFormato))
    elif(opcion=="3"):
        montoEuros = float(monto) / 4.06 
        montoEurosFormato = "${:,.2f}".format(montoEuros)
        print("El monto en euros es: "+ montoEurosFormato)   
    else:
        print("La opcion no es valida-Por favor elija una opcion VALIDA")    
        opcion =""
    #OUTPUTS - SALIDAS