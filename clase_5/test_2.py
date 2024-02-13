


def maxima(a,b,c,d):
    
    a = int(input("escriba el primer numero: "))
    b = int(input("escriba el segundo numero: "))
    c = int(input("escriba el tercero numero: "))
    d = int(input("escriba el cuarto numero: "))

    
    if a > b and a>c and a > d:
        resultado = a**3
        print("el primer numero es el mayor de todos y su cubo es: {}".format(resultado))
    elif b > a and b > c and b > d:
        resultado2 = b**3
        print("el segundo numero es el mayor de todos y su cubo es: {}".format(resultado2))
    elif c > a and c > b and c > d:
        resultado3 = c**3
        print("el tercer numero es el mayor de todos y su cubo es: {}".format(resultado3))
    elif d > a and d > b and d > c:
        resultado4 = d**3
        print("el cuarto numero es el mayor de todos y su cubo es: {}".format(resultado4))
    return maxima