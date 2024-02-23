import random


def numeros_random():
    lista = []
    for i in range(30):
        numeros_aleatorios = random.randint(0, 100)
        lista.append(numeros_aleatorios)
    return lista


def ordenar_lista(lista):
    Lista_ordenada = sorted(lista)
    print("lista original: ", lista)
    print("lista ordenada: ", Lista_ordenada)