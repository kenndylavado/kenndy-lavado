
file = open("C:\\Users\\kenndy\\Desktop\\python\\clases_uni\\reforzamiento\\Reforzamiendo_4\\R_4.9\\tabla.txt", "w")

def numero():
    while True:   
        valor = int(input("ingrese un valor entre 1 y 20: "))
        if valor < 1 or valor >20:
            print("Solo valores entre el 1 y el 20")
        else:
            break
    return valor    
def tabla_de_multiplicar(valor):
    file.write(f"Tabla del {valor}\n")
    for i in range(1,11):
        resultado = valor * i
        file.write(f"{valor}x{i} = {resultado}\n")

valor_1 =numero()
tabla_de_multiplicar(valor_1)