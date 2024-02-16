import json

json_data = '{"nombre": "python", "tipo": "backend", "paradigma": "POO"}'
json_to_python = json.loads(json_data)

print("nuestro dato tipo json a python {}".format(json_to_python))
print("El tipo de dato de nuestra variable es: {}".format(type(json_to_python)))