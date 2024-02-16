

def Ingresar_datos(): 
    dato_1 = int(input("ingresar un dato: "))
    dato_2 = int(input("ingresar otro dato: "))

    return dato_1, dato_2
def dividir_datos(dato_1, dato_2):
    try:
        resultado = dato_1/dato_2
    except ZeroDivisionError:
        print("No se puede dividir entre 0, digite otro numero")
    return resultado
def suma_datos(dato_1, dato_2):
    try:
        resultado = dato_1 + dato_2
    except TypeError:
        print("ingrese el tipo de dato correcto, solo numeros.")
    return resultado
def Ingresar_datos_lista():
    lista = []
    n = int(input("ingrese la cantidad de datos para la lista: "))
    for i in range(n):
        datos = input("ingrese los datos para su lista {}".format(i+1))
    lista.append(datos)
    return lista
def buscar_indice(lista):
    try:
        buscar_por_indice = int(input("ingrese el valor del indice que busca: "))
        dato = lista[buscar_por_indice]
        print("El dato en el índice {} es: {}".format(buscar_por_indice,dato))
    except IndexError:
        print("El índice ingresado no se encuentra en la lista.")
datos_ingresados = Ingresar_datos()
dato_1, dato_2 = datos_ingresados
resultado_suma = suma_datos(dato_1,dato_2)

resultado_division = dividir_datos(dato_1, dato_2)
print("Resultado de la división:", resultado_division)


datos_ingresados = Ingresar_datos_lista()
print("datos ingresados", datos_ingresados)
buscar_indice(datos_ingresados)

