""" manejo de errores"""
"""tipos de errores"""
"""
TypeError
ZeroDivisionerror
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""


"""extructura y usos"""
#try:
#    bloque de codigo
#except'exepcion 1':
#    bloque de codigo2
#else:
#    bloque de codigo3 

def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
    else:
        print(resultado)
        
division(40,0)
division(1000, 25)