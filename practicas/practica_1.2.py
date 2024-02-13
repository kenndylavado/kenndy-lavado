import random

lista1 = []
for i in range(10):
    numero = random.randint(1,50)
    lista1.append(numero)
lista2=[]
for a in lista1:
    a = a**3
    lista2.append(a)
print(lista2)
        
lista3=[]
for b in lista1:
    b = b**2
    lista3.append(b)
print(lista3)

suma = lista2 + lista3
print("la suma de las 2 listas es: {}".format(suma))
