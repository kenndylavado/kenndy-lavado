file = open("C:/Users/kenndy/Desktop/python/clases_uni/reforzamiento/Reforzamiendo_4/R_4.10/agenda.txt", "a")


def ingresar_usuario(nombre, apellido, edad):
    nombre = input("Escriba su nombre: ")
    apellido = input("Escriba su apellido: ")
    edad = int(input("Escriba su edad: "))
    file.write(f"{nombre}, {apellido}, {edad}\n")
ingresar_usuario("","",0)