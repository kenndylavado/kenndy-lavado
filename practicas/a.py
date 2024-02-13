
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dni = input("Ingrese su DNI: ")

diccionarioPersona = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'dni': dni}

# Mostrar en pantalla sólo los values del diccionario

valuesDic = diccionarioPersona.values()
print("Los valores de mi diccionario actual son: {}".format(valuesDic))

# Agregando un nuevo key a mi diccionario

diccionarioPersona['profesion'] = input("Ingrese su profesión: ")

# Eliminando el key dni

del diccionarioPersona['dni']

# Mostrando mi diccionario actualizado

print("Mi diccionario actualizado es: {}".format(diccionarioPersona))