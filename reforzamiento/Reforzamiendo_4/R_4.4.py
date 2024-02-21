def suma(a, b):
    try:
        return a + b
    except (TypeError,ZeroDivisionError):
        print("Datos ingresados erroneos, ingrese numeros naturales")  
suma("hola como estas", 0)