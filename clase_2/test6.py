"""diccionarios de python"""
"""del: eliminar valores del dicc """

var_1 = {"nombre": "margarita", "edad": 27, "promedio": 15}
"""para eliminar valores de nuestro diccionario usamos "del" delante de la variable"""

del var_1["edad"]

print("el diccionario actualizado es: {}".format(var_1))