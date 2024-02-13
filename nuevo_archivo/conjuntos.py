#creando un conjunto con set
conjunto = set(["dato1",("si deja las tuplas"),"dato2"])

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset[("dato1", "dato1")]
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)
#teoria de conjuntos

#verificando si es un subconjunto
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}
resultado = conjunto3.issubset(conjunto4)
resultado2 = conjunto4 <= conjunto3
print("resultado 1: {} y resultado 2: {}".format(resultado,resultado2))

#verificando si es un superconjunto
resultado3 = conjunto3.issuperset(conjunto4)
resultado4 = conjunto4 > conjunto3
print("resultado 3: {} y resultado 4: {}".format(resultado3,resultado4))
#verificar si hay resultados en comun
resultado5 = conjunto3.isdisjoint(conjunto4)

print(resultado5)




