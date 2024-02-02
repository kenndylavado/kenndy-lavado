nombre = input("ingrese tu nombre: ")
apellido = input("ingrese tu apellido: ")

completo = nombre + " " + apellido


print("su nombre completo es: {}".format(completo.upper()))
print("el tamaño de su nombre completo es: {}".format(len(completo)))

if len(nombre) < len(apellido):
    print("su apellido es mas grande que su nombre")
else:
    print("su nombre es mas grande que su apellido")