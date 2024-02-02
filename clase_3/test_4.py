""" Uso del flujo condicional"""


edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
elif -1>= edad <=100:
    print("ingrese otra edad ")
else:
    print("Usted es menor de edad")
    
#-------------------------------------------------------------------------
var_1 = int(input("ingrese un numero: "))
var_2 = int(input("ingrese un numero: "))

if var_1 > var_2:
    print("el valor de la variable 1 es mayor que la variable 2")
elif var_1 == var_2:
    print("los valores son iguales")
else:
    print("el valor de la variable 1 es  menor que la variable 2")
    
#---------------------------------------------------------------------------------------------------------

a, b, c = 60,  100.10,"python"

if a == 50 and b >40.0 or c == "python":
    print("ingrese la primera condicional triple")
else:
    print("ingrese else") 