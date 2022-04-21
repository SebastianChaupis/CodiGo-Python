class Automovil:
    #atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa =pl
        self.color = col
        self.marca = mar
    
    def encender (self):
        print("Encender " + self.marca)        
    
    def avanzar (self):
        print("Anvanzar " + self.marca)        
    
    def acelerar (self):
        print("Acelerar " + self.marca)        
    
    def frenar (self):
        print("Frenar " + self.marca)
        
vw = Automovil(1970,'102020','rojo','Volkwagen')
vw.encender()