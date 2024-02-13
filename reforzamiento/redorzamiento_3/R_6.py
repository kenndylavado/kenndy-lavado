class operaciones():
    
    def __init__(self,variable,resultado_1, resultado_2):
        self.resultado = resultado_1
        self.variable  = variable
        self.resultado2 = resultado_2
    
    def soliciar_numero(self):
        self.variable =int(input("ingresar un nummero"))

    def cubo(self):
        self.resultado = self.variable**3
        return
    def cuadrado(self):
        self.resultado = self.variable**3
        self.resultado2 = self.resultado**2

usuario = operaciones(variable=0, resultado_1=0, resultado_2=0)
usuario.soliciar_numero()
usuario.cubo()
usuario.cuadrado()
print("Número ingresado:", usuario.variable)
print("Cubo del número:", usuario.resultado)
print("Cuadrado del cubo:", usuario.resultado2)
