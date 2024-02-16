
def datos():
    a = input("escriba su nombre: ")
    print("hola {}".format(a))
    return a 

def impuesto(x):
    x = int(input("ingrese su sueldo: "))
    if x > 5000:
        impuesto = x * 0.18
        print("El impuesto es del 18%, lo cual es: {}".format(impuesto))
    else:
        print("El sueldo tiene que superar los 5000")
    return