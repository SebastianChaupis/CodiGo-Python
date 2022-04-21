class Usuario:
        
    def __init__(self,nom,pwd):
        self.nombre = nom
        self.password = pwd
        
    def iniciarSesion(self):
        if (self.nombre == 'admin' and self.password == '12345'):
            print("Bienvenido: "+ self.nombre)
        else:
            print ("Datos incorrecto")
    
usuarios1 = Usuario('admin','admin')
usuarios1.iniciarSesion()

usuarios2 = Usuario("admin","12345")
usuarios2.iniciarSesion()
print(usuarios2.nombre, usuarios2.password)