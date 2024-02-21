from modulo import usuario


nom_usuario = input("ingrese su nombre  de usuario: ")
if usuario(nom_usuario) == True:
    print("El {} cumple.".format(nom_usuario))
else:
    print(usuario(nom_usuario))

