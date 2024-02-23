def cargar_numero():
    try:
        numero = int(input("Ingrese un valor: "))
        return numero
    except ValueError:
        print("Debes ingresar un numero entero.")
        return None
def suma(a, b):
    try:
        return a + b
    except ValueError:
        print("ingrese un numero natural.")



