def conteo(oracion):
    palabras = oracion.split()
    count = 0
    for i in palabras:
        count+=1
        
    if count < 3:
        print("La oración debe tener al menos 3 palabras.")
        oracion = input("Ingrese una oración de nuevo: ")
        conteo(oracion)
    else:
        print("La oración tiene {} palabras.".format(count))

oracion = input("Ingrese una oracion: ")
conteo(oracion)