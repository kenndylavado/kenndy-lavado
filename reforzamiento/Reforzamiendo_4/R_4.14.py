def decorador(func):
    
    def wrapper(*args, **kwargs ):
        print("La cantidad de argumentos que tiene la función es")
        resultado = func(*args, **kwargs)
        print(len(args))
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper
@decorador
def operacion(var1, var2, var3, var4):
   return "resultado", var1+var2+var3+var4

operacion(4,5,6,7)
