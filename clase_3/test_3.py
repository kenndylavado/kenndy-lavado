"""
requizitos 
-Dentro de una empreza se va a solicitar pedir nombre y apellido de emplado.
-distrito de recidencia
-Sueldo y calculo del bono final del año, que sera el tripe del sueldo mensual menos el 10 porciento
-todos los datos ingresaran a una lista
-por asignacion multiple asignar los valores de esta lista a tres nuevas variables 
-Mostrar por la terminal el mensaje "nombres" "apellido" "recibira "bono"soles de bono fin de año.
"""
nombre = input("escriba su nombre: ")
apellidos = input("escriba su apellido: ")
distrito = input("escriba su distrito: ")
sueldo = int(input("escriba su sueldo: "))
bono = 3*sueldo - sueldo*0.1

lista=[]
lista.append(nombre)
lista.append(apellidos)
lista.append(distrito)
lista.append(sueldo)
lista.append(bono)

a , b , c , d, e = lista
print("{}{} recibira {} soles de bono a fin de año".format(a, b, e))
