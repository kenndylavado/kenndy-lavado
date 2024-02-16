diccionario = {
    "nombre": "kenndy",
    "apellido": "lavado",
    "edad": "18"
}
#recorriendo diccionariso para obtener key y value

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es {value}')
    