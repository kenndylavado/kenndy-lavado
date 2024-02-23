import funciones

funciones.crear_nuevo_archivo()
numeros = funciones.listas("notas.txt",
                           int(input("Ingrese el tamaño de la lista: ")))
funciones.raiz("notas.txt", numeros)
