import json


data_python = {'nombre': 'Milagros', 'edad': 28, 'distrito': 'jesus Maria', 'promedio': 16.5}

data_python_to_json = json.dumps(data_python)

print(data_python_to_json)
print(type(data_python_to_json))