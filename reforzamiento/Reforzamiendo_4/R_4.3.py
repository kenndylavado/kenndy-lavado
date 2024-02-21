def buscar_en_dic(diccionario):
    while True:
        try:
            clave = input("ingrese la clave a extraer: ")
            return diccionario[clave]
        except KeyError:
            print("el valor ingresado no se ah encontro")

diccionario = {'Nombre': 'Xavier', 'Apellidos': 'Rodriguez', 'DNI':63325345}

resultado =buscar_en_dic(diccionario) 
print(resultado)