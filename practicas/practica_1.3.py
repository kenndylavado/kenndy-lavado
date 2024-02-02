
a = input("Ingresar su nombre: ")
b = input("Ingresar su apellido: ")
c = int(input("Ingresar su edad: "))
d = int(input("Ingresar su DNI: "))

dic = {'nombre':a,'apellido':b,'edad':c,'dni':d}
print(dic["nombre"],dic["apellido"],dic["edad"],dic["dni"])


dic["profesiones"] = "profesor"

del dic["dni"]
print(dic)