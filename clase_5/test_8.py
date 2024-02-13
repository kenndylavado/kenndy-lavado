"""
requisitos
- Crea una clase alumno
- crea un metodo que indicara si el alumno esta aprobado o no de acuerdo a su promedio
- tendra 3 notas, la nota inicial sera de 0 para todos
- obtener el nombre y distrito de residencia   
"""


class alumno:
    nacionalidad = "peruano"
    
    def __init__(self, nota_1, nota_2, nota_3, nacionalidad="peruano",nombre):
        self.nota1= nota_1
        self.nota2= nota_2
        self.nota3= nota_3
        self.nacionalidad = nacionalidad
    
    def promedio(Self):
        promeddio_1 = Self.nota1 + Self.nota2 + Self.nota3 //3
        if promeddio_1 >= 11:
            print("estado aprobado")
        else:
            print("desaprobado")
        Self.promedio_1 = promeddio_1

alumno_1 = alumno(0,15,11, "peruano","kenndy")        

print("el promedio del alumno 1 es: {}".format(alumno_1.promedio_1))