


lista=[]

for i in range(2):
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    lista.append(nombre)
    lista.append(edad)

suma = lista[1] + lista[3]

print(lista)
print("la suma de las edades es: {}".format(suma))
print("los tipos de datos son: {} y {}".format(type(nombre),type(edad)))



