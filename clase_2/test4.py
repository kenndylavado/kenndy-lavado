"""listas python"""
"""requisitos
- Crear dos listas 



"""

lista_1 = []
lista_2 = []

lista_1.extend(["kenndy", 18, "estudiante"])
lista_2.extend(["javier", 20, "carpintero"])

suma_de_listas = lista_1 + lista_2
print("la suma de la lista es {}".format(suma_de_listas))
suma_de_listas.reverse()


print("la lista invertida es: {}".format(suma_de_listas))
suma_de_listas.pop(1)
suma_de_listas.pop(3)

print("la lista actualizada es: {}".format(suma_de_listas))
