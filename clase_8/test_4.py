""" decoradores en python"""



def funcionA(funcionB):
    
    
    def funcionC(*args):
        print("1: antes de ejecutar la funcion a decorar")
        resultado = funcionB(*args)
        print("2: Despues de ejecutar la funcion a decorar")
        return resultado
    return funcionC

@funcionA
def saludo(nombre, apellido, edad):
    
    print("hola {} {}, usted tiene {} años".format(nombre,apellido,edad))


nombre = input("escriba su nombre: ")
apellido= input("escriba su apellido: ")
edad = input("escriba su edad: ")