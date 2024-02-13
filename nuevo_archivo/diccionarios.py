#creando diccionarios con dict()
diccionario = dict(nombre="kenndy", apellido="Lavado")

#las listas no pueden ser keys porque son mutables y usamos frozenset para agregar conjuntos

#creamos diccionarios con fromkeys()

diccionario2 = dict.fromkeys("ABCD")


print(diccionario2)