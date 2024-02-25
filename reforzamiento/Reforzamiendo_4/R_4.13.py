def decorador(func):
    
    def wrapper(*args, **kwargs ):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutado correctamente")
        return resultado
    return wrapper
@decorador
def operacion(var1, var2, var3, var4):
    print("resultado", var1*var2*var3*var4)

operacion(4,5,6,7)
