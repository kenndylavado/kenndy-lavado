
file_w = open("C:\\Users\\kenndy\\Desktop\\python\\clases_uni\\reforzamiento\\Reforzamiendo_4\\R_4.11\\calificaciones.txt", "w")
file_r = open("C:\\Users\\kenndy\\Desktop\\python\\clases_uni\\reforzamiento\\Reforzamiendo_4\\R_4.11\\calificaciones.txt", "r")


def alumno(nombre, nota_1, nota_2):
    nombre = input("Ingrese el nombre completo del alumno: ")
    nota_1 = int(input("Ingrese la nota 1: "))
    nota_2 = int(input("Ingrese la nota 2: "))
    promedio = (nota_1 + nota_2)/2
    file_w.write(f"{nombre},{nota_1},{nota_2},{promedio}")
    file_w.close()
    
    
def promocion():
    usuario = file_r.read()
    file_r.close()
    datos = usuario.split(",")
    if float(datos[3]) >= 10.5:
        print(f"Alumno {datos[0]}, aprobado")
    else:
        print(f"Alumno {datos[0]}, desaprobado")


alumno("", 0, 0)
promocion()