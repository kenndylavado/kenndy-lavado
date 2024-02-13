class carro:
    """atributos"""
    ruedas = 4
    
    
    """constructor"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0


    """metodos y funciones"""
    def acelerar (self):
        self.velocidad = self.velocidad + self.aceleracion
        
    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad=0
"""instanciamos nuestra clase"""
carro_1 = carro("negro", 70)

print("la velocidad inicial del carro 1 es {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()

print("la velocidad actual del carro es {}".format(carro_1.velocidad))

carro_1.frena()
carro_1.frena()
print("la velocidad actual del carro es {}".format(carro_1.velocidad))