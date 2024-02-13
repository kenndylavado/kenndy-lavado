#-------- Ejercicio 1 -----------

def suma(a):
    
    sumatoria = 0 
    for i in str(a):
        sumatoria += int(i)
    return sumatoria
    
a = int(input("escriba un numero positivo: "))
def suma2(b):
    sumatoria_2 = 0
    for e in str(b):
        sumatoria_2 += int(e)
    return sumatoria_2
b = int(input("escriba un numero positivo: "))
if suma(a) > suma2(b):
    print("la suma de digitos del primer numero ingresado es mayor que la del segundo ")
elif suma(a) < suma2(b):
    print("la suma de digitos del segundo numero ingresado es mayor que la del primero ")

if suma(a) < 10 and suma2(b)<10:
    print("la sumarotia de los digitos de ambos numeros es menor que 10")
elif suma2(b) < 10:
    print("la sumarotia de los digitos del segundos numero es menor que 10")    
elif suma(a) < 10:
    print("la sumarotia de los digitos del primer numero es menor que 10")