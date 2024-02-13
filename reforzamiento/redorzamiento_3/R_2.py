
lista=[]
def numeros(a, b):
    if a > b:
        a, b = a, b
        
    for i in range(a, b + 1 ):
        cuadrado = i**2
        lista.append(cuadrado)
    return

numero_1= int(input("escriba su primer numero: "))
numero_2 = int(input("escriba su segundo numero: "))

numeros(numero_1, numero_2)
print("los numeros al cuadrado entre {} y {} son: {} ".format(numero_1, numero_2, lista))