"""uso del flujo condicional if """
estado = 0
"""aplicando la forma ternaria"""

if estado==1:
    print("1, Su estado final es terminado")
else:
    print("2, su estado final es no terminado")
final = "1. Su estado final es terminado" if estado == 1 else "2. Su estado es no terminado"
print(final) 