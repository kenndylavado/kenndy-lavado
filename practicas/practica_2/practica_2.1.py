from datetime import datetime

class Persona():
    def __init__(self, nombre, edad, saldo, nacionalidad="peruana"):
        
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad
        
        
    def solicitar_datos(self):
        try:
            self.nombre = input("Escriba su nombre: ")
            self.edad = int(input("Escriba su edad: "))
            self.saldo = int(input("ingrese su saldo: "))
        except ValueError:
            print("Error: ingrese un valor valido. ")
    def cumpleaños(self):
        self.edad += 1    
        
    def Fecha(self):
        fecha_actual = datetime.now()
        
        fecha_hora_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M")
        
        return fecha_hora_formateada
    def transferencia(self, otra_persona, cantidad):
        try:
            cantidad = float(cantidad)
            
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor que cero.")
                return
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                otra_persona.saldo += cantidad
                print("Transferencia exitosa. Saldo actual: {}".format(self.saldo))
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Error: Ingrese un valor válido para la cantidad.")
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


    
persona_1 = Persona("", 0, 0)
persona_2 = Persona("",0,0)
fecha_registro = persona_1.Fecha()
fecha_registro2 = persona_2.Fecha()


persona_1.solicitar_datos()
persona_2.solicitar_datos()



print("-------------------------------------------------------------------------")
print("Nombre de la primera persona: {}".format(persona_1.nombre))
print("Edad de la primera persona: {}".format(persona_1.edad))
print("Saldo de la primera persona: {}".format(persona_1.saldo))
print("Nacionalidad de la primera persona: {}".format(persona_1.nacionalidad))
print("La fecha, hora y minuto en que se registro es: {}".format(fecha_registro))
print("-------------------------------------------------------------------------")
print("Nombre de la segunda persona: {}".format(persona_2.nombre))
print("Edad de la segunda persona: {}".format(persona_2.edad))
print("Saldo de la segunda persona: {}".format(persona_2.saldo))
print("Nacionalidad de la segunda persona: {}".format(persona_2.nacionalidad))
print("La fecha, hora y minuto en que se registro es: {}".format(fecha_registro2))
print("-------------------------------------------------------------------------")
persona_1.cumpleaños()
persona_1.cumpleaños()
persona_2.cumpleaños()
persona_2.cumpleaños()

print("edad actualizada de la primera persona es {} años".format(persona_1.edad))
print("edad actualizada de la segunda persona es {} años".format(persona_2.edad))
print("-------------------------------------------------------------------------")

cantidad_a_transferir = input("Ingrese la cantidad a transferir de persona 1 a persona 2: ")
persona_1.transferencia(persona_2, cantidad_a_transferir)
print("-------------------------------------------------------------------------")
persona_1.mostrar_saldo()
persona_2.mostrar_saldo()
