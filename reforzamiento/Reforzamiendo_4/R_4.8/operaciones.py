import math

def valor(numero):
    while True:    
        try:
            numero = int(input("ingrese un valor: "))
            return numero
        except ValueError:
            print("ingrese un valor entero.")
            
def raiz(numero):
    raiz_de_numero = math.sqrt(numero)
    print (f"La raiz cuadradad de {numero} es: {raiz_de_numero}")

def cuadradoycubo(numero):
    cuadrado = pow(numero,2)
    cubo = pow(numero,3)
    print(f"El cuadrado de {numero} es: {cuadrado} ")
    print(f"El cubo de {numero} es {cubo}")