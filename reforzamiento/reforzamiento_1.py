#1)
print("----------------------------------1-----------------------------------------")
mi_nombre = "kenndy lavado"

mi_saludo = f'¡HI {mi_nombre}!'

print(mi_saludo)

#-------------------------------------------------------------------------------------------------------------------------
#2)
print("----------------------------------2-----------------------------------------")
numero = int(10)

operacion_1 = numero * 10
operacion_2 = numero - 10
print("el resultado de la operacion 1 es: {}".format(operacion_1))
print("el resultado de la operacion 2 es: {}".format(operacion_2))

#3)
print("----------------------------------3-----------------------------------------")
var_1 = "123"

var_2 = 1
suma = int(var_1) + int(var_2)
print("el resultado de la suma es: {}".format(suma))

#4)
print("----------------------------------4-----------------------------------------")

print("volumen de una esfera: ingrese datos")
r = float(input("ingrese valor del radio: "))

Volumen = 4/3 * 3.1416 * r**3
#''
print(round(Volumen,2))