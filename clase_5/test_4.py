"""poo: programacion orientada a objetos"""

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

print("el color del primer carro es: {}".format(carro_1.color))
print("la aceleracion de mi primer carro es: {}".format(carro_1.aceleracion))
print("la cantidad de ruedas de nuestro carro es: {}".format(carro_1.ruedas))
print("---------------------------------------------------------------------------------------------------------")

carro_2 = carro("azul", 60)
print("el color del primer carro es: {}".format(carro_2.color))
print("la aceleracion de mi primer carro es: {}".format(carro_2.aceleracion))
print("la cantidad de ruedas de nuestro carro es: {}".format(carro_2.ruedas))

