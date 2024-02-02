lista = ["calculo", "calculo 2", "quimica", "introduccion a la mecatronica", "comunicacion","algebra lineal"]

lista.append("calculo 3")
lista.append("termodinamica")
lista.append("filosofia")
lista.append("programacion 1")

lista.remove("filosofia")
lista.remove("calculo 2")
lista.pop(0)
lista.reverse()
print(lista)
print("el tamaño de la lista es: {}".format(len(lista)))
lista.append("calculo 2")
lista.append("calculo 2")
lista.append("calculo 2")
print("se repiten: {}".format(lista.count("calculo 2")))


lista2 =[]

lista2.append(3.25)
lista2.append(2.34)
lista2.append(1.98)

lista2.append(10)
lista2.append(9)
lista2.append(8)

lista2.append("hola")
lista2.append("como")
lista2.append("estas")

lista3 = lista + lista2

print("la suma de las dos listas es: {}".format(lista3))

lista4= [1,5,3,2,6,7,9,8]

lista5 = [2.5, 3.9, True, False, 5.4, 3.5, 99.9]
print("el penultimo y ultimo elemento de la lista 5 son: {} y {} ".format(lista5[5],lista5[6]))

print(type(lista5[0]))
print(type(lista5[1]))
print(type(lista5[2]))
print(type(lista5[3]))
print(type(lista5[4]))
print(type(lista5[5]))
print(type(lista5[6]))
lista5.clear()
print(lista5)
lista4.pop(2)
lista4.pop(3)
print(lista4)
lista6 = [i for i in range(1, 101)]
lista6.pop(11)
lista6.pop(36)
print(lista6)

lista7=[1,2,3,4,5,6,7,8,9,10]
lista8=[]
for a in lista7:
    a = a**2
    
    lista8.append(a)
    
print(lista8)

lista9 = [v for v in range(1, 31, 2)]
print(lista9)