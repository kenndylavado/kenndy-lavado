def lista():
    
    listas = []
    b = int(input("ingrese el tamaño de su lista: "))
    for i in range(b):
        a = int(input("ingrese valores para su lista: "))
        listas.append(a)
    return listas
def buscar_por_indice(lista):
    while True:
        try:
            buscar = int(input("ingrese el indice del numero a encontrar: "))
            if buscar == -1:
                break
            datos = lista[buscar]
            print("el valor del indice {} es: {}".format(buscar, datos))
        except IndexError:
            print("No se a encontrado valor al indice ingresado, ingrese otro valor")
    

crear_lista = lista()
buscar_por_indice(crear_lista)