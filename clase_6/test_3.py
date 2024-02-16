




def operaciones(a, b):
    try:
        resultado = a+b
        resultado2 = a/b
    except TypeError:
        print("no se pude sumar dos tipos de datos diferentes")
    except ZeroDivisionError:
        print("no se pude dividir entre 0")
    else:
        print(resultado)
        print(resultado2)
operaciones(40, "hola")
operaciones(1000, 500)
operaciones(500, 0)