
lista = []

def separacion(x):
    suma_de_digitos = 0
    while x > 0:
        lista.append(x%10)
        x = x//10
    
    for i in lista:
        suma_de_digitos += i        
    print(suma_de_digitos)
numero = int(input("ingrese un numero: "))
separacion(numero)

