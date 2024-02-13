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
carro_1 = carro("negro", 50)
print("El color del primer carro es: {}".format(carro_1.color))
carro_2 = carro("rojo",80)
carro_2.marchas = 30000
print("el numero de marchas del carro dos es {} y su color es {}".format(carro_2.marchas, carro_2.color))