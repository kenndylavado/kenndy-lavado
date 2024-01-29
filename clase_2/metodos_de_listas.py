#creamos una lista con list[]
lista = list(["hola",56,18])
#cuenta el numero de elementos de una lista 
resultado = len(lista)

#agregando elementos a una lista con append
lista.append("ajajjajaja")
#agregando un elemento a la lista en un indice especifico
lista.insert(2,"papaya")
#agregando varios elementos a la lista
lista.extend([False,2019 ])

#eliminando un elemneto de la lista por su indice, si ponemos -1 comenzara desde el ultimo elemento 
lista.pop(1)

#removiendo un elemento de la lista por su valor 
lista.remove("hola")

#para ordenar los elementos de la lista 
#reversed = True nos lo ordena de forma decendente
lista.sort(reversed = True)
    
#invierte la lista 
lista.reverse()

#eliminando todos los elementos de toda la lista 
lista.clear()



print(lista)
