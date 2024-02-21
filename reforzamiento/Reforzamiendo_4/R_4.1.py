def suma(a, b):

        try:
            resultado = a + b
            print("el resultado de la suma es: {}".format(resultado)) 
        except TypeError:
            print("Se a ingresado un string, ingrese un valor numerico")
suma(80,"hola como estas")
