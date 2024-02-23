import random


def numero_random():
    lista_aleatoria = random.sample(range(0, 101), 10)
    print(f"La lista de numeros aleatorios es: {lista_aleatoria}")
    return lista_aleatoria


def numeros_no_repetidos(lista):
    no_repetidos = list(set(lista))
    print(f"Numeros no repetidos: {no_repetidos}")
    return lista


def ordenar(numeros_no_repetidos):
    lista_mayor_menor = sorted(numeros_no_repetidos, reverse=True)
    lista_menor_mayor = sorted(numeros_no_repetidos)
    print("Lista ordenada de mayor a menor: ", lista_mayor_menor)
    print("Lista ordenada de menor a mayor: ", lista_menor_mayor)
    return lista_mayor_menor, lista_menor_mayor


def mayor_par(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    if numeros_pares:
        par_mayor = max(numeros_pares)
        print(f"El mayor numero par es: {par_mayor}")
        return par_mayor
    else:
        print("No hay pares en la lista.")
        return False


numeros_random = numero_random()
lista_de_no_repetidos = numeros_no_repetidos(numeros_random)
listas_ordenadas = ordenar(lista_de_no_repetidos)
numero_mayor_par = mayor_par(lista_de_no_repetidos)
