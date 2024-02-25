import requests as rq

data = rq.get("https://jsonplaceholder.typicode.com/users").json()

for i in range(0, len(data)):
    if 'age' not in data[i]:
        data[i]['age'] = "N.A."
    print(f"Bienvenido {data[i]['name']}, usted tiene {data[i]['age']} años. El correo que "+ 
        f"nos proporcionó es {data[i]['email']} y la compañía actual donde \n"+
        f"trabaja se llama {data[i]['company']['name']}. Dentro de sus datos "+
        f"también encontramos una website que es: {data[i]['website']}")

nuevo_usuario = {"id": len(data)+1,
    "name": "juan perez",
    "age":20,
    "email": "juanzito@april.biz",
    "website": "hildegard.org",
    "company": {
      "name": "compañia nueva alianza"
    }}
data.append(nuevo_usuario)
print("\n\ndata")
print(len(data))
print("\n\n")
for i in range(0, len(data)):
    if 'age' not in data[i]:
        data[i]['age'] = "N.A."
    print(f"Bienvenido {data[i]['name']}, usted tiene {data[i]['age']} años. El correo que "+ 
        f"nos proporcionó es {data[i]['email']} y la compañía actual donde \n"+
        f"trabaja se llama {data[i]['company']['name']}. Dentro de sus datos "+
        f"también encontramos una website que es: {data[i]['website']}")
