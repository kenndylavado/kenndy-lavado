import requests

# Hacer una solicitud GET a una API (en este caso, la API JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:
    # Imprimir el contenido de la respuesta en formato JSON
    data = response.json()
    print("Datos de la API:", data)
else:
    print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")
