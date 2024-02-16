"""manejo de errores"""



def operacion(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError and TypeError:
        print("solo se puede ingresar numero naturales")
    else:
        print(resultado)
a = input("ingrese un dato:")
b = input("ingrese otro dato: ")
operacion(a, b)
