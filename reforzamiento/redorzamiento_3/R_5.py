
def parametros(a, b, lista):
    print("Lista original:", lista)

    try:
        lista.remove(b)
        print("Número eliminado:", b)
    except ValueError:
        print("El número {} no está en la lista.".format(b))

    print("Lista actualizada:", lista)

# Solicitar valores al usuario
a = (input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor a eliminar: "))
lista_usuario = list(map(int, input("Ingrese la lista separada por espacios: ").split()))
parametros(a,b,lista_usuario)
