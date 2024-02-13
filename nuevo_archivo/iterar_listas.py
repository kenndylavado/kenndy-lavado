animales = ["gato", "loro", "perro", "cocodrilo"]
numeros = [1 , 3, 5, 4, 10 ,12 ]
for animal in animales:
    print("ahora la variable animal es: {}".format(animal))
    
    
for numero in numeros:
    resultado = numero* 2
    print("el producto del numero es: {}".format(resultado))
    


for numero, animal in zip(animales,numeros):
    print(f'recorrido de lista 1:{numero}')
    print(f'recorrido de lista 2:{animal}')
    
    
    
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el inidice es {indice} y el valor es {valor}')
    
    
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("el bucle finalizo")    