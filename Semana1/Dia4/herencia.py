class Persona:
    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema
        
    def mostrar(self):
        print("Nombre " + self.nombre + "Email " + self.email)


class Alumno(Persona):
    pass


class Profesor(Persona):
    def __init__(self, nom, ema, mod):
        super().__init__(nom,ema)
        self.modulo = mod
    def mostrar(self):
        super().mostrar()
        print("Dicta el modulo de: "+ self.modulo)
    

alu1 =Alumno('Sebastian','sebaschaupis1@gmail.com')
alu1.mostrar()

prof1= Profesor('Cesar','cesar@gmail.com','Backend')
prof1.mostrar()