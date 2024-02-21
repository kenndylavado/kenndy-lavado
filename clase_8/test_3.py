""" decoradores en python"""



def funcionA(funcionB):
    
    
    def funcionC():
        print("1: antes de ejecutar la funcion a decorar")
        funcionB()
        print("2: Despues de ejecutar la funcion a decorar")
    return funcionC

@funcionA
def saludo():
    print("hola a todos")
saludo()