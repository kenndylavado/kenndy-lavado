import random
import math


def crear_nuevo_archivo():
    with open("notas.txt", "w"):
        pass
    print("Archivo notas.txt creado exitosamente")


def listas(archivo, tamaño_lista):
    with open(archivo, "a") as file:
        file.write("Numeros random\n")
        lista_numeros = [random.randint(0, 100) for _ in range(tamaño_lista)]
        for numero in lista_numeros:
            file.write(f"{numero}\n")
        return lista_numeros


def raiz(archivo, lista_numeros):
    with open(archivo, "a") as file:
        file.write("Raices de los numeros\n")
        for numero in lista_numeros:
            resultado = math.sqrt(numero)
            file.write(f"{resultado}\n")
