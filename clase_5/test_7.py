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
"""Aplicamos herencia"""


class carrovolador(carro):
    
    ruedas = 6
    
    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion)
        
        self.estadovolando = estado_volando
    def vuela(self):
        self.estadovolando= True
    def aterriza(self):
        self.estadovolando = False
carro_1 = carro("rojo", 45)
carro_volador = carrovolador("blanco", 55)

print("el color de el carro volador es: {}".format(carro_volador.color))
print("el estado inicial del carro volador es: {}".format(carro_volador.estadovolando))

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()
print("el estado actual del carro volador es: {}".format(carro_volador.estadovolando))
print("La velocidad de mi carro volador es: {}".format(carro_volador.velocidad))

    
    
    
    